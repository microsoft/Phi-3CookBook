# **Kvantisering av Phi-familien med llama.cpp**

## **Hva er llama.cpp**

llama.cpp er et åpen kildekode-bibliotek skrevet primært i C++ som utfører inferens på ulike store språkmodeller (LLMs), som Llama. Hovedmålet er å levere topp ytelse for LLM-inferens på et bredt spekter av maskinvare med minimal oppsett. I tillegg finnes det Python-bindinger for dette biblioteket, som tilbyr et høynivå-API for tekstfullføring og en OpenAI-kompatibel webserver.

Hovedmålet med llama.cpp er å muliggjøre LLM-inferens med minimal oppsett og topp ytelse på et bredt spekter av maskinvare – både lokalt og i skyen.

- Ren C/C++-implementasjon uten avhengigheter
- Apple Silicon er en førsteklasses plattform – optimalisert med ARM NEON, Accelerate og Metal-rammeverk
- AVX, AVX2 og AVX512-støtte for x86-arkitekturer
- 1,5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit og 8-bit heltalls-kvantisering for raskere inferens og redusert minnebruk
- Egendefinerte CUDA-kjerner for å kjøre LLM-er på NVIDIA GPU-er (støtte for AMD GPU-er via HIP)
- Vulkan- og SYCL-backend-støtte
- Hybrid CPU+GPU-inferens for delvis å akselerere modeller som er større enn den totale VRAM-kapasiteten

## **Kvantisering av Phi-3.5 med llama.cpp**

Phi-3.5-Instruct-modellen kan kvantiseres med llama.cpp, men Phi-3.5-Vision og Phi-3.5-MoE støttes foreløpig ikke. Formatet som konverteres av llama.cpp er gguf, som også er det mest brukte kvantiseringsformatet.

Det finnes et stort antall kvantiserte GGUF-formatmodeller på Hugging Face. AI Foundry, Ollama og LlamaEdge bruker llama.cpp, så GGUF-modeller er også ofte i bruk.

### **Hva er GGUF**

GGUF er et binært format som er optimalisert for rask lasting og lagring av modeller, noe som gjør det svært effektivt for inferensformål. GGUF er designet for bruk med GGML og andre eksekveringsmotorer. GGUF ble utviklet av @ggerganov, som også er utvikleren av llama.cpp, et populært C/C++ LLM-inferensrammeverk. Modeller som opprinnelig er utviklet i rammeverk som PyTorch kan konverteres til GGUF-format for bruk med disse motorene.

### **ONNX vs GGUF**

ONNX er et tradisjonelt maskinlærings-/dyp læringsformat som er godt støttet i ulike AI-rammeverk og har gode bruksområder på kant-enheter. Når det gjelder GGUF, er det basert på llama.cpp og kan sies å være et produkt av GenAI-æraen. De to har lignende bruksområder. Hvis du ønsker bedre ytelse på innebygd maskinvare og applikasjonslag, kan ONNX være ditt valg. Hvis du bruker rammeverket og teknologien avledet fra llama.cpp, kan GGUF være bedre.

### **Kvantisering av Phi-3.5-Instruct med llama.cpp**

**1. Miljøkonfigurasjon**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantisering**

Bruke llama.cpp for å konvertere Phi-3.5-Instruct til FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Kvantisere Phi-3.5 til INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testing**

Installer llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Merk*** 

Hvis du bruker Apple Silicon, installer llama-cpp-python slik


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testing 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Ressurser**

1. Lær mer om llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Lær mer om GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.