# Methodology — Eval-driven, not copy-driven

[English](./methodology.md) | [Türkçe](./methodology.tr.md)

## The problem with reading finished code

The predecessor course handed you a complete `code.py` per lesson. You read it, nodded, and moved on — and retained almost nothing, because understanding-by-reading is an illusion. You only learn a mechanism when you are forced to *make it work*.

So every lesson here is a **failing test you make pass**.

## The loop of every lesson

```
1. READ      README.en.md / README.tr.md   — the mechanism and WHY it matters
2. RUN       python NN_lesson/eval.py        — RED: the eval fails; the harness is incomplete
3. IMPLEMENT NN_lesson/stub.py                — write the 5–10 lines that matter (the TODO)
4. RUN       python NN_lesson/eval.py        — GREEN: you proved the mechanism works
5. COMPARE   NN_lesson/reference.py           — diff your design against ours
```

If your eval is GREEN, you didn't just read about the mechanism — you built one that demonstrably works.

## File anatomy of a lesson

```
NN_lesson/
  README.en.md     # narrative: the idea, the why, the design choices
  README.tr.md     # Turkish narrative (terms glossed; see terminology convention below)
  reference.py     # the complete, correct implementation
  stub.py          # the same, with the crucial part replaced by a TODO — YOU fill it
  eval.py          # imports YOUR stub and checks it; RED until correct
```

## Why most evals use a fake model (and no API key)

A harness bug and a model mistake look the same from the outside, which makes agents maddening to debug. So our evals **isolate the engineering**: they drive your harness with a *scripted fake model* that returns predetermined responses. That gives three things:

- **Deterministic** — same result every run; no flakiness.
- **Free & offline** — no API key, no token cost, runs in CI.
- **Honest** — a GREEN eval means *your loop/logic* is correct, not that "the model happened to cooperate."

Every eval here runs offline against a scripted fake model — even retrieval (Lesson 09) uses a deterministic bag-of-words embedding so the check is reproducible. A real deployment swaps in live model calls; the eval mechanism is identical.

```python
# the shape of a fake-model eval (Lesson 01)
client = FakeClient(script=[
    tool_use("bash", {"command": "echo hi"}),   # 1st call: model asks for a tool
    text("done"),                                # 2nd call: model finishes
])
final = your_agent_loop(client, ..., handlers={"bash": recording_handler})
check("tool result was fed back", client.saw_tool_result)   # tests YOUR loop
```

## The terminology convention (Turkish track)

Educational content should welcome beginners. In the Turkish docs we therefore:

1. **Keep technical terms in English** (you'll meet them that way in code and industry).
2. **Gloss each term on first use** in parentheses: *harness (koşum takımı — modelin çalışma ortamı)*.
3. Maintain one beginner-friendly **[glossary](./terminoloji.tr.md)** as the single source of truth.

This minimizes cognitive load while maximizing transfer to real code. English docs assume the reader reads English technical terms natively; a concise [English glossary](./glossary.md) mirrors the Turkish one for newcomers.

## Scaling rule for authors

When you build a scaffolded lesson, keep the eval **small and surgical**: it should test the *one* mechanism the lesson adds, not the whole world. One mechanism, one motto, one failing test, one fix.

← Back to [README](../README.md) · see also: [philosophy](./philosophy.md)
