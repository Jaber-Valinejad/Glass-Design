"""Simple local web UI for running glass-system design reviews.

Usage:
    python -m glass_review.app
"""
import threading
import uuid
from datetime import datetime
from pathlib import Path

from flask import Flask, jsonify, render_template, request, send_from_directory

from . import config, gemini_client
from .review import review_pdf
from .vector_store import LocalVectorStore

UPLOAD_DIR = config.UPLOAD_DIR
TEST_DIR = config.ROOT_DIR / "test"

app = Flask(__name__, template_folder="templates")
app.config["MAX_CONTENT_LENGTH"] = 80 * 1024 * 1024

_lock = threading.Lock()
_job = {
    "id": None,
    "status": "idle",
    "filename": None,
    "started_at": None,
    "finished_at": None,
    "page": 0,
    "total": 0,
    "logs": [],
    "report": None,
    "report_name": None,
    "error": None,
}


def _reset_job():
    _job.update(
        {
            "id": None,
            "status": "idle",
            "filename": None,
            "started_at": None,
            "finished_at": None,
            "page": 0,
            "total": 0,
            "logs": [],
            "report": None,
            "report_name": None,
            "error": None,
        }
    )


def _append_log(event: dict):
    entry = {
        "ts": datetime.now().strftime("%H:%M:%S"),
        "level": event.get("level", "info"),
        "message": event.get("message", ""),
        "step": event.get("step"),
        "page": event.get("page"),
        "total": event.get("total"),
    }
    _job["logs"].append(entry)
    if event.get("page") is not None:
        _job["page"] = event["page"]
    if event.get("total") is not None:
        _job["total"] = event["total"]


def _safe_pdf_name(name: str) -> str:
    cleaned = Path(name).name.replace("\x00", "").strip()
    if not cleaned.lower().endswith(".pdf"):
        raise ValueError("Only PDF files are allowed.")
    return cleaned


def _list_review_pdfs():
    items = []
    for folder, source in ((TEST_DIR, "test"), (UPLOAD_DIR, "upload")):
        if not folder.exists():
            continue
        for path in sorted(folder.glob("*.pdf")):
            items.append(
                {
                    "name": path.name,
                    "source": source,
                    "size_kb": round(path.stat().st_size / 1024),
                }
            )
    return items


def _report_dirs():
    dirs = [config.REVIEW_OUTPUT_DIR, config.COMMITTED_REVIEW_OUTPUT_DIR]
    seen = set()
    unique = []
    for folder in dirs:
        resolved = folder.resolve()
        if resolved in seen:
            continue
        seen.add(resolved)
        unique.append(folder)
    return unique


def _find_report(name: str) -> Path | None:
    safe = Path(name).name
    for folder in _report_dirs():
        path = folder / safe
        if path.exists() and path.suffix.lower() == ".md":
            return path
    return None


def _list_reports():
    reports = []
    seen = set()
    for folder in _report_dirs():
        if not folder.exists():
            continue
        for path in folder.glob("*.md"):
            if path.name in seen:
                continue
            seen.add(path.name)
            reports.append(
                (
                    path.stat().st_mtime,
                    {
                        "name": path.name,
                        "modified": datetime.fromtimestamp(path.stat().st_mtime).strftime("%Y-%m-%d %H:%M"),
                    },
                )
            )
    reports.sort(key=lambda item: item[0], reverse=True)
    return [item[1] for item in reports]


def _run_review(job_id: str, pdf_path: Path, api_key: str | None = None):
    def on_progress(event):
        with _lock:
            if _job["id"] != job_id:
                return
            _append_log(event)

    try:
        on_progress({"message": f"Starting review of {pdf_path.name}...", "step": "start"})
        with gemini_client.using_api_key(api_key):
            report = review_pdf(pdf_path, on_progress=on_progress)
        config.REVIEW_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
        out_path = config.REVIEW_OUTPUT_DIR / f"{pdf_path.stem}_review.md"
        out_path.write_text(report, encoding="utf-8")
        with _lock:
            if _job["id"] != job_id:
                return
            _job["report"] = report
            _job["report_name"] = out_path.name
            _job["status"] = "done"
            _job["finished_at"] = datetime.now().isoformat(timespec="seconds")
            _append_log(
                {
                    "message": f"Review complete. Report saved as {out_path.name}.",
                    "step": "done",
                    "page": _job["total"],
                    "total": _job["total"],
                }
            )
    except Exception as exc:
        with _lock:
            if _job["id"] != job_id:
                return
            _job["status"] = "error"
            _job["error"] = str(exc)
            _job["finished_at"] = datetime.now().isoformat(timespec="seconds")
            _append_log({"message": f"Review failed: {exc}", "level": "error", "step": "error"})


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/api/status")
def status():
    store = LocalVectorStore()
    return jsonify(
        {
            "root": str(config.ROOT_DIR),
            "api_key_set": bool(config.GEMINI_API_KEY),
            "api_key_required": True,
            "baseline_pages": len(store.chunks),
            "baseline_pdfs": len(list(config.BASELINE_PDF_DIR.glob("*.pdf"))) if config.BASELINE_PDF_DIR.exists() else 0,
        }
    )


