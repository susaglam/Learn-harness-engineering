"""
Lesson 10 - Skill Loading  (YOUR implementation)

manifest() and _first_desc() are given. Implement load(name): return the full
SKILL.md body on demand, or an ERROR string if the skill is unknown.

Run:  python 10_skill_loading/eval.py     # RED until the TODO is done
"""
from __future__ import annotations

import os


class SkillManager:
    def __init__(self, skills_dir: str):
        self.skills_dir = skills_dir

    def manifest(self) -> list[dict]:
        out = []
        for name in sorted(os.listdir(self.skills_dir)):
            path = os.path.join(self.skills_dir, name, "SKILL.md")
            if os.path.isfile(path):
                out.append({"name": name, "description": self._first_desc(path)})
        return out

    def _first_desc(self, path: str) -> str:
        with open(path, encoding="utf-8") as f:
            for line in f:
                s = line.strip()
                if s and not s.startswith("#"):
                    return s
        return ""

    def load(self, name: str) -> str:
        # =====================================================================
        # TODO(you):
        #   - Reject path traversal first: if "/" in name or "\\" in name or
        #     name in ("", ".", "..") -> return f"ERROR: invalid skill name '{name}'".
        #   path = os.path.join(self.skills_dir, name, "SKILL.md")
        #   - if it's not a file -> return f"ERROR: unknown skill '{name}'"
        #   - otherwise open it (encoding="utf-8") and return the full text.
        # =====================================================================
        raise NotImplementedError("Implement SkillManager.load - see the TODO above")
