# Ders 25 — Concurrency & Leases

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Yenilemediğin claim'i kaybedersin.*
>
> **Arc 7 — Production.** Ders 21'in `Lock`'una production cevabı.
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Ders 21, claim'i (üstlenme) in-process bir `Lock` ile atomic yaptı. Bu yalnızca **tek** bir process'teki thread'leri korur. Gerçek swarm'lar (sürüler) process'ler ve makineler arası çalışır — lock oraya ulaşmaz — ve daha kötüsü, bir ajan **claim'i tutarken çökebilir** ve task'ı sonsuza dek park eder. Production primitive'i bir **lease** (kira): bir **expiry (TTL)** ile gelen claim. Task'ı yalnızca lease'in canlıyken tutarsın; tutmaya devam etmek için yenilemelisin; ölürsen, expire olur ve başkası işi reclaim eder (geri alır).

```python
acquire(leases, "task-7", "A", now=0,  ttl=10)   # True  — A, t=10'a dek tutar
acquire(leases, "task-7", "B", now=5,  ttl=10)   # False — A'nın lease'i hâlâ canlı
acquire(leases, "task-7", "B", now=20, ttl=10)   # True  — A expire oldu; B reclaim eder
```

## Expiry neden bütün mesele

Expiry olmadan, çökmüş bir claimant'ın işi takılı kalır (L21'in `Lock`/`owner`'ı asla serbest kalmaz). TTL, "claimed"i "*şimdilik* claimed"e çevirir — dağıtık bir swarm'ı self-heal (kendi kendine iyileşen) yapan tam da budur. Gerçek sistemler bunu DB satırı + compare-and-set, Redis `SET NX PX` ya da bir cloud lease API ile destekler — ama semantik tam olarak budur.

## Ne kuracaksın

`is_held()` verilmiş. [`stub.py`](./stub.py) içinde `acquire(leases, task_id, agent, now, ttl)`'i uygula:

1. Bir lease varsa, **expire olmamışsa** (`expires > now`) ve **farklı** bir ajana aitse → `False` döndür.
2. Değilse `{"agent": agent, "expires": now + ttl}` kaydet ve `True` döndür.

## Çalıştır

```sh
python 25_concurrency_leases/eval.py                       # RED
python 25_concurrency_leases/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 25_concurrency_leases/eval.py
```

→ Sonraki: **Ders 26 — Human-in-the-Loop** (*bazı eylemler bir insanı bekler*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
