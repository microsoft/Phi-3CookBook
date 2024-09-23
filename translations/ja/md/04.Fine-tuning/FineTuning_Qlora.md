**Phi-3のQLoRAによるファインチューニング**

MicrosoftのPhi-3 Mini言語モデルを[QLoRA (Quantum Low-Rank Adaptation)](https://github.com/artidoro/qlora)を使ってファインチューニングします。

QLoRAは、会話の理解と応答生成の向上に役立ちます。

transformersとbitsandbytesを使用して4ビットでモデルをロードするには、accelerateとtransformersをソースからインストールし、最新バージョンのbitsandbytesライブラリを確保する必要があります。

**サンプル**
- [このサンプルノートブックで詳細を学ぶ](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Pythonファインチューニングサンプルの例](../../../../code/04.Finetuning/FineTrainingScript.py)
- [LORAを使ったHugging Face Hubファインチューニングの例](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [QLORAを使ったHugging Face Hubファインチューニングの例](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

免責事項: この翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない可能性があります。
出力を確認し、必要に応じて修正を加えてください。