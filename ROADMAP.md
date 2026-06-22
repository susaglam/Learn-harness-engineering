# Roadmap & Backlog

This file tracks what's been hardened, what could be added (v2 curriculum), and
the small backlog of nits surfaced by a multi-agent audit (each finding was
adversarially verified). Nothing here blocks the course from working today —
all 23 lessons are RED(stub) → GREEN(reference) and `run_all_evals.py` is green.

---

## Fixed in the audit pass

- **9 evals were "gameable"** (a wrong/cheating stub could pass GREEN) — now
  hardened so the mechanism is load-bearing: L04 (final-event semantics),
  L07 (keep_recent), L09 (cosine vs dot-product), L11 (closure binding +
  metadata), L13 (pattern identity + keyword-bait), L17 (non-blocking/threaded),
  L21 (concurrent no-double-claim), L22 (verdict consumed), L23 (feedback +
  DENIED content).
- **Harness:** `run_all_evals` now distinguishes a real RED from a crashed eval;
  `harness/loop.py` guards the empty tool-turn and raises on `max_turns`;
  `load_lesson` uses `normpath`.
- **Correctness:** L18 non-positive interval is one-shot (no infinite loop);
  L15 unclassified errors fall back instead of crashing; L21 claim is atomic
  via a `Lock`.
- **Docs:** cross-platform Quickstart, dropped the false "lessons import
  run_agent" claim, added `max_tokens` to the core snippet, MODEL_ID made
  consistent, philosophy "twenty"→"twenty-three", offline-eval claim corrected,
  "the loop never changes" softened to "the *conceptual* loop".
- **Added:** `CONTRIBUTING.md`, `.editorconfig`, this `ROADMAP.md`.

---

## v2 curriculum — SHIPPED as Arc 7 (Production)

Items 2–7 below now exist as eval-verified lessons **24–29** (EN/TR), turning the
candidate list into a real arc. Item 1 (production-bridge "Toy vs production"
callouts inside the Arc 1–6 lesson READMEs) is the remaining decorative piece;
the Arc 7 lessons themselves are the production content.

1. **Production-bridge notes** — a short "Toy vs production" callout at the end of
   each lesson where the gap is sharp (compaction isn't real summarization;
   in-process lock vs DB lease; heuristic injection detection vs a real filter;
   in-memory cron vs durable store). *Cheapest, highest-value; partially started
   in L21/L07 reference notes.*
2. **Secrets, sandboxing & audit trail** (extends Arc 4) — secret redaction,
   credential scoping, an exfiltration eval, a shell sandbox.
3. **Concurrency & leases** (extends L21) — locks, lease + TTL, retry
   idempotency, reclaiming a crashed claimant's work.
4. **Eval expansion** (extends L04) — golden trajectories, adversarial evals,
   cost/latency budgets, a regression dashboard.
5. **Human-in-the-loop** — approval UX, pause/resume, cancel, rollback, escalation
   (beyond L12's allow/ask/deny).
6. **Tool-result management** — large-output truncation, artifact storage,
   structured summaries, provenance.
7. **Versioning & migration** — prompt / schema / skill / memory migration for
   long-lived agents.

---

## Backlog (minor / nit, by area)

Small, low-risk improvements; safe to pick up piecemeal.

- **L01** — note that error handling is deferred to L02; guard the empty
  tool-turn in `reference.py` (harness/loop.py already does).
- **L05** — test `.strip()` normalization; optionally validate unknown status.
- **L06** — assert the first feedback is empty.
- **L10** — note real `SKILL.md` uses YAML frontmatter; reject `..`/separators in `name`.
- **L11** — demo two servers with the same tool name to justify `prefix`.
- **L12** — README predicate should use `i.get("command","")` (matches the eval).
- **L13** — compile patterns with `re.DOTALL`; add a false-positives note to the caveat.
- **L14** — state that post-hooks don't run on a blocked call.
- **L16** — add fixtures: a task with no `blockedBy` key; a dangling dependency.
- **L17** — `drain()` is best-effort; deadline-based join + `get_nowait`.
- **L19** — assert FIFO by sending two messages to one inbox.
- **L20** — assert the stored binding (so a stateless `allocate` fails).
- **L23** — branch on all three permission decisions (`ask` is currently auto-allowed);
  record a terminal event on `max_turns`; reuse L04 scorers in the eval.
- **Web** (`scripts/build_web.py`) — fix `lesson_title` acronyms (MCP/IO), add a
  `hashchange` listener, rewrite in-SPA `.md` links, persist language in the hash.
- **Docs** — call the glossary a "core-terms" glossary (or add the missing terms);
  reword duplicate RED/GREEN "Run it" commands as before/after.
- **Hygiene** — consider pinning `requirements.txt` upper bounds; optional
  `SECURITY.md`, `CODE_OF_CONDUCT.md`, issue/PR templates, `CHANGELOG.md`.
