# Lesson 08 — Subagents

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Delegate the noise, keep the signal.*

## The idea

Some sub-tasks are noisy: searching a big tree, reading ten files, trying three approaches. If all that happens in the main conversation, the parent's context fills with intermediate junk and the important thread gets buried. A **subagent** solves this: spin up a *fresh* loop with only the sub-task, let it do its messy work in isolation, and return **only the final result** to the parent.

```python
summary = run_subagent("Find every TODO in src/ and summarize them",
                       client, model, tools, handlers)
# parent sees: the summary. parent does NOT see: 10 file reads + scratch work.
```

## Why fresh context is the whole point

Two wins, both about context (Lesson 07):

- **Isolation:** the subagent starts from just the task — not the parent's history — so it isn't distracted, and the parent isn't polluted by the subagent's steps.
- **Compression:** a 30-step investigation collapses into one paragraph in the parent. This is the cheapest, most powerful context-saver you have.

## What you'll build

The inner loop (`_run_loop`, the Lesson 01 loop) and `_extract_text` are given. In [`stub.py`](./stub.py), implement `run_subagent`:

1. Start a **fresh** conversation: `messages = [{"role": "user", "content": task}]` — do *not* pass the parent's history.
2. Run the loop to completion.
3. Return only `_extract_text(final)` — the result, not the noise.

## Run it

```sh
python 08_subagents/eval.py                       # RED
python 08_subagents/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 08_subagents/eval.py
```

→ Next: **Lesson 09 — Memory & Retrieval** (*remember what matters; retrieve when relevant*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
