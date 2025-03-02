# **Conversați cu Phi-4-mini ONNX**

***ONNX*** este un format deschis creat pentru a reprezenta modelele de învățare automată. ONNX definește un set comun de operatori - blocurile de bază ale modelelor de învățare automată și profundă - și un format comun de fișier care le permite dezvoltatorilor AI să utilizeze modele cu o varietate de framework-uri, unelte, runtime-uri și compilatoare.

Ne dorim să implementăm modele generative AI pe dispozitive edge și să le folosim în medii cu putere de calcul limitată sau offline. Acum putem atinge acest obiectiv convertind modelul într-un mod cuantificat. Putem converti modelul cuantificat în format GGUF sau ONNX.

Microsoft Olive vă poate ajuta să convertiți SLM în format ONNX cuantificat. Metoda pentru a realiza conversia modelului este foarte simplă.

**Instalați Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**Conversie pentru suport CPU ONNX**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Notă*** acest exemplu utilizează CPU


### **Inferență cu modelul Phi-4-mini ONNX folosind ONNX Runtime GenAI**

- **Instalați ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Cod Python**

*Aceasta este versiunea 0.5.2 a ONNX Runtime GenAI*

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

*Aceasta este versiunea 0.6.0 a ONNX Runtime GenAI*

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

**Declinarea responsabilității**:  
Acest document a fost tradus folosind servicii de traducere bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa nativă ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm responsabilitatea pentru eventualele neînțelegeri sau interpretări greșite care ar putea apărea în urma utilizării acestei traduceri.