# Lesson 25 — Concurrency & Leases

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *A claim you don't renew, you lose.*
>
> **Arc 7 — Production.** The production answer to Lesson 21's `Lock`.

## The idea

Lesson 21 made claiming atomic with an in-process `Lock`. That only guards
threads in **one** process. Real swarms run across processes and machines, where
a lock doesn't reach — and worse, an agent can **crash holding a claim**, parking
the task forever. The production primitive is a **lease**: a claim with an
**expiry (TTL)**. You hold the task only while your lease is live; you must renew
it to keep it; if you die, it expires and someone else reclaims the work.

```python
acquire(leases, "task-7", "A", now=0,  ttl=10)   # True  — A holds it until t=10
acquire(leases, "task-7", "B", now=5,  ttl=10)   # False — A's lease still live
acquire(leases, "task-7", "B", now=20, ttl=10)   # True  — A's lease expired; B reclaims
```

## Why expiry is the whole point

Without expiry, a crashed claimant's work is stuck (the L21 `Lock`/`owner` never
releases). The TTL turns "claimed" into "claimed *for now*", which is what makes a
distributed swarm self-heal. Real systems back this with a DB row + compare-and-set,
Redis `SET NX PX`, or a cloud lease API — but the semantics are exactly these.

## What you'll build

`is_held()` is given. In [`stub.py`](./stub.py), implement `acquire(leases, task_id, agent, now, ttl)`:

1. If a lease exists, is **unexpired** (`expires > now`), and belongs to a
   **different** agent → return `False`.
2. Otherwise record `{"agent": agent, "expires": now + ttl}` and return `True`.

## Run it

```sh
python 25_concurrency_leases/eval.py                       # RED
python 25_concurrency_leases/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 25_concurrency_leases/eval.py
```

→ Next: **Lesson 26 — Human-in-the-Loop** (*some actions wait for a human*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
