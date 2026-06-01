# Ders 03 — System Prompt

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Ajan konuşmadan önce yapılandırılır.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

System prompt (sistem yönergesi), modelin ilk user mesajından *önce* aldığı talimat kümesidir — ajanın kim olduğunu ve nasıl davranacağını tanımlar. Yeni başlayan, tek büyük bir string'i sabit-kodlar. Bu, prompt'un bağlama (context) göre değişmesi gerektiği an kırılır: debug vs production, farklı bir persona (kişilik), yalnızca bazen mevcut olan bir tool, projeye özel bir kural.

Çözüm **runtime assembly** (çalışma-anı montajı): prompt'u, her biri opsiyonel bir koşula (condition) bağlı, adlandırılmış **section'lardan** (bölümlerden) oluşan bir liste olarak tut ve koşum başlarken uygun olanları birleştir. Aynı section'lar, farklı context → farklı prompt.

```python
prompt = (SystemPromptBuilder()
          .add("identity", "You are a coding agent.")
          .add("tools", "You can use bash.")
          .add("debug", "DEBUG MODE: be verbose.", when=lambda c: c.get("debug")))
system = prompt.build({"debug": is_dev})   # koşum başına montajlanır
```

## Section'lar neden tek büyük string'i yener

- **Koşullu davranış**, `if` çorbası olmadan: bir section yalnızca `when(context)` doğruyken görünür.
- **Composability (birleştirilebilirlik):** sonraki dersler runtime'da section enjekte eder — memory (Ders 9) "hatırladıkların" section'ı, skill'ler (Ders 10) "mevcut skill'ler" section'ı ekler — hepsi aynı builder'a.
- **Sıra anlamdır:** önce identity (kimlik), sonra yetenekler, sonra duruma özel kurallar. Builder ekleme sırasını korur, böylece prompt tutarlı okunur.

## Ne kuracaksın

[`stub.py`](./stub.py) içinde `SystemPromptBuilder.build(context)`'i uygula:

1. `self.sections`'ı sırayla dolaş.
2. Bir section'ı, `s.when is None` **ya da** `s.when(context)` doğruysa dahil et.
3. Dahil edilen her `s.text.strip()`'i topla ve `"\n\n"` ile birleştirip döndür.

## Çalıştır

```sh
python 03_system_prompt/eval.py                       # RED
#   ...stub.py içinde build()'i uygula...
python 03_system_prompt/eval.py                       # GREEN
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 03_system_prompt/eval.py
```

→ Sonraki: **Ders 04 — Eval & Observability** (*ölçemiyorsan umuyorsun demektir*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
