# Lesson 27 — Tool-Result Management

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *A 10MB result will blow your context.*
>
> **Arc 7 — Production.** What Lesson 07's budget runs into when tools get real.

## The idea

Lesson 07 budgeted the *conversation*. But a single tool call can return a
multi-megabyte log, file, or query result — feeding it straight back blows the
budget in one shot, and truncating it naively (`text[:2000]`) throws away the
*end*, which is often where the error or answer is. The production move:

1. **Store** the full output as an **artifact** (with a handle).
2. Feed the model a **bounded excerpt** — head **and** tail — plus an omission
   marker and the handle, so it can fetch the rest if it needs to.

```python
store_result(artifacts, "r1", huge_log)
summarize_result(huge_log, "r1", max_chars=200)
# -> "HEAD...\n...[8421 chars omitted; full result at artifact 'r1']...\n...TAIL"
```

## Why head + tail + handle

Head shows what a result *is*; tail shows how it *ended* (the stack trace, the
final count). The handle keeps the full data one fetch away without spending the
context now — the same progressive-disclosure idea as skills (L10) and memory
(L09), applied to tool output. Production adds structured summaries and
provenance (which tool, when), but this is the load-bearing core.

## What you'll build

`store_result()` is given. In [`stub.py`](./stub.py), implement
`summarize_result(text, key, max_chars, keep)`:

1. If `len(text) <= max_chars`, return it unchanged.
2. Otherwise return `text[:keep]` + an omission marker (count + artifact `key`) + `text[-keep:]`.

## Run it

```sh
python 27_tool_result_management/eval.py                       # RED
python 27_tool_result_management/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 27_tool_result_management/eval.py
```

→ Next: **Lesson 28 — Versioning & Migration** (*long-lived state needs migrations*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
