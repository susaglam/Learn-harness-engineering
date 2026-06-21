# Harness Mühendisliğini Öğren

> **Bir modeli gerçek bir ajana dönüştüren ortamı kur — ve onu ölç.**

[English](./README.md) | [Türkçe](./README.tr.md)

> ℹ️ **Terminoloji notu (yeni başlayanlar için):** Teknik terimleri İngilizce orijinaliyle kullanıyoruz — kod, dokümanlar ve sektör hep bu dili konuşur; terimi "çevirip" seni yabancılaştırmak yerine tanıdık tutuyoruz. Her terimi ilk geçtiğinde parantez içinde kısaca açıklıyoruz. Tüm terimlerin yeni-başlayan-dostu tam açıklaması için → **[Terminoloji Sözlüğü](./docs/terminoloji.tr.md)**.

---

## Tez

**Yetenek modelde gizlidir. Harness, onun ne kadarının dünyaya ulaşacağını belirler.**

> *Terimler:* **harness** (koşum takımı): modelin çalışma ortamı — araçlar, bağlam, hafıza ve sınırların tümü. **agency** (eylemlilik): algılama, akıl yürütme ve eyleme geçme kapasitesi. **model**: metni üreten yapay sinir ağı (LLM).

Agency *eğitilir* — ama *gerçekleşen* agency *mühendislik ürünüdür*. Kötü bir harness'in ardındaki dahi bir model, karanlık bir odaya kilitlenmiş dahidir: akıl yürütebilir ama algılayamaz, eyleyemez, hatırlayamaz, toparlanamaz. Harness, modelin sürdüğü pasif bir "araç" değildir. O, modelin **duyu-motor sistemi ve çalışma belleğidir** — ve modelin gizli yeteneğinin ne kadarının faydalı davranışa dönüşeceğinin tavanını koyar.

Bu repo, o harness'i tek tek mekanizmalarla kurmayı ve — en kritik kısım — her mekanizmanın gerçekten işe yarayıp yaramadığını **ölçmeyi** öğretir.

### Bu çerçeve neden önemli

Eski slogan "agency modelden gelir, harness'ten değil" yarı-doğru ve kendini baltalayan bir ifadedir: harness önemli olmasaydı öğretilecek hiçbir şey olmazdı. Dürüst versiyon, **ölçülebilir bir sınırı olan ortaklıktır**:

- Model **zekâyı** sağlar (algı, akıl yürütme, yargı).
- Harness **eylem uzayını, bağlamı, hafızayı ve koruma bantlarını** sağlar.
- İkisinin çarpımı — tek başına hiçbiri değil — sevkettiğin ajandır.

Ve eski çerçevenin görmezden geldiği bir geri besleme döngüsü var: 2025–2026'da ajanlar giderek *ajansal yörüngeler üzerinde* pekiştirmeli öğrenmeyle eğitiliyor. Bugün kurduğun harness, yarının modelini eğiten veriyi şekillendiriyor. **Harness tasarımı, model tasarımının parçası hâline geliyor.**

---

## Orkestrasyon spektrumu (ikili değil)

Yaygın bir dogma der ki: "gerçek ajanlar her şeye modelin karar vermesini bırakır; sabit-kodlu workflow'lar sahte ajandır." Bu fazla mutlaktır — ve bu müfredatın kendi sonraki dersleri (task grafikleri, takım protokolleri, cron) *zaten* yapılandırılmış orkestrasyondur.

Gerçek bir spektrumdur:

```
 deterministik <───────────────────────────────────────────> otonom
 (scriptli)                                                   (model-güdümlü)

 şunlara ihtiyacın varsa sabitle:        şunlara ihtiyacın varsa modele bırak:
   güvenilirlik, düşük maliyet,            açık-uçlu yargı, yeni yollar,
   denetlenebilirlik, güvenlik             uyum, yaratıcılık
```

İyi harness mühendisliği, **her alt-problem için bu spektrumdaki doğru noktayı seçmektir** — taraf tutmak değil. Son ders bu seçimi iyi yapmaya ayrılmıştır.

---

## Çekirdek desen

Her ders bu döngünün üzerine bir mekanizma ekler. *Kavramsal* döngü asla değişmez — ama production runtime'ı etrafında bir execution policy (yürütme politikası) büyür: streaming, paralel tool call, cancellation, approval bekleme, resumability. Aşağıdaki, öğretim iskeleti.

```python
def agent_loop(client, model, messages, tools, handlers, system=""):
    while True:
        resp = client.messages.create(
            model=model, system=system, messages=messages, tools=tools,
            max_tokens=1024,          # API tarafından zorunlu
        )
        messages.append({"role": "assistant", "content": resp.content})

        if resp.stop_reason != "tool_use":
            return resp                      # model işini bitirdi

        results = []
        for block in resp.content:
            if block.type == "tool_use":
                output = handlers[block.name](**block.input)
                results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": str(output),
                })
        messages.append({"role": "user", "content": results})
```

Model ne zaman tool çağıracağına ve ne zaman duracağına karar verir. Harness sadece çalıştırır ve sonucu geri besler. **Döngü ajana aittir; etrafına kurduğun her şey harness'e.**

---

## Metodoloji: eval-driven, kopya-driven değil

Eski yol: bitmiş bir dosyayı oku, başını salla, geç. Kalıcı hiçbir şey öğrenmezsin.

**Bizim yolumuz — her ders, yeşile çevireceğin bir kırmızı testtir:**

