# **Kvantizacija Phi obitelji pomoću llama.cpp**

## **Što je llama.cpp**

llama.cpp je open-source softverska biblioteka napisana prvenstveno u C++ jeziku koja omogućuje izvođenje inferencije na raznim Velikim Jezičnim Modelima (LLMs), poput Llama. Njezin glavni cilj je pružiti vrhunske performanse za inferenciju LLM-ova na širokom spektru hardvera uz minimalnu konfiguraciju. Osim toga, dostupne su Python poveznice za ovu biblioteku, koje nude API visoke razine za dovršavanje teksta i web poslužitelj kompatibilan s OpenAI-jem.

Glavni cilj llama.cpp je omogućiti inferenciju LLM-ova uz minimalnu konfiguraciju i vrhunske performanse na raznovrsnom hardveru - lokalno i u oblaku.

- Implementacija u čistom C/C++ bez dodatnih ovisnosti
- Apple Silicon ima prioritet - optimiziran putem ARM NEON, Accelerate i Metal okvira
- Podrška za AVX, AVX2 i AVX512 za x86 arhitekture
- Kvantizacija u 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit i 8-bitne cijele brojeve za bržu inferenciju i smanjenu potrošnju memorije
- Prilagođene CUDA jezgre za izvođenje LLM-ova na NVIDIA GPU-ovima (podrška za AMD GPU-ove putem HIP-a)
- Vulkan i SYCL podrška za pozadinske procese
- Hibridna CPU+GPU inferencija za djelomično ubrzavanje modela većih od ukupnog kapaciteta VRAM-a

## **Kvantizacija Phi-3.5 pomoću llama.cpp**

Model Phi-3.5-Instruct može se kvantizirati pomoću llama.cpp, ali Phi-3.5-Vision i Phi-3.5-MoE još nisu podržani. Format koji llama.cpp koristi za konverziju je gguf, koji je ujedno i najrašireniji format za kvantizaciju.

Na Hugging Face platformi postoji velik broj modela u kvantiziranom GGUF formatu. AI Foundry, Ollama i LlamaEdge oslanjaju se na llama.cpp, pa se GGUF modeli također često koriste.

### **Što je GGUF**

GGUF je binarni format optimiziran za brzo učitavanje i spremanje modela, što ga čini vrlo učinkovitim za potrebe inferencije. GGUF je dizajniran za upotrebu s GGML-om i drugim izvršnim sustavima. GGUF je razvio @ggerganov, koji je ujedno i autor llama.cpp, popularnog C/C++ okvira za inferenciju LLM-ova. Modeli izvorno razvijeni u okvirima poput PyTorcha mogu se konvertirati u GGUF format za upotrebu s tim alatima.

### **ONNX vs GGUF**

ONNX je tradicionalni format za strojno učenje/duboko učenje, koji je dobro podržan u različitim AI okvirima i ima dobre scenarije primjene na rubnim uređajima. S druge strane, GGUF je baziran na llama.cpp i može se smatrati proizvodom GenAI ere. Oba formata imaju slične namjene. Ako želite bolje performanse na ugrađenom hardveru i aplikacijskim slojevima, ONNX bi mogao biti vaš izbor. Ako koristite izvedene okvire i tehnologiju llama.cpp, tada bi GGUF mogao biti bolji.

### **Kvantizacija Phi-3.5-Instruct pomoću llama.cpp**

**1. Konfiguracija okruženja**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantizacija**

Koristeći llama.cpp konvertirajte Phi-3.5-Instruct u FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Kvantizacija Phi-3.5 u INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testiranje**

Instalirajte llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Napomena*** 

Ako koristite Apple Silicon, instalirajte llama-cpp-python ovako


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testiranje 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Resursi**

1. Saznajte više o llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Saznajte više o GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden koristeći usluge strojno baziranog AI prijevoda. Iako težimo točnosti, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne snosimo odgovornost za nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.