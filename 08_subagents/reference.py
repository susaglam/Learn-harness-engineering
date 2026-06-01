"""
Lesson 08 - Subagents  (reference implementation)

A subagent does side work in a FRESH, isolated context and returns ONLY its
final result to the parent. The parent's context stays clean: it never sees the
subagent's intermediate tool calls and noise -- just the answer.

The inner loop (_run_loop) is the Lesson 01 loop, given here. You build the
subagent wrapper.
"""
from __future__ import annotations


def _extract_text(resp) -> str:
    if resp is None:
        return ""
    return "".join(getattr(b, "text", "") for b in resp.content
                   if getattr(b, "type", None) == "text")


def _run_loop(messages, client, model, tools, handlers, system, max_turns):
    last = None
    for _ in range(max_turns):
        last = client.messages.create(model=model, system=system, messages=messages,
                                      tools=tools, max_tokens=1024)
        messages.append({"role": "assistant", "content": last.content})
        if last.stop_reason != "tool_use":
            return last
        results = []
        for b in last.content:
            if getattr(b, "type", None) == "tool_use":
                results.append({"type": "tool_result", "tool_use_id": b.id,
                                "content": str(handlers[b.name](**b.input))})
        messages.append({"role": "user", "content": results})
    return last


def run_subagent(task, client, model, tools, handlers, system="", max_turns=10) -> str:
    """Run `task` in a fresh context; return only the final text."""
    messages = [{"role": "user", "content": task}]   # fresh, isolated context
    final = _run_loop(messages, client, model, tools, handlers, system, max_turns)
    return _extract_text(final)                       # only the result crosses back
