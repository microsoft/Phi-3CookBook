# **使用 Apple MLX 框架進行 Phi-3 微調**

我們可以通過 Apple MLX 框架的命令行結合 Lora 完成微調。（如果您想了解更多有關 MLX 框架操作的資訊，請參閱 [使用 Apple MLX 框架推理 Phi-3](../03.FineTuning/03.Inference/MLX_Inference.md)）

## **1. 資料準備**

預設情況下，MLX 框架需要 train、test 和 eval 的 jsonl 格式，並結合 Lora 完成微調任務。

### ***注意:***

1. jsonl 資料格式：

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. 我們的範例使用 [TruthfulQA 的資料](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv)，但資料量相對不足，因此微調結果不一定最佳。建議學習者根據自身場景使用更好的資料進行微調。

3. 資料格式需結合 Phi-3 模板

請從此 [連結](../../../../code/04.Finetuning/mlx) 下載資料，請確保 ***data*** 資料夾中包含所有 .jsonl 檔案。

## **2. 在終端進行微調**

請在終端執行以下指令：

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

### ***注意:***

1. 這是 LoRA 微調，MLX 框架目前未發佈 QLoRA。

2. 您可以通過 config.yaml 修改一些參數，例如：

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

## **3. 運行微調適配器進行測試**

您可以在終端運行微調適配器，如下所示：

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

並運行原始模型以進行結果比較：

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

您可以嘗試比較微調後模型與原始模型的結果。

## **4. 合併適配器生成新模型**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. 使用 Ollama 運行量化後的微調模型**

在使用之前，請配置您的 llama.cpp 環境：

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***注意:*** 

1. 現在支援 fp32、fp16 和 INT 8 的量化轉換。

2. 合併後的模型缺少 tokenizer.model，請從 https://huggingface.co/microsoft/Phi-3-mini-4k-instruct 下載。

設置 Ollama 模型檔案（如果尚未安裝 Ollama，請參閱 [Ollama 快速入門](https://ollama.com/)）。

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

在終端執行以下指令：

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

恭喜！您已掌握使用 MLX 框架進行微調的方法。

**免責聲明**：  
本文件使用機器翻譯AI服務進行翻譯。儘管我們努力確保翻譯的準確性，但請注意，自動翻譯可能會包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解釋不承擔責任。