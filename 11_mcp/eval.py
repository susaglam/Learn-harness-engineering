"""
Lesson 11 eval -- runs WITHOUT an API key (and no real MCP server).

A fake in-process MCP server advertises two tools. Checks they get mounted into
the registry, namespaced by prefix, and that dispatching forwards to the server
with the ORIGINAL tool name -- including the closure-binding detail.

    python 11_mcp/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 11_mcp/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


class FakeMCPServer:
    def __init__(self):
        self.calls = []

    def list_tools(self):
        return [
            {"name": "get_weather", "description": "Get weather",
             "input_schema": {"type": "object", "properties": {"city": {"type": "string"}}}},
            {"name": "get_time", "description": "Get time",
             "input_schema": {"type": "object", "properties": {"tz": {"type": "string"}}}},
        ]

    def call_tool(self, name, args):
        self.calls.append((name, args))
        return f"{name} -> {args}"


def main():
    mod = load_lesson(HERE)
    reg = mod.ToolRegistry()
    server = FakeMCPServer()

    safe(lambda: mod.mount_mcp_server(reg, server, prefix="mcp_"))

    names = [s["name"] for s in reg.schemas()]
    w = safe(lambda: reg.dispatch("mcp_get_weather", {"city": "Paris"}))
    t = safe(lambda: reg.dispatch("mcp_get_time", {"tz": "UTC"}))

    check("both MCP tools were mounted into the registry", len(names) == 2,
          f"schemas={names}")
    check("mounted tool names are namespaced with the prefix",
          set(names) == {"mcp_get_weather", "mcp_get_time"}, f"names={names}")
    check("dispatching a mounted tool forwards to the MCP server",
          isinstance(w, str) and "get_weather" in w and "Paris" in w, repr(w)[:70])
    check("the server received the ORIGINAL (unprefixed) name + args",
          ("get_weather", {"city": "Paris"}) in server.calls, f"calls={server.calls}")
    check("BOTH tools are bound per-iteration (closure): each forwards its OWN name",
          ("get_weather", {"city": "Paris"}) in server.calls
          and ("get_time", {"tz": "UTC"}) in server.calls,
          f"late-binding bug would send ('get_time', ...) for weather: {server.calls}")
    check("mounted schemas forward the MCP tool's description and input_schema",
          any(s.get("description") == "Get weather"
              and s.get("input_schema", {}).get("properties", {}).get("city")
              for s in reg.schemas()),
          f"metadata dropped: {reg.schemas()}")

    # --- prefix prevents collisions: mount a SECOND server with the same tools ---
    server2 = FakeMCPServer()
    safe(lambda: mod.mount_mcp_server(reg, server2, prefix="alt_"))
    names2 = [s["name"] for s in reg.schemas()]
    safe(lambda: reg.dispatch("alt_get_weather", {"city": "Rome"}))
    check("a second server mounts under a different prefix without colliding",
          "mcp_get_weather" in names2 and "alt_get_weather" in names2, f"names={names2}")
    check("each prefix routes to its OWN server instance",
          ("get_weather", {"city": "Rome"}) in server2.calls
          and ("get_weather", {"city": "Rome"}) not in server.calls,
          f"server2={server2.calls}")

    report("Lesson 11 - MCP")


if __name__ == "__main__":
    main()
