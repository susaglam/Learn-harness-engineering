"""
Lesson 03 - System Prompt  (YOUR implementation)

Implement SystemPromptBuilder.build: concatenate the sections that apply to the
given context, in insertion order, separated by a blank line.

Run:  python 03_system_prompt/eval.py     # RED until the TODO is done
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class Section:
    name: str
    text: str
    when: Optional[Callable[[dict], bool]] = None


class SystemPromptBuilder:
    def __init__(self):
        self.sections: list[Section] = []

    def add(self, name: str, text: str, when: Optional[Callable[[dict], bool]] = None):
        self.sections.append(Section(name, text, when))
        return self

    def build(self, context: Optional[dict] = None) -> str:
        context = context or {}
        # =====================================================================
        # TODO(you): build the prompt.
        #   - Walk self.sections IN ORDER.
        #   - Include a section if s.when is None OR s.when(context) is truthy.
        #   - Collect each included s.text.strip().
        #   - Return them joined with "\n\n" (a blank line between sections).
        # =====================================================================
        raise NotImplementedError("Implement SystemPromptBuilder.build - see the TODO above")
