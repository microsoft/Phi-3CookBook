# **ਐਪਲ MLX ਫਰੇਮਵਰਕ ਨਾਲ Phi-3 ਦਾ ਫਾਈਨ-ਟਿਊਨਿੰਗ**

ਅਸੀਂ ਐਪਲ MLX ਫਰੇਮਵਰਕ ਕਮਾਂਡ ਲਾਈਨ ਰਾਹੀਂ Lora ਦੇ ਨਾਲ ਜੋੜ ਕੇ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਪੂਰੀ ਕਰ ਸਕਦੇ ਹਾਂ। (ਜੇਕਰ ਤੁਸੀਂ MLX ਫਰੇਮਵਰਕ ਦੇ ਆਪਰੇਸ਼ਨ ਬਾਰੇ ਹੋਰ ਜਾਣਕਾਰੀ ਲੈਣੀ ਚਾਹੁੰਦੇ ਹੋ ਤਾਂ ਕਿਰਪਾ ਕਰਕੇ [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md) ਪੜ੍ਹੋ।)

## **1. ਡਾਟਾ ਤਿਆਰੀ**

ਡਿਫਾਲਟ ਰੂਪ ਵਿੱਚ, MLX ਫਰੇਮਵਰਕ ਨੂੰ ਟ੍ਰੇਨ, ਟੈਸਟ ਅਤੇ ਇਵੈਲ ਲਈ jsonl ਫਾਰਮੈਟ ਦੀ ਲੋੜ ਹੁੰਦੀ ਹੈ, ਅਤੇ ਇਹ Lora ਦੇ ਨਾਲ ਮਿਲ ਕੇ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਕੰਮ ਪੂਰੇ ਕਰਦਾ ਹੈ।

### ***ਨੋਟ:***

1. jsonl ਡਾਟਾ ਫਾਰਮੈਟ:

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. ਸਾਡੇ ਉਦਾਹਰਣ ਵਿੱਚ [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) ਵਰਤਿਆ ਗਿਆ ਹੈ, ਪਰ ਡਾਟਾ ਦੀ ਮਾਤਰਾ ਤੂਲਨਾ ਵਿੱਚ ਘੱਟ ਹੈ, ਇਸ ਲਈ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਦੇ ਨਤੀਜੇ ਜ਼ਰੂਰੀ ਨਹੀਂ ਕਿ ਸਭ ਤੋਂ ਵਧੀਆ ਹੋਣ। ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ ਕਿ ਵਿਦਿਆਰਥੀ ਆਪਣੇ ਸਵੈ-ਸਨਰਿਓਜ਼ ਦੇ ਆਧਾਰ 'ਤੇ ਵਧੀਆ ਡਾਟਾ ਵਰਤ ਕੇ ਪੂਰਾ ਕਰਨ।

3. ਡਾਟਾ ਫਾਰਮੈਟ ਨੂੰ Phi-3 ਟੈਂਪਲੇਟ ਨਾਲ ਜੋੜਿਆ ਗਿਆ ਹੈ।

ਕਿਰਪਾ ਕਰਕੇ ਇਸ [ਲਿੰਕ](../../../../code/04.Finetuning/mlx) ਤੋਂ ਡਾਟਾ ਡਾਊਨਲੋਡ ਕਰੋ, ***data*** ਫੋਲਡਰ ਵਿੱਚ ਸਾਰੇ .jsonl ਸ਼ਾਮਲ ਕਰੋ।  

## **2. ਆਪਣੇ ਟਰਮਿਨਲ ਵਿੱਚ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਚਲਾਓ**

ਕਿਰਪਾ ਕਰਕੇ ਇਹ ਕਮਾਂਡ ਟਰਮਿਨਲ ਵਿੱਚ ਚਲਾਓ:

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***ਨੋਟ:***

1. ਇਹ LoRA ਫਾਈਨ-ਟਿਊਨਿੰਗ ਹੈ, MLX ਫਰੇਮਵਰਕ ਨੇ QLoRA ਪ੍ਰਕਾਸ਼ਿਤ ਨਹੀਂ ਕੀਤਾ।

