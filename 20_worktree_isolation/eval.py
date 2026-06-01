"""
Lesson 20 eval -- runs WITHOUT an API key or git.

Checks the task->worktree binding: unique per task, idempotent, under base_dir,
and re-allocatable after release.

    python 20_worktree_isolation/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 20_worktree_isolation/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


def main():
    mod = load_lesson(HERE)
    reg = mod.WorktreeRegistry(base_dir="/tmp/agents")

    p1 = safe(lambda: reg.allocate("t1"))
    p1b = safe(lambda: reg.allocate("t1"))
    p2 = safe(lambda: reg.allocate("t2"))

    check("allocate returns a path string", isinstance(p1, str)
          and not p1.startswith("__RAISED__"), repr(p1)[:60])
    check("the same task always gets the same directory (idempotent)",
          isinstance(p1, str) and p1 == p1b, f"{p1!r} vs {p1b!r}")
    check("different tasks get DIFFERENT directories (no collision)",
          isinstance(p1, str) and isinstance(p2, str) and p1 != p2,
          f"{p1!r} vs {p2!r}")
    check("allocated directory is under base_dir",
          isinstance(p1, str) and "agents" in p1.replace("\\", "/"), repr(p1)[:60])

    reg.release("t1")
    p1c = safe(lambda: reg.allocate("t1"))
    check("a task can be allocated again after release",
          isinstance(p1c, str) and not p1c.startswith("__RAISED__"), repr(p1c)[:60])

    report("Lesson 20 - Worktree Isolation")


if __name__ == "__main__":
    main()
