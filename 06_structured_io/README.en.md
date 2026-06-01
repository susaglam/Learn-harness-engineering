# Lesson 06 — Structured I/O

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Design the output the model has to read.*

## The idea

Free-text is fine for humans, but when *your code* needs to act on the model's output — a list of files, a decision, a JSON record — you must make that output **machine-readable and validated**. The pattern: define a schema, ask the model for it, **validate**, and on mismatch **hand the error back** so the model fixes itself on the next attempt (retry-on-mismatch).

This is the same instinct as Lesson 02's "errors are data": a validation failure isn't fatal, it's feedback.

```python
schema = {"name": str, "score": int}
obj, attempts = request_structured(ask_model, schema)   # retries until valid
```

## Why retry-with-feedback beats "parse and pray"

Models occasionally emit malformed JSON or miss a field. If you just `json.loads` and crash, one stochastic slip kills the task. If instead you return *"your output was invalid: missing field 'score'"*, the model almost always corrects on the next turn. You trade a hard failure for a cheap retry.

## What you'll build

`validate()` and `parse_and_validate()` are given. In [`stub.py`](./stub.py), implement `request_structured(model_fn, schema, max_retries)`:

1. Loop up to `max_retries`; first `feedback` is `""`.
2. `text = model_fn(feedback)`; try `parse_and_validate(text, schema)` → return `(obj, attempt)`.
3. On `ValidationError`, set `feedback` to a corrective message containing the error, then retry.
4. If never valid, raise `ValidationError`.

## Run it

```sh
python 06_structured_io/eval.py                       # RED
python 06_structured_io/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 06_structured_io/eval.py
```

→ Next: **Lesson 07 — Context & Token Economics** (*context is a budget; spend it deliberately*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
