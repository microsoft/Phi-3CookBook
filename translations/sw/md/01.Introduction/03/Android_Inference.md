# **Inference Phi-3 kwenye Android**

Hebu tuangalie jinsi unavyoweza kufanya inference na Phi-3-mini kwenye vifaa vya Android. Phi-3-mini ni mfululizo mpya wa modeli kutoka Microsoft unaowezesha matumizi ya Large Language Models (LLMs) kwenye vifaa vya ukingoni na vifaa vya IoT.

## Semantic Kernel na Inference

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) ni mfumo wa programu unaokuwezesha kuunda programu zinazooana na Azure OpenAI Service, modeli za OpenAI, na hata modeli za ndani. Ikiwa wewe ni mgeni kwenye Semantic Kernel, tunapendekeza uangalie [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo).

### Kupata Phi-3-mini kwa Kutumia Semantic Kernel

Unaweza kuichanganya na Hugging Face Connector ndani ya Semantic Kernel. Rejelea [Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo).

Kwa chaguo-msingi, inalingana na ID ya modeli kwenye Hugging Face. Hata hivyo, unaweza pia kuunganisha kwenye seva ya modeli ya Phi-3-mini iliyojengwa ndani.

### Kuita Modeli Zilizopunguzwa na Ollama au LlamaEdge

Watumiaji wengi wanapendelea kutumia modeli zilizopunguzwa ili kuziendesha ndani ya nchi. [Ollama](https://ollama.com/) na [LlamaEdge](https://llamaedge.com) zinawawezesha watumiaji binafsi kuita modeli tofauti zilizopunguzwa:

#### Ollama

Unaweza moja kwa moja kuendesha `ollama run Phi-3` au kuisanidi nje ya mtandao kwa kuunda `Modelfile` yenye njia ya faili yako ya `.gguf`.

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[Sample Code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

Ikiwa unataka kutumia faili za `.gguf` kwenye wingu na kwenye vifaa vya ukingoni kwa wakati mmoja, LlamaEdge ni chaguo bora. Unaweza kurejelea [sample code](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) kuanza.

### Kusanidi na Kuendesha kwenye Simu za Android

1. **Pakua programu ya MLC Chat** (Bure) kwa simu za Android.  
2. Pakua faili ya APK (148MB) na usakinishe kwenye kifaa chako.  
3. Fungua programu ya MLC Chat. Utaona orodha ya modeli za AI, ikijumuisha Phi-3-mini.  

Kwa muhtasari, Phi-3-mini inafungua uwezekano wa kusisimua wa AI generative kwenye vifaa vya ukingoni, na unaweza kuanza kuchunguza uwezo wake kwenye Android.

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za kutafsiri za AI zinazotegemea mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya awali inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia huduma za utafsiri wa kibinadamu wa kitaalamu. Hatutawajibika kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.