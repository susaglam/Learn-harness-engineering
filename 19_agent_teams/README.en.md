# Lesson 19 — Agent Teams & Protocols

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Too big for one — coordinate many.*

## The idea

A subagent (Lesson 08) does one errand and vanishes. Some work needs *persistent* teammates that run alongside each other and talk: a researcher, a coder, a reviewer. They coordinate through a **MessageBus** — each agent has an **inbox**, messages are **routed by recipient**, and they agree on a fixed **protocol** (a message shape, e.g. `request` / `reply`) so anyone can understand anyone.

```python
bus.send(to="B", frm="A", type="request", body="ping")
for msg in bus.recv("B"):          # B reads its inbox
    bus.send(to=msg["from"], frm="B", type="reply", body="pong")
bus.recv("A")                      # A gets the reply
```

## Why a bus + a protocol

- **Routing by recipient** decouples senders from receivers — A doesn't call B directly, it drops a message; B reads on its own schedule. That's what makes asynchronous, many-to-many coordination tractable.
- **A protocol** (shared message shape) is the social contract: without an agreed `type`/`from`/`body`, teammates can't reliably interpret each other. Lesson 16's task graph plus this bus is the substrate for the self-organizing agents in Lesson 21.

## What you'll build

In [`stub.py`](./stub.py), implement the mailbox on `MessageBus`:

- `send(to, frm, type, body)` → append `{"to","from","type","body"}` to `self.inboxes[to]`.
- `recv(who)` → return all of `who`'s messages and reset that inbox to empty (deliver-once, FIFO).

## Run it

```sh
python 19_agent_teams/eval.py                       # RED
python 19_agent_teams/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 19_agent_teams/eval.py
```

→ Next: **Lesson 20 — Worktree Isolation** (*each agent gets its own room*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
