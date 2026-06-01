# Lesson 01 — The Agent Loop

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *One loop, and the model drives.*

## The idea

An agent is not a clever prompt. It is a **loop**:

```
ask the model  →  did it ask for a tool?
                     ├─ no  → it's done, return its answer
                     └─ yes → run the tool, feed the result back, ask again
```

That's it. The model decides *what* to do and *when to stop*; your code just runs what it asks for and reports back. Everything else in this course — planning, memory, teams, security — layers on top of this loop. **The loop itself never changes.** Internalize it now and the other 22 lessons are just additions.

## Why feeding results back is the whole trick

A model can't run a `bash` command — it has no hands. When it wants one, it emits a `tool_use` block (`stop_reason == "tool_use"`) saying *"please run bash with this input."* Your harness runs it and appends a `tool_result` to the conversation. On the next turn the model **sees the result** and continues reasoning.

Skip that step and the model is blind: it asked for something and never learned what happened. The agent stalls. So the one line that matters — the line that turns a chatbot into an agent — is *feeding the tool result back into `messages`*.

## What you'll build

In [`stub.py`](./stub.py), implement the tool-result step inside `agent_loop`:

1. For each `tool_use` block in the model's response, call `handlers[block.name](**block.input)`.
2. Wrap each output as `{"type": "tool_result", "tool_use_id": block.id, "content": str(output)}`.
3. Append them all as **one** user message: `messages.append({"role": "user", "content": results})`.

## Run it

```sh
python 01_agent_loop/eval.py        # RED — the TODO isn't done yet
#   ...implement the TODO in stub.py...
python 01_agent_loop/eval.py        # GREEN — you built a working loop

python 01_agent_loop/reference.py   # (optional) run the real thing — needs an API key in .env
```

The eval uses a **scripted fake model** — no API key, no cost. It checks that your loop calls the handler, feeds a correctly-linked `tool_result` back, and terminates with the model's final answer. A GREEN here means your *engineering* is correct, independent of any model's mood.

## Compare

Once GREEN, diff your `stub.py` against [`reference.py`](./reference.py). Notice how small the essential code is — and how the loop body is identical to what every later lesson builds on.

→ Next: **Lesson 02 — Tool Use** (*a new tool is just a new handler*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
