# **Kwantyzacja rodziny Phi za pomocą llama.cpp**

## **Czym jest llama.cpp**

llama.cpp to otwartoźródłowa biblioteka oprogramowania napisana głównie w C++, która umożliwia wnioskowanie na różnych dużych modelach językowych (LLM), takich jak Llama. Jej głównym celem jest zapewnienie najnowocześniejszej wydajności wnioskowania LLM na szerokiej gamie sprzętu przy minimalnej konfiguracji. Dodatkowo, dostępne są powiązania w Pythonie, które oferują wysokopoziomowe API do uzupełniania tekstu oraz serwer internetowy kompatybilny z OpenAI.

Głównym celem llama.cpp jest umożliwienie wnioskowania LLM przy minimalnej konfiguracji oraz osiągnięcie najnowocześniejszej wydajności na różnorodnym sprzęcie - lokalnie i w chmurze.

- Implementacja w czystym C/C++ bez żadnych zależności
- Apple silicon jako priorytet - zoptymalizowane za pomocą ARM NEON, Accelerate i Metal frameworks
- Obsługa AVX, AVX2 i AVX512 dla architektur x86
- Kwantyzacja liczb całkowitych 1,5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit i 8-bit dla szybszego wnioskowania i zmniejszonego zużycia pamięci
- Niestandardowe jądra CUDA do uruchamiania LLM na GPU NVIDIA (obsługa GPU AMD przez HIP)
- Obsługa backendu Vulkan i SYCL
- Hybrydowe wnioskowanie CPU+GPU w celu częściowego przyspieszenia modeli większych niż całkowita pojemność VRAM

## **Kwantyzacja Phi-3.5 za pomocą llama.cpp**

Model Phi-3.5-Instruct można kwantyzować za pomocą llama.cpp, ale Phi-3.5-Vision i Phi-3.5-MoE nie są jeszcze obsługiwane. Format konwertowany przez llama.cpp to GGUF, który jest również najczęściej używanym formatem kwantyzacji.

Na Hugging Face dostępna jest duża liczba modeli w skwantyzowanym formacie GGUF. AI Foundry, Ollama i LlamaEdge opierają się na llama.cpp, więc modele GGUF są również często wykorzystywane.

### **Czym jest GGUF**

GGUF to format binarny zoptymalizowany pod kątem szybkiego ładowania i zapisywania modeli, co czyni go bardzo wydajnym w zastosowaniach związanych z wnioskowaniem. GGUF został zaprojektowany do użycia z GGML i innymi wykonawcami. GGUF został opracowany przez @ggerganov, który jest również twórcą llama.cpp, popularnego frameworka wnioskowania LLM w C/C++. Modele pierwotnie opracowane w takich frameworkach jak PyTorch można konwertować do formatu GGUF w celu ich użycia z tymi silnikami.

### **ONNX vs GGUF**

ONNX to tradycyjny format uczenia maszynowego/głębokiego, który jest dobrze wspierany w różnych frameworkach AI i znajduje dobre zastosowanie w urządzeniach brzegowych. Z kolei GGUF opiera się na llama.cpp i można powiedzieć, że powstał w erze GenAI. Oba mają podobne zastosowania. Jeśli zależy Ci na lepszej wydajności na sprzęcie wbudowanym i w warstwach aplikacyjnych, ONNX może być lepszym wyborem. Jeśli korzystasz z frameworka i technologii pochodnych llama.cpp, GGUF może być bardziej odpowiedni.

### **Kwantyzacja Phi-3.5-Instruct za pomocą llama.cpp**

**1. Konfiguracja środowiska**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kwantyzacja**

Konwertowanie Phi-3.5-Instruct na FP16 GGUF za pomocą llama.cpp


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Kwantyzacja Phi-3.5 do INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testowanie**

Instalacja llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Uwaga*** 

Jeśli używasz Apple Silicon, zainstaluj llama-cpp-python w ten sposób


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testowanie


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Zasoby**

1. Dowiedz się więcej o llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Dowiedz się więcej o GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uważany za wiarygodne źródło. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.