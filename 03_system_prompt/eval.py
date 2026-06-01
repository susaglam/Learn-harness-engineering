"""
Lesson 03 eval -- runs WITHOUT an API key.

Builds a prompt from four sections (two always-on, two conditional) and checks
inclusion, exclusion, ordering, and separation -- purely your build() logic.

    python 03_system_prompt/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 03_system_prompt/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


def main():
    mod = load_lesson(HERE)
    b = mod.SystemPromptBuilder()
    b.add("identity", "You are a coding agent.")
    b.add("tools", "You can use bash.")
    b.add("debug", "DEBUG MODE: be verbose.", when=lambda c: c.get("debug"))
    b.add("persona", "Arr, talk like a pirate.", when=lambda c: c.get("persona") == "pirate")

    base = safe(lambda: b.build({}))
    dbg = safe(lambda: b.build({"debug": True}))
    pir = safe(lambda: b.build({"persona": "pirate"}))

    check("base prompt includes always-on sections",
          "coding agent" in str(base) and "bash" in str(base),
          repr(base)[:90])
    check("base prompt excludes conditional 'debug' section",
          "bash" in str(base) and "DEBUG MODE" not in str(base),
          "debug section leaked into the base prompt")
    check("debug context includes the debug section",
          "DEBUG MODE" in str(dbg),
          "debug section missing when context enables it")
    check("persona context includes the persona section",
          "pirate" in str(pir),
          "persona section missing when context enables it")
    check("sections keep insertion order (identity before tools)",
          str(base).find("coding agent") != -1
          and str(base).find("coding agent") < str(base).find("bash"),
          "ordering not preserved")
    check("sections are separated by a blank line",
          "coding agent" in str(base) and "\n\n" in str(base),
          "expected sections joined with a blank line")

    report("Lesson 03 - System Prompt")


if __name__ == "__main__":
    main()
