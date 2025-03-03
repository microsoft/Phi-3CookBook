# **在 Nvidia Jetson 上推理 Phi-3**

Nvidia Jetson 是 Nvidia 推出的嵌入式計算板系列。Jetson TK1、TX1 和 TX2 型號均搭載 Nvidia 的 Tegra 處理器（或 SoC），整合了基於 ARM 架構的中央處理單元（CPU）。Jetson 是一個低功耗系統，專為加速機器學習應用而設計。Nvidia Jetson 被專業開發者用於創造各行業的突破性 AI 產品，也被學生和愛好者用於實踐 AI 學習和創建令人驚嘆的項目。SLM 部署在像 Jetson 這樣的邊緣設備上，將實現更好的工業生成式 AI 應用場景。

## 在 NVIDIA Jetson 上的部署：
從事自主機器人和嵌入式設備的開發者可以利用 Phi-3 Mini。Phi-3 的相對小尺寸使其非常適合邊緣部署。在訓練過程中參數經過精心調整，確保了響應的高準確性。

### TensorRT-LLM 優化：
NVIDIA 的 [TensorRT-LLM 函式庫](https://github.com/NVIDIA/TensorRT-LLM?WT.mc_id=aiml-138114-kinfeylo) 可優化大型語言模型的推理。它支持 Phi-3 Mini 的長上下文窗口，提升了吞吐量和延遲表現。優化技術包括 LongRoPE、FP8 和流批處理（inflight batching）。

### 可用性與部署：
開發者可以在 [NVIDIA's AI](https://www.nvidia.com/en-us/ai-data-science/generative-ai/) 上探索具備 128K 上下文窗口的 Phi-3 Mini。它以 NVIDIA NIM 形式封裝，這是一個具有標準 API 的微服務，可以部署到任何地方。此外，[GitHub 上的 TensorRT-LLM 實現](https://github.com/NVIDIA/TensorRT-LLM)也提供了相關資源。

## **1. 準備工作**

a. Jetson Orin NX / Jetson NX

b. JetPack 5.1.2+
   
c. Cuda 11.8
   
d. Python 3.8+

## **2. 在 Jetson 上運行 Phi-3**

我們可以選擇 [Ollama](https://ollama.com) 或 [LlamaEdge](https://llamaedge.com)。

如果您希望同時在雲端和邊緣設備上使用 gguf，LlamaEdge 可以被理解為 WasmEdge（WasmEdge 是一個輕量級、高性能、可擴展的 WebAssembly 執行環境，適用於雲原生、邊緣和去中心化應用。它支持無伺服器應用、嵌入式函數、微服務、智能合約和物聯網設備。您可以通過 LlamaEdge 將 gguf 的量化模型部署到邊緣設備和雲端）。

![llamaedge](../../../../../translated_images/llamaedge.1356a35c809c5e9d89d8168db0c92161e87f5e2c34831f2fad800f00fc4e74dc.tw.jpg)

以下是使用步驟：

1. 安裝並下載相關庫和文件

```bash

curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- --plugin wasi_nn-ggml

curl -LO https://github.com/LlamaEdge/LlamaEdge/releases/latest/download/llama-api-server.wasm

curl -LO https://github.com/LlamaEdge/chatbot-ui/releases/latest/download/chatbot-ui.tar.gz

tar xzf chatbot-ui.tar.gz

```

**注意**: llama-api-server.wasm 和 chatbot-ui 需要在同一目錄下。

2. 在終端運行腳本

```bash

wasmedge --dir .:. --nn-preload default:GGML:AUTO:{Your gguf path} llama-api-server.wasm -p phi-3-chat

```

以下是運行結果：

![llamaedgerun](../../../../../translated_images/llamaedgerun.66eb2acd7f14e814437879522158b9531ae7c955014d48d0708d0e4ce6ac94a6.tw.png)

***示例代碼*** [Phi-3 mini WASM Notebook Sample](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm)

總之，Phi-3 Mini 在語言建模領域實現了一次飛躍，結合了效率、上下文感知以及 NVIDIA 的優化能力。無論您是在構建機器人還是邊緣應用，Phi-3 Mini 都是一個值得關注的強大工具。

**免責聲明**：  
本文件是使用基於機器的人工智能翻譯服務進行翻譯的。雖然我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用本翻譯而引起的任何誤解或誤讀不承擔責任。