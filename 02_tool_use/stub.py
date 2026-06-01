"""
Lesson 02 - Tool Use  (YOUR implementation)

Implement ToolRegistry.dispatch: route a tool name to its handler, run it,
and return the output as a string -- turning errors into ERROR strings instead
of crashes.

Run:  python 02_tool_use/eval.py     # RED until the TODO is done
"""
from __future__ import annotations


class ToolRegistry:
    def __init__(self):
        self._schemas: list[dict] = []
        self.handlers: dict = {}

    def register(self, name: str, description: str, input_schema: dict):
        def decorator(fn):
            self._schemas.append(
                {"name": name, "description": description, "input_schema": input_schema}
            )
            self.handlers[name] = fn
            return fn

        return decorator

    def schemas(self) -> list[dict]:
        return list(self._schemas)

    def dispatch(self, name: str, tool_input: dict) -> str:
        # =====================================================================
        # TODO(you): route the call to its handler.
        #   1. If `name` is not in self.handlers -> return f"ERROR: unknown tool '{name}'"
        #   2. Otherwise call self.handlers[name](**tool_input), wrapped in
        #      try/except, returning str(result) on success or f"ERROR: {exc}"
        #      on failure (so a tool bug is recoverable signal, not a crash).
        # =====================================================================
        raise NotImplementedError("Implement ToolRegistry.dispatch - see the TODO above")
