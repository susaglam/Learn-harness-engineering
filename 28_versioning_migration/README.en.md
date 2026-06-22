# Lesson 28 — Versioning & Migration

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Long-lived state needs migrations.*
>
> **Arc 7 — Production.** What happens to L09 memory / L10 skills / L16 tasks over time.

## The idea

An agent that runs for months accumulates persisted state — memory records
(L09), saved task graphs (L16), skill manifests (L10). Then you change the
schema. Every *old* record on disk is now the wrong shape. If the loader assumes
the new shape, it crashes on the first old record. The fix is the same one
databases use: **versioned records + an ordered migration chain.** Each record
carries a `version`; `migrate()` applies exactly the upgrade steps it still needs
to reach the latest.

```python
migrations = [v0_to_v1, v1_to_v2]          # latest version == 2
migrate({"version": 0, ...}, migrations)   # runs both steps  -> version 2
migrate({"version": 1, ...}, migrations)   # runs only the 2nd -> version 2
migrate({"version": 2, ...}, migrations)   # already current  -> unchanged
```

## Why start from the record's own version

Two failure modes a naive version ignores: running *only* the latest migration
(skipping the steps an old record still needs) corrupts it; running *all* steps
from zero on an already-current record double-applies and corrupts it the other
way. The `version` field is what makes each record get exactly the steps it's
missing — no more, no less.

## What you'll build

In [`stub.py`](./stub.py), implement `migrate(record, migrations)`:

1. Copy the record. While `version < len(migrations)`:
2. Apply `migrations[version]` (upgrades `version` → `version+1`), then set `version += 1`.
3. Return the upgraded record.

## Run it

```sh
python 28_versioning_migration/eval.py                       # RED
python 28_versioning_migration/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 28_versioning_migration/eval.py
```

→ Next: **Lesson 29 — Eval Expansion** (*grade trajectories, not vibes — with budgets*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
