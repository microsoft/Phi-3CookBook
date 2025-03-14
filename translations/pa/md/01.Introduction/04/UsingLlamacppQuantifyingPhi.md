# **llama.cpp ਦੀ ਵਰਤੋਂ ਨਾਲ Phi ਪਰਿਵਾਰ ਨੂੰ ਕਵਾਂਟਾਈਜ਼ ਕਰਨਾ**

## **llama.cpp ਕੀ ਹੈ**

llama.cpp ਇੱਕ ਖੁੱਲ੍ਹਾ ਸਰੋਤ ਸੌਫਟਵੇਅਰ ਲਾਇਬ੍ਰੇਰੀ ਹੈ, ਜੋ ਮੁੱਖ ਤੌਰ 'ਤੇ C++ ਵਿੱਚ ਲਿਖੀ ਗਈ ਹੈ। ਇਹ ਵੱਖ-ਵੱਖ ਵੱਡੇ ਭਾਸ਼ਾ ਮਾਡਲਾਂ (LLMs), ਜਿਵੇਂ ਕਿ Llama, 'ਤੇ ਅਨੁਮਾਨ ਲਗਾਉਂਦੀ ਹੈ। ਇਸ ਦਾ ਮੁੱਖ ਉਦੇਸ਼ ਘੱਟ ਸੈਟਅੱਪ ਨਾਲ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ 'ਤੇ ਅਨੁਮਾਨ ਲਈ ਰਾਜ-ਅਧੁਨਿਕ ਪ੍ਰਦਰਸ਼ਨ ਪ੍ਰਦਾਨ ਕਰਨਾ ਹੈ। ਇਸ ਲਾਇਬ੍ਰੇਰੀ ਲਈ ਪਾਇਥਨ ਬਾਈਂਡਿੰਗ ਵੀ ਉਪਲਬਧ ਹਨ, ਜੋ ਟੈਕਸਟ ਪੂਰਨਤਾ ਲਈ ਇੱਕ ਉੱਚ-ਸਤ੍ਹਾ API ਅਤੇ OpenAI ਅਨੁਕੂਲ ਵੈੱਬ ਸਰਵਰ ਪ੍ਰਦਾਨ ਕਰਦੀਆਂ ਹਨ।

llama.cpp ਦਾ ਮੁੱਖ ਉਦੇਸ਼ ਘੱਟ ਸੈਟਅੱਪ ਨਾਲ ਅਤੇ ਵੱਖ-ਵੱਖ ਹਾਰਡਵੇਅਰ 'ਤੇ ਰਾਜ-ਅਧੁਨਿਕ ਪ੍ਰਦਰਸ਼ਨ ਨਾਲ LLM ਅਨੁਮਾਨ ਸਹੂਲਤਮੰਦ ਬਣਾਉਣਾ ਹੈ - ਸਥਾਨਕ ਤੌਰ 'ਤੇ ਅਤੇ ਕਲਾਉਡ ਵਿੱਚ।

- ਬਿਨਾਂ ਕਿਸੇ ਡਿਪੈਂਡੇੰਸੀ ਦੇ ਸਾਫ਼ C/C++ ਇੰਪਲੀਮੈਂਟੇਸ਼ਨ  
- ਐਪਲ ਸਿਲਿਕਾਨ ਨੂੰ ਪਹਿਲੀ ਤਰਜੀਹ ਦਿੱਤੀ ਗਈ ਹੈ - ARM NEON, Accelerate ਅਤੇ Metal ਫਰੇਮਵਰਕ ਦੁਆਰਾ ਅਨੁਕੂਲਿਤ  
- x86 ਆਰਕੀਟੈਕਚਰ ਲਈ AVX, AVX2 ਅਤੇ AVX512 ਸਹਾਇਤਾ  
- ਤੇਜ਼ ਅਨੁਮਾਨ ਅਤੇ ਘੱਟ ਮੈਮੋਰੀ ਖਪਤ ਲਈ 1.5-ਬਿੱਟ, 2-ਬਿੱਟ, 3-ਬਿੱਟ, 4-ਬਿੱਟ, 5-ਬਿੱਟ, 6-ਬਿੱਟ, ਅਤੇ 8-ਬਿੱਟ ਇੰਟਿਜਰ ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ  
- NVIDIA GPUs 'ਤੇ LLM ਚਲਾਉਣ ਲਈ ਕਸਟਮ CUDA ਕਰਨਲ (HIP ਰਾਹੀਂ AMD GPUs ਲਈ ਸਹਾਇਤਾ)  
- Vulkan ਅਤੇ SYCL ਬੈਕਐਂਡ ਸਹਾਇਤਾ  
- ਮਾਡਲਾਂ ਨੂੰ ਗਤੀਸ਼ੀਲ ਕਰਨ ਲਈ CPU+GPU ਹਾਈਬ੍ਰਿਡ ਅਨੁਮਾਨ ਜੋ ਕੁੱਲ VRAM ਸਮਰੱਥਾ ਤੋਂ ਵੱਧ ਵੱਡੇ ਹਨ  

