# Lesson 22 — The Orchestration Spectrum

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Hardcode what must be reliable; delegate what must be smart.*

## The idea

This lesson resolves the argument the whole course has been building toward. "Is a hardcoded workflow a *real* agent?" is the wrong question. Every system sits on a **spectrum**, and good engineering is choosing the right point *per sub-problem*:

- **Scripted** — deterministic rules. Cheap, reliable, auditable; brittle to anything you didn't anticipate.
- **Autonomous** — hand the whole task to the model. Flexible and adaptive; a black box that varies run to run.
- **Hybrid** — a deterministic **skeleton** (the loop, the aggregation, the control flow) with **delegated judgment** at exactly the spots where judgment pays off.

We solve one task — *count the bugs in a list of issue titles* — all three ways. The scripted keyword rule misses *"the page won't load at all"* (a bug with no keyword). The hybrid keeps a reliable loop-and-count skeleton but delegates the per-item *judgment* to the model, catching the paraphrase without becoming an unpredictable black box.

```python
classify_scripted(items)                 # bugs: 1   (missed the paraphrase)
classify_hybrid(items, model_classify)   # bugs: 2   (smart per item, reliable overall)
```

## Why hybrid is usually the answer

A great agent is typically a *deterministic skeleton with autonomous muscles*: the harness owns the parts that must be reliable (iteration, retries, permissions, aggregation), and calls the model exactly where open-ended judgment is worth the cost and variance. That's not "less of an agent" — it's the engineering maturity the earlier 21 lessons were teaching.

## What you'll build

`classify_scripted` and `classify_autonomous` are given for contrast. In [`stub.py`](./stub.py), implement `classify_hybrid(items, model_classify)`:

1. Loop over `items` (the deterministic skeleton).
2. Call `model_classify(item)` per item (the delegated judgment); count `"bug"`.
3. Return `{"bugs": count, "style": "hybrid"}`.

## Run it

```sh
python 22_orchestration_spectrum/eval.py                       # RED
python 22_orchestration_spectrum/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 22_orchestration_spectrum/eval.py
```

→ Next: **Lesson 23 — The Comprehensive Agent** (*many mechanisms, one measurable loop*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
