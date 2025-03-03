# **Phi család kvantálása a llama.cpp segítségével**

## **Mi az a llama.cpp?**

A llama.cpp egy nyílt forráskódú szoftverkönyvtár, amely elsősorban C++ nyelven íródott, és különböző nagy nyelvi modellek (LLM-ek), például a Llama inferenciáját végzi. Fő célja, hogy csúcsteljesítményt nyújtson LLM inferenciában széleskörű hardvereken, minimális beállítással. Ezenkívül Python kötéseket is kínál, amelyek magas szintű API-t biztosítanak szövegkiegészítéshez és egy OpenAI-kompatibilis webszerverhez.

A llama.cpp fő célja, hogy minimális beállítással és csúcsteljesítménnyel tegye lehetővé az LLM inferenciát különböző hardvereken - helyben és a felhőben is.

- Egyszerű C/C++ implementáció függőségek nélkül
- Az Apple silicon elsődleges támogatást élvez - optimalizálva ARM NEON, Accelerate és Metal keretrendszerekkel
- AVX, AVX2 és AVX512 támogatás x86 architektúrákhoz
- 1,5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit és 8-bit integer kvantálás a gyorsabb inferencia és csökkentett memóriahasználat érdekében
- Egyedi CUDA kernel az LLM-ek futtatásához NVIDIA GPU-kon (AMD GPU támogatás HIP-en keresztül)
- Vulkan és SYCL háttértámogatás
- CPU+GPU hibrid inferencia a teljes VRAM kapacitásnál nagyobb modellek részleges gyorsításához

## **Phi-3.5 kvantálása a llama.cpp segítségével**

A Phi-3.5-Instruct modellt kvantálni lehet a llama.cpp segítségével, de a Phi-3.5-Vision és a Phi-3.5-MoE egyelőre nem támogatott. A llama.cpp által átalakított formátum a GGUF, amely egyben a legszélesebb körben használt kvantálási formátum is.

Számos kvantált GGUF formátumú modell található a Hugging Face-en. Az AI Foundry, Ollama és LlamaEdge a llama.cpp-re támaszkodik, így a GGUF modellek gyakran használtak.

### **Mi az a GGUF?**

A GGUF egy bináris formátum, amelyet a modellek gyors betöltésére és mentésére optimalizáltak, így rendkívül hatékony az inferenciában. A GGUF-et a GGML és más végrehajtók használatára tervezték. A GGUF-et @ggerganov fejlesztette, aki egyben a llama.cpp, egy népszerű C/C++ LLM inferenciakeret fejlesztője is. Az olyan keretrendszerekben, mint a PyTorch fejlesztett modellek átalakíthatók GGUF formátumba ezen motorokkal való használatra.

### **ONNX vs GGUF**

Az ONNX egy hagyományos gépi tanulási/mélytanulási formátum, amelyet jól támogatnak különböző AI keretrendszerek, és jó használati forgatókönyvei vannak élkészülékeken. A GGUF ezzel szemben a llama.cpp-n alapul, és mondhatjuk, hogy a generatív mesterséges intelligencia korszakában jött létre. A kettő hasonló célokra használható. Ha jobb teljesítményt szeretnél beágyazott hardveren és alkalmazási rétegeken, az ONNX lehet a választásod. Ha a llama.cpp származékos keretrendszerét és technológiáját használod, akkor a GGUF lehet előnyösebb.

### **Phi-3.5-Instruct kvantálása a llama.cpp segítségével**

**1. Környezet beállítása**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Kvantálás**

A Phi-3.5-Instruct átalakítása FP16 GGUF formátumba a llama.cpp segítségével


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5 kvantálása INT4-re


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Tesztelés**

A llama-cpp-python telepítése


```bash

pip install llama-cpp-python -U

```

***Megjegyzés*** 

Ha Apple Silicon-t használsz, így telepítsd a llama-cpp-python-t


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Tesztelés 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Erőforrások**

1. Tudj meg többet a llama.cpp-ről: [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Tudj meg többet a GGUF-ről: [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítószolgáltatások segítségével került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget az ebből a fordításból eredő félreértésekért vagy téves értelmezésekért.