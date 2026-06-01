# Örnek Skill'ler

[English](./README.md) | [Türkçe](./README.tr.md)

> ℹ️ Teknik terimler İngilizce; açıklamalar için → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

Bir **skill** (yetenek paketi), talep üzerine yüklenen bir bilgi paketidir: ilk
başlıksız satırı tek-satırlık açıklama olan (ucuz *manifest* girdisi) ve gövdesi tam
prosedür olan (yalnızca gerektiğinde yüklenen) bir `SKILL.md`. **Lesson 10 (Skill
Loading)**, `SkillManager`'ına tam bu formatı okumayı öğretir.

Bu üç örnek skill müfredata eşlenir:

| Skill | Ne öğretir | Bağlı ders |
|---|---|---|
| `task-planning/` | eylemden önce planla (TodoWrite) | Lesson 05 |
| `subagent-delegation/` | gürültülü işi devret, sonucu tut | Lesson 08, 19 |
| `mcp-connection/` | bir MCP server'ın tool'larını ödünç al | Lesson 11 |

## Çalışırken gör

```sh
python skills/demo.py
```

`demo.py`, **Lesson 10 referans `SkillManager`**'ını yükler ve *bu* dizine karşı
çalıştırır — ucuz `manifest()`'i (isimler + açıklamalar) ve bir skill'in tam
`load()`'unu yazdırır. Bu, gerçek içerik üzerinde progressive-disclosure
(kademeli açma) ilkesidir: index hep mevcuttur; gövde talep üzerine gelir.

## Genişlet

Kendi skill'ini ekle: `skills/<name>/SKILL.md` oluştur — bir `# Başlık`, sonraki
satırda tek-satırlık açıklama ve prosedürel bir gövde. `manifest()`'te otomatik
görünür — kod değişikliği gerekmez. Lesson 16+'ya geldiğinde bu dizini doğal
olarak büyüteceksin.
