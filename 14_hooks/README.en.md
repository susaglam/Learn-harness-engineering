# Lesson 14 — Hooks

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Extend around the loop, never rewrite it.*

## The idea

You'll constantly want to add cross-cutting behavior: log every tool call, redact secrets from results, enforce the permission check from Lesson 12, time slow tools. The wrong way is to keep editing the loop until it's an unreadable tangle. The right way is **hooks**: fixed extension points where external functions run, leaving the loop pristine.

- **PreToolUse** hooks run *before* a tool. They can inspect the call and **block** it.
- **PostToolUse** hooks run *after* a tool. They can **transform** the result.

```python
@bus.on_pre
def guard(name, inp):
    if dangerous(inp): return "deny:blocked by guard"   # stops the call

@bus.on_post
def redact(name, inp, result):
    return scrub_secrets(result)                         # transforms the result
```

## Why this is the extensibility seam

Hooks are how a harness grows without rot. Permissions (L12), injection scanning (L13), tracing (L04), and memory writes can all be *hooks* rather than tangled `if`s inside the loop. The loop calls `call_tool_with_hooks` and stays exactly as simple as Lesson 01 — every new capability is additive.

## What you'll build

`HookBus` is given. In [`stub.py`](./stub.py), implement `call_tool_with_hooks(bus, name, tool_input, handler)`:

1. Run each pre-hook; if one returns a string starting with `"deny"`, return `f"BLOCKED: {verdict}"` **without** running the handler.
2. Otherwise run `handler(**tool_input)`.
3. Pass the result through each post-hook (each may transform it), then return it.

## Run it

```sh
python 14_hooks/eval.py                       # RED
python 14_hooks/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 14_hooks/eval.py
```

→ Next: **Lesson 15 — Error Recovery** (*failure is a branch, not a dead end*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
