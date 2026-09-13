"""Shared configuration and paths for the glass system design reviewer."""
import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
IS_VERCEL = bool(os.environ.get("VERCEL"))
WRITABLE_DIR = Path("/tmp/glass_review") if IS_VERCEL else ROOT_DIR

BASELINE_PDF_DIR = ROOT_DIR / "pdfs"
VECTOR_STORE_DIR = ROOT_DIR / "vector_store"
VECTOR_STORE_IMAGES_DIR = VECTOR_STORE_DIR / "images"
VECTOR_STORE_INDEX_PATH = VECTOR_STORE_DIR / "index.json"
VECTOR_STORE_EMBEDDINGS_PATH = VECTOR_STORE_DIR / "embeddings.npy"

COMMITTED_REVIEW_OUTPUT_DIR = ROOT_DIR / "review_output"
REVIEW_OUTPUT_DIR = WRITABLE_DIR / "review_output"
UPLOAD_DIR = WRITABLE_DIR / "uploads"

# Gemini models (free-tier eligible on this account). gemini-2.0-flash/-lite and
# text-embedding-004 returned 0 free quota. The other generateContent models each get
# their own small free-tier bucket (observed: 20 requests/day per model on this key),
# so vision/comparison calls try each of these in order and move to the next model
# once one hits its daily cap (see gemini_client._is_daily_quota_error).
VISION_MODEL_CANDIDATES = [
    "gemini-2.5-flash-lite",
    "gemini-flash-lite-latest",
    "gemini-3-flash-preview",
    "gemini-3.1-flash-lite",
    "gemini-2.5-flash",
]
COMPARISON_MODEL_CANDIDATES = VISION_MODEL_CANDIDATES
EMBEDDING_MODEL = "gemini-embedding-001"

RENDER_DPI = 200
TOP_K_MATCHES = 6
MAX_BASELINE_IMAGES_IN_PROMPT = 3
