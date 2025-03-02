# **Inference Phi-3 pe Android**

Să explorăm cum poți realiza inferență cu Phi-3-mini pe dispozitive Android. Phi-3-mini este o nouă serie de modele de la Microsoft care permite implementarea modelelor de limbaj mari (LLM) pe dispozitive edge și IoT.

## Semantic Kernel și Inferență

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) este un framework de aplicații care îți permite să creezi aplicații compatibile cu Azure OpenAI Service, modelele OpenAI și chiar modele locale. Dacă ești nou în utilizarea Semantic Kernel, îți sugerăm să consulți [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Accesarea Phi-3-mini folosind Semantic Kernel

Poți combina acest framework cu Hugging Face Connector din Semantic Kernel. Consultă acest [Exemplu de Cod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Implicit, acesta corespunde unui model ID pe Hugging Face. Totuși, poți conecta și un server local pe care ai construit modelul Phi-3-mini.

### Apelarea modelelor cuantificate cu Ollama sau LlamaEdge

Mulți utilizatori preferă utilizarea modelelor cuantificate pentru a rula local. [Ollama](https://ollama.com/) și [LlamaEdge](https://llamaedge.com) permit utilizatorilor să apeleze diferite modele cuantificate:

#### Ollama

Poți rula direct `ollama run Phi-3` sau îl poți configura offline creând un `Modelfile` cu calea către fișierul `.gguf`.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Exemplu de Cod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Dacă dorești să utilizezi fișierele `.gguf` atât în cloud, cât și pe dispozitive edge, LlamaEdge este o alegere excelentă. Poți consulta acest [exemplu de cod](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) pentru a începe.

### Instalare și rulare pe telefoane Android

1. **Descarcă aplicația MLC Chat** (gratuită) pentru telefoanele Android.
2. Descarcă fișierul APK (148MB) și instalează-l pe dispozitivul tău.
3. Lansează aplicația MLC Chat. Vei vedea o listă de modele AI, inclusiv Phi-3-mini.

În concluzie, Phi-3-mini deschide posibilități interesante pentru AI generativ pe dispozitive edge, iar acum poți explora capabilitățile sale pe Android.

**Declinarea responsabilității**:  
Acest document a fost tradus folosind servicii de traducere automată bazate pe inteligență artificială. Deși depunem eforturi pentru a asigura acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.