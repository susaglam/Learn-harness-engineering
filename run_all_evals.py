#!/usr/bin/env python3
"""Run every lesson's eval and assert the RED -> GREEN contract.

For each NN_*/eval.py we run it twice:
  - with the learner's stub.py        -> expect RED   (exit code 1)
  - with reference.py (LHE_SOLUTION=1) -> expect GREEN (exit code 0)

A lesson "passes" only if it is RED with the stub and GREEN with the reference.
Prints a per-lesson table and a summary; exits non-zero if any lesson breaks the
contract. Pure Python, cross-platform -- used both locally and in CI.

    python run_all_evals.py          # quiet table
    python run_all_evals.py -v       # also stream each eval's check lines
"""
from __future__ import annotations

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))


def lesson_evals():
    """Discover NN_*/eval.py folders in numeric order."""
    found = []
    for name in sorted(os.listdir(ROOT)):
        path = os.path.join(ROOT, name)
        if (
            os.path.isdir(path)
            and len(name) >= 3
            and name[:2].isdigit()
            and name[2] == "_"
        ):
            ev = os.path.join(path, "eval.py")
            if os.path.isfile(ev):
                found.append((name, ev))
    return found


def run_eval(eval_path: str, *, solution: bool, verbose: bool) -> int:
    """Run one eval; return its exit code. solution=True loads reference.py."""
    env = dict(os.environ)
    if solution:
        env["LHE_SOLUTION"] = "1"
    else:
        env.pop("LHE_SOLUTION", None)
    result = subprocess.run(
        [sys.executable, eval_path],
        env=env,
        capture_output=not verbose,
        text=True,
    )
    return result.returncode


def main(argv) -> int:
    verbose = "-v" in argv or "--verbose" in argv
    evals = lesson_evals()
    if not evals:
        print("No NN_*/eval.py lessons found.")
        return 1

    rows = []
    all_ok = True
    for name, ev in evals:
        if verbose:
            print(f"\n=== {name} (stub -> expect RED) ===")
        red = run_eval(ev, solution=False, verbose=verbose)
        if verbose:
            print(f"=== {name} (reference -> expect GREEN) ===")
        green = run_eval(ev, solution=True, verbose=verbose)
        ok = (red == 1 and green == 0)
        all_ok = all_ok and ok
        rows.append((ok, name, red, green))

    width = max(len(n) for _, n, _, _ in rows)
    print()
    print(f"{'':6}{'lesson':<{width}}  RED  GREEN")
    print("-" * (width + 19))
    for ok, name, red, green in rows:
        mark = "[ ok ]" if ok else "[FAIL]"
        print(f"{mark}{name:<{width}}  {red:>3}  {green:>5}")

    passed = sum(1 for r in rows if r[0])
    print()
    print(f"{passed}/{len(rows)} lessons satisfy the RED -> GREEN contract")
    if all_ok:
        print("ALL GREEN: every lesson is RED with its stub and GREEN with its reference.")
        return 0
    print("BROKEN: some lessons do not satisfy the contract (see FAIL rows above).")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
