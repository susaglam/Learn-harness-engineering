# Ders 01 — The Agent Loop

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Tek döngü, ve modeli sürer.*
>
> ℹ️ Teknik terimler İngilizce; açıklamalar için → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Bir **agent** (ajan) zekice bir prompt değildir. Bir **loop**'tur (döngü):

```
modele sor  →  bir tool (araç) mı istedi?
                  ├─ hayır → işi bitti, cevabını döndür
                  └─ evet  → tool'u çalıştır, sonucu geri besle, tekrar sor
```

Hepsi bu. Model *ne* yapacağına ve *ne zaman duracağına* karar verir; senin kodun yalnızca istediğini çalıştırıp geri bildirir. Bu kurstaki diğer her şey — planlama, hafıza, takımlar, güvenlik — bu döngünün *üzerine* eklenir. **Döngünün kendisi asla değişmez.** Şimdi içselleştir, kalan 22 ders sadece ekleme olur.

## Sonucu geri beslemek neden bütün marifet

Model bir `bash` komutu çalıştıramaz — eli yoktur. İstediğinde bir `tool_use` bloğu üretir (`stop_reason == "tool_use"`), yani *"lütfen bu girdiyle bash'i çalıştır"* der. Senin harness'in onu çalıştırır ve konuşmaya bir `tool_result` ekler. Bir sonraki turda model **sonucu görür** ve akıl yürütmeye devam eder.

Bu adımı atlarsan model kördür: bir şey istedi ama ne olduğunu hiç öğrenemedi. Ajan takılır. Yani önemli olan tek satır — bir chatbot'u ajana çeviren satır — *tool sonucunu `messages`'a geri beslemektir*.

## Ne kuracaksın

[`stub.py`](./stub.py) içinde, `agent_loop` fonksiyonundaki tool-sonucu adımını uygula:

1. Modelin yanıtındaki her `tool_use` bloğu için `handlers[block.name](**block.input)` çağır.
2. Her çıktıyı şu şekilde sar: `{"type": "tool_result", "tool_use_id": block.id, "content": str(output)}`.
3. Hepsini **tek** bir user mesajı olarak ekle: `messages.append({"role": "user", "content": results})`.

## Çalıştır

```sh
python 01_agent_loop/eval.py        # RED — TODO henüz yapılmadı
#   ...stub.py içindeki TODO'yu uygula...
python 01_agent_loop/eval.py        # GREEN — çalışan bir loop kurdun

python 01_agent_loop/reference.py   # (opsiyonel) gerçeğini çalıştır — .env içinde API key gerekir
```

Eval **senaryolu bir sahte model** kullanır — API key yok, maliyet yok. Loop'unun handler'ı çağırdığını, doğru-bağlanmış bir `tool_result` geri beslediğini ve modelin son cevabıyla durduğunu kontrol eder. Buradaki GREEN, *mühendisliğinin* doğru olduğu anlamına gelir — herhangi bir modelin keyfinden bağımsız.

## Karşılaştır

GREEN olunca `stub.py`'ını [`reference.py`](./reference.py) ile karşılaştır. Asıl kodun ne kadar küçük olduğuna — ve loop gövdesinin sonraki tüm derslerin üzerine inşa ettiği şeyle birebir aynı olduğuna dikkat et.

→ Sonraki: **Ders 02 — Tool Use** (*yeni tool = yeni handler*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
