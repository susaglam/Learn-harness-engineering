# Ders 26 — Human-in-the-Loop

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Bazı eylemler bir insanı bekler.*
>
> **Arc 7 — Production.** Ders 12'nin `ask` kararının arkasındaki mekanizma.
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Ders 12 `ask` döndürebiliyordu ama aslında hiçbir şey *beklemiyordu*. Production'da yüksek-riskli bir eylem — deploy, silme, para gönderme — bir **insanı beklemeli (pause)** ve yalnızca onayla devam etmeli. Bu, bloke eden bir prompt değil, kalıcı state ister: eylemi **pending** (beklemede) park et, bir insan kendi programında **resolve** etsin (approve/deny), ve yürütmeyi (execution) o karara **gate**'le (kapıla). Ajan bu sırada başka işlerle uğraşmaya devam eder.

```python
request_approval(queue, "deploy-1", action)     # park edildi: pending
execute_if_approved(queue, "deploy-1", run)      # -> "PENDING" (hiçbir şey çalışmadı)
resolve(queue, "deploy-1", "approved")           # bir insan onaylar
execute_if_approved(queue, "deploy-1", run)      # -> eylemi çalıştırır
```

## Neden kuyruk, bloke eden prompt değil

Bloke eden bir "emin misin? (e/h)" ajanı dondurur ve process'le ölür. Bir **pending queue** (bekleyen kuyruk) restart'lardan sağ çıkar, onayların eşzamansız gelmesine izin verir ve pause / resume / cancel / rollback / escalation'a genelleşir — tam human-in-the-loop yüzeyi. Tek değişmez: **status `approved` olmadıkça `run()` asla çalışmamalı** (fail safe — pending/unknown asla yürütülmez).

## Ne kuracaksın

`request_approval()` ve `resolve()` verilmiş. [`stub.py`](./stub.py) içinde `execute_if_approved(queue, action_id, run)`'i uygula:

- status `approved` → `return run()` (çalıştırabilecek tek yol),
- status `denied` → `return "DENIED"`,
- değilse (pending / unknown) → `return "PENDING"`.

## Çalıştır

```sh
python 26_human_in_the_loop/eval.py                       # RED
python 26_human_in_the_loop/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 26_human_in_the_loop/eval.py
```

→ Sonraki: **Ders 27 — Tool-Result Management** (*10MB'lık bir sonuç context'ini patlatır*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
