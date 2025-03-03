# **Razgovor sa Phi-4-mini ONNX**

***ONNX*** je otvoreni format razvijen za predstavljanje modela mašinskog učenja. ONNX definiše zajednički skup operatora - osnovne elemente modela mašinskog i dubokog učenja - i zajednički format datoteka kako bi omogućio AI programerima da koriste modele sa različitim okvirima, alatima, okruženjima za izvršavanje i kompajlerima.

Nadamo se da ćemo implementirati generativne AI modele na uređajima na ivici mreže i koristiti ih u okruženjima sa ograničenom računarskom snagom ili u offline režimu. Sada možemo ostvariti ovaj cilj pretvaranjem modela u kvantizovanom obliku. Kvantizovani model možemo pretvoriti u GGUF ili ONNX format.

Microsoft Olive može vam pomoći da konvertujete SLM u kvantizovani ONNX format. Metoda za postizanje konverzije modela je veoma jednostavna.

**Instalirajte Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**Konvertovanje CPU ONNX Podrške**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Napomena*** ovaj primer koristi CPU


### **Inferencija Phi-4-mini ONNX Modela Korišćenjem ONNX Runtime GenAI**

- **Instalirajte ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Python Kod**

*Ovo je verzija ONNX Runtime GenAI 0.5.2*

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


*Ovo je verzija ONNX Runtime GenAI 0.6.0*

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

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења на бази вештачке интелигенције. Иако се трудимо да обезбедимо тачност, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неспоразуме који могу проистећи из коришћења овог превода.