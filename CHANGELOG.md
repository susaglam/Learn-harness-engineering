# Changelog

All notable changes to this course. Format loosely follows
[Keep a Changelog](https://keepachangelog.com/). Lessons are eval-driven:
every entry keeps `python run_all_evals.py` green.

## [0.2.0] — Arc 7: Production

### Added
- **Arc 7 — Production** (Lessons 24–29): Secrets/Sandboxing & Audit,
  Concurrency & Leases, Human-in-the-Loop, Tool-Result Management,
  Versioning & Migration, Eval Expansion. The curriculum is now **7 arcs,
  29 lessons** (EN/TR), each with a cheat-rejecting offline eval.
- "Toy → production" callouts linking Arc 1–6 lessons to their Arc 7 counterparts.
- `CONTRIBUTING.md`, `.editorconfig`, `SECURITY.md`, `CODE_OF_CONDUCT.md`,
  issue / PR templates, this changelog.

### Changed / Fixed (audit hardening)
- Hardened nine evals that a wrong/cheating stub could previously pass
  (L04, L07, L09, L11, L13, L17, L21, L22, L23).
- `run_all_evals.py` now distinguishes a real RED from a crashed eval;
  `harness/loop.py` guards the empty tool-turn and raises on `max_turns`.
- Correctness: L15 unclassified-error fallback, L18 non-positive-interval
  one-shot (no infinite loop), L21 atomic claim via `Lock`, L10 rejects
  path-traversal skill names, L01 guards the empty tool-turn.
- Docs: cross-platform Quickstart, accurate import/claims, MODEL_ID
  consistency, lesson-count and "loop never changes" wording.

## [0.1.0] — Initial curriculum

### Added
- 6 arcs, 23 eval-driven lessons (EN/TR): the agent loop through the
  comprehensive agent, each `README.en/tr` + `reference` + `stub` + `eval`.
- Shared `harness/` (client, loop, evals), `run_all_evals.py`, CI workflow,
  example `skills/`, and a static `web/` preview generator.
