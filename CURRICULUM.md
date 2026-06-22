# Curriculum — 7 Arcs, 29 Lessons

[English](./CURRICULUM.md) | [Türkçe](./CURRICULUM.tr.md)

Each lesson adds **one** harness mechanism on top of the unchanging agent loop, and ships as an eval-driven exercise (`README` → `eval.py` RED → `stub.py` → GREEN → compare `reference.py`). See [methodology](./docs/methodology.md).

**Status:** ✅ built and eval-verified (stub RED → reference GREEN, offline, no API key)

---

## Arc 1 — The Core *(the irreducible agent)*

| # | Lesson | Motto | What you build | Status |
|---|---|---|---|---|
| 01 | Agent Loop | *One loop, and the model drives* | The loop: feed tool results back so the model can continue | ✅ |
| 02 | Tool Use | *A new tool is just a new handler* | A dispatch map; add tools without touching the loop | ✅ |
| 03 | System Prompt | *The agent is configured before it speaks* | Runtime assembly of the system prompt from sections | ✅ |
| 04 | Eval & Observability | *If you can't measure it, you're hoping* | A trajectory tracer + scorers that grade agent runs | ✅ |

## Arc 2 — Doing Real Work *(turn intent into output)*

| # | Lesson | Motto | What you build | Status |
|---|---|---|---|---|
| 05 | Planning | *A plan turns intention into checkable steps* | A TodoWrite tool the agent uses to plan then execute | ✅ |
| 06 | Structured I/O | *Design the output the model has to read* | Schema-validated tool results + retry-on-mismatch | ✅ |
| 07 | Context & Token Economics | *Context is a budget; spend it deliberately* | Compaction strategies + a token budget meter | ✅ |
| 08 | Subagents | *Delegate the noise, keep the signal* | Spawn a child agent with fresh context; return only the result | ✅ |

## Arc 3 — Knowledge & Memory *(know things, recall things)*

| # | Lesson | Motto | What you build | Status |
|---|---|---|---|---|
| 09 | Memory & Retrieval | *Remember what matters; retrieve when relevant* | Persist facts + semantic recall (embeddings) | ✅ |
| 10 | Skill Loading | *Load knowledge on demand, not upfront* | A skill manifest; inject skill bodies only when needed | ✅ |
| 11 | MCP | *Borrow capabilities; keep one tool pool* | Route an external MCP server's tools into the loop | ✅ |

## Arc 4 — Hardening *(make it safe and robust)*

| # | Lesson | Motto | What you build | Status |
|---|---|---|---|---|
| 12 | Permissions & Trust | *Freedom needs boundaries to be safe* | A permission pipeline: allow / ask / deny | ✅ |
| 13 | Security & Injection | *Every token from outside is a potential adversary* | Quarantine untrusted content; detect injection attempts | ✅ |
| 14 | Hooks | *Extend around the loop, never rewrite it* | PreToolUse / PostToolUse extension points | ✅ |
| 15 | Error Recovery | *Failure is a branch, not a dead end* | A failure taxonomy + retry / fallback strategies | ✅ |

## Arc 5 — Scale *(long-running, many agents)*

| # | Lesson | Motto | What you build | Status |
|---|---|---|---|---|
| 16 | Task Graphs | *Big goals persist to disk as ordered tasks* | A file-backed task graph with `blockedBy` dependencies | ✅ |
| 17 | Background & Async | *Slow work goes async; the agent keeps thinking* | Threaded execution + a completion-notification queue | ✅ |
| 18 | Cron / Self-Scheduling | *The agent can wake itself* | Scheduled triggers fired by an injectable clock | ✅ |
| 19 | Agent Teams & Protocols | *Too big for one — coordinate many* | Persistent teammates + an async mailbox + a request/reply protocol | ✅ |
| 20 | Worktree Isolation | *Each agent gets its own room* | Bind tasks to git worktrees so parallel agents don't collide | ✅ |
| 21 | Autonomous Agents | *Agents that claim their own work* | An idle loop where agents self-claim work from a board | ✅ |

## Arc 6 — Synthesis *(put it together, honestly)*

| # | Lesson | Motto | What you build | Status |
|---|---|---|---|---|
| 22 | The Orchestration Spectrum | *Hardcode what must be reliable; delegate what must be smart* | The same task solved at 3 points on the determinism↔autonomy axis, scored | ✅ |
| 23 | Comprehensive Agent | *Many mechanisms, one measurable loop* | Assemble every mechanism around one loop, with evals proving it | ✅ |

## Arc 7 — Production *(where the toy meets the real world)*

| # | Lesson | Motto | What you build | Status |
|---|---|---|---|---|
| 24 | Secrets, Sandboxing & Audit | *Never let a secret reach the model or a log* | Redact known + secret-shaped values | ✅ |
| 25 | Concurrency & Leases | *A claim you don't renew, you lose* | A lease-with-TTL acquire (reclaim on expiry) | ✅ |
| 26 | Human-in-the-Loop | *Some actions wait for a human* | An approval-gated execute (pending / approved / denied) | ✅ |
| 27 | Tool-Result Management | *A 10MB result will blow your context* | Head+tail excerpt + artifact handle | ✅ |
| 28 | Versioning & Migration | *Long-lived state needs migrations* | An ordered record-migration chain | ✅ |
| 29 | Eval Expansion | *Grade trajectories, not vibes — with budgets* | Golden-trajectory + budget scorers | ✅ |

---

← Back to [README](./README.md)
