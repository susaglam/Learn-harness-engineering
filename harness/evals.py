"""A tiny RED/GREEN eval runner. No framework, no magic — just checks.

Usage:
    from harness.evals import check, report
    check("the loop fed a tool_result back", client.saw_tool_result, "missing")
    report("Lesson 01 — The Agent Loop")   # prints summary, exits 0 (GREEN) or 1 (RED)
"""
from __future__ import annotations

import importlib.util
import os
import sys

_checks: list[tuple[str, bool, str]] = []


def check(name: str, passed: bool, detail: str = "") -> bool:
    """Record and print a single check. Returns the boolean for convenience."""
    passed = bool(passed)
    _checks.append((name, passed, detail))
    mark = "PASS" if passed else "FAIL"
    line = f"  [{mark}] {name}"
    if not passed and detail:
        line += f"  -> {detail}"
    print(line)
    return passed


def report(title: str = "") -> None:
    """Print a summary and exit: 0 if all GREEN, 1 if any RED."""
    passed = sum(1 for _, ok, _ in _checks if ok)
    total = len(_checks)
    print()
    if title:
        print(title)
    if total and passed == total:
        print(f"{passed}/{total} checks passed  --  GREEN")
        sys.exit(0)
    print(f"{passed}/{total} checks passed  --  RED")
    sys.exit(1)


def load_lesson(here: str):
    """Load the learner's stub.py, or reference.py if LHE_SOLUTION is set.

    Lets one eval verify both targets:
        python NN_lesson/eval.py                      -> tests YOUR stub.py  (RED until done)
        $env:LHE_SOLUTION=1; python NN_lesson/eval.py  -> tests reference.py  (must be GREEN)
    """
    fname = "reference.py" if os.environ.get("LHE_SOLUTION") else "stub.py"
    path = os.path.join(here, fname)
    # Unique module name per (lesson, target) so an in-process runner could load
    # many lessons without colliding in sys.modules.
    tag = "ref" if os.environ.get("LHE_SOLUTION") else "stub"
    spec_name = f"lhe_target_{os.path.basename(here.rstrip(os.sep))}_{tag}"
    spec = importlib.util.spec_from_file_location(spec_name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    # Register before exec so @dataclass et al. can resolve cls.__module__.
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def safe(thunk):
    """Run a thunk; return its value, or a sentinel string if it raised.

    Keeps an eval from crashing (so report() still runs and shows RED) when the
    learner's stub is incomplete and raises NotImplementedError.
    """
    try:
        return thunk()
    except Exception as exc:  # noqa: BLE001 - surface any learner bug as a failed check
        return f"__RAISED__ {type(exc).__name__}: {exc}"
