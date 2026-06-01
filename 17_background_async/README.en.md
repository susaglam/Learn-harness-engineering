# Lesson 17 — Background & Async

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Slow work goes async; the agent keeps thinking.*

## The idea

Some tool calls are slow: a multi-minute build, a big download, a long test suite. If the loop blocks on them, the agent sits frozen and you burn wall-clock. The fix: run slow work on a **background thread**, return a handle *immediately*, and deliver a **notification** when it finishes. The agent keeps reasoning (or starts other work) and picks up the result when it's ready.

```python
runner.start("build", run_build)     # returns at once, build runs in the background
# ...agent does other things...
for note in runner.drain():          # collect finished jobs
    handle(note["id"], note["result"])
```

## Why a notification queue

The background job and the main loop run concurrently, so you need a safe handoff: a thread-safe **queue** the worker posts results into and the loop drains. Capturing exceptions as `ERROR: ...` results (instead of letting a thread die silently) keeps failures *observable* (Lesson 04) and *recoverable* (Lesson 15) — a crashed worker that posts nothing is the worst outcome.

## What you'll build

`drain()` (join + collect) is given. In [`stub.py`](./stub.py), implement `start(job_id, fn)`:

1. Define `run()` that calls `fn()` in try/except (`result = value` or `f"ERROR: {exc}"`) and `put`s `{"id": job_id, "result": result}` onto `self.notifications`.
2. Start a **daemon** thread on `run`, append it to `self._threads`, and return `job_id` immediately.

## Run it

```sh
python 17_background_async/eval.py                       # RED
python 17_background_async/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 17_background_async/eval.py
```

→ Next: **Lesson 18 — Cron / Self-Scheduling** (*the agent can wake itself*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
