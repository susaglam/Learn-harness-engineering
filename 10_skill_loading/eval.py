"""
Lesson 10 eval -- runs WITHOUT an API key.

Creates a temporary skills/ dir with two SKILL.md files, then checks that the
manifest is cheap (summaries only) and load() pulls the full body on demand.

    python 10_skill_loading/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 10_skill_loading/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import shutil
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe

PDF = "# PDF Skill\nExtract text and tables from PDF files.\n\n## Steps\nUse the pdfplumber library to open the file and iterate pages.\n"
CSV = "# CSV Skill\nParse and summarize CSV files.\n\n## Steps\nUse the csv module; handle the header row and delimiters.\n"


def _make_skills():
    root = tempfile.mkdtemp(prefix="lhe_skills_")
    for name, body in (("pdf", PDF), ("csv", CSV)):
        os.makedirs(os.path.join(root, name))
        with open(os.path.join(root, name, "SKILL.md"), "w", encoding="utf-8") as f:
            f.write(body)
    return root


def main():
    mod = load_lesson(HERE)
    root = _make_skills()
    try:
        mgr = mod.SkillManager(root)
        man = mgr.manifest()
        descs = " ".join(s.get("description", "") for s in man)
        pdf_body = safe(lambda: mgr.load("pdf"))
        csv_body = safe(lambda: mgr.load("csv"))
        unknown = safe(lambda: mgr.load("nope"))

        check("manifest lists both skills", len(man) == 2, f"got {len(man)}")
        check("manifest holds summaries, not full bodies ('pdfplumber' absent)",
              "pdfplumber" not in descs, "manifest must stay cheap")
        check("load('pdf') returns the FULL body (contains 'pdfplumber')",
              isinstance(pdf_body, str) and "pdfplumber" in pdf_body, repr(pdf_body)[:70])
        check("load('csv') returns its full body (contains 'delimiters')",
              isinstance(csv_body, str) and "delimiters" in csv_body, repr(csv_body)[:70])
        check("loaded body includes the skill's summary line too",
              isinstance(pdf_body, str) and "Extract text" in pdf_body, "expected full doc")
        check("load() of an unknown skill returns an ERROR string",
              isinstance(unknown, str) and unknown.startswith("ERROR"), repr(unknown)[:70])
    finally:
        shutil.rmtree(root, ignore_errors=True)

    report("Lesson 10 - Skill Loading")


if __name__ == "__main__":
    main()
