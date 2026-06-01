# Ders 02 — Tool Use

[English](./README.en.md) | [Türkçe](./README.tr.md)

> **Motto:** *Yeni tool = yeni handler.*
>
> ℹ️ Teknik terimler İngilizce; tam liste → **[Terminoloji Sözlüğü](../docs/terminoloji.tr.md)**.

## Fikir

Ders 01'de loop (döngü) tek, sabit-kodlu bir tool (araç) çağırıyordu. Gerçek ajanlarda *birçok* tool olur ve bu küme zamanla değişir. İşi temiz tutan disiplin şu: **loop'a hiç dokunma, tüm değişkenliği bir dispatch map'e (yönlendirme haritası) koy** — bir tool *adını* iki şeye eşleyen bir registry (kayıt sicili):

- modelin gördüğü bir **schema** (şema — tool'un var olduğunu ve nasıl çağrılacağını bilmesi için), ve
- model çağırınca senin kodunun çalıştırdığı bir **handler** (işleyici).

Tool eklemek böylece tek satıra iner — bir schema + handler kaydet — ve Ders 01'deki loop hiç değişmez. Sadece sabit bir fonksiyon çağırmak yerine `registry.dispatch(name, input)` araması yapar.

```python
registry.dispatch(block.name, block.input)   # loop'un tool'la ilgili tek satırı
```

## Neden bir registry — ve hatalar neden string'e dönüyor

İki tasarım kararı önemli:

1. **Decoupling (ayrıştırma).** Loop hangi tool'ların var olduğunu bilmemeli; bunu registry sahiplenir. Bu dikiş yeri (seam), sonraki derslerde skill'leri (Ders 10) ve MCP tool'larını (Ders 11) loop'u düzenlemeden *aynı* havuza eklemeni sağlar.
2. **Hatalar veridir, çökme değil.** Model var olmayan ya da yanlış argümanlı tool çağıracaktır. `dispatch` ikisini de yakalar ve bir `"ERROR: ..."` string'i döndürür. Bu string modele sıradan bir `tool_result` olarak geri akar; böylece model onu okuyup bir sonraki turda *kendini düzeltir*. `dispatch`'ten kaçan bir exception (istisna) tüm ajanı öldürürdü — kurtarılabilir bir hatayı ölümcül yapardı (bkz. recoverable signal: kurtarılabilir sinyal).

## Ne kuracaksın

[`stub.py`](./stub.py) içinde `ToolRegistry.dispatch(name, tool_input)`'i uygula:

1. `name` bilinen bir handler değilse → `f"ERROR: unknown tool '{name}'"` döndür.
2. Değilse `self.handlers[name](**tool_input)`'i bir `try/except` içinde çağır; başarıda `str(result)`, hatada `f"ERROR: {exc}"` döndür (böylece bir tool hatası ölümcül değil, kurtarılabilir sinyal olur).

## Çalıştır

```sh
python 02_tool_use/eval.py                       # RED — dispatch henüz yok
#   ...stub.py içindeki TODO'yu uygula...
python 02_tool_use/eval.py                       # GREEN

# Referans çözümün de geçtiğini doğrula (PowerShell):
#   $env:LHE_SOLUTION=1; python 02_tool_use/eval.py
```

Eval model gerektirmez: iki sahte tool (`add`, `echo`) kaydeder ve yönlendirmeyi, bilinmeyen-tool yolunu ve handler-hata yolunu kontrol eder — tamamen senin dispatch mantığını.

## Karşılaştır

`stub.py`'ını [`reference.py`](./reference.py) ile karşılaştır. `register`'ın bir decorator (dekoratör) olduğuna ve `schemas()`'in modele `tools=` olarak vereceğin şey olduğuna dikkat et.

→ Sonraki: **Ders 03 — System Prompt** (*ajan konuşmadan önce yapılandırılır*).

← [Müfredat](../CURRICULUM.tr.md) · [README](../README.tr.md)
