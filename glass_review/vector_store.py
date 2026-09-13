"""A small local, file-based vector store (no external DB server required).

Persists to <project_root>/vector_store/:
  - index.json       metadata + text for every chunk (source file, page, description, etc.)
  - embeddings.npy    float32 matrix, one row per chunk, aligned by position with index.json
  - images/           rendered PNG of every indexed baseline page, for re-use in comparison prompts
"""
import json
from dataclasses import asdict, dataclass

import numpy as np

from . import config


@dataclass
class Chunk:
    source_file: str
    page_num: int
    text: str
    description: str
    image_path: str


class LocalVectorStore:
    def __init__(self):
        self.chunks: list[Chunk] = []
        self.embeddings: np.ndarray | None = None
        config.VECTOR_STORE_DIR.mkdir(parents=True, exist_ok=True)
        config.VECTOR_STORE_IMAGES_DIR.mkdir(parents=True, exist_ok=True)
        self.load()

    def load(self):
        if config.VECTOR_STORE_INDEX_PATH.exists() and config.VECTOR_STORE_EMBEDDINGS_PATH.exists():
            with open(config.VECTOR_STORE_INDEX_PATH, "r", encoding="utf-8") as f:
                raw = json.load(f)
            self.chunks = [Chunk(**c) for c in raw]
            self.embeddings = np.load(config.VECTOR_STORE_EMBEDDINGS_PATH)
        else:
            self.chunks = []
            self.embeddings = None

    def save(self):
        with open(config.VECTOR_STORE_INDEX_PATH, "w", encoding="utf-8") as f:
            json.dump([asdict(c) for c in self.chunks], f, indent=2)
        if self.embeddings is not None:
            np.save(config.VECTOR_STORE_EMBEDDINGS_PATH, self.embeddings)

    def has_source(self, source_file: str) -> bool:
        return any(c.source_file == source_file for c in self.chunks)

    def has_page(self, source_file: str, page_num: int) -> bool:
        return any(c.source_file == source_file and c.page_num == page_num for c in self.chunks)

    def add(self, chunk: Chunk, embedding: list[float]):
        self.chunks.append(chunk)
        vec = np.array(embedding, dtype=np.float32).reshape(1, -1)
        if self.embeddings is None:
            self.embeddings = vec
        else:
            self.embeddings = np.vstack([self.embeddings, vec])

    def search(self, query_embedding: list[float], top_k: int = config.TOP_K_MATCHES) -> list[tuple[Chunk, float]]:
        if self.embeddings is None or len(self.chunks) == 0:
            return []
        q = np.array(query_embedding, dtype=np.float32)
        q_norm = q / (np.linalg.norm(q) + 1e-8)
        m_norm = self.embeddings / (np.linalg.norm(self.embeddings, axis=1, keepdims=True) + 1e-8)
        scores = m_norm @ q_norm
        top_idx = np.argsort(-scores)[:top_k]
        return [(self.chunks[i], float(scores[i])) for i in top_idx]
