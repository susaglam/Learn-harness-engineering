"""
Lesson 08 eval -- runs WITHOUT an API key.

A scripted subagent calls a tool then answers. Checks the subagent runs in a
fresh context (only the task), executes its tool, and returns ONLY the final
text -- not the intermediate tool output.

    python 08_subagents/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 08_subagents/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys
from types import SimpleNamespace

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


def _blk(t, **kw):
    return SimpleNamespace(type=t, **kw)


class FakeClient:
    def __init__(self):
        self.calls = 0
        self.first_messages = None

    class _M:
        def __init__(self, o):
            self.o = o

        def create(self, *, model, system, messages, tools, max_tokens, **_):
            self.o.calls += 1
            if self.o.calls == 1:
                self.o.first_messages = [dict(m) for m in messages]
                return SimpleNamespace(stop_reason="tool_use", content=[
                    _blk("tool_use", id="t1", name="compute", input={"x": 21})])
            return SimpleNamespace(stop_reason="end_turn", content=[
                _blk("text", text="Subtask done: 42.")])

    @property
    def messages(self):
        return FakeClient._M(self)


def main():
    mod = load_lesson(HERE)
    calls = []

    def compute(x):
        calls.append(x)
        return "RAW_TOOL_OUTPUT 42"

    client = FakeClient()
    tools = [{"name": "compute", "description": "double x",
              "input_schema": {"type": "object", "properties": {"x": {"type": "integer"}}}}]

    result = safe(lambda: mod.run_subagent("Double 21.", client, "fake", tools,
                                           {"compute": compute}))

    check("run_subagent returns a string", isinstance(result, str)
          and not result.startswith("__RAISED__"), repr(result)[:80])
    check("returns the subagent's final answer",
          isinstance(result, str) and "42" in result and "done" in result.lower(),
          repr(result)[:80])
    check("subagent started in a FRESH context (only the task)",
          client.first_messages is not None and len(client.first_messages) == 1
          and client.first_messages[0].get("content") == "Double 21.",
          repr(client.first_messages)[:90])
    check("the subagent executed its tool", calls == [21], f"calls={calls}")
    check("intermediate tool output did NOT leak to the parent",
          isinstance(result, str) and "RAW_TOOL_OUTPUT" not in result,
          "only the final text should cross back")

    report("Lesson 08 - Subagents")


if __name__ == "__main__":
    main()
