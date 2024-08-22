# Microsoft Phi-3 Cookbookへようこそ

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

これは、Microsoft Phi-3ファミリーを使用する方法に関するクックブックです。

![Phi3Family](/imgs/00/Phi3getstarted.png)

Phi-3は、Microsoftが開発した一連のオープンAIモデルです。Phi-3モデルは、言語、推論、コーディング、数学のベンチマークで同じサイズおよび次のサイズのモデルを上回る、最も強力でコスト効果の高い小型言語モデル（SLM）です。

Phi-3-miniは、3.8Bの言語モデルで、[Microsoft Azure AI Studio](https://aka.ms/phi3-azure-ai)、[Hugging Face](https://huggingface.co/collections/microsoft/phi-3-6626e15e9585a200d2d761e3)、および[Ollama](https://ollama.com/library/phi3)で利用できます。Phi-3モデルは、主要なベンチマークで同じサイズおよび次のサイズの言語モデルを大幅に上回ります（以下のベンチマークデータを参照、数値が高いほど良い）。Phi-3-miniは、そのサイズの2倍のモデルを上回り、Phi-3-smallおよびPhi-3-mediumは、GPT-3.5Tを含むより大きなモデルを上回ります。

報告されたすべての数値は、比較可能な数値を確保するために同じプロセスを使用して生成されました。したがって、評価方法の微妙な違いにより、これらの数値は他の公開された数値と異なる場合があります。ベンチマークの詳細については、技術論文を参照してください。

Phi-3-smallは、7Bのパラメータで、言語、推論、コーディング、数学のベンチマークでGPT-3.5Tを上回ります。

![phimodelsmall](/imgs/00/phi3small.png)

Phi-3-mediumは、14Bのパラメータを持ち、この傾向を続け、Gemini 1.0 Proを上回ります。

![phimodelmedium](/imgs/00/phi3medium.png)

Phi-3-visionは、4.2Bのパラメータを持ち、この傾向を続け、一般的な視覚推論タスク、OCR、表およびグラフの理解タスクで、Claude-3 HaikuおよびGemini 1.0 Pro Vなどのより大きなモデルを上回ります。

![phimodelvision](/imgs/00/phi3vision.png)

注意: Phi-3モデルは、TriviaQAなどの事実知識ベンチマークでは、より小さなモデルほど優れていません。これは、モデルのサイズが小さいため、事実を保持する能力が制限されるためです。

Phi Silicaの導入を準備しています。これは、Phiファミリーのモデルに基づいて構築され、Copilot + PCのNPU用に設計されています。Windowsは、NPUおよび受信トレイに最適化された高度な小型言語モデル（SLM）を備えた最初のプラットフォームです。Phi Silica APIおよびOCR、Studio Effects、Live Captions、Recall User Activity APIは、6月にWindows Copilotライブラリで提供されます。Vector Embedding、RAG API、Text Summarizationなどの追加のAPIは、後日提供されます。

## Azure AI Studio

Microsoft Phi-3の使用方法と、さまざまなハードウェアデバイスでE2Eソリューションを構築する方法を学ぶことができます。Phi-3を体験するには、[Azure AI Studio, Azure AI Model Catalog](https://aka.ms/phi3-azure-ai)を使用して、シナリオに合わせてPhi-3をカスタマイズすることから始めてください。

**Playground**
各モデルには、モデルをテストするための専用のPlaygroundがあります [Azure AI Playground](https://aka.ms/try-phi3)。

## Hugging Face

このモデルは、[Hugging Face](https://huggingface.co/microsoft)でも見つけることができます。

**Playground**
 [Hugging Chat playground](https://huggingface.co/chat/models/microsoft/Phi-3-mini-4k-instruct)。

## 目次

このクックブックには以下が含まれます:

## **Microsoft Phi-3 Cookbook**

* [紹介]()
    * [環境の設定](../../md/01.Introduce/translations/ja-jp/EnvironmentSetup.md)(✅)
    * [Phi-3ファミリーへようこそ](../../md/01.Introduce/translations/ja-jp/Phi3Family.md)(✅)
    * [主要技術の理解](../../md/01.Introduce/translations/ja-jp/Understandingtech.md)(✅)
    * [Phi-3モデルのAI安全性](../../md/01.Introduce/translations/ja-jp/AISafety.md)(✅)
    * [Phi-3のハードウェアサポート](../../md/01.Introduce/translations/ja-jp/Hardwaresupport.md)(✅)
    * [Phi-3モデルとプラットフォーム間の可用性](../../md/01.Introduce/translations/ja-jp/Edgeandcloud.md)(✅)

* [クイックスタート]()
    * [Hugging faceでPhi-3を使用する](../../md/02.QuickStart/translations/ja-jp/Huggingface_QuickStart.md)(✅)
    * [Azure AI StudioでPhi-3を使用する](../../md/02.QuickStart/translations/ja-jp/AzureAIStudio_QuickStart.md)(✅)
    * [OllamaでPhi-3を使用する](../../md/02.QuickStart/translations/ja-jp/Ollama_QuickStart.md)(✅)
    * [LM StudioでPhi-3を使用する](../../md/02.QuickStart/translations/ja-jp/LMStudio_QuickStart.md)(✅)
    * [AI Toolkit VSCodeでPhi-3を使用する](../../md/02.QuickStart/translations/ja-jp/AITookit_QuickStart.md)(✅)

* [Phi-3推論](../../md/03.Inference/translations/ja-jp/overview.md)
    * [iOSでPhi-3を推論する](../../md/03.Inference/translations/ja-jp/iOS_Inference.md)(✅)
    * [JetsonでPhi-3を推論する](../../md/03.Inference/translations/ja-jp/Jetson_Inference.md)(✅)
    * [AI PCでPhi-3を推論する](../../md/03.Inference/translations/ja-jp/AIPC_Inference.md)(✅)
    * [Apple MLX FrameworkでPhi-3を推論する](../../md/03.Inference/translations/ja-jp/MLX_Inference.md)(✅)
    * [ローカルサーバーでPhi-3を推論する](../../md/03.Inference/translations/ja-jp/Local_Server_Inference.md)(✅)
    * [AI Toolkitを使用してリモートサーバーでPhi-3を推論する](../../md/03.Inference/translations/ja-jp/Remote_Interence.md)(✅)
    * [ローカルでPhi-3-Visionを推論する](../../md/03.Inference/translations/ja-jp/Vision_Inference.md)(✅)

* [Phi-3の微調整]()
    * [サンプルデータセットのダウンロードと作成](../../md/04.Fine-tuning/translations/ja-jp/CreatingSampleData.md)(✅)
    * [微調整シナリオ](../../md/04.Fine-tuning/translations/ja-jp/FineTuning_Scenarios.md)(✅)
    * [微調整 vs RAG](../../md/04.Fine-tuning/translations/ja-jp/FineTuning_vs_RAG.md)(✅)
    * [Phi-3を業界の専門家にする](../../md/04.Fine-tuning/translations/ja-jp/LetPhi3gotoIndustriy.md)(✅)
    * [VS CodeのAIツールキットを使用してPhi-3を微調整する](../../md/04.Fine-tuning/translations/ja-jp/Finetuning_VSCodeaitoolkit.md)(✅)
    * [Azure Machine Learning Serviceを使用してPhi-3を微調整する](../../md/04.Fine-tuning/translations/ja-jp/Introduce_AzureML.md)(✅)
    * [Loraを使用してPhi-3を微調整する](../../md/04.Fine-tuning/translations/ja-jp/FineTuning_Lora.md)(✅)
    * [QLoraを使用してPhi-3を微調整する](../../md/04.Fine-tuning/translations/ja-jp/FineTuning_Qlora.md)(✅)
    * [Azure AI Studioを使用してPhi-3を微調整する](../../md/04.Fine-tuning/translations/ja-jp/FineTuning_AIStudio.md)(✅)
    * [Azure ML CLI/SDKを使用してPhi-3を微調整する](../../md/04.Fine-tuning/translations/ja-jp/FineTuning_MLSDK.md)(✅)
    * [Microsoft Oliveを使用して微調整する](../../md/04.Fine-tuning/translations/ja-jp/FineTuning_MicrosoftOlive.md)(✅)
    * [Weights and Biasを使用してPhi-3-visionを微調整する](../../md/04.Fine-tuning/translations/ja-jp/FineTuning_Phi-3-visionWandB.md)(✅)
    * [Apple MLX Frameworkを使用してPhi-3を微調整する](../../md/04.Fine-tuning/translations/ja-jp/FineTuning_MLX.md)(✅)

* [Phi-3の評価]()
    * [責任あるAIの紹介](../../md/05.Evaluation/translations/ja-jp/ResponsibleAI.md)(✅)
    * [Promptflowの紹介](../../md/05.Evaluation/translations/ja-jp/Promptflow.md)(✅)
    * [Azure AI Studioの評価の紹介](../../md/05.Evaluation/translations/ja-jp/AzureAIStudio.md)(✅)

* [Phi-3-miniのエンドツーエンドのサンプル]()
    * [エンドツーエンドのサンプルの紹介](../../md/06.E2ESamples/translations/ja-jp/E2E_Introduction.md)(✅)
    * [業界データの準備](../../md/06.E2ESamples/translations/ja-jp/E2E_Datasets.md)(✅)
    * [Microsoft Oliveを使用してプロジェクトを設計する](../../md/06.E2ESamples/translations/ja-jp/E2E_LoRA&QLoRA_Config_With_Olive.md)(✅)
    * [微調整されたONNX Runtimeモデルを推論する](../../md/06.E2ESamples/translations/ja-jp/E2E_Inference_ORT.md)(✅)
    * [マルチモデル - インタラクティブPhi-3-miniとOpenAI Whisper](../../md/06.E2ESamples/translations/ja-jp/E2E_Phi-3-mini_with_whisper.md)(✅)
    * [MLFlow - ラッパーを構築し、Phi-3とMLFlowを使用する](../../md/06.E2ESamples/translations/ja-jp/E2E_Phi-3-MLflow.md)(✅)

* [Phi-3-visionのエンドツーエンドのサンプル]()
    * [Phi3-vision-画像テキストからテキストへ](../../md/06.E2ESamples/translations/ja-jp/E2E_Phi-3-vision-image-text-to-text-online-endpoint.ipynb)(✅)
    * [Phi-3-Vision-ONNX](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
    * [Phi-3-vision CLIP埋め込み](../../md/06.E2ESamples/translations/ja-jp/E2E_Phi-3-Embedding_Images_with_CLIPVision.md)(✅)

* [Phi-3の実験室とワークショップのサンプル]()
    * [C# .NET実験室](../../md/07.Labs/translations/ja-jp/Csharp/csharplabs.md)(✅)
    * [Microsoft Phi-3ファミリーを使用して独自のVisual Studio Code GitHub Copilot Chatを構築する](../../md/07.Labs/translations/ja-jp/VSCode/README.md)(✅)
    * [Phi-3 ONNXガイド](https://onnxruntime.ai/docs/genai/tutorials/phi3-python.html)(✅)
    * [Phi-3-vision ONNXガイド](https://onnxruntime.ai/docs/genai/tutorials/phi3-v.html)(✅)
    * [ONNX Runtime generate() APIを使用してPhi-3モデルを実行する](https://github.com/microsoft/onnxruntime-genai/blob/main/examples/python/phi-3-tutorial.md)(✅)
    * [Phi-3 ONNXマルチモデルLLMチャットUI、これはチャットデモです](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/chat_app)(✅)
    * [C# Hello Phi-3 ONNXサンプルPhi-3](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi)(✅)
    * [C# API Phi-3 ONNXサンプルPhi3-Visionをサポート](https://github.com/microsoft/onnxruntime-genai/tree/main/examples/csharp/HelloPhi3V)(✅)

## 商標

このプロジェクトには、プロジェクト、製品、またはサービスの商標またはロゴが含まれている場合があります。Microsoftの商標またはロゴの使用は、[Microsoftの商標およびブランドガイドライン](https://www.microsoft.com/legal/intellectualproperty/trademarks/usage/general)に従う必要があります。このプロジェクトの変更バージョンでMicrosoftの商標またはロゴを使用する場合、混乱を引き起こしたり、Microsoftのスポンサーシップを暗示したりしてはなりません。第三者の商標またはロゴの使用は、第三者のポリシーに従う必要があります。
