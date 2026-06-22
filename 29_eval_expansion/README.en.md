# Lesson 29 — Eval Expansion

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Grade trajectories, not vibes — with budgets.*
>
> **Arc 7 — Production.** The grown-up version of Lesson 04, and the course's last word.

## The idea

Lesson 04 scored single facts ("did it call bash?"). Production grading asks
harder questions, and asks them automatically over many runs:

- **Golden trajectory** — did the run hit the *required tool sequence, in order*?
  (Search → read → write, not write → search.) Extra steps are fine; missing or
  out-of-order required steps are not.
- **Budgets** — did it stay within a **step** and **cost** ceiling? An agent that
  gets the right answer in 50 expensive calls is still a regression.

```python
matches_golden(traj, ["search", "read", "write"])   # ordered subsequence?
within_budget(traj, max_steps=10, max_cost=5)        # under the ceilings?
```

## Why this closes the course

The whole curriculum is eval-driven; this lesson hands you the scorers a real
team runs in CI: golden trajectories catch *behavioral* regressions, budgets
catch *cost/latency* regressions, and together they feed a regression dashboard.
It's the same thesis the course opened with — **a measurable agent is all you
need** — turned into the tools that keep an agent measurable in production.

## What you'll build

In [`stub.py`](./stub.py), implement two scorers over a trajectory (a list of event dicts):

- `matches_golden(traj, golden_tools)` → are the golden tools an *ordered subsequence* of the `tool_call` names?
- `within_budget(traj, max_steps, max_cost)` → step count and summed `cost` within the (optional) limits?

## Run it

```sh
python 29_eval_expansion/eval.py                       # RED
python 29_eval_expansion/eval.py                       # GREEN (after the TODOs)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 29_eval_expansion/eval.py
```

You've reached the end. Twenty-nine lessons, one loop, every one proven by a
failing test you made pass — through the toy mechanisms and out the other side to
the production boundaries. **A measurable agent is all you need.**

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
