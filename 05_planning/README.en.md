# Lesson 05 — Planning

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *A plan turns intention into checkable steps.*

## The idea

Hand a model a multi-step task and it tends to drift — forget a step, repeat one, declare victory early. The fix is a tool that makes the agent **write its plan down first**: a `TodoWrite` tool. The model emits a list of steps with statuses; the harness stores it and renders it back into the conversation so the plan stays visible and gets updated as work proceeds.

This is cheap and high-leverage: externalizing the plan as state measurably raises completion on long tasks, and — connecting to Lesson 04 — gives you something concrete to *observe* and score.

```python
todo_write([
    {"content": "Read the failing test", "status": "completed"},
    {"content": "Fix the bug",          "status": "in_progress"},
    {"content": "Re-run the suite",     "status": "pending"},
])
# -> "[x] Read the failing test
#     [~] Fix the bug
#     [ ] Re-run the suite
#     (1/3 done)"
```

## Why render it back

The rendered list is fed to the model on the next turn. Seeing `[~]`/`[x]` keeps the agent oriented: what's done, what's next, what's left. It's working memory for the *task*, the same way the system prompt is working memory for the *role*.

## What you'll build

`render()` is given. In [`stub.py`](./stub.py), implement `TodoStore.write(todos)`:

1. Normalize each item to `{"content": ..stripped.., "status": ..default "pending"..}`.
2. Replace `self.todos` with the normalized list.
3. `return self.render()`.

## Run it

```sh
python 05_planning/eval.py                       # RED
python 05_planning/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 05_planning/eval.py
```

→ Next: **Lesson 06 — Structured I/O** (*design the output the model has to read*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
