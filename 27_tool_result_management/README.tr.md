# Ders 27 — Tool-Result Management

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *10MB'lık bir sonuç context'ini patlatır.*
>
> **Arc 7 — Production.** Tool'lar gerçekleşince Ders 07'nin bütçesinin çarptığı şey.
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Ders 07 *konuşmayı* bütçeledi. Ama tek bir tool çağrısı megabaytlarca log, dosya ya da sorgu sonucu döndürebilir — onu doğrudan geri beslemek bütçeyi tek hamlede patlatır, naif truncation (`text[:2000]`) ise *sonu* atar — ki hata veya cevap genelde oradadır. Production hamlesi:

1. Tam çıktıyı bir **artifact** (handle ile) olarak **store** et.
2. Modele **sınırlı bir alıntı** besle — head **ve** tail — artı bir omission marker (atlama işareti) ve handle; gerekirse gerisini çekebilsin.

```python
store_result(artifacts, "r1", huge_log)
summarize_result(huge_log, "r1", max_chars=200)
# -> "HEAD...\n...[8421 chars omitted; full result at artifact 'r1']...\n...TAIL"
```

## Neden head + tail + handle

Head sonucun *ne olduğunu* gösterir; tail *nasıl bittiğini* (stack trace, son sayım). Handle, tüm veriyi context'i şimdi harcamadan bir fetch uzakta tutar — skill'ler (L10) ve memory (L09) ile aynı progressive-disclosure fikri, tool çıktısına uygulanmış. Production structured summary ve provenance (hangi tool, ne zaman) ekler, ama yük taşıyan çekirdek budur.

## Ne kuracaksın

`store_result()` verilmiş. [`stub.py`](./stub.py) içinde `summarize_result(text, key, max_chars, keep)`'i uygula:

1. `len(text) <= max_chars` ise değiştirmeden döndür.
2. Değilse `text[:keep]` + bir omission marker (sayı + artifact `key`) + `text[-keep:]` döndür.

## Çalıştır

```sh
python 27_tool_result_management/eval.py                       # RED
python 27_tool_result_management/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 27_tool_result_management/eval.py
```

→ Sonraki: **Ders 28 — Versioning & Migration** (*uzun yaşayan state migration ister*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
