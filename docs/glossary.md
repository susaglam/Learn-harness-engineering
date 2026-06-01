# Glossary

[English](./glossary.md) | [Türkçe](./terminoloji.tr.md)

A beginner-friendly reference for the terms used across the course.

## Core
- **model / LLM** — the neural network that generates text; where "intelligence" comes from.
- **agent** — a system that perceives, reasons, and acts toward a goal: model + harness.
- **agency** — the capacity to perceive, decide, and act. *Trained* in the model; *realized* by the harness.
- **harness** — everything you build around the model: tools, knowledge, context management, memory, permissions.
- **agent loop** — ask the model → run any tools it requests → feed results back → repeat until it stops.
- **prompt** — the text you give the model. **system prompt** — the persistent instruction set at the start that configures behavior.
- **message** — one turn (`role` + `content`); the whole conversation is `messages[]`.
- **tool / tool use** — a function the model can invoke to act; the model *requests* a call, the harness executes it.
- **handler** — the code that performs a tool's work. **dispatch** — mapping a requested tool name to its handler.
- **stop_reason** — why the model stopped; `"tool_use"` means continue the loop, otherwise it's done.
- **tool_use / tool_result** — the model's "call this tool" block and the result block you feed back, linked by `tool_use_id`.

## Methodology
- **eval** — an automated check that the harness actually works.
- **RED / GREEN** — failing / passing test states; each lesson starts RED, you make it GREEN.
- **stub** — a deliberately incomplete file with a `TODO` for you to fill. **reference** — the complete solution.
- **fake / mock model** — a scripted stand-in so evals run deterministically without an API key.

## Context & tokens
- **token** — the smallest unit the model processes; the unit of cost and limits.
- **context / context window** — all the text the model sees at once; finite.
- **compaction** — summarizing old context to make room. **token economics** — managing cost/speed/quality within a budget.
- **latency** — time to get a response.

## Knowledge & memory
- **memory** — info that persists beyond a session. **retrieval** — fetching the relevant piece when needed.
- **RAG** — retrieval-augmented generation. **embedding** — a vector representing meaning, for semantic search.
- **skill** — an on-demand package of instructions + resources. **MCP** — Model Context Protocol; connect external tools into the tool pool.

## Hardening
- **permission** — rule for whether a tool may run / needs approval. **trust boundary** — line between trusted code and untrusted data.
- **prompt injection** — malicious instructions hidden in external content. **hook** — code that runs on events without changing the loop.
- **error recovery** — retry / make room / reroute on failure. **observability** — being able to see what the agent did (logs, traces, metrics).

## Scale & multi-agent
- **subagent** — a child agent that does side work in clean context and returns only the result.
- **task graph / DAG** — disk-persisted tasks with `blockedBy` dependencies.
- **background / async** — running slow work off the main thread. **cron** — time-triggered scheduling.
- **agent team / mailbox / protocol** — persistent agents coordinating via async messages and a fixed format.
- **worktree** — a separate working copy of a git repo so parallel agents don't collide.
- **autonomous agent** — one that claims its own work. **orchestration** — coordinating steps/agents along the deterministic↔autonomous spectrum.
- **trajectory** — the sequence of perceive→reason→act steps; raw material for training future models.

## Providers & API
- **API / API key** — the remote interface to the model / your secret credential (kept in `.env`).
- **provider** — who serves the model (Anthropic, GLM/Zhipu, Moonshot/Kimi, DeepSeek, MiniMax...).
- **base URL** — the server address; change it to target an **Anthropic-compatible** provider with the same code.

← Back to [README](../README.md)
