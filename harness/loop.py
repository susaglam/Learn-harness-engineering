"""The canonical agent loop — the graduated version of Lesson 01.

Lessons 2+ import `run_agent` from here instead of rewriting the loop.
It accepts an injectable `client`, so the same function works against a real
model or a scripted fake one in evals.
"""
from __future__ import annotations

from .client import get_client, get_model


def run_agent(
    messages,
    tools,
    handlers,
    system: str = "",
    *,
    client=None,
    model: str | None = None,
    max_turns: int = 50,
    max_tokens: int = 4096,
):
    """Run the loop until the model stops requesting tools.

    Args:
        messages:  the conversation so far (mutated in place).
        tools:     tool schemas passed to the model.
        handlers:  {tool_name: callable(**input) -> result}.
        system:    system prompt.
        client:    an Anthropic-compatible client; defaults to get_client().
        model:     model id; defaults to get_model().
    Returns:
        the final model response (stop_reason != "tool_use").
    """
    client = client or get_client()
    model = model or get_model()

    last = None
    for _ in range(max_turns):
        last = client.messages.create(
            model=model,
            system=system,
            messages=messages,
            tools=tools,
            max_tokens=max_tokens,
        )
        messages.append({"role": "assistant", "content": last.content})

        if last.stop_reason != "tool_use":
            return last

        results = []
        for block in last.content:
            if getattr(block, "type", None) == "tool_use":
                try:
                    output = handlers[block.name](**block.input)
                except Exception as exc:  # a tool error is recoverable signal
                    output = f"ERROR: {exc}"
                results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(output),
                    }
                )
        messages.append({"role": "user", "content": results})

    return last
