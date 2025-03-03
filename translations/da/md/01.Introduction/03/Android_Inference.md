# **Inference Phi-3 på Android**

Lad os udforske, hvordan du kan udføre inferens med Phi-3-mini på Android-enheder. Phi-3-mini er en ny serie af modeller fra Microsoft, der gør det muligt at implementere Large Language Models (LLMs) på edge-enheder og IoT-enheder.

## Semantic Kernel og Inferens

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) er en applikationsramme, der giver dig mulighed for at oprette applikationer kompatible med Azure OpenAI Service, OpenAI-modeller og endda lokale modeller. Hvis du er ny til Semantic Kernel, anbefaler vi, at du kigger på [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Sådan får du adgang til Phi-3-mini med Semantic Kernel

Du kan kombinere det med Hugging Face Connector i Semantic Kernel. Se dette [Eksempel på kode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Som standard svarer det til model-ID'et på Hugging Face. Du kan dog også forbinde til en lokalt opbygget Phi-3-mini modelserver.

### Kald af Kvantiserede Modeller med Ollama eller LlamaEdge

Mange brugere foretrækker at bruge kvantiserede modeller til at køre modeller lokalt. [Ollama](https://ollama.com/) og [LlamaEdge](https://llamaedge.com) giver individuelle brugere mulighed for at kalde forskellige kvantiserede modeller:

#### Ollama

Du kan direkte køre `ollama run Phi-3` eller konfigurere det offline ved at oprette en `Modelfile` med stien til din `.gguf` fil.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Eksempel på kode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Hvis du ønsker at bruge `.gguf` filer både i skyen og på edge-enheder samtidig, er LlamaEdge et godt valg. Du kan henvise til denne [eksempel kode](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) for at komme i gang.

### Installation og Kørsel på Android-telefoner

1. **Download MLC Chat-appen** (Gratis) til Android-telefoner.  
2. Download APK-filen (148MB) og installer den på din enhed.  
3. Start MLC Chat-appen. Du vil se en liste over AI-modeller, inklusive Phi-3-mini.  

Kort sagt åbner Phi-3-mini op for spændende muligheder for generativ AI på edge-enheder, og du kan begynde at udforske dens kapaciteter på Android.

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-baserede maskinoversættelsestjenester. Selvom vi bestræber os på at opnå nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.