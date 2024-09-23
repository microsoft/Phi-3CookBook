## ファインチューニングシナリオ

![FineTuning with MS Services](../../../../translated_images/FinetuningwithMS.921fa8c240611562e7c4a5ceb7eca04f458ad6f3c899d5a0dc120030398d9e08.ja.png)

**プラットフォーム** これには、Azure AI Studio、Azure Machine Learning、AI Tools、Kaito、ONNX Runtimeなどのさまざまな技術が含まれます。

**インフラストラクチャ** これには、ファインチューニングプロセスに不可欠なCPUおよびFPGAが含まれます。これらの技術のアイコンをお見せします。

**ツール & フレームワーク** これにはONNX Runtimeが含まれます。これらの技術のアイコンをお見せします。
[Insert icons for ONNX Runtime and ONNX Runtime]

Microsoftの技術を使用したファインチューニングプロセスには、さまざまなコンポーネントとツールが含まれます。これらの技術を理解し活用することで、アプリケーションを効果的にファインチューニングし、より良いソリューションを作成することができます。

## モデル・アズ・サービス

ホストされたファインチューニングを使用して、コンピュートを作成および管理する必要なしにモデルをファインチューニングします。

![MaaS Fine Tuning](../../../../translated_images/MaaSfinetune.1678f33544c36b9016d8c018ce9c4c1622fb3bc2d72751291c39813f88bce052.ja.png)

サーバーレスファインチューニングはPhi-3-miniおよびPhi-3-mediumモデルで利用可能で、開発者はコンピュートを手配することなく、クラウドおよびエッジのシナリオに対してモデルを迅速かつ簡単にカスタマイズできます。また、Phi-3-smallがModels-as-a-Service提供を通じて利用可能になったことを発表しましたので、開発者は基盤となるインフラストラクチャを管理することなく、AI開発を迅速かつ簡単に開始できます。

[Fine Tuning Sample](https://github.com/microsoft/Phi-3CookBook/blob/main/md/04.Fine-tuning/FineTuning_AIStudio.md)
## モデル・アズ・プラットフォーム

ユーザーは自分のコンピュートを管理し、モデルをファインチューニングします。

![Maap Fine Tuning](../../../../translated_images/MaaPFinetune.f88828d32d16ced1198525fceed9184ce17516f5c1a404c264d87a4ca816947f.ja.png)

[Fine Tuning Sample](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/system/finetune/chat-completion/chat-completion.ipynb)

## ファインチューニングシナリオ

| | | | | | | |
|-|-|-|-|-|-|-|
|シナリオ|LoRA|QLoRA|PEFT|DeepSpeed|ZeRO|DORA|
|特定のタスクやドメインに合わせた事前トレーニング済みLLMの適応|Yes|Yes|Yes|Yes|Yes|Yes|
|テキスト分類、固有表現認識、機械翻訳などのNLPタスクのファインチューニング|Yes|Yes|Yes|Yes|Yes|Yes|
|QAタスクのファインチューニング|Yes|Yes|Yes|Yes|Yes|Yes|
|チャットボットでの人間らしい応答生成のファインチューニング|Yes|Yes|Yes|Yes|Yes|Yes|
|音楽、アート、その他の創造的な形態の生成のファインチューニング|Yes|Yes|Yes|Yes|Yes|Yes|
|計算および財政コストの削減|Yes|Yes|No|Yes|Yes|No|
|メモリ使用量の削減|No|Yes|No|Yes|Yes|Yes|
|効率的なファインチューニングのためのパラメータの削減|No|Yes|Yes|No|No|Yes|
|利用可能なすべてのGPUデバイスの総GPUメモリにアクセスできるメモリ効率の良いデータ並列化の形式|No|No|No|Yes|Yes|Yes|

## ファインチューニングパフォーマンス例

![Finetuning Performance](../../../../translated_images/Finetuningexamples.88bad3a5350927b08b1f06e4bced95cfd3715caa933d21c9ff658dcf0db94f73.ja.png)

