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

The second-reviewer roadmap is fully shipped as eval-verified lessons **24–29**
(EN/TR): Secrets/Sandboxing & Audit, Concurrency & Leases, Human-in-the-Loop,
Tool-Result Management, Versioning & Migration, Eval Expansion. Production-bridge
"Toy → production" callouts link the sharpest Arc 1–6 lessons to their hardened
counterpart (L07→L27, L13→L24, L18→L25, L21→L25), and each Arc 7 lesson links
back to the toy it grows up from.

---

## Backlog — cleared

Every confirmed item from the multi-agent audit has been addressed:

- **Evals hardened** (no longer gameable): L04, L07, L09, L11, L13, L17, L21, L22, L23.
- **Eval rigor added**: L05 `.strip()`, L06 first-feedback, L11 multi-server prefix,
  L16 dangling-dep / no-`blockedBy`, L19 FIFO, L20 stored-binding, L10 path-traversal.
- **Correctness**: L01 empty-turn guard, L10 traversal guard, L13 `re.DOTALL`,
  L15 unclassified-error fallback, L18 one-shot interval, L21 atomic `Lock`,
  L23 three-way permission + `exhausted` trace; runner RED-signal + loop guards.
- **Prose**: L12 predicate, L13 false-positives, L14 post-hook contract, L10 YAML note,
  cross-platform Quickstart, accurate import/claims, MODEL_ID, lesson counts,
  glossary "core-terms" wording, "loop never changes" softening.
- **Tooling / hygiene**: `run_all_evals.py` + CI, `CONTRIBUTING.md`, `.editorconfig`,
  `SECURITY.md`, `CODE_OF_CONDUCT.md`, `CHANGELOG.md`, issue/PR templates, pinned
  `requirements.txt` (dropped unused `pyyaml`), `scaffold_lessons.py` covers 24–29,
  web fixes (acronyms, link rewriting, hashchange, language-in-hash).

### Intentional simplifications (left as-is, by design)

- **L05** maps an unknown status to `pending` — input validation is L06's subject.
- **L17** `drain()` is best-effort (eval jobs finish instantly); a deadline join +
  `get_nowait` is the production form.
- **L23** keeps its own simple trajectory checks instead of importing L04's scorers
  (a capstone reads cleaner self-contained).
- The "Run it" blocks show the command twice (`# RED` then `# GREEN`) — the
  consistent repo convention; L01/L02 spell out the before/after in words.
