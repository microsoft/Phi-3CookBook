# **Apple MLXフレームワークを使用したPhi-3のファインチューニング**

Apple MLXフレームワークのコマンドラインを使用して、Loraと組み合わせたファインチューニングを行うことができます。（MLXフレームワークの操作について詳しく知りたい場合は、[Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md) をご覧ください）

## **1. データ準備**

デフォルトでは、MLXフレームワークはtrain、test、evalのjsonl形式を要求し、Loraと組み合わせてファインチューニングを完了します。

### ***注意:***

1. jsonlデータ形式：  

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. この例では[TruthfulQAのデータ](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)を使用していますが、データ量が比較的不足しているため、ファインチューニング結果が必ずしも最良であるとは限りません。学習者は自分のシナリオに基づいてより良いデータを使用して完了することをお勧めします。

3. データ形式はPhi-3テンプレートと組み合わせて使用します。

[こちらのリンク](../../../../code/04.Finetuning/mlx)からデータをダウンロードしてください。***data***フォルダ内のすべての.jsonlファイルを含めてください。

## **2. ターミナルでのファインチューニング**

ターミナルで次のコマンドを実行してください。

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***注意:***

1. これはLoRAファインチューニングです。MLXフレームワークはQLoRAを公開していません。

2. config.yamlを設定することで、以下のような引数を変更できます。

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
  scale: 1
  dropout: 0.1


```

ターミナルで次のコマンドを実行してください。

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. ファインチューニングアダプターのテスト実行**

ターミナルでファインチューニングアダプターを次のように実行できます。

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

また、オリジナルモデルを実行して結果を比較してください。

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

ファインチューニング結果とオリジナルモデルの結果を比較してみてください。

## **4. アダプターをマージして新しいモデルを生成**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Ollamaを使用して量子化されたファインチューニングモデルを実行**

使用前に、llama.cpp環境を設定してください。

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***注意:***  

1. 現在、fp32、fp16、INT8の量子化変換をサポートしています。

2. マージされたモデルにはtokenizer.modelが欠けているため、https://huggingface.co/microsoft/Phi-3-mini-4k-instruct からダウンロードしてください。

Ollamaモデルファイルを設定（Ollamaがインストールされていない場合は、[Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md) を参照してください）

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

ターミナルで次のコマンドを実行してください。

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

おめでとうございます！MLXフレームワークを使用したファインチューニングをマスターしました。

**免責事項**:  
この文書は、機械翻訳AIサービスを使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。原文（元の言語で書かれた文書）が公式な情報源として優先されるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の利用により生じた誤解や解釈の誤りについて、当方は一切の責任を負いかねます。