"""
Lesson 21 - Autonomous Agents  (YOUR implementation)

Implement claim_next(board, agent_id): self-claim the next free task, marking it
owned and in_progress, so two agents never grab the same one.

Run:  python 21_autonomous_agents/eval.py     # RED until the TODO is done
"""
from __future__ import annotations


def claim_next(board, agent_id):
    # =========================================================================
    # TODO(you): scan board in order. The first task that is
    #     status == "pending" AND has no "owner"
    #   is claimable. Claim it: set task["owner"] = agent_id and
    #   task["status"] = "in_progress", then return that task.
    #   If nothing is claimable, return None.
    # =========================================================================
    raise NotImplementedError("Implement claim_next - see the TODO above")
