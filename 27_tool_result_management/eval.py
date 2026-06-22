"""
Lesson 27 eval -- runs WITHOUT an API key.

A large result must be bounded to head+tail+marker+handle (so a plain text[:n]
truncation, which drops the tail and the handle, fails); a small result passes
through unchanged; the full output stays retrievable from the artifact store.

    python 27_tool_result_management/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 27_tool_result_management/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


def main():
    mod = load_lesson(HERE)
    artifacts = {}

    big = "HEAD_" + ("x" * 1000) + "_TAIL"
    mod.store_result(artifacts, "r1", big)                 # given
    s = safe(lambda: mod.summarize_result(big, "r1", max_chars=200, keep=80))
    small = safe(lambda: mod.summarize_result("short output", "r2", max_chars=200))

    check("a large result is bounded (much smaller than the original)",
          isinstance(s, str) and len(s) < 300 and len(s) < len(big), f"len={len(s) if isinstance(s,str) else 'n/a'}")
    check("the HEAD of the output survives", isinstance(s, str) and s.startswith("HEAD_"),
          repr(s[:40]) if isinstance(s, str) else repr(s))
    check("the TAIL of the output survives (a plain text[:n] truncation fails here)",
          isinstance(s, str) and s.endswith("_TAIL"), repr(s[-40:]) if isinstance(s, str) else repr(s))
    check("an omission marker + artifact handle is present",
          isinstance(s, str) and "omitted" in s and "'r1'" in s, repr(s)[:90])
    check("the FULL result is retrievable from the artifact store",
          artifacts.get("r1") == big, "full output not stored")
    check("a small result passes through unchanged",
          small == "short output", repr(small))

    report("Lesson 27 - Tool-Result Management")


if __name__ == "__main__":
    main()
