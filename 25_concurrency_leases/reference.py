"""
Lesson 25 - Concurrency & Leases  (reference implementation)

Lesson 21's in-process Lock guards threads in ONE process. Across processes or
machines you need a LEASE: a claim with an expiry. An agent holds a task only
until its lease runs out; if it crashes, the lease expires and someone else can
reclaim the work. is_held() is given; you build acquire().
"""
from __future__ import annotations


def acquire(leases, task_id, agent, now, ttl):
    """Grant `agent` a lease on `task_id` if it's free or the prior lease expired.

    leases: dict task_id -> {"agent": str, "expires": number}.
    Returns True and records/renews the lease, or False if another agent holds
    an unexpired lease. (Time is passed in, so the lesson stays deterministic.)
    """
    held = leases.get(task_id)
    if held is not None and held["expires"] > now and held["agent"] != agent:
        return False                      # another agent holds a live lease
    leases[task_id] = {"agent": agent, "expires": now + ttl}
    return True


def is_held(leases, task_id, now):
    """True if task_id has a lease that hasn't expired as of `now`."""
    held = leases.get(task_id)
    return held is not None and held["expires"] > now
