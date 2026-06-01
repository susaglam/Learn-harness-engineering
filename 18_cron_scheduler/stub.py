"""
Lesson 18 - Cron / Self-Scheduling  (YOUR implementation)

Implement due(jobs, now): return the jobs whose next_run has arrived, and
advance each fired job's next_run to the next future tick.

Run:  python 18_cron_scheduler/eval.py     # RED until the TODO is done
"""
from __future__ import annotations


def due(jobs, now):
    # =========================================================================
    # TODO(you):
    #   fired = []
    #   for j in jobs:
    #       if j["next_run"] <= now:
    #           fired.append(j)
    #           while j["next_run"] <= now:        # catch up if we missed ticks
    #               j["next_run"] += j["interval"]
    #   return fired
    # =========================================================================
    raise NotImplementedError("Implement due - see the TODO above")
