# **Fino podešavanje Phi-3 pomoću Apple MLX Framework-a**

Možemo završiti fino podešavanje kombinovano sa Lora-om putem komandne linije Apple MLX Framework-a. (Ako želite da saznate više o radu MLX Framework-a, pročitajte [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))


## **1. Priprema podataka**

Podrazumevano, MLX Framework zahteva jsonl format za train, test i eval, i koristi se zajedno sa Lora-om za završavanje zadataka finog podešavanja.


### ***Napomena:***

1. jsonl format podataka ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Naš primer koristi [TruthfulQA podatke](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), ali količina podataka je relativno nedovoljna, pa rezultati finog podešavanja nisu nužno najbolji. Preporučuje se da korisnici koriste bolje podatke u skladu sa svojim scenarijima za završavanje zadatka.

3. Format podataka je kombinovan sa Phi-3 šablonom.

Molimo preuzmite podatke sa ovog [linka](../../../../code/04.Finetuning/mlx), obavezno uključite sve .jsonl fajlove u folder ***data***.


## **2. Fino podešavanje u terminalu**

Pokrenite ovu komandu u terminalu


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Napomena:***

1. Ovo je LoRA fino podešavanje, MLX Framework još uvek ne podržava QLoRA.

2. Možete podesiti config.yaml da promenite neke argumente, kao što su:


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

Pokrenite ovu komandu u terminalu


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Pokretanje adaptera za fino podešavanje radi testiranja**

Možete pokrenuti adapter za fino podešavanje u terminalu, ovako:


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

i pokrenuti originalni model za poređenje rezultata:


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Možete pokušati da uporedite rezultate finog podešavanja sa originalnim modelom.


## **4. Spajanje adaptera za generisanje novih modela**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Pokretanje kvantifikovanih modela za fino podešavanje koristeći ollama**

Pre upotrebe, konfigurišite svoje llama.cpp okruženje


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Napomena:*** 

1. Sada je podržana kvantizacija u fp32, fp16 i INT8.

2. Spojenom modelu nedostaje tokenizer.model, molimo preuzmite ga sa https://huggingface.co/microsoft/Phi-3-mini-4k-instruct.

Podesite Ollama Model fajl (Ako Ollama nije instalirana, pročitajte [Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md)).


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

pokrenite komandu u terminalu:


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Čestitamo! Savladali ste fino podešavanje pomoću MLX Framework-a.

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења заснованих на вештачкој интелигенцији. Иако тежимо тачности, молимо вас да имате у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати меродавним. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било какве неспоразуме или погрешна тумачења која могу произаћи из коришћења овог превода.