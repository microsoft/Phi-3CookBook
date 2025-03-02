# **Fine-tuning Phi-3 con il framework Apple MLX**

È possibile completare il fine-tuning combinato con Lora attraverso il comando del framework Apple MLX. (Se desideri saperne di più sul funzionamento del framework MLX, leggi [Inference Phi-3 con il framework Apple MLX](../03.FineTuning/03.Inference/MLX_Inference.md)


## **1. Preparazione dei dati**

Per impostazione predefinita, il framework MLX richiede che i dati di training, test ed eval siano in formato jsonl e siano combinati con Lora per completare i lavori di fine-tuning.


### ***Nota:***

1. Formato dati jsonl:


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Nel nostro esempio utilizziamo i dati di [TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), ma la quantità di dati è relativamente insufficiente, quindi i risultati del fine-tuning potrebbero non essere ottimali. Si consiglia agli utenti di utilizzare dati migliori basati sui propri scenari per ottenere risultati migliori.

3. Il formato dei dati è combinato con il template di Phi-3.

Scarica i dati da questo [link](../../../../code/04.Finetuning/mlx), assicurandoti di includere tutti i file .jsonl nella cartella ***data***.


## **2. Eseguire il fine-tuning nel terminale**

Esegui questo comando nel terminale:


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Nota:***

1. Questo è un fine-tuning con LoRA; il framework MLX non supporta QLoRA al momento.

2. Puoi modificare il file config.yaml per cambiare alcuni parametri, come:


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

Esegui questo comando nel terminale:


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Eseguire l'adapter di fine-tuning per test**

Puoi eseguire l'adapter di fine-tuning nel terminale, come segue:


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

E poi eseguire il modello originale per confrontare i risultati:


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Prova a confrontare i risultati del fine-tuning con quelli del modello originale.


## **4. Unire gli adapter per generare nuovi modelli**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```


## **5. Eseguire modelli di fine-tuning quantificati con Ollama**

Prima di iniziare, configura l'ambiente llama.cpp:


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Nota:***

1. Attualmente è supportata la conversione quantizzata di fp32, fp16 e INT8.

2. Il modello unito manca del file tokenizer.model, scaricalo da https://huggingface.co/microsoft/Phi-3-mini-4k-instruct.

Imposta il file del modello Ollama (se Ollama non è installato, leggi [Ollama QuickStart](https://ollama.com/)):


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Esegui il comando nel terminale:


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Congratulazioni! Ora hai imparato a eseguire il fine-tuning con il framework MLX.

**Disclaimer**:  
Questo documento è stato tradotto utilizzando servizi di traduzione automatica basati sull'intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.