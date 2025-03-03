# **تنظیم دقیق Phi-3 با چارچوب Apple MLX**

ما می‌توانیم تنظیم دقیق را با ترکیب Lora از طریق خط فرمان چارچوب Apple MLX انجام دهیم. (اگر می‌خواهید اطلاعات بیشتری درباره عملکرد چارچوب MLX بدانید، لطفاً [استنتاج Phi-3 با چارچوب Apple MLX](../03.FineTuning/03.Inference/MLX_Inference.md) را بخوانید.)

## **۱. آماده‌سازی داده‌ها**

به طور پیش‌فرض، چارچوب MLX به فرمت jsonl برای داده‌های آموزش، آزمون و ارزیابی نیاز دارد و با ترکیب Lora کارهای تنظیم دقیق را تکمیل می‌کند.

### ***توجه:***

1. فرمت داده jsonl:

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. مثال ما از [داده‌های TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) استفاده می‌کند، اما حجم داده‌ها نسبتاً کم است، بنابراین نتایج تنظیم دقیق لزوماً بهترین نیستند. توصیه می‌شود که کاربران بر اساس سناریوهای خود از داده‌های بهتری استفاده کنند.

3. فرمت داده با قالب Phi-3 ترکیب شده است.

لطفاً داده‌ها را از این [لینک](../../../../code/04.Finetuning/mlx) دانلود کنید و تمام فایل‌های .jsonl را در پوشه ***data*** قرار دهید.

## **۲. تنظیم دقیق در ترمینال**

لطفاً این دستور را در ترمینال اجرا کنید:

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

## ***توجه:***

1. این تنظیم دقیق LoRA است، چارچوب MLX هنوز QLoRA را منتشر نکرده است.

2. می‌توانید فایل config.yaml را برای تغییر برخی از پارامترها تنظیم کنید، مانند:

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

لطفاً این دستور را در ترمینال اجرا کنید:

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **۳. اجرای آداپتور تنظیم دقیق برای آزمایش**

می‌توانید آداپتور تنظیم دقیق را در ترمینال اجرا کنید، مانند این:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

و مدل اصلی را برای مقایسه نتیجه اجرا کنید:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

می‌توانید نتایج تنظیم دقیق را با مدل اصلی مقایسه کنید.

## **۴. ترکیب آداپتورها برای تولید مدل‌های جدید**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **۵. اجرای مدل‌های تنظیم دقیق‌شده کمّی با استفاده از Ollama**

قبل از استفاده، لطفاً محیط llama.cpp خود را پیکربندی کنید.

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***توجه:***

1. در حال حاضر از تبدیل کمّی fp32، fp16 و INT8 پشتیبانی می‌شود.

2. مدل ترکیب‌شده فایل tokenizer.model را ندارد، لطفاً آن را از https://huggingface.co/microsoft/Phi-3-mini-4k-instruct دانلود کنید.

فایل مدل Ollama را تنظیم کنید (اگر Ollama نصب نشده است، لطفاً [شروع سریع Ollama](https://ollama.com/) را بخوانید).

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

دستور را در ترمینال اجرا کنید:

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

تبریک می‌گویم! تنظیم دقیق با چارچوب MLX را یاد گرفتید.

**سلب مسئولیت**:  
این سند با استفاده از خدمات ترجمه ماشینی مبتنی بر هوش مصنوعی ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است شامل خطاها یا نارسایی‌هایی باشد. سند اصلی به زبان اصلی آن باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا تفسیرهای نادرست ناشی از استفاده از این ترجمه نداریم.