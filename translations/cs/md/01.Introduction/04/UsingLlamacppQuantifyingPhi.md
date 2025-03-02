# **Kvantizace rodiny Phi pomocí llama.cpp**

## **Co je llama.cpp**

llama.cpp je open-source knihovna napsaná primárně v jazyce C++, která umožňuje inferenci na různých modelech velkých jazykových modelů (LLMs), jako je Llama. Jejím hlavním cílem je poskytovat špičkový výkon pro inferenci LLM na široké škále hardwaru s minimálními požadavky na nastavení. Tato knihovna také nabízí Pythonové vazby, které poskytují high-level API pro doplňování textu a webový server kompatibilní s OpenAI.

Hlavním cílem llama.cpp je umožnit inferenci LLM s minimálním nastavením a špičkovým výkonem na různých hardwarových platformách – lokálně i v cloudu.

- Implementace v čistém C/C++ bez jakýchkoliv závislostí
- Apple Silicon je plně podporován – optimalizace pomocí ARM NEON, Accelerate a Metal frameworků
- Podpora AVX, AVX2 a AVX512 pro x86 architektury
- Kvantizace na 1,5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit a 8-bit pro rychlejší inferenci a snížení paměťové náročnosti
- Vlastní CUDA jádra pro provoz LLM na NVIDIA GPU (podpora AMD GPU přes HIP)
- Podpora backendů Vulkan a SYCL
- Hybridní CPU+GPU inference pro částečné zrychlení modelů větších než celková kapacita VRAM

## **Kvantizace Phi-3.5 pomocí llama.cpp**

Model Phi-3.5-Instruct lze kvantizovat pomocí llama.cpp, ale modely Phi-3.5-Vision a Phi-3.5-MoE zatím nejsou podporovány. Formát, který llama.cpp převádí, je gguf, což je také nejrozšířenější formát kvantizace.

Na Hugging Face je k dispozici velké množství modelů ve formátu GGUF. AI Foundry, Ollama a LlamaEdge spoléhají na llama.cpp, takže GGUF modely jsou často používány.

### **Co je GGUF**

GGUF je binární formát optimalizovaný pro rychlé načítání a ukládání modelů, což ho činí vysoce efektivním pro účely inference. GGUF je navržen pro použití s GGML a dalšími exekutory. GGUF byl vyvinut @ggerganovem, který je také autorem llama.cpp, populárního inference frameworku pro LLM napsaného v jazyce C/C++. Modely původně vytvořené v rámci jako PyTorch lze převést do formátu GGUF pro použití s těmito enginy.

### **ONNX vs GGUF**

ONNX je tradiční formát pro strojové učení a hluboké učení, který je dobře podporován v různých AI rámcích a má široké možnosti využití na edge zařízeních. Na druhou stranu GGUF je založen na llama.cpp a lze ho označit za produkt éry GenAI. Oba mají podobné způsoby použití. Pokud hledáte lepší výkon na embedded hardwaru a v aplikačních vrstvách, ONNX může být vhodnější volbou. Pokud však používáte framework a technologie odvozené z llama.cpp, GGUF může být lepší variantou.

### **Kvantizace Phi-3.5-Instruct pomocí llama.cpp**

**1. Konfigurace prostředí**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantizace**

Pomocí llama.cpp převést Phi-3.5-Instruct na FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Kvantizace Phi-3.5 na INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testování**

Nainstalovat llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Poznámka*** 

Pokud používáte Apple Silicon, nainstalujte llama-cpp-python tímto způsobem


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testování 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Zdroje**

1. Více o llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Více o GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Prohlášení**:  
Tento dokument byl přeložen pomocí strojových překladových služeb založených na umělé inteligenci. I když se snažíme o přesnost, vezměte prosím na vědomí, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nenese zodpovědnost za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.