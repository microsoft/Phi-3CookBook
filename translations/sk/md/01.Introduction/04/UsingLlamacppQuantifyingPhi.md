# **Kvantizácia Phi Family pomocou llama.cpp**

## **Čo je llama.cpp**

llama.cpp je open-source softvérová knižnica, napísaná primárne v jazyku C++, ktorá umožňuje inferenciu rôznych veľkých jazykových modelov (LLMs), ako je Llama. Jej hlavným cieľom je dosiahnuť špičkový výkon pre inferenciu LLM na širokej škále hardvéru s minimálnou potrebnou konfiguráciou. Navyše, táto knižnica obsahuje aj Pythonové rozhrania, ktoré poskytujú vysokoúrovňové API pre generovanie textu a webový server kompatibilný s OpenAI.

Hlavným cieľom llama.cpp je umožniť inferenciu LLM s minimálnou konfiguráciou a špičkovým výkonom na rôznorodom hardvéri - lokálne aj v cloude.

- Implementácia v čistom C/C++ bez závislostí
- Apple Silicon ako plnohodnotná platforma - optimalizovaná pomocou ARM NEON, Accelerate a Metal frameworkov
- Podpora AVX, AVX2 a AVX512 pre x86 architektúry
- Kvantizácia na 1,5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit a 8-bit celé čísla pre rýchlejšiu inferenciu a zníženie pamäťovej náročnosti
- Vlastné CUDA jadrá pre spúšťanie LLM na NVIDIA GPU (podpora pre AMD GPU cez HIP)
- Podpora Vulkan a SYCL backendov
- Hybridná inferencia CPU+GPU pre čiastočné zrýchlenie modelov väčších, ako je celková kapacita VRAM

## **Kvantizácia Phi-3.5 pomocou llama.cpp**

Model Phi-3.5-Instruct je možné kvantizovať pomocou llama.cpp, avšak modely Phi-3.5-Vision a Phi-3.5-MoE zatiaľ nie sú podporované. Formát konvertovaný pomocou llama.cpp je gguf, ktorý je zároveň najrozšírenejším formátom kvantizácie.

Na platforme Hugging Face je dostupné veľké množstvo modelov vo formáte GGUF. AI Foundry, Ollama a LlamaEdge sa spoliehajú na llama.cpp, a preto sa modely vo formáte GGUF často používajú.

### **Čo je GGUF**

GGUF je binárny formát optimalizovaný na rýchle načítanie a ukladanie modelov, vďaka čomu je vysoko efektívny na inferenciu. GGUF je navrhnutý na použitie s GGML a ďalšími vykonávacími nástrojmi. GGUF bol vyvinutý @ggerganov, ktorý je zároveň vývojárom llama.cpp, populárneho rámca pre inferenciu LLM v C/C++. Modely pôvodne vyvinuté vo frameworkoch ako PyTorch je možné konvertovať do formátu GGUF na použitie s týmito nástrojmi.

### **ONNX vs GGUF**

ONNX je tradičný formát pre strojové učenie/hĺbkové učenie, ktorý je dobre podporovaný v rôznych AI frameworkoch a má široké využitie na okrajových zariadeniach. GGUF je naopak založený na llama.cpp a možno ho považovať za produkt éry generatívnej AI. Obe majú podobné použitie. Ak chcete dosiahnuť lepší výkon na vstavanom hardvéri a aplikačných vrstvách, ONNX môže byť vhodnejšou voľbou. Ak však používate odvodené frameworky a technológie llama.cpp, GGUF môže byť lepšou alternatívou.

### **Kvantizácia Phi-3.5-Instruct pomocou llama.cpp**

**1. Nastavenie prostredia**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantizácia**

Použitie llama.cpp na konverziu Phi-3.5-Instruct do FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Kvantizácia Phi-3.5 do INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testovanie**

Inštalácia llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Poznámka*** 

Ak používate Apple Silicon, nainštalujte llama-cpp-python týmto spôsobom


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testovanie 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Zdroje**

1. Viac informácií o llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Viac informácií o GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových prekladateľských služieb AI. Hoci sa snažíme o presnosť, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.