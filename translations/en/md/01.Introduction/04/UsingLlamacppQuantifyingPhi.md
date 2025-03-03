# **Quantizing Phi Family using llama.cpp**

## **What's llama.cpp**

llama.cpp is an open-source software library primarily written in C++ that enables inference on various Large Language Models (LLMs), such as Llama. Its main objective is to deliver cutting-edge performance for LLM inference on a wide range of hardware with minimal configuration. Additionally, it provides Python bindings, which offer a high-level API for text completion and an OpenAI-compatible web server.

The primary goal of llama.cpp is to enable LLM inference with minimal configuration and top-notch performance on diverse hardware platforms, both locally and in the cloud.

- Pure C/C++ implementation with no external dependencies
- Apple silicon is fully supported, optimized with ARM NEON, Accelerate, and Metal frameworks
- AVX, AVX2, and AVX512 support for x86 architectures
- Integer quantization formats including 1.5-bit, 2-bit, 3-bit, 4-bit, 5-bit, 6-bit, and 8-bit for faster inference and reduced memory consumption
- Custom CUDA kernels for running LLMs on NVIDIA GPUs (AMD GPU support via HIP)
- Vulkan and SYCL backend support
- CPU+GPU hybrid inference to accelerate models larger than total VRAM capacity

## **Quantizing Phi-3.5 with llama.cpp**

The Phi-3.5-Instruct model can be quantized using llama.cpp, but Phi-3.5-Vision and Phi-3.5-MoE are not yet supported. The format converted by llama.cpp is GGUF, which is also the most widely adopted quantization format.

A large number of quantized GGUF format models are available on Hugging Face. Platforms like AI Foundry, Ollama, and LlamaEdge rely on llama.cpp, so GGUF models are frequently utilized.

### **What's GGUF**

GGUF is a binary format optimized for fast loading and saving of models, making it highly efficient for inference tasks. GGUF is designed to work with GGML and other executors. It was developed by @ggerganov, who is also the creator of llama.cpp, a widely used C/C++ LLM inference framework. Models originally developed in frameworks like PyTorch can be converted into GGUF format for use with these engines.

### **ONNX vs GGUF**

ONNX is a traditional machine learning/deep learning format, widely supported across various AI frameworks and suitable for many edge device scenarios. On the other hand, GGUF is based on llama.cpp and is tailored for the GenAI era. Both formats serve similar purposes. If you're aiming for optimal performance on embedded hardware and application layers, ONNX may be the better choice. However, if you're working with llama.cpp's derivative frameworks and technologies, GGUF might be more suitable.

### **Quantizing Phi-3.5-Instruct using llama.cpp**

**1. Environment Configuration**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. Quantization**

Convert Phi-3.5-Instruct to FP16 GGUF using llama.cpp


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

Quantize Phi-3.5 to INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. Testing**

Install llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***Note*** 

If you're using Apple Silicon, install llama-cpp-python like this


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

Testing 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **Resources**

1. Learn more about llama.cpp [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Learn more about GGUF [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.