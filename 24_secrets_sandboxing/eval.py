"""
Lesson 24 eval -- runs WITHOUT an API key.

Checks that BOTH known secrets and secret-shaped tokens are masked, benign text
survives, and benign text isn't over-masked. A known-only or pattern-only stub
fails.

    python 24_secrets_sandboxing/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 24_secrets_sandboxing/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


def main():
    mod = load_lesson(HERE)

    text = ("Use API key sk-ABCD1234EFGH9999 with password hunter2; the GitHub "
            "token is ghp_ABCDEFGHIJKLMNOPQRST1234. Then summarize the report.")
    out = safe(lambda: mod.redact(text, ["hunter2"]))
    benign = safe(lambda: mod.redact("Please ask the user to confirm the plan.", []))

    check("redact returns a string", isinstance(out, str) and not out.startswith("__RAISED__"),
          repr(out)[:60])
    check("a KNOWN secret value is masked (hunter2)",
          isinstance(out, str) and "hunter2" not in out, repr(out)[:80])
    check("an API-key-SHAPED token is masked (pattern, not just known values)",
          isinstance(out, str) and "sk-ABCD1234EFGH9999" not in out, repr(out)[:80])
    check("a GitHub token is masked",
          isinstance(out, str) and "ghp_ABCDEFGHIJKLMNOPQRST1234" not in out, repr(out)[:80])
    check("benign text survives ('summarize the report')",
          isinstance(out, str) and "summarize the report" in out, repr(out)[:80])
    check("benign text is NOT over-masked (no false positives)",
          benign == "Please ask the user to confirm the plan.", repr(benign)[:80])

    report("Lesson 24 - Secrets, Sandboxing & Audit")


if __name__ == "__main__":
    main()
