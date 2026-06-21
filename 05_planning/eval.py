"""
Lesson 05 eval -- runs WITHOUT an API key.

Checks that writing a plan stores normalized todos and renders a progress view.

    python 05_planning/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 05_planning/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


def main():
    mod = load_lesson(HERE)
    store = mod.TodoStore()

    out = safe(lambda: store.write([
        {"content": "design", "status": "completed"},
        {"content": "build", "status": "in_progress"},
        {"content": "  test  "},  # no status -> pending; whitespace must be stripped
    ]))

    check("write stored all three todos",
          len(getattr(store, "todos", [])) == 3,
          f"got {len(getattr(store, 'todos', []))}")
    check("missing status defaults to 'pending'",
          safe(lambda: store.todos[2]["status"]) == "pending",
          "third todo should default to pending")
    check("content is .strip()-normalized",
          safe(lambda: store.todos[2]["content"]) == "test",
          "leading/trailing whitespace not stripped")
    check("rendered view shows progress count (1/3 done)",
          "1/3 done" in str(out), repr(out)[:90])
    check("rendered view marks completed items with [x]",
          "[x] design" in str(out), "completed mark missing")
    check("rendered view marks in_progress items with [~]",
          "[~] build" in str(out), "in_progress mark missing")
    check("rendered view marks pending items with [ ]",
          "[ ] test" in str(out), "pending mark missing")

    report("Lesson 05 - Planning")


if __name__ == "__main__":
    main()
