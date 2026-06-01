"""
Lesson 12 eval -- runs WITHOUT an API key.

Checks the allow/ask/deny pipeline: dangerous calls denied, safe ones allowed,
unknown tools fall through to a wildcard, and an empty ruleset returns default.

    python 12_permissions/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 12_permissions/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


def main():
    mod = load_lesson(HERE)
    R = mod.Rule
    rules = [
        R("bash", "deny", when=lambda i: "rm -rf" in i.get("command", "")),  # dangerous
        R("bash", "allow"),                                                   # other bash
        R("read_file", "allow"),
        R("*", "ask"),                                                        # everything else
    ]

    check("dangerous bash is denied (predicate + first-match)",
          safe(lambda: mod.resolve("bash", {"command": "rm -rf /"}, rules)) == "deny",
          "expected deny")
    check("ordinary bash is allowed",
          safe(lambda: mod.resolve("bash", {"command": "ls"}, rules)) == "allow",
          "expected allow")
    check("read_file is allowed",
          safe(lambda: mod.resolve("read_file", {"path": "x"}, rules)) == "allow",
          "expected allow")
    check("an unlisted tool falls through to the wildcard ('ask')",
          safe(lambda: mod.resolve("delete_database", {}, rules)) == "ask",
          "expected ask via '*'")
    check("empty ruleset returns the default",
          safe(lambda: mod.resolve("anything", {}, [], default="deny")) == "deny",
          "expected the default decision")

    report("Lesson 12 - Permissions & Trust")


if __name__ == "__main__":
    main()
