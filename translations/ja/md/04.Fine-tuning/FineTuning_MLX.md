# **Apple MLXフレームワークでPhi-3をファインチューニング**

Apple MLXフレームワークのコマンドラインを使用して、Loraと組み合わせたファインチューニングを行うことができます。（MLXフレームワークの操作について詳しく知りたい方は、[Inference Phi-3 with Apple MLX Framework](../03.Inference/MLX_Inference.md)をご覧ください）


## **1. データ準備**

デフォルトでは、MLXフレームワークはtrain、test、およびevalのjsonl形式を必要とし、Loraと組み合わせてファインチューニングジョブを完了します。


### ***注意:***

1. jsonlデータ形式：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. 例として[TruthfulQAのデータ](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)を使用していますが、データ量が比較的少ないため、ファインチューニングの結果が必ずしも最良とは限りません。各自のシナリオに基づいて、より良いデータを使用することをお勧めします。

3. データ形式はPhi-3テンプレートと組み合わせます

この[リンク](../../../../code/04.Finetuning/mlx)からデータをダウンロードしてください。***data***フォルダにすべての.jsonlファイルを含めてください。


## **2. ターミナルでファインチューニング**

以下のコマンドをターミナルで実行してください


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***注意:***

1. これはLoRAファインチューニングであり、MLXフレームワークはQLoRAを公開していません

2. config.yamlを設定して、以下のようにいくつかの引数を変更できます


```yaml


# ローカルモデルディレクトリまたはHugging Faceリポジトリへのパス
model: "microsoft/Phi-3-mini-4k-instruct"
# トレーニングを行うかどうか（ブール値）
train: true

# {train, valid, test}.jsonlファイルがあるディレクトリ
data: "data"

# PRNGシード
seed: 0

# ファインチューニングするレイヤーの数
lora_layers: 32

# ミニバッチサイズ
batch_size: 1

# トレーニングの反復回数
iters: 1000

# 検証バッチの数、-1は検証セット全体を使用
val_batches: 25

# Adam学習率
learning_rate: 1e-6

# 損失報告の間のトレーニングステップ数
steps_per_report: 10

# 検証の間のトレーニングステップ数
steps_per_eval: 200

# 指定されたアダプタウェイトでトレーニングを再開するためのロードパス
resume_adapter_file: null

# トレーニングされたアダプタウェイトの保存/ロードパス
adapter_path: "adapters"

# N回の反復ごとにモデルを保存
save_every: 1000

# トレーニング後にテストセットで評価
test: false

# テストセットバッチの数、-1はテストセット全体を使用
test_batches: 100

# 最大シーケンス長
max_seq_length: 2048

# メモリ使用量を減らすための勾配チェックポイントの使用
grad_checkpoint: true

# LoRAパラメータはconfigファイルでのみ指定可能
lora_parameters:
  # LoRAを適用するレイヤーキー
  # これらは最後のlora_layersに適用されます
  keys: ["o_proj","qkv_proj"]
  rank: 64
  alpha: 64
  dropout: 0.1


```

以下のコマンドをターミナルで実行してください


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. ファインチューニングアダプタのテスト**

ターミナルでファインチューニングアダプタを実行できます。このように


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

そして、元のモデルを実行して結果を比較します


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

ファインチューニングの結果と元のモデルの結果を比較してみてください


## **4. アダプタをマージして新しいモデルを生成**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. ollamaを使用して量子化されたファインチューニングモデルを実行**

使用前に、llama.cpp環境を設定してください


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***注意:*** 

1. 現在、fp32、fp16、およびINT 8の量子化変換をサポートしています

2. マージされたモデルにはtokenizer.modelが欠けています。https://huggingface.co/microsoft/Phi-3-mini-4k-instruct からダウンロードしてください

Ollmaモデルファイルを設定（ollamaがインストールされていない場合は、[Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md)をご覧ください）


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

ターミナルで以下のコマンドを実行


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

おめでとうございます！MLXフレームワークでファインチューニングをマスターしました

免責事項: この翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない可能性があります。
出力を確認し、必要に応じて修正を行ってください。