# **Chat med Phi-4-mini ONNX**

***ONNX*** er et åbent format designet til at repræsentere maskinlæringsmodeller. ONNX definerer et fælles sæt af operatorer - byggestenene for maskinlærings- og dyb læringsmodeller - samt et fælles filformat, der gør det muligt for AI-udviklere at bruge modeller med forskellige frameworks, værktøjer, køretider og compilere.

Vi håber at kunne implementere generative AI-modeller på edge-enheder og bruge dem i miljøer med begrænset regnekraft eller offline. Nu kan vi nå dette mål ved at konvertere modellen på en kvantiseret måde. Vi kan konvertere den kvantiserede model til GGUF- eller ONNX-format.

Microsoft Olive kan hjælpe dig med at konvertere SLM til kvantiseret ONNX-format. Metoden til at opnå modelkonvertering er meget enkel.

**Installer Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**Konverter CPU ONNX Support**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** dette eksempel bruger CPU


### **Inferens med Phi-4-mini ONNX-model via ONNX Runtime GenAI**

- **Installer ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Python-kode**

*Dette er version 0.5.2 af ONNX Runtime GenAI*

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


*Dette er version 0.6.0 af ONNX Runtime GenAI*

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

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.