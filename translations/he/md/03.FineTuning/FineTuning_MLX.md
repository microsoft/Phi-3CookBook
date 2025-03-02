# **כיוונון עדין של Phi-3 עם מסגרת Apple MLX**

ניתן לבצע כיוונון עדין בשילוב עם Lora באמצעות שורת הפקודה של מסגרת Apple MLX. (אם ברצונכם לדעת יותר על פעולת מסגרת MLX, אנא קראו [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))

## **1. הכנת נתונים**

כברירת מחדל, מסגרת MLX דורשת את פורמט jsonl עבור קבצי train, test ו-eval, ומשלבת אותם עם Lora כדי להשלים משימות כיוונון עדין.

### ***הערה:***

1. פורמט הנתונים jsonl:

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. בדוגמה שלנו נעשה שימוש בנתוני [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), אך כמות הנתונים יחסית קטנה, ולכן תוצאות הכיוונון העדין לא בהכרח יהיו הטובות ביותר. מומלץ למשתמשים להשתמש בנתונים טובים יותר המתאימים לתרחישים שלהם.

3. פורמט הנתונים משולב עם תבנית Phi-3.

אנא הורידו את הנתונים מהקישור הזה [link](../../../../code/04.Finetuning/mlx), ודאו לכלול את כל קבצי ה-.jsonl בתיקיית ***data***.

## **2. כיוונון עדין באמצעות הטרמינל**

אנא הריצו את הפקודה הזו בטרמינל:

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***הערה:***

1. זהו כיוונון עדין עם LoRA, מסגרת MLX אינה תומכת ב-QLoRA.

2. ניתן לערוך את config.yaml כדי לשנות פרמטרים מסוימים, כמו:

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

אנא הריצו את הפקודה הזו בטרמינל:

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. הרצת מתאם הכיוונון העדין לבדיקות**

ניתן להריץ את מתאם הכיוונון העדין בטרמינל כך:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

ולבצע הרצה של המודל המקורי כדי להשוות את התוצאות:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

נסו להשוות את תוצאות הכיוונון העדין לתוצאות המודל המקורי.

## **4. מיזוג מתאמים ליצירת מודלים חדשים**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. הרצת מודלים מכווננים כמותית באמצעות ollama**

לפני השימוש, יש להגדיר את סביבת llama.cpp.

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***הערה:***

1. כעת נתמכת המרה כמותית ל-fp32, fp16 ו-INT 8.

2. במודל הממוזג חסר tokenizer.model, יש להוריד אותו מהקישור https://huggingface.co/microsoft/Phi-3-mini-4k-instruct.

הגדירו את קובץ המודל של Ollama (אם לא התקנתם את ollama, אנא קראו [Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md)).

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

הריצו את הפקודה בטרמינל:

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

מזל טוב! למדתם לבצע כיוונון עדין עם מסגרת MLX.

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. למרות שאנו שואפים לדיוק, יש לקחת בחשבון שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי מתרגם אנושי. איננו אחראים לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.