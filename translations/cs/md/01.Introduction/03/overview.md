V kontextu Phi-3-mini se inference vztahuje k procesu používání modelu pro předpovídání nebo generování výstupů na základě vstupních dat. Níže vám poskytnu více informací o Phi-3-mini a jeho schopnostech inference.

Phi-3-mini je součástí řady modelů Phi-3, které vydala společnost Microsoft. Tyto modely jsou navrženy tak, aby předefinovaly možnosti malých jazykových modelů (Small Language Models, SLMs).

Zde jsou klíčové body o Phi-3-mini a jeho schopnostech inference:

## **Přehled Phi-3-mini:**
- Phi-3-mini má velikost parametrů 3,8 miliardy.
- Může běžet nejen na tradičních výpočetních zařízeních, ale také na edge zařízeních, jako jsou mobilní zařízení a IoT zařízení.
- Uvedení Phi-3-mini umožňuje jednotlivcům a podnikům nasazovat SLM na různých hardwarových zařízeních, zejména v prostředích s omezenými zdroji.
- Podporuje různé formáty modelů, včetně tradičního formátu PyTorch, kvantizované verze ve formátu gguf a kvantizované verze založené na ONNX.

## **Přístup k Phi-3-mini:**
K Phi-3-mini můžete přistupovat pomocí [Semantic Kernel](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) v aplikaci Copilot. Semantic Kernel je obecně kompatibilní s Azure OpenAI Service, open-source modely na Hugging Face a lokálními modely.  
Můžete také použít [Ollama](https://ollama.com) nebo [LlamaEdge](https://llamaedge.com) pro volání kvantizovaných modelů. Ollama umožňuje jednotlivým uživatelům volat různé kvantizované modely, zatímco LlamaEdge poskytuje multiplatformní dostupnost pro GGUF modely.

## **Kvantizované modely:**
Mnoho uživatelů dává přednost používání kvantizovaných modelů pro lokální inference. Například můžete přímo spustit Ollama run Phi-3 nebo jej nakonfigurovat offline pomocí Modelfile. Modelfile specifikuje cestu k GGUF souboru a formát promptu.

## **Možnosti generativní AI:**
Kombinace SLM jako Phi-3-mini otevírá nové možnosti pro generativní AI. Inference je jen prvním krokem; tyto modely lze využít pro různé úkoly v prostředích s omezenými zdroji, nízkou latencí a omezenými náklady.

## **Odemykání generativní AI s Phi-3-mini: Průvodce inferencí a nasazením**
Zjistěte, jak používat Semantic Kernel, Ollama/LlamaEdge a ONNX Runtime pro přístup k modelům Phi-3-mini a jejich inferenci, a prozkoumejte možnosti generativní AI v různých aplikačních scénářích.

**Funkce**
Inferování modelu phi3-mini v:

- [Semantic Kernel](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)
- [Ollama](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)
- [LlamaEdge WASM](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo)
- [ONNX Runtime](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/onnx?WT.mc_id=aiml-138114-kinfeylo)
- [iOS](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios?WT.mc_id=aiml-138114-kinfeylo)

Stručně řečeno, Phi-3-mini umožňuje vývojářům prozkoumat různé formáty modelů a využívat generativní AI v různých aplikačních scénářích.

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových AI překladatelských služeb. I když se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Nezodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.