# **Quantiseren van de Phi-familie met llama.cpp**

## **Wat is llama.cpp**

llama.cpp is een open-source softwarebibliotheek, voornamelijk geschreven in C++, die inferentie uitvoert op verschillende Large Language Models (LLMs), zoals Llama. Het hoofddoel is om state-of-the-art prestaties te leveren voor LLM-inferentie op een breed scala aan hardware met minimale configuratie. Daarnaast zijn er Python-bindings beschikbaar voor deze bibliotheek, die een high-level API bieden voor tekstaanvulling en een OpenAI-compatibele webserver.

Het belangrijkste doel van llama.cpp is om LLM-inferentie mogelijk te maken met minimale configuratie en state-of-the-art prestaties op een grote verscheidenheid aan hardware - lokaal en in de cloud.

- Pure C/C++-implementatie zonder afhankelijkheden
- Apple Silicon is een eersteklas platform - geoptimaliseerd via ARM NEON, Accelerate en Metal-frameworks
- AVX-, AVX2- en AVX512-ondersteuning voor x86-architecturen
- 1,5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit en 8-bit integer kwantisatie voor snellere inferentie en minder geheugengebruik
- Aangepaste CUDA-kernels voor het uitvoeren van LLM's op NVIDIA GPU's (ondersteuning voor AMD GPU's via HIP)
- Ondersteuning voor Vulkan- en SYCL-backends
- CPU+GPU hybride inferentie om modellen te versnellen die groter zijn dan de totale VRAM-capaciteit

## **Phi-3.5 kwantiseren met llama.cpp**

Het Phi-3.5-Instruct-model kan worden gekwantiseerd met llama.cpp, maar Phi-3.5-Vision en Phi-3.5-MoE worden momenteel nog niet ondersteund. Het formaat dat door llama.cpp wordt geconverteerd, is GGUF, dat ook het meest gebruikte kwantisatieformaat is.

Er zijn veel gekwantiseerde GGUF-modellen beschikbaar op Hugging Face. AI Foundry, Ollama en LlamaEdge vertrouwen op llama.cpp, dus GGUF-modellen worden vaak gebruikt.

### **Wat is GGUF**

GGUF is een binair formaat dat geoptimaliseerd is voor snel laden en opslaan van modellen, waardoor het zeer efficiënt is voor inferentie. GGUF is ontworpen voor gebruik met GGML en andere uitvoerders. GGUF is ontwikkeld door @ggerganov, die ook de ontwikkelaar is van llama.cpp, een populair C/C++ LLM-inferentieraamwerk. Modellen die oorspronkelijk in frameworks zoals PyTorch zijn ontwikkeld, kunnen worden geconverteerd naar het GGUF-formaat voor gebruik met deze engines.

### **ONNX versus GGUF**

ONNX is een traditioneel machine learning/diep leren-formaat, dat goed wordt ondersteund in verschillende AI-frameworks en nuttige toepassingsscenario's heeft op randapparaten. GGUF daarentegen is gebaseerd op llama.cpp en kan worden beschouwd als een product van het GenAI-tijdperk. De twee hebben vergelijkbare toepassingen. Als je betere prestaties wilt op embedded hardware en applicatielagen, is ONNX wellicht de juiste keuze. Als je gebruik maakt van het afgeleide framework en de technologie van llama.cpp, dan is GGUF waarschijnlijk beter.

### **Phi-3.5-Instruct kwantiseren met llama.cpp**

**1. Omgevingsconfiguratie**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kwantisatie**

Gebruik llama.cpp om Phi-3.5-Instruct te converteren naar FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5 kwantiseren naar INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testen**

Installeer llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Opmerking*** 

Als je Apple Silicon gebruikt, installeer dan llama-cpp-python op deze manier


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testen 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Bronnen**

1. Meer informatie over llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Meer informatie over GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Disclaimer**:  
Dit document is vertaald met behulp van machine-gebaseerde AI-vertalingsdiensten. Hoewel we ons best doen om nauwkeurigheid te garanderen, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.