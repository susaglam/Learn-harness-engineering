# Müfredat — 6 Ark, 23 Ders

[English](./CURRICULUM.md) | [Türkçe](./CURRICULUM.tr.md)

> ℹ️ Teknik terimler İngilizce; yeni-başlayan-dostu açıklamalar için → **[Terminoloji Sözlüğü](./docs/terminoloji.tr.md)**.

Her ders, değişmeyen agent loop'un üzerine **bir** harness mekanizması ekler ve eval-driven bir alıştırma olarak gelir (`README` → `eval.py` RED → `stub.py` → GREEN → `reference.py` ile karşılaştır). Bkz. [metodoloji](./docs/methodology.tr.md).

**Durum:** ✅ hazır ve eval-doğrulandı (stub RED → reference GREEN, çevrimdışı, API key gerekmez)

---

## Ark 1 — Çekirdek *(indirgenemez ajan)*

| # | Ders | Motto | Ne kuracaksın | Durum |
|---|---|---|---|---|
| 01 | Agent Loop | *Tek döngü, ve modeli sürer* | Döngü: tool sonuçlarını geri besle ki model devam edebilsin | ✅ |
| 02 | Tool Use | *Yeni tool = yeni handler* | Dispatch haritası; döngüye dokunmadan tool ekle | ✅ |
| 03 | System Prompt | *Ajan konuşmadan önce yapılandırılır* | System prompt'u parçalardan runtime'da montajla | ✅ |
| 04 | Eval & Observability | *Ölçemiyorsan umuyorsun demektir* | Trajectory (yörünge) izleyici + ajan koşumlarını notlayan scorer'lar | ✅ |

## Ark 2 — Gerçek İş *(niyeti çıktıya çevir)*

| # | Ders | Motto | Ne kuracaksın | Durum |
|---|---|---|---|---|
| 05 | Planning | *Plan, niyeti kontrol edilebilir adıma çevirir* | Ajanın plan yapıp sonra uyguladığı bir TodoWrite tool'u | ✅ |
| 06 | Structured I/O | *Modelin okuyacağı çıktıyı tasarla* | Şema-doğrulamalı tool sonuçları + uyumsuzlukta yeniden dene | ✅ |
| 07 | Context & Token Ekonomisi | *Context bir bütçedir; bilinçli harca* | Compaction (sıkıştırma) stratejileri + token bütçe göstergesi | ✅ |
| 08 | Subagents | *Gürültüyü devret, sinyali tut* | Temiz bağlamlı alt-ajan başlat; yalnızca sonucu döndür | ✅ |

## Ark 3 — Bilgi & Hafıza *(bil ve geri çağır)*

| # | Ders | Motto | Ne kuracaksın | Durum |
|---|---|---|---|---|
| 09 | Memory & Retrieval | *Önemliyi hatırla, gerektiğinde geri çağır* | Gerçekleri diske yaz + semantik geri çağırma (embedding) | ✅ |
| 10 | Skill Loading | *Bilgiyi talep üzerine yükle* | Skill manifest'i; skill gövdesini yalnızca gerektiğinde enjekte et | ✅ |
| 11 | MCP | *Yeteneği ödünç al, tek havuzda tut* | Dış bir MCP sunucusunun tool'larını döngüye yönlendir | ✅ |

## Ark 4 — Sertleştirme *(güvenli ve dayanıklı yap)*

| # | Ders | Motto | Ne kuracaksın | Durum |
|---|---|---|---|---|
| 12 | Permissions & Trust | *Özgürlük güvenli olmak için sınır ister* | İzin hattı: allow / ask / deny | ✅ |
| 13 | Security & Injection | *Dışarıdan gelen her token potansiyel düşman* | Güvenilmeyen içeriği karantinaya al; injection tespiti | ✅ |
| 14 | Hooks | *Döngünün etrafını genişlet, döngüyü yazma* | PreToolUse / PostToolUse genişletme noktaları | ✅ |
| 15 | Error Recovery | *Hata bir dal, çıkmaz sokak değil* | Hata taksonomisi + retry / fallback stratejileri | ✅ |

## Ark 5 — Ölçek *(uzun-soluklu, çok ajan)*

| # | Ders | Motto | Ne kuracaksın | Durum |
|---|---|---|---|---|
| 16 | Task Graphs | *Büyük hedef diske sıralı task olur* | `blockedBy` bağımlılıklı, diske yazılı task grafiği | ✅ |
| 17 | Background & Async | *Yavaş iş arka plana, ajan düşünmeye devam* | İş-parçacıklı çalıştırma + tamamlanma bildirim kuyruğu | ✅ |
| 18 | Cron / Self-Scheduling | *Ajan kendini uyandırabilir* | Zamanla tetiklenen kalıcı zamanlanmış görevler | ✅ |
| 19 | Agent Teams & Protocols | *Tek ajana büyük gelen iş → koordinasyon* | Kalıcı takım arkadaşları + async mailbox + istek/yanıt protokolü | ✅ |
| 20 | Worktree Isolation | *Her ajana kendi odası* | Task'ları git worktree'lere bağla; paralel ajanlar çakışmasın | ✅ |
| 21 | Autonomous Agents | *İşini kendi çeken ajanlar* | Ajanların panodan işi kendi aldığı bir idle (boşta) döngüsü | ✅ |

## Ark 6 — Sentez *(dürüstçe birleştir)*

| # | Ders | Motto | Ne kuracaksın | Durum |
|---|---|---|---|---|
| 22 | Orchestration Spectrum | *Güvenilir olması gerekeni sabitle, akıllı olması gerekeni devret* | Aynı görevi determinizm↔otonomi ekseninde 3 noktada çöz, notla | ✅ |
| 23 | Comprehensive Agent | *Çok mekanizma, tek ölçülebilir döngü* | Tüm mekanizmaları tek döngü etrafında birleştir, eval'lerle kanıtla | ✅ |

---

← Geri: [README.tr.md](./README.tr.md)
