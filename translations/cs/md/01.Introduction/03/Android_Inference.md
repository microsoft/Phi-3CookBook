# **Inference Phi-3 na Androidu**

Pojďme prozkoumat, jak můžete provádět inference s Phi-3-mini na zařízeních s Androidem. Phi-3-mini je nová řada modelů od Microsoftu, která umožňuje nasazení velkých jazykových modelů (LLMs) na edge zařízeních a IoT zařízeních.

## Semantic Kernel a inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) je aplikační rámec, který vám umožňuje vytvářet aplikace kompatibilní s Azure OpenAI Service, modely OpenAI a dokonce i lokálními modely. Pokud jste v Semantic Kernel nováčkem, doporučujeme vám podívat se na [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Přístup k Phi-3-mini pomocí Semantic Kernel

Můžete jej zkombinovat s Hugging Face Connector v Semantic Kernel. Podívejte se na tento [ukázkový kód](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Ve výchozím nastavení odpovídá ID modelu na Hugging Face. Můžete se však také připojit k lokálně vytvořenému serveru modelu Phi-3-mini.

### Volání kvantovaných modelů pomocí Ollama nebo LlamaEdge

Mnoho uživatelů preferuje použití kvantovaných modelů pro lokální běh. [Ollama](https://ollama.com/) a [LlamaEdge](https://llamaedge.com) umožňují jednotlivým uživatelům volat různé kvantované modely:

#### Ollama

Můžete přímo spustit `ollama run Phi-3` nebo jej nakonfigurovat offline vytvořením `Modelfile` s cestou k vašemu `.gguf` souboru.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Ukázkový kód](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Pokud chcete používat `.gguf` soubory v cloudu i na edge zařízeních současně, LlamaEdge je skvělou volbou. Pro začátek se můžete podívat na tento [ukázkový kód](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo).

### Instalace a spuštění na telefonech s Androidem

1. **Stáhněte si aplikaci MLC Chat** (zdarma) pro telefony s Androidem.
2. Stáhněte si APK soubor (148 MB) a nainstalujte jej na své zařízení.
3. Spusťte aplikaci MLC Chat. Zobrazí se seznam AI modelů, včetně Phi-3-mini.

Stručně řečeno, Phi-3-mini otevírá vzrušující možnosti pro generativní AI na edge zařízeních, a můžete začít zkoumat jeho schopnosti na Androidu.

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových AI překladatelských služeb. Přestože se snažíme o přesnost, mějte na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální překlad od člověka. Nenese odpovědnost za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.