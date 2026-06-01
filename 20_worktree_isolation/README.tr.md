# Ders 20 — Worktree Isolation

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Her ajana kendi odası.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Birkaç ajanı (Ders 19) *aynı* repository üzerinde çalıştırırsan birbirlerinin düzenlemelerini ezerler, working tree (çalışma ağacı) için kavga ederler ve koşumlarını bozarlar. Bir git **worktree** temiz çözümdür: aynı repository'nin birden çok dizine, her biri kendi branch'inde checkout edilmesi. Task başına bir worktree bağla (bind), paralel ajanlar asla çakışmaz — ayrı odalardadırlar.

Harness parçası **binding** (bağlama): `task_id → benzersiz bir dizin`, idempotent (aynı task hep aynı odaya döner) ve collision-free (iki task bir dizini paylaşmaz).

```python
reg.allocate("task-42")   # -> /agents/wt-task-42   (bir kez oluşturulur)
reg.allocate("task-42")   # -> aynı path (idempotent)
reg.allocate("task-99")   # -> farklı bir path (izole)
```

> Ders git'siz çalışsın diye yalnızca binding'i modelliyoruz. Production bir `allocate()` ayrıca `git worktree add <path> -b <branch>` çalıştırır, `release()` ise `git worktree remove`.

## Neden ID-dizin bağlaması

Isolation yalnızca *kararlıysa* faydalıdır: devam eden bir task, taze bir worktree'ye değil kendi worktree'sine dönmeli, yoksa in-progress state'ini (durumunu) kaybeder. Ve allocation collision-free olmalı, yoksa iki ajan aynı dizinde son bulur — tam da çözdüğümüz problem. Bu iki değişmez (invariant) — idempotent ve benzersiz — mekanizmanın tamamıdır.

## Ne kuracaksın

`release()` verilmiş. [`stub.py`](./stub.py) içinde `allocate(task_id)`'i uygula:

1. `task_id` zaten bağlıysa mevcut path'ini döndür.
2. Değilse `base_dir` altında benzersiz bir path oluştur (örn. `wt-<task_id>`), sakla ve döndür.

## Çalıştır

```sh
python 20_worktree_isolation/eval.py                       # RED
python 20_worktree_isolation/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 20_worktree_isolation/eval.py
```

→ Sonraki: **Ders 21 — Autonomous Agents** (*işini kendi çeken ajanlar*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
