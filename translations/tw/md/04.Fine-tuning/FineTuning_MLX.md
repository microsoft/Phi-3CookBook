# **使用 Apple MLX 框架進行 Phi-3 微調**

我們可以通過 Apple MLX 框架的命令行完成結合 Lora 的微調。（如果你想了解更多有關 MLX 框架的操作，請閱讀 [Inference Phi-3 with Apple MLX Framework](../03.Inference/MLX_Inference.md)

## **1. 資料準備**

預設情況下，MLX 框架需要 train、test 和 eval 的 jsonl 格式，並結合 Lora 來完成微調工作。

### ***注意:***

1. jsonl 資料格式：

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. 我們的範例使用 [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)，但資料量相對不足，因此微調結果不一定是最好的。建議學習者根據自己的情境使用更好的資料來完成。

3. 資料格式結合 Phi-3 模板

請從這個 [link](../../../../code/04.Finetuning/mlx) 下載資料，請將所有 .jsonl 包含在 ***data*** 資料夾中。

## **2. 在終端中進行微調**

請在終端中運行此命令

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***注意:***

1. 這是 LoRA 微調，MLX 框架尚未發布 QLoRA

2. 你可以設置 config.yaml 來更改一些參數，例如

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

請在終端中運行此命令

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. 運行微調適配器進行測試**

你可以在終端中運行微調適配器，如下所示

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

並運行原始模型來比較結果

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

你可以嘗試比較微調後的結果與原始模型的結果

## **4. 合併適配器以生成新模型**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. 使用 ollama 運行量化微調模型**

使用前，請配置你的 llama.cpp 環境

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***注意:***

1. 現在支持 fp32、fp16 和 INT 8 的量化轉換

2. 合併的模型缺少 tokenizer.model，請從 https://huggingface.co/microsoft/Phi-3-mini-4k-instruct 下載

設置 Ollma 模型文件（如果未安裝 ollama，請閱讀 [Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md)

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

在終端中運行命令

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

恭喜！掌握了使用 MLX 框架進行微調

**免責聲明**: 
本文檔使用基於機器的AI翻譯服務進行翻譯。儘管我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原語言的原始文檔為權威來源。對於關鍵信息，建議尋求專業的人類翻譯。我們不對因使用此翻譯而產生的任何誤解或誤讀負責。