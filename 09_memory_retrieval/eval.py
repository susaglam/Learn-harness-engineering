"""
Lesson 09 eval -- runs WITHOUT an API key.

Stores four facts and checks recall ranks the semantically relevant ones first.

    python 09_memory_retrieval/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 09_memory_retrieval/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


def main():
    mod = load_lesson(HERE)
    m = mod.MemoryStore()
    m.add("The capital of France is Paris.")
    m.add("Python is a programming language.")
    m.add("The Eiffel Tower is located in Paris, France.")
    m.add("Cats are mammals.")

    r1 = safe(lambda: m.recall("Eiffel Tower", 1))
    r2 = safe(lambda: m.recall("programming language", 1))
    r3 = safe(lambda: m.recall("Paris France capital", 2))

    check("recall returns a list", isinstance(r1, list), repr(r1)[:80])
    check("k=1 returns exactly one item", isinstance(r1, list) and len(r1) == 1,
          f"len={len(r1) if isinstance(r1, list) else 'n/a'}")
    check("ranks the Eiffel fact first for an Eiffel query",
          isinstance(r1, list) and r1 and "Eiffel" in r1[0], repr(r1)[:80])
    check("ranks the Python fact first for a programming query",
          isinstance(r2, list) and r2 and "Python" in r2[0], repr(r2)[:80])
    check("k=2 returns two items", isinstance(r3, list) and len(r3) == 2,
          repr(r3)[:80])
    check("both Paris-related facts retrieved for a Paris query",
          isinstance(r3, list) and sum(1 for t in r3 if "Paris" in t) == 2,
          repr(r3)[:90])

    # --- make cosine NORMALIZATION load-bearing: a raw dot-product stub fails here ---
    # Short on-topic fact vs a keyword-stuffed long one. Raw dot-product ranks the
    # long fact (3x "deploy") first; length-normalized cosine ranks the short one.
    m.add("Deploy the release.")
    m.add("deploy deploy deploy alpha bravo charlie delta echo foxtrot golf hotel "
          "india juliet kilo lima mike november oscar papa quebec romeo sierra")
    rd = safe(lambda: m.recall("deploy", 1))
    check("cosine ranks a short on-topic fact over a keyword-stuffed long one",
          isinstance(rd, list) and rd and rd[0] == "Deploy the release.",
          f"a dot-product (un-normalized) impl fails here: {rd!r}"[:110])

    # --- edges ---
    one = safe(lambda: m.recall("Paris"))
    check("default k returns exactly one item",
          isinstance(one, list) and len(one) == 1, repr(one)[:60])
    empty = mod.MemoryStore()
    check("recall on an empty store returns []",
          safe(lambda: empty.recall("anything", 3)) == [], "expected []")

    report("Lesson 09 - Memory & Retrieval")


if __name__ == "__main__":
    main()
