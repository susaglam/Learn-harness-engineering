# Ders 07 — Context & Token Economics

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Context bir bütçedir; bilinçli harca.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Context window (bağlam penceresi) sonludur ve her token paraya ve gecikmeye (latency) mal olur. Uzun-soluklu bir ajan onu *mutlaka* doldurur. Bu yüzden harness'in **ipi kaybetmeden yer açma** yöntemine ihtiyacı vardır: compaction (sıkıştırma). En basit etkili strateji, **seed**'i (görev/sistem çerçevesi) ve **en son turları** tutar, bayatlamış ortayı kısa bir özet işaretçisiyle değiştirir.

Buradaki token sayımı `~4 karakter = 1 token` kaba vekiliyle (proxy) yapılır ki ders çevrimdışı ve deterministik kalsın; production'da modelin gerçek tokenizer'ını ve (kritik olarak) prompt caching kullanarak sabit önekleri (prefix) tekrar ödememelisin.

```python
if total_tokens(messages) > budget:
    messages = compact(messages, budget, keep_recent=2)
```

## Neden "seed + recent + özet"

- **Seed** hedefi tutar; kaybedersen ajan ne yaptığını unutur.
- **Son turlar** canlı çalışma durumunu tutar.
- **Orta** genelde sıkıştırmaya güvenlidir — hâlâ önemli olan kilit gerçekleri ya son turlara taşınmıştır ya da hafızaya (Ders 09) yazılmış olmalıydı.

## Ne kuracaksın

Token tahmincileri verilmiş. [`stub.py`](./stub.py) içinde `compact(messages, budget, keep_recent)`'i uygula:

1. Bütçenin altındaysa listeyi değiştirmeden döndür.
2. Değilse `messages[:1]` + bir özet işaretçisi + `messages[-keep_recent:]` tut.

## Çalıştır

```sh
python 07_context_economics/eval.py                       # RED
python 07_context_economics/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 07_context_economics/eval.py
```

→ Sonraki: **Ders 08 — Subagents** (*gürültüyü devret, sinyali tut*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
