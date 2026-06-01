"""
Lesson 16 - Task Graphs  (reference implementation)

A big goal becomes many small tasks, persisted to disk, with `blockedBy`
dependencies. The scheduler asks: which tasks are READY right now? -- pending,
and with every dependency already completed. save/load are given; you build
next_ready().
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
    """Return the pending tasks whose every blockedBy dependency is completed."""
    done = {t["id"] for t in tasks if t.get("status") == "completed"}
    ready = []
    for t in tasks:
        if t.get("status") == "pending" and all(dep in done for dep in t.get("blockedBy", [])):
            ready.append(t)
    return ready
