"""
Lesson 21 - Autonomous Agents  (reference implementation)

No leader hands out work one by one. Agents watch a shared board and CLAIM the
next available task themselves. The critical property is no double-claim: a task
goes to exactly one agent. You build claim_next().
"""
from __future__ import annotations


def claim_next(board, agent_id):
    """Claim the first claimable task for `agent_id`.

    Claimable = status "pending" and no owner yet. On claim, set owner and flip
    status to "in_progress". Returns the claimed task, or None if none are free.
    """
    for task in board:
        if task.get("status") == "pending" and not task.get("owner"):
            task["owner"] = agent_id
            task["status"] = "in_progress"
            return task
    return None
