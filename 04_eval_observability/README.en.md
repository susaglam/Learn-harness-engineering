# Lesson 04 — Eval & Observability

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *If you can't measure it, you're hoping.*

## The idea

This is the most under-taught harness skill, so it comes early — it frames every lesson after it. Two halves:

- **Observability:** record everything the agent does as a **trajectory** — an ordered log of events (model turns, tool calls, tool results, the final answer).
- **Evaluation:** grade that trajectory with **scorers** — small pure functions that answer questions like *did it call the right tool? did the final answer contain the expected fact? how many steps did it take?*

A harness bug and a model mistake look identical from the outside. Trajectories make the agent's behavior *inspectable*; scorers make it *measurable*. Together they turn "it seems to work" into a number you can track across changes.

```python
traj = Trajectory()
# ...the loop records as it runs...
traj.record("tool_call", name="bash", input={"command": "ls"})
traj.record("final", text="Done.")

assert used_tool(traj, "bash")          # behavior, asserted
assert step_count(traj) <= 5            # efficiency, asserted
```

## Why it comes before the rest

Every later mechanism (memory, teams, recovery) is a *claim* that something improves the agent. Without scorers you can't tell. The whole course is eval-driven for exactly this reason: a GREEN eval is evidence; a vibe is not.

## What you'll build

The `Trajectory` recorder is given. In [`stub.py`](./stub.py), implement three scorers:

- `used_tool(traj, name)` → did any `tool_call` event use this tool?
- `final_contains(traj, substr)` → does the last `final` event's text contain `substr` (case-insensitive)?
- `step_count(traj)` → how many `tool_call` events occurred?

## Run it

```sh
python 04_eval_observability/eval.py                       # RED
python 04_eval_observability/eval.py                       # GREEN (after the TODOs)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 04_eval_observability/eval.py
```

→ Next: **Lesson 05 — Planning** (*a plan turns intention into checkable steps*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
