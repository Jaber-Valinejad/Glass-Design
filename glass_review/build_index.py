"""Index every baseline standard-design PDF in pdfs/ into the local vector store.

Usage:
    python -m glass_review.build_index [--rebuild]
"""
import argparse
import sys

from . import config, gemini_client, pdf_utils
from .vector_store import Chunk, LocalVectorStore


def build(rebuild: bool = False):
    store = LocalVectorStore()
    if rebuild:
        store.chunks = []
        store.embeddings = None

    pdf_paths = sorted(config.BASELINE_PDF_DIR.glob("*.pdf"))
    if not pdf_paths:
        print(f"No baseline PDFs found in {config.BASELINE_PDF_DIR}")
        return

    for pdf_path in pdf_paths:
        print(f"Indexing {pdf_path.name} ...", flush=True)
        pages = pdf_utils.extract_pages(pdf_path)
        for page in pages:
            if not rebuild and store.has_page(pdf_path.name, page.page_num):
                print(f"  page {page.page_num}/{len(pages)}: already indexed, skipping", flush=True)
                continue

            print(f"  page {page.page_num}/{len(pages)}: describing with Gemini vision ...", flush=True)
            try:
                description = gemini_client.describe_page(page.image_bytes, page.text)
            except Exception as exc:
                print(f"    ! description failed: {exc}", file=sys.stderr, flush=True)
                continue

            image_filename = f"{pdf_path.stem}__p{page.page_num}.png"
            image_path = config.VECTOR_STORE_IMAGES_DIR / image_filename
            image_path.write_bytes(page.image_bytes)

            embed_input = f"SOURCE: {pdf_path.name} page {page.page_num}\n\n{description}\n\nRAW TEXT:\n{page.text}"
            try:
                embedding = gemini_client.embed_text(embed_input)
            except Exception as exc:
                print(f"    ! embedding failed: {exc}", file=sys.stderr, flush=True)
                continue

            chunk = Chunk(
                source_file=pdf_path.name,
                page_num=page.page_num,
                text=page.text,
                description=description,
                image_path=str(image_path.relative_to(config.ROOT_DIR)),
            )
            store.add(chunk, embedding)
            store.save()

        print(f"  saved index after {pdf_path.name}", flush=True)

    print(f"Done. Vector store now has {len(store.chunks)} chunks at {config.VECTOR_STORE_DIR}")


def main():
    parser = argparse.ArgumentParser(description="Build local vector store from baseline glazing PDFs.")
    parser.add_argument("--rebuild", action="store_true", help="Rebuild the entire index from scratch.")
    args = parser.parse_args()
    build(rebuild=args.rebuild)


if __name__ == "__main__":
    main()