## **llama.cpp ਨਾਲ Phi-3.5 ਨੂੰ ਕਵਾਂਟਾਈਜ਼ ਕਰਨਾ**

Phi-3.5-Instruct ਮਾਡਲ ਨੂੰ llama.cpp ਦੀ ਵਰਤੋਂ ਨਾਲ ਕਵਾਂਟਾਈਜ਼ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ, ਪਰ Phi-3.5-Vision ਅਤੇ Phi-3.5-MoE ਅਜੇ ਤੱਕ ਸਹਾਇਤਾਪ੍ਰਾਪਤ ਨਹੀਂ ਹਨ। llama.cpp ਦੁਆਰਾ ਰੂਪਾਂਤਰਤ ਫਾਰਮੈਟ gguf ਹੈ, ਜੋ ਸਭ ਤੋਂ ਵੱਧ ਵਰਤਿਆ ਜਾਣ ਵਾਲਾ ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ ਫਾਰਮੈਟ ਵੀ ਹੈ।

Hugging Face 'ਤੇ gguf ਫਾਰਮੈਟ ਦੇ ਬਹੁਤ ਸਾਰੇ ਕਵਾਂਟਾਈਜ਼ ਮਾਡਲ ਉਪਲਬਧ ਹਨ। AI Foundry, Ollama, ਅਤੇ LlamaEdge llama.cpp 'ਤੇ ਨਿਰਭਰ ਕਰਦੇ ਹਨ, ਇਸ ਲਈ gguf ਮਾਡਲ ਵੀ ਅਕਸਰ ਵਰਤੇ ਜਾਂਦੇ ਹਨ।

### **GGUF ਕੀ ਹੈ**

GGUF ਇੱਕ ਬਾਈਨਰੀ ਫਾਰਮੈਟ ਹੈ ਜੋ ਮਾਡਲਾਂ ਨੂੰ ਤੇਜ਼ੀ ਨਾਲ ਲੋਡ ਅਤੇ ਸੇਵ ਕਰਨ ਲਈ ਅਨੁਕੂਲਿਤ ਹੈ, ਜਿਸ ਕਰਕੇ ਇਹ ਅਨੁਮਾਨ ਲਈ ਬਹੁਤ ਪ੍ਰਭਾਵਸ਼ਾਲੀ ਹੈ। GGUF ਨੂੰ GGML ਅਤੇ ਹੋਰ ਐਗਜ਼ਿਕਿਊਟਰਾਂ ਨਾਲ ਵਰਤਣ ਲਈ ਡਿਜ਼ਾਈਨ ਕੀਤਾ ਗਿਆ ਹੈ। GGUF ਨੂੰ @ggerganov ਨੇ ਵਿਕਸਿਤ ਕੀਤਾ ਹੈ, ਜੋ llama.cpp ਦੇ ਡਿਵੈਲਪਰ ਵੀ ਹਨ, ਜੋ ਇੱਕ ਪ੍ਰਸਿੱਧ C/C++ LLM ਅਨੁਮਾਨ ਫਰੇਮਵਰਕ ਹੈ। ਜਿਹੜੇ ਮਾਡਲ ਸ਼ੁਰੂਆਤ ਵਿੱਚ PyTorch ਵਰਗੇ ਫਰੇਮਵਰਕ ਵਿੱਚ ਵਿਕਸਿਤ ਕੀਤੇ ਗਏ ਹਨ, ਉਹਨਾਂ ਨੂੰ GGUF ਫਾਰਮੈਟ ਵਿੱਚ ਰੂਪਾਂਤਰਤ ਕੀਤਾ ਜਾ ਸਕਦਾ ਹੈ।

### **ONNX ਵਸ GGUF**

