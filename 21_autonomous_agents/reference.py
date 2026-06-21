"""
Lesson 21 - Autonomous Agents  (reference implementation)

No leader hands out work one by one. Agents watch a shared board and CLAIM the
next available task themselves. The critical property is no double-claim: a task
goes to exactly one agent. You build claim_next().
"""
from __future__ import annotations

import threading

# One lock makes the check-then-set atomic: without it, two threads can both pass
# the "is this task free?" test for the same task and double-claim it.
_claim_lock = threading.Lock()


def claim_next(board, agent_id):
    """Claim the first claimable task for `agent_id`.

    Claimable = status "pending" and no owner yet. On claim, set owner and flip
    status to "in_progress". Returns the claimed task, or None if none are free.
    The lock is what makes "no double-claim" hold when several threads call this
    at once.

    PRODUCTION NOTE: an in-process lock only guards threads in ONE process. Across
    processes or machines you need the equivalent atomicity from your store: a DB
    transaction / row lock, a compare-and-set, or a lease with a TTL so a crashed
    claimant's task is reclaimed.
    """
    with _claim_lock:
        for task in board:
            if task.get("status") == "pending" and not task.get("owner"):
                task["owner"] = agent_id
                task["status"] = "in_progress"
                return task
        return None
