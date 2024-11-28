## ファインチューニングのシナリオ

![FineTuning with MS Services](../../../../translated_images/FinetuningwithMS.921fa8c240611562e7c4a5ceb7eca04f458ad6f3c899d5a0dc120030398d9e08.ja.png)

**プラットフォーム** これには、Azure AI Foundry、Azure Machine Learning、AI Tools、Kaito、ONNX Runtimeなどのさまざまな技術が含まれます。

**インフラストラクチャ** これには、ファインチューニングプロセスに不可欠なCPUとFPGAが含まれます。これらの技術のアイコンをお見せします。

**ツール & フレームワーク** これには、ONNX RuntimeとONNX Runtimeが含まれます。これらの技術のアイコンをお見せします。
[Insert icons for ONNX Runtime and ONNX Runtime]

Microsoftの技術を使用したファインチューニングプロセスには、さまざまなコンポーネントとツールが含まれます。これらの技術を理解し、活用することで、アプリケーションを効果的にファインチューニングし、より良いソリューションを作成することができます。

## サービスとしてのモデル

ホストされたファインチューニングを使用して、計算リソースを作成および管理する必要なくモデルをファインチューニングします。

![MaaS Fine Tuning](../../../../translated_images/MaaSfinetune.1678f33544c36b9016d8c018ce9c4c1622fb3bc2d72751291c39813f88bce052.ja.png)

サーバーレスファインチューニングは、Phi-3-miniおよびPhi-3-mediumモデルに利用可能であり、開発者がクラウドおよびエッジシナリオに合わせてモデルを迅速かつ簡単にカスタマイズできるようにします。また、Phi-3-smallがModels-as-a-Serviceオファリングを通じて利用可能になったことを発表しました。これにより、開発者は基盤となるインフラストラクチャを管理することなく、AI開発を迅速かつ簡単に開始できます。

[Fine Tuning Sample](https://github.com/microsoft/Phi-3CookBook/blob/main/md/04.Fine-tuning/FineTuning_AIStudio.md)

## プラットフォームとしてのモデル

ユーザーは自分の計算リソースを管理して、モデルをファインチューニングします。

![Maap Fine Tuning](../../../../translated_images/MaaPFinetune.f88828d32d16ced1198525fceed9184ce17516f5c1a404c264d87a4ca816947f.ja.png)

[Fine Tuning Sample](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## ファインチューニングのシナリオ

| | | | | | | |
|-|-|-|-|-|-|-|
|シナリオ|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|事前学習されたLLMを特定のタスクやドメインに適応させる|Yes|Yes|Yes|Yes|Yes|Yes|
|テキスト分類、固有表現抽出、機械翻訳などのNLPタスクのためのファインチューニング|Yes|Yes|Yes|Yes|Yes|Yes|
|QAタスクのためのファインチューニング|Yes|Yes|Yes|Yes|Yes|Yes|
|チャットボットで人間のような応答を生成するためのファインチューニング|Yes|Yes|Yes|Yes|Yes|Yes|
|音楽、アート、その他の創造的な形態を生成するためのファインチューニング|Yes|Yes|Yes|Yes|Yes|Yes|
|計算および財務コストの削減|Yes|Yes|No|Yes|Yes|No|
|メモリ使用量の削減|No|Yes|No|Yes|Yes|Yes|
|効率的なファインチューニングのために少ないパラメーターを使用|No|Yes|Yes|No|No|Yes|
|利用可能なすべてのGPUデバイスの集約GPUメモリにアクセスできるメモリ効率の良いデータ並列化|No|No|No|Yes|Yes|Yes|

## ファインチューニングのパフォーマンス例

![Finetuning Performance](../../../../translated_images/Finetuningexamples.88bad3a5350927b08b1f06e4bced95cfd3715caa933d21c9ff658dcf0db94f73.ja.png)

**免責事項**:
この文書は、機械翻訳AIサービスを使用して翻訳されています。正確さを期すために努力していますが、自動翻訳には誤りや不正確さが含まれる可能性があります。元の言語の文書が権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤訳について、当社は一切の責任を負いません。