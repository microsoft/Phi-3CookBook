# **گفت‌وگو با Phi-4-mini ONNX**

***ONNX*** یک فرمت باز است که برای نمایش مدل‌های یادگیری ماشین طراحی شده است. ONNX مجموعه‌ای مشترک از عملگرها - بلوک‌های سازنده مدل‌های یادگیری ماشین و یادگیری عمیق - و یک فرمت فایل مشترک را تعریف می‌کند تا توسعه‌دهندگان هوش مصنوعی بتوانند مدل‌ها را با انواع فریم‌ورک‌ها، ابزارها، زمان اجراها و کامپایلرها استفاده کنند.

ما امیدواریم مدل‌های هوش مصنوعی مولد را روی دستگاه‌های لبه‌ای مستقر کنیم و از آن‌ها در محیط‌هایی با توان محاسباتی محدود یا آفلاین استفاده کنیم. اکنون می‌توانیم این هدف را با تبدیل مدل به روشی کوانتیزه‌شده محقق کنیم. ما می‌توانیم مدل کوانتیزه‌شده را به فرمت GGUF یا ONNX تبدیل کنیم.

Microsoft Olive می‌تواند به شما کمک کند تا SLM را به فرمت کوانتیزه‌شده ONNX تبدیل کنید. روش دستیابی به تبدیل مدل بسیار ساده است.

**نصب Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**تبدیل پشتیبانی CPU ONNX**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***توجه*** این مثال از CPU استفاده می‌کند.

### **استنتاج مدل Phi-4-mini ONNX با ONNX Runtime GenAI**

- **نصب ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **کد پایتون**

*این نسخه 0.5.2 از ONNX Runtime GenAI است*

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

*این نسخه 0.6.0 از ONNX Runtime GenAI است*

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

**سلب مسئولیت**:  
این سند با استفاده از خدمات ترجمه ماشینی مبتنی بر هوش مصنوعی ترجمه شده است. در حالی که ما برای دقت تلاش می‌کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی اشتباهات یا نادرستی‌هایی باشند. سند اصلی به زبان اصلی خود باید به‌عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حساس، توصیه می‌شود از ترجمه حرفه‌ای انسانی استفاده کنید. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا برداشت‌های نادرست ناشی از استفاده از این ترجمه نداریم.