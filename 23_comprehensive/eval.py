"""
Lesson 23 eval -- runs WITHOUT an API key.

A scripted model requests two tools in one turn: an allowed 'write_file' and a
denied 'rm'. Checks the comprehensive loop permission-gates, dispatches, traces,
feeds results back, and terminates -- the whole harness, proven end to end.

    python 23_comprehensive/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 23_comprehensive/eval.py  # tests reference.py (GREEN)
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

    class _M:
        def __init__(self, o):
            self.o = o

        def create(self, *, model, messages, tools, max_tokens, **_):
            self.o.calls += 1
            if self.o.calls == 1:
                return SimpleNamespace(stop_reason="tool_use", content=[
                    _blk("tool_use", id="a1", name="write_file",
                         input={"path": "a.txt", "content": "hi"}),
                    _blk("tool_use", id="a2", name="rm", input={"path": "a.txt"}),
                ])
            return SimpleNamespace(stop_reason="end_turn", content=[_blk("text", text="Done.")])

    @property
    def messages(self):
        return FakeClient._M(self)


def main():
    mod = load_lesson(HERE)
    reg = mod.Registry()
    wf_calls, rm_calls = [], []
    reg.add("write_file", lambda path, content: wf_calls.append(path) or "wrote")
    reg.add("rm", lambda path: rm_calls.append(path) or "deleted")

    permission = lambda name, inp: "deny" if name == "rm" else "allow"
    trace = mod.Trajectory()
    client = FakeClient()
    messages = [{"role": "user", "content": "Write a.txt then delete it."}]

    final = safe(lambda: mod.run_agent(client, "fake", messages, reg, permission, trace))
    text = "".join(getattr(b, "text", "") for b in final.content
                   if getattr(b, "type", None) == "text") if hasattr(final, "content") else ""
    kinds = [e["kind"] for e in trace.events]

    check("the loop terminates with the model's final answer ('Done.')",
          "Done." in text, repr(text)[:50])
    check("the allowed tool (write_file) executed",
          wf_calls == ["a.txt"], f"wf_calls={wf_calls}")
    check("the denied tool (rm) was blocked while the allowed one ran",
          wf_calls == ["a.txt"] and rm_calls == [], f"rm_calls={rm_calls}")
    check("the trajectory recorded a tool_call and a denial",
          "tool_call" in kinds and "denied" in kinds, f"kinds={kinds}")
    check("the trajectory recorded the final answer",
          any(e["kind"] == "final" and "Done." in str(e.get("text", "")) for e in trace.events),
          f"kinds={kinds}")

    report("Lesson 23 - The Comprehensive Agent")


if __name__ == "__main__":
    main()
