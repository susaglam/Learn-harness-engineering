# Ders 15 — Error Recovery

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Hata bir dal, çıkmaz sokak değil.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Gerçek tool'lar başarısız olur: ağlar zaman aşımına uğrar, API'ler rate-limit uygular, dosyalar kaybolur, model çöp döndürür. Naif bir harness ilk hatada çöker ve tüm koşumu kaybeder. Sağlam olan ise **hatayı sınıflandırır ve tepki verir**:

- **Transient** (geçici — timeout, rate limit, kararsız ağ) → **retry** (yeniden dene), belki backoff'la.
- **Permanent** (kalıcı — bozuk input, bulunamadı, yetki reddi) → retry'ı boşa harcama; **fallback** (yedek: bir default, daha basit bir yol ya da insana yükselt).

Recovery (kurtarma), sona eklenen bir düşünce değildir — bir demo ile gözetimsiz çalışmasına güvendiğin bir şey arasındaki farktır.

```python
value, info = run_with_recovery(call_api, fallback=use_cache, max_retries=3)
# info -> {"outcome": "ok", "attempts": 2}  veya  {"outcome": "fallback", "reason": "permanent"}
```

## Neden sınıflandır, "her şeyi yeniden dene" değil

*Permanent* bir hatayı yeniden denemek saf israftır — kullanıcı beklerken üç kez daha aynı şekilde başarısız olur. *Transient* olanı yeniden denemek tam doğrudur. Taxonomy (sınıflandırma), policy'nin (politika) her biri için doğru şeyi yapmasını sağlar. Yapılandırılmış `info` döndürmek (Ders 04'e bağlanarak) recovery'nin kendisini gözlemlenebilir kılar.

## Ne kuracaksın

`TransientError` / `PermanentError` taksonomisi verilmiş. [`stub.py`](./stub.py) içinde `run_with_recovery(fn, fallback, max_retries)`'i uygula:

1. `attempt`'i 1'den `max_retries`'e döngüle; `try` ile `(fn(), {"outcome": "ok", "attempts": attempt})` döndür.
2. `TransientError`'da `continue` (yeniden dene).
3. `PermanentError`'da `(fallback(), {"outcome": "fallback", "reason": "permanent", "attempts": attempt})` döndür.
4. Döngü tükenirse `(fallback(), {"outcome": "fallback", "reason": "exhausted", "attempts": max_retries})` döndür.

## Çalıştır

```sh
python 15_error_recovery/eval.py                       # RED
python 15_error_recovery/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 15_error_recovery/eval.py
```

→ Sonraki: **Ders 16 — Task Graphs** (*büyük hedef diske sıralı task olur*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
