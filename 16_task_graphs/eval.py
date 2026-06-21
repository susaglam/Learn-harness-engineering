"""
Lesson 16 eval -- runs WITHOUT an API key.

Builds a small task graph and checks readiness resolution + disk round-trip.

    python 16_task_graphs/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 16_task_graphs/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


def _ids(tasks):
    return sorted(t["id"] for t in tasks) if isinstance(tasks, list) else None


def main():
    mod = load_lesson(HERE)
    tasks = [
        {"id": "A", "status": "pending", "blockedBy": []},
        {"id": "B", "status": "pending", "blockedBy": ["A"]},
        {"id": "C", "status": "pending", "blockedBy": ["A", "B"]},
        {"id": "D", "status": "completed", "blockedBy": []},
        {"id": "E", "status": "pending", "blockedBy": ["D"]},
    ]

    ready0 = safe(lambda: mod.next_ready(tasks))
    check("next_ready returns a list", isinstance(ready0, list), repr(ready0)[:70])
    check("initially ready = A (no deps) and E (dep D done)",
          _ids(ready0) == ["A", "E"], f"got {_ids(ready0)}")
    check("blocked tasks (B, C) are NOT ready initially",
          isinstance(ready0, list)
          and all(t["id"] not in ("B", "C") for t in ready0),
          f"got {_ids(ready0)}")

    tasks[0]["status"] = "completed"  # complete A
    ready1 = safe(lambda: mod.next_ready(tasks))
    check("after A completes, B becomes ready",
          isinstance(ready1, list) and "B" in _ids(ready1), f"got {_ids(ready1)}")
    check("C is still blocked (needs B too)",
          isinstance(ready1, list) and "C" not in _ids(ready1), f"got {_ids(ready1)}")

    tmp = os.path.join(tempfile.mkdtemp(prefix="lhe_tg_"), "tasks.json")
    mod.save(tasks, tmp)
    check("tasks round-trip through disk (save/load)",
          mod.load(tmp) == tasks, "persisted graph should reload identically")

    # --- edge cases that make next_ready non-trivial ---
    edge = [
        {"id": "noKey", "status": "pending"},                          # no 'blockedBy' key
        {"id": "dangling", "status": "pending", "blockedBy": ["ZZZ"]}, # dep not on the board
    ]
    re2 = safe(lambda: mod.next_ready(edge))
    check("a task with no 'blockedBy' key is ready (uses the .get default)",
          isinstance(re2, list) and "noKey" in _ids(re2), f"got {_ids(re2)}")
    check("a task blocked by a non-existent id is NEVER ready",
          isinstance(re2, list) and "dangling" not in _ids(re2), f"got {_ids(re2)}")

    report("Lesson 16 - Task Graphs")


if __name__ == "__main__":
    main()
