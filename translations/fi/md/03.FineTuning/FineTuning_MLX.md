# **Phi-3:n hienosäätö Apple MLX Frameworkilla**

Voimme suorittaa Phi-3:n hienosäädön yhdistettynä Loraan Apple MLX Frameworkin komentorivin kautta. (Jos haluat lisätietoja MLX Frameworkin toiminnasta, lue [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))

## **1. Datan valmistelu**

Oletuksena MLX Framework vaatii train-, test- ja eval-datan jsonl-muodossa, ja se yhdistetään Loraan hienosäätötehtävien suorittamiseksi.

### ***Huom:***

1. jsonl-datan muoto:

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Esimerkissämme käytetään [TruthfulQA:n dataa](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), mutta datan määrä on suhteellisen vähäinen, joten hienosäädön tulokset eivät välttämättä ole parhaat mahdolliset. Suosittelemme, että käyttäjät käyttävät parempaa dataa omien tarpeidensa mukaan.

3. Datan muoto yhdistetään Phi-3-mallipohjaan.

Lataa data tästä [linkistä](../../../../code/04.Finetuning/mlx), sisällytä kaikki .jsonl-tiedostot ***data***-kansioon.

## **2. Hienosäätö terminaalissa**

Suorita tämä komento terminaalissa:

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***Huom:***

1. Tämä on LoRA-hienosäätö, MLX Framework ei tue QLoRA:aa.

2. Voit muuttaa config.yaml-tiedostoa säätääksesi joitakin parametreja, kuten:

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

Suorita tämä komento terminaalissa:

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. Hienosäätöadapterin testaaminen**

Voit suorittaa hienosäätöadapterin terminaalissa näin:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

ja suorittaa alkuperäisen mallin tulosten vertailua varten:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Voit yrittää verrata hienosäädetyn mallin tuloksia alkuperäiseen malliin.

## **4. Adapterien yhdistäminen uusien mallien luomiseksi**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Kvantifioitujen hienosäätömallien käyttö ollaman avulla**

Ennen käyttöä, konfiguroi llama.cpp-ympäristösi:

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Huom:***

1. Nyt tuetaan fp32-, fp16- ja INT8-kvantisointimuunnoksia.

2. Yhdistetyltä mallilta puuttuu tokenizer.model, lataa se osoitteesta https://huggingface.co/microsoft/Phi-3-mini-4k-instruct.

Määritä Ollama-mallitiedosto (jos ollamaa ei ole asennettu, lue [Ollama QuickStart](https://ollama.com/)):

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Suorita komento terminaalissa:

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Onnittelut! Olet oppinut käyttämään MLX Frameworkia hienosäätöön.

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisilla tekoälykäännöspalveluilla. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittistä tietoa varten suositellaan ammattimaista ihmiskääntämistä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virheellisistä tulkinnoista.