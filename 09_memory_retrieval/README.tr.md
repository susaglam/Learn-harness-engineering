# Ders 09 — Memory & Retrieval

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Önemliyi hatırla, gerektiğinde geri çağır.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Context her oturumda silinir (Ders 07 onu koşum ortasında sıkıştırır bile). **Memory** (hafıza), hayatta kalan şeydir: diske kalıcılaştırdığın gerçekler. Ama faydalı bir hafıza "her seferinde her şeyi yükle" değildir — bu, korumak için uğraştığın context'i yeniden doldurur. İşin püf noktası **retrieval** (geri çağırma): çok sayıda gerçek sakla, her adımda yalnızca *mevcut sorguyla ilgili* birkaçını geri getir.

Bunu zekice hissettiren şey, **anlamca** (semantic) ilgililiktir — kelime eşleşmesi değil. Bunu küçük bir bag-of-words **embedding** (gömme vektörü) ve **cosine similarity** (kosinüs benzerliği) ile yaklaşıklarız ki ders çevrimdışı ve deterministik olsun — production gerçek model embedding'lerini koyar ama mekanizma aynıdır.

```python
mem.add("The Eiffel Tower is in Paris.")
mem.recall("Where is the Eiffel Tower?", k=1)   # -> ["The Eiffel Tower is in Paris."]
```

## Neden retrieval, "hepsini yükle" değil

Gerçek bir ajan binlerce gerçek biriktirir. Hepsini enjekte etmek hem bütçeyi patlatır *hem de* sinyali boğar. Retrieval, hafızayı sınırsız tutarken her prompt'u küçük tutar — context'i yalnızca şu an ilgili olana harcarsın. RAG'ın arkasındaki motor budur.

## Ne kuracaksın

`embed()`, `cosine()`, `add()` verilmiş. [`stub.py`](./stub.py) içinde `MemoryStore.recall(query, k)`'i uygula:

1. Sorguyu embed et.
2. Saklanan öğeleri `cosine(sorgu_vektörü, öğe_vektörü)`'ne göre azalan sırala.
3. İlk `k` tanesinin metinlerini döndür.

## Çalıştır

```sh
python 09_memory_retrieval/eval.py                       # RED
python 09_memory_retrieval/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 09_memory_retrieval/eval.py
```

→ Sonraki: **Ders 10 — Skill Loading** (*bilgiyi talep üzerine yükle*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
