# Welcome to Microsoft Phi-3 Cookbook

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

[![GitHub contributors](https://img.shields.io/github/contributors/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub issues](https://img.shields.io/github/issues/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHub watchers](https://img.shields.io/github/watchers/microsoft/phi-3cookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phi-3cookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub forks](https://img.shields.io/github/forks/microsoft/phi-3cookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phi-3cookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHub stars](https://img.shields.io/github/stars/microsoft/phi-3cookbook?style=social&label=Star)](https://GitHub.com/microsoft/phi-3cookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phi-3, is a family of open AI models developed by Microsoft. Phi-3 models are the most capable and cost-effective small language models (SLMs) available, outperforming models of the same size and next size up across a variety of language, reasoning, coding, and math benchmarks. Here is a manual on how to use the Microsoft Phi-3 family.

![Phi3Family](/imgs/00/Phi3getstarted.png)

## Microsoft's Phi-3 family

Phi-3 models significantly outperform language models of the same and larger sizes on key benchmarks (see benchmark numbers below, higher is better). Phi-3-mini does better than models twice its size, and Phi-3-small and Phi-3-medium outperform much larger models, including GPT-3.5T.

All reported numbers are produced with the same pipeline to ensure that the numbers are comparable. As a result, these numbers may differ from other published numbers due to slight differences in the evaluation methodology. More details on benchmarks are provided in our technical paper.

### Phi-3-mini

Phi-3-mini, a 3.8B language model is available on [Microsoft Azure AI Studio](https://aka.ms/phi3-azure-ai), [Hugging Face](https://huggingface.co/collections/microsoft/phi-3-6626e15e9585a200d2d761e3), and [Ollama](https://ollama.com/library/phi3).

### Phi-3-small

Phi-3-small with only 7B parameters beats GPT-3.5T across a variety of language, reasoning, coding, and math benchmarks.

![phimodelsmall](/imgs/00/phi3small.png)

### Phi-3-midium

Phi-3-medium with 14B parameters continues the trend and outperforms Gemini 1.0 Pro.

![phimodelmedium](/imgs/00/phi3medium.png)

### Phi-3-vision

Phi-3-vision with just 4.2B parameters continues that trend and outperforms larger models such as Claude-3 Haiku and Gemini 1.0 Pro V across general visual reasoning tasks, OCR, table and chart understanding tasks.

![phimodelvision](/imgs/00/phi3vision.png)

> **Note**
>
> Phi-3 models do not perform as well on factual knowledge benchmarks (such as TriviaQA) as the smaller model size results in less capacity to retain facts.

### Phi-Silica

We are introducing Phi Silica which is built from the Phi series of models and is designed specifically for the NPUs in Copilot+ PCs. Windows is the first platform to have a state-of-the-art small language model (SLM) custom built for the NPU and shipping inbox. Phi Silica API along with OCR, Studio Effects, Live Captions, and Recall User Activity APIs will be available in Windows Copilot Library in June. More APIs like Vector Embedding, RAG API, and Text Summarization will be coming later.

## Phi-3 on Azure AI Studio

You can learn how to use Microsoft Phi-3 and how to build E2E solutions in your different hardware devices. To experience Phi-3 for yourself, start by playing with the model and customizing Phi-3 for your scenarios using the [Azure AI Studio, Azure AI Model Catalog](https://aka.ms/phi3-azure-ai)

**Playground**
Each model has a dedicated playground to test the model [Azure AI Playground](https://aka.ms/try-phi3).

## Phi-3 on Hugging Face

You can also find the model on the [Hugging Face](https://huggingface.co/microsoft)

**Playground**
 [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## Contents

This cookbook includes:

## **Microsoft Phi-3 Cookbook**

- [Introduction]()
  - [Setting up your environment](./md/01.Introduce/EnvironmentSetup.md)(✅)
  - [Welcome to the Phi-3 Family](./md/01.Introduce/Phi3Family.md)(✅)
  - [Understanding Key Technologies](./md/01.Introduce/Understandingtech.md)(✅)
  - [AI Safety for Phi-3 Models](./md/01.Introduce/AISafety.md)(✅)
  - [Phi-3 Hardware Support](./md/01.Introduce/Hardwaresupport.md)(✅)
  - [Phi-3 Models & Availability across platforms](./md/01.Introduce/Edgeandcloud.md)(✅)

- [Quick Start]()
  - [Using Phi-3 in Hugging face](./md/02.QuickStart/Huggingface_QuickStart.md)(✅)
  - [Using Phi-3 in Azure AI Studio](./md/02.QuickStart/AzureAIStudio_QuickStart.md)(✅)
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
  - [Inference Phi-3-Vision in Local](./md/03.Inference/Vision_Inference.md)(✅)

- [Fine-tuning Phi-3]()
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

- [Evaluation Phi-3]()
  - [Introduction to Responsible AI](./md/05.Evaluation/ResponsibleAI.md)(✅)
  - [Introduction to Promptflow](./md/05.Evaluation/Promptflow.md)(✅)
  - [Introduction to Azure AI Studio for evaluation](./md/05.Evaluation/AzureAIStudio.md)(✅)

- [E2E Samples for Phi-3-mini]()
  - [Introduction to End to End Samples](./md/06.E2ESamples/E2E_Introduction.md)(✅)
  - [Prepare your industry data](./md/06.E2ESamples/E2E_Datasets.md)(✅)
  - [Use Microsoft Olive to architect your projects](./md/06.E2ESamples/E2E_LoRA&QLoRA_Config_With_Olive.md)(✅)
  - [Inference Your Fine-tuning ONNX Runtime Model](./md/06.E2ESamples/E2E_Inference_ORT.md)(✅)
  - [Multi Model - Interactive Phi-3-mini and OpenAI Whisper](./md/06.E2ESamples/E2E_Phi-3-mini_with_whisper.md)(✅)
  - [MLFlow - Building a wrapper and using Phi-3 with MLFlow](./md/06.E2ESamples/E2E_Phi-3-MLflow.md)(✅)
  - [WinUI3 App with Phi-3 mini-4k-instruct-onnx](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)(✅)
  - [WinUI3 Multi Model AI Powered Notes App Sample](https://github.com/microsoft/ai-powered-notes-winui3-sample)(✅)
  - [Fine-tune and Integrate custom Phi-3 models with Prompt flow](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)(✅)

- [E2E Samples for Phi-3-vision]()
  - [Phi-3-vision-Image text to text](./md/06.E2ESamples/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)(✅)
  - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [Phi-3-vision CLIP Embedding](./md/06.E2ESamples/E2E_Phi-3-Embedding_Images_with_CLIPVision.md)(✅)

- [Labs and workshops samples Phi-3]()
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

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

## Trademarks

This project may contain trademarks or logos for projects, products, or services. Authorized use of Microsoft trademarks or logos is subject to and must follow [Microsoft's Trademark & Brand Guidelines](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general).
Use of Microsoft trademarks or logos in modified versions of this project must not cause confusion or imply Microsoft sponsorship.
Any use of third-party trademarks or logos are subject to those third-party's policies.
