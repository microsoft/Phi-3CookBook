# **Prilagajanje Phi-3 z Apple MLX Framework**

Prilagajanje lahko izvedemo v kombinaciji z Lora prek ukazne vrstice Apple MLX Framework. (Če želite izvedeti več o delovanju MLX Framework, preberite [Inferenca Phi-3 z Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))


## **1. Priprava podatkov**

Privzeto MLX Framework zahteva jsonl format za train, test in eval, ki je kombiniran z Lora za dokončanje nalog prilagajanja.


### ***Opomba:***

1. Format podatkov jsonl ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Naš primer uporablja [podatke TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), vendar je količina podatkov relativno nezadostna, zato rezultati prilagajanja niso nujno najboljši. Priporočamo, da uporabniki uporabijo boljše podatke glede na svoje scenarije.

3. Format podatkov je kombiniran s predlogo Phi-3

Prosimo, prenesite podatke s te [povezave](../../../../code/04.Finetuning/mlx), vključite vse .jsonl datoteke v mapo ***data***


## **2. Prilagajanje v terminalu**

Zaženite ta ukaz v terminalu


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Opomba:***

1. To je prilagajanje LoRA, MLX Framework ne podpira QLoRA

2. V config.yaml lahko nastavite nekatere parametre, kot so


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

Zaženite ta ukaz v terminalu


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Zagon prilagoditvenega adapterja za testiranje**

V terminalu lahko zaženete prilagoditveni adapter, kot je ta


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

in zaženite originalni model za primerjavo rezultatov


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Poskusite primerjati rezultate prilagajanja z originalnim modelom


## **4. Združevanje adapterjev za ustvarjanje novih modelov**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Zagon kvantificiranih prilagojenih modelov z ollama**

Pred uporabo konfigurirajte svoje okolje llama.cpp


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Opomba:*** 

1. Trenutno je podprta kvantizacijska pretvorba fp32, fp16 in INT 8

2. Združenemu modelu manjka tokenizer.model, prenesite ga s https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

nastavite datoteko Ollama Model (Če Ollama ni nameščen, preberite [Ollama QuickStart](https://ollama.com/))


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

zaženite ukaz v terminalu


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Čestitamo! Obvladali ste prilagajanje z MLX Framework

**Izjava o omejitvi odgovornosti**:  
Ta dokument je bil preveden s pomočjo strojnih prevajalskih storitev z umetno inteligenco. Čeprav si prizadevamo za natančnost, prosimo, upoštevajte, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v njegovem izvirnem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije je priporočljivo uporabiti profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.