# MCP Connection Skill
Mount an external MCP server's tools into your agent's single tool pool.

## When to use
When a capability already exists as an MCP server (a database connector, a
browser, a third-party API) instead of building a native tool from scratch.

## Procedure
1. Start or connect to the MCP server; call `server.list_tools()`.
2. `mount_mcp_server(registry, server, prefix="mcp_")` to register each tool.
3. The loop now dispatches MCP tools exactly like native ones -- one pool,
   uniform permissions (Lesson 12) and hooks (Lesson 14).

## Closure caveat
When you build handlers inside a loop, bind the tool name PER ITERATION (a
factory function or default argument). Otherwise every handler captures the
last tool name -- a classic bug the Lesson 11 eval checks for.

## Ties to
Lesson 11 (MCP), Lesson 02 (Tool Use).
