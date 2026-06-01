"""
Lesson 04 - Eval & Observability  (YOUR implementation)

The Trajectory recorder is given. Implement the three SCORERS that grade a run.

Run:  python 04_eval_observability/eval.py     # RED until the TODOs are done
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Trajectory:
    events: list = field(default_factory=list)

    def record(self, kind: str, **data):
        self.events.append({"kind": kind, **data})
        return self


def used_tool(traj: Trajectory, name: str) -> bool:
    # TODO(you): True if any event is a "tool_call" with this tool name.
    raise NotImplementedError("Implement used_tool")


def final_contains(traj: Trajectory, substr: str) -> bool:
    # TODO(you): True if the last "final" event's text contains substr
    # (case-insensitive). False if there is no final event.
    raise NotImplementedError("Implement final_contains")


def step_count(traj: Trajectory) -> int:
    # TODO(you): how many "tool_call" events the trajectory contains.
    raise NotImplementedError("Implement step_count")
