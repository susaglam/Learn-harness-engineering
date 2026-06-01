# Ders 06 — Structured I/O

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Modelin okuyacağı çıktıyı tasarla.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Serbest metin insanlar için iyidir; ama *senin kodun* modelin çıktısı üzerine işlem yapacaksa — bir dosya listesi, bir karar, bir JSON kaydı — o çıktıyı **makine-okur ve doğrulanmış (validated)** yapmalısın. Desen: bir schema (şema) tanımla, modelden onu iste, **validate** (doğrula) et ve uyumsuzlukta **hatayı geri ver** ki model bir sonraki denemede kendini düzeltsin (retry-on-mismatch: uyumsuzlukta yeniden deneme).

Bu, Ders 02'deki "hatalar veridir" içgüdüsünün aynısıdır: bir doğrulama hatası ölümcül değil, geri bildirimdir.

```python
schema = {"name": str, "score": int}
obj, attempts = request_structured(ask_model, schema)   # geçerli olana dek yeniden dener
```

## Geri-bildirimli retry neden "parse et ve dua et"i yener

Modeller bazen bozuk JSON üretir ya da bir alanı atlar. Sadece `json.loads` yapıp çökersen, tek bir olasılıksal kayma görevi öldürür. Bunun yerine *"çıktın geçersizdi: 'score' alanı eksik"* dersen, model neredeyse her zaman bir sonraki turda düzeltir. Sert bir hatayı ucuz bir retry ile takas etmiş olursun.

## Ne kuracaksın

`validate()` ve `parse_and_validate()` verilmiş. [`stub.py`](./stub.py) içinde `request_structured(model_fn, schema, max_retries)`'i uygula:

1. `max_retries`'e kadar döngü; ilk `feedback` `""`.
2. `text = model_fn(feedback)`; `parse_and_validate(text, schema)` dene → `(obj, attempt)` döndür.
3. `ValidationError`'da `feedback`'i hatayı içeren düzeltici bir mesaja ayarla, tekrar dene.
4. Hiç geçerli olmazsa `ValidationError` fırlat.

## Çalıştır

```sh
python 06_structured_io/eval.py                       # RED
python 06_structured_io/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 06_structured_io/eval.py
```

→ Sonraki: **Ders 07 — Context & Token Economics** (*context bir bütçedir; bilinçli harca*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
