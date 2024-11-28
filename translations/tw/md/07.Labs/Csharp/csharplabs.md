## 歡迎來到使用 C# 的 Phi-3 實驗室

這裡有一系列的實驗室展示如何在 .NET 環境中整合不同版本的 Phi-3 模型。

## 先決條件
在運行範例之前，請確保您已安裝以下內容：

**.NET 8:** 確保您的機器上已安裝[最新版本的 .NET](https://dotnet.microsoft.com/download/dotnet/8.0?WT.mc_id=aiml-137032-kinfeylo)。

**(可選) Visual Studio 或 Visual Studio Code:** 您需要一個能夠運行 .NET 專案的 IDE 或程式碼編輯器。我們推薦使用 [Visual Studio](https://visualstudio.microsoft.com/) 或 [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo)。

**使用 git** 從 [Hugging Face](https://huggingface.co) 本地克隆其中一個可用的 Phi-3 版本。

**下載 phi3-mini-4k-instruct-onnx 模型**到您的本地機器：

### 瀏覽到存放模型的資料夾
```bash
cd c:\phi3\models
```
### 添加 lfs 支持
```bash
git lfs install 
```
### 克隆並下載 mini 4K instruct 模型
```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx
```

### 克隆並下載 vision 128K 模型
```
git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```
**重要:** 目前的演示是設計來使用模型的 ONNX 版本。前面的步驟克隆了以下模型。

![OnnxDownload](../../../../../translated_images/DownloadOnnx.237f4b37d4d8d66d3f4a4a7219d6004bd6f84bc72cce50251ffc034cb28f6fb8.tw.png)

## 關於實驗室

主要解決方案有幾個範例實驗室，展示了使用 C# 的 Phi-3 模型的功能。

| 專案 | 描述 | 位置 |
| ------------ | ----------- | -------- |
| LabsPhi301    | 這是一個使用本地 phi3 模型來提問的範例專案。該專案使用 `Microsoft.ML.OnnxRuntime` libraries. | .\src\LabsPhi301\ |
| LabsPhi302    | This is a sample project that implement a Console chat using Semantic Kernel. | .\src\LabsPhi302\ |
| LabsPhi303 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. | .\src\LabsPhi303\ |
| LabsPhi304 | This is a sample project that uses a local phi3 vision model to analyze images.. The project load a local ONNX Phi-3 Vision model using the `Microsoft.ML.OnnxRuntime` libraries. The project also presents a menu with different options to interacti with the user. | .\src\LabsPhi304\ |
| LabsPhi305 | This is a sample project that uses a the Phi-3 hosted in ollama model to answer a question.  |**coming soon**|
| LabsPhi306 | This is a sample project that implement a Console chat using Semantic Kernel. |**coming soon**|
| LabsPhi307  | This is a sample project that implement a RAG using local embeddings and Semantic Kernel. |**coming soon**|


## How to Run the Projects

To run the projects, follow these steps:
1. Clone the repository to your local machine.

1. Open a terminal and navigate to the desired project. In example, let's run `LabsPhi301` 加載本地 ONNX Phi-3 模型。
    ```bash
    cd .\src\LabsPhi301\
    ```

1. 使用以下命令運行專案
    ```bash
    dotnet run
    ```

1.  範例專案會要求用戶輸入並使用本地模式進行回應。

    運行中的演示類似於這個：

    ![Chat running demo](../../../../../imgs/07/00/SampleConsole.gif)

    ***注意:** 第一個問題中有一個拼寫錯誤，Phi-3 足夠聰明會給出正確答案！*

1.  專案 `LabsPhi304` 要求用戶選擇不同的選項，然後處理請求。例如，分析本地圖像。

    運行中的演示類似於這個：

    ![Image Analysis running demo](../../../../../imgs/07/00/SampleVisionConsole.gif)

**免責聲明**：
本文件是使用基於機器的AI翻譯服務進行翻譯的。我們雖然力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原語言的原始文件為權威來源。對於關鍵信息，建議進行專業人工翻譯。我們不對使用本翻譯而引起的任何誤解或誤釋承擔責任。