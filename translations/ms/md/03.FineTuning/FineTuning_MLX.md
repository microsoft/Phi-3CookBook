# **Fine-tuning Phi-3 dengan Kerangka Kerja Apple MLX**

Kita boleh melengkapkan Fine-tuning yang digabungkan dengan Lora melalui baris perintah kerangka kerja Apple MLX. (Jika anda ingin tahu lebih lanjut tentang operasi Kerangka Kerja MLX, sila baca [Inference Phi-3 dengan Kerangka Kerja Apple MLX](../03.FineTuning/03.Inference/MLX_Inference.md))


## **1. Penyediaan Data**

Secara lalai, Kerangka Kerja MLX memerlukan format jsonl untuk train, test, dan eval, dan digabungkan dengan Lora untuk melengkapkan tugas fine-tuning.


### ***Nota:***

1. Format data jsonl ：


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Contoh kami menggunakan [data TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), tetapi jumlah data agak kurang, jadi hasil fine-tuning mungkin tidak semestinya terbaik. Adalah disyorkan agar pelajar menggunakan data yang lebih baik berdasarkan senario mereka sendiri untuk melengkapkan.

3. Format data digabungkan dengan templat Phi-3

Sila muat turun data dari [pautan ini](../../../../code/04.Finetuning/mlx), pastikan semua .jsonl dimasukkan dalam folder ***data***


## **2. Fine-tuning di terminal anda**

Sila jalankan perintah ini di terminal


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Nota:***

1. Ini adalah fine-tuning LoRA, kerangka kerja MLX belum menerbitkan QLoRA

2. Anda boleh mengubah config.yaml untuk menukar beberapa parameter, seperti


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

Sila jalankan perintah ini di terminal


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Jalankan Fine-tuning adapter untuk ujian**

Anda boleh menjalankan fine-tuning adapter di terminal, seperti ini 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

dan jalankan model asal untuk membandingkan hasil 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Anda boleh cuba membandingkan hasil Fine-tuning dengan model asal


## **4. Gabungkan adapter untuk menjana model baru**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Menjalankan model fine-tuning yang dikuantifikasi menggunakan ollama**

Sebelum digunakan, sila konfigurasikan persekitaran llama.cpp anda


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Nota:*** 

1. Kini menyokong penukaran kuantisasi untuk fp32, fp16 dan INT 8

2. Model yang digabungkan kekurangan tokenizer.model, sila muat turun dari https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

Tetapkan fail Model Ollama (Jika belum memasang ollama, sila baca [Ollama QuickStart](https://ollama.com/)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

jalankan perintah di terminal


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Tahniah! Anda telah menguasai fine-tuning dengan Kerangka Kerja MLX

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan perkhidmatan terjemahan berasaskan AI. Walaupun kami berusaha untuk memastikan ketepatan, sila maklum bahawa terjemahan automatik mungkin mengandungi kesilapan atau ketidaktepatan. Dokumen asal dalam bahasa asalnya harus dianggap sebagai sumber yang berwibawa. Untuk maklumat kritikal, terjemahan manusia profesional adalah disyorkan. Kami tidak bertanggungjawab atas sebarang salah faham atau salah tafsir yang timbul daripada penggunaan terjemahan ini.