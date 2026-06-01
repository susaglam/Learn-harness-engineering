"""
Lesson 09 - Memory & Retrieval  (YOUR implementation)

embed(), cosine(), add() are given. Implement MemoryStore.recall: rank stored
memories by cosine similarity to the query and return the top k texts.

Run:  python 09_memory_retrieval/eval.py     # RED until the TODO is done
"""
from __future__ import annotations

import math
import re


def _tokens(text: str):
    return re.findall(r"[a-z0-9]+", str(text).lower())


def embed(text: str) -> dict:
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
        self.items: list[tuple[str, dict]] = []

    def add(self, text: str):
        self.items.append((text, embed(text)))
        return self

    def recall(self, query: str, k: int = 1) -> list[str]:
        # =====================================================================
        # TODO(you):
        #   1. q = embed(query)
        #   2. Sort self.items by cosine(q, item_vector) DESCENDING.
        #   3. Return the texts of the top k items (a list of strings).
        # =====================================================================
        raise NotImplementedError("Implement MemoryStore.recall - see the TODO above")
