# Ders 28 — Versioning & Migration

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Uzun yaşayan state migration ister.*
>
> **Arc 7 — Production.** L09 memory / L10 skill / L16 task'lara zamanla ne olur.
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Aylarca çalışan bir ajan kalıcı state biriktirir — memory record'ları (L09), kaydedilmiş task graph'ları (L16), skill manifest'leri (L10). Sonra şemayı (schema) değiştirirsin. Diskteki her *eski* record artık yanlış biçimde. Loader yeni biçimi varsayarsa, ilk eski record'da çöker. Çözüm, veritabanlarının kullandığının aynısı: **versiyonlu record'lar + sıralı bir migration zinciri.** Her record bir `version` taşır; `migrate()`, en son sürüme ulaşmak için tam da hâlâ ihtiyacı olan upgrade adımlarını uygular.

```python
migrations = [v0_to_v1, v1_to_v2]          # en son sürüm == 2
migrate({"version": 0, ...}, migrations)   # iki adımı da çalıştırır -> sürüm 2
migrate({"version": 1, ...}, migrations)   # yalnızca 2.'yi          -> sürüm 2
migrate({"version": 2, ...}, migrations)   # zaten güncel            -> değişmez
```

## Neden record'un kendi sürümünden başla

Naif bir versiyonun görmezden geldiği iki hata: *yalnızca* en son migration'ı çalıştırmak (eski record'un hâlâ ihtiyacı olan adımları atlamak) onu bozar; zaten güncel bir record'a sıfırdan *tüm* adımları çalıştırmak çift-uygular ve onu diğer yönden bozar. `version` alanı, her record'un eksik olduğu adımları tam olarak almasını sağlar — ne fazla ne eksik.

## Ne kuracaksın

[`stub.py`](./stub.py) içinde `migrate(record, migrations)`'i uygula:

1. Record'u kopyala. `version < len(migrations)` olduğu sürece:
2. `migrations[version]`'ı uygula (`version` → `version+1`), sonra `version += 1`.
3. Yükseltilmiş record'u döndür.

## Çalıştır

```sh
python 28_versioning_migration/eval.py                       # RED
python 28_versioning_migration/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 28_versioning_migration/eval.py
```

→ Sonraki: **Ders 29 — Eval Expansion** (*vibe değil, yörünge notla — bütçelerle*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
