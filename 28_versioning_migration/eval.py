"""
Lesson 28 eval -- runs WITHOUT an API key.

A v0 record migrates through every step to the latest; a v1 record gets only the
steps it still needs; an already-latest record is untouched. A "latest-only" or
"always-from-zero" stub fails.

    python 28_versioning_migration/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 28_versioning_migration/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe

# migrations[v] upgrades a v-record to v+1; latest version == 2.
MIGRATIONS = [
    lambda r: {**r, "name": r.get("title", "")},   # v0 -> v1: rename title -> name
    lambda r: {**r, "tags": []},                    # v1 -> v2: add tags
]


def main():
    mod = load_lesson(HERE)

    m0 = safe(lambda: mod.migrate({"version": 0, "title": "hello"}, MIGRATIONS))
    m1 = safe(lambda: mod.migrate({"version": 1, "name": "yo"}, MIGRATIONS))
    latest = safe(lambda: mod.migrate({"version": 2, "name": "x", "tags": ["a"]}, MIGRATIONS))

    check("migrate returns a dict", isinstance(m0, dict), repr(m0)[:60])
    check("version is bumped to the latest (2)", isinstance(m0, dict) and m0.get("version") == 2,
          repr(m0)[:70])
    check("the v0->v1 step ran (title renamed to name)",
          isinstance(m0, dict) and m0.get("name") == "hello", repr(m0)[:70])
    check("the v1->v2 step ran (tags added)",
          isinstance(m0, dict) and m0.get("tags") == [], repr(m0)[:70])
    check("a v1 record gets ONLY the steps it still needs",
          isinstance(m1, dict) and m1.get("version") == 2 and m1.get("name") == "yo"
          and m1.get("tags") == [], repr(m1)[:70])
    check("an already-latest record is untouched (no re-running from zero)",
          isinstance(latest, dict) and latest.get("name") == "x"
          and latest.get("tags") == ["a"], repr(latest)[:70])

    report("Lesson 28 - Versioning & Migration")


if __name__ == "__main__":
    main()
