# Metodoloji — Eval-driven, kopya-driven değil

[English](./methodology.md) | [Türkçe](./methodology.tr.md)

> ℹ️ Teknik terimler İngilizce; açıklamalar için → **[Terminoloji Sözlüğü](./terminoloji.tr.md)**.

## Bitmiş kodu okumanın sorunu

Öncül kurs sana ders başına tam bir `code.py` veriyordu. Okudun, başını salladın, geçtin — ve neredeyse hiçbir şey aklında kalmadı, çünkü "okuyarak anlamak" bir yanılsamadır. Bir mekanizmayı ancak onu *çalıştırmaya* zorlandığında öğrenirsin.

Bu yüzden buradaki her ders, **yeşile çevireceğin bir kırmızı testtir**.

## Her dersin döngüsü

```
1. OKU       README.en.md / README.tr.md   — mekanizma ve NEDEN önemli olduğu
2. ÇALIŞTIR  python NN_ders/eval.py          — RED: eval başarısız; harness eksik
3. UYGULA    NN_ders/stub.py                 — önemli olan 5–10 satırı yaz (TODO)
4. ÇALIŞTIR  python NN_ders/eval.py          — GREEN: mekanizmanın çalıştığını kanıtladın
5. KARŞILAŞTIR NN_ders/reference.py          — kendi tasarımını bizimkiyle kıyasla
```

Eval'in GREEN ise, mekanizmayı sadece okumadın — kanıtlanabilir biçimde çalışan bir tane kurdun.

## Bir dersin dosya anatomisi

```
NN_ders/
  README.en.md     # anlatı: fikir, neden, tasarım kararları
  README.tr.md     # Türkçe anlatı (terimler gloss'lanır; aşağıdaki konvansiyona bak)
  reference.py     # tam, doğru implementasyon
  stub.py          # aynısı; ama kritik kısım TODO ile değiştirilmiş — SEN doldurursun
  eval.py          # SENİN stub'ını import edip kontrol eder; doğru olana dek RED
```

## Çoğu eval neden sahte model kullanır (ve API key gerektirmez)

Bir harness hatası ile bir model hatası dışarıdan aynı görünür; bu da ajanları çıldırtıcı derecede zor debug edilir yapar. Bu yüzden eval'lerimiz **mühendisliği izole eder**: harness'ini, önceden belirlenmiş yanıtlar döndüren *senaryolu bir sahte model* ile sürer. Bu üç şey kazandırır:

- **Deterministik** — her koşuda aynı sonuç; kararsızlık (flakiness) yok.
- **Ücretsiz & çevrimdışı** — API key yok, token maliyeti yok, CI'da çalışır.
- **Dürüst** — GREEN eval, *senin döngün/mantığın* doğru demektir; "model tesadüfen işbirliği yaptı" demek değil.

Buradaki her eval senaryolu bir sahte modele karşı çevrimdışı çalışır — retrieval (Ders 09) bile deterministik bir bag-of-words embedding kullanır, böylece kontrol tekrarlanabilir. Gerçek bir dağıtım canlı model çağrılarını yerine koyar; eval mekanizması aynıdır.

```python
# sahte-model eval'inin biçimi (Ders 01)
client = FakeClient(script=[
    tool_use("bash", {"command": "echo hi"}),   # 1. çağrı: model bir tool ister
    text("done"),                                # 2. çağrı: model bitirir
])
final = senin_agent_loop(client, ..., handlers={"bash": kaydeden_handler})
check("tool sonucu geri beslendi mi", client.saw_tool_result)   # SENİN döngünü test eder
```

## Terminoloji konvansiyonu (Türkçe track)

Öğretici içerik yeni başlayanları kucaklamalı. Bu yüzden Türkçe dokümanlarda:

1. **Teknik terimleri İngilizce tutarız** (kodda ve sektörde onlarla bu şekilde karşılaşacaksın).
2. **Her terimi ilk geçişte parantezle açıklarız**: *harness (koşum takımı — modelin çalışma ortamı)*.
3. Tek doğruluk kaynağı olarak yeni-başlayan-dostu bir **[sözlük](./terminoloji.tr.md)** tutarız.

Bu, bilişsel yükü en aza indirir ve gerçek koda transferi en üst düzeye çıkarır. İngilizce dokümanlar, okurun teknik terimleri zaten İngilizce okuduğunu varsayar; yeni başlayanlar için kısa bir [İngilizce sözlük](./glossary.md) Türkçesini aynalar.

## Yazarlar için ölçek kuralı

İskelet bir dersi kurarken, eval'i **küçük ve cerrahi** tut: dersin eklediği *tek* mekanizmayı test etmeli, bütün dünyayı değil. Tek mekanizma, tek motto, tek kırmızı test, tek düzeltme.

← Geri: [README.tr.md](../README.tr.md) · ayrıca bkz.: [felsefe](./philosophy.tr.md)
