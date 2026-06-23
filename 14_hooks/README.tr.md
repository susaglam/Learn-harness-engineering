# Ders 14 — Hooks

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Döngünün etrafını genişlet, döngüyü yazma.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Sürekli kesişen (cross-cutting) davranış eklemek isteyeceksin: her tool çağrısını logla, sonuçlardan sırları redakte et, Ders 12'deki permission kontrolünü uygula, yavaş tool'ları süre tut. Yanlış yol, loop'u okunmaz bir yumağa dönene dek düzenlemektir. Doğru yol **hook'lar** (kancalar): dış fonksiyonların çalıştığı sabit extension point'ler (genişletme noktaları), loop'u el değmemiş bırakır.

- **PreToolUse** hook'ları bir tool'dan *önce* çalışır. Çağrıyı inceleyip **block** (engelleme) edebilirler.
- **PostToolUse** hook'ları bir tool'dan *sonra* çalışır. Sonucu **transform** (dönüştürme) edebilirler.

```python
@bus.on_pre
def guard(name, inp):
    if dangerous(inp): return "deny:blocked by guard"   # çağrıyı durdurur

@bus.on_post
def redact(name, inp, result):
    return scrub_secrets(result)                         # sonucu dönüştürür
```

## Bu neden genişletilebilirlik dikişi

Hook'lar, bir harness'in çürümeden büyümesinin yoludur. Permission'lar (Ders 12), injection taraması (Ders 13), tracing (Ders 04) ve memory yazımları — hepsi loop içine karışmış `if`'ler yerine birer *hook* olabilir. Loop, `call_tool_with_hooks`'u çağırır ve tam Ders 01'deki kadar basit kalır — her yeni yetenek eklemeli (additive) olur.

## Ne kuracaksın

`HookBus` verilmiş. [`stub.py`](./stub.py) içinde `call_tool_with_hooks(bus, name, tool_input, handler)`'i uygula:

1. Her pre-hook'u çalıştır; biri `"deny"` ile başlayan bir string döndürürse, handler'ı **ya da post-hook'ları çalıştırmadan** hemen `f"BLOCKED: {verdict}"` döndür.
2. Değilse `handler(**tool_input)`'i çalıştır.
3. Sonucu her post-hook'tan geçir (her biri dönüştürebilir), sonra döndür.

## Çalıştır

```sh
python 14_hooks/eval.py                       # RED
python 14_hooks/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 14_hooks/eval.py
```

→ Sonraki: **Ders 15 — Error Recovery** (*hata bir dal, çıkmaz sokak değil*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
