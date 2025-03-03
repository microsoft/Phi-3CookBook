# **ਫਾਈ-4-ਮਿਨੀ ONNX ਨਾਲ ਗੱਲਬਾਤ ਕਰੋ**

***ONNX*** ਇੱਕ ਖੁੱਲ੍ਹਾ ਫਾਰਮੈਟ ਹੈ ਜੋ ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਮਾਡਲਾਂ ਨੂੰ ਪ੍ਰਦਰਸ਼ਿਤ ਕਰਨ ਲਈ ਬਣਾਇਆ ਗਿਆ ਹੈ। ONNX ਮਸ਼ੀਨ ਲਰਨਿੰਗ ਅਤੇ ਡੀਪ ਲਰਨਿੰਗ ਮਾਡਲਾਂ ਦੇ ਬਿਲਡਿੰਗ ਬਲਾਕਾਂ ਲਈ ਇੱਕ ਸਾਂਝਾ ਸੈੱਟ ਪਰਿਭਾਸ਼ਿਤ ਕਰਦਾ ਹੈ ਅਤੇ ਇੱਕ ਸਾਂਝਾ ਫਾਇਲ ਫਾਰਮੈਟ ਮੁਹੱਈਆ ਕਰਦਾ ਹੈ ਤਾਂ ਜੋ AI ਡਿਵੈਲਪਰ ਵੱਖ-ਵੱਖ ਫਰੇਮਵਰਕ, ਟੂਲ, ਰਨਟਾਈਮ ਅਤੇ ਕੰਪਾਈਲਰਾਂ ਨਾਲ ਮਾਡਲਾਂ ਦੀ ਵਰਤੋਂ ਕਰ ਸਕਣ। 

ਅਸੀਂ ਜਨਰੇਟਿਵ AI ਮਾਡਲਾਂ ਨੂੰ ਐਜ ਡਿਵਾਈਸਾਂ 'ਤੇ ਡਿਪਲੋਇ ਕਰਨ ਅਤੇ ਉਨ੍ਹਾਂ ਨੂੰ ਸੀਮਿਤ ਕੰਪਿਊਟਿੰਗ ਪਾਵਰ ਜਾਂ ਆਫਲਾਈਨ ਮਾਹੌਲਾਂ ਵਿੱਚ ਵਰਤਣਾ ਚਾਹੁੰਦੇ ਹਾਂ। ਹੁਣ ਅਸੀਂ ਮਾਡਲ ਨੂੰ ਕਵਾਂਟਾਈਜ਼ਡ ਢੰਗ ਨਾਲ ਕਨਵਰਟ ਕਰਕੇ ਇਸ ਲਕਸ਼ ਨੂੰ ਪ੍ਰਾਪਤ ਕਰ ਸਕਦੇ ਹਾਂ। ਅਸੀਂ ਕਵਾਂਟਾਈਜ਼ਡ ਮਾਡਲ ਨੂੰ GGUF ਜਾਂ ONNX ਫਾਰਮੈਟ ਵਿੱਚ ਬਦਲ ਸਕਦੇ ਹਾਂ।

Microsoft Olive ਤੁਹਾਨੂੰ SLM ਨੂੰ ਕਵਾਂਟਾਈਜ਼ਡ ONNX ਫਾਰਮੈਟ ਵਿੱਚ ਕਨਵਰਟ ਕਰਨ ਵਿੱਚ ਮਦਦ ਕਰ ਸਕਦਾ ਹੈ। ਮਾਡਲ ਕਨਵਰਜ਼ਨ ਹਾਸਲ ਕਰਨ ਦਾ ਤਰੀਕਾ ਬਹੁਤ ਹੀ ਆਸਾਨ ਹੈ।

**Microsoft Olive SDK ਇੰਸਟਾਲ ਕਰੋ**


```bash

pip install olive-ai

pip install transformers

```

**CPU ONNX ਸਪੋਰਟ ਕਨਵਰਟ ਕਰੋ**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** ਇਹ ਉਦਾਹਰਣ CPU ਦੀ ਵਰਤੋਂ ਕਰਦਾ ਹੈ।


### **ONNX ਰਨਟਾਈਮ GenAI ਨਾਲ ਫਾਈ-4-ਮਿਨੀ ONNX ਮਾਡਲ ਦਾ ਇੰਫਰੈਂਸ**

- **ONNX ਰਨਟਾਈਮ GenAI ਇੰਸਟਾਲ ਕਰੋ**

```bash

pip install --pre onnxruntime-genai

```

- **Python ਕੋਡ**

*ਇਹ ONNX ਰਨਟਾਈਮ GenAI 0.5.2 ਵਰਜਨ ਹੈ*

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


*ਇਹ ONNX ਰਨਟਾਈਮ GenAI 0.6.0 ਵਰਜਨ ਹੈ*

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

**ਅਸਵੀਕਤੀ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਮਸ਼ੀਨ-ਆਧਾਰਿਤ AI ਅਨੁਵਾਦ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦਿਤ ਕੀਤਾ ਗਿਆ ਹੈ। ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਪਰ ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਦਿਓ ਕਿ ਸਵੈਚਾਲਿਤ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁਚੱਜੇਪਣ ਹੋ ਸਕਦੇ ਹਨ। ਮੂਲ ਦਸਤਾਵੇਜ਼ ਉਸਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਪ੍ਰਮਾਣਿਕ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪ੍ਰੋਫੈਸ਼ਨਲ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਿਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੇ ਇਸਤੇਮਾਲ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੇ ਕਿਸੇ ਵੀ ਗਲਤ ਫਹਿਮੀ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।