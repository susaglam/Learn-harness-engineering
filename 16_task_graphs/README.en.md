# Lesson 16 — Task Graphs

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Big goals persist to disk as ordered tasks.*

## The idea

The TodoWrite list (Lesson 05) lives in the conversation and dies with it. For long, multi-session, or multi-agent work you need something sturdier: a **task graph** persisted to disk, where each task declares which others must finish first via `blockedBy`. That turns "a big goal" into a **DAG** (directed acyclic graph) the harness can drive deterministically.

The core query is **readiness**: *which tasks can run right now?* — the ones that are still `pending` and whose every dependency is already `completed`.

```python
tasks = [
    {"id": "A", "status": "pending",   "blockedBy": []},
    {"id": "B", "status": "pending",   "blockedBy": ["A"]},   # waits for A
]
next_ready(tasks)   # -> [A]   (B unblocks once A completes)
```

## Why disk + dependencies

- **Disk** means the plan survives a crash, a new session, or being handed to another agent — the groundwork for the multi-agent lessons that follow.
- **Dependencies** let you express real structure ("can't deploy before tests pass") and safely parallelize everything that *isn't* ordered. `next_ready` is the scheduler other agents will pull from in Lesson 21.

## What you'll build

`save()` / `load()` (JSON persistence) are given. In [`stub.py`](./stub.py), implement `next_ready(tasks)`:

1. Compute `done` = the set of ids of `completed` tasks.
2. Return every `pending` task whose every `blockedBy` id is in `done`.

## Run it

```sh
python 16_task_graphs/eval.py                       # RED
python 16_task_graphs/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 16_task_graphs/eval.py
```

→ Next: **Lesson 17 — Background & Async** (*slow work goes async; the agent keeps thinking*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
