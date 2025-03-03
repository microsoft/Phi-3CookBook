# **Kvantisering af Phi-familien med llama.cpp**

## **Hvad er llama.cpp**

llama.cpp er et open-source softwarebibliotek primært skrevet i C++, der udfører inferens på forskellige Large Language Models (LLMs), såsom Llama. Dets hovedmål er at levere topmoderne ydeevne for LLM-inferens på en bred vifte af hardware med minimal opsætning. Derudover findes der Python-bindings til dette bibliotek, som tilbyder en høj-niveau API til tekstfuldførelse og en OpenAI-kompatibel webserver.

Hovedmålet med llama.cpp er at muliggøre LLM-inferens med minimal opsætning og topmoderne ydeevne på en bred vifte af hardware - både lokalt og i skyen.

- Ren C/C++-implementering uden afhængigheder
- Apple Silicon er en førsteklasses platform - optimeret via ARM NEON, Accelerate og Metal-frameworks
- AVX, AVX2 og AVX512 understøttelse for x86-arkitekturer
- 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit og 8-bit heltalskvantisering for hurtigere inferens og reduceret hukommelsesforbrug
- Custom CUDA-kernels til at køre LLM'er på NVIDIA GPU'er (understøttelse af AMD GPU'er via HIP)
- Vulkan- og SYCL-backend-understøttelse
- Hybrid CPU+GPU-inferens for delvist at accelerere modeller, der er større end den samlede VRAM-kapacitet

## **Kvantisering af Phi-3.5 med llama.cpp**

Phi-3.5-Instruct-modellen kan kvantiseres ved hjælp af llama.cpp, men Phi-3.5-Vision og Phi-3.5-MoE understøttes endnu ikke. Formatet, der konverteres af llama.cpp, er GGUF, som også er det mest udbredte kvantiseringsformat.

Der findes et stort antal kvantiserede GGUF-formatmodeller på Hugging Face. AI Foundry, Ollama og LlamaEdge er afhængige af llama.cpp, så GGUF-modeller bruges også ofte.

### **Hvad er GGUF**

GGUF er et binært format, der er optimeret til hurtig indlæsning og lagring af modeller, hvilket gør det meget effektivt til inferensformål. GGUF er designet til brug med GGML og andre eksekveringsmotorer. GGUF blev udviklet af @ggerganov, som også er udvikleren af llama.cpp, et populært C/C++ LLM-inferensframework. Modeller, der oprindeligt blev udviklet i frameworks som PyTorch, kan konverteres til GGUF-format til brug med disse motorer.

### **ONNX vs GGUF**

ONNX er et traditionelt maskinlærings-/dyb læringsformat, der er godt understøttet i forskellige AI-frameworks og har gode anvendelsesscenarier på edge-enheder. Når det gælder GGUF, er det baseret på llama.cpp og kan siges at være udviklet i GenAI-æraen. De to formater har lignende anvendelser. Hvis du ønsker bedre ydeevne på indlejret hardware og applikationslag, kan ONNX være dit valg. Hvis du bruger afledte frameworks og teknologi fra llama.cpp, kan GGUF være bedre.

### **Kvantisering af Phi-3.5-Instruct med llama.cpp**

**1. Miljøkonfiguration**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantisering**

Brug llama.cpp til at konvertere Phi-3.5-Instruct til FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Kvantisering af Phi-3.5 til INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Test**

Installer llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Bemærk*** 

Hvis du bruger Apple Silicon, skal du installere llama-cpp-python på denne måde


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Test


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Ressourcer**

1. Lær mere om llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Lær mere om GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af AI-baserede maskinoversættelsestjenester. Selvom vi bestræber os på at opnå nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.