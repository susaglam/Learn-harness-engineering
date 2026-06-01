"""
Lesson 01 — The Agent Loop  (YOUR implementation)

Implement the one step that makes an agent an agent: feeding tool results
back into the conversation so the model can continue.

Run:  python 01_agent_loop/eval.py     # RED until the TODO below is done
"""
from __future__ import annotations


def agent_loop(client, model, messages, tools, handlers, system="", max_turns=10):
    """Drive the model until it stops asking for tools.

    `client.messages.create(...)` returns a response object with:
        .content      a list of blocks; each block has .type
        .stop_reason  "tool_use" if the model wants tools, otherwise it's done
    A tool_use block has: .id (str), .name (str), .input (dict).
    """
    last = None
    for _ in range(max_turns):
        last = client.messages.create(
            model=model,
            system=system,
            messages=messages,
            tools=tools,
            max_tokens=1024,
        )
        messages.append({"role": "assistant", "content": last.content})

        if last.stop_reason != "tool_use":
            return last  # the model is done — return its final message

        # =====================================================================
        # TODO(you): the model asked to use one or more tools.
        #
        #   1. results = []
        #   2. for block in last.content:
        #          if getattr(block, "type", None) == "tool_use":
        #              output = handlers[block.name](**block.input)
        #              results.append({
        #                  "type": "tool_result",
        #                  "tool_use_id": block.id,
        #                  "content": str(output),
        #              })
        #   3. messages.append({"role": "user", "content": results})
        #
        # Without this, the loop can't continue and the eval stays RED.
        # Delete the line below once you've implemented the step.
        # =====================================================================
        raise NotImplementedError("Implement the tool-result step - see the TODO above")

    return last