2. ਤੁਸੀਂ config.yaml ਸੈਟ ਕਰਕੇ ਕੁਝ ਆਰਗਯੂਮੈਂਟਸ ਬਦਲ ਸਕਦੇ ਹੋ, ਜਿਵੇਂ:

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

ਕਿਰਪਾ ਕਰਕੇ ਇਹ ਕਮਾਂਡ ਟਰਮਿਨਲ ਵਿੱਚ ਚਲਾਓ:

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. ਫਾਈਨ-ਟਿਊਨਿੰਗ ਅਡਾਪਟਰ ਟੈਸਟ ਕਰਨ ਲਈ ਚਲਾਓ**

ਤੁਸੀਂ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਅਡਾਪਟਰ ਟਰਮਿਨਲ ਵਿੱਚ ਚਲਾ ਸਕਦੇ ਹੋ, ਇਸ ਤਰ੍ਹਾਂ:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

ਅਤੇ ਅਸਲ ਮਾਡਲ ਚਲਾਓ ਅਤੇ ਨਤੀਜਿਆਂ ਦੀ ਤੁਲਨਾ ਕਰੋ:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

ਤੁਸੀਂ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਦੇ ਨਤੀਜਿਆਂ ਦੀ ਅਸਲ ਮਾਡਲ ਨਾਲ ਤੁਲਨਾ ਕਰਨ ਦੀ ਕੋਸ਼ਿਸ਼ ਕਰ ਸਕਦੇ ਹੋ।  

## **4. ਅਡਾਪਟਰ ਨੂੰ ਨਵੇਂ ਮਾਡਲ ਬਣਾਉਣ ਲਈ ਮਰਜ ਕਰੋ**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. ollama ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਮਾਤਰਾ-ਬੱਧ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਮਾਡਲ ਚਲਾਉਣਾ**

ਵਰਤੋਂ ਤੋਂ ਪਹਿਲਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਆਪਣੇ llama.cpp ਵਾਤਾਵਰਣ ਨੂੰ ਕਨਫਿਗਰ ਕਰੋ:

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***ਨੋਟ:***

1. ਹੁਣ fp32, fp16 ਅਤੇ INT 8 ਦੀ ਮਾਤਰਾ-ਬੱਧ ਰੂਪਾਂਤਰਨ ਦਾ ਸਮਰਥਨ ਹੈ।

2. ਮਰਜ ਕੀਤਾ ਮਾਡਲ tokenizer.model ਤੋਂ ਗੈਰਹਾਜ਼ਰ ਹੈ, ਕਿਰਪਾ ਕਰਕੇ ਇਸਨੂੰ https://huggingface.co/microsoft/Phi-3-mini-4k-instruct ਤੋਂ ਡਾਊਨਲੋਡ ਕਰੋ।

Ollama ਮਾਡਲ ਫਾਈਲ ਸੈਟ ਕਰੋ (ਜੇ ollama ਇੰਸਟਾਲ ਨਹੀਂ ਹੈ, ਕਿਰਪਾ ਕਰਕੇ [Ollama QuickStart](https://ollama.com/) ਪੜ੍ਹੋ):

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

ਕਮਾਂਡ ਟਰਮਿਨਲ ਵਿੱਚ ਚਲਾਓ:

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

ਮੁਬਾਰਕਾਂ! MLX ਫਰੇਮਵਰਕ ਨਾਲ ਫਾਈਨ-ਟਿਊਨਿੰਗ ਦਾ ਮਾਹਰ ਬਣੋ।

**ਅਸਵੀਕਾਰਣਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਮਸ਼ੀਨ-ਅਧਾਰਿਤ AI ਅਨੁਵਾਦ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਪਰ ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਤੀਆਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਉਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਅਧਿਕਾਰਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੇ ਪ੍ਰਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤ ਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।