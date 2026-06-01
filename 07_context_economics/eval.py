"""
Lesson 07 eval -- runs WITHOUT an API key.

Builds an over-budget conversation and checks compaction brings it under
budget while preserving the seed and the most recent turn.

    python 07_context_economics/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 07_context_economics/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


def main():
    mod = load_lesson(HERE)

    msgs = [{"role": "user", "content": "seed"}]
    for _ in range(5):
        msgs.append({"role": "assistant", "content": "x" * 120})  # ~30 tokens each
    msgs.append({"role": "assistant", "content": "second to last"})
    msgs.append({"role": "user", "content": "the last one"})

    budget = 40
    orig = mod.total_tokens(msgs)
    out = safe(lambda: mod.compact(msgs, budget=budget, keep_recent=2))
    is_list = isinstance(out, list)
    new = mod.total_tokens(out) if is_list else None

    check("compact returns a list of messages", is_list, repr(out)[:80])
    check("original really was over budget", orig > budget, f"orig={orig}")
    check("compacted conversation fits the budget", is_list and new <= budget,
          f"new={new}, budget={budget}")
    check("kept the seed (first) message", is_list and out[0] == msgs[0], "seed dropped")
    check("kept the most recent message", is_list and out[-1] == msgs[-1], "recent dropped")
    check("inserted a compaction marker",
          is_list and any("compact" in str(m.get("content", "")).lower() for m in out),
          "no summary marker")

    report("Lesson 07 - Context & Token Economics")


if __name__ == "__main__":
    main()
