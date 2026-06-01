"""
Lesson 22 - The Orchestration Spectrum  (YOUR implementation)

scripted() and autonomous() are given. Implement classify_hybrid: a
deterministic skeleton with a delegated per-item judgment.

Run:  python 22_orchestration_spectrum/eval.py     # RED until the TODO is done
"""
from __future__ import annotations

_KEYWORDS = ("crash", "error", "broken", "fix")


def classify_scripted(items):
    bugs = sum(1 for it in items if any(k in it.lower() for k in _KEYWORDS))
    return {"bugs": bugs, "style": "scripted"}


def classify_autonomous(items, model_solve):
    return {"bugs": int(model_solve(items)), "style": "autonomous"}


def classify_hybrid(items, model_classify):
    # =========================================================================
    # TODO(you): the deterministic skeleton + delegated judgment.
    #   bugs = 0
    #   for it in items:                      # <- hardcoded control flow (reliable)
    #       if model_classify(it) == "bug":   # <- delegated judgment (smart)
    #           bugs += 1
    #   return {"bugs": bugs, "style": "hybrid"}
    # =========================================================================
    raise NotImplementedError("Implement classify_hybrid - see the TODO above")
