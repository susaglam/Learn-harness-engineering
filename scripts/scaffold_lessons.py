"""Scaffold stub READMEs (EN + TR) for lessons not yet fully built.

Idempotent: only writes a README if it does not already exist, so it never
overwrites a lesson you've finished. Run from anywhere:

    python scripts/scaffold_lessons.py
"""
from __future__ import annotations

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# num, slug, title, arc_en, arc_tr, motto_en, motto_tr, build_en, build_tr
LESSONS = [
    ("02", "tool_use", "Tool Use", "The Core", "Çekirdek",
     "A new tool is just a new handler", "Yeni tool = yeni handler",
     "A dispatch map so you can add tools without touching the loop.",
     "Döngüye dokunmadan tool eklemeni sağlayan bir dispatch haritası."),
    ("03", "system_prompt", "System Prompt", "The Core", "Çekirdek",
     "The agent is configured before it speaks", "Ajan konuşmadan önce yapılandırılır",
     "Assemble the system prompt at runtime from composable sections.",
     "System prompt'u runtime'da birleştirilebilir parçalardan montajla."),
    ("04", "eval_observability", "Eval & Observability", "The Core", "Çekirdek",
     "If you can't measure it, you're hoping", "Ölçemiyorsan umuyorsun demektir",
     "A trajectory tracer plus scorers that grade an agent run.",
     "Bir trajectory (yörünge) izleyici + ajan koşumunu notlayan scorer'lar."),
    ("05", "planning", "Planning", "Doing Real Work", "Gerçek İş",
     "A plan turns intention into checkable steps", "Plan, niyeti kontrol edilebilir adıma çevirir",
     "A TodoWrite tool the agent uses to plan first, then execute.",
     "Ajanın önce plan yapıp sonra uyguladığı bir TodoWrite tool'u."),
    ("06", "structured_io", "Structured I/O", "Doing Real Work", "Gerçek İş",
     "Design the output the model has to read", "Modelin okuyacağı çıktıyı tasarla",
     "Schema-validated tool results with retry-on-mismatch.",
     "Şema-doğrulamalı tool sonuçları + uyumsuzlukta yeniden deneme."),
    ("07", "context_economics", "Context & Token Economics", "Doing Real Work", "Gerçek İş",
     "Context is a budget; spend it deliberately", "Context bir bütçedir; bilinçli harca",
     "Compaction strategies plus a token-budget meter.",
     "Compaction (sıkıştırma) stratejileri + token bütçe göstergesi."),
    ("08", "subagents", "Subagents", "Doing Real Work", "Gerçek İş",
     "Delegate the noise, keep the signal", "Gürültüyü devret, sinyali tut",
     "Spawn a child agent with fresh context; return only its result.",
     "Temiz bağlamlı bir alt-ajan başlat; yalnızca sonucunu döndür."),
    ("09", "memory_retrieval", "Memory & Retrieval", "Knowledge & Memory", "Bilgi & Hafıza",
     "Remember what matters; retrieve when relevant", "Önemliyi hatırla, gerektiğinde geri çağır",
     "Persist facts to disk and recall them semantically with embeddings.",
     "Gerçekleri diske yaz, embedding ile semantik olarak geri çağır."),
    ("10", "skill_loading", "Skill Loading", "Knowledge & Memory", "Bilgi & Hafıza",
     "Load knowledge on demand, not upfront", "Bilgiyi talep üzerine yükle",
     "A skill manifest; inject a skill's body only when it's needed.",
     "Skill manifest'i; skill gövdesini yalnızca gerektiğinde enjekte et."),
    ("11", "mcp", "MCP", "Knowledge & Memory", "Bilgi & Hafıza",
     "Borrow capabilities; keep one tool pool", "Yeteneği ödünç al, tek havuzda tut",
     "Route an external MCP server's tools into the same loop.",
     "Dış bir MCP sunucusunun tool'larını aynı döngüye yönlendir."),
    ("12", "permissions", "Permissions & Trust", "Hardening", "Sertleştirme",
     "Freedom needs boundaries to be safe", "Özgürlük güvenli olmak için sınır ister",
     "A permission pipeline that resolves allow / ask / deny.",
     "allow / ask / deny çözen bir izin hattı."),
    ("13", "security_injection", "Security & Injection", "Hardening", "Sertleştirme",
     "Every token from outside is a potential adversary", "Dışarıdan gelen her token potansiyel düşman",
     "Quarantine untrusted content and detect prompt-injection attempts.",
     "Güvenilmeyen içeriği karantinaya al, prompt-injection tespit et."),
    ("14", "hooks", "Hooks", "Hardening", "Sertleştirme",
     "Extend around the loop, never rewrite it", "Döngünün etrafını genişlet, döngüyü yazma",
     "PreToolUse / PostToolUse extension points around the loop.",
     "Döngünün etrafında PreToolUse / PostToolUse genişletme noktaları."),
    ("15", "error_recovery", "Error Recovery", "Hardening", "Sertleştirme",
     "Failure is a branch, not a dead end", "Hata bir dal, çıkmaz sokak değil",
     "A failure taxonomy with retry and fallback strategies.",
     "Retry ve fallback stratejileriyle bir hata taksonomisi."),
    ("16", "task_graphs", "Task Graphs", "Scale", "Ölçek",
     "Big goals persist to disk as ordered tasks", "Büyük hedef diske sıralı task olur",
     "A file-backed task graph with blockedBy dependencies.",
     "blockedBy bağımlılıklı, diske yazılı bir task grafiği."),
    ("17", "background_async", "Background & Async", "Scale", "Ölçek",
     "Slow work goes async; the agent keeps thinking", "Yavaş iş arka plana, ajan düşünmeye devam",
     "Threaded execution plus a completion-notification queue.",
     "İş-parçacıklı çalıştırma + tamamlanma bildirim kuyruğu."),
    ("18", "cron_scheduler", "Cron / Self-Scheduling", "Scale", "Ölçek",
     "The agent can wake itself", "Ajan kendini uyandırabilir",
     "Durable scheduled triggers fired by time.",
     "Zamanla tetiklenen kalıcı zamanlanmış görevler."),
    ("19", "agent_teams", "Agent Teams & Protocols", "Scale", "Ölçek",
     "Too big for one - coordinate many", "Tek ajana büyük gelen iş -> koordinasyon",
     "Persistent teammates, an async mailbox, and a request/reply protocol.",
     "Kalıcı takım arkadaşları, async mailbox ve istek/yanıt protokolü."),
    ("20", "worktree_isolation", "Worktree Isolation", "Scale", "Ölçek",
     "Each agent gets its own room", "Her ajana kendi odası",
     "Bind tasks to git worktrees so parallel agents don't collide.",
     "Task'ları git worktree'lere bağla; paralel ajanlar çakışmasın."),
    ("21", "autonomous_agents", "Autonomous Agents", "Scale", "Ölçek",
     "Agents that claim their own work", "İşini kendi çeken ajanlar",
     "An idle loop where agents self-claim work from a board.",
     "Ajanların panodan işi kendi aldığı bir idle (boşta) döngüsü."),
    ("22", "orchestration_spectrum", "The Orchestration Spectrum", "Synthesis", "Sentez",
     "Hardcode what must be reliable; delegate what must be smart",
     "Güvenilir olması gerekeni sabitle, akıllı olması gerekeni devret",
     "The same task solved at three points on the determinism-autonomy axis, scored.",
     "Aynı görevi determinizm-otonomi ekseninde üç noktada çöz, notla."),
    ("23", "comprehensive", "The Comprehensive Agent", "Synthesis", "Sentez",
     "Many mechanisms, one measurable loop", "Çok mekanizma, tek ölçülebilir döngü",
     "Assemble every mechanism around one loop, with evals proving it works.",
     "Tüm mekanizmaları tek döngü etrafında birleştir, eval'lerle kanıtla."),
    ("24", "secrets_sandboxing", "Secrets, Sandboxing & Audit", "Production", "Production",
     "Never let a secret reach the model or a log", "Secret'ı modele/log'a ulaştırma",
     "Redact known + secret-shaped values.",
     "Bilinen + secret-biçimli değerleri redact et."),
    ("25", "concurrency_leases", "Concurrency & Leases", "Production", "Production",
     "A claim you don't renew, you lose", "Yenilemediğin claim'i kaybedersin",
     "A lease-with-TTL acquire that reclaims on expiry.",
     "Expire'da reclaim eden, TTL'li lease acquire."),
    ("26", "human_in_the_loop", "Human-in-the-Loop", "Production", "Production",
     "Some actions wait for a human", "Bazı eylemler bir insanı bekler",
     "An approval-gated execute (pending / approved / denied).",
     "Onay-kapılı execute (pending / approved / denied)."),
    ("27", "tool_result_management", "Tool-Result Management", "Production", "Production",
     "A 10MB result will blow your context", "10MB'lık sonuç context'i patlatır",
     "Bound a huge result; keep a handle to the rest.",
     "Dev sonucu sınırla; gerisine bir handle tut."),
    ("28", "versioning_migration", "Versioning & Migration", "Production", "Production",
     "Long-lived state needs migrations", "Uzun yaşayan state migration ister",
     "An ordered record-migration chain.",
     "Sıralı bir record-migration zinciri."),
    ("29", "eval_expansion", "Eval Expansion", "Production", "Production",
     "Grade trajectories, not vibes - with budgets", "Vibe değil, yörünge notla - bütçelerle",
     "Golden-trajectory + step/cost budget scorers.",
     "Golden-trajectory + step/cost bütçe scorer'ları."),
]

