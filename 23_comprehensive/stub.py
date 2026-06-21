"""
Lesson 23 - The Comprehensive Agent  (YOUR implementation)

Registry, Trajectory, and extract_text are given. Implement run_agent: the loop
that ties a permission gate + dispatch + trace around every tool call.

Run:  python 23_comprehensive/eval.py     # RED until the TODO is done
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
    # =========================================================================
    # TODO(you): the comprehensive loop. Each turn:
    #   1. resp = client.messages.create(model=model, messages=messages,
    #             tools=registry.schemas, max_tokens=1024)
    #   2. trace.record("model_turn", stop=resp.stop_reason)
    #      messages.append({"role":"assistant","content":resp.content})
    #   3. if resp.stop_reason != "tool_use":
    #          trace.record("final", text=extract_text(resp)); return resp
    #   4. For each tool_use block b, branch on permission(b.name, b.input):
    #        - "allow": trace.record("tool_call", ...); out = registry.dispatch(...)
    #        - "deny":  trace.record("denied", name=b.name)
    #                   out = f"DENIED: tool '{b.name}' is not permitted"
    #        - else ("ask"): trace.record("ask", name=b.name)
    #                   out = f"ASK: tool '{b.name}' needs human approval (not executed)"
    #        - collect {"type":"tool_result","tool_use_id":b.id,"content":out}
    #   5. messages.append({"role":"user","content":results})
    #   6. After the loop (turn budget hit): trace.record("exhausted", turns=max_turns)
    # =========================================================================
    raise NotImplementedError("Implement run_agent - see the TODO above")
