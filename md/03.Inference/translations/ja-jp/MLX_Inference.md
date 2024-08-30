# **Apple MLXフレームワークでPhi-3を推論する**

## **MLXフレームワークとは**

MLXは、Appleの機械学習研究チームが提供する、Appleシリコン上での機械学習研究のための配列フレームワークです。

MLXは、機械学習研究者によって設計され、機械学習研究者のために設計されています。このフレームワークはユーザーフレンドリーでありながら、モデルのトレーニングとデプロイメントにおいても効率的です。フレームワーク自体の設計も概念的にシンプルです。新しいアイデアを迅速に探求するために、研究者がMLXを簡単に拡張および改善できるようにすることを目指しています。

LLMは、MLXを通じてAppleシリコンデバイスで加速され、モデルは非常に便利にローカルで実行できます。

## **MLXを使用してPhi-3-miniを推論する**

### **1. MLX環境を設定する**

1. Python 3.11.x
2. MLXライブラリをインストールする

```bash

pip install mlx-lm

```

### **2. ターミナルでMLXを使用してPhi-3-miniを実行する**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

結果（私の環境はApple M1 Max,64GB）は次のとおりです

![Terminal](../../imgs/03/MLX/01.png)

### **3. ターミナルでMLXを使用してPhi-3-miniを量子化する**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***注意：*** モデルはmlx_lm.convertを介して量子化でき、デフォルトの量子化はINT4です。この例では、Phi-3-miniをINT4に量子化します

モデルはmlx_lm.convertを介して量子化でき、デフォルトの量子化はINT4です。この例では、Phi-3-miniをINT4に量子化します。量子化後、デフォルトのディレクトリ./mlx_modelに保存されます。

ターミナルからMLXを使用して量子化されたモデルをテストできます

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

結果は次のとおりです

![INT4](../../imgs/03/MLX/02.png)

### **4. Jupyter NotebookでMLXを使用してPhi-3-miniを実行する**

![Notebook](../../imgs/03/MLX/03.png)

***注意:*** このサンプルを参照してください [このリンクをクリック](../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **リソース**

1. Apple MLXフレームワークについて学ぶ [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. Apple MLX GitHubリポジトリ [https://github.com/ml-explore](https://github.com/ml-explore)
