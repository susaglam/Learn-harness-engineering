# Ders 23 — The Comprehensive Agent

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Çok mekanizma, tek ölçülebilir döngü.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Burası bitiş noktası. Önceki her ders bir mekanizma ekledi; burada hepsi tek bir loop'ta birleşir — ve bir eval tüm şeyin uçtan uca (end-to-end) çalıştığını kanıtlar. Bu koşum şunları birbirine bağlar:

- **agent loop** (Ders 01),
- bir **tool registry / dispatch** (Ders 02),
- bir **permission gate** (izin kapısı, Ders 12), ve
- bir **trajectory tracer** (yörünge izleyici, Ders 04),

böylece her tool çağrısı permission-kontrollü, dispatch edilen ve kaydedilen olur — ve *denied* (reddedilen) bir çağrı, modelin göremeyeceği bir eylem yerine kurtarılabilir bir geri bildirime (`DENIED: ...`) dönüşür.

```python
final = run_agent(client, model, messages, registry, permission, trace)
# write_file -> izinli, çalıştırıldı, trace edildi
# rm         -> reddedildi, asla çalıştırılmadı, "denied" olarak trace edildi
# loop iki tool_result'u geri besler, model bitirir, trace'te "final" olayı olur
```

## Loop neden hâlâ değişmedi

Gövdeye bak: Ders 01'in loop'u. Permission'lar, tracing, dispatch — hepsi tool çağrısının *etrafına* oturur, tam Ders 12/04/02'nin söylediği yere. Tez somutlaşır: loop ajana aittir ve asla değişmez; harness, etrafına dizdiğin her şeydir. Memory, hook, subagent, team'leri de aynı şekilde ekle — her biri bu tek loop'un etrafına oturan başka bir şey.

## Ne kuracaksın

`Registry`, `Trajectory` ve `extract_text` verilmiş. [`stub.py`](./stub.py) içinde `run_agent(client, model, messages, registry, permission, trace)`'i uygula:

1. Modeli `tools=registry.schemas` ile çağır; bir `model_turn` kaydet; assistant mesajını ekle.
2. Tool istemediyse bir `final` olayı kaydet ve dön.
3. Her `tool_use` bloğu için: `permission` `deny` derse `denied` kaydet ve bir `DENIED: ...` sonucu üret; değilse `tool_call` kaydet ve `registry.dispatch(...)`.
4. Tüm `tool_result`'ları tek bir user mesajı olarak geri besle ve döngüle.

## Çalıştır

```sh
python 23_comprehensive/eval.py                       # RED
python 23_comprehensive/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 23_comprehensive/eval.py
```

## Bitirdin

Yirmi üç mekanizma, tek loop, her biri yeşile çevirdiğin bir kırmızı testle kanıtlandı. Harness mühendisliğini okumadın — onu kurdun ve ölçtün. **Ölçülebilir bir ajan, ihtiyacın olan tek şeydir.**

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
