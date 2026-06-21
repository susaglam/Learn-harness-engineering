"""The canonical agent loop — the graduated version of Lesson 01.

`run_agent` is a reference implementation of the loop with the hardening the
lessons add (error-as-data, unknown-tool messages, edge guards). Lessons keep
their own loop bodies for pedagogy; this is the polished version to compare against.
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
    Raises:
        RuntimeError: if the model never stops within max_turns.
    """
    client = client or get_client()
    model = model or get_model()

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
                if block.name not in handlers:
                    output = f"ERROR: unknown tool '{block.name}'"  # clear recoverable signal
                else:
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

        if not results:
            # stop_reason was "tool_use" but the turn carried no tool_use block.
            # Posting {"role":"user","content":[]} is rejected by the real API, so
            # treat this as terminal instead.
            return last
        messages.append({"role": "user", "content": results})

    raise RuntimeError(f"agent did not finish within {max_turns} turns")
