# **Kvantisering av Phi-familjen med llama.cpp**

## **Vad är llama.cpp**

llama.cpp är ett öppen källkod-bibliotek skrivet huvudsakligen i C++ som används för inferens på olika stora språkmodeller (LLMs), såsom Llama. Dess huvudsakliga mål är att erbjuda toppmodern prestanda för LLM-inferens på en mängd olika hårdvaror med minimal installation. Dessutom finns det Python-bindningar tillgängliga för detta bibliotek, vilket ger ett högre API för textkomplettering och en OpenAI-kompatibel webbserver.

Huvudsyftet med llama.cpp är att möjliggöra LLM-inferens med minimal installation och toppmodern prestanda på en mängd olika hårdvaror - både lokalt och i molnet.

- Enkel implementation i C/C++ utan några beroenden
- Apple Silicon är en förstklassig medborgare - optimerad via ARM NEON, Accelerate och Metal-ramverk
- AVX, AVX2 och AVX512-stöd för x86-arkitekturer
- 1,5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit och 8-bitars heltalskvantisering för snabbare inferens och minskad minnesanvändning
- Anpassade CUDA-kärnor för att köra LLMs på NVIDIA GPU:er (stöd för AMD GPU:er via HIP)
- Vulkan- och SYCL-bakändestöd
- CPU+GPU hybridinferens för att delvis accelerera modeller som är större än det totala VRAM-kapaciteten

## **Kvantisering av Phi-3.5 med llama.cpp**

Phi-3.5-Instruct-modellen kan kvantiseras med llama.cpp, men Phi-3.5-Vision och Phi-3.5-MoE stöds ännu inte. Formatet som konverteras av llama.cpp är gguf, vilket också är det mest använda kvantiseringsformatet.

Det finns ett stort antal kvantiserade GGUF-formatmodeller på Hugging Face. AI Foundry, Ollama och LlamaEdge förlitar sig på llama.cpp, så GGUF-modeller används också ofta.

### **Vad är GGUF**

GGUF är ett binärt format som är optimerat för snabb laddning och sparande av modeller, vilket gör det mycket effektivt för inferensändamål. GGUF är designat för att användas med GGML och andra exekveringsmiljöer. GGUF utvecklades av @ggerganov, som också är utvecklaren av llama.cpp, ett populärt C/C++-ramverk för LLM-inferens. Modeller som ursprungligen utvecklades i ramverk som PyTorch kan konverteras till GGUF-format för användning med dessa motorer.

### **ONNX vs GGUF**

ONNX är ett traditionellt maskininlärnings-/djupinlärningsformat som stöds väl i olika AI-ramverk och har bra användningsscenarier för kant-enheter. När det gäller GGUF är det baserat på llama.cpp och kan sägas vara framtaget under GenAI-eran. De två har liknande användningsområden. Om du vill ha bättre prestanda i inbäddad hårdvara och applikationslager kan ONNX vara ditt val. Om du använder härledda ramverk och teknik från llama.cpp kan GGUF vara bättre.

### **Kvantisering av Phi-3.5-Instruct med llama.cpp**

**1. Miljökonfiguration**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantisering**

Använd llama.cpp för att konvertera Phi-3.5-Instruct till FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Kvantisera Phi-3.5 till INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testning**

Installera llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Obs*** 

Om du använder Apple Silicon, installera llama-cpp-python på detta sätt


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testning 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Resurser**

1. Läs mer om llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Läs mer om GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, var medveten om att automatiserade översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.