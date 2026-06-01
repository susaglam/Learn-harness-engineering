# Ders 05 — Planning

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Plan, niyeti kontrol edilebilir adıma çevirir.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Bir modele çok-adımlı bir görev verirsen sürüklenmeye meyleder — bir adımı unutur, birini tekrarlar, erken zafer ilan eder. Çözüm, ajanı **önce planını yazmaya** zorlayan bir tool: bir `TodoWrite` tool'u. Model, durumlu (status) bir adım listesi üretir; harness onu saklar ve konuşmaya geri render eder (görselleştirir) — böylece plan görünür kalır ve iş ilerledikçe güncellenir.

Bu ucuz ve yüksek kaldıraçlıdır: planı state (durum) olarak dışsallaştırmak uzun görevlerde tamamlanmayı ölçülebilir biçimde artırır ve — Ders 04'e bağlanarak — sana *gözlemleyip* (observe) notlayabileceğin somut bir şey verir.

```python
todo_write([
    {"content": "Read the failing test", "status": "completed"},
    {"content": "Fix the bug",          "status": "in_progress"},
    {"content": "Re-run the suite",     "status": "pending"},
])
# -> "[x] Read the failing test
#     [~] Fix the bug
#     [ ] Re-run the suite
#     (1/3 done)"
```

## Neden geri render edilir

Render edilen liste bir sonraki turda modele beslenir. `[~]`/`[x]` işaretlerini görmek ajanı yönlendirir: ne bitti, sırada ne var, ne kaldı. Bu, *görev* için çalışma belleğidir — tıpkı system prompt'un *rol* için çalışma belleği olması gibi.

## Ne kuracaksın

`render()` verilmiş. [`stub.py`](./stub.py) içinde `TodoStore.write(todos)`'i uygula:

1. Her öğeyi normalize et: `{"content": ..strip'lenmiş.., "status": ..varsayılan "pending"..}`.
2. `self.todos`'u normalize edilmiş listeyle değiştir.
3. `return self.render()`.

## Çalıştır

```sh
python 05_planning/eval.py                       # RED
python 05_planning/eval.py                       # GREEN (TODO'dan sonra)
# referans kontrolü (PowerShell): $env:LHE_SOLUTION=1; python 05_planning/eval.py
```

→ Sonraki: **Ders 06 — Structured I/O** (*modelin okuyacağı çıktıyı tasarla*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
