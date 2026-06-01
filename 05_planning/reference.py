"""
Lesson 05 - Planning  (reference implementation)

A TodoWrite tool: the model writes a plan as a todo list; the harness stores it
and renders it back. Externalizing the plan as state raises completion rates on
multi-step tasks -- and gives you (and the eval) something to inspect.
"""
from __future__ import annotations

_MARKS = {"pending": "[ ]", "in_progress": "[~]", "completed": "[x]"}


class TodoStore:
    def __init__(self):
        self.todos: list[dict] = []

    def write(self, todos: list[dict]) -> str:
        """Replace the list with a normalized copy; return the rendered view."""
        normalized = []
        for t in todos:
            normalized.append(
                {
                    "content": str(t.get("content", "")).strip(),
                    "status": t.get("status", "pending"),
                }
            )
        self.todos = normalized
        return self.render()

    def render(self) -> str:
        if not self.todos:
            return "(no todos)"
        lines = [f"{_MARKS.get(t['status'], '[ ]')} {t['content']}" for t in self.todos]
        done = sum(1 for t in self.todos if t["status"] == "completed")
        lines.append(f"({done}/{len(self.todos)} done)")
        return "\n".join(lines)
