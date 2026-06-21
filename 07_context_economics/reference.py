"""
Lesson 07 - Context & Token Economics  (reference implementation)

The context window is finite and metered. When the conversation outgrows a
budget, compact it: keep the seed message and the most recent turns, replace
the middle with a short summary marker. estimate/total are given; you build
compact().
"""
from __future__ import annotations


def estimate_tokens(text) -> int:
    """Crude proxy: ~4 characters per token (real tokenizers vary)."""
    return max(1, len(str(text)) // 4)


def message_tokens(msg: dict) -> int:
    content = msg.get("content", "")
    if isinstance(content, str):
        return estimate_tokens(content)
    return sum(estimate_tokens(str(b)) for b in content)


def total_tokens(messages) -> int:
    return sum(message_tokens(m) for m in messages)


def compact(messages, budget: int, keep_recent: int = 2):
    """Shorten the conversation by dropping the MIDDLE.

    Strategy: keep messages[0] (the seed) and the last `keep_recent` turns,
    and replace the dropped middle with a short marker. Assumes keep_recent >= 1.

    NOTE: this is not real summarization — it inserts a placeholder marker, not
    an LLM-written summary of what it dropped. And it frees only the *middle*: a
    very large recent tail can still exceed `budget`. A production compactor would
    summarize the dropped span and trim/condense the tail too.
    """
    # Under budget, or too short to have a droppable middle -> leave untouched.
    if total_tokens(messages) <= budget or len(messages) <= keep_recent + 1:
        return list(messages)

    head = messages[:1]
    tail = messages[-keep_recent:]
    dropped = messages[1: len(messages) - keep_recent]
    summary = {
        "role": "user",
        "content": f"[compacted {len(dropped)} earlier messages to save context]",
    }
    return head + [summary] + tail
