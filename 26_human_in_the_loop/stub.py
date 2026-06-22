"""
Lesson 26 - Human-in-the-Loop  (YOUR implementation)

request_approval() and resolve() are given. Implement execute_if_approved():
the gate that runs an action only after a human approves it.

Run:  python 26_human_in_the_loop/eval.py     # RED until the TODO is done
"""
from __future__ import annotations


def request_approval(queue, action_id, action):
    queue[action_id] = {"id": action_id, "action": action, "status": "pending"}
    return queue[action_id]


def resolve(queue, action_id, decision):
    if action_id in queue:
        queue[action_id]["status"] = decision
    return queue.get(action_id)


def execute_if_approved(queue, action_id, run):
    # =========================================================================
    # TODO(you): look up the action's status in `queue`.
    #   - "approved" -> return run()        (only here may run() fire)
    #   - "denied"   -> return "DENIED"
    #   - otherwise (pending / unknown) -> return "PENDING"
    # Do NOT call run() unless the status is "approved".
    # =========================================================================
    raise NotImplementedError("Implement execute_if_approved - see the TODO above")
