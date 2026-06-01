"""
Lesson 06 eval -- runs WITHOUT an API key.

A scripted model returns invalid output first, then valid. Checks that the
retry loop validates, feeds back the error, retries, and eventually succeeds --
and that it errors out when output is never valid.

    python 06_structured_io/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 06_structured_io/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


class FakeModel:
    def __init__(self, scripts):
        self.scripts = scripts
        self.calls = 0
        self.feedbacks = []

    def __call__(self, feedback):
        self.feedbacks.append(feedback)
        out = self.scripts[min(self.calls, len(self.scripts) - 1)]
        self.calls += 1
        return out


def main():
    mod = load_lesson(HERE)
    schema = {"name": str, "score": int}

    fm = FakeModel(['{"name": "test"}',                       # invalid: missing score
                    '{"name": "test", "score": 9}'])          # valid
    res = safe(lambda: mod.request_structured(fm, schema, max_retries=3))
    ok = isinstance(res, tuple) and len(res) == 2
    obj, attempts = (res if ok else ({}, None))

    check("returns (obj, attempts) on success", ok, repr(res)[:90])
    check("eventually returns the valid object",
          ok and obj.get("name") == "test" and obj.get("score") == 9,
          repr(obj)[:90])
    check("retried after the invalid first attempt (2 model calls)",
          fm.calls == 2, f"calls={fm.calls}")
    check("reports it took 2 attempts", ok and attempts == 2, f"attempts={attempts}")
    check("sent corrective feedback on the retry",
          any("invalid" in str(f).lower() for f in fm.feedbacks[1:]),
          "retry feedback should mention the validation error")

    never = FakeModel(['{"name": "x"}'])  # always missing score
    res2 = safe(lambda: mod.request_structured(never, schema, max_retries=2))
    check("raises ValidationError when output is never valid",
          "ValidationError" in str(res2), repr(res2)[:90])

    report("Lesson 06 - Structured I/O")


if __name__ == "__main__":
    main()
