"""
Lesson 11 - MCP  (YOUR implementation)

ToolRegistry is given. Implement mount_mcp_server: register each tool an MCP
server advertises into the registry, so MCP tools join the same pool the loop
dispatches through.

Run:  python 11_mcp/eval.py     # RED until the TODO is done
"""
from __future__ import annotations


class ToolRegistry:
    def __init__(self):
        self._schemas: list[dict] = []
        self.handlers: dict = {}

    def register(self, name, description, input_schema, handler):
        self._schemas.append(
            {"name": name, "description": description, "input_schema": input_schema}
        )
        self.handlers[name] = handler

    def schemas(self):
        return list(self._schemas)

    def dispatch(self, name, tool_input):
        if name not in self.handlers:
            return f"ERROR: unknown tool '{name}'"
        try:
            return str(self.handlers[name](**tool_input))
        except Exception as exc:
            return f"ERROR: {exc}"


def mount_mcp_server(registry: ToolRegistry, server, prefix: str = ""):
    # =========================================================================
    # TODO(you): for each spec in server.list_tools():
    #   - original = spec["name"]
    #   - build a handler that forwards to server.call_tool(original, kwargs).
    #     IMPORTANT: bind `original` per-iteration (a def/factory or default arg),
    #     or every handler will capture the LAST tool name (classic closure bug).
    #   - registry.register(f"{prefix}{original}", spec.get("description",""),
    #                       spec.get("input_schema",{}), handler)
    # Return registry.
    # =========================================================================
    raise NotImplementedError("Implement mount_mcp_server - see the TODO above")
