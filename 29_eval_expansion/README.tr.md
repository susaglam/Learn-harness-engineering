# Ders 29 — Eval Expansion

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Vibe değil, yörünge notla — bütçelerle.*
>
> **Arc 7 — Production.** Ders 04'ün yetişkin hâli ve kursun son sözü.
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Ders 04 tek gerçekleri notluyordu ("bash çağırdı mı?"). Production grading (notlama) daha zor sorular sorar ve bunları birçok koşum üzerinde otomatik sorar:

- **Golden trajectory** (altın yörünge) — koşum *gerekli tool dizisini, sırayla* yakaladı mı? (Search → read → write, write → search değil.) Ekstra adımlar sorun değil; eksik ya da sırasız gerekli adımlar sorundur.
- **Budgets** (bütçeler) — bir **step** ve **cost** tavanının altında kaldı mı? Doğru cevabı 50 pahalı çağrıda bulan bir ajan yine de bir regresyondur.

```python
matches_golden(traj, ["search", "read", "write"])   # sıralı subsequence mı?
within_budget(traj, max_steps=10, max_cost=5)        # tavanların altında mı?
```

## Bu kursu neden kapatır

Tüm müfredat eval-driven; bu ders sana gerçek bir ekibin CI'da koştuğu scorer'ları verir: golden trajectory *davranışsal* regresyonları, bütçeler *cost/latency* regresyonlarını yakalar ve birlikte bir regression dashboard'u beslerler. Kursun açıldığı tezin aynısı — **ölçülebilir bir ajan, ihtiyacın olan tek şeydir** — bir ajanı production'da ölçülebilir tutan araçlara dönüşmüş hâli.

## Ne kuracaksın

[`stub.py`](./stub.py) içinde bir trajectory (event dict listesi) üzerinde iki scorer uygula:

- `matches_golden(traj, golden_tools)` → golden tool'lar, `tool_call` adlarının *sıralı subsequence*'i mi?
- `within_budget(traj, max_steps, max_cost)` → step sayısı ve toplam `cost`, (opsiyonel) limitlerin altında mı?

## Çalıştır

```sh
python 29_eval_expansion/eval.py                       # RED
python 29_eval_expansion/eval.py                       # GREEN (TODO'lardan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 29_eval_expansion/eval.py
```

Sona geldin. Yirmi dokuz ders, tek loop, her biri yeşile çevirdiğin bir kırmızı testle kanıtlandı — oyuncak mekanizmalardan geçip production sınırlarına çıktın. **Ölçülebilir bir ajan, ihtiyacın olan tek şeydir.**

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
