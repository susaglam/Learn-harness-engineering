# Lesson 20 — Worktree Isolation

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Each agent gets its own room.*

## The idea

Run several agents (Lesson 19) on the *same* repository and they'll overwrite each other's edits, fight over the working tree, and corrupt each other's runs. A git **worktree** is the clean fix: the same repository checked out into multiple directories, each on its own branch. Bind one worktree per task and parallel agents never collide — they're in separate rooms.

The harness piece is the **binding**: `task_id → a unique directory`, idempotent (the same task always returns to the same room) and collision-free (no two tasks share one).

```python
reg.allocate("task-42")   # -> /agents/wt-task-42   (created once)
reg.allocate("task-42")   # -> same path (idempotent)
reg.allocate("task-99")   # -> a different path (isolated)
```

> We model just the binding so the lesson runs without git. A production `allocate()` would also shell out to `git worktree add <path> -b <branch>`, and `release()` to `git worktree remove`.

## Why ID-to-directory binding

Isolation is only useful if it's *stable*: a task that resumes must return to its own worktree, not a fresh one, or it loses its in-progress state. And allocation must be collision-free or two agents end up in the same directory — exactly the problem we're solving. Those two invariants — idempotent and unique — are the whole mechanism.

## What you'll build

`release()` is given. In [`stub.py`](./stub.py), implement `allocate(task_id)`:

1. If `task_id` is already bound, return its existing path.
2. Otherwise build a unique path under `base_dir` (e.g. `wt-<task_id>`), store it, and return it.

## Run it

```sh
python 20_worktree_isolation/eval.py                       # RED
python 20_worktree_isolation/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 20_worktree_isolation/eval.py
```

→ Next: **Lesson 21 — Autonomous Agents** (*agents that claim their own work*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
