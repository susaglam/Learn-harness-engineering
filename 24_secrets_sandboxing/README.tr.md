# Ders 24 — Secrets, Sandboxing & Audit

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Bir secret'ın (sır) modele ya da log'a ulaşmasına asla izin verme.*
>
> **Arc 7 — Production.** Bu dersler, Ark 1–6'nın oyuncak mekanizmalarının gerçek
> dünya kısıtlarıyla buluştuğu yeri işaretler.
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Ajanın credential'larla (kimlik bilgileri) çalışır: `.env`'deki API key, bir tool'un döndürdüğü token, okuduğu bir config'deki parola. Bunların herhangi biri bir prompt'a, bir tool sonucuna ya da log'ladığın bir trajectory'ye (Ders 04) sızabilir — ve bir secret bir kez log'a ya da model sağlayıcısına gittiğinde, ele geçirilmiş demektir. Savunma **sınırda redaction** (maskeleme): modele ya da log'a geçen her şeyden secret'ları temizle.

Yakalanacak iki tür secret:

- **Bilinen** değerler — kodunun enjekte ettiği/aldığı parola/key'ler. Literali maskele.
- **Bilinmeyen ama secret-*biçimli*** — `sk-…`, `ghp_…`, `AKIA…`. Değeri önceden bilmesen de pattern (desen) ile yakala.

```python
redact("key sk-ABCD1234EFGH and pw hunter2", known_secrets=["hunter2"])
# -> "key ***REDACTED*** and pw ***REDACTED***"
```

## Neden iki yarı da gerekli

Sadece-bilinen maskeleme, bir tool'un yeni çektiği token'ı kaçırır; sadece-pattern, key-biçimli olmayan kendi parolanı kaçırır. İkisi de gerekir — ayrıca gerçek bir sistemde: least-privilege credential scoping (en az yetkiyle kimlik kapsamı), `bash` için shell **sandbox**, ve ne çalıştığının **audit trail**'i (denetim izi). Bu ders redaction çekirdeğini kurar; gerisi production checklist'i.

## Ne kuracaksın

[`stub.py`](./stub.py) içinde `redact(text, known_secrets)`'i uygula:

1. `known_secrets`'taki her değeri `MASK` ile değiştir.
2. `_SECRET_PATTERNS`'taki her pattern'i `re.sub` ile `MASK`'le.
3. Temizlenmiş metni döndür.

## Çalıştır

```sh
python 24_secrets_sandboxing/eval.py                       # RED
python 24_secrets_sandboxing/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 24_secrets_sandboxing/eval.py
```

→ Sonraki: **Ders 25 — Concurrency & Leases** (*yenilemediğin claim'i kaybedersin*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
