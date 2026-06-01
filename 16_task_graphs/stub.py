"""
Lesson 16 - Task Graphs  (YOUR implementation)

save/load are given. Implement next_ready: the dependency resolver that returns
the tasks ready to run now.

Run:  python 16_task_graphs/eval.py     # RED until the TODO is done
"""
from __future__ import annotations

import json


def save(tasks, path):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(tasks, f)


def load(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def next_ready(tasks):
    # =========================================================================
    # TODO(you):
    #   1. done = set of ids of tasks whose status == "completed".
    #   2. Return every task that is status == "pending" AND whose every id in
    #      task.get("blockedBy", []) is in `done`.
    # =========================================================================
    raise NotImplementedError("Implement next_ready - see the TODO above")
