# Felsefe — Yetenek gizlidir; onu harness gerçekleştirir

[English](./philosophy.md) | [Türkçe](./philosophy.tr.md)

> ℹ️ Teknik terimler İngilizce; açıklamalar için → **[Terminoloji Sözlüğü](./terminoloji.tr.md)**.

## Tez, dikkatle ifade edilmiş hâliyle

> **Yetenek (capability) modelde gizlidir. Harness, onun ne kadarının dünyaya ulaşacağını belirler. Agency eğitilir; gerçekleşen agency mühendislik ürünüdür.**

Model (LLM), devasa metin üzerinde gradient descent ile şekillenmiş bir fonksiyondur. İçinde muazzam bir gizli yetenek yaşar: akıl yürütme, dünya bilgisi, kod akıcılığı, yargı. Ama gizli yetenek, davranış değildir. Tool'u olmayan model eyleyemez; hafızası olmayan kalıcı olamaz; context (bağlam) yönetimi olmayan boğulur; kurtarma (recovery) olmayan ilk hatada ölür.

**Harness**, gizli yeteneği gerçekleşen davranışa çeviren şeydir. Modelin duyu-motor sistemi (tool'lar), çalışma belleği (context), uzun-dönem hafızası (kalıcılık) ve vicdanıdır (permission/izinler). Harness'i değiştirirsin — *aynı* modelle farklı bir ajan elde edersin.

## Eski mutlakçılığı neden reddediyoruz

Popüler bir çerçeve der ki: *"agency modelden gelir, harness'ten değil; harness mühendisleri sadece aracı kurar."* Bu yarı-doğru ve retorik olarak kendini baltalar:

1. **Kendini baltalar.** Harness önemli olmasaydı öğretilecek hiçbir şey olmazdı — oysa çerçeve yirmi dokuz ders dolusu harness mekanizması sunar. Çelişki içine gömülüdür.
2. **Sınırda ampirik olarak yanlış.** *Aynı* model, iyi vs kötü tool / context / recovery ile çarpıcı biçimde farklı başarı oranı verir. Bu fark eğitim değil, mühendisliktir.
3. **En önemli beceriyi gizler.** Harness'i pasif bir araç sanırsan onu **ölçmeyi** asla öğrenmezsin. Oysa bütün oyun ölçmektir (bkz. [metodoloji](./methodology.tr.md)).

Dürüst versiyon, **ölçülebilir bir sınırı olan ortaklıktır**: model zekâyı sağlar; harness eylem uzayını, bağlamı, hafızayı ve koruma bantlarını sağlar; çarpımları ajandır. Tek başına hiçbiri sevkedilemez.

## Eski çerçevenin görmezden geldiği geri besleme döngüsü

2025–2026'da öncü ajanlar giderek **ajansal trajectory'ler (yörüngeler)** üzerinde — tool kullanan ortamlarda gerçek algı → akıl → eylem dizileri — pekiştirmeli öğrenme (RL) ile eğitiliyor. Bu şu demek:

> Bugün kurduğun harness, yarının modelini eğiten yörüngeleri üretir.

Dolayısıyla harness tasarımı, model tasarımının *parçası* hâline geliyor. "Zekâ" ile "ortam" arasındaki sınır artık net değil. Bunu anlayan bir harness mühendisi yalnızca bugünkü görev başarısı için değil, dağıtımının ürettiği eğitim sinyalinin kalitesi için de tasarım yapar.

## Orkestrasyon spektrumu ("gerçek ajan mı?" kavgasını çözmek)

Alandaki bir dogma, sabit-kodlu workflow'ları "sahte ajan", yalnızca tamamen model-güdümlü sistemleri "gerçek" sayar. Bu yanlış bir ikilemdir. Her ciddi sistem bir spektrumda bir yerdedir:

```
 deterministik <──────────────────────────────────────────────> otonom
 (scriptli kontrol akışı)                                        (model karar verir)

 şunlar için deterministik seç:         şunlar için otonom seç:
   güvenilirlik                           açık-uçlu yargı
   düşük/öngörülebilir maliyet            yeni çözüm yolları
   denetlenebilirlik & uyumluluk          sürprize uyum
   güvenlik-kritik adımlar                yaratıcılık
```

Beceri, **her alt-problem için yerleştirme** yapmaktır — kabile seçmek değil. Güvenilir olması gereken adımları sabitle; akıllı olması gerekenleri devret. İyi bir ajan genellikle *deterministik bir iskelet + otonom kaslardır* — yargının değer kattığı tam noktada model yargısını çağıran güvenilir bir dış döngü. Ders 22 bunu somutlaştırır: aynı görevi eksen üzerinde üç noktada çözüp ödünleşimleri notlar.

## Bu senin için ne anlama geliyor

Sen zekâ yazmıyorsun. Zekânın içinde yaşadığı dünyayı kuruyor — ve **ölçüyorsun**. O dünyayı iyi kur, çalıştığını kanıtla; gerisini model halleder.

← Geri: [README.tr.md](../README.tr.md) · sonraki: [metodoloji](./methodology.tr.md)
