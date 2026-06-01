"""
Lesson 18 - Cron / Self-Scheduling  (reference implementation)

An agent that can schedule its own future work doesn't need a human to poke it.
Jobs carry an interval and a next_run time. `due(jobs, now)` returns the jobs
whose time has come and advances their next_run -- catching up if the clock
jumped past several ticks. (Time is passed IN so the lesson is deterministic.)
"""
from __future__ import annotations


def due(jobs, now):
    """Return jobs with next_run <= now; advance each fired job to its next future tick.

    A job is {"id": str, "interval": number, "next_run": number}. Mutates next_run.
    """
    fired = []
    for j in jobs:
        if j["next_run"] <= now:
            fired.append(j)
            while j["next_run"] <= now:        # catch up past long gaps
                j["next_run"] += j["interval"]
    return fired
