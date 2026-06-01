"""
Lesson 12 - Permissions & Trust  (reference implementation)

Before a tool runs, resolve it against an ordered list of rules into one of
three decisions: allow / ask / deny. First matching rule wins; if none match,
a default applies. Rule is given; you build resolve().
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional

ALLOW, ASK, DENY = "allow", "ask", "deny"


@dataclass
class Rule:
    tool: str                                          # tool name, or "*" for any
    decision: str                                      # allow | ask | deny
    when: Optional[Callable[[dict], bool]] = None      # extra predicate on the input


def resolve(tool_name: str, tool_input: dict, rules, default: str = ASK) -> str:
    """Return the decision of the first matching rule, else `default`."""
    for r in rules:
        if r.tool in (tool_name, "*") and (r.when is None or r.when(tool_input)):
            return r.decision
    return default
