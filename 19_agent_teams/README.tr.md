# Ders 19 — Agent Teams & Protocols

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Tek ajana büyük gelen iş → koordinasyon.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Bir subagent (Ders 08) tek bir işi yapar ve kaybolur. Bazı işler yan yana çalışıp konuşan *kalıcı* takım arkadaşları (teammates) ister: bir araştırmacı, bir coder, bir reviewer. Bunlar bir **MessageBus** üzerinden koordine olur — her ajanın bir **inbox**'ı (gelen kutusu) vardır, mesajlar **alıcıya göre route edilir** (yönlendirilir) ve sabit bir **protocol** (protokol — bir mesaj biçimi, örn. `request` / `reply`) üzerinde anlaşırlar ki herkes herkesi anlayabilsin.

```python
bus.send(to="B", frm="A", type="request", body="ping")
for msg in bus.recv("B"):          # B inbox'ını okur
    bus.send(to=msg["from"], frm="B", type="reply", body="pong")
bus.recv("A")                      # A yanıtı alır
```

## Neden bir bus + bir protocol

- **Alıcıya göre routing**, göndericileri alıcılardan decouple eder (ayrıştırır) — A, B'yi doğrudan çağırmaz, bir mesaj bırakır; B kendi programında okur. Eşzamansız, çoktan-çoğa koordinasyonu yönetilebilir kılan budur.
- **Protocol** (paylaşılan mesaj biçimi), sosyal sözleşmedir: anlaşılmış bir `type`/`from`/`body` olmadan takım arkadaşları birbirini güvenilir biçimde yorumlayamaz. Ders 16'nın task graph'ı artı bu bus, Ders 21'deki kendi-kendini-örgütleyen ajanların alt katmanıdır.

## Ne kuracaksın

[`stub.py`](./stub.py) içinde `MessageBus` mailbox'ını uygula:

- `send(to, frm, type, body)` → `self.inboxes[to]`'a `{"to","from","type","body"}` ekle.
- `recv(who)` → `who`'nun tüm mesajlarını döndür ve o inbox'ı boşalt (deliver-once, FIFO).

## Çalıştır

```sh
python 19_agent_teams/eval.py                       # RED
python 19_agent_teams/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 19_agent_teams/eval.py
```

→ Sonraki: **Ders 20 — Worktree Isolation** (*her ajana kendi odası*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
