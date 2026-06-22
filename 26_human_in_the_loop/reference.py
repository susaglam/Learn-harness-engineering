"""
Lesson 26 - Human-in-the-Loop  (reference implementation)

Lesson 12 could 'ask', but nothing waited. Real high-stakes actions PAUSE for a
human: parked as pending, executed only on approval, dropped on denial. The
queue + resolve() are given; you build the gate that decides whether an action
may run yet.
"""
from __future__ import annotations


def request_approval(queue, action_id, action):
    """Park an action as pending human approval."""
    queue[action_id] = {"id": action_id, "action": action, "status": "pending"}
    return queue[action_id]


def resolve(queue, action_id, decision):
    """Record a human's decision: 'approved' or 'denied'."""
    if action_id in queue:
        queue[action_id]["status"] = decision
    return queue.get(action_id)


def execute_if_approved(queue, action_id, run):
    """Run the action ONLY if a human approved it.

    Returns run()'s result if approved, "DENIED" if denied, "PENDING" if still
    awaiting a decision (or unknown). run() must not fire in the last two cases.
    """
    rec = queue.get(action_id)
    status = rec["status"] if rec else "pending"
    if status == "approved":
        return run()
    if status == "denied":
        return "DENIED"
    return "PENDING"
