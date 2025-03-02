# **Kvantizacija Phi porodice koristeći llama.cpp**

## **Šta je llama.cpp**

llama.cpp je open-source softverska biblioteka, prvenstveno napisana u C++, koja omogućava izvođenje inferencije na raznim modelima velikih jezika (LLMs), poput Llama. Glavni cilj joj je pružanje vrhunskih performansi za inferenciju LLM-a na širokom spektru hardvera uz minimalno podešavanje. Takođe, dostupne su Python biblioteke za ovu biblioteku, koje nude API visokog nivoa za završavanje teksta i veb server kompatibilan sa OpenAI.

Glavni cilj llama.cpp je omogućavanje inferencije LLM-a uz minimalno podešavanje i vrhunske performanse na različitim vrstama hardvera – lokalno i u oblaku.

- Implementacija u čistom C/C++ bez zavisnosti
- Apple silicon je prioritet – optimizovano putem ARM NEON, Accelerate i Metal framework-ova
- Podrška za AVX, AVX2 i AVX512 za x86 arhitekture
- Kvantizacija celih brojeva od 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit i 8-bit za bržu inferenciju i smanjenu potrošnju memorije
- Prilagođeni CUDA kernel za pokretanje LLM-ova na NVIDIA GPU-ovima (podrška za AMD GPU-ove putem HIP-a)
- Vulkan i SYCL podrška za pozadinske procese
- Hibridna CPU+GPU inferencija za delimično ubrzanje modela većih od ukupnog kapaciteta VRAM-a

## **Kvantizacija Phi-3.5 sa llama.cpp**

Phi-3.5-Instruct model može se kvantizovati koristeći llama.cpp, ali Phi-3.5-Vision i Phi-3.5-MoE još nisu podržani. Format koji llama.cpp konvertuje je gguf, koji je ujedno i najčešće korišćen format za kvantizaciju.

Na Hugging Face platformi postoji veliki broj modela u kvantizovanom GGUF formatu. AI Foundry, Ollama i LlamaEdge oslanjaju se na llama.cpp, tako da se GGUF modeli često koriste.

### **Šta je GGUF**

GGUF je binarni format optimizovan za brzo učitavanje i čuvanje modela, što ga čini izuzetno efikasnim za inferenciju. GGUF je dizajniran za upotrebu sa GGML i drugim izvršnim okruženjima. GGUF je razvio @ggerganov, koji je takođe autor llama.cpp, popularnog C/C++ okvira za inferenciju LLM-ova. Modeli razvijeni u okvirima poput PyTorch-a mogu se konvertovati u GGUF format za upotrebu s ovim alatima.

### **ONNX vs GGUF**

ONNX je tradicionalni format za mašinsko učenje/duboko učenje, koji je dobro podržan u različitim AI okvirima i ima dobre primene na uređajima na ivici mreže. S druge strane, GGUF je baziran na llama.cpp i može se smatrati proizvodom GenAI ere. Ova dva formata imaju slične namene. Ako želite bolje performanse na ugrađenom hardveru i aplikacionim slojevima, ONNX može biti vaš izbor. Ako koristite izvedene okvire i tehnologiju llama.cpp, onda je GGUF možda bolji.

### **Kvantizacija Phi-3.5-Instruct koristeći llama.cpp**

**1. Konfiguracija okruženja**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantizacija**

Koristeći llama.cpp konvertujte Phi-3.5-Instruct u FP16 GGUF


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

Ako koristite Apple Silicon, instalirajte llama-cpp-python na sledeći način


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

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем машинских услуга за превођење базираних на вештачкој интелигенцији. Иако настојимо да превод буде тачан, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Не преузимамо одговорност за било каква погрешна тумачења или неразумевања која могу настати услед коришћења овог превода.