"""
Lesson 08 - Subagents  (YOUR implementation)

The inner loop and text extractor are given. Implement run_subagent: the
fresh-context-in, result-only-out wrapper.

Run:  python 08_subagents/eval.py     # RED until the TODO is done
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
    # =========================================================================
    # TODO(you):
    #   1. Start a FRESH conversation: messages = [{"role":"user","content":task}]
    #      (do NOT pass the parent's history -- that is the whole point).
    #   2. final = _run_loop(messages, client, model, tools, handlers, system, max_turns)
    #   3. return _extract_text(final)   # only the result goes back to the parent
    # =========================================================================
    raise NotImplementedError("Implement run_subagent - see the TODO above")
