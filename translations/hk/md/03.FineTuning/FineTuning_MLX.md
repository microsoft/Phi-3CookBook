# **使用 Apple MLX Framework 微調 Phi-3**

我們可以透過 Apple MLX Framework 的指令結合 Lora 完成微調。（如果想了解更多關於 MLX Framework 的操作，請閱讀 [使用 Apple MLX Framework 進行推理 Phi-3](../03.FineTuning/03.Inference/MLX_Inference.md)）

## **1. 資料準備**

預設情況下，MLX Framework 需要訓練、測試和評估資料的 jsonl 格式，並結合 Lora 完成微調工作。

### ***注意：***

1. jsonl 資料格式：

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. 我們的範例使用了 [TruthfulQA 的資料](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)，但資料量相對不足，因此微調結果不一定是最佳的。建議學習者根據自己的場景使用更好的資料進行微調。

3. 資料格式需結合 Phi-3 模板。

請從這個 [連結](../../../../code/04.Finetuning/mlx) 下載資料，請確保將所有 .jsonl 檔案放入 ***data*** 資料夾中。

## **2. 在終端進行微調**

請在終端執行以下指令：

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

### ***注意：***

1. 這是 LoRA 微調，目前 MLX Framework 尚未發布 QLoRA。

2. 你可以透過設定 config.yaml 來修改一些參數，例如：

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

請在終端執行以下指令：

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. 執行微調適配器進行測試**

你可以在終端執行微調適配器，如下所示：

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

並執行原始模型以進行結果比較：

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

你可以嘗試比較微調結果與原始模型的差異。

## **4. 合併適配器生成新模型**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. 使用 Ollama 執行量化微調模型**

在使用前，請先配置好你的 llama.cpp 環境：

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***注意：*** 

1. 現在支援 fp32、fp16 和 INT8 的量化轉換。

2. 合併後的模型缺少 tokenizer.model，請從 https://huggingface.co/microsoft/Phi-3-mini-4k-instruct 下載。

設定 Ollama 模型檔案（如果尚未安裝 Ollama，請閱讀 [Ollama 快速入門](../02.QuickStart/Ollama_QuickStart.md)）。

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

在終端執行以下指令：

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

恭喜！你已經掌握使用 MLX Framework 進行微調的技巧。

**免責聲明**：  
本文件是使用機器翻譯人工智能服務進行翻譯的。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵信息，建議使用專業的人工作翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀概不負責。