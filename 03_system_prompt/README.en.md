# Lesson 03 — System Prompt

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *The agent is configured before it speaks.*

## The idea

The system prompt is the instruction set the model receives *before* the first user message — it defines who the agent is and how it behaves. A beginner hardcodes one big string. That breaks the moment you need the prompt to differ by context: debug vs production, a different persona, a tool that's only sometimes available, a project-specific rule.

The fix is **runtime assembly**: keep the prompt as a list of named **sections**, each optionally gated by a condition, and concatenate the applicable ones when the run starts. Same sections, different context → different prompt.

```python
prompt = (SystemPromptBuilder()
          .add("identity", "You are a coding agent.")
          .add("tools", "You can use bash.")
          .add("debug", "DEBUG MODE: be verbose.", when=lambda c: c.get("debug")))
system = prompt.build({"debug": is_dev})   # assembled per run
```

## Why sections beat one big string

- **Conditional behavior** without `if`-soup: a section appears only when its `when(context)` is true.
- **Composability:** later lessons inject sections at runtime — memory (L9) adds a "what you remember" section, skills (L10) add a "skills available" section — all into this same builder.
- **Order is meaning:** identity first, then capabilities, then situational rules. The builder preserves insertion order so the prompt reads coherently.

## What you'll build

In [`stub.py`](./stub.py), implement `SystemPromptBuilder.build(context)`:

1. Walk `self.sections` in order.
2. Include a section if `s.when is None` **or** `s.when(context)` is truthy.
3. Collect each included `s.text.strip()` and return them joined with `"\n\n"`.

## Run it

```sh
python 03_system_prompt/eval.py                       # RED
#   ...implement build() in stub.py...
python 03_system_prompt/eval.py                       # GREEN
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 03_system_prompt/eval.py
```

→ Next: **Lesson 04 — Eval & Observability** (*if you can't measure it, you're hoping*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
