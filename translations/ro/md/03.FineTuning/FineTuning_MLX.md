# **Ajustarea fină a Phi-3 cu cadrul Apple MLX**

Putem realiza ajustarea fină combinată cu Lora prin intermediul liniei de comandă a cadrului Apple MLX. (Dacă doriți să aflați mai multe despre funcționarea cadrului MLX, vă rugăm să citiți [Inferența Phi-3 cu cadrul Apple MLX](../03.FineTuning/03.Inference/MLX_Inference.md))


## **1. Pregătirea datelor**

În mod implicit, cadrul MLX necesită formatul jsonl pentru train, test și eval, și este combinat cu Lora pentru a finaliza sarcinile de ajustare fină.


### ***Notă:***

1. Formatul de date jsonl ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Exemplul nostru folosește [datele TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), dar cantitatea de date este relativ insuficientă, astfel încât rezultatele ajustării fine nu sunt neapărat cele mai bune. Se recomandă ca utilizatorii să folosească date mai bune, în funcție de propriile scenarii, pentru a obține rezultate mai bune.

3. Formatul datelor este combinat cu șablonul Phi-3

Vă rugăm să descărcați datele de la acest [link](../../../../code/04.Finetuning/mlx), asigurați-vă că includeți toate fișierele .jsonl în folderul ***data***


## **2. Ajustarea fină în terminal**

Rulați această comandă în terminal


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Notă:***

1. Aceasta este o ajustare fină LoRA, cadrul MLX nu a publicat QLoRA

2. Puteți seta config.yaml pentru a modifica anumite argumente, cum ar fi


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

Rulați această comandă în terminal


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Rulați adapterul de ajustare fină pentru testare**

Puteți rula adapterul de ajustare fină în terminal, astfel:


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

și rulați modelul original pentru a compara rezultatele 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Puteți încerca să comparați rezultatele ajustării fine cu modelul original


## **4. Îmbinarea adapterelor pentru a genera modele noi**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Rularea modelelor ajustate și cuantificate utilizând ollama**

Înainte de utilizare, configurați mediul llama.cpp


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Notă:*** 

1. Acum se acceptă conversia cuantizării pentru fp32, fp16 și INT 8

2. Modelul îmbinat nu include tokenizer.model, vă rugăm să-l descărcați de la https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

Setați fișierul model Ollama (Dacă nu aveți instalat ollama, vă rugăm să citiți [Ollama QuickStart](https://ollama.com/)))


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Rulați comanda în terminal


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Felicitări! Ați învățat să realizați ajustarea fină cu cadrul MLX

**Declinări de responsabilitate**:  
Acest document a fost tradus folosind servicii de traducere bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa maternă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă o traducere profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care ar putea rezulta din utilizarea acestei traduceri.