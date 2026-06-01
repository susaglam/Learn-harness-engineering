"""
Demo: load these example skills with the Lesson 10 reference SkillManager.

Proves the progressive-disclosure idea on real content: the manifest (names +
one-line descriptions) is cheap and always available; the full body is loaded
only on demand.

    python skills/demo.py
"""
from __future__ import annotations

import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def _load_skillmanager():
    """Load Lesson 10's reference SkillManager (folder name starts with a digit)."""
    path = os.path.join(ROOT, "10_skill_loading", "reference.py")
    spec = importlib.util.spec_from_file_location("lhe_skill_ref", path)
    if spec is None or spec.loader is None:
        raise SystemExit(f"cannot load Lesson 10 reference at {path}")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod.SkillManager


def main():
    SkillManager = _load_skillmanager()
    mgr = SkillManager(HERE)

    print("== manifest (cheap, always in context) ==")
    for s in mgr.manifest():
        print(f"  - {s['name']}: {s['description']}")

    print("\n== load('task-planning') (full body, on demand) ==")
    body = mgr.load("task-planning")
    print("\n".join(body.splitlines()[:8]))
    print("  ...")


if __name__ == "__main__":
    main()
