# Phi-3 Cookbook: Hands-On Examples with Microsoft's Phi-3 Models

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phi-3cookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phi-3cookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phi-3cookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phi-3cookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phi-3cookbook?style=social&label=Star)](https://GitHub.com/microsoft/phi-3cookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi-3, is a family of open AI models developed by Microsoft. Phi-3 models are the most capable and cost-effective small language models (SLMs) available, outperforming models of the same size and next size up across a variety of language, reasoning, coding, and math benchmarks. The Phi-3 Family includes mini, small, medium and vision versions, trained based on different parameter amounts to serve various application scenarios. For more detailed information about Microsoft's Phi-3 family, please visit the [Welcome to the Phi-3 Family](/md/01.Introduce/Phi3Family.md) page.

![Phi3Family](/imgs/00/Phi3getstarted.png)

## Table of Contents

- Introduction
  - [Setting up your environment](./md/01.Introduce/EnvironmentSetup.md)(✅)
  - [Welcome to the Phi-3 Family](./md/01.Introduce/Phi3Family.md)(✅)
  - [Understanding Key Technologies](./md/01.Introduce/Understandingtech.md)(✅)
  - [AI Safety for Phi-3 Models](./md/01.Introduce/AISafety.md)(✅)
  - [Phi-3 Hardware Support](./md/01.Introduce/Hardwaresupport.md)(✅)
  - [Phi-3 Models & Availability across platforms](./md/01.Introduce/Edgeandcloud.md)(✅)

- Quick Start
  - [Using Phi-3 in GitHub Model Catalog](./md/02.QuickStart/GitHubModel_QuickStart.md)(✅)
  - [Using Phi-3 in Hugging face](./md/02.QuickStart/Huggingface_QuickStart.md)(✅)
  - [Using Phi-3 in Azure AI Studio](./md/02.QuickStart/AzureAIStudio_QuickStart.md)(✅)
  - [Using Phi-3 Model Inference with Azure MaaS or MaaP](./md/02.QuickStart/AzureModel_Inference.md)(✅)
  - [Deploying Phi-3 models as serverless APIs in Azure AI Studio](./md/02.QuickStart/AzureAIStudio_MaaS.md)(✅)
  - [Using Phi-3 in Ollama](./md/02.QuickStart/Ollama_QuickStart.md)(✅)
  - [Using Phi-3 in LM Studio](./md/02.QuickStart/LMStudio_QuickStart.md)(✅)
  - [Using Phi-3 in AI Toolkit VSCode](./md/02.QuickStart/AITookit_QuickStart.md)(✅)

- [Inference Phi-3](./md/03.Inference/overview.md)  
  - [Inference Phi-3 in iOS](./md/03.Inference/iOS_Inference.md)(✅)
  - [Inference Phi-3 in Jetson](./md/03.Inference/Jetson_Inference.md)(✅)
  - [Inference Phi-3 in AI PC](./md/03.Inference/AIPC_Inference.md)(✅)
  - [Inference Phi-3 with Apple MLX Framework](./md/03.Inference/MLX_Inference.md)(✅)
  - [Inference Phi-3 in Local Server](./md/03.Inference/Local_Server_Inference.md)(✅)
  - [Inference Phi-3 in Remote Server using AI Toolkit](./md/03.Inference/Remote_Interence.md)(✅)
  - [Inference Phi-3 with Rust](./md/03.Inference/Rust_Inference.md)(✅)
  - [Inference Phi-3-Vision in Local](./md/03.Inference/Vision_Inference.md)(✅)
  - [Interence Phi-3 with Kaito AKS, Azure Containers(official support)](./md/03.Inference/Kaito_Inference.md)(✅)

- Fine-tuning Phi-3
  - [Downloading & Creating Sample Data Set](./md/04.Fine-tuning/CreatingSampleData.md)(✅)
  - [Fine-tuning Scenarios](./md/04.Fine-tuning/FineTuning_Scenarios.md)(✅)
  - [Fine-tuning vs RAG](./md/04.Fine-tuning/FineTuning_vs_RAG.md)(✅)
  - [Fine-tuning Let Phi-3 become an industry expert](./md/04.Fine-tuning/LetPhi3gotoIndustriy.md)(✅)
  - [Fine-tuning Phi-3 with AI Toolkit for VS Code](./md/04.Fine-tuning/Finetuning_VSCodeaitoolkit.md)(✅)
  - [Fine-tuning Phi-3 with Azure Machine Learning Service](./md/04.Fine-tuning/Introduce_AzureML.md)(✅)
  - [Fine-tuning Phi-3 with Lora](./md/04.Fine-tuning/FineTuning_Lora.md)(✅)
  - [Fine-tuning Phi-3 with QLora](./md/04.Fine-tuning/FineTuning_Qlora.md)(✅)
  - [Fine-tuning Phi-3 with Azure AI Studio](./md/04.Fine-tuning/FineTuning_AIStudio.md)(✅)
  - [Fine-tuning Phi-3 with Azure ML CLI/SDK](./md/04.Fine-tuning/FineTuning_MLSDK.md)(✅)
  - [Fine-tuning with Microsoft Olive](./md/04.Fine-tuning/FineTuning_MicrosoftOlive.md)(✅)
  - [Fine-tuning Phi-3-vision with Weights and Bias](./md/04.Fine-tuning/FineTuning_Phi-3-visionWandB.md)(✅)
  - [Fine-tuning Phi-3 with Apple MLX Framework](./md/04.Fine-tuning/FineTuning_MLX.md)(✅)
  - [Fine-tuning Phi-3-vision (official support)](./md/04.Fine-tuning/FineTuning_Vision.md)(✅)
  - [Fine-Tuning Phi-3 with Kaito AKS , Azure Containers(official Support)](./md/04.Fine-tuning/FineTuning_Kaito.md)(✅)

- Evaluation Phi-3
  - [Introduction to Responsible AI](./md/05.Evaluation/ResponsibleAI.md)(✅)
  - [Introduction to Promptflow](./md/05.Evaluation/Promptflow.md)(✅)
  - [Introduction to Azure AI Studio for evaluation](./md/05.Evaluation/AzureAIStudio.md)(✅)

- E2E Samples for Phi-3-mini
  - [Introduction to End to End Samples](./md/06.E2ESamples/E2E_Introduction.md)(✅)
  - [Prepare your industry data](./md/06.E2ESamples/E2E_Datasets.md)(✅)
  - [Use Microsoft Olive to architect your projects](./md/06.E2ESamples/E2E_LoRA&QLoRA_Config_With_Olive.md)(✅)
  - [Inference Your Fine-tuning ONNX Runtime Model](./md/06.E2ESamples/E2E_Inference_ORT.md)(✅)
  - [Local Chatbot on Android with Phi-3, ONNXRuntime Mobile and ONNXRuntime Generate API](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/mobile/examples/phi-3/android)(✅)
  - [Local Chatbot in the browser using Phi3, ONNX Runtime Web and WebGPU](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)(✅)
  [OpenVino Chat](/md/06.E2ESamples/E2E_OpenVino_Chat.md)(✅)
  - [Multi Model - Interactive Phi-3-mini and OpenAI Whisper](./md/06.E2ESamples/E2E_Phi-3-mini_with_whisper.md)(✅)
  - [WebGPU and Phi-3-mini - Phi-3-mini provides the user with a private (and powerful) chatbot experience. You can try it out](https://huggingface.co/spaces/Xenova/experimental-phi3-webgpu)(✅)
  - [MLFlow - Building a wrapper and using Phi-3 with MLFlow](./md/06.E2ESamples/E2E_Phi-3-MLflow.md)(✅)
  - [Model Optimization - How to optimize Phi-3-min model for ONNX Runtime Web with Olive](https://github.com/microsoft/Olive/tree/main/examples/phi3)(✅)
  - [WinUI3 App with Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)(✅)
  - [WinUI3 Multi Model AI Powered Notes App Sample](https://github.com/microsoft/ai-powered-notes-winui3-sample)(✅)
  - [Fine-tune and Integrate custom Phi-3 models with Prompt flow](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)(✅)
  - [Fine-tune and Integrate custom Phi-3 models with Prompt flow in Azure AI Studio](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIstudio.md)(✅)

- E2E Samples for Phi-3-vision
  - [Phi-3-vision-Image text to text](./md/06.E2ESamples/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)(✅)
  - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [Phi-3-vision CLIP Embedding](./md/06.E2ESamples/E2E_Phi-3-Embedding_Images_with_CLIPVision.md)(✅)
  - [DEMO: Phi-3 Recycling](https://github.com/jennifermarsman/PhiRecycling/)(✅)
  - [Phi-3-vision - Visual language assistant with Phi3-Vision and OpenVINO](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)(✅)
  - [Phi-3 Vision Nvidia NIM](/md/06.E2ESamples/E2E_Nvidia_NIM_Vision.md)(✅)
  - [Phi-3 Vision OpenVino](/md/06.E2ESamples/E2E_OpenVino_Phi3Vision.md)(✅)


- Labs and workshops samples Phi-3
  - [C# .NET Labs](./md/07.Labs/Csharp/csharplabs.md)(✅)
  - [Build your own Visual Studio Code GitHub Copilot Chat with Microsoft Phi-3 Family](./md/07.Labs/VSCode/README.md)(✅)
  - [Phi-3 ONNX Tutorial](https://onnxruntime.ai/docs/genai/tutorials/phi3-python.html)(✅)
  - [Phi-3-vision ONNX Tutorial](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [Run the Phi-3 models with the ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai/blob/main/examples/python/phi-3-tutorial.md)(✅)
  - [Phi-3 ONNX Multi Model LLM Chat UI, This is a chat demo](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/chat_app)(✅)
  - [C# Hello Phi-3 ONNX example Phi-3](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi)(✅)
  - [C# API Phi-3 ONNX example to support Phi3-Vision](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi3V)(✅)
  - [Run C# Phi-3 samples in a CodeSpace](./md/07.Labs/CsharpOllamaCodeSpaces/CsharpOllamaCodeSpaces.md)(✅)
  - [Using Phi-3 with Promptflow and Azure AI Search](./code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md)(✅)
  - [Windows AI-PC APIs with Windows Copilot Library](https://developer.microsoft.com/windows/ai/?WT.mc_id=aiml-137032-kinfeylo)

## Using Phi-3 Models

### Phi-3 on Azure AI Studio

You can learn how to use Microsoft Phi-3 and how to build E2E solutions in your different hardware devices. To experience Phi-3 for yourself, start by playing with the model and customizing Phi-3 for your scenarios using the [Azure AI Studio, Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) you can learn more at Getting Started with [Azure AI Studio](/md/02.QuickStart/AzureAIStudio_QuickStart.md)

**Playground**
Each model has a dedicated playground to test the model [Azure AI Playground](https://aka.ms/try-phi3).

### Phi-3 on GitHub Models
You can learn how to use Microsoft Phi-3 and how to build E2E solutions in your different hardware devices. To experience Phi-3 for yourself, start by playing with the model and customizing Phi-3 for your scenarios using the [GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) you can learn more at Getting Started with [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md)

**Playground**
Each model has a dedicated [playground to test the model](/md/02.QuickStart/GitHubModel_QuickStart.md).

### Phi-3 on Hugging Face

You can also find the model on the [Hugging Face](https://huggingface.co/microsoft)

**Playground**
 [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Multi-Language Support

| Language            | Code | Translation                                   | Translators                                                        |
|---------------------|------|-----------------------------------------------|--------------------------------------------------------------------|
| Traditional Chinese | zh-tw| [閱讀正體中文](./translations/zh-tw/README.md) | [@doggy8088](https://github.com/doggy8088) (MVP & RD)              |
| Simplified Chinese  | zh-cn| [阅读简体中文](./translations/zh-cn/README.md) | [@shijiong](https://github.com/shijiong) (MVP), [@JamboChen](https://github.com/JamboChen) (Student Ambassador) |

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship. Any use of third-party trademarks or logos are subject to those third-party's policies.
