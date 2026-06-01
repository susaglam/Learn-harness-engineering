"""
Lesson 02 eval -- runs WITHOUT an API key.

Tests the dispatch map directly (no model needed): registering tools, routing
calls to handlers, and turning unknown-tool / handler errors into ERROR strings.

    python 02_tool_use/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 02_tool_use/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


def main():
    mod = load_lesson(HERE)
    reg = mod.ToolRegistry()

    @reg.register(
        "add",
        "Add two integers.",
        {
            "type": "object",
            "properties": {"a": {"type": "integer"}, "b": {"type": "integer"}},
            "required": ["a", "b"],
        },
    )
    def _add(a, b):
        return a + b

    @reg.register(
        "echo",
        "Echo text back.",
        {
            "type": "object",
            "properties": {"text": {"type": "string"}},
            "required": ["text"],
        },
    )
    def _echo(text):
        return text

    check("two tool schemas are registered", len(reg.schemas()) == 2,
          f"got {len(reg.schemas())}")
    check("schemas carry name + input_schema",
          all("name" in s and "input_schema" in s for s in reg.schemas()),
          "schema shape is wrong")
    check("dispatch routes 'add' to its handler",
          safe(lambda: reg.dispatch("add", {"a": 2, "b": 3})) == "5",
          "expected '5'")
    check("dispatch routes 'echo' to its handler",
          safe(lambda: reg.dispatch("echo", {"text": "hi"})) == "hi",
          "expected 'hi'")
    check("unknown tool returns an ERROR string (no crash)",
          str(safe(lambda: reg.dispatch("nope", {}))).startswith("ERROR"),
          "unknown tool should return 'ERROR: ...', not raise")
    check("a handler exception is caught and returned as ERROR",
          str(safe(lambda: reg.dispatch("add", {"a": 1}))).startswith("ERROR"),
          "missing argument should yield 'ERROR: ...', not raise")

    report("Lesson 02 - Tool Use")


if __name__ == "__main__":
    main()
