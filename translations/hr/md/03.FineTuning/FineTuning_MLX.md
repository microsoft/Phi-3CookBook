# **Fino podešavanje Phi-3 s Apple MLX Frameworkom**

Fino podešavanje u kombinaciji s Lora metodom možemo izvršiti putem naredbenog retka Apple MLX Frameworka. (Ako želite saznati više o radu MLX Frameworka, pročitajte [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))


## **1. Priprema podataka**

Prema zadanim postavkama, MLX Framework zahtijeva jsonl format za train, test i eval te se koristi u kombinaciji s Lora metodom za dovršavanje poslova finog podešavanja.


### ***Napomena:***

1. jsonl format podataka ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Naš primjer koristi [TruthfulQA podatke](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), ali količina podataka je relativno mala, pa rezultati finog podešavanja nisu nužno najbolji. Preporučuje se da korisnici koriste kvalitetnije podatke prilagođene svojim scenarijima.

3. Format podataka je kombiniran s Phi-3 predloškom.

Molimo preuzmite podatke s ove [poveznice](../../../../code/04.Finetuning/mlx), uključite sve .jsonl datoteke u ***data*** mapu.


## **2. Fino podešavanje putem terminala**

Pokrenite ovu naredbu u terminalu


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Napomena:***

1. Ovo je LoRA fino podešavanje, MLX Framework trenutno ne podržava QLoRA.

2. Možete izmijeniti config.yaml za promjenu određenih parametara, poput


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

Pokrenite ovu naredbu u terminalu


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Pokretanje adaptera za fino podešavanje radi testiranja**

Možete pokrenuti adapter za fino podešavanje u terminalu, ovako 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

i pokrenuti originalni model za usporedbu rezultata 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Možete pokušati usporediti rezultate finog podešavanja s originalnim modelom.


## **4. Spajanje adaptera za generiranje novih modela**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Pokretanje kvantificiranih modela finog podešavanja pomoću Ollama**

Prije korištenja, konfigurirajte svoje llama.cpp okruženje.


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Napomena:*** 

1. Trenutno podržava kvantizacijsku konverziju fp32, fp16 i INT 8.

2. Spojeni model nedostaje tokenizer.model, molimo preuzmite ga s https://huggingface.co/microsoft/Phi-3-mini-4k-instruct.

Postavite Ollama Model datoteku (ako Ollama nije instalirana, pročitajte [Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md)).


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Pokrenite naredbu u terminalu


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Čestitamo! Savladali ste fino podešavanje s MLX Frameworkom.

**Odricanje odgovornosti**:  
Ovaj dokument je preveden korištenjem usluga automatskog prijevoda temeljenih na umjetnoj inteligenciji. Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešne interpretacije proizašle iz korištenja ovog prijevoda.