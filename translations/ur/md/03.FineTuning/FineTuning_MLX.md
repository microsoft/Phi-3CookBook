# **ایپل MLX فریم ورک کے ساتھ Phi-3 کی فائن ٹیوننگ**

ہم ایپل MLX فریم ورک کے کمانڈ لائن کے ذریعے Lora کے ساتھ مل کر فائن ٹیوننگ مکمل کر سکتے ہیں۔ (اگر آپ MLX فریم ورک کے آپریشن کے بارے میں مزید جاننا چاہتے ہیں تو براہ کرم [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md) پڑھیں۔)

## **1. ڈیٹا کی تیاری**

ڈیفالٹ کے طور پر، MLX فریم ورک ٹرین، ٹیسٹ، اور ایوال کے jsonl فارمیٹ کی ضرورت کرتا ہے، اور Lora کے ساتھ مل کر فائن ٹیوننگ کے کاموں کو مکمل کرتا ہے۔

### ***نوٹ:***

1. jsonl ڈیٹا فارمیٹ:

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. ہماری مثال میں [TruthfulQA's data](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) استعمال کیا گیا ہے، لیکن ڈیٹا کی مقدار نسبتاً کم ہے، اس لیے فائن ٹیوننگ کے نتائج ضروری نہیں کہ بہترین ہوں۔ تجویز دی جاتی ہے کہ سیکھنے والے اپنے مخصوص حالات کے مطابق بہتر ڈیٹا استعمال کریں۔

3. ڈیٹا فارمیٹ Phi-3 ٹیمپلیٹ کے ساتھ ملا ہوا ہے۔

براہ کرم اس [لنک](../../../../code/04.Finetuning/mlx) سے ڈیٹا ڈاؤن لوڈ کریں، اور ***data*** فولڈر میں تمام .jsonl شامل کریں۔

## **2. اپنے ٹرمینل میں فائن ٹیوننگ کریں**

براہ کرم یہ کمانڈ ٹرمینل میں چلائیں:

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***نوٹ:***

1. یہ LoRA فائن ٹیوننگ ہے، MLX فریم ورک نے ابھی تک QLoRA جاری نہیں کیا۔

2. آپ config.yaml کو کچھ آرگیومنٹس تبدیل کرنے کے لیے سیٹ کر سکتے ہیں، جیسے:

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

براہ کرم یہ کمانڈ ٹرمینل میں چلائیں:

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. فائن ٹیوننگ ایڈاپٹر کو ٹیسٹ کرنے کے لیے چلائیں**

آپ فائن ٹیوننگ ایڈاپٹر کو ٹرمینل میں اس طرح چلا سکتے ہیں:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

اور اصل ماڈل کو نتیجہ موازنہ کرنے کے لیے چلائیں:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

آپ فائن ٹیوننگ کے نتائج کو اصل ماڈل کے ساتھ موازنہ کرنے کی کوشش کر سکتے ہیں۔

## **4. ایڈاپٹرز کو ضم کرکے نیا ماڈل بنائیں**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. اولاما کے ذریعے کوانٹفائیڈ فائن ٹیوننگ ماڈلز چلانا**

استعمال سے پہلے، براہ کرم اپنے llama.cpp ماحول کو کنفیگر کریں:

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***نوٹ:*** 

1. اب fp32، fp16، اور INT 8 کی کوانٹائزیشن کنورژن کو سپورٹ کرتا ہے۔

2. مرج کیا ہوا ماڈل tokenizer.model سے خالی ہے، براہ کرم اسے https://huggingface.co/microsoft/Phi-3-mini-4k-instruct سے ڈاؤن لوڈ کریں۔

اولاما ماڈل فائل سیٹ کریں (اگر اولاما انسٹال نہیں کیا ہے تو براہ کرم [Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md) پڑھیں۔)

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

ٹرمینل میں کمانڈ چلائیں:

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

مبارک ہو! آپ نے MLX فریم ورک کے ساتھ فائن ٹیوننگ کو مکمل طور پر سیکھ لیا ہے۔

**اعلانِ لاتعلقی**:  
یہ دستاویز مشین پر مبنی AI ترجمہ خدمات کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی بھرپور کوشش کرتے ہیں، براہِ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا خامیاں ہوسکتی ہیں۔ اصل دستاویز کو اس کی اصل زبان میں مستند ماخذ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ ہم اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے ذمہ دار نہیں ہیں۔