# Terminoloji Sözlüğü

> Bu kurs teknik terimleri **İngilizce orijinaliyle** kullanır — çünkü kodda, kütüphane dokümanlarında ve iş hayatında karşına hep bu terimler çıkacak. Burada her terimi **yeni başlayan birinin anlayacağı** şekilde açıklıyoruz. Türkçe karşılığı parantez içinde verdik; ama günlük kullanımda İngilizcesini tercih et.
>
> Format: **terim** *(Türkçe karşılık)* — açıklama.

İçindekiler: [Çekirdek](#1-çekirdek-kavramlar) · [Metodoloji](#2-metodoloji-eval-driven) · [Bağlam & Token](#3-bağlam--token) · [Hafıza & Bilgi](#4-hafıza--bilgi) · [Güvenlik & Sertleştirme](#5-güvenlik--sertleştirme) · [Ölçek & Çok-Ajan](#6-ölçek--çok-ajan) · [Sağlayıcı & API](#7-sağlayıcı--api)

---

## 1. Çekirdek kavramlar

- **model / LLM** *(Large Language Model — büyük dil modeli)* — Devasa metin üzerinde eğitilmiş, bir sonraki kelimeyi tahmin ederek metin üreten yapay sinir ağı. Claude, GPT, GLM birer modeldir. Bu kursta "zekânın" geldiği yer burasıdır.
- **agent** *(ajan)* — Bir amaca ulaşmak için **algılayan, akıl yürüten ve eyleyen** bir sistem. Pratikte: model + harness.
- **agency** *(eylemlilik)* — Algılama, karar verme ve eyleme geçme kapasitesi. Tezimiz: agency *eğitilir* (modelde gizlidir), harness onu *gerçekleştirir*.
- **harness** *(koşum takımı / çalışma düzeneği)* — Modelin etrafına kurduğun her şey: araçlar (tool), bilgi, bağlam yönetimi, hafıza, izinler. "Modelin duyu-motor sistemi ve çalışma belleği." Bu kursun konusu budur.
- **agent loop** *(ajan döngüsü)* — Tüm sistemin kalbi olan döngü: modele sor → model tool isterse çalıştır → sonucu geri ver → tekrar sor → model durunca bitir. Sonraki tüm dersler bu döngünün *etrafına* eklenir; döngünün kendisi hiç değişmez.
- **prompt** *(istem / yönerge)* — Modele verdiğin metin girdisi. "Modele ne söylediğin."
- **system prompt** *(sistem yönergesi)* — Konuşmanın en başında modele verilen, kim olduğunu ve nasıl davranacağını belirleyen kalıcı talimat. Ajan "konuşmadan önce" onu yapılandırır.
- **message** *(mesaj)* — Konuşmadaki tek bir sıra. `role` (rol: `user`/`assistant`) ve `content` (içerik) taşır. Tüm konuşma bir mesaj listesidir (`messages[]`).
- **tool** *(araç)* — Modelin dünyada eylem yapmasını sağlayan bir fonksiyon: dosya okuma, shell komutu, API çağrısı vb. Modele "el" verir.
- **tool use** *(araç kullanımı)* — Modelin "şu aracı şu girdiyle çalıştır" demesi. Modelin kendisi aracı çalıştırmaz; *çağırmak istediğini söyler*, harness çalıştırır.
- **handler** *(işleyici)* — Bir tool'un asıl işini yapan kod parçası. `handlers["bash"]` → bash komutunu çalıştıran fonksiyon.
- **dispatch** *(yönlendirme)* — Modelin istediği tool adını doğru handler'a eşleştirme adımı. "Tool eklemek = bir handler eklemek" — döngü değişmez.
- **stop_reason** *(durma nedeni)* — Modelin yanıtındaki "neden durdum" bilgisi. `"tool_use"` ise tool çağırmak istiyor (döngü devam eder); değilse işi bitmiştir (döngü döner).
- **tool_use / tool_result** — Modelin yanıtındaki "şu aracı çağır" bloğu (`tool_use`) ve senin geri beslediğin sonuç bloğu (`tool_result`). İkisi `tool_use_id` ile eşleşir.

## 2. Metodoloji (eval-driven)

- **eval** *(değerlendirme / test)* — Harness'inin gerçekten çalışıp çalışmadığını ölçen otomatik kontrol. Bu kursun en önemli fikri: "ölçemiyorsan mühendislik yapmıyorsun, umut ediyorsun."
- **RED / GREEN** *(kırmızı / yeşil)* — Test terminolojisi. **RED**: test başarısız (mekanizma henüz eksik). **GREEN**: test geçti (mekanizmayı doğru kurdun). Her ders RED başlar, sen GREEN'e çevirirsin.
- **stub** *(taslak / iskelet)* — İçinde senin doldurman gereken bir `TODO` boşluğu olan, kasıtlı eksik dosya. Asıl öğrenme burada olur.
- **reference** *(referans implementasyon)* — Tam, çalışan çözüm. Eval'i GREEN yaptıktan *sonra* kendi çözümünle karşılaştırmak için.
- **fake model / mock** *(sahte model)* — Eval'lerin API key olmadan çalışması için, gerçek modelin yerine senaryolu yanıtlar döndüren sahte nesne. Böylece *modeli* değil *senin mühendisliğini* test ederiz.
- **TODO** — Kodda "burayı sen doldur" işareti.

## 3. Bağlam & Token

- **token** — Modelin metni işlediği en küçük parça (kabaca bir kelime parçası). Hem maliyetin hem de sınırların birimi. "Context bir bütçedir; token ile ölçülür."
- **context / context window** *(bağlam / bağlam penceresi)* — Modelin aynı anda "görebildiği" toplam metin (sistem prompt + tüm mesajlar + tool sonuçları). Sınırlıdır; dolarsa yer açman gerekir.
- **compaction** *(sıkıştırma)* — Bağlam dolmaya yaklaşınca eski/gereksiz kısımları özetleyip yer açma stratejisi. "Sonsuz oturum" bununla mümkün olur.
- **token economics** *(token ekonomisi)* — Maliyet/hız/kalite dengesini token bütçesiyle yönetme: caching (önbellek), ucuz/pahalı model seçimi vb.
- **latency** *(gecikme)* — Bir isteğin yanıt gelene kadar geçen süresi.

## 4. Hafıza & Bilgi

- **memory** *(hafıza)* — Bir oturumun ötesinde kalıcı kalan bilgi: kullanıcı tercihleri, proje gerçekleri, ders çıkarımları. Diske yazılır.
- **retrieval** *(geri çağırma)* — Kalıcı hafızadan *ilgili* parçayı, ihtiyaç anında bulup getirme.
- **RAG** *(Retrieval-Augmented Generation)* — Modele cevap verdirmeden önce ilgili dokümanları arayıp bağlama ekleme tekniği.
- **embedding** *(gömme vektörü)* — Bir metni, anlamını temsil eden sayı dizisine (vektör) çevirme. "Anlamca benzer" şeyleri bulmayı (semantik arama) sağlar.
- **skill** *(yetenek paketi)* — İhtiyaç anında yüklenen, talimat + kaynak içeren bilgi paketi. "Bilgiyi önden değil, talep üzerine yükle."
- **MCP** *(Model Context Protocol)* — Dış araç ve servisleri (veritabanı, tarayıcı, üçüncü-parti API'ler) standart bir protokolle ajanın tool havuzuna bağlama yöntemi. "Yeteneği ödünç al, tek havuzda tut."

## 5. Güvenlik & Sertleştirme

- **permission** *(izin)* — Bir tool'un çalışıp çalışamayacağını, onay gerekip gerekmediğini belirleyen kural. "Özgürlük güvenli olmak için sınır ister."
- **trust boundary** *(güven sınırı)* — Güvenilen (senin kodun) ile güvenilmeyen (dışarıdan gelen veri) arasındaki çizgi.
- **prompt injection** *(prompt enjeksiyonu)* — Dışarıdan gelen bir metnin (web sayfası, dosya, e-posta) içine gizlenmiş, modeli kandırıp istenmeyen eylem yaptırmaya çalışan saldırı. "Dışarıdan gelen her token potansiyel düşmandır."
- **hook** *(kanca)* — Döngüyü değiştirmeden, belirli olaylarda (tool öncesi/sonrası, oturum başı/sonu) çalışan ek kod. "Döngünün etrafını genişlet, döngüyü yazma."
- **error recovery** *(hata kurtarma)* — Bir tool veya model hatasında çökmek yerine yeniden deneme, yer açma ya da başka yol bulma stratejisi. "Hata bir dal, çıkmaz sokak değil."
- **observability** *(gözlemlenebilirlik)* — Ajanın içinde ne olduğunu görebilme: loglama, izleme (tracing), metrikler. Ölçmenin önkoşulu.

## 6. Ölçek & Çok-Ajan

- **subagent** *(alt-ajan)* — Bir yan görevi temiz/ayrı bir bağlamda yapıp sadece sonucu geri getiren ikincil ajan. "Gürültüyü devret, sinyali tut."
- **task graph** *(görev grafiği)* — Büyük hedefin, diske kaydedilmiş, birbirine bağımlı (`blockedBy`) küçük görevlere bölünmüş hâli.
- **DAG** *(Directed Acyclic Graph — yönlü çevrimsiz grafik)* — Görevlerin bağımlılık ilişkisini temsil eden, döngü içermeyen yapı.
- **background / async** *(arka plan / eşzamansız)* — Yavaş işleri (uzun komut, derleme) ayrı bir iş parçacığında çalıştırıp ajanı bloke etmeden devam ettirme.
- **cron** — Görevleri belirli zamanlarda otomatik tetikleyen zamanlayıcı. "Ajan kendini uyandırabilir."
- **agent team** *(ajan takımı)* — Kalıcı birden fazla ajanın, mesaj kutuları (mailbox) üzerinden haberleşerek birlikte çalışması.
- **mailbox** *(posta kutusu)* — Ajanların birbirine eşzamansız mesaj bıraktığı kuyruk.
- **protocol** *(protokol)* — Ajanların anlaşması için sabit mesaj formatı (örn. istek-yanıt, kapanış el sıkışması).
- **worktree** *(git worktree — çalışma ağacı)* — Aynı git deposunun ayrı bir dizindeki ikinci kopyası. Paralel ajanların birbirine çakışmadan çalışmasını sağlar. "Her ajana kendi odası."
- **autonomous agent** *(otonom ajan)* — Kendisine tek tek iş atanmadan, bir panodan işi kendi alan, kendini örgütleyen ajan.
- **orchestration** *(orkestrasyon)* — Birden çok adımı/ajanı koordine etme. **deterministic** (scriptli, sabit) ↔ **autonomous** (model-güdümlü) spektrumunda bir yer seçmek.
- **trajectory** *(yörünge)* — Ajanın bir görevde izlediği eylem dizisi (algı → akıl → eylem). Gelecek modelleri eğitmek için ham veridir.

## 7. Sağlayıcı & API

- **API** *(Application Programming Interface)* — İki yazılımın konuşma arayüzü. Modele istek göndermek için kullandığın uzak servis.
- **API key** *(API anahtarı)* — Sağlayıcıya kimliğini kanıtlayan gizli anahtar. `.env` dosyasında tutulur, asla git'e gönderilmez.
- **provider** *(sağlayıcı)* — Modeli sunan firma/servis (Anthropic, Zhipu/GLM, Moonshot/Kimi, DeepSeek, MiniMax...).
- **base URL** *(temel adres)* — İsteklerin gönderildiği sunucu adresi. Değiştirerek Anthropic-uyumlu başka bir sağlayıcıya yönlenirsin.
- **Anthropic-compatible** *(Anthropic-uyumlu)* — Anthropic'in API formatını taklit eden sağlayıcılar; sadece `base URL` ve `model id` değiştirerek aynı kodu onlarla da kullanabilirsin.

---

← Geri: [README.tr.md](../README.tr.md) · [Müfredat](../CURRICULUM.tr.md)
