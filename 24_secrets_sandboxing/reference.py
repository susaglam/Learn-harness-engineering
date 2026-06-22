"""
Lesson 24 - Secrets, Sandboxing & Audit  (reference implementation)

Never let a secret reach the model or a log. `redact()` masks both the secrets
you KNOW (passwords, values you injected) and secret-SHAPED tokens you don't
(API keys), so a leaked credential can't ride out in a prompt, a tool result,
or a trace. You build redact().
"""
from __future__ import annotations

import re

# Secret-shaped tokens we can catch even without knowing the value in advance.
_SECRET_PATTERNS = [
    r"sk-[A-Za-z0-9]{8,}",        # OpenAI/Anthropic-style API key
    r"ghp_[A-Za-z0-9]{20,}",      # GitHub personal access token
    r"AKIA[0-9A-Z]{16}",          # AWS access key id
]
MASK = "***REDACTED***"


def redact(text, known_secrets=()):
    """Return `text` with known secret values AND secret-shaped tokens masked."""
    out = str(text)
    for s in known_secrets:
        if s:
            out = out.replace(str(s), MASK)
    for pattern in _SECRET_PATTERNS:
        out = re.sub(pattern, MASK, out)
    return out
