**Phi-3をQLoRAでファインチューニングする**

MicrosoftのPhi-3 Mini言語モデルを[QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora)を使用してファインチューニングします。

QLoRAを使用することで、会話の理解力や応答生成能力を向上させることができます。

transformersとbitsandbytesを使用してモデルを4ビットで読み込むには、accelerateとtransformersをソースからインストールし、bitsandbytesライブラリの最新バージョンを使用していることを確認してください。

**サンプル**
- [このサンプルノートブックでさらに学ぶ](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Pythonによるファインチューニングのサンプル](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Hugging Face HubでのLORAを使用したファインチューニング例](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face HubでのQLORAを使用したファインチューニング例](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳にはエラーや不正確な部分が含まれる可能性があります。元の言語で作成された原文が正式な情報源として優先されるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の使用により生じた誤解や誤った解釈について、当方は一切の責任を負いません。