```
1. Oku    README.en.md / README.tr.md   → mekanizmayı ve neden önemli olduğunu anla
2. Çalıştır python <ders>/eval.py        → RED (eval başarısız; harness eksik)
3. Düzenle <ders>/stub.py                → önemli olan 5–10 satırı yaz (TODO)
4. Çalıştır python <ders>/eval.py        → GREEN (mekanizmanın çalıştığını kanıtladın)
5. Karşılaştır reference.py ile           → kendi tasarımını bizimkiyle kıyasla
```

Evallerin tamamı **API key olmadan** çalışır — her biri harness mantığını senaryolu bir sahte modelle sürer; böylece *modeli* değil, *mühendisliği* test edersin. Bu, alanın en az öğrettiği ama en önemli harness becerisidir: **ölçemiyorsan mühendislik yapmıyorsun — umut ediyorsun.**

---

## Müfredat — 6 ark, 23 ders

Mottolarla tam liste: **[CURRICULUM.tr.md](./CURRICULUM.tr.md)**.

| Ark | Tema | Dersler |
|---|---|---|
| **1. Çekirdek** | indirgenemez ajan | Loop · Tool Use · System Prompt · **Eval & Observability** |
| **2. Gerçek İş** | niyeti çıktıya çevir | Planlama · Structured I/O · Context & Token Ekonomisi · Subagent |
| **3. Bilgi & Hafıza** | bil ve geri çağır | Memory & Retrieval · Skill Loading · MCP |
| **4. Sertleştirme** | güvenli ve dayanıklı yap | Permissions · **Security & Injection** · Hooks · Error Recovery |
| **5. Ölçek** | uzun-soluklu, çok ajan | Task Graphs · Background · Cron · Teams · Worktrees · Autonomous |
| **6. Sentez** | dürüstçe birleştir | **Orchestration Spectrum** · Comprehensive Agent |

**Kalın** = öncül kursta eksik olan konular. En önemli iki hamle: **System Prompt** ve **Eval** *başta* (her şeyi çerçeveler); **Permissions, Security, Hooks** *sonra*, bir "sertleştirme" arkı olarak — zaten faydalı iş yapan bir ajanı sertleştirirsin, ondan önce değil.

---

## Hızlı başlangıç

```sh
git clone <fork-url-niz> learn-harness-engineering
cd learn-harness-engineering
python -m venv .venv
. .venv/bin/activate              # macOS/Linux  ·  Windows (PowerShell): .venv\Scripts\Activate.ps1
pip install -r requirements.txt
cp .env.example .env              # API key ekle  ·  Windows: copy .env.example .env

# Ders 1: eval'ler API key GEREKTİRMEZ — senaryolu sahte model kullanır.
python 01_agent_loop/eval.py        # RED
#   ...01_agent_loop/stub.py içindeki TODO'yu uygula...
python 01_agent_loop/eval.py        # GREEN

# TÜM derslerin eval'ini tek seferde çalıştır (CI tam olarak bunu koşar):
python run_all_evals.py

# Opsiyonel: tüm derslerin çevrimdışı, gezilebilir önizlemesini üret (EN/TR):
python scripts/build_web.py         # sonra web/index.html'i aç

# Bir dersi gerçek modele karşı çalıştırmak için:
python 01_agent_loop/reference.py
```

---

## Proje yapısı

```
learn-harness-engineering/
  README.md / README.tr.md        # bu dosya (EN / TR)
  CURRICULUM.md / .tr.md          # tam 23-ders haritası
  docs/
    philosophy.md / .tr.md        # tez & orkestrasyon spektrumu, derinlemesine
    methodology.md / .tr.md       # eval-driven öğretim yöntemi, derinlemesine
    glossary.md / terminoloji.tr.md  # yeni-başlayan sözlüğü (EN / TR)
  harness/                        # paylaşılan, sağlayıcı-bağımsız altyapı
    client.py                     #   .env'den Anthropic-uyumlu client kur
    loop.py                       #   referans kanonik loop (dersler pedagoji için kendi loop'unu tutar)
    evals.py                      #   küçük bir RED/GREEN eval runner
  01_agent_loop/                  # her ders: README.en/tr + reference + stub + eval
    README.en.md / README.tr.md
    reference.py                  #   tam implementasyon
    stub.py                       #   TODO'yu sen uygularsın
    eval.py                       #   stub'ın doğru olana dek başarısız
  02_tool_use/ ... 23_comprehensive/
  skills/                         # Lesson 10'un yükleyebileceği örnek SKILL.md paketleri (+ demo.py)
  scripts/                        # scaffold_lessons.py, build_web.py
  web/                            # üretilen tek-dosya önizleme (web/index.html, git-ignored)
  run_all_evals.py                # her dersin eval'ini çalıştır (RED stub -> GREEN reference)
  .github/workflows/test.yml      # CI: push / PR'da run_all_evals.py koşar
```

---

## Diller

Bu ilk sürüm yalnızca **İngilizce** ve **Türkçe** içerir. Müfredat oturduktan sonra diğer çeviriler gelebilir — öncül repoyu vuran iki-track sürüklenmesini önlemek için bilinçli olarak.

## Lisans

MIT.

---

**Zekâyı model getirir. Eyleyeceği dünyayı sen kurarsın — ve o dünyanın çalıştığını kanıtlarsın. Ölçülebilir bir ajan, ihtiyacın olan tek şeydir.**
