# **Chat met Phi-4-mini ONNX**

***ONNX*** is een open formaat dat is ontwikkeld om machine learning-modellen te representeren. ONNX definieert een gemeenschappelijke set operators - de bouwstenen van machine learning- en deep learning-modellen - en een gemeenschappelijk bestandsformaat, zodat AI-ontwikkelaars modellen kunnen gebruiken met verschillende frameworks, tools, runtimes en compilers.

We hopen generatieve AI-modellen op edge-apparaten te implementeren en deze te gebruiken in omgevingen met beperkte rekenkracht of offline. Nu kunnen we dit doel bereiken door het model op een gequantiseerde manier om te zetten. We kunnen het gequantiseerde model converteren naar GGUF- of ONNX-formaat.

Microsoft Olive kan je helpen om SLM om te zetten naar gequantiseerd ONNX-formaat. De methode om modelconversie te bereiken is heel eenvoudig.

**Installeer Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**Converteren voor CPU ONNX-ondersteuning**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Let op*** dit voorbeeld gebruikt CPU


### **Inference Phi-4-mini ONNX-model met ONNX Runtime GenAI**

- **Installeer ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Python-code**

*Dit is ONNX Runtime GenAI versie 0.5.2*

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

*Dit is ONNX Runtime GenAI versie 0.6.0*

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

**Disclaimer**:  
Dit document is vertaald met behulp van machine-gebaseerde AI-vertalingsdiensten. Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.