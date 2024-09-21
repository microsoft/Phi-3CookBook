# Phi-3 クックブック: MicrosoftのPhi-3モデルを使った実践例

[![GitHub Codespacesでサンプルを開いて使用する](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)
[![Dev Containersで開く](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

[![GitHubのコントリビューター](https://img.shields.io/github/contributors/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/graphs/contributors/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHubの問題](https://img.shields.io/github/issues/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/issues/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHubのプルリクエスト](https://img.shields.io/github/issues-pr/microsoft/phi-3cookbook.svg)](https://GitHub.com/microsoft/phi-3cookbook/pulls/?WT.mc_id=aiml-137032-kinfeylo)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com?WT.mc_id=aiml-137032-kinfeylo)

[![GitHubウォッチャー](https://img.shields.io/github/watchers/microsoft/phi-3cookbook.svg?style=social&label=Watch)](https://GitHub.com/microsoft/phi-3cookbook/watchers/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHubフォーク](https://img.shields.io/github/forks/microsoft/phi-3cookbook.svg?style=social&label=Fork)](https://GitHub.com/microsoft/phi-3cookbook/network/?WT.mc_id=aiml-137032-kinfeylo)
[![GitHubスター](https://img.shields.io/github/stars/microsoft/phi-3cookbook?style=social&label=Star)](https://GitHub.com/microsoft/phi-3cookbook/stargazers/?WT.mc_id=aiml-137032-kinfeylo)

[![Azure AI Community Discord](https://dcbadge.vercel.app/api/server/ByRwuEEgH4)](https://discord.com/invite/ByRwuEEgH4?WT.mc_id=aiml-137032-kinfeylo)

Phiは、Microsoftが開発したオープンなAIモデルのファミリーです。Phiモデルは、同じサイズやそれ以上のサイズのモデルを凌駕する最も高性能でコスト効率の良い小型言語モデル（SLM）です。Phi-3ファミリーには、mini、small、medium、visionバージョンがあり、異なるパラメータ量に基づいてトレーニングされ、さまざまなアプリケーションシナリオに対応します。MicrosoftのPhiファミリーについての詳細は、[Welcome to the Phi Family](/md/01.Introduce/Phi3Family.md)ページをご覧ください。

![Phi3Family](/imgs/00/Phi3getstarted.png)

## 目次

- はじめに
  - [環境のセットアップ](./md/01.Introduce/EnvironmentSetup.md)(✅)
  - [Phiファミリーへようこそ](./md/01.Introduce/Phi3Family.md)(✅)
  - [主要技術の理解](./md/01.Introduce/Understandingtech.md)(✅)
  - [PhiモデルのAI安全性](./md/01.Introduce/AISafety.md)(✅)
  - [Phi-3ハードウェアサポート](./md/01.Introduce/Hardwaresupport.md)(✅)
  - [Phi-3モデルとプラットフォーム間の利用可能性](./md/01.Introduce/Edgeandcloud.md)(✅)
  - [Guidance-aiとPhiの使用](./md/01.Introduce/Guidance.md)(✅)

- クイックスタート
  - [GitHubモデルカタログでPhi-3を使用する](./md/02.QuickStart/GitHubModel_QuickStart.md)(✅)
  - [Hugging faceでPhi-3を使用する](./md/02.QuickStart/Huggingface_QuickStart.md)(✅)
  - [OpenAI SDKでPhi-3を使用する](./md/02.QuickStart/OpenAISDK_Quickstart.md)(✅)
  - [HttpリクエストでPhi-3を使用する](./md/02.QuickStart/HttpAPI_QuickStart.md)(✅)
  - [Azure AI StudioでPhi-3を使用する](./md/02.QuickStart/AzureAIStudio_QuickStart.md)(✅)
  - [Azure MaaSまたはMaaPでPhi-3モデル推論を使用する](./md/02.QuickStart/AzureModel_Inference.md)(✅)
  - [Azure AI StudioでサーバーレスAPIとしてPhi-3モデルをデプロイする](./md/02.QuickStart/AzureAIStudio_MaaS.md)(✅)
  - [OllamaでPhi-3を使用する](./md/02.QuickStart/Ollama_QuickStart.md)(✅)
  - [LM StudioでPhi-3を使用する](./md/02.QuickStart/LMStudio_QuickStart.md)(✅)
  - [AI Toolkit VSCodeでPhi-3を使用する](./md/02.QuickStart/AITookit_QuickStart.md)(✅)
  - [Phi-3とLiteLLMを使用する](./md/02.QuickStart/LiteLLM_QuickStart.md)(✅)
- [Inference Phi-3](./md/03.Inference/overview.md)  
  - [Inference Phi-3 in iOS](./md/03.Inference/iOS_Inference.md)(✅)
  - [Inference Phi-3 in Jetson](./md/03.Inference/Jetson_Inference.md)(✅)
  - [Inference Phi-3 in AI PC](./md/03.Inference/AIPC_Inference.md)(✅)
  - [Inference Phi-3 with Apple MLX Framework](./md/03.Inference/MLX_Inference.md)(✅)
  - [Inference Phi-3 in Local Server](./md/03.Inference/Local_Server_Inference.md)(✅)
  - [Inference Phi-3 in Remote Server using AI Toolkit](./md/03.Inference/Remote_Interence.md)(✅)
  - [Inference Phi-3 with Rust](./md/03.Inference/Rust_Inference.md)(✅)
  - [Inference Phi-3-Vision in Local](./md/03.Inference/Vision_Inference.md)(✅)
  - [Inference Phi-3 with Kaito AKS, Azure Containers(official support)](./md/03.Inference/Kaito_Inference.md)(✅)
  - [Inference Your Fine-tuning ONNX Runtime Model](./md/06.E2ESamples/E2E_Inference_ORT.md)(✅)

- Phi-3のファインチューニング
  - [サンプルデータセットのダウンロードと作成](./md/04.Fine-tuning/CreatingSampleData.md)(✅)
  - [ファインチューニングのシナリオ](./md/04.Fine-tuning/FineTuning_Scenarios.md)(✅)
  - [ファインチューニング vs RAG](./md/04.Fine-tuning/FineTuning_vs_RAG.md)(✅)
  - [Phi-3を業界のエキスパートにするファインチューニング](./md/04.Fine-tuning/LetPhi3gotoIndustriy.md)(✅)
  - [VS Code用AIツールキットでのPhi-3のファインチューニング](./md/04.Fine-tuning/Finetuning_VSCodeaitoolkit.md)(✅)
  - [Azure Machine Learning ServiceでのPhi-3のファインチューニング](./md/04.Fine-tuning/Introduce_AzureML.md)(✅)
  - [Loraを使ったPhi-3のファインチューニング](./md/04.Fine-tuning/FineTuning_Lora.md)(✅)
  - [QLoraを使ったPhi-3のファインチューニング](./md/04.Fine-tuning/FineTuning_Qlora.md)(✅)
  - [Azure AI StudioでのPhi-3のファインチューニング](./md/04.Fine-tuning/FineTuning_AIStudio.md)(✅)
  - [Azure ML CLI/SDKでのPhi-3のファインチューニング](./md/04.Fine-tuning/FineTuning_MLSDK.md)(✅)
  - [Microsoft Oliveでのファインチューニング](./md/04.Fine-tuning/FineTuning_MicrosoftOlive.md)(✅)
  - [Weights and Biasを使ったPhi-3-visionのファインチューニング](./md/04.Fine-tuning/FineTuning_Phi-3-visionWandB.md)(✅)
  - [Apple MLX FrameworkでのPhi-3のファインチューニング](./md/04.Fine-tuning/FineTuning_MLX.md)(✅)
  - [Phi-3-visionのファインチューニング (公式サポート)](./md/04.Fine-tuning/FineTuning_Vision.md)(✅)
  - [Kaito AKS, Azure ContainersでのPhi-3のファインチューニング (公式サポート)](./md/04.Fine-tuning/FineTuning_Kaito.md)(✅)

- Phi-3の評価
  - [責任あるAIの紹介](./md/05.Evaluation/ResponsibleAI.md)(✅)
  - [Promptflowの紹介](./md/05.Evaluation/Promptflow.md)(✅)
  - [評価のためのAzure AI Studioの紹介](./md/05.Evaluation/AzureAIStudio.md)(✅)

- Phi-3-miniのE2Eサンプル
  - [エンドツーエンドサンプルの紹介](./md/06.E2ESamples/E2E_Introduction.md)(✅)
- [業界データの準備](./md/06.E2ESamples/E2E_Datasets.md)(✅)
  - [Microsoft Oliveを使ってプロジェクトを設計](./md/06.E2ESamples/E2E_LoRA&QLoRA_Config_With_Olive.md)(✅)
  - [Phi-3、ONNXRuntime Mobile、ONNXRuntime Generate APIを使ったAndroid上のローカルチャットボット](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/mobile/examples/phi-3/android)(✅)
  - [Hugging Face Space WebGPUとPhi-3-miniデモ - Phi-3-miniはプライベートで強力なチャットボット体験を提供します。試してみてください](https://huggingface.co/spaces/Xenova/experimental-phi3-webgpu)(✅)
  - [Phi3、ONNX Runtime Web、WebGPUを使ったブラウザ上のローカルチャットボット](https://github.com/microsoft/onnxruntime-inference-examples/tree/main/js/chat)(✅)
  - [OpenVinoチャット](/md/06.E2ESamples/E2E_OpenVino_Chat.md)(✅)
  - [マルチモデル - インタラクティブなPhi-3-miniとOpenAI Whisper](./md/06.E2ESamples/E2E_Phi-3-mini_with_whisper.md)(✅)
  - [MLFlow - ラッパーを作成し、Phi-3をMLFlowで使用](./md/06.E2ESamples/E2E_Phi-3-MLflow.md)(✅)
  - [モデル最適化 - ONNX Runtime Web用にPhi-3-minモデルをOliveで最適化する方法](https://github.com/microsoft/Olive/tree/main/examples/phi3)(✅)
  - [Phi-3 mini-4k-instruct-onnxを使ったWinUI3アプリ](https://github.com/microsoft/Phi3-Chat-WinUI3-Sample/)(✅)
  - [WinUI3マルチモデルAIパワードノーツアプリサンプル](https://github.com/microsoft/ai-powered-notes-winui3-sample)(✅)
  - [Prompt flowでカスタムPhi-3モデルを微調整し統合](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration.md)(✅)
  - [Azure AI StudioでPrompt flowを使ってカスタムPhi-3モデルを微調整し統合](./md/06.E2ESamples/E2E_Phi-3-FineTuning_PromptFlow_Integration_AIstudio.md)(✅)
  - [Phi-3.5-mini-instruct言語予測サンプル（中国語/英語）](../../code/09.UpdateSamples/Aug/phi3-instruct-demo.ipynb)(✅)

- Phi-3-visionのE2Eサンプル
  - [Phi-3-vision-画像テキストからテキスト](../../code/06.E2E/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)(✅)
  - [Phi-3-vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [Phi-3-vision CLIP埋め込み](./md/06.E2ESamples/E2E_Phi-3-Embedding_Images_with_CLIPVision.md)(✅)
  - [デモ: Phi-3リサイクル](https://github.com/jennifermarsman/PhiRecycling/)(✅)
  - [Phi-3-vision - Phi3-VisionとOpenVINOを使ったビジュアル言語アシスタント](https://docs.openvino.ai/nightly/notebooks/phi-3-vision-with-output.html)(✅)
  - [Phi-3 Vision Nvidia NIM](/md/06.E2ESamples/E2E_Nvidia_NIM_Vision.md)(✅)
  - [Phi-3 Vision OpenVino](/md/06.E2ESamples/E2E_OpenVino_Phi3Vision.md)(✅)
  - [Phi-3.5 Visionマルチフレームまたはマルチ画像サンプル](../../code/09.UpdateSamples/Aug/phi3-vision-demo.ipynb)(✅)

- Phi-3.5-MoEのE2Eサンプル
  - [Phi-3.5エキスパートモデル（MoEs）ソーシャルメディアサンプル](../../code/09.UpdateSamples/Aug/phi3_moe_demo.ipynb)(✅)
  - [NVIDIA NIM Phi-3 MOE、Azure AI Search、LlamaIndexを使ったリトリーバル強化生成（RAG）パイプラインの構築](https://github.com/farzad528/azure-ai-search-python-playground/blob/main/azure-ai-search-nvidia-rag.ipynb)(✅)

- Phi-3のラボとワークショップサンプル
  - [C# .NETラボ](./md/07.Labs/Csharp/csharplabs.md)(✅)
  - [Microsoft Phi-3ファミリーを使って自分のVisual Studio Code GitHub Copilotチャットを作成](./md/07.Labs/VSCode/README.md)(✅)
  - [ローカルRAGファイルを使ったローカルWebGPU Phi-3 Mini RAGチャットボットサンプル](./code/08.RAG/rag_webgpu_chat/README.md)(✅)
  - [Phi-3 ONNXチュートリアル](https://onnxruntime.ai/docs/genai/tutorials/phi3-python.html)(✅)
  - [Phi-3-vision ONNXチュートリアル](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
  - [ONNX Runtime generate() APIを使ってPhi-3モデルを実行](https://github.com/microsoft/onnxruntime-genai/blob/main/examples/python/phi-3-tutorial.md)(✅)
- [Phi-3 ONNX マルチモデル LLM チャット UI、これはチャットデモです](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/chat_app)(✅)
  - [C# Hello Phi-3 ONNX 例 Phi-3](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi)(✅)
  - [C# API Phi-3 ONNX 例 Phi3-Vision をサポート](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi3V)(✅)
  - [CodeSpace で C# Phi-3 サンプルを実行](./md/07.Labs/CsharpOllamaCodeSpaces/CsharpOllamaCodeSpaces.md)(✅)
  - [Promptflow と Azure AI Search を使って Phi-3 を利用](./code/07.Lab/RAG_with_PromptFlow_and_AISearch/README.md)(✅)
  - [Windows Copilot Library を使用した Windows AI-PC API](https://developer.microsoft.com/windows/ai/?WT.mc_id=aiml-137032-kinfeylo)

- Phi-3.5 の学習
  - [Phi-3.5 ファミリーの新機能](./md/08.Update/Phi35/010.WhatsNewInPhi35.md)(✅)
  - [Phi-3.5 ファミリーの量子化](./md/08.Update/Phi35/020.QuantifyingPhi35.md)(✅)
    - [llama.cpp を使って Phi-3.5 を量子化](./md/08.Update/Phi35/021.UsingLlamacppQuantifyingPhi35.md)(✅)
    - [onnxruntime の生成 AI 拡張を使って Phi-3.5 を量子化](./md/08.Update/Phi35/022.UsingORTGenAIQuantifyingPhi35.md)(✅)
    - [Intel OpenVINO を使って Phi-3.5 を量子化](./md/08.Update/Phi35/023.UsingIntelOpenVINOQuantifyingPhi35.md)(✅)
    - [Apple MLX Framework を使って Phi-3.5 を量子化](./md/08.Update/Phi35/024.UsingAppleMLXQuantifyingPhi35.md)(✅)
  - Phi-3.5 アプリケーションサンプル
    - [Phi-3.5-Instruct WebGPU RAG チャットボット](./md/08.Update/Phi35/031.WebGPUWithPhi35Readme.md)(✅)
    - [GitHub Models を使って Visual Studio Code チャット Copilot エージェントを作成](./md/08.Update/Phi35/032.CreateVSCodeChatAgentWithGitHubModels.md)(✅)


## Phi-3 モデルの使用

### Azure AI Studio での Phi-3

Microsoft Phi-3 の使い方や、さまざまなハードウェアデバイスでの E2E ソリューションの構築方法を学ぶことができます。Phi-3 を体験するには、[Azure AI Studio, Azure AI Model Catalog](https://aka.ms/phi3-azure-ai) を使用して、モデルを試し、シナリオに合わせてカスタマイズしてください。詳細は [Azure AI Studio](/md/02.QuickStart/AzureAIStudio_QuickStart.md) の使い方をご覧ください。

**プレイグラウンド**
各モデルには、[Azure AI Playground](https://aka.ms/try-phi3) でモデルをテストする専用のプレイグラウンドがあります。

### GitHub Models での Phi-3

Microsoft Phi-3 の使い方や、さまざまなハードウェアデバイスでの E2E ソリューションの構築方法を学ぶことができます。Phi-3 を体験するには、[GitHub Model Catalog](https://github.com/marketplace/models?WT.mc_id=aiml-137032-kinfeylo) を使用して、モデルを試し、シナリオに合わせてカスタマイズしてください。詳細は [GitHub Model Catalog](/md/02.QuickStart/GitHubModel_QuickStart.md) の使い方をご覧ください。

**プレイグラウンド**
各モデルには、モデルをテストする専用の[プレイグラウンド](/md/02.QuickStart/GitHubModel_QuickStart.md)があります。

### Hugging Face での Phi-3

モデルは [Hugging Face](https://huggingface.co/microsoft) でも見つけることができます。

**プレイグラウンド**
 [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)

## 🌐 多言語サポート

> **Note:**
> これらの翻訳はオープンソースの [co-op-translator](https://github.com/Azure/co-op-translator) を使用して自動生成されたものであり、誤りや不正確さが含まれている可能性があります。重要な情報については、原文を参照するか、専門の翻訳者に相談することをお勧めします。翻訳を追加または更新したい場合は、[co-op-translator](https://github.com/Azure/co-op-translator) リポジトリを参照してください。簡単なコマンドで貢献できます。

| 言語                 | コード | 翻訳された README へのリンク                           | 最終更新日    |
|----------------------|------|---------------------------------------------------------|--------------|
| 中国語 (簡体字)      | zh   | [中国語の翻訳](../zh/README.md)             | 2024-09-21   |
| フランス語           | fr   | [フランス語の翻訳](../fr/README.md)         | 2024-09-21   |
| 日本語               | ja   | [日本語の翻訳](./README.md)             | 2024-09-21   |
| 韓国語               | ko   | [韓国語の翻訳](../ko/README.md)             | 2024-09-21   |
| スペイン語           | es   | [スペイン語の翻訳](../es/README.md)         | 2024-09-21   |
 
## 商標

このプロジェクトには、プロジェクト、製品、またはサービスの商標やロゴが含まれている場合があります。Microsoft の商標やロゴの許可された使用は、[Microsoft の商標およびブランド ガイドライン](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general) に従う必要があります。
このプロジェクトの修正版で Microsoft の商標やロゴを使用する場合、混乱を招いたり、Microsoft の後援を示唆したりしないようにする必要があります。第三者の商標やロゴの使用は、それぞれの第三者のポリシーに従う必要があります。

免責事項: 翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない可能性があります。
出力を確認し、必要な修正を行ってください。