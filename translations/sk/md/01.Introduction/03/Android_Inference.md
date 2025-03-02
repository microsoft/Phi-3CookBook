# **Inference Phi-3 v systéme Android**

Pozrime sa, ako môžete vykonávať inferenciu s Phi-3-mini na zariadeniach s Androidom. Phi-3-mini je nová séria modelov od spoločnosti Microsoft, ktorá umožňuje nasadenie veľkých jazykových modelov (LLM) na edge zariadeniach a IoT zariadeniach.

## Semantic Kernel a Inferencia

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) je aplikačný rámec, ktorý vám umožňuje vytvárať aplikácie kompatibilné so službou Azure OpenAI Service, modelmi OpenAI a dokonca aj lokálnymi modelmi. Ak ste v Semantic Kernel nováčikom, odporúčame vám pozrieť si [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Ako získať prístup k Phi-3-mini pomocou Semantic Kernel

Môžete ho skombinovať s Hugging Face Connector v rámci Semantic Kernel. Pozrite si tento [ukážkový kód](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Predvolene zodpovedá ID modelu na Hugging Face. Môžete sa však pripojiť aj k lokálne vytvorenému serveru modelu Phi-3-mini.

### Volanie kvantovaných modelov s Ollama alebo LlamaEdge

Mnoho používateľov uprednostňuje používanie kvantovaných modelov na lokálny chod modelov. [Ollama](https://ollama.com/) a [LlamaEdge](https://llamaedge.com) umožňujú jednotlivým používateľom volať rôzne kvantované modely:

#### Ollama

Môžete priamo spustiť `ollama run Phi-3` alebo ho nastaviť offline vytvorením `Modelfile` s cestou k vášmu `.gguf` súboru.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Ukážkový kód](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Ak chcete používať `.gguf` súbory v cloude aj na edge zariadeniach súčasne, LlamaEdge je skvelou voľbou. Môžete si pozrieť tento [ukážkový kód](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo), aby ste mohli začať.

### Inštalácia a spustenie na telefónoch s Androidom

1. **Stiahnite si aplikáciu MLC Chat** (zadarmo) pre telefóny s Androidom.  
2. Stiahnite si súbor APK (148 MB) a nainštalujte ho do svojho zariadenia.  
3. Spustite aplikáciu MLC Chat. Uvidíte zoznam AI modelov vrátane Phi-3-mini.  

Na záver, Phi-3-mini otvára vzrušujúce možnosti pre generatívnu AI na edge zariadeniach a môžete začať objavovať jeho schopnosti na Androide.

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových AI prekladateľských služieb. Aj keď sa snažíme o presnosť, upozorňujeme, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.