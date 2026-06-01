"""
Lesson 17 - Background & Async  (YOUR implementation)

drain() is given. Implement start(): run fn() on a background daemon thread and
post {"id": job_id, "result": ...} to self.notifications when it finishes.

Run:  python 17_background_async/eval.py     # RED until the TODO is done
"""
from __future__ import annotations

import queue
import threading


class BackgroundRunner:
    def __init__(self):
        self.notifications: "queue.Queue" = queue.Queue()
        self._threads: list = []

    def start(self, job_id, fn):
        # =====================================================================
        # TODO(you):
        #   1. Define run(): call fn() in try/except; on success result = value,
        #      on exception result = f"ERROR: {exc}". Then
        #      self.notifications.put({"id": job_id, "result": result}).
        #   2. Start a daemon threading.Thread(target=run), append it to
        #      self._threads, and return job_id immediately (non-blocking).
        # =====================================================================
        raise NotImplementedError("Implement BackgroundRunner.start - see the TODO above")

    def drain(self, timeout: float = 2.0):
        for t in self._threads:
            t.join(timeout)
        out = []
        while not self.notifications.empty():
            out.append(self.notifications.get())
        return out
