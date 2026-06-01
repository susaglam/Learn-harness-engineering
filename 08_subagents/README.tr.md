# Ders 08 — Subagents

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Gürültüyü devret, sinyali tut.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Bazı alt-görevler gürültülüdür: büyük bir ağaçta arama, on dosya okuma, üç yaklaşım deneme. Bütün bunlar ana konuşmada olursa, parent'ın (üst ajan) context'i ara-çöple dolar ve önemli ip kaybolur. Bir **subagent** (alt-ajan) bunu çözer: yalnızca alt-görevle *temiz* (fresh) bir loop başlat, dağınık işini izolasyonda (isolation) yapsın ve parent'a **yalnızca son sonucu** döndürsün.

```python
summary = run_subagent("src/ içindeki tüm TODO'ları bul ve özetle",
                       client, model, tools, handlers)
# parent görür: özeti. parent GÖRMEZ: 10 dosya okuma + müsvedde işi.
```

## Temiz context neden bütün mesele

İkisi de context (Ders 07) ile ilgili iki kazanç:

- **Isolation (izolasyon):** subagent yalnızca görevden başlar — parent'ın geçmişinden değil — yani dikkati dağılmaz, parent da subagent'in adımlarıyla kirlenmez.
- **Compression (sıkıştırma):** 30 adımlık bir araştırma, parent'ta tek paragrafa iner. Bu, sahip olduğun en ucuz ve en güçlü context-tasarrufudur.

## Ne kuracaksın

İç loop (`_run_loop`, Ders 01'in loop'u) ve `_extract_text` verilmiş. [`stub.py`](./stub.py) içinde `run_subagent`'i uygula:

1. **Temiz** bir konuşma başlat: `messages = [{"role": "user", "content": task}]` — parent'ın geçmişini geçirme.
2. Loop'u sonuna kadar çalıştır.
3. Yalnızca `_extract_text(final)`'i döndür — sonucu, gürültüyü değil.

## Çalıştır

```sh
python 08_subagents/eval.py                       # RED
python 08_subagents/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 08_subagents/eval.py
```

→ Sonraki: **Ders 09 — Memory & Retrieval** (*önemliyi hatırla, gerektiğinde geri çağır*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
