"""PDF page extraction: render each page to a PNG image and pull its raw text."""
from dataclasses import dataclass
from pathlib import Path

import fitz  # PyMuPDF

from . import config


@dataclass
class PageData:
    source_file: str
    page_num: int  # 1-indexed
    text: str
    image_bytes: bytes


def extract_pages(pdf_path: Path, dpi: int = config.RENDER_DPI) -> list[PageData]:
    """Render every page of a PDF to PNG bytes and extract its embedded text."""
    doc = fitz.open(pdf_path)
    pages = []
    zoom = dpi / 72
    matrix = fitz.Matrix(zoom, zoom)
    try:
        for i, page in enumerate(doc):
            text = page.get_text().strip()
            pix = page.get_pixmap(matrix=matrix)
            image_bytes = pix.tobytes("png")
            pages.append(
                PageData(
                    source_file=Path(pdf_path).name,
                    page_num=i + 1,
                    text=text,
                    image_bytes=image_bytes,
                )
            )
    finally:
        doc.close()
    return pages
