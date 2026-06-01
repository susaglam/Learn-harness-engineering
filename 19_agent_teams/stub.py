"""
Lesson 19 - Agent Teams & Protocols  (YOUR implementation)

Implement the mailbox: send() routes a message to a recipient's inbox; recv()
drains and returns all messages addressed to one agent.

Run:  python 19_agent_teams/eval.py     # RED until the TODO is done
"""
from __future__ import annotations

from collections import defaultdict


class MessageBus:
    def __init__(self):
        self.inboxes = defaultdict(list)   # name -> [message, ...]

    def send(self, to, frm, type, body):
        # TODO(you): append {"to": to, "from": frm, "type": type, "body": body}
        # to self.inboxes[to].
        raise NotImplementedError("Implement MessageBus.send")

    def recv(self, who):
        # TODO(you): return all messages in self.inboxes[who], and reset that
        # inbox to empty (so each message is delivered once, FIFO).
        raise NotImplementedError("Implement MessageBus.recv")
