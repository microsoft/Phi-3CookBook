# **Kufanya Fine-tuning kwa Phi-3 kwa Kutumia Mfumo wa Apple MLX**

Tunaweza kukamilisha Fine-tuning pamoja na Lora kupitia amri ya mfumo wa Apple MLX. (Ikiwa unataka kujifunza zaidi kuhusu uendeshaji wa Mfumo wa MLX, tafadhali soma [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)

## **1. Maandalizi ya Data**

Kwa chaguo-msingi, Mfumo wa MLX unahitaji muundo wa jsonl wa train, test, na eval, na unachanganywa na Lora ili kukamilisha kazi za Fine-tuning.

### ***Kumbuka:***

1. Muundo wa data ya jsonl:

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Mfano wetu unatumia [data ya TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), lakini kiasi cha data ni kidogo, kwa hivyo matokeo ya Fine-tuning si lazima yawe bora zaidi. Inashauriwa wanafunzi kutumia data bora zaidi kulingana na hali zao ili kukamilisha.

3. Muundo wa data umeunganishwa na template ya Phi-3.

Tafadhali pakua data kutoka kwa [kiungo hiki](../../../../code/04.Finetuning/mlx), tafadhali jumuisha faili zote za .jsonl kwenye folda ya ***data***.

## **2. Kufanya Fine-tuning kwenye terminal yako**

Tafadhali endesha amri hii kwenye terminal:

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***Kumbuka:***

1. Hii ni Fine-tuning ya LoRA, mfumo wa MLX haujachapisha QLoRA.

2. Unaweza kuweka config.yaml kubadilisha baadhi ya hoja, kama:

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

Tafadhali endesha amri hii kwenye terminal:

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. Kuendesha Fine-tuning adapter ili kujaribu**

Unaweza kuendesha Fine-tuning adapter kwenye terminal, kama hivi:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

na kuendesha modeli ya asili ili kulinganisha matokeo:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Unaweza kujaribu kulinganisha matokeo ya Fine-tuning na modeli ya asili.

## **4. Kuunganisha adapters ili kuzalisha modeli mpya**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Kuendesha modeli za Fine-tuning zilizo na kiasi kwa kutumia ollama**

Kabla ya kutumia, tafadhali sanidi mazingira yako ya llama.cpp:

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Kumbuka:***

1. Sasa inasaidia ubadilishaji wa kiasi wa fp32, fp16 na INT 8.

2. Modeli iliyounganishwa inakosa tokenizer.model, tafadhali ipakue kutoka https://huggingface.co/microsoft/Phi-3-mini-4k-instruct.

Weka faili ya Ollama Model (Ikiwa hujafunga ollama, tafadhali soma [Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md)):

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Endesha amri kwenye terminal:

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Hongera! Umefanikiwa kujifunza Fine-tuning kwa kutumia Mfumo wa MLX.

**Kanusho:**  
Hati hii imetafsiriwa kwa kutumia huduma za tafsiri za AI zinazotegemea mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati asilia katika lugha yake ya awali inapaswa kuchukuliwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia tafsiri ya kitaalamu ya binadamu. Hatutawajibika kwa kutoelewana au tafsiri zisizo sahihi zinazotokana na matumizi ya tafsiri hii.