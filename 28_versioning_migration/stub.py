"""
Lesson 28 - Versioning & Migration  (YOUR implementation)

Implement migrate(record, migrations): apply the ordered migration chain to
bring `record` from its current version up to the latest.

Run:  python 28_versioning_migration/eval.py     # RED until the TODO is done
"""
from __future__ import annotations


def migrate(record, migrations):
    # =========================================================================
    # TODO(you):
    #   rec = dict(record)
    #   while rec["version"] < len(migrations):     # latest version == len(migrations)
    #       v = rec["version"]
    #       rec = migrations[v](rec)                 # upgrade v -> v+1
    #       rec["version"] = v + 1
    #   return rec
    # Start from the record's OWN version (don't re-run earlier migrations on an
    # already-current record, and don't skip the ones it still needs).
    # =========================================================================
    raise NotImplementedError("Implement migrate - see the TODO above")