@app.get("/api/pdfs")
def pdfs():
    return jsonify({"pdfs": _list_review_pdfs(), "reports": _list_reports()})


@app.get("/api/job")
def job():
    with _lock:
        return jsonify(
            {
                "id": _job["id"],
                "status": _job["status"],
                "filename": _job["filename"],
                "started_at": _job["started_at"],
                "finished_at": _job["finished_at"],
                "page": _job["page"],
                "total": _job["total"],
                "logs": list(_job["logs"]),
                "report": _job["report"],
                "report_name": _job["report_name"],
                "error": _job["error"],
            }
        )


@app.get("/api/reports/<path:name>")
def get_report(name):
    path = _find_report(name)
    if path is None:
        return jsonify({"error": "Report not found."}), 404
    return jsonify({"name": path.name, "markdown": path.read_text(encoding="utf-8")})


@app.get("/reports/<path:name>")
def download_report(name):
    path = _find_report(name)
    if path is None:
        return jsonify({"error": "Report not found."}), 404
    return send_from_directory(path.parent, path.name, as_attachment=True)


@app.post("/api/review")
def start_review():
    with _lock:
        if _job["status"] == "running":
            return jsonify({"error": "A review is already running."}), 409

    api_key = (request.form.get("gemini_api_key") or "").strip()
    if not api_key and not config.GEMINI_API_KEY:
        return jsonify(
            {
                "error": "Enter your GEMINI_API_KEY. Each person can create one in Google AI Studio."
            }
        ), 400

    pdf_path = None
    selected = (request.form.get("pdf") or "").strip()
    upload = request.files.get("file")

    try:
        if upload and upload.filename:
            UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
            filename = _safe_pdf_name(upload.filename)
            pdf_path = UPLOAD_DIR / filename
            upload.save(pdf_path)
        elif selected:
            filename = _safe_pdf_name(selected)
            for folder in (TEST_DIR, UPLOAD_DIR):
                candidate = folder / filename
                if candidate.exists():
                    pdf_path = candidate
                    break
            if pdf_path is None:
                return jsonify({"error": f"PDF not found: {filename}"}), 404
        else:
            return jsonify({"error": "Choose a PDF or upload one."}), 400
    except ValueError as exc:
        return jsonify({"error": str(exc)}), 400

    job_id = uuid.uuid4().hex[:8]
    with _lock:
        _reset_job()
        _job["id"] = job_id
        _job["status"] = "running"
        _job["filename"] = pdf_path.name
        _job["started_at"] = datetime.now().isoformat(timespec="seconds")
        _append_log({"message": f"Queued {pdf_path.name}.", "step": "queue"})

    if config.IS_VERCEL:
        # Serverless instances do not keep background threads after the response.
        _run_review(job_id, pdf_path, api_key=api_key)
        with _lock:
            return jsonify(
                {
                    "id": _job["id"],
                    "status": _job["status"],
                    "filename": _job["filename"],
                    "report": _job["report"],
                    "report_name": _job["report_name"],
                    "logs": list(_job["logs"]),
                    "error": _job["error"],
                }
            )

    thread = threading.Thread(
        target=_run_review, args=(job_id, pdf_path, api_key), daemon=True
    )
    thread.start()
    return jsonify({"id": job_id, "status": "running", "filename": pdf_path.name})


def main():
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    config.REVIEW_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Glass review UI: http://127.0.0.1:5050")
    print(f"Project root: {config.ROOT_DIR}")
    app.run(host="127.0.0.1", port=5050, debug=False, threaded=True)


if __name__ == "__main__":
    main()
