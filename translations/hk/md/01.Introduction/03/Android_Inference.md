# **在 Android 上進行 Phi-3 推理**

讓我們一起探索如何在 Android 設備上使用 Phi-3-mini 進行推理。Phi-3-mini 是 Microsoft 推出的新系列模型，能夠在邊緣設備和物聯網設備上部署大型語言模型 (LLMs)。

## Semantic Kernel 與推理

[Semantic Kernel](https://github.com/microsoft/semantic-kernel) 是一個應用框架，讓你能夠建立與 Azure OpenAI Service、OpenAI 模型，甚至本地模型兼容的應用。如果你是 Semantic Kernel 的新手，我們建議你參考 [Semantic Kernel Cookbook](https://github.com/microsoft/SemanticKernelCookBook?WT.mc_id=aiml-138114-kinfeylo)。

### 使用 Semantic Kernel 訪問 Phi-3-mini

你可以將其與 Semantic Kernel 的 Hugging Face Connector 結合使用。參考這段 [範例代碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/semantickernel?WT.mc_id=aiml-138114-kinfeylo)。

默認情況下，它對應於 Hugging Face 上的模型 ID。不過，你也可以連接到本地構建的 Phi-3-mini 模型服務器。

### 使用 Ollama 或 LlamaEdge 調用量化模型

許多用戶更喜歡使用量化模型在本地運行模型。[Ollama](https://ollama.com/) 和 [LlamaEdge](https://llamaedge.com) 允許個人用戶調用不同的量化模型：

#### Ollama

你可以直接運行 `ollama run Phi-3`，或者通過創建一個包含 `.gguf` 文件路徑的 `Modelfile` 進行離線配置。

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

[範例代碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ollama?WT.mc_id=aiml-138114-kinfeylo)

#### LlamaEdge

如果你希望同時在雲端和邊緣設備上使用 `.gguf` 文件，LlamaEdge 是一個不錯的選擇。你可以參考這段 [範例代碼](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/wasm?WT.mc_id=aiml-138114-kinfeylo) 開始使用。

### 在 Android 手機上安裝與運行

1. **下載 MLC Chat 應用**（免費）適用於 Android 手機。
2. 下載 APK 文件（148MB），並安裝到你的設備上。
3. 啟動 MLC Chat 應用。你會看到一個包含 Phi-3-mini 在內的 AI 模型列表。

總結來說，Phi-3-mini 為邊緣設備上的生成式 AI 開啟了令人興奮的可能性，你可以在 Android 設備上開始探索它的功能。

**免責聲明**:  
本文件是使用機器翻譯AI服務進行翻譯的。我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文檔的母語版本作為權威來源。對於關鍵資訊，建議使用專業的人手翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。