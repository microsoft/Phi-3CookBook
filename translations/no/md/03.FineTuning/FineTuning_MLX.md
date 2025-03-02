# **Finjustering av Phi-3 med Apple MLX-rammeverket**

Vi kan gjennomføre finjustering kombinert med Lora via Apple MLX-rammeverkets kommandolinje. (Hvis du vil vite mer om hvordan MLX-rammeverket fungerer, les [Inference Phi-3 med Apple MLX-rammeverket](../03.FineTuning/03.Inference/MLX_Inference.md)).

## **1. Forberedelse av data**

Som standard krever MLX-rammeverket at trenings-, test- og evalueringsdata er i jsonl-format og kombineres med Lora for å fullføre finjusteringsjobber.

### ***Merk:***

1. jsonl-dataformat:

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. I vårt eksempel bruker vi [TruthfulQAs data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), men datamengden er relativt begrenset, så finjusteringsresultatene er ikke nødvendigvis optimale. Det anbefales at brukere benytter bedre datasett tilpasset sine egne behov.

3. Dataformatet kombineres med Phi-3-mal.

Vennligst last ned data fra denne [lenken](../../../../code/04.Finetuning/mlx), og sørg for å inkludere alle .jsonl-filer i ***data***-mappen.

## **2. Finjustering i terminalen**

Kjør denne kommandoen i terminalen:

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***Merk:***

1. Dette er LoRA-finjustering; MLX-rammeverket har ennå ikke publisert QLoRA.

2. Du kan redigere config.yaml for å endre enkelte parametere, som for eksempel:

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

Kjør denne kommandoen i terminalen:

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. Teste finjusteringsadapteren**

Du kan teste finjusteringsadapteren i terminalen ved å kjøre følgende kommando:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Og kjør den originale modellen for å sammenligne resultatene:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Prøv å sammenligne resultatene fra finjusteringen med den originale modellen.

## **4. Slå sammen adaptere for å generere nye modeller**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Kjøre kvantifiserte finjusteringsmodeller med Ollama**

Før bruk, konfigurer llama.cpp-miljøet ditt:

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Merk:*** 

1. Nå støttes kvantiseringskonvertering for fp32, fp16 og INT8.

2. Den sammenslåtte modellen mangler tokenizer.model, vennligst last den ned fra https://huggingface.co/microsoft/Phi-3-mini-4k-instruct.

Angi Ollama-modellfilen (hvis Ollama ikke er installert, les [Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md)).

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Kjør kommandoen i terminalen:

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Gratulerer! Du har mestret finjustering med MLX-rammeverket.

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettingstjenester. Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.