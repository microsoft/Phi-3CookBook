# **Inference Phi-3 på Android**

La oss se hvordan du kan utføre inferens med Phi-3-mini på Android-enheter. Phi-3-mini er en ny serie modeller fra Microsoft som gjør det mulig å bruke store språkmodeller (LLMs) på kant- og IoT-enheter.

## Semantic Kernel og inferens

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) er et rammeverk som lar deg lage applikasjoner kompatible med Azure OpenAI Service, OpenAI-modeller og til og med lokale modeller. Hvis du er ny på Semantic Kernel, anbefaler vi at du tar en titt på [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### For å få tilgang til Phi-3-mini med Semantic Kernel

Du kan kombinere det med Hugging Face Connector i Semantic Kernel. Se denne [eksempelkoden](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Som standard tilsvarer det modell-ID-en på Hugging Face. Du kan imidlertid også koble til en lokalt bygget Phi-3-mini-modelltjener.

### Kjøre kvantiserte modeller med Ollama eller LlamaEdge

Mange brukere foretrekker å bruke kvantiserte modeller for å kjøre modeller lokalt. [Ollama](https://ollama.com/) og [LlamaEdge](https://llamaedge.com) lar enkeltbrukere kjøre ulike kvantiserte modeller:

#### Ollama

Du kan kjøre `ollama run Phi-3` direkte eller konfigurere det offline ved å opprette en `Modelfile` med banen til din `.gguf`-fil.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Eksempelkode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Hvis du ønsker å bruke `.gguf`-filer både i skyen og på kant-enheter samtidig, er LlamaEdge et godt valg. Du kan se denne [eksempelkoden](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) for å komme i gang.

### Installere og kjøre på Android-telefoner

1. **Last ned MLC Chat-appen** (gratis) for Android-telefoner.  
2. Last ned APK-filen (148 MB) og installer den på enheten din.  
3. Start MLC Chat-appen. Du vil se en liste over AI-modeller, inkludert Phi-3-mini.

Oppsummert åpner Phi-3-mini opp for spennende muligheter for generativ AI på kant-enheter, og du kan begynne å utforske dens funksjoner på Android.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettingstjenester. Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.