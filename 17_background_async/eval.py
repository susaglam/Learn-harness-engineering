"""
Lesson 17 eval -- runs WITHOUT an API key.

Starts two background jobs (one succeeds, one raises) and checks both deliver
notifications, with the error captured rather than crashing.

    python 17_background_async/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 17_background_async/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


def main():
    mod = load_lesson(HERE)
    runner = mod.BackgroundRunner()

    def quick():
        return "QUICK_DONE"

    def boom():
        raise ValueError("kaboom")

    h1 = safe(lambda: runner.start("j1", quick))
    safe(lambda: runner.start("j2", boom))
    notes = safe(lambda: runner.drain())
    is_list = isinstance(notes, list)
    by_id = {n["id"]: n for n in notes} if is_list else {}

    check("start() returns the job id (a non-blocking handle)", h1 == "j1",
          repr(h1)[:50])
    check("both jobs delivered a notification", set(by_id.keys()) == {"j1", "j2"},
          f"ids={list(by_id.keys())}")
    check("the successful job's result was captured",
          by_id.get("j1", {}).get("result") == "QUICK_DONE", repr(by_id.get("j1"))[:60])
    check("the failing job's error was captured (not crashed)",
          "ERROR" in str(by_id.get("j2", {}).get("result"))
          and "kaboom" in str(by_id.get("j2", {}).get("result")),
          repr(by_id.get("j2"))[:60])
    check("drain returned exactly two notifications", is_list and len(notes) == 2,
          f"len={len(notes) if is_list else 'n/a'}")

    report("Lesson 17 - Background & Async")


if __name__ == "__main__":
    main()
