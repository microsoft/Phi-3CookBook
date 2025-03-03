# **Quantizarea Familiei Phi folosind llama.cpp**

## **Ce este llama.cpp**

llama.cpp este o bibliotecă software open-source scrisă în principal în C++ care realizează inferență pe diverse modele de limbaj de mari dimensiuni (LLMs), cum ar fi Llama. Scopul principal al acesteia este de a oferi performanțe de ultimă generație pentru inferența LLM pe o gamă largă de hardware, cu o configurare minimă. În plus, există și legături pentru Python disponibile pentru această bibliotecă, care oferă o API de nivel înalt pentru completarea textului și un server web compatibil cu OpenAI.

Obiectivul principal al llama.cpp este de a permite inferența LLM cu o configurare minimă și performanțe de ultimă generație pe o varietate mare de hardware - local și în cloud.

- Implementare simplă în C/C++ fără dependențe
- Siliconul Apple este un cetățean de primă clasă - optimizat prin ARM NEON, Accelerate și framework-urile Metal
- Suport AVX, AVX2 și AVX512 pentru arhitecturi x86
- Cuantizare pe 1,5 biți, 2 biți, 3 biți, 4 biți, 5 biți, 6 biți și 8 biți pentru inferență mai rapidă și utilizare redusă a memoriei
- Kernel-uri CUDA personalizate pentru rularea LLM-urilor pe GPU-uri NVIDIA (suport pentru GPU-uri AMD prin HIP)
- Suport pentru backend Vulkan și SYCL
- Inferență hibridă CPU+GPU pentru a accelera parțial modelele mai mari decât capacitatea totală a memoriei VRAM

## **Cuantizarea Phi-3.5 cu llama.cpp**

Modelul Phi-3.5-Instruct poate fi cuantizat folosind llama.cpp, însă Phi-3.5-Vision și Phi-3.5-MoE nu sunt încă suportate. Formatul convertit de llama.cpp este gguf, care este de asemenea cel mai utilizat format de cuantizare.

Există un număr mare de modele în format GGUF cuantizate pe Hugging Face. AI Foundry, Ollama și LlamaEdge se bazează pe llama.cpp, așa că modelele GGUF sunt de asemenea frecvent utilizate.

### **Ce este GGUF**

GGUF este un format binar optimizat pentru încărcarea și salvarea rapidă a modelelor, ceea ce îl face extrem de eficient pentru inferență. GGUF este proiectat pentru utilizare cu GGML și alți executori. GGUF a fost dezvoltat de @ggerganov, care este și dezvoltatorul llama.cpp, un framework popular de inferență LLM în C/C++. Modelele dezvoltate inițial în framework-uri precum PyTorch pot fi convertite în format GGUF pentru utilizare cu aceste motoare.

### **ONNX vs GGUF**

ONNX este un format tradițional pentru învățare automată/profundă, bine suportat în diferite framework-uri AI și cu scenarii bune de utilizare pe dispozitive edge. În ceea ce privește GGUF, acesta este bazat pe llama.cpp și poate fi considerat produs al erei GenAI. Cele două au utilizări similare. Dacă doriți performanțe mai bune pe hardware încorporat și în straturile aplicațiilor, ONNX poate fi alegerea dvs. Dacă utilizați framework-ul derivat și tehnologia llama.cpp, atunci GGUF ar putea fi mai potrivit.

### **Cuantizarea Phi-3.5-Instruct folosind llama.cpp**

**1. Configurarea mediului**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Cuantizare**

Folosind llama.cpp pentru a converti Phi-3.5-Instruct în GGUF FP16


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Cuantizarea Phi-3.5 la INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testare**

Instalarea llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Notă*** 

Dacă utilizați Siliconul Apple, instalați llama-cpp-python astfel


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testare 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Resurse**

1. Aflați mai multe despre llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Aflați mai multe despre GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Declinări de responsabilitate**:  
Acest document a fost tradus utilizând servicii de traducere bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot rezulta din utilizarea acestei traduceri.