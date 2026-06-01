# Lesson 15 — Error Recovery

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Failure is a branch, not a dead end.*

## The idea

Real tools fail: networks time out, APIs rate-limit, files vanish, the model returns garbage. A naive harness crashes on the first error and loses the whole run. A robust one **classifies the failure and reacts**:

- **Transient** (timeout, rate limit, flaky network) → **retry**, maybe with backoff.
- **Permanent** (bad input, not found, auth denied) → don't waste retries; **fall back** (a default, a simpler path, or escalate to a human).

Recovery isn't an afterthought bolted on at the end — it's the difference between a demo and something you'd trust running unattended.

```python
value, info = run_with_recovery(call_api, fallback=use_cache, max_retries=3)
# info -> {"outcome": "ok", "attempts": 2}  or  {"outcome": "fallback", "reason": "permanent"}
```

## Why classify instead of "just retry everything"

Retrying a *permanent* error is pure waste — it will fail identically three more times while the user waits. Retrying a *transient* one is exactly right. The taxonomy is what lets the policy do the smart thing for each. Returning structured `info` (connecting to Lesson 04) makes the recovery itself observable.

## What you'll build

The `TransientError` / `PermanentError` taxonomy is given. In [`stub.py`](./stub.py), implement `run_with_recovery(fn, fallback, max_retries)`:

1. Loop `attempt` from 1 to `max_retries`; `try` returning `(fn(), {"outcome": "ok", "attempts": attempt})`.
2. On `TransientError`, `continue` (retry).
3. On `PermanentError`, return `(fallback(), {"outcome": "fallback", "reason": "permanent", "attempts": attempt})`.
4. If the loop exhausts, return `(fallback(), {"outcome": "fallback", "reason": "exhausted", "attempts": max_retries})`.

## Run it

```sh
python 15_error_recovery/eval.py                       # RED
python 15_error_recovery/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 15_error_recovery/eval.py
```

→ Next: **Lesson 16 — Task Graphs** (*big goals persist to disk as ordered tasks*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
