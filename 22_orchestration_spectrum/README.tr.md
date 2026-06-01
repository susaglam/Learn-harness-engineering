# Ders 22 — The Orchestration Spectrum

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Güvenilir olması gerekeni sabitle, akıllı olması gerekeni devret.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Bu ders, tüm kursun yöneldiği tartışmayı çözer. "Sabit-kodlu bir workflow *gerçek* bir ajan mı?" yanlış sorudur. Her sistem bir **spektrumda** yer alır ve iyi mühendislik, *her alt-problem için* doğru noktayı seçmektir:

- **Scripted** — deterministik kurallar. Ucuz, güvenilir, denetlenebilir; öngörmediğin her şeye karşı kırılgan (brittle).
- **Autonomous** — tüm görevi modele ver. Esnek ve uyarlanır; koşumdan koşuma değişen bir kara kutu.
- **Hybrid** — deterministik bir **skeleton** (iskelet — loop, aggregation, kontrol akışı) + tam yargının (judgment) değer kattığı noktalarda **delegated judgment** (devredilmiş yargı).

Tek bir görevi — *issue başlıkları listesindeki bug'ları say* — üç yolla çözüyoruz. Scripted keyword kuralı *"the page won't load at all"*ı (keyword'süz bir bug) kaçırır. Hybrid, güvenilir bir döngüle-ve-say iskeleti tutar ama her öğenin *yargısını* modele devreder; kara kutu olmadan paraphrase'i (başka sözcüklerle ifade) yakalar.

```python
classify_scripted(items)                 # bugs: 1   (paraphrase'i kaçırdı)
classify_hybrid(items, model_classify)   # bugs: 2   (öğe başına akıllı, genelde güvenilir)
```

## Hybrid neden genelde cevap

İyi bir ajan tipik olarak *deterministik bir iskelet + otonom kaslardır*: harness, güvenilir olması gereken kısımlara (iterasyon, retry, permission, aggregation) sahip olur ve modeli tam olarak açık-uçlu yargının maliyete ve varyansa değdiği yerde çağırır. Bu "daha az ajan" değil — önceki 21 dersin öğrettiği mühendislik olgunluğudur.

## Ne kuracaksın

`classify_scripted` ve `classify_autonomous` kıyas için verilmiş. [`stub.py`](./stub.py) içinde `classify_hybrid(items, model_classify)`'i uygula:

1. `items` üzerinde döngü kur (deterministik iskelet).
2. Her öğe için `model_classify(item)` çağır (devredilmiş yargı); `"bug"` say.
3. `{"bugs": count, "style": "hybrid"}` döndür.

## Çalıştır

```sh
python 22_orchestration_spectrum/eval.py                       # RED
python 22_orchestration_spectrum/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 22_orchestration_spectrum/eval.py
```

→ Sonraki: **Ders 23 — The Comprehensive Agent** (*çok mekanizma, tek ölçülebilir döngü*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
