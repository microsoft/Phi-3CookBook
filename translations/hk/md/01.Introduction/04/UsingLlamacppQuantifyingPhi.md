# **使用 llama.cpp 量化 Phi 系列**

## **什麼是 llama.cpp**

llama.cpp 是一個主要用 C++ 編寫的開源軟件庫，用於在多種大型語言模型（LLMs）上進行推理，例如 Llama。其主要目標是以最少的設置，在廣泛的硬件上實現最先進的 LLM 推理性能。此外，該庫還提供了 Python 綁定，提供高層次的 API 用於文本補全以及與 OpenAI 相容的網絡服務器。

llama.cpp 的主要目標是以最少的設置，實現在多種硬件上（無論本地還是雲端）的最先進 LLM 推理性能。

- 純 C/C++ 實現，無需依賴其他庫
- Apple Silicon 是核心支持對象 - 通過 ARM NEON、Accelerate 和 Metal 框架進行優化
- 支持 x86 架構的 AVX、AVX2 和 AVX512
- 支持 1.5-bit、2-bit、3-bit、4-bit、5-bit、6-bit 和 8-bit 的整數量化，以實現更快的推理速度及更低的內存使用
- 自定義 CUDA 核心，用於在 NVIDIA GPU 上運行 LLM（支持通過 HIP 在 AMD GPU 上運行）
- 支持 Vulkan 和 SYCL 後端
- CPU+GPU 混合推理，部分加速超過 VRAM 容量的模型

## **使用 llama.cpp 量化 Phi-3.5**

Phi-3.5-Instruct 模型可以使用 llama.cpp 進行量化，但 Phi-3.5-Vision 和 Phi-3.5-MoE 尚不支持。llama.cpp 轉換後的格式為 GGUF，這也是目前最廣泛使用的量化格式。

在 Hugging Face 上有大量 GGUF 格式的量化模型。AI Foundry、Ollama 和 LlamaEdge 都依賴 llama.cpp，因此 GGUF 模型也經常被使用。

### **什麼是 GGUF**

GGUF 是一種二進制格式，專為快速加載和保存模型而優化，非常高效於推理用途。GGUF 是為 GGML 和其他執行器設計的格式。GGUF 是由 @ggerganov 開發的，他也是 llama.cpp（知名的 C/C++ LLM 推理框架）的開發者。最初用 PyTorch 等框架開發的模型可以轉換為 GGUF 格式，供這些引擎使用。

### **ONNX 與 GGUF 的比較**

ONNX 是一種傳統的機器學習/深度學習格式，得到了多種 AI 框架的良好支持，並且在邊緣設備中有不錯的應用場景。而 GGUF 則基於 llama.cpp，可以說是生成式 AI 時代的產物。兩者用途相似。如果你希望在嵌入式硬件和應用層中獲得更好的性能，ONNX 可能是你的選擇。如果你使用的是 llama.cpp 衍生的框架和技術，那麼 GGUF 可能會更合適。

### **使用 llama.cpp 量化 Phi-3.5-Instruct**

**1. 環境配置**


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

make -j8

```


**2. 量化**

使用 llama.cpp 將 Phi-3.5-Instruct 轉換為 FP16 GGUF


```bash

./convert_hf_to_gguf.py <Your Phi-3.5-Instruct Location> --outfile phi-3.5-128k-mini_fp16.gguf

```

將 Phi-3.5 量化為 INT4


```bash

./llama.cpp/llama-quantize <Your phi-3.5-128k-mini_fp16.gguf location> ./gguf/phi-3.5-128k-mini_Q4_K_M.gguf Q4_K_M

```


**3. 測試**

安裝 llama-cpp-python


```bash

pip install llama-cpp-python -U

```

***注意*** 

如果你使用的是 Apple Silicon，請這樣安裝 llama-cpp-python


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

測試 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **資源**

1. 瞭解更多關於 llama.cpp 的資訊 [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. 瞭解更多關於 GGUF 的資訊 [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**免責聲明**:  
本文件是使用機器翻譯人工智能服務進行翻譯的。我們致力於確保翻譯準確，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤讀概不負責。