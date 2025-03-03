# **Inference Phi-3 på Android**

Låt oss utforska hur du kan utföra inferens med Phi-3-mini på Android-enheter. Phi-3-mini är en ny serie modeller från Microsoft som möjliggör användning av stora språkmodeller (LLMs) på edge-enheter och IoT-enheter.

## Semantic Kernel och inferens

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) är ett applikationsramverk som låter dig skapa applikationer kompatibla med Azure OpenAI Service, OpenAI-modeller och även lokala modeller. Om du är ny på Semantic Kernel föreslår vi att du tittar på [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### För att använda Phi-3-mini med Semantic Kernel

Du kan kombinera det med Hugging Face Connector i Semantic Kernel. Se denna [exempelkod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Som standard motsvarar det modell-ID:t på Hugging Face. Men du kan också ansluta till en lokalt uppsatt Phi-3-mini-modellserver.

### Anropa kvantiserade modeller med Ollama eller LlamaEdge

Många användare föredrar att använda kvantiserade modeller för att köra modeller lokalt. [Ollama](https://ollama.com/) och [LlamaEdge](https://llamaedge.com) gör det möjligt för enskilda användare att anropa olika kvantiserade modeller:

#### Ollama

Du kan direkt köra `ollama run Phi-3` eller konfigurera det offline genom att skapa en `Modelfile` med sökvägen till din `.gguf`-fil.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Exempelkod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Om du vill använda `.gguf`-filer både i molnet och på edge-enheter samtidigt är LlamaEdge ett utmärkt val. Du kan hänvisa till denna [exempelkod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) för att komma igång.

### Installera och köra på Android-telefoner

1. **Ladda ner appen MLC Chat** (gratis) för Android-telefoner.
2. Ladda ner APK-filen (148 MB) och installera den på din enhet.
3. Starta MLC Chat-appen. Du kommer att se en lista över AI-modeller, inklusive Phi-3-mini.

Sammanfattningsvis öppnar Phi-3-mini upp spännande möjligheter för generativ AI på edge-enheter, och du kan börja utforska dess kapaciteter på Android.

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen notera att automatiserade översättningar kan innehålla fel eller inexaktheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för missförstånd eller feltolkningar som uppstår vid användning av denna översättning.