# **使用 llama.cpp 量化 Phi 系列**

## **什麼是 llama.cpp**

llama.cpp 是一個主要用 C++ 編寫的開源軟體庫，用於執行多種大型語言模型（LLMs）的推理，例如 Llama。其主要目的是在各種硬體上，以最少的設置提供最先進的 LLM 推理性能。此外，該庫還提供了 Python 綁定，讓使用者可以透過高層級 API 完成文本生成，並且提供與 OpenAI 相容的網頁伺服器。

llama.cpp 的主要目標是實現 LLM 推理，並在本地和雲端的多種硬體上提供最先進的性能，同時保持簡單的設置。

- 純 C/C++ 實現，無需任何依賴
- Apple Silicon 是一等公民 - 通過 ARM NEON、Accelerate 和 Metal 框架進行優化
- 支援 x86 架構的 AVX、AVX2 和 AVX512
- 支援 1.5-bit、2-bit、3-bit、4-bit、5-bit、6-bit 和 8-bit 的整數量化，以加快推理速度並減少記憶體使用
- 提供自定義 CUDA 核心，用於在 NVIDIA GPU 上運行 LLM（支援通過 HIP 的 AMD GPU）
- 支援 Vulkan 和 SYCL 後端
- CPU+GPU 混合推理，用於部分加速超出 VRAM 總容量的模型

## **使用 llama.cpp 量化 Phi-3.5**

Phi-3.5-Instruct 模型可以通過 llama.cpp 進行量化，但 Phi-3.5-Vision 和 Phi-3.5-MoE 尚不支援。llama.cpp 轉換的格式為 GGUF，這也是目前最廣泛使用的量化格式。

Hugging Face 上有大量的 GGUF 格式量化模型。AI Foundry、Ollama 和 LlamaEdge 都依賴於 llama.cpp，因此 GGUF 模型也被廣泛使用。

### **什麼是 GGUF**

GGUF 是一種二進位格式，專為快速加載和保存模型而設計，非常適合推理用途。GGUF 是為 GGML 和其他執行器設計的。GGUF 是由 @ggerganov 開發的，他也是受歡迎的 C/C++ LLM 推理框架 llama.cpp 的開發者。最初在 PyTorch 等框架中開發的模型可以轉換為 GGUF 格式，以便與這些引擎一起使用。

### **ONNX vs GGUF**

ONNX 是一種傳統的機器學習/深度學習格式，受到不同 AI 框架的良好支援，在邊緣設備上有很好的應用場景。而 GGUF 基於 llama.cpp，可以說是生成式 AI 時代的產物。這兩者用途相似。如果您需要在嵌入式硬體和應用層中獲得更好的性能，ONNX 可能是您的選擇。如果您使用 llama.cpp 的衍生框架和技術，那麼 GGUF 可能更適合。

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

如果您使用的是 Apple Silicon，請這樣安裝 llama-cpp-python


```bash

CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python -U

```

測試 


```bash

llama.cpp/llama-cli --model <Your phi-3.5-128k-mini_Q4_K_M.gguf location> --prompt "<|user|>\nCan you introduce .NET<|end|>\n<|assistant|>\n"  --gpu-layers 10

```



## **資源**

1. 瞭解更多有關 llama.cpp 的資訊 [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. 瞭解更多有關 GGUF 的資訊 [https://huggingface.co/docs/hub/en/gguf](https://huggingface.co/docs/hub/en/gguf)

**免責聲明**：  
本文件使用基於機器的人工智能翻譯服務進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能會包含錯誤或不精確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解讀概不負責。