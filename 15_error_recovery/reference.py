"""
Lesson 15 - Error Recovery  (reference implementation)

Failures come in kinds. A TRANSIENT error (timeout, rate limit) deserves a
retry; a PERMANENT error (bad request, not found) should fall back immediately.
Classifying, then retrying-or-falling-back, keeps an agent alive through the
messiness of the real world. The error classes are given; you build the policy.
"""
from __future__ import annotations


class TransientError(Exception):
    """Retry me (timeout, rate limit, flaky network)."""


class PermanentError(Exception):
    """Don't retry me (bad input, not found, auth) -- fall back instead."""


def run_with_recovery(fn, fallback, max_retries: int = 3):
    """Run fn(); retry on TransientError up to max_retries; on PermanentError or
    exhausted retries, use fallback(). Returns (value, info)."""
    for attempt in range(1, max_retries + 1):
        try:
            return fn(), {"outcome": "ok", "attempts": attempt}
        except TransientError:
            continue
        except PermanentError:
            return fallback(), {"outcome": "fallback", "reason": "permanent",
                                "attempts": attempt}
        except Exception:
            # Unknown / out-of-taxonomy error: don't retry blindly. Fall back
            # (safe default) so an unclassified exception can't crash the loop
            # the lesson promises to keep alive.
            return fallback(), {"outcome": "fallback", "reason": "unclassified",
                                "attempts": attempt}
    return fallback(), {"outcome": "fallback", "reason": "exhausted",
                        "attempts": max_retries}
