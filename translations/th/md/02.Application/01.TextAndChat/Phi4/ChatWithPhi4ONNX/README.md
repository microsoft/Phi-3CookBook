# **สนทนากับ Phi-4-mini ONNX**

***ONNX*** เป็นรูปแบบเปิดที่สร้างขึ้นเพื่อแทนโมเดลการเรียนรู้ของเครื่อง ONNX กำหนดชุดของโอเปอเรเตอร์ที่ใช้ร่วมกันได้ ซึ่งเป็นส่วนประกอบสำคัญของโมเดลการเรียนรู้ของเครื่องและการเรียนรู้เชิงลึก รวมถึงรูปแบบไฟล์ทั่วไป เพื่อให้นักพัฒนา AI สามารถใช้โมเดลกับเฟรมเวิร์ก เครื่องมือ รันไทม์ และคอมไพเลอร์ที่หลากหลายได้

เรามุ่งหวังที่จะปรับใช้โมเดล AI เชิงสร้างสรรค์บนอุปกรณ์ปลายทาง และใช้งานในสภาพแวดล้อมที่มีพลังการประมวลผลจำกัดหรือออฟไลน์ ตอนนี้เราสามารถบรรลุเป้าหมายนี้ได้โดยการแปลงโมเดลในรูปแบบที่ลดความละเอียด (quantized) เราสามารถแปลงโมเดลที่ลดความละเอียดเป็นรูปแบบ GGUF หรือ ONNX ได้

Microsoft Olive สามารถช่วยคุณแปลง SLM ให้เป็นรูปแบบ ONNX ที่ลดความละเอียดได้ วิธีการแปลงโมเดลนั้นง่ายมาก

**ติดตั้ง Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**แปลงให้รองรับ CPU ONNX**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** ตัวอย่างนี้ใช้ CPU

### **รันโมเดล Phi-4-mini ONNX ด้วย ONNX Runtime GenAI**

- **ติดตั้ง ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **โค้ด Python**

*นี่คือตัวอย่างสำหรับ ONNX Runtime GenAI เวอร์ชัน 0.5.2*

```python

import onnxruntime_genai as og
import numpy as np
import os


model_folder = "Your Phi-4-mini-onnx-cpu-int4 location"


model = og.Model(model_folder)


tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()


search_options = {}
search_options['max_length'] = 2048
search_options['past_present_share_buffer'] = False


chat_template = "<|user|>\n{input}</s>\n<|assistant|>"


text = """Can you introduce yourself"""


prompt = f'{chat_template.format(input=text)}'


input_tokens = tokenizer.encode(prompt)


params = og.GeneratorParams(model)


params.set_search_options(**search_options)
params.input_ids = input_tokens


generator = og.Generator(model, params)


while not generator.is_done():
      generator.compute_logits()
      generator.generate_next_token()

      new_token = generator.get_next_tokens()[0]
      print(tokenizer_stream.decode(new_token), end='', flush=True)

```

*นี่คือตัวอย่างสำหรับ ONNX Runtime GenAI เวอร์ชัน 0.6.0*

```python

import onnxruntime_genai as og
import numpy as np
import os
import time
import psutil

model_folder = "Your Phi-4-mini-onnx model path"

model = og.Model(model_folder)

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

search_options = {}
search_options['max_length'] = 1024
search_options['past_present_share_buffer'] = False

chat_template = "<|user|>{input}<|assistant|>"

text = """can you introduce yourself"""

prompt = f'{chat_template.format(input=text)}'

input_tokens = tokenizer.encode(prompt)

params = og.GeneratorParams(model)

params.set_search_options(**search_options)

generator = og.Generator(model, params)

generator.append_tokens(input_tokens)

while not generator.is_done():
      generator.generate_next_token()

      new_token = generator.get_next_tokens()[0]
      token_text = tokenizer.decode(new_token)
      # print(tokenizer_stream.decode(new_token), end='', flush=True)
      if token_count == 0:
        first_token_time = time.time()
        first_response_latency = first_token_time - start_time
        print(f"firstly token delpay: {first_response_latency:.4f} s")

      print(token_text, end='', flush=True)
      token_count += 1

```

**ข้อจำกัดความรับผิดชอบ**:  
เอกสารนี้ได้รับการแปลโดยใช้บริการแปลภาษาอัตโนมัติที่ขับเคลื่อนด้วยปัญญาประดิษฐ์ (AI) แม้ว่าเราจะพยายามอย่างเต็มที่เพื่อให้การแปลถูกต้อง แต่อย่างไรก็ตาม การแปลอัตโนมัติอาจมีข้อผิดพลาดหรือความไม่ถูกต้องเกิดขึ้นได้ เอกสารต้นฉบับในภาษาต้นทางควรถือเป็นแหล่งข้อมูลที่เชื่อถือได้มากที่สุด สำหรับข้อมูลที่สำคัญ แนะนำให้ใช้บริการแปลภาษามนุษย์ที่เป็นมืออาชีพ เราจะไม่รับผิดชอบต่อความเข้าใจผิดหรือการตีความที่ผิดพลาดซึ่งเกิดจากการใช้การแปลนี้