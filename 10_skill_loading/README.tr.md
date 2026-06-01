# Ders 10 — Skill Loading

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Bilgiyi talep üzerine yükle.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Bir ajanın PDF işlemeyi, bir veritabanını sorgulamayı, deploy checklist'ini takip etmeyi — onlarca özel prosedürü — bilmesi gerekebilir. Bunların hepsini system prompt'a tıkmak context'i (Ders 07) israf eder ve modeli dağıtır. Bir **skill** (yetenek paketi), diskte saklanan bir bilgi paketidir. Yalnızca tek-satırlık **manifest** (bildirim) girdisi context'te kalır; tam gövde, ajan ilgili olduğuna karar verince **talep üzerine (on-demand)** yüklenir (inject edilir).

```
manifest (her zaman mevcut, ucuz):
  - pdf: Extract text and tables from PDF files.
  - csv: Parse and summarize CSV files.

load("pdf")  ->  tam prosedür, yalnızca şimdi enjekte edilir
```

## Bu neden retrieval ile aynı fikir

Ders 09 *gerçekleri* ilgiye göre geri çağırıyordu; bu *prosedürleri* ada göre getirir. İkisi de aynı kurala uyar: index'i küçük ve her zaman mevcut tut, ağır içeriği yalnızca gerektiğinde getir. Progressive disclosure (kademeli açma), bir ajana devasa bir prompt olmadan devasa yetenek vermenin yoludur.

## Ne kuracaksın

`manifest()` (ucuz listeleme) verilmiş. [`stub.py`](./stub.py) içinde `load(name)`'i uygula:

1. `skills_dir/name/SKILL.md` yolunu oluştur.
2. Dosya değilse → `f"ERROR: unknown skill '{name}'"` döndür.
3. Değilse tam metni oku ve döndür.

## Çalıştır

```sh
python 10_skill_loading/eval.py                       # RED
python 10_skill_loading/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 10_skill_loading/eval.py
```

→ Sonraki: **Ders 11 — MCP** (*yeteneği ödünç al, tek havuzda tut*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