EN_TMPL = """# Lesson {num} — {title}

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *{motto_en}*

**Arc:** {arc_en} · **Status:** \U0001f527 scaffold — not yet implemented

## What this lesson adds

{build_en}

## When built, this folder will contain

- `README.en.md` / `README.tr.md` — the narrative (the idea and why it matters)
- `reference.py` — the complete implementation
- `stub.py` — the 5–10 lines you implement (the TODO)
- `eval.py` — RED until your stub is correct

← [Curriculum](../CURRICULUM.md) · [README](../README.md)
"""

TR_TMPL = """# Ders {num} — {title}

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *{motto_tr}*
>
> ℹ️ Teknik terimler İngilizce; açıklamalar için → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

**Ark:** {arc_tr} · **Durum:** \U0001f527 iskelet — henüz implemente edilmedi

## Bu ders ne ekler

{build_tr}

## Kurulduğunda bu klasör şunları içerecek

- `README.en.md` / `README.tr.md` — anlatı (fikir ve neden önemli olduğu)
- `reference.py` — tam implementasyon
- `stub.py` — senin yazacağın 5–10 satır (TODO)
- `eval.py` — stub'ın doğru olana dek RED

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
"""


def write_if_absent(path: str, text: str) -> bool:
    if os.path.exists(path):
        return False
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    return True


def main() -> None:
    created = 0
    for (num, slug, title, arc_en, arc_tr, motto_en, motto_tr,
         build_en, build_tr) in LESSONS:
        folder = os.path.join(ROOT, f"{num}_{slug}")
        os.makedirs(folder, exist_ok=True)
        fields = dict(num=num, title=title, arc_en=arc_en, arc_tr=arc_tr,
                      motto_en=motto_en, motto_tr=motto_tr,
                      build_en=build_en, build_tr=build_tr)
        if write_if_absent(os.path.join(folder, "README.en.md"),
                           EN_TMPL.format(**fields)):
            created += 1
        if write_if_absent(os.path.join(folder, "README.tr.md"),
                           TR_TMPL.format(**fields)):
            created += 1
        print(f"  {num}_{slug}")
    print(f"\nScaffold done. {created} README file(s) written, "
          f"{len(LESSONS)} lesson folders ensured.")


if __name__ == "__main__":
    main()
