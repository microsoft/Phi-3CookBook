# **Inferenza di Phi-3 su Android**

Vediamo come eseguire l'inferenza con Phi-3-mini su dispositivi Android. Phi-3-mini è una nuova serie di modelli di Microsoft che consente il deployment di modelli di linguaggio di grandi dimensioni (LLM) su dispositivi edge e IoT.

## Semantic Kernel e Inferenza

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) è un framework applicativo che permette di creare applicazioni compatibili con Azure OpenAI Service, modelli OpenAI e persino modelli locali. Se sei nuovo a Semantic Kernel, ti consigliamo di consultare il [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Per Accedere a Phi-3-mini con Semantic Kernel

Puoi combinarlo con il connettore Hugging Face in Semantic Kernel. Consulta questo [Codice di esempio](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Per impostazione predefinita, corrisponde all'ID del modello su Hugging Face. Tuttavia, è possibile anche connettersi a un server locale con un modello Phi-3-mini.

### Utilizzo di Modelli Quantizzati con Ollama o LlamaEdge

Molti utenti preferiscono utilizzare modelli quantizzati per eseguire i modelli localmente. [Ollama](https://ollama.com/) e [LlamaEdge](https://llamaedge.com) permettono agli utenti di accedere a diversi modelli quantizzati:

#### Ollama

Puoi eseguire direttamente `ollama run Phi-3` o configurarlo offline creando un `Modelfile` con il percorso al tuo file `.gguf`.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Codice di esempio](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Se desideri utilizzare file `.gguf` sia nel cloud che su dispositivi edge, LlamaEdge è un'ottima scelta. Puoi fare riferimento a questo [codice di esempio](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) per iniziare.

### Installazione ed Esecuzione su Telefoni Android

1. **Scarica l'app MLC Chat** (gratuita) per telefoni Android.
2. Scarica il file APK (148 MB) e installalo sul tuo dispositivo.
3. Avvia l'app MLC Chat. Vedrai un elenco di modelli AI, inclusa Phi-3-mini.

In sintesi, Phi-3-mini apre nuove possibilità per l'IA generativa su dispositivi edge, e puoi iniziare a esplorarne le funzionalità su Android.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando servizi di traduzione automatica basati sull'intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali incomprensioni o interpretazioni errate derivanti dall'uso di questa traduzione.