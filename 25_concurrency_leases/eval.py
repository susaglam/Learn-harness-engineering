"""
Lesson 25 eval -- runs WITHOUT an API key (time is passed in; deterministic).

A holds a lease; B is refused while it's live, then reclaims after expiry. An
acquire that ignores expiry (always grants) or never reclaims (grants only if
absent) fails.

    python 25_concurrency_leases/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 25_concurrency_leases/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


def main():
    mod = load_lesson(HERE)
    leases = {}

    a = safe(lambda: mod.acquire(leases, "t", "A", now=0, ttl=10))
    b_live = safe(lambda: mod.acquire(leases, "t", "B", now=5, ttl=10))   # A live till 10
    b_reclaim = safe(lambda: mod.acquire(leases, "t", "B", now=20, ttl=10))  # A expired

    check("A acquires a free lease", a is True, repr(a))
    check("B is REFUSED while A's lease is still live (expiry respected)",
          b_live is False, repr(b_live))
    check("B RECLAIMS the task after A's lease expires", b_reclaim is True, repr(b_reclaim))
    check("after reclaim the owner is B until its own expiry",
          leases.get("t", {}).get("agent") == "B"
          and leases.get("t", {}).get("expires") == 30,
          repr(leases.get("t")))
    check("is_held reflects expiry (B's lease is gone by t=100)",
          safe(lambda: mod.is_held(leases, "t", 100)) is False, "expected expired")

    report("Lesson 25 - Concurrency & Leases")


if __name__ == "__main__":
    main()
