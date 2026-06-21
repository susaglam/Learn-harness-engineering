# Ders 12 — Permissions & Trust

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Özgürlük güvenli olmak için sınır ister.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

`bash` tool'una sahip bir ajan her şeyi yapabilir — `rm -rf /` dahil. Artık **hardening** (sertleştirme) arkındayız: ajan zaten faydalı iş yapıyor; burada onu *güvenli* yapıyoruz. Mekanizma, her tool çağrısından önce çalışan ve onu üç karardan birine çözen bir **permission pipeline** (izin hattı):

- **allow** — sessizce çalıştır.
- **ask** — duraklat ve insan onayı iste.
- **deny** — reddet ve modele nedenini söyle (ki Ders 02'ye göre bu kurtarılabilir geri bildirime dönüşür).

Kararlar **sıralı bir ruleset'ten** (kural kümesi) gelir. Bir rule (kural), tool adıyla (ya da `*`) artı input üzerindeki opsiyonel bir predicate (yüklem/koşul) ile eşleşir ve **ilk eşleşen kazanır**. Eşleşmeyen her şey bir default'a düşer — ki bu `ask` veya `deny` olmalı, asla `allow` değil (deny-by-default güvenli duruştur).

```python
rules = [
    Rule("bash", "deny", when=lambda i: "rm -rf" in i.get("command", "")),  # önce spesifik tehlike
    Rule("bash", "allow"),                                          # sonra genel durum
    Rule("*",    "ask"),                                            # geri kalan: sor
]
resolve("bash", {"command": "rm -rf /"}, rules)   # -> "deny"
```

## Sıra ve default neden önemli

Dar, tehlikeli kuralı geniş allow'dan *önce* koymak, `rm -rf`'in deny olup `ls`'in allow olmasını sağlar. Default ise güvenlik ağındır: bir kuralı unutursan, deny-by-default açık değil kapalı (fail closed) başarısız olur.

## Ne kuracaksın

`Rule` verilmiş. [`stub.py`](./stub.py) içinde `resolve(tool_name, tool_input, rules, default)`'i uygula:

1. Kuralları sırayla dolaş; bir kural, tool'u `tool_name` ya da `"*"` ise **ve** (`when is None` ya da `when(tool_input)`) ise eşleşir.
2. İlk eşleşmenin `.decision`'ını döndür; hiçbiri eşleşmezse `default` döndür.

## Çalıştır

```sh
python 12_permissions/eval.py                       # RED
python 12_permissions/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 12_permissions/eval.py
```

→ Sonraki: **Ders 13 — Security & Injection** (*dışarıdan gelen her token potansiyel düşman*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
