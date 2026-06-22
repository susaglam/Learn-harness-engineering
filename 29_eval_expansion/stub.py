"""
Lesson 29 - Eval Expansion  (YOUR implementation)

Implement two production scorers over a trajectory (a list of event dicts):
  - matches_golden(traj, golden_tools): required tool sequence, in order.
  - within_budget(traj, max_steps, max_cost): stayed within budgets.

Run:  python 29_eval_expansion/eval.py     # RED until the TODOs are done
"""
from __future__ import annotations


def matches_golden(traj, golden_tools):
    # TODO(you): collect [e["name"] for e in traj if e["kind"]=="tool_call"], then
    # check golden_tools appears as an ORDERED SUBSEQUENCE (walk an index i over
    # golden_tools, advancing when the next call matches; True if i reaches the end).
    raise NotImplementedError("Implement matches_golden")


def within_budget(traj, max_steps=None, max_cost=None):
    # TODO(you): steps = number of tool_call events; cost = sum of e.get("cost",0).
    # Return False if (max_steps is not None and steps > max_steps) or
    # (max_cost is not None and cost > max_cost); otherwise True.
    raise NotImplementedError("Implement within_budget")
