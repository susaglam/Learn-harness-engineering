# Lesson 07 — Context & Token Economics

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Context is a budget; spend it deliberately.*

## The idea

The context window is finite, and every token costs money and latency. A long-running agent *will* fill it. So the harness needs a way to **make room without losing the thread**: compaction. The simplest effective strategy keeps the **seed** (the task/system framing) and the **most recent turns**, and replaces the stale middle with a short summary marker.

Token counting here uses a crude `~4 chars = 1 token` proxy so the lesson stays offline and deterministic; in production you'd use the model's real tokenizer and (crucially) prompt caching to avoid re-paying for stable prefixes.

```python
if total_tokens(messages) > budget:
    messages = compact(messages, budget, keep_recent=2)
```

## Why "seed + recent + summary"

- The **seed** holds the goal; lose it and the agent forgets what it's doing.
- **Recent turns** hold the live working state.
- The **middle** is usually safe to compress — its key facts, if they still matter, were carried forward into recent turns or should have been written to memory (Lesson 09).

## What you'll build

The token estimators are given. In [`stub.py`](./stub.py), implement `compact(messages, budget, keep_recent)`:

1. If under budget, return the list unchanged.
2. Else keep `messages[:1]` + a summary marker + `messages[-keep_recent:]`.

## Run it

```sh
python 07_context_economics/eval.py                       # RED
python 07_context_economics/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 07_context_economics/eval.py
```

> **Toy → production:** this drops the middle with a *marker*, not a real summary, and frees only the middle — a large recent tail can still exceed budget. Bounding big tool outputs is **Lesson 27**.

→ Next: **Lesson 08 — Subagents** (*delegate the noise, keep the signal*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
