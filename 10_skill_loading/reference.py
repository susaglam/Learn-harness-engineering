"""
Lesson 10 - Skill Loading  (reference implementation)

A skill is an on-demand package of knowledge. The manifest (name + one-line
description of each skill) is always in context -- it's cheap. The full body is
loaded ONLY when the agent decides it needs that skill. manifest() is given;
you build load().
"""
from __future__ import annotations

import os


class SkillManager:
    def __init__(self, skills_dir: str):
        self.skills_dir = skills_dir

    def manifest(self) -> list[dict]:
        """Cheap listing: each skill's name + first descriptive line."""
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
        """Load the FULL skill body on demand."""
        path = os.path.join(self.skills_dir, name, "SKILL.md")
        if not os.path.isfile(path):
            return f"ERROR: unknown skill '{name}'"
        with open(path, encoding="utf-8") as f:
            return f.read()
