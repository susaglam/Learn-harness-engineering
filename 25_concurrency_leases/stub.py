"""
Lesson 25 - Concurrency & Leases  (YOUR implementation)

is_held() is given. Implement acquire(): grant a lease if the task is free OR
the previous lease has expired; refuse if another agent's lease is still live.

Run:  python 25_concurrency_leases/eval.py     # RED until the TODO is done
"""
from __future__ import annotations


def acquire(leases, task_id, agent, now, ttl):
    # =========================================================================
    # TODO(you):
    #   held = leases.get(task_id)
    #   If held exists AND held["expires"] > now AND held["agent"] != agent:
    #       return False                         # someone else holds a LIVE lease
    #   leases[task_id] = {"agent": agent, "expires": now + ttl}
    #   return True
    # The expiry check is what lets a crashed agent's task be reclaimed.
    # =========================================================================
    raise NotImplementedError("Implement acquire - see the TODO above")


def is_held(leases, task_id, now):
    held = leases.get(task_id)
    return held is not None and held["expires"] > now
