# Lesson 18 — Cron / Self-Scheduling

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *The agent can wake itself.*

## The idea

So far the agent only acts when a human prompts it. **Cron** flips that: the agent schedules its own future work, and the harness fires those jobs when their time arrives — "every 30 seconds check for new work", "every morning audit the site". Each job carries an `interval` and a `next_run` timestamp. The scheduler's core question is **what's due now?**

A subtlety worth getting right: if the process was asleep and the clock jumped past several ticks, a fired job should **catch up** to the next *future* tick, not fire repeatedly for each missed one.

```python
jobs = [{"id": "heartbeat", "interval": 30, "next_run": 0}]
due(jobs, now=100)     # -> [heartbeat];  jobs[0]["next_run"] is now 120 (caught up)
```

> Time is passed *into* `due(jobs, now)` rather than read from the clock — that keeps the lesson deterministic and is also good design: an injectable clock is testable.

## Why this turns a tool into an assistant

This is the mechanism behind always-on agents: a heartbeat job wakes the agent to check a queue; cron jobs fire scheduled duties. Combined with background execution (Lesson 17) and task graphs (Lesson 16), the agent stops being "poke it and it moves" and becomes "it moves on its own."

## What you'll build

In [`stub.py`](./stub.py), implement `due(jobs, now)`:

1. For each job with `next_run <= now`, add it to `fired`.
2. Advance that job's `next_run` by its `interval` repeatedly **until it's in the future** (`> now`).
3. Return `fired`.

## Run it

```sh
python 18_cron_scheduler/eval.py                       # RED
python 18_cron_scheduler/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 18_cron_scheduler/eval.py
```

> **Toy → production:** jobs live in memory and vanish on restart. A durable scheduler persists them and uses leases (**Lesson 25**) so a crashed runner's job is reclaimed, not lost.

→ Next: **Lesson 19 — Agent Teams & Protocols** (*too big for one — coordinate many*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
