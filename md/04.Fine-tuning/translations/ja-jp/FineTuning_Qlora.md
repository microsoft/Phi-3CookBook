**QLoRAを使用してPhi-3をファインチューニングする**

[QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora)を使用してMicrosoftのPhi-3 Mini言語モデルをファインチューニングします。

QLoRAは、会話の理解と応答生成を向上させるのに役立ちます。

transformersとbitsandbytesを使用して4ビットでモデルをロードするには、accelerateとtransformersをソースからインストールし、最新バージョンのbitsandbytesライブラリを持っていることを確認する必要があります。

**サンプル**
- [このサンプルノートブックで詳細を学ぶ](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Pythonファインチューニングサンプルの例](../../../../code/04.Finetuning/FineTrainingScript.py)
- [Hugging Face HubでのLoRAを使用したファインチューニングの例](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Hugging Face HubでのQLoRAを使用したファインチューニングの例](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)
