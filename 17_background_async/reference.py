"""
Lesson 17 - Background & Async  (reference implementation)

Slow work (a long build, a big fetch) shouldn't freeze the agent. Run it on a
background thread and deliver a notification when it finishes, so the agent can
keep thinking and pick up results later. drain() is given; you build start().
"""
from __future__ import annotations

import queue
import threading


class BackgroundRunner:
    def __init__(self):
        self.notifications: "queue.Queue" = queue.Queue()
        self._threads: list = []

    def start(self, job_id, fn):
        """Run fn() on a daemon thread; post a notification when it finishes.

        Returns immediately with job_id (non-blocking). A failure is captured as
        an 'ERROR: ...' result rather than crashing the worker.
        """
        def run():
            try:
                result = fn()
            except Exception as exc:
                result = f"ERROR: {exc}"
            self.notifications.put({"id": job_id, "result": result})

        t = threading.Thread(target=run, daemon=True)
        t.start()
        self._threads.append(t)
        return job_id

    def drain(self, timeout: float = 2.0):
        """Wait for started jobs, then return all collected notifications."""
        for t in self._threads:
            t.join(timeout)
        out = []
        while not self.notifications.empty():
            out.append(self.notifications.get())
        return out
