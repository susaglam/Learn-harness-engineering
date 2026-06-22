"""
Lesson 24 - Secrets, Sandboxing & Audit  (YOUR implementation)

Implement redact(text, known_secrets): mask the secrets you were given AND any
secret-shaped token matching _SECRET_PATTERNS, returning the scrubbed text.

Run:  python 24_secrets_sandboxing/eval.py     # RED until the TODO is done
"""
from __future__ import annotations

import re

_SECRET_PATTERNS = [
    r"sk-[A-Za-z0-9]{8,}",
    r"ghp_[A-Za-z0-9]{20,}",
    r"AKIA[0-9A-Z]{16}",
]
MASK = "***REDACTED***"


def redact(text, known_secrets=()):
    # =========================================================================
    # TODO(you):
    #   out = str(text)
    #   1. For each value in known_secrets, replace it with MASK.
    #   2. For each pattern in _SECRET_PATTERNS, re.sub(pattern, MASK, out).
    #   Return out. (Both halves matter: known values AND unknown secret shapes.)
    # =========================================================================
    raise NotImplementedError("Implement redact - see the TODO above")
