# Learn Harness Engineering

> **Build the environment that turns a model into a real agent — and measure it.**

[English](./README.md) | [Türkçe](./README.tr.md)

---

## The thesis

**Capability is latent in the model. The harness decides how much of it reaches the world.**

Agency is *trained* — but *realized* agency is *engineered*. A brilliant model behind a poor harness is a genius locked in a dark room: it can reason, but it cannot perceive, act, remember, or recover. The harness is not a passive "vehicle" the model drives. It is the model's **sensory-motor system and working memory** — and it sets the ceiling on how much of the model's latent capability ever becomes useful behavior.

This repository teaches you to build that harness, one mechanism at a time, and — crucially — to **measure** whether each mechanism actually helps.

### Why this framing matters

The older slogan "agency comes from the model, not the harness" is half-true and self-defeating: if the harness didn't matter, there would be nothing to teach. The honest version is a **partnership with a measurable boundary**:

- The model supplies **intelligence** (perception, reasoning, judgment).
- The harness supplies **the action space, the context, the memory, and the guardrails**.
- Their product — not either alone — is the agent you ship.

And there is a feedback loop the old framing ignores: in 2025–2026, agents are increasingly trained with reinforcement learning *on agentic trajectories*. The harness you build today shapes the data that trains tomorrow's model. **Harness design is becoming part of model design.**

---

## The orchestration spectrum (not a binary)

A common dogma says "real agents let the model decide everything; hardcoded workflows are fake agents." That is too absolute — and this curriculum's own later lessons (task graphs, team protocols, cron) *are* structured orchestration.

The truth is a spectrum:

```
 deterministic  <───────────────────────────────────────────>  autonomous
 (scripted)                                                     (model-driven)

 hardcode when you need:                  delegate to the model when you need:
   reliability, low cost,                   open-ended judgment, novel paths,
   auditability, safety                     adaptation, creativity
```

Good harness engineering is **choosing the right point on this spectrum for each sub-problem** — not picking a side. The final lesson is dedicated to making this choice well.

---

## The core pattern

Every lesson layers one mechanism on top of this loop. The loop never changes.

```python
def agent_loop(client, model, messages, tools, handlers, system=""):
    while True:
        resp = client.messages.create(
            model=model, system=system, messages=messages, tools=tools,
        )
        messages.append({"role": "assistant", "content": resp.content})

        if resp.stop_reason != "tool_use":
            return resp                      # the model is done

        results = []
        for block in resp.content:
            if block.type == "tool_use":
                output = handlers[block.name](**block.input)
                results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(output),
                })
        messages.append({"role": "user", "content": results})
```

The model decides when to call tools and when to stop. The harness just executes and feeds results back. **The loop belongs to the agent; everything you build around it belongs to the harness.**

---

## Methodology: eval-driven, not copy-driven

The old way: read a finished file, nod, move on. You learn nothing durable.

**Our way — every lesson is a failing test you make pass:**

```
1. Read  README.en.md / README.tr.md   → understand the mechanism and why it matters
2. Run   python <lesson>/eval.py        → RED (the eval fails; the harness is incomplete)
3. Edit  <lesson>/stub.py               → implement the 5–10 lines that matter (the TODO)
4. Run   python <lesson>/eval.py        → GREEN (you proved the mechanism works)
5. Diff  against reference.py            → compare your design with ours
```

Most evals run **without an API key** — they drive your harness logic with a scripted fake model, so you test the *engineering*, not the model. This is the single most important harness skill the field under-teaches: **if you can't measure it, you're not engineering — you're hoping.**

---

## Curriculum — 6 arcs, 23 lessons

Full list with mottos: **[CURRICULUM.md](./CURRICULUM.md)**.

| Arc | Theme | Lessons |
|---|---|---|
| **1. The Core** | the irreducible agent | Loop · Tool Use · System Prompt · **Eval & Observability** |
| **2. Doing Real Work** | turn intent into output | Planning · Structured I/O · Context & Token Economics · Subagents |
| **3. Knowledge & Memory** | know things, recall things | Memory & Retrieval · Skill Loading · MCP |
| **4. Hardening** | make it safe and robust | Permissions · **Security & Injection** · Hooks · Error Recovery |
| **5. Scale** | long-running, many agents | Task Graphs · Background · Cron · Teams · Worktrees · Autonomous |
| **6. Synthesis** | put it together, honestly | **The Orchestration Spectrum** · Comprehensive Agent |

**Bold** = topics the predecessor course was missing. Two early moves matter most: **System Prompt** and **Evaluation** come *first* (they frame everything); **Permissions, Security, and Hooks** come *later*, grouped as a "hardening" arc — you harden an agent that already does useful work, not before.

---

## Quickstart

```sh
git clone <your-fork-url> learn-harness-engineering
cd learn-harness-engineering
python -m venv .venv && . .venv/Scripts/activate   # Windows: .venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .env.example .env                                # add your API key (any Anthropic-compatible provider)

# Lesson 1: most evals need NO API key — they use a scripted fake model.
python 01_agent_loop/eval.py        # RED
#   ...implement the TODO in 01_agent_loop/stub.py...
python 01_agent_loop/eval.py        # GREEN

# Run EVERY lesson's eval at once (exactly what CI runs):
python run_all_evals.py

# Optional: build a browsable offline preview of all lessons (EN/TR):
python scripts/build_web.py         # then open web/index.html

# To run a lesson against a real model:
python 01_agent_loop/reference.py
```

---

## Project structure

```
learn-harness-engineering/
  README.md / README.tr.md        # this file (EN / TR)
  CURRICULUM.md / .tr.md          # the full 23-lesson map
  docs/
    philosophy.md / .tr.md        # the thesis & the orchestration spectrum, in depth
    methodology.md / .tr.md       # the eval-driven teaching method, in depth
  harness/                        # shared, provider-agnostic infrastructure
    client.py                     #   build an Anthropic-compatible client from .env
    loop.py                       #   the canonical agent loop (lessons 2+ import this)
    evals.py                      #   a tiny RED/GREEN eval runner
  01_agent_loop/                  # each lesson: README.en/tr + reference + stub + eval
    README.en.md / README.tr.md
    reference.py                  #   complete implementation
    stub.py                       #   you implement the TODO
    eval.py                       #   fails until your stub is correct
  02_tool_use/ ... 23_comprehensive/
  skills/                         # example SKILL.md packages Lesson 10 can load (+ demo.py)
  scripts/                        # scaffold_lessons.py, build_web.py
  web/                            # generated single-file preview (web/index.html, git-ignored)
  run_all_evals.py                # run every lesson's eval (RED stub -> GREEN reference)
  .github/workflows/test.yml      # CI: runs run_all_evals.py on push / PR
```

---

## Languages

This initial version ships in **English** and **Türkçe** only. Other translations may follow once the curriculum stabilizes — deliberately, to avoid the two-track drift that plagued the predecessor.

## License

MIT.

---

**The model brings the intelligence. You build the world it acts in — and you prove that world works. A measurable agent is all you need.**
