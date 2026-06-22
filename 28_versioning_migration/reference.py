"""
Lesson 28 - Versioning & Migration  (reference implementation)

A long-lived agent's persisted state (memory records, skills, saved plans)
outlives the code that wrote it. When the schema changes, OLD records must be
upgraded, not crash the loader. `migrate()` applies an ordered chain of
migrations to bring any record up to the latest version. You build it.
"""
from __future__ import annotations


def migrate(record, migrations):
    """Upgrade `record` to the latest schema version.

    record: a dict with a "version" int. migrations: a list where migrations[v]
    is a function upgrading a v-record to v+1 (so the latest version is
    len(migrations)). Applies each step from record["version"] upward.
    """
    rec = dict(record)
    while rec.get("version", 0) < len(migrations):
        v = rec.get("version", 0)
        rec = migrations[v](rec)
        rec["version"] = v + 1
    return rec
