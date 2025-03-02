# **Inference Phi-3 amin'ny Android**

Andao hojerentsika ny fomba ahafahanao manao inference miaraka amin'ny Phi-3-mini amin'ny fitaovana Android. Ny Phi-3-mini dia andiany vaovao amin'ny modely avy amin'i Microsoft izay ahafahana mampiasa Large Language Models (LLMs) amin'ny fitaovana edge sy IoT.

## Semantic Kernel sy Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) dia rafitra fampiharana ahafahanao mamorona rindranasa mifanaraka amin'ny Azure OpenAI Service, modely OpenAI, ary na dia modely eo an-toerana aza. Raha vao manomboka ianao dia manoro hevitra izahay mba hijery ny [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Ahoana ny Fidirana amin'ny Phi-3-mini Amin'ny Alalan'ny Semantic Kernel

Afaka mampifandray izany amin'ny Hugging Face Connector ao amin'ny Semantic Kernel ianao. Jereo ny [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Amin'ny ankapobeny, mifanaraka amin'ny model ID ao amin'ny Hugging Face izany. Na izany aza, azonao atao koa ny mampifandray amin'ny server modely Phi-3-mini izay naorina eo an-toerana.

### Fampiasana Modely Quantized miaraka amin'i Ollama na LlamaEdge

Maro ireo mpampiasa no tia mampiasa modely quantized mba hampandehanana modely eo an-toerana. [Ollama](https://ollama.com/) sy [LlamaEdge](https://llamaedge.com) dia ahafahan'ny mpampiasa tsirairay miantso modely quantized samihafa:

#### Ollama

Afaka mampandeha mivantana `ollama run Phi-3` ianao na manamboatra azy io amin'ny fomba offline amin'ny famoronana `Modelfile` miaraka amin'ny làlan'ny `.gguf` anao.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Jereo ny ohatra amin'ny kaody](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Raha tianao ny mampiasa `.gguf` amin'ny rahona sy amin'ny fitaovana edge miaraka, dia safidy tsara ny LlamaEdge. Azonao jerena ity [ohatra amin'ny kaody](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) ity raha te hanomboka ianao.

### Fametrahana sy Fampandehanana amin'ny Finday Android

1. **Sintomy ny rindranasa MLC Chat** (Maimaimpoana) ho an'ny finday Android.
2. Sintomy ny rakitra APK (148MB) ary apetraho ao amin'ny fitaovanao.
3. Sokafy ny rindranasa MLC Chat. Hiseho eo ny lisitry ny modely AI, anisan'izany ny Phi-3-mini.

Raha fintinina, ny Phi-3-mini dia manokatra fahafahana mahaliana ho an'ny generative AI amin'ny fitaovana edge, ary azonao atao ny manomboka mijery ny fahaizany amin'ny Android.

It seems like "mo" might refer to a specific language or abbreviation, but it's unclear which one you're referring to. Could you clarify which language you'd like the text translated into? For example, is it Maori, Mongolian, or something else?