"""
Lesson 20 - Worktree Isolation  (reference implementation)

When several agents work the same repo in parallel, they trample each other's
files. A git *worktree* gives each task its own checkout in its own directory.
The harness piece is the binding: task_id -> a unique directory, idempotent per
task and never shared. (We model the binding so the lesson runs without git;
a real allocate() would also run `git worktree add <path> -b <branch>`.)
"""
from __future__ import annotations

import os


class WorktreeRegistry:
    def __init__(self, base_dir: str):
        self.base_dir = base_dir
        self.by_task: dict = {}   # task_id -> worktree path

    def allocate(self, task_id: str) -> str:
        """Return the directory bound to task_id, creating a unique one on first use."""
        if task_id in self.by_task:
            return self.by_task[task_id]            # idempotent: same task, same room
        path = os.path.join(self.base_dir, f"wt-{task_id}")
        self.by_task[task_id] = path
        return path

    def release(self, task_id: str):
        """Unbind a task (a real impl would `git worktree remove` here)."""
        return self.by_task.pop(task_id, None)
