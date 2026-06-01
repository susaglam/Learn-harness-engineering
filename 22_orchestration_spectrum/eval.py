"""
Lesson 22 eval -- runs WITHOUT an API key (the "model" is a scripted classifier).

One input where a paraphrased bug ("won't load") has no keyword. Shows the
trade-off: the scripted rule misses it; the hybrid (delegated judgment) catches
it while keeping a deterministic, per-item skeleton.

    python 22_orchestration_spectrum/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 22_orchestration_spectrum/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe

ITEMS = [
    "app crashes on login",        # bug (keyword: crash)
    "add dark mode",               # feature
    "the page won't load at all",  # bug, but NO keyword -> scripted misses it
    "support CSV import",          # feature
]
# A "smart" per-item judge that understands the paraphrase.
SMART = {ITEMS[0]: "bug", ITEMS[1]: "feature", ITEMS[2]: "bug", ITEMS[3]: "feature"}


def main():
    mod = load_lesson(HERE)

    calls = []

    def model_classify(item):
        calls.append(item)
        return SMART[item]

    hybrid = safe(lambda: mod.classify_hybrid(ITEMS, model_classify))
    scripted = mod.classify_scripted(ITEMS)  # given; for contrast

    check("hybrid returns a result tagged 'hybrid'",
          isinstance(hybrid, dict) and hybrid.get("style") == "hybrid", repr(hybrid)[:60])
    check("hybrid counts bugs correctly via delegated judgment (2)",
          isinstance(hybrid, dict) and hybrid.get("bugs") == 2, repr(hybrid)[:60])
    check("hybrid skeleton calls the model once PER ITEM (deterministic loop)",
          calls == ITEMS, f"calls={len(calls)} expected {len(ITEMS)}")
    check("the pure-scripted rule MISSES the paraphrased bug (gets 1, not 2)",
          scripted["bugs"] == 1, f"scripted={scripted}")
    check("hybrid beats scripted on this input (judgment where it pays off)",
          isinstance(hybrid, dict) and hybrid.get("bugs", 0) > scripted["bugs"],
          "hybrid should out-score the brittle rule")

    report("Lesson 22 - The Orchestration Spectrum")


if __name__ == "__main__":
    main()
