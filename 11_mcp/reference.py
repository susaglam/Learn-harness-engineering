"""
Lesson 11 - MCP  (reference implementation)

MCP (Model Context Protocol) lets you plug an external server's tools into your
agent. The harness trick: register each advertised tool into the SAME registry
the loop already dispatches through, so MCP tools and native tools live in one
pool. ToolRegistry is given; you build mount_mcp_server().
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
    """Register every tool the MCP `server` advertises into `registry`.

    `server` exposes:  list_tools() -> [{name, description, input_schema}, ...]
                       call_tool(name, args_dict) -> result
    Each tool becomes a registry handler that forwards to server.call_tool.
    `prefix` namespaces tool names to avoid collisions across servers.
    """
    for spec in server.list_tools():
        original = spec["name"]

        def make_handler(tool_name):
            # bind tool_name now (closure-safe) so all handlers don't share the last one
            return lambda **kwargs: server.call_tool(tool_name, kwargs)

        registry.register(
            f"{prefix}{original}",
            spec.get("description", ""),
            spec.get("input_schema", {}),
            make_handler(original),
        )
    return registry
