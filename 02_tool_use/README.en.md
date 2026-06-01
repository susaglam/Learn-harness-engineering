# Lesson 02 — Tool Use

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *A new tool is just a new handler.*

## The idea

In Lesson 01 the loop called a single hard-wired tool. Real agents have *many* tools, and the set changes over time. The discipline that keeps this sane: **leave the loop untouched and put all the variation in a dispatch map** — a registry that maps a tool *name* to two things:

- a **schema** the model sees (so it knows the tool exists and how to call it), and
- a **handler** your code runs when the model calls it.

Adding a tool becomes a one-liner — register a schema + handler — and the loop from Lesson 01 doesn't change at all. It just looks up `registry.dispatch(name, input)` instead of calling one fixed function.

```python
registry.dispatch(block.name, block.input)   # the loop's only tool-related line
```

## Why a registry — and why errors become strings

Two design choices matter here:

1. **Decoupling.** The loop shouldn't know which tools exist; the registry owns that. This is the seam that lets later lessons add skills (L10) and MCP tools (L11) into the *same* pool without editing the loop.
2. **Errors are data, not crashes.** A model will call tools that don't exist, or with bad arguments. `dispatch` catches both and returns an `"ERROR: ..."` string. That string flows back to the model as a normal `tool_result`, so the model can read it and *correct itself* on the next turn. An exception that escaped `dispatch` would kill the whole agent — a recoverable mistake turned fatal.

## What you'll build

In [`stub.py`](./stub.py), implement `ToolRegistry.dispatch(name, tool_input)`:

1. If `name` isn't a known handler → return `f"ERROR: unknown tool '{name}'"`.
2. Otherwise call `self.handlers[name](**tool_input)` inside a `try/except`, returning `str(result)` on success or `f"ERROR: {exc}"` on failure.

## Run it

```sh
python 02_tool_use/eval.py                       # RED — dispatch isn't implemented
#   ...implement the TODO in stub.py...
python 02_tool_use/eval.py                       # GREEN

# Verify the reference solution passes too:
#   PowerShell:  $env:LHE_SOLUTION=1; python 02_tool_use/eval.py
```

The eval needs no model: it registers two fake tools (`add`, `echo`) and checks routing, the unknown-tool path, and the handler-error path — purely your dispatch logic.

## Compare

Diff your `stub.py` against [`reference.py`](./reference.py). Note how `register` is a decorator and `schemas()` is what you'd pass to the model as `tools=`.

→ Next: **Lesson 03 — System Prompt** (*the agent is configured before it speaks*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
