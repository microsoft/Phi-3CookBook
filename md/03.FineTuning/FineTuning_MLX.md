# **Fine-tuning Phi-3 with Apple MLX Framework**

We can complete Fine-tuning combined with Lora through the Apple MLX framework command line. (If you want to know more about the operation of MLX Framework, please read [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)


## **1. Data preparation**

By default, MLX Framework requires the jsonl format of train, test, and eval, and is combined with Lora to complete fine-tuning jobs.


### ***Note:***

1. jsonl data format ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Our example uses [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) , but the amount of data is relatively insufficient, so the fine-tuning results are not necessarily the best. It is recommended that learners use better data based on their own scenarios to complete.

3. The data format is combined with the Phi-3 template

Please download data from this [link](../../code/04.Finetuning/mlx/), please include all .jsonl in ***data*** folder


## **2. Fine-tuning in your terminal**

Please run this command in terminal


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Note:***

1. This is LoRA fine-tuning, MLX framework  not published QLoRA

2. You can set config.yaml to change some arguments,such as


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

Please run this command in terminal


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Run Fine-tuning adapter to test**

You can run fine-tuning adapter in terminal,like this 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

and run original model  to compare result 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

You can try to compare the results of Fine-tuning with the original model


## **4. Merge adapters to generate new models**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Running quantified fine-tuning models using ollama**

Before use, please configure your llama.cpp environment


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Note:*** 

1. Now supports quantization conversion of fp32, fp16 and INT 8

2. The merged model is missing tokenizer.model, please download it from https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

set a [Ollma Model](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

run command in terminal


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Congratulations! Master fine-tuning with the MLX Framework










