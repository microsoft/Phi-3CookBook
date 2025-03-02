# **Чат с Phi-4-mini ONNX**

***ONNX*** — это открытый формат, созданный для представления моделей машинного обучения. ONNX определяет общий набор операторов — строительные блоки моделей машинного и глубокого обучения — и общий файловый формат, позволяющий разработчикам ИИ использовать модели с различными фреймворками, инструментами, средами выполнения и компиляторами.

Мы стремимся развертывать генеративные модели ИИ на устройствах с ограниченными вычислительными ресурсами или в оффлайн-режиме. Теперь мы можем достичь этой цели, преобразовав модель в квантизированном формате. Мы можем преобразовать квантизированную модель в формат GGUF или ONNX.

Microsoft Olive может помочь вам преобразовать SLM в квантизированный формат ONNX. Метод преобразования модели очень прост.

**Установка Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**Преобразование с поддержкой CPU ONNX**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Примечание***: в этом примере используется CPU.

### **Инференс модели Phi-4-mini ONNX с ONNX Runtime GenAI**

- **Установка ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Код на Python**

*Это версия ONNX Runtime GenAI 0.5.2*

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

*Это версия ONNX Runtime GenAI 0.6.0*

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

**Отказ от ответственности**:  
Этот документ был переведен с использованием автоматизированных AI-сервисов перевода. Хотя мы стремимся к точности, пожалуйста, имейте в виду, что автоматические переводы могут содержать ошибки или неточности. Оригинальный документ на его исходном языке следует считать авторитетным источником. Для критически важной информации рекомендуется использовать профессиональный перевод человеком. Мы не несем ответственности за недоразумения или неправильные интерпретации, возникшие в результате использования данного перевода.