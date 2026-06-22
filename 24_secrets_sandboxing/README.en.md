# Lesson 24 — Secrets, Sandboxing & Audit

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Never let a secret reach the model or a log.*
>
> **Arc 7 — Production.** These lessons mark where the toy mechanisms of Arcs 1–6
> meet real-world constraints.

## The idea

Your agent handles credentials: an API key in `.env`, a token a tool returns, a
password in a config it reads. Any of those can leak into a prompt, a tool
result, or a trajectory you log (Lesson 04) — and once a secret is in your logs
or sent to a model provider, it's compromised. The defense is **redaction at the
boundary**: scrub secrets out of everything that crosses into the model or a log.

Two kinds of secret to catch:

- **Known** values — passwords/keys your code injected or was given. Mask the literal.
- **Unknown but secret-*shaped*** — `sk-…`, `ghp_…`, `AKIA…`. Catch by pattern even
  when you don't know the value in advance.

```python
redact("key sk-ABCD1234EFGH and pw hunter2", known_secrets=["hunter2"])
# -> "key ***REDACTED*** and pw ***REDACTED***"
```

## Why both halves matter

Known-only redaction misses a token a tool just fetched; pattern-only misses your
app's own password that doesn't look key-shaped. You need both — plus, in a real
system: least-privilege credential scoping, a shell **sandbox** for `bash`, and an
**audit trail** of what ran. This lesson builds the redaction core; the rest is
the production checklist.

## What you'll build

In [`stub.py`](./stub.py), implement `redact(text, known_secrets)`:

1. Replace each value in `known_secrets` with `MASK`.
2. `re.sub` each pattern in `_SECRET_PATTERNS` with `MASK`.
3. Return the scrubbed text.

## Run it

```sh
python 24_secrets_sandboxing/eval.py                       # RED
python 24_secrets_sandboxing/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 24_secrets_sandboxing/eval.py
```

→ Next: **Lesson 25 — Concurrency & Leases** (*a claim you don't renew, you lose*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
