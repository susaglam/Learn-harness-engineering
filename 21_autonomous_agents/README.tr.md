# Ders 21 — Autonomous Agents

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *İşini kendi çeken ajanlar.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Ders 19'da bir lider'in task'ları takım arkadaşlarına tek tek atadığını düşünebilirsin. O lider bir darboğazdır (bottleneck). **Autonomous** (otonom) ajanlar onu kaldırır: ortada paylaşılan bir task **board**'u (pano) durur ve her boştaki ajan bir sonraki müsait task'ı kendisi **claim** eder (üstlenir), işler, sonra fazlası için geri döner. Merkezi bir dağıtıcı yok — sistem kendi kendini örgütler (self-organizing).

Tutması gereken tek özellik **no double-claim** (çift-sahiplenme yok): bir task tam olarak bir ajana gitmeli, birkaçı aynı anda işe uzansa bile. Bu yüzden claim, *atomic* (atomik) bir "boş mu kontrol et, sonra benim olarak işaretle" adımıdır.

```python
task = claim_next(board, "agent-A")   # pending+sahipsiz -> artık A'nın, in_progress
# ...A onu işler... sonra tekrar claim_next'e döner
```

## Bu neden ölçek arkının zirvesi

Her şeyi birleştir: kalıcı bir task graph (Ders 16) claim edilebilir iş sağlar; message bus (Ders 19) ajanların koordine olmasını sağlar; worktree'ler (Ders 20) düzenlemelerini ayrı tutar; ve self-claiming bir task yığınını kendi kendine çalışan bir swarm'a (sürü) çevirir. Harness board'u ve atomik claim'i sağlar; ajanlar yargıyı sağlar.

## Ne kuracaksın

[`stub.py`](./stub.py) içinde `claim_next(board, agent_id)`'i uygula:

1. `board`'ı sırayla tara; `status == "pending"` **ve** `owner`'ı olmayan ilk task.
2. Onu claim et: `owner = agent_id` ve `status = "in_progress"`; task'ı döndür.
3. Claim edilebilir bir şey yoksa `None` döndür.

## Çalıştır

```sh
python 21_autonomous_agents/eval.py                       # RED
python 21_autonomous_agents/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 21_autonomous_agents/eval.py
```

→ Sonraki: **Ders 22 — The Orchestration Spectrum** (*güvenilir olması gerekeni sabitle, akıllı olması gerekeni devret*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
