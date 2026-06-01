"""
Lesson 01 eval — runs WITHOUT an API key.

Drives YOUR agent_loop (from stub.py) with a scripted fake model and checks
that you feed tool results back so the loop can finish.

    python 01_agent_loop/eval.py
"""
from __future__ import annotations

import os
import sys
from types import SimpleNamespace

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)  # so `import harness.*` works when run directly

from harness.evals import check, load_lesson, report


# --- A scripted fake model: no network, fully deterministic ------------------

def _block(type_, **kw):
    return SimpleNamespace(type=type_, **kw)


class _FakeMessages:
    def __init__(self, outer):
        self.outer = outer

    def create(self, *, model, system, messages, tools, max_tokens, **_):
        self.outer.calls += 1
        if self.outer.calls == 1:
            # 1st turn: the model asks to run a tool.
            return SimpleNamespace(
                stop_reason="tool_use",
                content=[
                    _block(
                        "tool_use",
                        id="tu_1",
                        name="bash",
                        input={"command": "echo hello"},
                    )
                ],
            )
        # 2nd turn: inspect what the loop sent back, then finish.
        last_msg = messages[-1]
        if isinstance(last_msg, dict) and last_msg.get("role") == "user":
            for blk in last_msg.get("content", []) or []:
                if isinstance(blk, dict) and blk.get("type") == "tool_result":
                    self.outer.saw_tool_result = True
                    self.outer.tool_result_id = blk.get("tool_use_id")
                    self.outer.tool_result_content = str(blk.get("content", ""))
        return SimpleNamespace(
            stop_reason="end_turn",
            content=[_block("text", text="All done.")],
        )


class FakeClient:
    def __init__(self):
        self.calls = 0
        self.saw_tool_result = False
        self.tool_result_id = None
        self.tool_result_content = ""
        self.messages = _FakeMessages(self)


TOOLS = [
    {
        "name": "bash",
        "description": "Run a shell command.",
        "input_schema": {
            "type": "object",
            "properties": {"command": {"type": "string"}},
            "required": ["command"],
        },
    }
]


def main():
    stub = load_lesson(HERE)

    handler_calls = []

    def fake_bash(command):
        handler_calls.append(command)
        return f"ran: {command}"

    client = FakeClient()
    messages = [{"role": "user", "content": "Say hello via bash, then finish."}]

    final = None
    error = ""
    try:
        final = stub.agent_loop(
            client, "fake-model", messages, TOOLS, {"bash": fake_bash}
        )
    except NotImplementedError as exc:
        error = f"the TODO in stub.py is not implemented yet ({exc})"
    except Exception as exc:  # noqa: BLE001 - surface any learner bug
        error = f"{type(exc).__name__}: {exc}"

    check("loop runs without raising (you implemented the TODO)", final is not None, error)
    check(
        "the bash handler was actually invoked",
        bool(handler_calls),
        "handlers[name](**block.input) was never called",
    )
    check(
        "the command from the model reached the handler",
        handler_calls == ["echo hello"],
        f"got {handler_calls!r}, expected ['echo hello']",
    )
    check(
        "a tool_result was fed back to the model",
        client.saw_tool_result,
        "no user message with a tool_result block before the 2nd model call",
    )
    check(
        "the tool_result references the correct tool_use id",
        client.tool_result_id == "tu_1",
        f"got tool_use_id={client.tool_result_id!r}, expected 'tu_1'",
    )
    check(
        "the loop terminated and returned the model's final text",
        bool(final)
        and any(getattr(b, "type", None) == "text" for b in final.content),
        "loop did not return a final assistant message with text",
    )

    report("Lesson 01 - The Agent Loop")


if __name__ == "__main__":
    main()
