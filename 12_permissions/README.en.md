# Lesson 12 — Permissions & Trust

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Freedom needs boundaries to be safe.*

## The idea

An agent with a `bash` tool can do anything — including `rm -rf /`. We're now in the **hardening** arc: the agent already does useful work; here we make it *safe*. The mechanism is a **permission pipeline** that runs before every tool call and resolves it to one of three decisions:

- **allow** — run it silently.
- **ask** — pause and require human approval.
- **deny** — refuse, and tell the model why (which, per Lesson 02, becomes recoverable feedback).

Decisions come from an **ordered ruleset**. A rule matches by tool name (or `*`) plus an optional predicate on the input, and **the first match wins**. Anything unmatched falls to a default — which should be `ask` or `deny`, never `allow` (deny-by-default is the safe posture).

```python
rules = [
    Rule("bash", "deny", when=lambda i: "rm -rf" in i.get("command", "")),  # specific danger first
    Rule("bash", "allow"),                                          # then the general case
    Rule("*",    "ask"),                                            # everything else: ask
]
resolve("bash", {"command": "rm -rf /"}, rules)   # -> "deny"
```

## Why order and default matter

Putting the narrow, dangerous rule *before* the broad allow is what makes `rm -rf` deny while `ls` allows. And the default is your safety net: if you forget a rule, deny-by-default fails closed instead of open.

## What you'll build

`Rule` is given. In [`stub.py`](./stub.py), implement `resolve(tool_name, tool_input, rules, default)`:

1. Walk rules in order; a rule matches if its tool is `tool_name` or `"*"` **and** (`when is None` or `when(tool_input)`).
2. Return the first match's `.decision`; if none match, return `default`.

## Run it

```sh
python 12_permissions/eval.py                       # RED
python 12_permissions/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 12_permissions/eval.py
```

→ Next: **Lesson 13 — Security & Injection** (*every token from outside is a potential adversary*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
