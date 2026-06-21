"""
Lesson 15 - Error Recovery  (YOUR implementation)

The error taxonomy is given. Implement run_with_recovery: retry transient
failures, fall back on permanent ones (or when retries run out).

Run:  python 15_error_recovery/eval.py     # RED until the TODO is done
"""
from __future__ import annotations


class TransientError(Exception):
    """Retry me (timeout, rate limit, flaky network)."""


class PermanentError(Exception):
    """Don't retry me (bad input, not found, auth) -- fall back instead."""


def run_with_recovery(fn, fallback, max_retries: int = 3):
    # =========================================================================
    # TODO(you): loop attempt = 1..max_retries:
    #   try:    return fn(), {"outcome": "ok", "attempts": attempt}
    #   except TransientError:  continue        # retry
    #   except PermanentError:  return fallback(), {"outcome":"fallback",
    #                                   "reason":"permanent","attempts":attempt}
    #   except Exception:       return fallback(), {"outcome":"fallback",
    #                                   "reason":"unclassified","attempts":attempt}
    # If the loop finishes without success:
    #   return fallback(), {"outcome":"fallback","reason":"exhausted",
    #                       "attempts": max_retries}
    # =========================================================================
    raise NotImplementedError("Implement run_with_recovery - see the TODO above")
