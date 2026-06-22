"""
Lesson 29 eval -- runs WITHOUT an API key.

Checks the golden-trajectory scorer respects ORDER and presence (a length-only
stub fails the wrong-order case) and that the budget scorer enforces step and
cost limits.

    python 29_eval_expansion/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 29_eval_expansion/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe

TRAJ = [
    {"kind": "tool_call", "name": "search", "cost": 1},
    {"kind": "tool_call", "name": "read", "cost": 1},
    {"kind": "tool_call", "name": "summarize", "cost": 2},   # extra call is allowed
    {"kind": "tool_call", "name": "write", "cost": 1},
    {"kind": "final"},
]  # 4 tool calls, total cost 5


def main():
    mod = load_lesson(HERE)

    check("golden sequence present in order (extras allowed)",
          safe(lambda: mod.matches_golden(TRAJ, ["search", "read", "write"])) is True,
          "expected True")
    check("WRONG ORDER fails (a length-only scorer would wrongly pass)",
          safe(lambda: mod.matches_golden(TRAJ, ["write", "read"])) is False,
          "order must matter")
    check("a MISSING required tool fails",
          safe(lambda: mod.matches_golden(TRAJ, ["search", "deploy"])) is False,
          "missing tool must fail")
    check("within_budget passes when under the step limit",
          safe(lambda: mod.within_budget(TRAJ, max_steps=5)) is True, "expected True")
    check("within_budget fails when over the step limit (4 > 3)",
          safe(lambda: mod.within_budget(TRAJ, max_steps=3)) is False, "expected False")
    check("within_budget fails when over the cost budget (5 > 3)",
          safe(lambda: mod.within_budget(TRAJ, max_cost=3)) is False, "expected False")

    report("Lesson 29 - Eval Expansion")


if __name__ == "__main__":
    main()
