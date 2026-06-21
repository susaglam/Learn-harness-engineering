"""
Lesson 21 - Autonomous Agents  (YOUR implementation)

Implement claim_next(board, agent_id): self-claim the next free task, marking it
owned and in_progress, so two agents never grab the same one.

Run:  python 21_autonomous_agents/eval.py     # RED until the TODO is done
"""
from __future__ import annotations

import threading

# Provided: wrap your check-then-set in this lock so concurrent callers can't
# both claim the same task.
_claim_lock = threading.Lock()


def claim_next(board, agent_id):
    # =========================================================================
    # TODO(you): make claiming ATOMIC, then scan.
    #   with _claim_lock:
    #       for task in board:
    #           if task is status "pending" AND has no "owner":
    #               set task["owner"] = agent_id and task["status"] = "in_progress"
    #               return task
    #       return None
    # The lock is what stops two threads from both passing the "is it free?"
    # check for the same task and double-claiming it.
    # =========================================================================
    raise NotImplementedError("Implement claim_next - see the TODO above")
