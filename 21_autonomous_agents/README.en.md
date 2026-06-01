# Lesson 21 — Autonomous Agents

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Agents that claim their own work.*

## The idea

In Lesson 19 you could imagine a leader assigning tasks to teammates one by one. That leader is a bottleneck. **Autonomous** agents remove it: a shared **board** of tasks sits in the open, and each idle agent **claims** the next available one itself, works it, then comes back for more. No central dispatcher — the system self-organizes.

The one property that must hold is **no double-claim**: a task must go to exactly one agent, even when several reach for work at the same moment. Claiming is therefore an *atomic* "check it's free, then mark it mine" step.

```python
task = claim_next(board, "agent-A")   # pending+unowned -> now owned by A, in_progress
# ...A works it... then loops back to claim_next again
```

## Why this is the top of the scale arc

Combine everything: a persisted task graph (Lesson 16) supplies claimable work; the message bus (Lesson 19) lets agents coordinate; worktrees (Lesson 20) keep their edits apart; and self-claiming turns a pile of tasks into a self-running swarm. The harness provides the board and the atomic claim; the agents provide the judgment.

## What you'll build

In [`stub.py`](./stub.py), implement `claim_next(board, agent_id)`:

1. Scan `board` in order for the first task that is `status == "pending"` **and** has no `owner`.
2. Claim it: set `owner = agent_id` and `status = "in_progress"`; return the task.
3. If nothing is claimable, return `None`.

## Run it

```sh
python 21_autonomous_agents/eval.py                       # RED
python 21_autonomous_agents/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 21_autonomous_agents/eval.py
```

→ Next: **Lesson 22 — The Orchestration Spectrum** (*hardcode what must be reliable; delegate what must be smart*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
