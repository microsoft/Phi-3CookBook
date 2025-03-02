# **Phi-3 Προσαρμογή με το Πλαίσιο Apple MLX**

Μπορούμε να ολοκληρώσουμε την προσαρμογή συνδυάζοντας το Lora μέσω της γραμμής εντολών του πλαισίου Apple MLX. (Αν θέλετε να μάθετε περισσότερα για τη λειτουργία του MLX Framework, διαβάστε [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md)

## **1. Προετοιμασία δεδομένων**

Από προεπιλογή, το MLX Framework απαιτεί δεδομένα σε μορφή jsonl για train, test και eval, και συνδυάζεται με το Lora για την ολοκλήρωση των εργασιών προσαρμογής.

### ***Σημείωση:***

1. Μορφή δεδομένων jsonl:

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. Το παράδειγμά μας χρησιμοποιεί [τα δεδομένα του TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), αλλά η ποσότητα των δεδομένων είναι σχετικά ανεπαρκής, επομένως τα αποτελέσματα της προσαρμογής δεν είναι απαραίτητα τα καλύτερα. Συνιστάται στους χρήστες να χρησιμοποιούν καλύτερα δεδομένα με βάση τα δικά τους σενάρια.

3. Η μορφή δεδομένων συνδυάζεται με το πρότυπο Phi-3.

Παρακαλούμε κατεβάστε τα δεδομένα από αυτόν τον [σύνδεσμο](../../../../code/04.Finetuning/mlx), συμπεριλάβετε όλα τα .jsonl στον φάκελο ***data***.

## **2. Προσαρμογή μέσω τερματικού**

Εκτελέστε αυτήν την εντολή στο τερματικό:

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

### ***Σημείωση:***

1. Αυτή είναι προσαρμογή LoRA, το MLX Framework δεν έχει δημοσιεύσει το QLoRA.

2. Μπορείτε να αλλάξετε το αρχείο config.yaml για να τροποποιήσετε ορισμένες παραμέτρους, όπως:

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

Εκτελέστε αυτήν την εντολή στο τερματικό:

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. Εκτέλεση Fine-tuning adapter για δοκιμή**

Μπορείτε να εκτελέσετε τον fine-tuning adapter στο τερματικό ως εξής:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

και να εκτελέσετε το αρχικό μοντέλο για να συγκρίνετε τα αποτελέσματα:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

Μπορείτε να προσπαθήσετε να συγκρίνετε τα αποτελέσματα της προσαρμογής με το αρχικό μοντέλο.

## **4. Συγχώνευση adapters για δημιουργία νέων μοντέλων**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Εκτέλεση ποσοτικοποιημένων μοντέλων προσαρμογής με το ollama**

Πριν τη χρήση, παρακαλούμε να ρυθμίσετε το περιβάλλον σας για το llama.cpp:

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Σημείωση:*** 

1. Υποστηρίζεται πλέον η μετατροπή ποσοτικοποίησης των fp32, fp16 και INT8.

2. Το συγχωνευμένο μοντέλο δεν περιλαμβάνει το tokenizer.model, παρακαλούμε κατεβάστε το από https://huggingface.co/microsoft/Phi-3-mini-4k-instruct.

Ρυθμίστε το αρχείο μοντέλου Ollama (Αν δεν έχετε εγκαταστήσει το ollama, διαβάστε [Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md)):

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

Εκτελέστε την εντολή στο τερματικό:

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

Συγχαρητήρια! Μάθατε πώς να κάνετε προσαρμογή με το MLX Framework.

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες μετάφρασης που βασίζονται σε τεχνητή νοημοσύνη. Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η έγκυρη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.