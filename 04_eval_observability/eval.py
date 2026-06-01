"""
Lesson 04 eval -- runs WITHOUT an API key.

Builds a synthetic trajectory and checks the scorers grade it correctly.
This is the course's own methodology, made into a lesson.

    python 04_eval_observability/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 04_eval_observability/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


def main():
    mod = load_lesson(HERE)

    traj = mod.Trajectory()
    traj.record("model_turn")
    traj.record("tool_call", name="bash", input={"command": "ls"})
    traj.record("tool_result", name="bash", content="a.txt\nb.txt")
    traj.record("tool_call", name="read_file", input={"path": "a.txt"})
    traj.record("final", text="Done. Found 2 files.")

    check("used_tool detects a tool that was called ('bash')",
          safe(lambda: mod.used_tool(traj, "bash")) is True, "expected True")
    check("used_tool detects 'read_file'",
          safe(lambda: mod.used_tool(traj, "read_file")) is True, "expected True")
    check("used_tool returns False for a tool never called",
          safe(lambda: mod.used_tool(traj, "network")) is False, "expected False")
    check("final_contains matches the final answer (case-insensitive)",
          safe(lambda: mod.final_contains(traj, "2 FILES")) is True, "expected True")
    check("final_contains is False for absent text",
          safe(lambda: mod.final_contains(traj, "error")) is False, "expected False")
    check("step_count counts tool calls (2)",
          safe(lambda: mod.step_count(traj)) == 2, "expected 2")

    report("Lesson 04 - Eval & Observability")


if __name__ == "__main__":
    main()
