"""
Lesson 18 eval -- runs WITHOUT an API key (and no real clock; `now` is passed in).

Checks firing, next_run advancement, catch-up past missed ticks, and that
nothing fires before its time.

    python 18_cron_scheduler/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 18_cron_scheduler/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


def _ids(jobs):
    return sorted(j["id"] for j in jobs) if isinstance(jobs, list) else None


def main():
    mod = load_lesson(HERE)

    jobsA = [{"id": "heartbeat", "interval": 30, "next_run": 0},
             {"id": "hourly", "interval": 3600, "next_run": 3600}]
    firedA = safe(lambda: mod.due(jobsA, 0))
    check("due returns a list", isinstance(firedA, list), repr(firedA)[:60])
    check("at now=0 the heartbeat fires but the hourly does not",
          _ids(firedA) == ["heartbeat"], f"got {_ids(firedA)}")
    check("a fired job's next_run advances by its interval (0 -> 30)",
          jobsA[0]["next_run"] == 30, f"next_run={jobsA[0]['next_run']}")

    jobsB = [{"id": "heartbeat", "interval": 30, "next_run": 0}]
    firedB = safe(lambda: mod.due(jobsB, 100))
    check("a job catches up PAST missed ticks (0 -> 120 at now=100)",
          isinstance(firedB, list) and len(firedB) == 1 and jobsB[0]["next_run"] == 120,
          f"next_run={jobsB[0]['next_run']}")

    jobsC = [{"id": "future", "interval": 30, "next_run": 200}]
    firedC = safe(lambda: mod.due(jobsC, 100))
    check("nothing fires before its time", isinstance(firedC, list) and firedC == [],
          repr(firedC)[:60])

    jobsD = [{"id": "hourly", "interval": 3600, "next_run": 3600}]
    firedD = safe(lambda: mod.due(jobsD, 3600))
    check("the hourly fires at its tick and reschedules (3600 -> 7200)",
          _ids(firedD) == ["hourly"] and jobsD[0]["next_run"] == 7200,
          f"next_run={jobsD[0]['next_run']}")

    report("Lesson 18 - Cron / Self-Scheduling")


if __name__ == "__main__":
    main()
