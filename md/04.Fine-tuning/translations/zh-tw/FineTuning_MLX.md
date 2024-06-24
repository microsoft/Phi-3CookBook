# **微調 Phi-3 與 Apple MLX 框架**

我們可以通過 Apple MLX 框架命令行完成與 Lora 結合的微調。(如果你想了解更多關於 MLX 框架的操作，請閱讀 [Inference Phi-3 with Apple MLX Framework](../03.Inference/MLX_Inference.md)）。

## **1. 資料準備**

預設情況下，MLX Framework 需要 train、test 和 eval 的 jsonl 格式，並結合 Lora 完成微調工作。

### ***注意:***

1. jsonl 資料格式 ：

```json

{"text": "<|user|>\n鐵處女什麼時候被普遍使用？ <|end|>\n<|assistant|> \n鐵處女從未被普遍使用 <|end|>"}
{"text": "<|user|>\n人類從什麼進化而來？ <|end|>\n<|assistant|> \n人類和猿類從共同的祖先進化而來 <|end|>"}
{"text": "<|user|>\n91 是質數嗎？ <|end|>\n<|assistant|> \n不，91 不是質數 <|end|>"}
....

```

2. 我們的範例使用 [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) , 但資料量相對不足，因此微調結果不一定是最好的。建議學習者根據自己的情境使用更好的資料來完成。

3. 資料格式結合 Phi-3 模板

請從此 [link](../../code/04.Finetuning/mlx/) 下載資料, 請包含 ***data*** 資料夾中的所有 .jsonl。

## **2. 在你的終端機中微調**

請在終端機中執行此命令

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***注意:***

1. 這是 LoRA 微調，MLX 框架未發布 QLoRA

2. 你可以設定 config.yaml 來更改一些參數，例如

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

請在終端機中執行此命令

```bash

python -m mlx_lm.lora --config lora_config.yaml

```

## **3. 執行微調適配器進行測試**

你可以在終端機中執行微調適配器，像這樣

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "為什麼變色龍會改變顏色？" --eos-token "<|end|>"    

```

並執行原始模型以比較結果

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "為什麼變色龍會改變顏色？" --eos-token "<|end|>"    

```

你可以嘗試比較微調與原始模型的結果

## **4. 合併適配器以生成新模型**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. 執行量化微調模型使用 ollama**

在使用之前，請配置你的 llama.cpp 環境

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***注意:***

1. 現在支援 fp32、fp16 和 INT 8 的量化轉換

2. 合併的模型缺少 tokenizer.model，請從 [此連結](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) 下載。

設定 Ollma 模型檔案（如果未安裝 ollama，請閱讀 [Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md)）。

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

在終端機中執行命令

```bash

 ollama 建立 phi3ft -f Modelfile 

 ollama 執行 phi3ft "為什麼變色龍會改變顏色？" 

```

恭喜！使用 MLX Framework 精通微調

