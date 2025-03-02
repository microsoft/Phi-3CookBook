# **Apple MLX ফ্রেমওয়ার্ক ব্যবহার করে Phi-3 এর ফাইন-টিউনিং**

Apple MLX ফ্রেমওয়ার্কের কমান্ড লাইন ব্যবহার করে Lora এর সাথে ফাইন-টিউনিং সম্পন্ন করা যায়। (যদি আপনি MLX ফ্রেমওয়ার্কের অপারেশন সম্পর্কে আরও জানতে চান, অনুগ্রহ করে [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md) পড়ুন।)


## **১. ডেটা প্রস্তুতি**

ডিফল্টভাবে, MLX ফ্রেমওয়ার্ক ট্রেন, টেস্ট এবং ইভাল এর jsonl ফরম্যাটের ডেটা প্রয়োজন, যা Lora এর সাথে মিলিয়ে ফাইন-টিউনিং কাজ সম্পন্ন করে।


### ***নোট:***

1. jsonl ডেটা ফরম্যাট :


```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. আমাদের উদাহরণে [TruthfulQA এর ডেটা](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) ব্যবহার করা হয়েছে, তবে ডেটার পরিমাণ তুলনামূলকভাবে অপর্যাপ্ত, তাই ফাইন-টিউনিং এর ফলাফল সর্বদা সেরা নাও হতে পারে। শিখতে ইচ্ছুকদের নিজস্ব পরিস্থিতি অনুযায়ী উন্নত ডেটা ব্যবহার করার পরামর্শ দেওয়া হচ্ছে।

3. ডেটা ফরম্যাট Phi-3 টেমপ্লেটের সাথে মিলিয়ে নিতে হবে।

এই [লিঙ্ক](../../../../code/04.Finetuning/mlx) থেকে ডেটা ডাউনলোড করুন, ***data*** ফোল্ডারে থাকা সমস্ত .jsonl ফাইল অন্তর্ভুক্ত করুন।


## **২. আপনার টার্মিনালে ফাইন-টিউনিং চালানো**

টার্মিনালে এই কমান্ডটি চালান:


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***নোট:***

1. এটি LoRA ফাইন-টিউনিং, MLX ফ্রেমওয়ার্ক এখনও QLoRA প্রকাশ করেনি।

2. config.yaml ব্যবহার করে কিছু আর্গুমেন্ট পরিবর্তন করতে পারেন, যেমন:


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

টার্মিনালে এই কমান্ডটি চালান:


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **৩. ফাইন-টিউনিং অ্যাডাপ্টার চালিয়ে পরীক্ষা করুন**

আপনি টার্মিনালে ফাইন-টিউনিং অ্যাডাপ্টার চালাতে পারেন, উদাহরণস্বরূপ:


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

এবং ফলাফল তুলনা করতে মূল মডেল চালান:


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

আপনি ফাইন-টিউনিং এর ফলাফল এবং মূল মডেলের ফলাফল তুলনা করে দেখতে পারেন।


## **৪. অ্যাডাপ্টার মার্জ করে নতুন মডেল তৈরি করা**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```


## **৫. Ollama ব্যবহার করে কোয়ান্টিফাইড ফাইন-টিউনিং মডেল চালানো**

ব্যবহারের আগে, আপনার llama.cpp পরিবেশ কনফিগার করুন।


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***নোট:***

1. এখন fp32, fp16 এবং INT 8 এর কোয়ান্টাইজেশন কনভার্সন সমর্থন করে।

2. মার্জ করা মডেলে tokenizer.model অনুপস্থিত, এটি https://huggingface.co/microsoft/Phi-3-mini-4k-instruct থেকে ডাউনলোড করুন।

Ollama মডেল ফাইল সেট করুন (যদি Ollama ইনস্টল না করা থাকে, অনুগ্রহ করে [Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md) পড়ুন।)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

টার্মিনালে এই কমান্ডটি চালান:


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

অভিনন্দন! MLX ফ্রেমওয়ার্ক দিয়ে ফাইন-টিউনিং আয়ত্ত করুন।

**অস্বীকৃতি**:  
এই নথি মেশিন-ভিত্তিক এআই অনুবাদ সেবার মাধ্যমে অনুবাদ করা হয়েছে। আমরা যথাসাধ্য নির্ভুলতার চেষ্টা করি, তবে অনুগ্রহ করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসংগতি থাকতে পারে। নথির মূল ভাষায় থাকা আসল নথিকেই প্রামাণিক উৎস হিসেবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের ক্ষেত্রে পেশাদার মানব অনুবাদ গ্রহণ করার পরামর্শ দেওয়া হচ্ছে। এই অনুবাদ ব্যবহারের ফলে সৃষ্ট কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়বদ্ধ নই।