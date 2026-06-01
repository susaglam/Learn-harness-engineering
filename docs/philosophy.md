# Philosophy — Capability is latent; the harness realizes it

[English](./philosophy.md) | [Türkçe](./philosophy.tr.md)

## The thesis, stated carefully

> **Capability is latent in the model. The harness decides how much of it reaches the world. Agency is trained; realized agency is engineered.**

A model is a function shaped by gradient descent over vast text. Inside it lives an enormous amount of latent capability: reasoning, world knowledge, code fluency, judgment. But latent capability is not behavior. A model with no tools cannot act; with no memory cannot persist; with no context management drowns; with no recovery dies on the first error.

The **harness** is what converts latent capability into realized behavior. It is the model's sensory-motor system (tools), its working memory (context), its long-term memory (persistence), and its conscience (permissions). Change the harness and you change the agent — with the *same* model.

## Why we reject the older absolutism

A popular framing says: *"agency comes from the model, not the harness; harness engineers just build the vehicle."* This is half right and rhetorically self-defeating:

1. **Self-defeating.** If the harness didn't matter, there would be nothing to teach — yet the framing introduces twenty lessons of harness mechanisms. The contradiction is built in.
2. **Empirically wrong at the margin.** The *same* model, given good vs poor tools / context / recovery, produces dramatically different task success. That delta is engineering, not training.
3. **It hides the most important skill.** If you believe the harness is a passive vehicle, you never learn to *measure* it. Measurement is the whole game (see [methodology](./methodology.md)).

The honest version is a **partnership with a measurable boundary**: the model supplies intelligence; the harness supplies the action space, context, memory, and guardrails; their product is the agent. Neither alone ships.

## The feedback loop the old framing ignores

In 2025–2026, frontier agents are increasingly trained with reinforcement learning **on agentic trajectories** — real sequences of perceive → reason → act in tool-using environments. This means:

> The harness you build today produces the trajectories that train tomorrow's model.

Harness design is therefore becoming *part of* model design. The boundary between "the intelligence" and "the environment" is no longer clean. A harness engineer who understands this designs not just for today's task success, but for the quality of the training signal their deployment generates.

## The orchestration spectrum (resolving the "is it a real agent?" fight)

A dogma in the field says hardcoded workflows are "fake agents" and only fully model-driven systems are "real." This is a false binary. Every serious system sits somewhere on a spectrum:

```
 deterministic <──────────────────────────────────────────────> autonomous
 (scripted control flow)                                         (model decides)

 choose deterministic for:              choose autonomous for:
   reliability                            open-ended judgment
   low/predictable cost                   novel solution paths
   auditability & compliance              adaptation to surprise
   safety-critical steps                  creativity
```

The skill is **per-sub-problem placement**, not picking a tribe. Pin the steps that must be reliable; delegate the steps that must be smart. A great agent is usually a *deterministic skeleton with autonomous muscles* — a reliable outer loop that calls model judgment exactly where judgment pays off. Lesson 22 makes this concrete by solving one task at three points on the axis and scoring the trade-offs.

## What this means for you

You are not writing intelligence. You are building — and **measuring** — the world that intelligence inhabits. Build that world well, prove it works, and the model will do the rest.

← Back to [README](../README.md) · next: [methodology](./methodology.md)