ONNX ਇੱਕ ਪਰੰਪਰਾਗਤ ਮਸ਼ੀਨ ਲਰਨਿੰਗ/ਡੀਪ ਲਰਨਿੰਗ ਫਾਰਮੈਟ ਹੈ, ਜੋ ਵੱਖ-ਵੱਖ AI ਫਰੇਮਵਰਕ ਵਿੱਚ ਚੰਗੀ ਸਹਾਇਤਾ ਪ੍ਰਦਾਨ ਕਰਦਾ ਹੈ ਅਤੇ ਐਜ ਡਿਵਾਈਸਾਂ ਵਿੱਚ ਚੰਗੇ ਵਰਤੋਂਕੇਸਾਂ ਲਈ ਜਾਣਿਆ ਜਾਂਦਾ ਹੈ। GGUF, llama.cpp ਦੇ ਆਧਾਰ 'ਤੇ ਹੈ ਅਤੇ ਇਸਨੂੰ GenAI ਯੁੱਗ ਵਿੱਚ ਤਿਆਰ ਕੀਤਾ ਗਿਆ ਹੈ। ਦੋਵੇਂ ਦੇ ਸਮਾਨ ਉਦੇਸ਼ ਹਨ। ਜੇਕਰ ਤੁਸੀਂ ਐਂਬੈਡਿਡ ਹਾਰਡਵੇਅਰ ਅਤੇ ਐਪਲੀਕੇਸ਼ਨ ਲੇਅਰ ਵਿੱਚ ਵਧੀਆ ਪ੍ਰਦਰਸ਼ਨ ਚਾਹੁੰਦੇ ਹੋ, ਤਾਂ ONNX ਤੁਹਾਡੀ ਚੋਣ ਹੋ ਸਕਦੀ ਹੈ। ਜੇਕਰ ਤੁਸੀਂ llama.cpp ਦੇ ਡਿਰਿਵੇਟਿਵ ਫਰੇਮਵਰਕ ਅਤੇ ਤਕਨਾਲੋਜੀ ਦੀ ਵਰਤੋਂ ਕਰਦੇ ਹੋ, ਤਾਂ GGUF ਬਿਹਤਰ ਹੋ ਸਕਦਾ ਹੈ।

### **llama.cpp ਦੀ ਵਰਤੋਂ ਨਾਲ Phi-3.5-Instruct ਨੂੰ ਕਵਾਂਟਾਈਜ਼ ਕਰਨਾ**

**1. ਮਾਹੌਲ ਸੰਰਚਨਾ**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. ਕਵਾਂਟਾਈਜ਼ੇਸ਼ਨ**

llama.cpp ਦੀ ਵਰਤੋਂ ਕਰਕੇ Phi-3.5-Instruct ਨੂੰ FP16 GGUF ਵਿੱਚ ਰੂਪਾਂਤਰਤ ਕਰਨਾ  


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Phi-3.5 ਨੂੰ INT4 ਵਿੱਚ ਕਵਾਂਟਾਈਜ਼ ਕਰਨਾ  


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. ਟੈਸਟਿੰਗ**

llama-cpp-python ਇੰਸਟਾਲ ਕਰੋ  


```bash

pip install llama-cpp-python -U

```

***ਨੋਟ***  

ਜੇਕਰ ਤੁਸੀਂ Apple Silicon ਵਰਤਦੇ ਹੋ, ਤਾਂ ਕਿਰਪਾ ਕਰਕੇ llama-cpp-python ਨੂੰ ਇਸ ਤਰ੍ਹਾਂ ਇੰਸਟਾਲ ਕਰੋ  


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

ਟੈਸਟਿੰਗ  


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **ਸਰੋਤ**

1. llama.cpp ਬਾਰੇ ਹੋਰ ਜਾਣੋ [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. GGUF ਬਾਰੇ ਹੋਰ ਜਾਣੋ [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**ਅਸਵੀਕਰਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਮਸ਼ੀਨ ਅਧਾਰਿਤ AI ਅਨੁਵਾਦ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਅਸੀਂ ਸਹੀ ਹੋਣ ਦੀ ਪੂਰੀ ਕੋਸ਼ਿਸ਼ ਕਰਦੇ ਹਾਂ, ਪਰ ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚਿੱਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਇਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਅਸੀਂ ਇਸ ਅਨੁਵਾਦ ਦੇ ਇਸਤੇਮਾਲ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤ ਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।