"""
Lesson 20 - Worktree Isolation  (YOUR implementation)

release() is given. Implement allocate(task_id): bind each task to a UNIQUE
directory under base_dir, returning the same path for the same task and
different paths for different tasks.

Run:  python 20_worktree_isolation/eval.py     # RED until the TODO is done
"""
from __future__ import annotations

import os


class WorktreeRegistry:
    def __init__(self, base_dir: str):
        self.base_dir = base_dir
        self.by_task: dict = {}

    def allocate(self, task_id: str) -> str:
        # =====================================================================
        # TODO(you):
        #   - If task_id is already bound, return its existing path (idempotent).
        #   - Otherwise build a unique path, e.g.
        #       path = os.path.join(self.base_dir, f"wt-{task_id}")
        #     store it in self.by_task[task_id], and return it.
        # =====================================================================
        raise NotImplementedError("Implement WorktreeRegistry.allocate - see the TODO above")

    def release(self, task_id: str):
        return self.by_task.pop(task_id, None)
