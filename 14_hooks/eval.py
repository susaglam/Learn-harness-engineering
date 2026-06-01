"""
Lesson 14 eval -- runs WITHOUT an API key.

A pre-hook blocks calls whose input contains "secret"; a post-hook upper-cases
results. Checks hooks fire, transform, and that a blocking pre-hook stops the
handler from running.

    python 14_hooks/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 14_hooks/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


def main():
    mod = load_lesson(HERE)
    bus = mod.HookBus()
    log = []
    handler_calls = []

    @bus.on_pre
    def guard(name, inp):
        log.append(("pre", name))
        if "secret" in str(inp):
            return "deny:contains secret"

    @bus.on_post
    def shout(name, inp, result):
        log.append(("post", name))
        return str(result).upper()

    def echo(text):
        handler_calls.append(text)
        return f"echo:{text}"

    allowed = safe(lambda: mod.call_tool_with_hooks(bus, "echo", {"text": "hi"}, echo))
    blocked = safe(lambda: mod.call_tool_with_hooks(bus, "echo", {"text": "secret"}, echo))

    check("allowed call runs and the post-hook transforms the result",
          allowed == "ECHO:HI", repr(allowed)[:60])
    check("pre-hook fired for the allowed call",
          ("pre", "echo") in log, f"log={log}")
    check("blocking pre-hook returns a BLOCKED result",
          isinstance(blocked, str) and blocked.startswith("BLOCKED"), repr(blocked)[:60])
    check("a blocked call never runs the handler",
          handler_calls == ["hi"], f"handler_calls={handler_calls}")
    check("post-hook ran only for the allowed call (not the blocked one)",
          log.count(("post", "echo")) == 1, f"post count={log.count(('post','echo'))}")

    report("Lesson 14 - Hooks")


if __name__ == "__main__":
    main()
