# **在 Android 上推理 Phi-3**

讓我們來看看如何在 Android 設備上使用 Phi-3-mini 進行推理。Phi-3-mini 是 Microsoft 推出的新系列模型，能夠讓大型語言模型 (LLMs) 部署在邊緣設備和物聯網設備上。

## Semantic Kernel 與推理

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) 是一個應用框架，允許您創建與 Azure OpenAI Service、OpenAI 模型甚至本地模型兼容的應用。如果您是 Semantic Kernel 的新手，我們建議您參考 [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。

### 使用 Semantic Kernel 訪問 Phi-3-mini

您可以將其與 Semantic Kernel 中的 Hugging Face Connector 結合使用。請參考這個 [範例代碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)。

預設情況下，它對應於 Hugging Face 上的模型 ID。不過，您也可以連接到本地構建的 Phi-3-mini 模型伺服器。

### 使用 Ollama 或 LlamaEdge 調用量化模型

許多用戶更喜歡使用量化模型來本地運行模型。[Ollama](https://ollama.com/) 和 [LlamaEdge](https://llamaedge.com) 允許個人用戶調用不同的量化模型：

#### Ollama

您可以直接運行 `ollama run Phi-3`，或者通過創建 `Modelfile` 並指定 `.gguf` 文件的路徑來離線配置。

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[範例代碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

如果您希望同時在雲端和邊緣設備上使用 `.gguf` 文件，LlamaEdge 是一個不錯的選擇。您可以參考這個 [範例代碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) 開始使用。

### 在 Android 手機上安裝與運行

1. **下載 MLC Chat 應用程式**（免費）適用於 Android 手機。
2. 下載 APK 文件（148MB），並安裝到您的設備上。
3. 啟動 MLC Chat 應用程式。您將看到一個 AI 模型列表，包括 Phi-3-mini。

總而言之，Phi-3-mini 為邊緣設備上的生成式 AI 開啟了令人興奮的可能性，您可以開始在 Android 上探索其功能。

**免責聲明**：  
本文檔使用基於機器的人工智能翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀不承擔責任。