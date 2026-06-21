#!/usr/bin/env python3
"""Run every lesson's eval and assert the RED -> GREEN contract.

For each NN_*/eval.py we run it twice:
  - with the learner's stub.py        -> expect RED   (checks ran, some FAILED)
  - with reference.py (LHE_SOLUTION=1) -> expect GREEN (all checks PASSED)

A lesson "passes" only if it is genuinely RED with the stub and GREEN with the
reference. We do NOT trust the exit code alone: a stub that crashes (ImportError,
SyntaxError, an exception before any check) also exits 1, but that is BROKEN, not
a legitimate RED. So we require the stub run to have actually recorded a failing
check ("[FAIL]" + a "checks passed" summary), and the reference run to have no
failing check.

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


def run_eval(eval_path: str, *, solution: bool):
    """Run one eval; return (exit_code, combined_output). solution=True -> reference.py."""
    env = dict(os.environ)
    if solution:
        env["LHE_SOLUTION"] = "1"
    else:
        env.pop("LHE_SOLUTION", None)
    r = subprocess.run(
        [sys.executable, eval_path], env=env, capture_output=True, text=True
    )
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def main(argv) -> int:
    verbose = "-v" in argv or "--verbose" in argv
    evals = lesson_evals()
    if not evals:
        print("No NN_*/eval.py lessons found.")
        return 1

    rows = []
    all_ok = True
    for name, ev in evals:
        rc_red, out_red = run_eval(ev, solution=False)
        rc_green, out_green = run_eval(ev, solution=True)
        if verbose:
            print(f"\n=== {name} (stub -> expect RED) ===\n{out_red.rstrip()}")
            print(f"=== {name} (reference -> expect GREEN) ===\n{out_green.rstrip()}")

        ran_red = "checks passed" in out_red          # report() actually ran
        red_ok = rc_red == 1 and ran_red and "[FAIL]" in out_red
        green_ok = rc_green == 0 and "checks passed" in out_green and "[FAIL]" not in out_green
        ok = red_ok and green_ok

        why = ""
        if not ok:
            if not ran_red and rc_red != 1:
                why = "stub crashed before any check ran (not a real RED)"
            elif not red_ok:
                why = "stub did not produce a failing check"
            elif not green_ok:
                why = "reference did not go fully GREEN"
        all_ok = all_ok and ok
        rows.append((ok, name, rc_red, rc_green, why))

    width = max(len(n) for _, n, _, _, _ in rows)
    print()
    print(f"{'':7}{'lesson':<{width}}  RED  GREEN")
    print("-" * (width + 20))
    for ok, name, red, green, _why in rows:
        mark = "[ ok ]" if ok else "[FAIL]"
        print(f"{mark} {name:<{width}}  {red:>3}  {green:>5}")

    failures = [(name, why) for ok, name, _, _, why in rows if not ok]
    passed = len(rows) - len(failures)
    print()
    print(f"{passed}/{len(rows)} lessons satisfy the RED -> GREEN contract")
    if all_ok:
        print("ALL GREEN: every lesson is RED with its stub and GREEN with its reference.")
        return 0
    print("BROKEN:")
    for name, why in failures:
        print(f"  - {name}: {why}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
