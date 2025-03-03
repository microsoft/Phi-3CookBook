# **Quantizzazione della famiglia Phi utilizzando llama.cpp**

## **Cos'è llama.cpp**

llama.cpp è una libreria software open-source scritta principalmente in C++ che esegue inferenze su vari modelli linguistici di grandi dimensioni (LLM), come Llama. Il suo obiettivo principale è fornire prestazioni all'avanguardia per l'inferenza di LLM su una vasta gamma di hardware con un setup minimo. Inoltre, sono disponibili binding Python per questa libreria, che offrono un'API di alto livello per il completamento di testi e un server web compatibile con OpenAI.

L'obiettivo principale di llama.cpp è abilitare l'inferenza LLM con un setup minimo e prestazioni all'avanguardia su una grande varietà di hardware, sia in locale che nel cloud.

- Implementazione in puro C/C++ senza dipendenze
- Apple Silicon è una piattaforma di prima classe - ottimizzata tramite ARM NEON, Accelerate e framework Metal
- Supporto AVX, AVX2 e AVX512 per architetture x86
- Quantizzazione intera a 1,5 bit, 2 bit, 3 bit, 4 bit, 5 bit, 6 bit e 8 bit per inferenze più veloci e uso ridotto della memoria
- Kernel CUDA personalizzati per eseguire LLM su GPU NVIDIA (supporto per GPU AMD tramite HIP)
- Supporto backend Vulkan e SYCL
- Inferenza ibrida CPU+GPU per accelerare parzialmente modelli più grandi della capacità totale della VRAM

## **Quantizzare Phi-3.5 con llama.cpp**

Il modello Phi-3.5-Instruct può essere quantizzato utilizzando llama.cpp, ma Phi-3.5-Vision e Phi-3.5-MoE non sono ancora supportati. Il formato convertito da llama.cpp è gguf, che è anche il formato di quantizzazione più ampiamente utilizzato.

Esistono un gran numero di modelli in formato GGUF quantizzati su Hugging Face. AI Foundry, Ollama e LlamaEdge si basano su llama.cpp, quindi i modelli GGUF sono spesso utilizzati.

### **Cos'è GGUF**

GGUF è un formato binario ottimizzato per il caricamento e il salvataggio rapido dei modelli, rendendolo altamente efficiente per scopi di inferenza. GGUF è progettato per essere utilizzato con GGML e altri esecutori. GGUF è stato sviluppato da @ggerganov, che è anche il creatore di llama.cpp, un popolare framework di inferenza LLM in C/C++. I modelli inizialmente sviluppati in framework come PyTorch possono essere convertiti in formato GGUF per essere utilizzati con questi motori.

### **ONNX vs GGUF**

ONNX è un formato tradizionale per machine learning/deep learning, ben supportato in diversi framework AI e con buoni scenari di utilizzo nei dispositivi edge. Per quanto riguarda GGUF, è basato su llama.cpp e può essere considerato un prodotto dell'era GenAI. I due hanno usi simili. Se desideri migliori prestazioni su hardware embedded e livelli applicativi, ONNX potrebbe essere la tua scelta. Se utilizzi il framework e la tecnologia derivati da llama.cpp, allora GGUF potrebbe essere più adatto.

### **Quantizzazione di Phi-3.5-Instruct utilizzando llama.cpp**

**1. Configurazione dell'ambiente**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Quantizzazione**

Utilizzo di llama.cpp per convertire Phi-3.5-Instruct in GGUF FP16


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Quantizzazione di Phi-3.5 in INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Test**

Installare llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Nota*** 

Se utilizzi Apple Silicon, installa llama-cpp-python in questo modo


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Test 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Risorse**

1. Per saperne di più su llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Per saperne di più su GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Disclaimer (Avvertenza)**:  
Questo documento è stato tradotto utilizzando servizi di traduzione automatica basati sull'intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.