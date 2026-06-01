"""
Lesson 23 - The Comprehensive Agent  (reference implementation)

The endpoint: one loop with every mechanism around it. This run wires together
- the agent loop          (Lesson 01)
- a tool registry/dispatch (Lesson 02)
- a permission gate        (Lesson 12)
- a trajectory tracer      (Lesson 04)
so that each tool call is permission-checked, dispatched, and recorded -- and a
denied call becomes recoverable feedback instead of an action. The pieces are
given; you build run_agent, the integration glue.
"""
from __future__ import annotations


class Registry:
    def __init__(self):
        self.handlers = {}
        self.schemas = []

    def add(self, name, fn, schema=None):
        self.handlers[name] = fn
        self.schemas.append({"name": name, **(schema or {})})

    def dispatch(self, name, inp):
        if name not in self.handlers:
            return f"ERROR: unknown tool '{name}'"
        try:
            return str(self.handlers[name](**inp))
        except Exception as exc:
            return f"ERROR: {exc}"


class Trajectory:
    def __init__(self):
        self.events = []

    def record(self, kind, **data):
        self.events.append({"kind": kind, **data})


def extract_text(resp):
    return "".join(getattr(b, "text", "") for b in resp.content
                   if getattr(b, "type", None) == "text")


def run_agent(client, model, messages, registry, permission, trace, max_turns=10):
    """One loop; permission-gate + dispatch + trace around every tool call."""
    last = None
    for _ in range(max_turns):
        last = client.messages.create(model=model, messages=messages,
                                      tools=registry.schemas, max_tokens=1024)
        trace.record("model_turn", stop=last.stop_reason)
        messages.append({"role": "assistant", "content": last.content})

        if last.stop_reason != "tool_use":
            trace.record("final", text=extract_text(last))
            return last

        results = []
        for b in last.content:
            if getattr(b, "type", None) == "tool_use":
                if permission(b.name, b.input) == "deny":
                    trace.record("denied", name=b.name)
                    out = f"DENIED: tool '{b.name}' is not permitted"
                else:
                    trace.record("tool_call", name=b.name, input=b.input)
                    out = registry.dispatch(b.name, b.input)
                results.append({"type": "tool_result", "tool_use_id": b.id, "content": out})
        messages.append({"role": "user", "content": results})
    return last
