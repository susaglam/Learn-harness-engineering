# Ders 16 — Task Graphs

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Büyük hedef diske sıralı task olur.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

TodoWrite listesi (Ders 05) konuşmada yaşar ve onunla ölür. Uzun, çok-oturumlu ya da çok-ajanlı iş için daha sağlam bir şey gerekir: diske kalıcılaştırılmış bir **task graph** (görev grafiği); her task'ın `blockedBy` ile hangi başka task'ların önce bitmesi gerektiğini bildirdiği. Bu, "büyük bir hedefi" harness'in deterministik sürebileceği bir **DAG**'a (yönlü çevrimsiz grafik) çevirir.

Çekirdek sorgu **readiness** (hazırlık): *şu an hangi task'lar çalışabilir?* — hâlâ `pending` olan ve her bağımlılığı (dependency) zaten `completed` olanlar.

```python
tasks = [
    {"id": "A", "status": "pending",   "blockedBy": []},
    {"id": "B", "status": "pending",   "blockedBy": ["A"]},   # A'yı bekler
]
next_ready(tasks)   # -> [A]   (B, A bitince açılır)
```

## Neden disk + bağımlılıklar

- **Disk**, planın bir çökmeden, yeni bir oturumdan ya da başka bir ajana devredilmekten sağ çıkması demektir — sonraki çok-ajan derslerinin zemini.
- **Bağımlılıklar**, gerçek yapıyı ifade etmeni ("testler geçmeden deploy edilemez") ve sıralı *olmayan* her şeyi güvenle paralelleştirmeni sağlar. `next_ready`, Ders 21'de ajanların çekeceği scheduler'dır (zamanlayıcı).

## Ne kuracaksın

`save()` / `load()` (JSON kalıcılığı) verilmiş. [`stub.py`](./stub.py) içinde `next_ready(tasks)`'i uygula:

1. `done` = `completed` task'ların id kümesi.
2. Her `pending` task'tan, `blockedBy` id'lerinin hepsi `done` içinde olanı döndür.

## Çalıştır

```sh
python 16_task_graphs/eval.py                       # RED
python 16_task_graphs/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 16_task_graphs/eval.py
```

→ Sonraki: **Ders 17 — Background & Async** (*yavaş iş arka plana, ajan düşünmeye devam*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
