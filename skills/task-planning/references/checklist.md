# Planning checklist (reference)

A good plan is:

- **Verifiable** — each step has a clear "done" signal (a test passes, a file exists).
- **Ordered** — dependencies come first (reproduce before fix; fix before verify).
- **Small** — 3-7 steps; if a step hides 5 more, split it.
- **Visible** — re-rendered after every status change so the agent stays oriented.

Anti-patterns: a single mega-step ("implement the feature"), or 30 micro-steps
that bury the signal.
