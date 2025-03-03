# **Phi-3 következtetés Androidon**

Nézzük meg, hogyan végezhetsz következtetést Phi-3-mini modellel Android eszközökön. A Phi-3-mini a Microsoft új modellcsaládja, amely lehetővé teszi Nagy Nyelvi Modellek (LLM-ek) telepítését edge eszközökre és IoT eszközökre.

## Semantic Kernel és következtetés

A [Semantic Kernel](https://github.com/microsoft/semantic-kernel) egy alkalmazáskeretrendszer, amely lehetővé teszi olyan alkalmazások létrehozását, amelyek kompatibilisek az Azure OpenAI Service-szel, az OpenAI modellekkel, sőt még helyi modellekkel is. Ha új vagy a Semantic Kernel világában, javasoljuk, hogy nézd meg a [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo) útmutatót.

### Phi-3-mini elérése Semantic Kernel segítségével

Ezt kombinálhatod a Semantic Kernelben található Hugging Face Connectorral. Nézd meg ezt a [példakódot](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Alapértelmezés szerint ez megfelel a Hugging Face-en található modellazonosítónak. Azonban csatlakozhatsz egy helyileg futó Phi-3-mini modell szerverhez is.

### Kvantált modellek hívása Ollama vagy LlamaEdge segítségével

Sok felhasználó előnyben részesíti a kvantált modellek használatát a helyi futtatáshoz. Az [Ollama](https://ollama.com/) és a [LlamaEdge](https://llamaedge.com) lehetővé teszi egyéni felhasználók számára, hogy különböző kvantált modelleket hívjanak meg:

#### Ollama

Közvetlenül futtathatod a `ollama run Phi-3`-t, vagy offline konfigurálhatod egy `Modelfile` létrehozásával, amely tartalmazza a `.gguf` fájl elérési útját.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Példakód](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Ha egyszerre szeretnéd használni a `.gguf` fájlokat a felhőben és edge eszközökön, a LlamaEdge remek választás. Kezdéshez nézd meg ezt a [példakódot](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo).

### Telepítés és futtatás Android telefonokon

1. **Töltsd le az MLC Chat alkalmazást** (ingyenes) Android telefonokra.
2. Töltsd le az APK fájlt (148 MB), és telepítsd az eszközödre.
3. Indítsd el az MLC Chat alkalmazást. Az alkalmazásban egy listát fogsz látni AI modellekről, beleértve a Phi-3-mini modellt is.

Összefoglalva, a Phi-3-mini izgalmas lehetőségeket nyit meg a generatív mesterséges intelligencia számára edge eszközökön, és már ma elkezdheted felfedezni képességeit Androidon.

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítási szolgáltatások segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt a professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.