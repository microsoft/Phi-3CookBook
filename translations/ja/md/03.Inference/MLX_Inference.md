# **Apple MLX フレームワークで Phi-3 を推論する**

## **MLX フレームワークとは**

MLX は、Apple シリコン上での機械学習研究のためのフレームワークで、Apple の機械学習研究チームによって提供されています。

MLX は、機械学習研究者によって設計され、機械学習研究者のために作られています。このフレームワークは使いやすさを重視しながらも、モデルのトレーニングやデプロイを効率的に行えるように設計されています。また、フレームワーク自体の設計も概念的にシンプルです。研究者が新しいアイデアを迅速に探求できるよう、MLX を簡単に拡張・改善できるようにすることを目指しています。

LLM は MLX を通じて Apple シリコンデバイスで加速され、モデルはローカルで非常に便利に実行できます。

## **MLX を使って Phi-3-mini を推論する**

### **1. MLX 環境をセットアップする**

1. Python 3.11.x
2. MLX ライブラリをインストール


```bash

pip install mlx-lm

```

### **2. MLX で Terminal から Phi-3-mini を実行する**


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

結果（私の環境は Apple M1 Max, 64GB）は次の通りです

![Terminal](../../../../translated_images/01.5cb5f10f82619d0a98bc3584bf81264105a33d9d8559f125418a93b8d7527728.ja.png)

### **3. Terminal で MLX を使って Phi-3-mini を量子化する**


```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***Note：*** モデルは mlx_lm.convert を通じて量子化でき、デフォルトの量子化は INT4 です。この例では Phi-3-mini を INT4 に量子化します

モデルは mlx_lm.convert を通じて量子化でき、デフォルトの量子化は INT4 です。この例では Phi-3-mini を INT4 に量子化します。量子化後、デフォルトのディレクトリ ./mlx_model に保存されます

Terminal から MLX で量子化されたモデルをテストできます


```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

結果は次の通りです

![INT4](../../../../translated_images/02.6ca278966b75435a31021b0a6f1f3b377102d7e59e7b90daf8f017c1a9876cb2.ja.png)


### **4. Jupyter Notebook で MLX を使って Phi-3-mini を実行する**


![Notebook](../../../../translated_images/03.5b701d4bfe17c5d20c075f7d4c8d1201b8073c8e8196b364a9a19cbe684dd26a.ja.png)

***Note:*** このサンプルを読むには [こちらのリンクをクリック](../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)


## **リソース**

1. Apple MLX フレームワークについて学ぶ [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHub リポジトリ [https://github.com/ml-explore](https://github.com/ml-explore)

免責事項: この翻訳はAIモデルによって元の言語から翻訳されたものであり、完璧ではない可能性があります。
出力内容を確認し、必要に応じて修正を加えてください。