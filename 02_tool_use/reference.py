"""
Lesson 02 - Tool Use  (reference implementation)

A dispatch map. Adding a tool = registering a schema + a handler.
The agent loop calls registry.dispatch(name, input) and never changes.
"""
from __future__ import annotations


class ToolRegistry:
    """Holds tool schemas (sent to the model) and handlers (run on dispatch)."""

    def __init__(self):
        self._schemas: list[dict] = []
        self.handlers: dict = {}

    def register(self, name: str, description: str, input_schema: dict):
        """Decorator: register a handler under `name` plus its schema."""

        def decorator(fn):
            self._schemas.append(
                {"name": name, "description": description, "input_schema": input_schema}
            )
            self.handlers[name] = fn
            return fn

        return decorator

    def schemas(self) -> list[dict]:
        """The tool schemas to pass to the model as `tools=`."""
        return list(self._schemas)

    def dispatch(self, name: str, tool_input: dict) -> str:
        """Route a tool_use to its handler; return its output as a string.

        Unknown tools and handler exceptions become ERROR strings (recoverable
        signal for the model) rather than crashing the loop.
        """
        if name not in self.handlers:
            return f"ERROR: unknown tool '{name}'"
        try:
            return str(self.handlers[name](**tool_input))
        except Exception as exc:
            return f"ERROR: {exc}"
