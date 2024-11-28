# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models

[![Open and use the samples in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phi-3cookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phi-3cookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phi-3cookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phi-3cookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phi-3cookbook?style=social&label=Star)](https://GitHub.com/microsoft/phi-3cookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)


[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi 是微軟開發的一系列開源 AI 模型。Phi 模型是目前最強大且具成本效益的小型語言模型（SLM），在各種語言、推理、編碼和數學基準上表現超越同尺寸和更大尺寸的模型。Phi-3 系列包括 mini、small、medium 和 vision 版本，根據不同的參數數量進行訓練，以滿足各種應用場景。關於微軟 Phi 系列的更多詳細資訊，請訪問 [Welcome to the Phi Family](/md/01.Introduce/Phi3Family.md) 頁面。

請按照以下步驟進行：
1. **Fork 這個倉庫**：點擊這個頁面右上角的 "Fork" 按鈕。
2. **Clone 這個倉庫**：  `git clone https://github.com/microsoft/Phi-3CookBook.git`

![Phi3Family](/imgs/00/Phi3getstarted.png)

## 目錄

- 簡介
  - [設定你的環境](./md/01.Introduce/EnvironmentSetup.md)(✅)
  - [歡迎來到 Phi 家族](./md/01.Introduce/Phi3Family.md)(✅)
  - [了解關鍵技術](./md/01.Introduce/Understandingtech.md)(✅)
  - [Phi 模型的 AI 安全性](./md/01.Introduce/AISafety.md)(✅)
  - [Phi-3 硬體支援](./md/01.Introduce/Hardwaresupport.md)(✅)
  - [Phi-3 模型及其在各平台的可用性](./md/01.Introduce/Edgeandcloud.md)(✅)
  - [使用 Guidance-ai 和 Phi](./md/01.Introduce/Guidance.md)(✅)
  - [GitHub Marketplace 模型](https://github.com/marketplace/models)(✅)
  - [Azure AI 模型目錄](https://ai.azure.com)(✅)

- 快速開始
  - [在 GitHub 模型目錄中使用 Phi-3](./md/02.QuickStart/GitHubModel_QuickStart.md)(✅)
  - [在 Hugging face 中使用 Phi-3](./md/02.QuickStart/Huggingface_QuickStart.md)(✅)
  - [使用 OpenAI SDK 與 Phi-3](./md/02.QuickStart/OpenAISDK_Quickstart.md)(✅)
  - [使用 Http 請求與 Phi-3](./md/02.QuickStart/HttpAPI_QuickStart.md)(✅)
  - [在 Azure AI Studio 中使用 Phi-3](./md/02.QuickStart/AzureAIStudio_QuickStart.md)(✅)
  - [使用 Azure MaaS 或 MaaP 進行 Phi-3 模型推理](./md/02.QuickStart/AzureModel_Inference.md)(✅)
  - [在 GitHub 和 Azure AI 中使用 Azure Inference API 與 Phi-3](./md/02.QuickStart/AzureInferenceAPI_QuickStart.md)
  - [在 Azure AI Studio 中部署 Phi-3 模型為無伺服器 API](./md/02.QuickStart/AzureAIStudio_MaaS.md)(✅)
  - [在 Ollama 中使用 Phi-3](./md/02.QuickStart/Ollama_QuickStart.md)(✅)
- [在 LM Studio 中使用 Phi-3](./md/02.QuickStart/LMStudio_QuickStart.md)(✅)
  - [在 AI Toolkit VSCode 中使用 Phi-3](./md/02.QuickStart/AITookit_QuickStart.md)(✅)
  - [使用 Phi-3 和 LiteLLM](./md/02.QuickStart/LiteLLM_QuickStart.md)(✅)

- [Phi-3 推理](./md/03.Inference/overview.md)  
  - [在 iOS 上进行 Phi-3 推理](./md/03.Inference/iOS_Inference.md)(✅)
  - [在 Android 上进行 Phi-3.5 推理](./md/08.Update/Phi35/050.UsingPhi35TFLiteCreateAndroidApp.md)(✅)
  - [在 Jetson 上进行 Phi-3 推理](./md/03.Inference/Jetson_Inference.md)(✅)
  - [在 AI PC 上进行 Phi-3 推理](./md/03.Inference/AIPC_Inference.md)(✅)
  - [使用 Apple MLX Framework 进行 Phi-3 推理](./md/03.Inference/MLX_Inference.md)(✅)
  - [在本地服务器上进行 Phi-3 推理](./md/03.Inference/Local_Server_Inference.md)(✅)
  - [使用 AI Toolkit 在远程服务器上进行 Phi-3 推理](./md/03.Inference/Remote_Interence.md)(✅)
  - [使用 Rust 进行 Phi-3 推理](./md/03.Inference/Rust_Inference.md)(✅)
  - [在本地进行 Phi-3-Vision 推理](./md/03.Inference/Vision_Inference.md)(✅)
  - [使用 Kaito AKS 和 Azure Containers（官方支持）进行 Phi-3 推理](./md/03.Inference/Kaito_Inference.md)(✅)
  - [推理你微调的 ONNX Runtime 模型](./md/06.E2ESamples/E2E_Inference_ORT.md)(✅)

- Phi-3 微调
  - [下载并创建样本数据集](./md/04.Fine-tuning/CreatingSampleData.md)(✅)
  - [微调场景](./md/04.Fine-tuning/FineTuning_Scenarios.md)(✅)
  - [微调 vs RAG](./md/04.Fine-tuning/FineTuning_vs_RAG.md)(✅)
  - [微调让 Phi-3 成为行业专家](./md/04.Fine-tuning/LetPhi3gotoIndustriy.md)(✅)
  - [使用 AI Toolkit for VS Code 微调 Phi-3](./md/04.Fine-tuning/Finetuning_VSCodeaitoolkit.md)(✅)
  - [使用 Azure Machine Learning Service 微调 Phi-3](./md/04.Fine-tuning/Introduce_AzureML.md)(✅)
  - [使用 Lora 微调 Phi-3](./md/04.Fine-tuning/FineTuning_Lora.md)(✅)
  - [使用 QLora 微调 Phi-3](./md/04.Fine-tuning/FineTuning_Qlora.md)(✅)
  - [使用 Azure AI Studio 微调 Phi-3](./md/04.Fine-tuning/FineTuning_AIStudio.md)(✅)
  - [使用 Azure ML CLI/SDK 微调 Phi-3](./md/04.Fine-tuning/FineTuning_MLSDK.md)(✅)
  - [使用 Microsoft Olive 微调](./md/04.Fine-tuning/FineTuning_MicrosoftOlive.md)(✅)
  - [Microsoft Olive 实践实验室微调](./code/04.Finetuning/olive-lab/readme.md)(✅)
  - [使用 Weights and Bias 微调 Phi-3-vision](./md/04.Fine-tuning/FineTuning_Phi-3-visionWandB.md)(✅)
  - [使用 Apple MLX Framework 微调 Phi-3](./md/04.Fine-tuning/FineTuning_MLX.md)(✅)
  - [Phi-3-vision 微调（官方支持）](./md/04.Fine-tuning/FineTuning_Vision.md)(✅)
- [使用 Kaito AKS 和 Azure Containers 進行 Phi-3 微調（官方支持）](./md/04.Fine-tuning/FineTuning_Kaito.md)(✅)
  - [Phi-3 和 3.5 Vision 的微調](https://github.com/2U1/Phi3-Vision-Finetune)(✅)

- 評估 Phi-3
  - [負責任 AI 簡介](./md/05.Evaluation/ResponsibleAI.md)(✅)
  - [Promptflow 簡介](./md/05.Evaluation/Promptflow.md)(✅)
  - [Azure AI Studio 評估簡介](./md/05.Evaluation/AzureAIStudio.md)(✅)

- Phi-3-mini 的端到端範例
  - [端到端範例簡介](./md/06.E2ESamples/E2E_Introduction.md)(✅)
  - [準備您的行業數據](./md/06.E2ESamples/E2E_Datasets.md)(✅)
  - [使用 Microsoft Olive 設計您的項目](./md/06.E2ESamples/E2E_LoRA&QLoRA_Config_With_Olive.md)(✅)
  - [在 Android 上使用 Phi-3、ONNXRuntime Mobile 和 ONNXRuntime Generate API 進行本地聊天機器人](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/mobile/examples/phi-3/android)(✅)
  - [Hugging Face Space WebGPU 和 Phi-3-mini Demo - Phi-3-mini 提供用戶一個私密且強大的聊天機器人體驗。你可以試試](https://huggingface.co/spaces/Xenova/experimental-phi3-webgpu)(✅)
  - [在瀏覽器中使用 Phi3、ONNX Runtime Web 和 WebGPU 的本地聊天機器人](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)(✅)
  - [OpenVino 聊天](/md/06.E2ESamples/E2E_OpenVino_Chat.md)(✅)
  - [多模型 - 互動式 Phi-3-mini 和 OpenAI Whisper](./md/06.E2ESamples/E2E_Phi-3-mini_with_whisper.md)(✅)
  - [MLFlow - 構建包裝器並使用 Phi-3 與 MLFlow](./md/06.E2ESamples/E2E_Phi-3-MLflow.md)(✅)
  - [模型優化 - 如何使用 Olive 優化 Phi-3-mini 模型以適應 ONNX Runtime Web](https://github.com/microsoft/Olive/tree/main/examples/phi3)(✅)
  - [使用 Phi-3 mini-4k-instruct-onnx 的 WinUI3 應用程式](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)(✅)
  - [WinUI3 多模型 AI 驅動的筆記應用程式範例](https://github.com/microsoft/ai-powered-notes-winui3-sample)(✅)
  - [使用 Prompt flow 微調並整合自定義 Phi-3 模型](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)(✅)
  - [在 Azure AI Studio 中使用 Prompt flow 微調並整合自定義 Phi-3 模型](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIstudio.md)(✅)
  - [在 Azure AI Studio 中根據 Microsoft 的負責任 AI 原則評估微調後的 Phi-3 / Phi-3.5 模型](./md/06.E2ESamples/E2E_Phi-3-Evaluation_AIstudio.md)(✅)
  - [Phi-3.5-mini-instruct 語言預測範例（中文/英文）](../../code/09.UpdateSamples/Aug/phi3-instruct-demo.ipynb)(✅)

- Phi-3-vision 的端到端範例
  - [Phi-3-vision-圖像文本轉文本](../../code/06.E2E/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)(✅)
  - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [Phi-3-vision CLIP 嵌入](./md/06.E2ESamples/E2E_Phi-3-Embedding_Images_with_CLIPVision.md)(✅)
  - [DEMO: Phi-3 回收](https://github.com/jennifermarsman/PhiRecycling/)(✅)
  - [Phi-3-vision - 使用 Phi3-Vision 和 OpenVINO 的視覺語言助手](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)(✅)
  - [Phi-3 Vision Nvidia NIM](/md/06.E2ESamples/E2E_Nvidia_NIM_Vision.md)(✅)
  - [Phi-3 Vision OpenVino](/md/06.E2ESamples/E2E_OpenVino_Phi3Vision.md)(✅)
  - [Phi-3.5 Vision 多幀或多圖像範例](../../code/09.UpdateSamples/Aug/phi3-vision-demo.ipynb)(✅)

- Phi-3.5-MoE 的端到端範例
  - [Phi-3.5 專家模型 (MoEs) 社交媒體範例](../../code/09.UpdateSamples/Aug/phi3_moe_demo.ipynb)(✅)
- [使用 NVIDIA NIM Phi-3 MOE、Azure AI Search 和 LlamaIndex 構建檢索增強生成 (RAG) 管道](https://github.com/farzad528/azure-ai-search-python-playground/blob/main/azure-ai-search-nvidia-rag.ipynb)(✅)

- Phi-3 實驗室和工作坊範例
  - [C# .NET 實驗室](./md/07.Labs/Csharp/csharplabs.md)(✅)
  - [使用 Microsoft Phi-3 家族構建你自己的 Visual Studio Code GitHub Copilot 聊天](./md/07.Labs/VSCode/README.md)(✅)
  - [本地 WebGPU Phi-3 迷你 RAG 聊天機器人範例與本地 RAG 文件](./code/08.RAG/rag_webgpu_chat/README.md)(✅)
  - [Phi-3 ONNX 教程](https://onnxruntime.ai/docs/genai/tutorials/phi3-python.html)(✅)
  - [Phi-3-vision ONNX 教程](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [使用 ONNX Runtime generate() API 運行 Phi-3 模型](https://github.com/microsoft/onnxruntime-genai/blob/main/examples/python/phi-3-tutorial.md)(✅)
  - [Phi-3 ONNX 多模型 LLM 聊天 UI，這是一個聊天演示](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/chat_app)(✅)
  - [C# Hello Phi-3 ONNX 範例 Phi-3](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi)(✅)
  - [支持 Phi3-Vision 的 C# API Phi-3 ONNX 範例](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi3V)(✅)
  - [在 CodeSpace 中運行 C# Phi-3 範例](./md/07.Labs/CsharpOllamaCodeSpaces/CsharpOllamaCodeSpaces.md)(✅)
  - [使用 Phi-3 與 Promptflow 和 Azure AI Search](./code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md)(✅)
  - [Windows AI-PC API 與 Windows Copilot Library](https://developer.microsoft.com/windows/ai/?WT.mc_id=aiml-137032-kinfeylo)

- 學習 Phi-3.5
  - [Phi-3.5 家族的新功能](./md/08.Update/Phi35/010.WhatsNewInPhi35.md)(✅)
  - [量化 Phi-3.5 家族](./md/08.Update/Phi35/020.QuantifyingPhi35.md)(✅)
    - [使用 llama.cpp 量化 Phi-3.5](./md/08.Update/Phi35/021.UsingLlamacppQuantifyingPhi35.md)(✅)
    - [使用 onnxruntime 的生成式 AI 擴展量化 Phi-3.5](./md/08.Update/Phi35/022.UsingORTGenAIQuantifyingPhi35.md)(✅)
    - [使用 Intel OpenVINO 量化 Phi-3.5](./md/08.Update/Phi35/023.UsingIntelOpenVINOQuantifyingPhi35.md)(✅)
    - [使用 Apple MLX 框架量化 Phi-3.5](./md/08.Update/Phi35/024.UsingAppleMLXQuantifyingPhi35.md)(✅)
  - Phi-3.5 應用範例
    - [Phi-3.5-Instruct WebGPU RAG 聊天機器人](./md/08.Update/Phi35/031.WebGPUWithPhi35Readme.md)(✅)
    - [使用 Phi-3.5 和 GitHub 模型創建你自己的 Visual Studio Code 聊天 Copilot 代理](./md/08.Update/Phi35/032.CreateVSCodeChatAgentWithGitHubModels.md)(✅)
    - [使用 Windows GPU 和 Phi-3.5-Instruct ONNX 創建 Prompt flow 解決方案](./md/08.Update/Phi35/040.UsingPromptFlowWithONNX.md)(✅)
    - [使用 Microsoft Phi-3.5 tflite 創建 Android 應用](./md/08.Update/Phi35/050.UsingPhi35TFLiteCreateAndroidApp.md)(✅)

## 使用 Phi-3 模型

### 在 Azure AI Studio 上使用 Phi-3

你可以學習如何使用 Microsoft Phi-3 以及如何在不同硬件設備上構建 E2E 解決方案。要親自體驗 Phi-3，請從使用 [Azure AI Foundry Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) 開始，了解如何為你的場景定制 Phi-3，更多信息請參見 [Azure AI Studio 快速入門](/md/02.QuickStart/AzureAIStudio_QuickStart.md)

**Playground**
每個模型都有專屬的測試區域 [Azure AI Playground](https://aka.ms/try-phi3)。

### 在 GitHub 模型上使用 Phi-3

你可以學習如何使用 Microsoft Phi-3 以及如何在不同硬件設備上構建 E2E 解決方案。要親自體驗 Phi-3，請從使用 [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) 開始，了解如何為你的場景定制 Phi-3，更多信息請參見 [GitHub Model Catalog 快速入門](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**
每個模型都有專屬的 [測試區域](/md/02.QuickStart/GitHubModel_QuickStart.md)。

### 在 Hugging Face 上使用 Phi-3

你也可以在 [Hugging Face](https://huggingface.co/microsoft) 找到這個模型

**Playground**
[Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🌐 多語言支援

> **Note:**
> 這些翻譯是使用開源的 [co-op-translator](https://github.com/Azure/co-op-translator) 自動生成的，可能包含錯誤或不準確之處。對於關鍵資訊，建議參考原文或諮詢專業人員。如果你想添加或更新翻譯，請參考 [co-op-translator](https://github.com/Azure/co-op-translator) 儲存庫，你可以使用簡單的命令輕鬆貢獻。

| 語言                | 代碼 | 翻譯後的 README 連結                                   | 最後更新日期   |
|---------------------|------|---------------------------------------------------------|--------------|
| 中文（簡體）        | zh   | [Chinese Translation](../zh/README.md)      | 2024-11-29   |
| 中文（繁體）        | tw   | [Chinese Translation](./README.md)      | 2024-11-29   |
| 法文                | fr   | [French Translation](../fr/README.md)       | 2024-11-29   |
| 日文                | ja   | [Japanese Translation](../ja/README.md)     | 2024-11-29   |
| 韓文                | ko   | [Korean Translation](../ko/README.md)       | 2024-11-29   |
| 西班牙文            | es   | [Spanish Translation](../es/README.md)      | 2024-11-29   |

## 商標

此專案可能包含專案、產品或服務的商標或標誌。使用 Microsoft 商標或標誌需經授權，並且必須遵循 [Microsoft 的商標與品牌指南](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)。
在修改版本的此專案中使用 Microsoft 商標或標誌不得引起混淆或暗示 Microsoft 贊助。任何使用第三方商標或標誌均需遵循該第三方的政策。

**免責聲明**:
本文檔已使用基於機器的人工智能翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以其原始語言的原始文件為權威來源。對於關鍵信息，建議進行專業的人類翻譯。我們對因使用此翻譯而產生的任何誤解或誤讀不承擔責任。