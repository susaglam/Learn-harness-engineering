# Ders 04 — Eval & Observability

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Ölçemiyorsan umuyorsun demektir.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Bu, en az öğretilen harness becerisidir; o yüzden erken gelir — kendinden sonraki her dersi çerçeveler. İki yarısı var:

- **Observability (gözlemlenebilirlik):** ajanın yaptığı her şeyi bir **trajectory** (yörünge) olarak kaydet — sıralı bir olay günlüğü (model turları, tool çağrıları, tool sonuçları, son cevap).
- **Evaluation (değerlendirme):** o trajectory'yi **scorer'larla** (puanlayıcılar) notla — şu soruları yanıtlayan küçük saf fonksiyonlar: *doğru tool'u çağırdı mı? son cevap beklenen bilgiyi içeriyor mu? kaç adımda yaptı?*

Bir harness hatası ile bir model hatası dışarıdan birebir aynı görünür. Trajectory ajanın davranışını *incelenebilir*, scorer'lar *ölçülebilir* yapar. İkisi birlikte "çalışıyor gibi"yi, değişiklikler arasında takip edebileceğin bir sayıya çevirir.

```python
traj = Trajectory()
# ...loop koşarken kaydeder...
traj.record("tool_call", name="bash", input={"command": "ls"})
traj.record("final", text="Done.")

assert used_tool(traj, "bash")          # davranış, kanıtlandı
assert step_count(traj) <= 5            # verimlilik, kanıtlandı
```

## Neden geri kalanından önce gelir

Sonraki her mekanizma (memory, teams, recovery), bir şeyin ajanı *iyileştirdiği* iddiasıdır. Scorer olmadan bunu söyleyemezsin. Tüm kurs tam da bu yüzden eval-driven: GREEN bir eval kanıttır; "his" değildir.

## Ne kuracaksın

`Trajectory` kaydedici verilmiş. [`stub.py`](./stub.py) içinde üç scorer uygula:

- `used_tool(traj, name)` → herhangi bir `tool_call` olayı bu tool'u kullandı mı?
- `final_contains(traj, substr)` → son `final` olayının metni `substr` içeriyor mu (büyük/küçük harf duyarsız)?
- `step_count(traj)` → kaç `tool_call` olayı oldu?

## Çalıştır

```sh
python 04_eval_observability/eval.py                       # RED
python 04_eval_observability/eval.py                       # GREEN (TODO'lardan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 04_eval_observability/eval.py
```

→ Sonraki: **Ders 05 — Planning** (*plan, niyeti kontrol edilebilir adıma çevirir*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
