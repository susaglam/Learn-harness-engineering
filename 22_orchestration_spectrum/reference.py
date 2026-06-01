"""
Lesson 22 - The Orchestration Spectrum  (reference implementation)

The same task, solved three ways:
  - scripted    : pure deterministic rule. Cheap, reliable, brittle to wording.
  - autonomous  : hand the whole task to the model. Flexible, but a black box.
  - hybrid      : deterministic skeleton (loop + aggregate) + delegated judgment
                  (one model call per item). Reliable control flow, smart calls.

scripted() and autonomous() are given for contrast; you build the hybrid.
"""
from __future__ import annotations

_KEYWORDS = ("crash", "error", "broken", "fix")


def classify_scripted(items):
    """Deterministic keyword rule -- misses anything phrased differently."""
    bugs = sum(1 for it in items if any(k in it.lower() for k in _KEYWORDS))
    return {"bugs": bugs, "style": "scripted"}


def classify_autonomous(items, model_solve):
    """Delegate the entire task to the model in one shot."""
    return {"bugs": int(model_solve(items)), "style": "autonomous"}


def classify_hybrid(items, model_classify):
    """Hardcode the loop + count (reliable); delegate per-item judgment (smart)."""
    bugs = 0
    for it in items:
        if model_classify(it) == "bug":
            bugs += 1
    return {"bugs": bugs, "style": "hybrid"}
