# **Apple MLXフレームワークでPhi-3を推論する**

## **MLXフレームワークとは**

MLXは、Appleシリコン上での機械学習研究のための配列フレームワークで、Appleの機械学習研究チームによって提供されています。

MLXは、機械学習研究者によって設計され、研究者向けに作られています。このフレームワークは使いやすさを重視しながらも、モデルのトレーニングやデプロイを効率的に行えるよう設計されています。また、フレームワーク自体の設計も概念的にシンプルで、研究者がMLXを拡張したり改良したりしやすいよう工夫されています。新しいアイデアを迅速に探求することを目指しています。

LLMはMLXを使用してAppleシリコンデバイスで高速化でき、モデルをローカルで非常に便利に実行できます。

## **MLXを使用してPhi-3-miniを推論する**

### **1. MLX環境をセットアップする**

1. Python 3.11.x  
2. MLXライブラリをインストールする  

```bash

pip install mlx-lm

```

### **2. MLXを使ってターミナルでPhi-3-miniを実行する**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

結果（私の環境はApple M1 Max、64GB）は以下の通りです：

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.ja.png)

### **3. ターミナルでMLXを使ってPhi-3-miniを量子化する**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***注意：*** モデルはmlx_lm.convertを使用して量子化可能で、デフォルトの量子化はINT4です。この例ではPhi-3-miniをINT4に量子化しています。

モデルはmlx_lm.convertを使って量子化することができ、デフォルトではINT4に量子化されます。この例ではPhi-3-miniをINT4に量子化しています。量子化後、モデルはデフォルトディレクトリ ./mlx_model に保存されます。

量子化したモデルをターミナルからMLXを使ってテストできます。

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

結果は以下の通りです：

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.ja.png)

### **4. Jupyter NotebookでMLXを使ってPhi-3-miniを実行する**

![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.ja.png)

***注意：*** このサンプルをご覧ください [こちらをクリック](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **リソース**

1. Apple MLXフレームワークについて学ぶ [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHubリポジトリ [https://github.com/ml-explore](https://github.com/ml-explore)

**免責事項**:  
本書類は、機械翻訳AIサービスを使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確な表現が含まれる可能性があります。原文（元の言語の文書）が正式かつ信頼できる情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の利用によって生じる誤解や誤った解釈について、当方は一切の責任を負いません。