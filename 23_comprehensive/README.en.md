# Lesson 23 — The Comprehensive Agent

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Many mechanisms, one measurable loop.*

## The idea

This is the endpoint. Every earlier lesson added one mechanism; here they come home to a single loop — and an eval proves the whole thing works end to end. This run wires together:

- the **agent loop** (Lesson 01),
- a **tool registry / dispatch** (Lesson 02),
- a **permission gate** (Lesson 12), and
- a **trajectory tracer** (Lesson 04),

so that every tool call is permission-checked, dispatched, and recorded — and a *denied* call turns into recoverable feedback (`DENIED: ...`) instead of an action the model can't see.

```python
final = run_agent(client, model, messages, registry, permission, trace)
# write_file -> allowed, executed, traced
# rm         -> denied, never executed, traced as "denied"
# loop feeds both tool_results back, model finishes, trace has the "final" event
```

## Why the loop still hasn't changed

Look at the body: it's the Lesson 01 loop. Permissions, tracing, dispatch — they slot *around* the tool call, exactly where Lessons 12/04/02 said they would. That's the thesis made concrete: the loop belongs to the agent and never changes; the harness is everything you compose around it. Add memory, hooks, subagents, teams the same way — each is another thing slotted around this one loop.

## What you'll build

`Registry`, `Trajectory`, and `extract_text` are given. In [`stub.py`](./stub.py), implement `run_agent(client, model, messages, registry, permission, trace)`:

1. Call the model with `tools=registry.schemas`; record a `model_turn`; append the assistant message.
2. If it didn't ask for tools, record a `final` event and return.
3. For each `tool_use` block: if `permission` says `deny`, record `denied` and produce a `DENIED: ...` result; otherwise record `tool_call` and `registry.dispatch(...)`.
4. Feed all `tool_result`s back as one user message and loop.

## Run it

```sh
python 23_comprehensive/eval.py                       # RED
python 23_comprehensive/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 23_comprehensive/eval.py
```

## You finished

Twenty-three mechanisms, one loop, every one proven by a failing test you made pass. You didn't read about harness engineering — you built it, and measured it. **A measurable agent is all you need.**

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
