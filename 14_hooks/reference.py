"""
Lesson 14 - Hooks  (reference implementation)

Hooks are extension points AROUND the loop, so you can add behavior (logging,
guards, redaction) without editing the loop. A PreToolUse hook can block a call;
a PostToolUse hook can transform its result. HookBus is given; you build the
hooked tool-call.
"""
from __future__ import annotations


class HookBus:
    def __init__(self):
        self.pre = []    # fn(name, tool_input) -> None | "deny:reason"
        self.post = []   # fn(name, tool_input, result) -> result (possibly transformed)

    def on_pre(self, fn):
        self.pre.append(fn)
        return fn

    def on_post(self, fn):
        self.post.append(fn)
        return fn


def call_tool_with_hooks(bus: HookBus, name, tool_input, handler):
    """Pre-hooks (may block) -> handler -> post-hooks (may transform)."""
    for hook in bus.pre:
        verdict = hook(name, tool_input)
        if isinstance(verdict, str) and verdict.startswith("deny"):
            return f"BLOCKED: {verdict}"
    result = handler(**tool_input)
    for hook in bus.post:
        result = hook(name, tool_input, result)
    return result
