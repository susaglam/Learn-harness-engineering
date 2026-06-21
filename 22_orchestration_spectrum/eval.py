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

    # --- the count must CONSUME each verdict: a different judge -> a different count ---
    smart2 = dict(SMART)
    smart2[ITEMS[2]] = "feature"   # this judge now calls item 2 a feature, not a bug
    h2 = safe(lambda: mod.classify_hybrid(ITEMS, lambda it: smart2[it]))
    check("a different judge yields a different count (hardcoded bugs=2 fails here)",
          isinstance(h2, dict) and h2.get("bugs") == 1, f"got {h2!r}"[:80])

    # --- exercise the autonomous arm too (whole task delegated in ONE call) ---
    auto_calls = []

    def model_solve(items):
        auto_calls.append(tuple(items))
        return 2

    auto = safe(lambda: mod.classify_autonomous(ITEMS, model_solve))
    check("autonomous arm delegates the WHOLE list in a single call",
          isinstance(auto, dict) and auto.get("style") == "autonomous"
          and auto.get("bugs") == 2 and len(auto_calls) == 1,
          f"auto={auto}, calls={len(auto_calls)}")

    report("Lesson 22 - The Orchestration Spectrum")


if __name__ == "__main__":
    main()
