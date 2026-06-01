# Ders 18 — Cron / Self-Scheduling

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Ajan kendini uyandırabilir.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Şimdiye kadar ajan yalnızca bir insan onu dürtünce eyledi. **Cron** bunu tersine çevirir: ajan kendi gelecekteki işini zamanlar (schedule) ve harness o job'ları (görevleri) vakti gelince tetikler — "her 30 saniyede yeni iş var mı bak", "her sabah siteyi audit'le". Her job bir `interval` (aralık) ve bir `next_run` zaman damgası taşır. Scheduler'ın (zamanlayıcı) çekirdek sorusu **şu an vakti gelen ne?**

Doğru yapılması gereken bir incelik: süreç uyuyorduysa ve saat birkaç tick'i (vuruş) atlayarak ilerlediyse, tetiklenen bir job her kaçırılan tick için tekrar tekrar değil, bir sonraki *gelecek* tick'e **catch-up** (yetişme) yapmalı.

```python
jobs = [{"id": "heartbeat", "interval": 30, "next_run": 0}]
due(jobs, now=100)     # -> [heartbeat];  jobs[0]["next_run"] artık 120 (yetişti)
```

> Zaman, saatten okunmak yerine `due(jobs, now)`'a *içeri* geçirilir — bu hem dersi deterministik tutar hem de iyi tasarımdır: enjekte edilebilir bir saat test edilebilirdir.

## Bu, bir tool'u neden asistana çevirir

Bu, always-on (sürekli açık) ajanların arkasındaki mekanizmadır: bir heartbeat job'ı ajanı bir kuyruğu kontrol etmek için uyandırır; cron job'ları zamanlanmış görevleri tetikler. Background execution (Ders 17) ve task graph'larla (Ders 16) birleşince, ajan "dürt de hareket etsin" olmaktan çıkıp "kendi kendine hareket eden" olur.

## Ne kuracaksın

[`stub.py`](./stub.py) içinde `due(jobs, now)`'i uygula:

1. `next_run <= now` olan her job'ı `fired`'a ekle.
2. O job'ın `next_run`'ını `interval` kadar, **gelecekte olana dek** (`> now`) tekrar tekrar ilerlet.
3. `fired`'ı döndür.

## Çalıştır

```sh
python 18_cron_scheduler/eval.py                       # RED
python 18_cron_scheduler/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 18_cron_scheduler/eval.py
```

→ Sonraki: **Ders 19 — Agent Teams & Protocols** (*tek ajana büyük gelen iş → koordinasyon*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
