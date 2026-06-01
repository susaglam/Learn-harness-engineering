"""
Lesson 15 eval -- runs WITHOUT an API key.

Three scenarios: transient-then-success, permanent-error, and exhausted-retries.
Checks the policy retries the right kind, falls back on the rest, and reports
what happened.

    python 15_error_recovery/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 15_error_recovery/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


class Flaky:
    """Raises `exc` for the first `fails` calls, then returns 'SUCCESS'."""

    def __init__(self, fails, exc):
        self.calls = 0
        self.fails = fails
        self.exc = exc

    def __call__(self):
        self.calls += 1
        if self.calls <= self.fails:
            raise self.exc("boom")
        return "SUCCESS"


def main():
    mod = load_lesson(HERE)
    T, P = mod.TransientError, mod.PermanentError
    fb = lambda: "FALLBACK"

    f1 = Flaky(2, T)                              # 2 transient failures, then OK
    r1 = safe(lambda: mod.run_with_recovery(f1, fb, max_retries=3))
    ok1 = isinstance(r1, tuple) and len(r1) == 2

    f2 = Flaky(99, P)                             # permanent on first call
    r2 = safe(lambda: mod.run_with_recovery(f2, fb, max_retries=3))
    ok2 = isinstance(r2, tuple) and len(r2) == 2

    f3 = Flaky(99, T)                             # always transient -> exhaust
    r3 = safe(lambda: mod.run_with_recovery(f3, fb, max_retries=3))
    ok3 = isinstance(r3, tuple) and len(r3) == 2

    check("transient-then-success ultimately succeeds",
          ok1 and r1[0] == "SUCCESS" and r1[1].get("outcome") == "ok", repr(r1)[:80])
    check("it retried until success (3 attempts)",
          ok1 and r1[1].get("attempts") == 3 and f1.calls == 3, f"calls={f1.calls}")
    check("a permanent error falls back immediately (1 call, reason 'permanent')",
          ok2 and r2[0] == "FALLBACK" and r2[1].get("reason") == "permanent"
          and f2.calls == 1, repr(r2)[:80] + f" calls={f2.calls}")
    check("exhausted retries fall back (reason 'exhausted')",
          ok3 and r3[0] == "FALLBACK" and r3[1].get("reason") == "exhausted", repr(r3)[:80])
    check("exhaustion tried exactly max_retries times",
          ok3 and f3.calls == 3, f"calls={f3.calls}")

    report("Lesson 15 - Error Recovery")


if __name__ == "__main__":
    main()
