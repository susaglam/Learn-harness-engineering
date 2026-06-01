"""
Lesson 03 - System Prompt  (reference implementation)

Assemble the system prompt at runtime from ordered, optionally-conditional
sections -- instead of one hardcoded string. The agent is configured before it
speaks; different contexts produce different prompts from the same sections.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Optional


@dataclass
class Section:
    name: str
    text: str
    when: Optional[Callable[[dict], bool]] = None  # include if None or when(ctx) truthy


class SystemPromptBuilder:
    def __init__(self):
        self.sections: list[Section] = []

    def add(self, name: str, text: str, when: Optional[Callable[[dict], bool]] = None):
        """Append a section. `when` (optional) gates inclusion on the context."""
        self.sections.append(Section(name, text, when))
        return self  # chainable

    def build(self, context: Optional[dict] = None) -> str:
        """Concatenate included sections, in insertion order, blank-line separated."""
        context = context or {}
        parts = []
        for s in self.sections:
            if s.when is None or s.when(context):
                parts.append(s.text.strip())
        return "\n\n".join(parts)
