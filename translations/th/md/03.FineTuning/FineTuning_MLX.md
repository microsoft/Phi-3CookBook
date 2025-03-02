# **การปรับแต่ง Phi-3 ด้วย Apple MLX Framework**

เราสามารถปรับแต่ง (Fine-tuning) รวมกับ Lora ผ่านคำสั่งของ Apple MLX Framework ได้ (หากคุณต้องการทราบข้อมูลเพิ่มเติมเกี่ยวกับการทำงานของ MLX Framework โปรดอ่าน [Inference Phi-3 with Apple MLX Framework](../03.FineTuning/03.Inference/MLX_Inference.md))

## **1. การเตรียมข้อมูล**

โดยค่าเริ่มต้น MLX Framework ต้องการข้อมูลในรูปแบบ jsonl สำหรับ train, test และ eval และจะรวมกับ Lora เพื่อทำงานปรับแต่งให้เสร็จสมบูรณ์

### ***หมายเหตุ:***

1. รูปแบบข้อมูล jsonl:

```json

{"text": "<|user|>\nWhen were iron maidens commonly used? <|end|>\n<|assistant|> \nIron maidens were never commonly used <|end|>"}
{"text": "<|user|>\nWhat did humans evolve from? <|end|>\n<|assistant|> \nHumans and apes evolved from a common ancestor <|end|>"}
{"text": "<|user|>\nIs 91 a prime number? <|end|>\n<|assistant|> \nNo, 91 is not a prime number <|end|>"}
....

```

2. ตัวอย่างของเราใช้ [ข้อมูลของ TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv) แต่ปริมาณข้อมูลค่อนข้างไม่เพียงพอ ดังนั้นผลลัพธ์ของการปรับแต่งอาจไม่ได้ดีที่สุด ขอแนะนำให้ผู้เรียนใช้ข้อมูลที่เหมาะสมกว่าตามสถานการณ์ของตนเอง

3. รูปแบบข้อมูลจะต้องรวมกับเทมเพลตของ Phi-3

โปรดดาวน์โหลดข้อมูลจาก [ลิงก์นี้](../../../../code/04.Finetuning/mlx) และใส่ไฟล์ .jsonl ทั้งหมดในโฟลเดอร์ ***data***

## **2. การปรับแต่งในเทอร์มินัล**

โปรดรันคำสั่งนี้ในเทอร์มินัล

```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```

### ***หมายเหตุ:***

1. นี่คือการปรับแต่งด้วย LoRA ปัจจุบัน MLX Framework ยังไม่รองรับ QLoRA

2. คุณสามารถแก้ไขไฟล์ config.yaml เพื่อเปลี่ยนพารามิเตอร์บางตัว เช่น

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

โปรดรันคำสั่งนี้ในเทอร์มินัล

```bash

python -m  mlx_lm.lora --config lora_config.yaml

```

## **3. รัน Fine-tuning adapter เพื่อทดสอบ**

คุณสามารถรัน Fine-tuning adapter ในเทอร์มินัลได้ ดังนี้:

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

และรันโมเดลต้นฉบับเพื่อเปรียบเทียบผลลัพธ์

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Why do chameleons change colors? " --eos-token "<|end|>"    

```

คุณสามารถลองเปรียบเทียบผลลัพธ์ระหว่างการปรับแต่งกับโมเดลต้นฉบับได้

## **4. รวม adapters เพื่อสร้างโมเดลใหม่**

```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. การรันโมเดลที่ปรับแต่งและถูกทำให้มีขนาดเล็กลงด้วย ollama**

ก่อนใช้งาน โปรดตั้งค่า llama.cpp environment ของคุณ

```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***หมายเหตุ:***

1. ขณะนี้รองรับการแปลง quantization ในรูปแบบ fp32, fp16 และ INT 8

2. โมเดลที่รวมกันจะไม่มี tokenizer.model โปรดดาวน์โหลดจาก https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

ตั้งค่าไฟล์ Ollama Model (หากยังไม่ได้ติดตั้ง Ollama โปรดอ่าน [Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md))

```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

รันคำสั่งในเทอร์มินัล

```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Why do chameleons change colors?" 

```

ยินดีด้วย! คุณได้เรียนรู้การปรับแต่งด้วย MLX Framework แล้ว

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาโดยปัญญาประดิษฐ์ (AI) แม้ว่าเราจะพยายามให้การแปลมีความถูกต้อง แต่โปรดทราบว่าการแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้องเกิดขึ้น เอกสารต้นฉบับในภาษาต้นฉบับควรถูกพิจารณาว่าเป็นแหล่งข้อมูลที่เชื่อถือได้ สำหรับข้อมูลที่สำคัญ ขอแนะนำให้ใช้บริการแปลภาษามนุษย์ที่เป็นมืออาชีพ เราไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดอันเกิดจากการใช้การแปลนี้