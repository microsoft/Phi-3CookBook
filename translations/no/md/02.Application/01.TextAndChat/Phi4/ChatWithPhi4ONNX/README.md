# **Chat med Phi-4-mini ONNX**

***ONNX*** er et åpent format laget for å representere maskinlæringsmodeller. ONNX definerer et felles sett med operatorer – byggesteinene for maskinlærings- og dyp læringsmodeller – og et felles filformat som gjør det mulig for AI-utviklere å bruke modeller med ulike rammeverk, verktøy, kjøringsmiljøer og kompilatorer.

Vi ønsker å distribuere generative AI-modeller på edge-enheter og bruke dem i miljøer med begrenset regnekraft eller offline. Nå kan vi oppnå dette målet ved å konvertere modellen på en kvantisert måte. Vi kan konvertere den kvantiserte modellen til GGUF- eller ONNX-format.

Microsoft Olive kan hjelpe deg med å konvertere SLM til kvantisert ONNX-format. Metoden for å oppnå modellkonvertering er svært enkel.

**Installer Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**Konverter CPU ONNX-støtte**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Merk*** dette eksemplet bruker CPU.

### **Inferens av Phi-4-mini ONNX-modell med ONNX Runtime GenAI**

- **Installer ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Python-kode**

*Dette er ONNX Runtime GenAI versjon 0.5.2*

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

*Dette er ONNX Runtime GenAI versjon 0.6.0*

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
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.