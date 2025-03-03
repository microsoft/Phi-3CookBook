# **Makipag-usap gamit ang Phi-4-mini ONNX**

***ONNX*** ay isang bukas na format na ginawa upang kumatawan sa mga modelo ng machine learning. Ang ONNX ay nagtatakda ng karaniwang hanay ng mga operator - ang mga pundasyon ng mga modelo ng machine learning at deep learning - at isang karaniwang format ng file upang bigyang-daan ang mga AI developer na gumamit ng mga modelo sa iba't ibang mga framework, tools, runtimes, at compilers.

Layunin naming i-deploy ang mga generative AI model sa mga edge device at gamitin ang mga ito sa mga limitadong computing power o offline na kapaligiran. Ngayon, maaari na nating makamit ang layuning ito sa pamamagitan ng pag-convert ng modelo sa isang quantized na paraan. Maaari nating i-convert ang quantized na modelo sa GGUF o ONNX format.

Makakatulong ang Microsoft Olive na i-convert ang SLM sa quantized ONNX format. Napakadali ng paraan para makamit ang conversion ng modelo.

**I-install ang Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**I-convert para sa CPU ONNX Support**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** ang halimbawang ito ay gumagamit ng CPU

### **Gumamit ng Phi-4-mini ONNX Model Gamit ang ONNX Runtime GenAI**

- **I-install ang ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Python Code**

*Ito ay ONNX Runtime GenAI bersyon 0.5.2*

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

*Ito ay ONNX Runtime GenAI bersyon 0.6.0*

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

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyong machine-based AI translation. Bagama't sinisikap naming maging wasto, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na pinagmulan. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot para sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.