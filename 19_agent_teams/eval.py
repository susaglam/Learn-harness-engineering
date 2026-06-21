"""
Lesson 19 eval -- runs WITHOUT an API key.

Runs a request/reply round between agents A and B and checks routing, the
protocol shape, inbox draining, and isolation between recipients.

    python 19_agent_teams/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 19_agent_teams/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


def main():
    mod = load_lesson(HERE)
    bus = mod.MessageBus()

    safe(lambda: bus.send("B", "A", "request", "ping"))
    b_inbox = safe(lambda: bus.recv("B"))
    ok_b = isinstance(b_inbox, list)
    req = b_inbox[0] if ok_b and b_inbox else None

    safe(lambda: bus.send((req or {}).get("from", "A"), "B", "reply", "pong"))
    a_inbox = safe(lambda: bus.recv("A"))
    b_again = safe(lambda: bus.recv("B"))
    c_inbox = safe(lambda: bus.recv("C"))

    check("recipient B received exactly one message", ok_b and len(b_inbox) == 1,
          repr(b_inbox)[:70])
    check("the request carries from=A, type=request, body=ping",
          isinstance(req, dict) and req.get("from") == "A"
          and req.get("type") == "request" and req.get("body") == "ping",
          repr(req)[:70])
    check("recv drained B's inbox (second recv is empty)",
          isinstance(b_again, list) and b_again == [], repr(b_again)[:50])
    check("requester A received the reply (type=reply, body=pong, from=B)",
          isinstance(a_inbox, list) and len(a_inbox) == 1
          and a_inbox[0].get("type") == "reply" and a_inbox[0].get("body") == "pong"
          and a_inbox[0].get("from") == "B", repr(a_inbox)[:70])
    check("messages are isolated by recipient (C got nothing)",
          isinstance(c_inbox, list) and c_inbox == [], repr(c_inbox)[:50])

    # --- FIFO: two messages to one inbox return in SEND order (rejects LIFO) ---
    fifo = mod.MessageBus()
    safe(lambda: fifo.send("Z", "A", "msg", "ping1"))
    safe(lambda: fifo.send("Z", "A", "msg", "ping2"))
    z = safe(lambda: fifo.recv("Z"))
    check("messages are delivered FIFO (send order preserved)",
          isinstance(z, list) and [m.get("body") for m in z] == ["ping1", "ping2"],
          f"got {[m.get('body') for m in z] if isinstance(z, list) else z}")

    report("Lesson 19 - Agent Teams & Protocols")


if __name__ == "__main__":
    main()
