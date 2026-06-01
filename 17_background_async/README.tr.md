# Ders 17 — Background & Async

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Yavaş iş arka plana, ajan düşünmeye devam.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Bazı tool çağrıları yavaştır: dakikalarca süren bir build, büyük bir indirme, uzun bir test suite. Loop onlarda bloke olursa, ajan donar ve duvar-saati (wall-clock) yakarsın. Çözüm: yavaş işi bir **background thread**'inde (arka plan iş parçacığı) çalıştır, *hemen* bir handle (tutamak) döndür ve bittiğinde bir **notification** (bildirim) ilet. Ajan akıl yürütmeye (ya da başka işe) devam eder, sonucu hazır olunca alır.

```python
runner.start("build", run_build)     # anında döner, build arka planda çalışır
# ...ajan başka şeyler yapar...
for note in runner.drain():          # biten işleri topla
    handle(note["id"], note["result"])
```

## Neden bir notification queue

Background job ile ana loop eşzamanlı (concurrent) çalışır; bu yüzden güvenli bir devir gerekir: worker'ın (işçi) sonuçları koyduğu, loop'un drain ettiği (boşalttığı) thread-safe bir **queue** (kuyruk). İstisnaları sessizce ölmek yerine `ERROR: ...` sonucu olarak yakalamak, hataları *gözlemlenebilir* (Ders 04) ve *kurtarılabilir* (Ders 15) tutar — hiçbir şey post etmeyen çökmüş bir worker en kötü sonuçtur.

## Ne kuracaksın

`drain()` (join + topla) verilmiş. [`stub.py`](./stub.py) içinde `start(job_id, fn)`'i uygula:

1. `fn()`'i try/except içinde çağıran (`result = değer` ya da `f"ERROR: {exc}"`) ve `self.notifications`'a `{"id": job_id, "result": result}` `put` eden bir `run()` tanımla.
2. `run` üzerinde bir **daemon** thread başlat, `self._threads`'e ekle ve `job_id`'yi anında döndür.

## Çalıştır

```sh
python 17_background_async/eval.py                       # RED
python 17_background_async/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 17_background_async/eval.py
```

→ Sonraki: **Ders 18 — Cron / Self-Scheduling** (*ajan kendini uyandırabilir*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
