# **Apple MLXフレームワークでPhi-3をファインチューニング**

Apple MLXフレームワークのコマンドラインを使用して、Loraと組み合わせたファインチューニングを行うことができます。（MLXフレームワークの操作について詳しく知りたい場合は、[Inference Phi-3 with Apple MLX Framework](../03.Inference/MLX_Inference.md)をお読みください）


## **1. データ準備**

デフォルトでは、MLXフレームワークはtrain、test、およびevalのjsonl形式を必要とし、Loraと組み合わせてファインチューニングを完了します。


### ***注意:***

1. jsonlデータ形式 ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. 例として[TruthfulQAのデータ](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)を使用していますが、データ量が比較的少ないため、ファインチューニングの結果が必ずしも最良であるとは限りません。学習者は自分のシナリオに基づいてより良いデータを使用することをお勧めします。

3. データ形式はPhi-3テンプレートと組み合わせて使用します

この[リンク](../../../../code/04.Finetuning/mlx)からデータをダウンロードし、***data***フォルダ内のすべての.jsonlを含めてください


## **2. ターミナルでのファインチューニング**

ターミナルでこのコマンドを実行してください


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***注意:***

1. これはLoRAファインチューニングであり、MLXフレームワークはQLoRAを公開していません

2. config.yamlを設定して、一部の引数を変更することができます。例えば


```yaml


# The path to the local model directory or Hugging Face repo.
model: "microsoft/Phi-3-mini-4k-instruct"
# Whether or not to train (boolean)
train: true

# Directory with {train, valid, test}.jsonl files
data: "data"

# The PRNG seed
seed: 0

# Number of layers to fine-tune
lora_layers: 32

# Minibatch size.
batch_size: 1

# Iterations to train for.
iters: 1000

# Number of validation batches, -1 uses the entire validation set.
val_batches: 25

# Adam learning rate.
learning_rate: 1e-6

# Number of training steps between loss reporting.
steps_per_report: 10

# Number of training steps between validations.
steps_per_eval: 200

# Load path to resume training with the given adapter weights.
resume_adapter_file: null

# Save/load path for the trained adapter weights.
adapter_path: "adapters"

# Save the model every N iterations.
save_every: 1000

# Evaluate on the test set after training
test: false

# Number of test set batches, -1 uses the entire test set.
test_batches: 100

# Maximum sequence length.
max_seq_length: 2048

# Use gradient checkpointing to reduce memory use.
grad_checkpoint: true

# LoRA parameters can only be specified in a config file
lora_parameters:
  # The layer keys to apply LoRA to.
  # These will be applied for the last lora_layers
  keys: ["o_proj","qkv_proj"]
  rank: 64
  alpha: 64
  dropout: 0.1


```

ターミナルでこのコマンドを実行してください


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. ファインチューニングアダプタをテストする**

ターミナルでファインチューニングアダプタを実行できます。例えば


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

そして、オリジナルモデルを実行して結果を比較します


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

ファインチューニングの結果とオリジナルモデルの結果を比較してみてください


## **4. アダプタをマージして新しいモデルを生成する**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. ollamaを使用して量子化されたファインチューニングモデルを実行する**

使用前に、llama.cpp環境を設定してください


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***注意:*** 

1. 現在、fp32、fp16、およびINT 8の量子化変換をサポートしています

2. マージされたモデルにはtokenizer.modelが欠けているため、https://huggingface.co/microsoft/Phi-3-mini-4k-instruct からダウンロードしてください

Ollamaモデルファイルを設定します（ollamaをインストールしていない場合は、[Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md)をお読みください）


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

ターミナルでコマンドを実行します


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

おめでとうございます！MLXフレームワークを使用したファインチューニングをマスターしました

**免責事項**:
この文書は機械翻訳サービスを使用して翻訳されています。正確さを期しておりますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご了承ください。原文の言語によるオリジナル文書を権威ある情報源と見なすべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤訳について、当社は責任を負いません。