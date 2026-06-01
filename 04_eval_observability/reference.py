"""
Lesson 04 - Eval & Observability  (reference implementation)

Observability = record everything the agent does as a *trajectory*.
Evaluation   = score that trajectory with pure functions.
You cannot improve what you cannot measure.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Trajectory:
    """An ordered log of agent events: model turns, tool calls, results, final."""

    events: list = field(default_factory=list)

    def record(self, kind: str, **data):
        self.events.append({"kind": kind, **data})
        return self


# --- Scorers: pure functions over a trajectory --------------------------------

def used_tool(traj: Trajectory, name: str) -> bool:
    return any(e.get("kind") == "tool_call" and e.get("name") == name
               for e in traj.events)


def final_contains(traj: Trajectory, substr: str) -> bool:
    finals = [e for e in traj.events if e.get("kind") == "final"]
    if not finals:
        return False
    return substr.lower() in str(finals[-1].get("text", "")).lower()


def step_count(traj: Trajectory) -> int:
    return sum(1 for e in traj.events if e.get("kind") == "tool_call")
