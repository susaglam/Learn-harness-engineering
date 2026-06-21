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

    # --- discriminating checks: a kind-blind / first-match scorer must go RED ---
    traj2 = mod.Trajectory()
    traj2.record("model_turn", text="note: the word ERROR appears in a NON-final event")
    traj2.record("final", text="All clear.")
    check("final_contains keys off the FINAL event, not just any event",
          safe(lambda: mod.final_contains(traj2, "ERROR")) is False,
          "scanned a non-final event's text")
    check("final_contains still finds text in the final event",
          safe(lambda: mod.final_contains(traj2, "clear")) is True, "expected True")

    traj3 = mod.Trajectory()
    traj3.record("final", text="first final")
    traj3.record("final", text="second final")
    check("final_contains uses the LAST final event when several exist",
          safe(lambda: mod.final_contains(traj3, "second")) is True
          and safe(lambda: mod.final_contains(traj3, "first")) is False,
          "did not use the last final event")

    empty = mod.Trajectory()
    check("final_contains is False when there is no final event",
          safe(lambda: mod.final_contains(empty, "anything")) is False, "expected False")
    check("used_tool is False on an empty trajectory",
          safe(lambda: mod.used_tool(empty, "bash")) is False, "expected False")
    check("step_count is 0 on an empty trajectory",
          safe(lambda: mod.step_count(empty)) == 0, "expected 0")

    report("Lesson 04 - Eval & Observability")


if __name__ == "__main__":
    main()
