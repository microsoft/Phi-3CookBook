# **Doladenie Phi-3 pomocou Apple MLX Framework**

Doladenie v kombinácii s Lora môžeme vykonať prostredníctvom príkazového riadku Apple MLX Framework. (Ak chcete vedieť viac o fungovaní MLX Framework, prečítajte si [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))

## **1. Príprava dát**

MLX Framework vyžaduje predvolene formát jsonl pre tréningové, testovacie a evaluačné dáta a v kombinácii s Lora umožňuje dokončiť úlohy doladenia.

### ***Poznámka:***

1. Formát dát jsonl:

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. V našom príklade používame [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), avšak množstvo dát je relatívne nedostatočné, takže výsledky doladenia nemusia byť najlepšie. Odporúčame, aby používatelia použili kvalitnejšie dáta podľa svojich vlastných scenárov.

3. Formát dát je kombinovaný so šablónou Phi-3.

Dáta si môžete stiahnuť z tohto [odkazu](../../../../code/04.Finetuning/mlx), uistite sa, že všetky .jsonl sú zahrnuté v priečinku ***data***.

## **2. Doladenie v termináli**

Spustite tento príkaz v termináli:

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

### ***Poznámka:***

1. Toto je doladenie pomocou LoRA, MLX Framework zatiaľ nepodporuje QLoRA.

2. Môžete upraviť config.yaml na zmenu niektorých argumentov, ako napríklad:

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

Spustite tento príkaz v termináli:

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. Spustenie Fine-tuning adaptéra na testovanie**

Adaptér doladenia môžete spustiť v termináli, napríklad takto:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

A následne spustite pôvodný model na porovnanie výsledkov:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Môžete skúsiť porovnať výsledky doladenia s pôvodným modelom.

## **4. Zlúčenie adaptérov na vytvorenie nových modelov**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Spustenie kvantifikovaných doladených modelov pomocou Ollama**

Pred použitím nakonfigurujte svoje prostredie llama.cpp:

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Poznámka:***

1. Aktuálne je podporovaná kvantifikácia na fp32, fp16 a INT 8.

2. Zlúčenému modelu chýba tokenizer.model, prosím stiahnite si ho z https://huggingface.co/microsoft/Phi-3-mini-4k-instruct.

Nastavte súbor modelu Ollama (ak nemáte nainštalovaný Ollama, prečítajte si [Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md)):

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Spustite príkaz v termináli:

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Gratulujeme! Ovládli ste doladenie pomocou MLX Framework.

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových prekladových služieb AI. Hoci sa snažíme o presnosť, uvedomte si, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za záväzný zdroj. Pre dôležité informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.