# Lesson 09 — Memory & Retrieval

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Remember what matters; retrieve when relevant.*

## The idea

Context is wiped each session (Lesson 07 even compacts it mid-run). **Memory** is what survives: facts you persist to disk. But a useful memory isn't "load everything every time" — that just refills the context you worked to protect. The trick is **retrieval**: store many facts, and at each step pull back only the few that are *relevant to the current query*.

Relevance by **meaning**, not keyword match, is what makes it feel intelligent. We approximate it with a tiny bag-of-words **embedding** and **cosine similarity** so the lesson is offline and deterministic — production swaps in real model embeddings, but the mechanism is identical.

```python
mem.add("The Eiffel Tower is in Paris.")
mem.recall("Where is the Eiffel Tower?", k=1)   # -> ["The Eiffel Tower is in Paris."]
```

## Why retrieval, not "load all"

A real agent accumulates thousands of facts. Injecting all of them would blow the budget *and* drown the signal. Retrieval keeps memory unbounded while keeping each prompt small — you spend context only on what's relevant now. This is the engine behind RAG.

## What you'll build

`embed()`, `cosine()`, and `add()` are given. In [`stub.py`](./stub.py), implement `MemoryStore.recall(query, k)`:

1. Embed the query.
2. Sort stored items by `cosine(query_vec, item_vec)` descending.
3. Return the texts of the top `k`.

## Run it

```sh
python 09_memory_retrieval/eval.py                       # RED
python 09_memory_retrieval/eval.py                       # GREEN (after the TODO)
# reference check (PowerShell): $env:LHE_SOLUTION=1; python 09_memory_retrieval/eval.py
```

→ Next: **Lesson 10 — Skill Loading** (*load knowledge on demand, not upfront*).

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
