"""
Lesson 26 eval -- runs WITHOUT an API key.

Checks an action waits (pending), runs only once approved, is dropped on denial,
and that run() never fires unless approved. An always-run stub fails.

    python 26_human_in_the_loop/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 26_human_in_the_loop/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


def main():
    mod = load_lesson(HERE)
    queue = {}
    calls = []

    def run():
        calls.append("ran")
        return "DID_IT"

    mod.request_approval(queue, "a1", {"tool": "deploy"})
    pending = safe(lambda: mod.execute_if_approved(queue, "a1", run))  # not resolved yet
    mod.resolve(queue, "a1", "approved")
    ok = safe(lambda: mod.execute_if_approved(queue, "a1", run))       # approved -> runs

    mod.request_approval(queue, "a2", {"tool": "rm -rf"})
    mod.resolve(queue, "a2", "denied")
    denied = safe(lambda: mod.execute_if_approved(queue, "a2", run))   # denied -> blocked

    unknown = safe(lambda: mod.execute_if_approved(queue, "nope", run))

    check("an unresolved action is PENDING (and does not run)",
          pending == "PENDING", repr(pending))
    check("an approved action runs", ok == "DID_IT", repr(ok))
    check("a denied action is blocked", denied == "DENIED", repr(denied))
    check("run() fired EXACTLY once — only for the approved action",
          calls == ["ran"], f"calls={calls}")
    check("an unknown action is PENDING (fail safe)", unknown == "PENDING", repr(unknown))

    report("Lesson 26 - Human-in-the-Loop")


if __name__ == "__main__":
    main()
