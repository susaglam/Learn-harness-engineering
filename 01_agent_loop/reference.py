"""
Lesson 01 — The Agent Loop  (reference implementation)

The complete loop plus a one-tool (bash) agent. Compare with your stub.py
after the eval is GREEN.

Run against a real model (needs ANTHROPIC_API_KEY in .env):
    python 01_agent_loop/reference.py
"""
from __future__ import annotations

import os
import subprocess
import sys

# Make the repo root importable so `harness` is found when run directly.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def agent_loop(client, model, messages, tools, handlers, system="", max_turns=10):
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
            return last

        results = []
        for block in last.content:
            if getattr(block, "type", None) == "tool_use":
                output = handlers[block.name](**block.input)
                results.append(
                    {
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(output),
                    }
                )
        messages.append({"role": "user", "content": results})

    return last


# --- A one-tool agent: bash. "One loop & bash is all you need to start." -----

def run_bash(command: str) -> str:
    try:
        proc = subprocess.run(
            command, shell=True, capture_output=True, text=True, timeout=30
        )
        return (proc.stdout + proc.stderr).strip() or "(no output)"
    except Exception as exc:
        return f"ERROR: {exc}"


TOOLS = [
    {
        "name": "bash",
        "description": "Run a shell command and return its combined stdout/stderr.",
        "input_schema": {
            "type": "object",
            "properties": {"command": {"type": "string"}},
            "required": ["command"],
        },
    }
]
HANDLERS = {"bash": run_bash}


def main():
    from harness.client import get_client, get_model

    client, model = get_client(), get_model()
    messages = [
        {
            "role": "user",
            "content": "Use bash to tell me the current directory and how many "
            "files it contains.",
        }
    ]
    final = agent_loop(client, model, messages, TOOLS, HANDLERS)
    text = "".join(
        b.text for b in final.content if getattr(b, "type", None) == "text"
    )
    print(text or "(no text in final message)")


if __name__ == "__main__":
    main()
