"""Thin wrapper around the Gemini API for vision description, text embeddings,
and the final baseline-vs-design comparison call.
"""
from contextlib import contextmanager
from contextvars import ContextVar

import httpx
from google import genai
from google.genai import errors as genai_errors
from google.genai import types
from tenacity import retry, retry_if_exception, stop_after_attempt, wait_exponential

from . import config

_api_key_override: ContextVar[str | None] = ContextVar("gemini_api_key", default=None)
_clients: dict[str, genai.Client] = {}


@contextmanager
def using_api_key(api_key: str | None):
    token = _api_key_override.set((api_key or "").strip() or None)
    try:
        yield
    finally:
        _api_key_override.reset(token)


def resolve_api_key() -> str | None:
    return _api_key_override.get() or config.GEMINI_API_KEY


def get_client() -> genai.Client:
    api_key = resolve_api_key()
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not set. Enter it in the review form, put it in a "
            ".env file, or export it as an environment variable."
        )
    client = _clients.get(api_key)
    if client is None:
        client = genai.Client(api_key=api_key)
        _clients[api_key] = client
    return client


def _is_daily_quota_error(exc: BaseException) -> bool:
    """True if this 429 is a per-day cap (won't clear on backoff; switch models instead)."""
    if not (isinstance(exc, genai_errors.ClientError) and getattr(exc, "code", None) == 429):
        return False
    details = getattr(exc, "details", None) or {}
    violations = details.get("error", {}).get("details", [])
    for d in violations:
        for v in d.get("violations", []):
            if "PerDay" in v.get("quotaId", ""):
                return True
    return False


def _is_transient_error(exc: BaseException) -> bool:
    if isinstance(exc, genai_errors.ClientError) and getattr(exc, "code", None) == 429:
        return not _is_daily_quota_error(exc)
    if isinstance(exc, genai_errors.ServerError):
        return True
    # DNS hiccups, dropped connections, and "server disconnected without sending a
    # response" surface as OSError/socket.gaierror or httpx transport errors, not as
    # a genai error type.
    if isinstance(exc, (OSError, ConnectionError, httpx.RequestError)):
        return True
    return False


with_rate_limit_retry = retry(
    retry=retry_if_exception(_is_transient_error),
    wait=wait_exponential(multiplier=2, min=2, max=60),
    stop=stop_after_attempt(8),
    reraise=True,
)


def _call_with_model_fallback(model_candidates: list[str], call_fn):
    """Try call_fn(model) over each candidate model, skipping to the next one as soon
    as a model's free-tier *daily* cap is hit. Per-minute 429s/network errors are
    retried on the same model via with_rate_limit_retry before falling through.
    """
    last_exc: Exception | None = None
    for model in model_candidates:
        try:
            return with_rate_limit_retry(call_fn)(model)
        except genai_errors.ClientError as exc:
            if _is_daily_quota_error(exc):
                last_exc = exc
                continue
            raise
    raise last_exc


DESCRIBE_PROMPT = """You are a senior glazing / interior glass-wall systems shop-drawing reviewer.
Look at this single shop-drawing sheet (image) from a glazing submittal package. It may be a
cover sheet, floor plan, elevation, or a detail sheet (head/sill/jamb sections of glass framing,
doors, partitions, etc.). Raw OCR text extracted from the sheet is also provided for reference,
but the drawing itself is the source of truth.

Produce a structured, detailed factual description, NOT a critique yet:
1. Sheet type and title/number if visible.
2. Every distinct detail/section shown (e.g. head detail, sill detail, jamb detail) with its callout/tag.
3. For each detail: components shown and their materials/finishes (e.g. aluminum tube, wood blocking,
   metal stud track, glazing gasket, structural silicone, setting block, glass type/thickness,
   fasteners, anchors, sealant, flashing, weep holes, fire-safing, insulation, drainage).
4. Dimensions, clearances, and callout notes/text visible on the sheet (verbatim where legible).
5. Any markups, redline comments, clouds, or annotations visible on the sheet (verbatim).
6. Anything that looks unclear, missing a callout, or inconsistent within this sheet alone.

Raw OCR text from this page:
---
{page_text}
---

Be thorough and specific; this description will be used for retrieval against a library of
standard glazing details, so include every technical term and callout you can identify.
"""

COMPARE_PROMPT = """You are a senior glazing / interior glass-wall systems QA reviewer performing a
shop-drawing submittal review. You are comparing a DESIGN sheet (the one being reviewed) against
relevant pages pulled from a library of STANDARD/BASELINE glazing detail drawings (previously
approved or reference submittals for similar projects).

DESIGN SHEET BEING REVIEWED: {design_source} (page {design_page})
Description of the design sheet:
---
{design_description}
---

RETRIEVED BASELINE/STANDARD REFERENCE CONTEXT (most relevant matches from the standards library):
---
{baseline_context}
---

You are also given the actual images: first the DESIGN sheet image, then up to a few of the
best-matching BASELINE reference sheet images, in that order.

Compare the design sheet against the baseline standards and produce a concise but specific QA
review. For each issue found, cite which baseline source/page it conflicts with or which standard
practice it deviates from. Structure your answer as:

## Summary
One or two sentences on overall conformance.

## Issues Found
A numbered list. For each issue: what's wrong/missing/inconsistent, why it matters
(constructability, code, water/air infiltration, structural, fire/life-safety, finish quality),
and which baseline reference supports the concern. If markups/redline comments are already present
on the design sheet itself, treat them as confirmed open issues and include them.

## Items That Match the Standard
Briefly note what conforms well (keep this short).

## Open Questions / Needs Clarification
Anything you can't fully judge from the sheet alone.

If you find no real issues, say so plainly in the Summary and keep the Issues list empty rather
than inventing problems.
"""


def describe_page(image_bytes: bytes, page_text: str) -> str:
    client = get_client()
    prompt = DESCRIBE_PROMPT.format(page_text=page_text or "(no extractable text)")

    def call(model: str):
        response = client.models.generate_content(
            model=model,
            contents=[
                types.Part.from_bytes(data=image_bytes, mime_type="image/png"),
                prompt,
            ],
        )
        return response.text or ""

    return _call_with_model_fallback(config.VISION_MODEL_CANDIDATES, call)


@with_rate_limit_retry
def embed_text(text: str) -> list[float]:
    client = get_client()
    response = client.models.embed_content(
        model=config.EMBEDDING_MODEL,
        contents=text,
    )
    return list(response.embeddings[0].values)


def compare_design(
    design_source: str,
    design_page: int,
    design_description: str,
    design_image_bytes: bytes,
    baseline_context: str,
    baseline_image_bytes_list: list[bytes],
) -> str:
    client = get_client()
    prompt = COMPARE_PROMPT.format(
        design_source=design_source,
        design_page=design_page,
        design_description=design_description,
        baseline_context=baseline_context or "(no closely matching baseline content retrieved)",
    )
    contents = [types.Part.from_bytes(data=design_image_bytes, mime_type="image/png")]
    for img_bytes in baseline_image_bytes_list:
        contents.append(types.Part.from_bytes(data=img_bytes, mime_type="image/png"))
    contents.append(prompt)

    def call(model: str):
        response = client.models.generate_content(model=model, contents=contents)
        return response.text or ""

    return _call_with_model_fallback(config.COMPARISON_MODEL_CANDIDATES, call)
