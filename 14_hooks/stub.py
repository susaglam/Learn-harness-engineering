"""
Lesson 14 - Hooks  (YOUR implementation)

HookBus is given. Implement call_tool_with_hooks: run pre-hooks (one may block),
then the handler, then post-hooks (each may transform the result).

Run:  python 14_hooks/eval.py     # RED until the TODO is done
"""
from __future__ import annotations


class HookBus:
    def __init__(self):
        self.pre = []
        self.post = []

    def on_pre(self, fn):
        self.pre.append(fn)
        return fn

    def on_post(self, fn):
        self.post.append(fn)
        return fn


def call_tool_with_hooks(bus: HookBus, name, tool_input, handler):
    # =========================================================================
    # TODO(you):
    #   1. Run each pre-hook: verdict = hook(name, tool_input).
    #      If verdict is a str starting with "deny", STOP and return
    #      f"BLOCKED: {verdict}" (do NOT run the handler).
    #   2. result = handler(**tool_input)
    #   3. Run each post-hook: result = hook(name, tool_input, result)
    #   4. return result
    # =========================================================================
    raise NotImplementedError("Implement call_tool_with_hooks - see the TODO above")
