"""
Lesson 07 - Context & Token Economics  (YOUR implementation)

The token estimators are given. Implement compact(): when the conversation is
over budget, keep the seed + recent turns and summarize the middle.

Run:  python 07_context_economics/eval.py     # RED until the TODO is done
"""
from __future__ import annotations


def estimate_tokens(text) -> int:
    return max(1, len(str(text)) // 4)


def message_tokens(msg: dict) -> int:
    content = msg.get("content", "")
    if isinstance(content, str):
        return estimate_tokens(content)
    return sum(estimate_tokens(str(b)) for b in content)


def total_tokens(messages) -> int:
    return sum(message_tokens(m) for m in messages)


def compact(messages, budget: int, keep_recent: int = 2):
    # =========================================================================
    # TODO(you):
    #   1. If total_tokens(messages) <= budget: return list(messages) unchanged.
    #   2. Otherwise:
    #        head    = messages[:1]                       # keep the seed
    #        tail    = messages[-keep_recent:]            # keep recent turns
    #        dropped = messages[1 : len(messages)-keep_recent]
    #        summary = {"role": "user",
    #                   "content": f"[compacted {len(dropped)} earlier messages to save context]"}
    #        return head + [summary] + tail
    # =========================================================================
    raise NotImplementedError("Implement compact - see the TODO above")
