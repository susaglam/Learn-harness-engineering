"""
Lesson 19 - Agent Teams & Protocols  (reference implementation)

When one agent isn't enough, several coordinate through a MessageBus: each has
an inbox; messages are routed by recipient; a fixed request/reply shape is the
protocol. You build send() and recv().
"""
from __future__ import annotations

from collections import defaultdict


class MessageBus:
    def __init__(self):
        self.inboxes = defaultdict(list)   # name -> [message, ...]

    def send(self, to, frm, type, body):
        """Deliver a message into the recipient's inbox."""
        self.inboxes[to].append({"to": to, "from": frm, "type": type, "body": body})

    def recv(self, who):
        """Pop and return all messages addressed to `who` (FIFO), emptying the inbox."""
        msgs = self.inboxes[who]
        self.inboxes[who] = []
        return msgs
