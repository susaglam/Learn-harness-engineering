"""
Lesson 12 - Permissions & Trust  (YOUR implementation)

Rule is given. Implement resolve(): first matching rule wins, else default.

Run:  python 12_permissions/eval.py     # RED until the TODO is done
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional

ALLOW, ASK, DENY = "allow", "ask", "deny"


@dataclass
class Rule:
    tool: str
    decision: str
    when: Optional[Callable[[dict], bool]] = None


def resolve(tool_name: str, tool_input: dict, rules, default: str = ASK) -> str:
    # =========================================================================
    # TODO(you): walk `rules` IN ORDER. A rule matches when:
    #     r.tool == tool_name OR r.tool == "*"        (name matches)
    #   AND (r.when is None OR r.when(tool_input))     (predicate passes)
    # Return the first matching rule's .decision. If none match, return default.
    # =========================================================================
    raise NotImplementedError("Implement resolve - see the TODO above")
