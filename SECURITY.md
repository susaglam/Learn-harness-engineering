# Security Policy

This is an **educational** repository. The lessons are offline, eval-driven
exercises: they run against scripted *fake* models, make **no network calls**,
and hold **no live secrets** (the only credential is your own `ANTHROPIC_API_KEY`
in a git-ignored `.env`, used solely if you opt to run a `reference.py` against a
real model). Lesson 24 even teaches redacting secrets out of prompts and logs.

## Reporting a vulnerability

If you find a genuine security issue — for example, an `eval.py`/`reference.py`
that could execute untrusted input unsafely, a `bash`-tool example that escapes
its intended scope, or a dependency advisory — please **open a GitHub issue**
(or email the maintainer) with steps to reproduce. There is no bug bounty; this
is a learning project, but real reports are very welcome.

## Scope notes for learners

Several lessons deliberately ship *toy* security mechanisms and say so:
- **L13 (Security & Injection)** — heuristic detection is a tripwire, not a filter.
- **L12 (Permissions)** — a rule pipeline, not a sandbox.
- **L24 (Secrets, Sandboxing & Audit)** — redaction core; production needs
  credential scoping + a real sandbox + an audit trail.

Treat the toy versions as teaching scaffolds, not production controls.
