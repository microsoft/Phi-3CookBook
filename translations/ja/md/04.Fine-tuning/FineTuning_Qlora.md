**Phi-3をQLoRAでファインチューニングする**

MicrosoftのPhi-3 Mini言語モデルを[QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora)を使用してファインチューニングします。

QLoRAは、会話の理解と応答生成の向上に役立ちます。

transformersとbitsandbytesを使用して4ビットでモデルをロードするには、accelerateとtransformersをソースからインストールし、最新バージョンのbitsandbytesライブラリを持っていることを確認する必要があります。

**サンプル**
- [このサンプルノートブックで詳細を学ぶ](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Pythonファインチューニングサンプルの例](../../../../code/04.Finetuning/FineTrainingScript.py)
- [LORAを使用したHugging Face Hubのファインチューニングの例](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [QLORAを使用したHugging Face Hubのファインチューニングの例](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免責事項**:
この文書は機械翻訳AIサービスを使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知おきください。権威ある情報源としては、元の言語の文書を参照してください。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤解釈については、一切の責任を負いかねます。