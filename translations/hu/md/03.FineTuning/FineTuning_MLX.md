# **Phi-3 finomhangolása az Apple MLX Framework segítségével**

Az Apple MLX Framework parancssorával elvégezhetjük a finomhangolást, kombinálva a Lora-val. (Ha többet szeretnél megtudni az MLX Framework működéséről, olvasd el ezt: [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))


## **1. Adatelőkészítés**

Alapértelmezés szerint az MLX Framework a train, test és eval jsonl formátumot követeli meg, és a Lora-val kombinálva végzi el a finomhangolási feladatokat.


### ***Megjegyzés:***

1. jsonl adatformátum:


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Példánk a [TruthfulQA adatait](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) használja, de az adatok mennyisége viszonylag kevés, így a finomhangolási eredmények nem feltétlenül a legjobbak. Javasoljuk, hogy a tanulók a saját forgatókönyveik alapján jobb adatokat használjanak.

3. Az adatformátum a Phi-3 sablonnal kombinált

Kérjük, töltsd le az adatokat erről a [linkről](../../../../code/04.Finetuning/mlx), és helyezd el az összes .jsonl fájlt a ***data*** mappában.


## **2. Finomhangolás a terminálban**

Futtasd az alábbi parancsot a terminálban:


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Megjegyzés:***

1. Ez egy LoRA finomhangolás, az MLX Framework még nem publikálta a QLoRA-t.

2. A config.yaml fájlban módosíthatsz bizonyos paramétereket, például:


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

Futtasd az alábbi parancsot a terminálban:


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. A finomhangolási adapter tesztelése**

A finomhangolási adaptert így futtathatod a terminálban:


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Majd futtasd az eredeti modellt az összehasonlításhoz:


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Próbáld összehasonlítani a finomhangolt modell és az eredeti modell eredményeit.


## **4. Adapterek egyesítése új modellek generálásához**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Kvantált finomhangolt modellek futtatása az ollama segítségével**

Használat előtt konfiguráld a llama.cpp környezetet:


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Megjegyzés:***

1. Jelenleg támogatja az fp32, fp16 és INT8 kvantálási konverziókat.

2. Az egyesített modellből hiányzik a tokenizer.model, kérjük, töltsd le innen: https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

Állítsd be az Ollama Modell fájlt (Ha nincs telepítve az ollama, olvasd el ezt: [Ollama QuickStart](https://ollama.com/))


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Futtasd a következő parancsot a terminálban:


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Gratulálunk! Mostantól képes vagy az MLX Framework segítségével finomhangolást végezni.

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítószolgáltatásokkal került lefordításra. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatizált fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális, emberi fordítást igénybe venni. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.