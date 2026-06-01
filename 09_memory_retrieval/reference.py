"""
Lesson 09 - Memory & Retrieval  (reference implementation)

Persist facts and recall the RELEVANT ones by meaning, not keyword equality.
We use a tiny bag-of-words embedding + cosine similarity so the lesson runs
offline and deterministically (a real system swaps in model embeddings).

embed() and cosine() are given; you build recall().
"""
from __future__ import annotations

import math
import re


def _tokens(text: str):
    return re.findall(r"[a-z0-9]+", str(text).lower())


def embed(text: str) -> dict:
    """A bag-of-words vector: {word: count}."""
    vec: dict = {}
    for w in _tokens(text):
        vec[w] = vec.get(w, 0) + 1
    return vec


def cosine(a: dict, b: dict) -> float:
    common = set(a) & set(b)
    dot = sum(a[w] * b[w] for w in common)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0


class MemoryStore:
    def __init__(self):
        self.items: list[tuple[str, dict]] = []  # (text, vector)

    def add(self, text: str):
        self.items.append((text, embed(text)))
        return self

    def recall(self, query: str, k: int = 1) -> list[str]:
        """Return the texts of the k most semantically similar memories."""
        q = embed(query)
        ranked = sorted(self.items, key=lambda it: cosine(q, it[1]), reverse=True)
        return [text for text, _ in ranked[:k]]
