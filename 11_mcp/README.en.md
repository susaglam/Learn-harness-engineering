# Lesson 11 — MCP

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Borrow capabilities; keep one tool pool.*

## The idea

You don't have to build every tool yourself. **MCP (Model Context Protocol)** is a standard way for an external server — a database connector, a browser, a third-party API — to *advertise* tools. The harness move is small but powerful: take whatever tools an MCP server lists and **register them into the same pool** your loop already dispatches through (Lesson 02). After mounting, an MCP tool is indistinguishable from a native one — the loop never learns it's remote.

```python
mount_mcp_server(registry, weather_server, prefix="mcp_")
registry.dispatch("mcp_get_weather", {"city": "Paris"})   # forwards to the server
```

## Why one pool, and why a prefix

- **One pool** means the loop, permissions (Lesson 12), and hooks (Lesson 14) treat every tool uniformly — no special-casing "MCP tools." Extensibility without complexity.
- **A prefix** namespaces names so two servers that both expose `search` don't collide.

There's a classic trap here: when you create handlers in a loop, you must **bind the tool name per iteration** (a factory function or default argument), or every handler ends up calling the *last* tool. The eval checks for exactly this bug.

## What you'll build

`ToolRegistry` is given. In [`stub.py`](./stub.py), implement `mount_mcp_server(registry, server, prefix)`:

1. For each `spec` in `server.list_tools()`, take `original = spec["name"]`.
2. Make a handler that forwards to `server.call_tool(original, kwargs)` — **bind `original` per iteration**.
3. `registry.register(prefix+original, description, input_schema, handler)`.

## Run it

```sh
python 11_mcp/eval.py                       # RED
python 11_mcp/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 11_mcp/eval.py
```

→ Next: **Lesson 12 — Permissions & Trust** (*freedom needs boundaries to be safe*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
