"""
Lesson 29 - Eval Expansion  (reference implementation)

Lesson 04 scored single facts about a run. Production grading needs more: did the
run hit the REQUIRED tool sequence (a "golden trajectory"), and did it stay
within step/cost BUDGETS? These two scorers turn "looks fine" into a gate you can
put in CI and a regression dashboard. You build both.
"""
from __future__ import annotations


def matches_golden(traj, golden_tools):
    """True if the run's tool_call names contain `golden_tools` as an ORDERED
    subsequence (the required tools happened, in order; extra calls are allowed)."""
    seq = [e["name"] for e in traj if e.get("kind") == "tool_call"]
    i = 0
    for name in seq:
        if i < len(golden_tools) and name == golden_tools[i]:
            i += 1
    return i == len(golden_tools)


def within_budget(traj, max_steps=None, max_cost=None):
    """True if the run stayed within the step and cost budgets (None = no limit)."""
    steps = sum(1 for e in traj if e.get("kind") == "tool_call")
    cost = sum(e.get("cost", 0) for e in traj)
    if max_steps is not None and steps > max_steps:
        return False
    if max_cost is not None and cost > max_cost:
        return False
    return True
