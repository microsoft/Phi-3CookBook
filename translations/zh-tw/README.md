# 歡迎來到 Microsoft Phi-3 Cookbook

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

這是一本關於如何使用 Microsoft Phi-3 系列的手冊。

![Phi3Family](/imgs/00/Phi3getstarted.png)

Phi-3，是由 Microsoft 開發的一系列開放 AI 模型。Phi-3 模型是目前最強大且具成本效益的小型語言模型（SLMs），在各種語言、推論、編碼和數學基準測試中，超越了相同大小和下一個大小的模型。

Phi-3-mini，一個 3.8B 語言模型，可在 [Microsoft Azure AI Studio](https://aka.ms/phi3-azure-ai)、[Hugging Face](https://huggingface.co/collections/microsoft/phi-3-6626e15e9585a200d2d761e3) 和 [Ollama](https://ollama.com/library/phi3) 上使用。Phi-3 模型在關鍵基準測試中顯著超越了相同和更大尺寸的語言模型（請參見下方基準測試數據，數值越高越好）。Phi-3-mini 的表現超過了其體積兩倍的模型，而 Phi-3-small 和 Phi-3-medium 則超越了包括 GPT-3.5T 在內的更大模型。

所有報告的數字都是通過相同的流程產生的，以確保數字具有可比性。因此，由於評估方法的細微差異，這些數字可能與其他已發表的數字有所不同。更多關於基準測試的詳細資訊請參見我們的技術文件。

Phi-3-small 僅用 7B 參數在各種語言、推論、程式碼和數學基準測試中擊敗 GPT-3.5T。

![phimodelsmall](/imgs/00/phi3small.png)

Phi-3-medium 擁有 14B 參數，繼續這一趨勢並超越 Gemini 1.0 Pro。

![phimodelmedium](/imgs/00/phi3medium.png)

Phi-3-vision 僅用 4.2B 參數延續了這一趨勢，並在一般視覺推論任務、OCR、表格和圖表理解任務中超越了更大的模型，如 Claude-3 Haiku 和 Gemini 1.0 Pro V。

![phimodelvision](/imgs/00/phi3vision.png)

注意: Phi-3 模型在事實知識基準（如 TriviaQA）上的表現不如較小的模型，因為較小的模型容量導致保留事實的能力較差。

我們準備推出 Phi Silica，它是從 Phi 系列模型建構而成，專為 Copilot+ PC 中的 NPU 設計。Windows 是首個擁有為 NPU 和內建收件匣量身定制的先進小型語言模型（SLM）的平台。Phi Silica API 以及 OCR、Studio Effects、Live Captions、Recall User Activity API 將於 6 月在 Windows Copilot 函式庫中提供。更多 API，如 Vector Embedding、RAG API、Text Summarization 將在稍後推出。

## Azure AI Studio

您可以學習如何使用 Microsoft Phi-3 以及如何在不同的硬體設備中建構 E2E 解決方案。要親自體驗 Phi-3，請從使用模型並使用 [Azure AI Studio, Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) 自訂 Phi-3 為您的情境開始。

**Playground**
每個模型都有專用的 Playground 來測試模型 [Azure AI Playground](https://aka.ms/try-phi3)。

## Hugging Face

你也可以在 [Hugging Face](https://huggingface.co/microsoft) 找到這個模型。

**Playground**
 [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)。

## 目錄

這本 Cookbook 包括:

## **Microsoft Phi-3 Cookbook**

* [簡介]()
    * [設定你的環境](../../md/01.Introduce/translations/zh-tw/EnvironmentSetup.md)(✅)
    * [歡迎來到 Phi-3 家族](../../md/01.Introduce/translations/zh-tw/Phi3Family.md)(✅)
    * [了解關鍵技術](../../md/01.Introduce/translations/zh-tw/Understandingtech.md)(✅)
    * [Phi-3 模型的 AI 安全性](../../md/01.Introduce/translations/zh-tw/AISafety.md)(✅)
    * [Phi-3 硬體支援](../../md/01.Introduce/translations/zh-tw/Hardwaresupport.md)(✅)
    * [Phi-3 模型及跨平台可用性](../../md/01.Introduce/translations/zh-tw/Edgeandcloud.md)(✅)

* [快速開始]()
    * [在 Hugging face 中使用 Phi-3](../../md/02.QuickStart/translations/zh-tw/Huggingface_QuickStart.md)(✅)
    * [在 Azure AI Studio 中使用 Phi-3](../../md/02.QuickStart/translations/zh-tw/AzureAIStudio_QuickStart.md)(✅)
    * [在 Ollama 中使用 Phi-3](../../md/02.QuickStart/translations/zh-tw/Ollama_QuickStart.md)(✅)
    * [在 LM Studio 中使用 Phi-3](../../md/02.QuickStart/translations/zh-tw/LMStudio_QuickStart.md)(✅)
    * [在 AI Toolkit VSCode 中使用 Phi-3](../../md/02.QuickStart/translations/zh-tw/AITookit_QuickStart.md)(✅)

* [Phi-3 推論](../../md/03.Inference/translations/zh-tw/overview.md)
    * [在 iOS 中推論 Phi-3](../../md/03.Inference/translations/zh-tw/iOS_Inference.md)(✅)
    * [在 Jetson 中推論 Phi-3](../../md/03.Inference/translations/zh-tw/Jetson_Inference.md)(✅)
    * [在 AI PC 中推論 Phi-3](../../md/03.Inference/translations/zh-tw/AIPC_Inference.md)(✅)
    * [使用 Apple MLX Framework 推論 Phi-3](../../md/03.Inference/translations/zh-tw/MLX_Inference.md)(✅)
    * [在本地伺服器中推論 Phi-3](../../md/03.Inference/translations/zh-tw/Local_Server_Inference.md)(✅)
    * [使用 AI Toolkit 在遠端伺服器中推論 Phi-3](../../md/03.Inference/translations/zh-tw/Remote_Interence.md)(✅)
    * [在本地推論 Phi-3-Vision](../../md/03.Inference/translations/zh-tw/Vision_Inference.md)(✅)

* [Phi-3 微調]()
    * [下載及建立範例數據集](../../md/04.Fine-tuning/translations/zh-tw/CreatingSampleData.md)(✅)
    * [微調場景](../../md/04.Fine-tuning/translations/zh-tw/FineTuning_Scenarios.md)(✅)
    * [微調 vs RAG](../../md/04.Fine-tuning/translations/zh-tw/FineTuning_vs_RAG.md)(✅)
    * [微調讓 Phi-3 成為行業專家](../../md/04.Fine-tuning/translations/zh-tw/LetPhi3gotoIndustriy.md)(✅)
    * [使用 AI Toolkit for VS Code 微調 Phi-3](../../md/04.Fine-tuning/translations/zh-tw/Finetuning_VSCodeaitoolkit.md)(✅)
    * [使用 Azure Machine Learning Service 微調 Phi-3](../../md/04.Fine-tuning/translations/zh-tw/Introduce_AzureML.md)(✅)
    * [使用 Lora 微調 Phi-3](../../md/04.Fine-tuning/translations/zh-tw/FineTuning_Lora.md)(✅)
    * [使用 QLora 微調 Phi-3](../../md/04.Fine-tuning/translations/zh-tw/FineTuning_Qlora.md)(✅)
    * [使用 Azure AI Studio 微調 Phi-3](../../md/04.Fine-tuning/translations/zh-tw/FineTuning_AIStudio.md)(✅)
    * [使用 Azure ML CLI/SDK 微調 Phi-3](../../md/04.Fine-tuning/translations/zh-tw/FineTuning_MLSDK.md)(✅)
    * [使用 Microsoft Olive 微調](../../md/04.Fine-tuning/translations/zh-tw/FineTuning_MicrosoftOlive.md)(✅)
    * [使用 Weights and Bias 微調 Phi-3-vision](../../md/04.Fine-tuning/translations/zh-tw/FineTuning_Phi-3-visionWandB.md)(✅)
    * [使用 Apple MLX Framework 微調 Phi-3](../../md/04.Fine-tuning/translations/zh-tw/FineTuning_MLX.md)(✅)

* [Phi-3 評估]()
    * [負責任 AI 簡介](../../md/05.Evaluation/translations/zh-tw/ResponsibleAI.md)(✅)
    * [Promptflow 簡介](../../md/05.Evaluation/translations/zh-tw/Promptflow.md)(✅)
    * [Azure AI Studio 評估簡介](../../md/05.Evaluation/translations/zh-tw/AzureAIStudio.md)(✅)

* [Phi-3-mini 的端到端範例]()
    * [端到端範例簡介](../../md/06.E2ESamples/translations/zh-tw/E2E_Introduction.md)(✅)
    * [準備你的行業數據](../../md/06.E2ESamples/translations/zh-tw/E2E_Datasets.md)(✅)
    * [使用 Microsoft Olive 架構你的項目](../../md/06.E2ESamples/translations/zh-tw/E2E_LoRA&QLoRA_Config_With_Olive.md)(✅)
    * [推論你的微調 ONNX Runtime 模型](../../md/06.E2ESamples/translations/zh-tw/E2E_Inference_ORT.md)(✅)
    * [多模型 - 互動 Phi-3-mini 和 OpenAI Whisper](../../md/06.E2ESamples/translations/zh-tw/E2E_Phi-3-mini_with_whisper.md)(✅)
    * [MLFlow - 建立包裝器並使用 Phi-3 與 MLFlow](../../md/06.E2ESamples/translations/zh-tw/E2E_Phi-3-MLflow.md)(✅)

* [Phi-3-vision 的端到端範例]()
    * [Phi3-vision-圖像文字轉文字](../../md/06.E2ESamples/translations/zh-tw/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)(✅)
    * [Phi-3-Vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
    * [Phi-3-vision CLIP 嵌入](../../md/06.E2ESamples/translations/zh-tw/E2E_Phi-3-Embedding_Images_with_CLIPVision.md)(✅)

* [Phi-3 的實驗室和工作坊範例]()
    * [C# .NET 實驗室](../../md/07.Labs/translations/zh-tw/Csharp/csharplabs.md)(✅)
    * [使用 Microsoft Phi-3 家族建立你自己的 Visual Studio Code GitHub Copilot Chat](../../md/07.Labs/translations/zh-tw/VSCode/README.md)(✅)
    * [Phi-3 ONNX 指南](https://onnxruntime.ai/docs/genai/tutorials/phi3-python.html)(✅)
    * [Phi-3-vision ONNX 指南](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
     * [使用 ONNX Runtime generate() API 執行 Phi-3 模型](https://github.com/microsoft/onnxruntime-genai/blob/main/examples/python/phi-3-tutorial.md)(✅)
    * [Phi-3 ONNX 多模型 LLM 聊天 UI，這是一個聊天展示](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/chat_app)(✅)
     * [C# Hello Phi-3 ONNX 範例 Phi-3](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi)(✅)
     * [C# API Phi-3 ONNX 範例支援 Phi3-Vision](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi3V)(✅)

## 貢獻

這個專案歡迎貢獻和建議。大多數貢獻需要您同意一份貢獻者許可協議 (CLA)，聲明您有權利並實際授予我們使用您貢獻的權利。詳情請訪問 https://cla.opensource.microsoft.com。

當你提交一個 pull request 時，CLA 機器人會自動判斷你是否需要提供 CLA 並適當地裝飾 PR（例如，狀態檢查、評論）。只需按照機器人提供的指示操作。你只需要在所有使用我們 CLA 的 repos 中執行一次這個操作。

這個專案已採用[Microsoft 開源行為準則](https://opensource.microsoft.com/codeofconduct/)。
欲了解更多資訊，請參閱[行為準則常見問題](https://opensource.microsoft.com/codeofconduct/faq/)或
聯繫[opencode@microsoft.com](mailto:opencode@microsoft.com)以提出任何其他問題或意見。

## 商標

此專案可能包含專案、產品或服務的商標或標誌。授權使用 Microsoft 商標或標誌必須遵守並遵循 [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/en-us/legal/intellectualproperty/trademarks/usage/general)。在此專案的修改版本中使用 Microsoft 商標或標誌不得引起混淆或暗示 Microsoft 的贊助。任何使用第三方商標或標誌均需遵守該第三方的政策。

