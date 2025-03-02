# **Kvadratizacija Phi Family z uporabo llama.cpp**

## **Kaj je llama.cpp**

llama.cpp je odprtokodna programska knjižnica, napisana predvsem v C++, ki omogoča izvajanje inferenc na različnih modelih velikih jezikov (LLM), kot je Llama. Njen glavni cilj je zagotavljanje vrhunske zmogljivosti pri inferencah LLM na širokem naboru strojne opreme z minimalno nastavitvijo. Poleg tega so za knjižnico na voljo tudi Python povezave, ki ponujajo visokoravni API za dopolnjevanje besedila in spletni strežnik, združljiv z OpenAI.

Glavni cilj llama.cpp je omogočiti inferenco LLM z minimalno nastavitvijo in vrhunsko zmogljivostjo na širokem spektru strojne opreme – lokalno in v oblaku.

- Implementacija v čistem C/C++ brez odvisnosti
- Apple silicon je prvorazredni državljan – optimizirano prek ARM NEON, Accelerate in Metal ogrodij
- Podpora za AVX, AVX2 in AVX512 za x86 arhitekture
- Kvadratizacija celih števil z 1,5-bitno, 2-bitno, 3-bitno, 4-bitno, 5-bitno, 6-bitno in 8-bitno natančnostjo za hitrejšo inferenco in manjšo porabo pomnilnika
- Prilagojena CUDA jedra za izvajanje LLM na NVIDIA GPU-jih (podpora za AMD GPU-je prek HIP)
- Podpora za Vulkan in SYCL zaledje
- Hibridna CPU+GPU inferenca za delno pospeševanje modelov, večjih od celotne zmogljivosti VRAM

## **Kvadratizacija Phi-3.5 z uporabo llama.cpp**

Model Phi-3.5-Instruct je mogoče kvadratizirati z uporabo llama.cpp, vendar modela Phi-3.5-Vision in Phi-3.5-MoE še nista podprta. Format, ki ga pretvori llama.cpp, je gguf, ki je tudi najbolj razširjen format za kvadratizacijo.

Na Hugging Face je na voljo veliko modelov v kvadratiziranem formatu GGUF. AI Foundry, Ollama in LlamaEdge se zanašajo na llama.cpp, zato se modeli GGUF pogosto uporabljajo.

### **Kaj je GGUF**

GGUF je binarni format, optimiziran za hitro nalaganje in shranjevanje modelov, zaradi česar je zelo učinkovit za namene inferenc. GGUF je zasnovan za uporabo z GGML in drugimi izvajalniki. GGUF je razvil @ggerganov, ki je tudi razvijalec llama.cpp, priljubljenega C/C++ okvira za inferenco LLM. Modele, prvotno razvite v ogrodjih, kot je PyTorch, je mogoče pretvoriti v format GGUF za uporabo s temi orodji.

### **ONNX proti GGUF**

ONNX je tradicionalen format za strojno učenje/globoko učenje, ki je dobro podprt v različnih AI ogrodjih in ima uporabne scenarije na robnih napravah. GGUF pa temelji na llama.cpp in lahko rečemo, da je bil ustvarjen v obdobju GenAI. Oba imata podobne namene. Če želite boljšo zmogljivost na vgrajeni strojni opremi in aplikacijskih slojih, je ONNX morda vaša izbira. Če uporabljate derivativni okvir in tehnologijo llama.cpp, je GGUF morda boljša izbira.

### **Kvadratizacija Phi-3.5-Instruct z uporabo llama.cpp**

**1. Konfiguracija okolja**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvadratizacija**

Z uporabo llama.cpp pretvorite Phi-3.5-Instruct v FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Kvadratizacija Phi-3.5 v INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testiranje**

Namestite llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Opomba*** 

Če uporabljate Apple Silicon, namestite llama-cpp-python na ta način


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testiranje 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Viri**

1. Več o llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Več o GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo strojnih storitev za prevajanje, ki temeljijo na umetni inteligenci. Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije je priporočljivo profesionalno človeško prevajanje. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi izhajale iz uporabe tega prevoda.