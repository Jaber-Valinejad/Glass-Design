"""Review a glass-system design PDF against the indexed baseline standards.

Usage:
    python -m glass_review.review "test/some design.pdf" [--top-k 6] [--out report.md]
"""
import argparse
import sys
from pathlib import Path

from . import config, gemini_client, pdf_utils
from .vector_store import LocalVectorStore


def _emit(on_progress, message, **extra):
    print(message, flush=True)
    if on_progress:
        on_progress({"message": message, **extra})


def review_pdf(pdf_path: Path, top_k: int = config.TOP_K_MATCHES, on_progress=None) -> str:
    _emit(on_progress, "Loading indexed baseline standards...", step="load")
    store = LocalVectorStore()
    if not store.chunks:
        raise RuntimeError(
            "Vector store is empty. Run `python -m glass_review.build_index` first to "
            "index the baseline PDFs in pdfs/."
        )
    _emit(
        on_progress,
        f"Baseline library ready: {len(store.chunks)} pages indexed.",
        step="load",
        total_chunks=len(store.chunks),
    )

    _emit(on_progress, f"Extracting pages from {pdf_path.name}...", step="extract")
    pages = pdf_utils.extract_pages(pdf_path)
    total = len(pages)
    _emit(on_progress, f"Found {total} page(s) to review.", step="extract", page=0, total=total)

    report_sections = [f"# Design Review: {pdf_path.name}\n"]

    for page in pages:
        _emit(
            on_progress,
            f"Page {page.page_num}/{total}: describing the sheet...",
            step="describe",
            page=page.page_num,
            total=total,
        )
        try:
            description = gemini_client.describe_page(page.image_bytes, page.text)
        except Exception as exc:
            print(f"  ! description failed: {exc}", file=sys.stderr)
            _emit(
                on_progress,
                f"Page {page.page_num}/{total}: description failed ({exc}).",
                step="describe",
                page=page.page_num,
                total=total,
                level="error",
            )
            report_sections.append(f"\n## Page {page.page_num}\n\n_Could not analyze this page: {exc}_\n")
            continue

        embed_input = f"SOURCE: {pdf_path.name} page {page.page_num}\n\n{description}\n\nRAW TEXT:\n{page.text}"
        _emit(
            on_progress,
            f"Page {page.page_num}/{total}: matching against baseline standards...",
            step="match",
            page=page.page_num,
            total=total,
        )
        try:
            query_embedding = gemini_client.embed_text(embed_input)
        except Exception as exc:
            print(f"  ! embedding failed: {exc}", file=sys.stderr)
            _emit(
                on_progress,
                f"Page {page.page_num}/{total}: embedding failed ({exc}).",
                step="match",
                page=page.page_num,
                total=total,
                level="error",
            )
            report_sections.append(f"\n## Page {page.page_num}\n\n_Could not embed this page: {exc}_\n")
            continue

        matches = store.search(query_embedding, top_k=top_k)
        top_match = f"{matches[0][0].source_file} p.{matches[0][0].page_num}" if matches else "none"
        _emit(
            on_progress,
            f"Page {page.page_num}/{total}: found {len(matches)} baseline match(es); best is {top_match}.",
            step="match",
            page=page.page_num,
            total=total,
        )

        baseline_context_parts = []
        baseline_images = []
        seen_images = set()
        for chunk, score in matches:
            baseline_context_parts.append(
                f"[{chunk.source_file} p.{chunk.page_num} | similarity={score:.3f}]\n{chunk.description}"
            )
            if len(baseline_images) < config.MAX_BASELINE_IMAGES_IN_PROMPT and chunk.image_path not in seen_images:
                img_full_path = config.ROOT_DIR / chunk.image_path
                if img_full_path.exists():
                    baseline_images.append(img_full_path.read_bytes())
                    seen_images.add(chunk.image_path)

        baseline_context = "\n\n---\n\n".join(baseline_context_parts)

        _emit(
            on_progress,
            f"Page {page.page_num}/{total}: comparing design to standards...",
            step="compare",
            page=page.page_num,
            total=total,
        )
        try:
            comments = gemini_client.compare_design(
                design_source=pdf_path.name,
                design_page=page.page_num,
                design_description=description,
                design_image_bytes=page.image_bytes,
                baseline_context=baseline_context,
                baseline_image_bytes_list=baseline_images,
            )
        except Exception as exc:
            print(f"  ! comparison failed: {exc}", file=sys.stderr)
            _emit(
                on_progress,
                f"Page {page.page_num}/{total}: comparison failed ({exc}).",
                step="compare",
                page=page.page_num,
                total=total,
                level="error",
            )
            comments = f"_Could not generate comparison: {exc}_"
        else:
            _emit(
                on_progress,
                f"Page {page.page_num}/{total}: page review complete.",
                step="compare",
                page=page.page_num,
                total=total,
            )

        matched_sources = ", ".join(
            f"{c.source_file} p.{c.page_num} ({s:.2f})" for c, s in matches
        ) or "(none)"
        report_sections.append(
            f"\n## Page {page.page_num}\n\n"
            f"**Retrieved baseline matches:** {matched_sources}\n\n"
            f"{comments}\n"
        )

    _emit(on_progress, "Assembling the review report...", step="write", page=total, total=total)
    return "\n".join(report_sections)


def main():
    parser = argparse.ArgumentParser(description="Review a glazing design PDF against indexed standards.")
    parser.add_argument("pdf", type=str, help="Path to the design PDF to review.")
    parser.add_argument("--top-k", type=int, default=config.TOP_K_MATCHES)
    parser.add_argument("--out", type=str, default=None, help="Output markdown report path.")
    args = parser.parse_args()

    pdf_path = Path(args.pdf)
    if not pdf_path.exists():
        print(f"File not found: {pdf_path}", file=sys.stderr)
        sys.exit(1)

    report = review_pdf(pdf_path, top_k=args.top_k)

    config.REVIEW_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = Path(args.out) if args.out else config.REVIEW_OUTPUT_DIR / f"{pdf_path.stem}_review.md"
    out_path.write_text(report, encoding="utf-8")

    print("\n" + "=" * 80)
    print(report)
    print("=" * 80)
    print(f"\nReport written to {out_path}")


if __name__ == "__main__":
    main()
