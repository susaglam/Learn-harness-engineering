# Lesson 10 — Skill Loading

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Load knowledge on demand, not upfront.*

## The idea

An agent might need to know how to process PDFs, query a database, follow your deploy checklist — dozens of specialized procedures. Stuffing all of that into the system prompt wastes context (Lesson 07) and distracts the model. A **skill** is a package of knowledge stored on disk. Only its one-line **manifest** entry stays in context; the full body is **loaded on demand** when the agent decides it's relevant.

```
manifest (always present, cheap):
  - pdf: Extract text and tables from PDF files.
  - csv: Parse and summarize CSV files.

load("pdf")  ->  the full procedure, injected only now
```

## Why this is the same idea as retrieval

Lesson 09 retrieved *facts* by relevance; this retrieves *procedures* by name. Both follow the rule: keep the index small and always-present, fetch the heavy content only when needed. Progressive disclosure is how you give an agent vast capability without a vast prompt.

## What you'll build

`manifest()` (the cheap listing) is given. In [`stub.py`](./stub.py), implement `load(name)`:

1. Build the path `skills_dir/name/SKILL.md`.
2. If it's not a file → return `f"ERROR: unknown skill '{name}'"`.
3. Otherwise read and return the full text.

## Run it

```sh
python 10_skill_loading/eval.py                       # RED
python 10_skill_loading/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 10_skill_loading/eval.py
```

> **Note:** real Claude `SKILL.md` files put the description in a YAML frontmatter
> `description:` field; we use the first non-heading line to keep parsing trivial.
> A hardened loader also rejects names with path separators or `..` — no traversal
> outside `skills_dir` (cf. **Lessons 13 & 24**).

→ Next: **Lesson 11 — MCP** (*borrow capabilities; keep one tool pool*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
