# Lesson 26 — Human-in-the-Loop

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Some actions wait for a human.*
>
> **Arc 7 — Production.** The mechanism behind Lesson 12's `ask` decision.

## The idea

Lesson 12 could return `ask`, but nothing actually *waited*. In production, a
high-stakes action — deploy, delete, send money — must **pause for a human** and
resume only on approval. That needs durable state, not a blocking prompt: park
the action as **pending**, let a human **resolve** it (approve/deny) on their own
schedule, and **gate execution** on that decision. The agent keeps working on
other things meanwhile.

```python
request_approval(queue, "deploy-1", action)     # parked: pending
execute_if_approved(queue, "deploy-1", run)      # -> "PENDING" (nothing ran)
resolve(queue, "deploy-1", "approved")           # a human approves
execute_if_approved(queue, "deploy-1", run)      # -> runs the action
```

## Why a queue, not a blocking prompt

A blocking "are you sure? (y/n)" freezes the agent and dies with the process.
A **pending queue** survives restarts, lets approvals arrive asynchronously, and
generalizes to pause / resume / cancel / rollback / escalation — the full
human-in-the-loop surface. The one invariant: **`run()` must never fire unless the
status is `approved`** (fail safe — unknown/pending never executes).

## What you'll build

`request_approval()` and `resolve()` are given. In [`stub.py`](./stub.py), implement
`execute_if_approved(queue, action_id, run)`:

- status `approved` → `return run()` (the only path that may run it),
- status `denied` → `return "DENIED"`,
- otherwise (pending / unknown) → `return "PENDING"`.

## Run it

```sh
python 26_human_in_the_loop/eval.py                       # RED
python 26_human_in_the_loop/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 26_human_in_the_loop/eval.py
```

→ Next: **Lesson 27 — Tool-Result Management** (*a 10MB result will blow your context*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
