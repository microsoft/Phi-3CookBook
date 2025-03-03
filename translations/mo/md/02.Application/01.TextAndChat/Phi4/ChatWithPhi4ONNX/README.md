# **Phi-4-mini ONNX-тай харилцах**

***ONNX*** нь машин сургалтын загваруудыг илэрхийлэхэд зориулсан нээлттэй формат юм. ONNX нь машин сургалт болон гүнзгий сургалтын загваруудын үндсэн элемент болох нийтлэг операторуудын багц, мөн загваруудыг янз бүрийн хүрээ, хэрэгсэл, гүйцэтгэлийн орчин, компайлераар ашиглах боломжтой нийтлэг файл форматыг тодорхойлдог.

Бид генератив хиймэл оюуны загваруудыг захын төхөөрөмжүүд дээр байршуулж, хязгаарлагдмал тооцоолох хүчин чадал эсвэл оффлайн орчинд ашиглахыг хүсэж байна. Одоо бид загварыг тоон хэмжээсээр хувиргах замаар энэ зорилгод хүрч чадна. Тоон хэмжээсээр хувиргасан загварыг GGUF эсвэл ONNX формат руу хөрвүүлж болно.

Microsoft Olive нь SLM-ийг тоон хэмжээсийн ONNX формат руу хөрвүүлэхэд тусална. Загварын хөрвүүлэлт хийх арга маш энгийн.

**Microsoft Olive SDK-г суулгах**

```bash

pip install olive-ai

pip install transformers

```

**CPU ONNX дэмжлэг рүү хөрвүүлэх**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** энэ жишээ CPU ашигласан болно


### **Phi-4-mini ONNX загварыг ONNX Runtime GenAI ашиглан дүгнэлт хийх**

- **ONNX Runtime GenAI-г суулгах**

```bash

pip install --pre onnxruntime-genai

```

- **Python код**

*Энэ бол ONNX Runtime GenAI 0.5.2 хувилбар*

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

*Энэ бол ONNX Runtime GenAI 0.6.0 хувилбар*

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

It seems you've requested a translation to "mo," but it's unclear what specific language or dialect "mo" refers to. Could you clarify the language you're referring to (e.g., Maori, Mongolian, Moore, etc.)? This will help me provide an accurate translation!