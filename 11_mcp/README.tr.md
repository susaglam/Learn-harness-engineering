# Ders 11 — MCP

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Yeteneği ödünç al, tek havuzda tut.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Her tool'u kendin kurmak zorunda değilsin. **MCP (Model Context Protocol)**, dış bir server'ın (sunucu) — bir veritabanı bağlayıcısı, bir tarayıcı, üçüncü-parti bir API — tool'larını *ilan etmesinin* standart yoludur. Harness hamlesi küçük ama güçlü: bir MCP server'ın listelediği tool'ları al ve loop'unun zaten dispatch ettiği (Ders 02) **aynı havuza register et**. Mount'tan (bağlama) sonra bir MCP tool'u, yerli (native) bir tool'dan ayırt edilemez — loop onun uzak olduğunu hiç öğrenmez.

```python
mount_mcp_server(registry, weather_server, prefix="mcp_")
registry.dispatch("mcp_get_weather", {"city": "Paris"})   # server'a iletir
```

## Neden tek havuz ve neden prefix

- **Tek havuz**, loop'un, permission'ların (Ders 12) ve hook'ların (Ders 14) her tool'u tekdüze ele alması demektir — "MCP tool'u" diye özel durum yok. Karmaşıklık olmadan genişletilebilirlik.
- **Prefix (önek)**, isimleri namespace'ler; ikisi de `search` sunan iki server çakışmasın diye.

Burada klasik bir tuzak var: bir loop içinde handler oluştururken tool adını **her iterasyonda bind etmelisin** (factory fonksiyon ya da default argüman), yoksa her handler *son* tool'u çağırır. Eval tam bu bug'ı kontrol eder.

## Ne kuracaksın

`ToolRegistry` verilmiş. [`stub.py`](./stub.py) içinde `mount_mcp_server(registry, server, prefix)`'i uygula:

1. `server.list_tools()`'taki her `spec` için `original = spec["name"]` al.
2. `server.call_tool(original, kwargs)`'a ileten bir handler yap — `original`'ı **iterasyon başına bind et**.
3. `registry.register(prefix+original, description, input_schema, handler)`.

## Çalıştır

```sh
python 11_mcp/eval.py                       # RED
python 11_mcp/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 11_mcp/eval.py
```

→ Sonraki: **Ders 12 — Permissions & Trust** (*özgürlük güvenli olmak için sınır ister*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
