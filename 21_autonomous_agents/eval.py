"""
Lesson 21 eval -- runs WITHOUT an API key.

Two agents repeatedly claim from one board. Checks ownership, in_progress flip,
NO double-claim, and that an exhausted board yields None.

    python 21_autonomous_agents/eval.py                      # tests stub.py  (RED)
    $env:LHE_SOLUTION=1; python 21_autonomous_agents/eval.py  # tests reference.py (GREEN)
"""
from __future__ import annotations

import os
import sys
import threading

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))

from harness.evals import check, load_lesson, report, safe


def main():
    mod = load_lesson(HERE)
    board = [{"id": "t1", "status": "pending"},
             {"id": "t2", "status": "pending"},
             {"id": "t3", "status": "pending"}]

    c1 = safe(lambda: mod.claim_next(board, "A"))
    c2 = safe(lambda: mod.claim_next(board, "B"))
    c3 = safe(lambda: mod.claim_next(board, "A"))
    c4 = safe(lambda: mod.claim_next(board, "B"))   # board exhausted

    claimed = [c for c in (c1, c2, c3) if isinstance(c, dict)]
    ids = [c.get("id") for c in claimed]

    check("claim_next returns a task", isinstance(c1, dict), repr(c1)[:60])
    check("a claimed task is owned and marked in_progress",
          isinstance(c1, dict) and c1.get("owner") == "A"
          and c1.get("status") == "in_progress", repr(c1)[:70])
    check("NO double-claim: three claims hit three distinct tasks",
          len(ids) == 3 and len(set(ids)) == 3, f"ids={ids}")
    check("ownership reflects the claiming agent (second claim -> B)",
          isinstance(c2, dict) and c2.get("owner") == "B", repr(c2)[:70])
    check("an exhausted board returns None", c4 is None, repr(c4)[:60])

    # --- force BOTH guard clauses (status AND owner) to be load-bearing ---
    board2 = [{"id": "a", "status": "in_progress"},            # unowned, but not pending
              {"id": "b", "status": "pending", "owner": "x"},  # pending, but already owned
              {"id": "c", "status": "pending"}]                # the only truly claimable one
    cc = safe(lambda: mod.claim_next(board2, "w"))
    check("skips in_progress and already-owned tasks; claims only the free one",
          isinstance(cc, dict) and cc.get("id") == "c",
          f"a status-only or owner-only guard picks the wrong task: {cc!r}"[:90])

    # --- the invariant the lesson exists for: concurrent claims => exactly one winner ---
    solo = [{"id": "solo", "status": "pending"}]
    winners = []
    gate = threading.Barrier(8)

    def worker():
        gate.wait()                        # release all threads at once (max contention)
        got = mod.claim_next(solo, "w")
        if got is not None:
            winners.append(got)

    ts = [threading.Thread(target=worker) for _ in range(8)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    check("under concurrency exactly ONE agent claims the single task (no double-claim)",
          len(winners) == 1, f"{len(winners)} agents claimed the same task")

    report("Lesson 21 - Autonomous Agents")


if __name__ == "__main__":
    main()
