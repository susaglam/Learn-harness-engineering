"""
Lesson 05 - Planning  (YOUR implementation)

render() is given. Implement TodoStore.write: normalize the incoming todos,
store them, and return the rendered view.

Run:  python 05_planning/eval.py     # RED until the TODO is done
"""
from __future__ import annotations

_MARKS = {"pending": "[ ]", "in_progress": "[~]", "completed": "[x]"}


class TodoStore:
    def __init__(self):
        self.todos: list[dict] = []

    def write(self, todos: list[dict]) -> str:
        # =====================================================================
        # TODO(you):
        #   1. Build a normalized list: each item is
        #        {"content": str(t.get("content","")).strip(),
        #         "status":  t.get("status", "pending")}   # default = pending
        #   2. Store it on self.todos (replacing the old list).
        #   3. return self.render()
        # =====================================================================
        raise NotImplementedError("Implement TodoStore.write - see the TODO above")

    def render(self) -> str:
        if not self.todos:
            return "(no todos)"
        lines = [f"{_MARKS.get(t['status'], '[ ]')} {t['content']}" for t in self.todos]
        done = sum(1 for t in self.todos if t["status"] == "completed")
        lines.append(f"({done}/{len(self.todos)} done)")
        return "\n".join(lines)
