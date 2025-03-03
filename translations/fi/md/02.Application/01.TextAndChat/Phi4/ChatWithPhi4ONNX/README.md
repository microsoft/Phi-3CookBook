# **Keskustele Phi-4-mini ONNX:n kanssa**

***ONNX*** on avoin formaatti, joka on suunniteltu koneoppimismallien esittämiseen. ONNX määrittelee yhteisen joukon operaattoreita - koneoppimisen ja syväoppimisen mallien rakennuspalikoita - sekä yhteisen tiedostomuodon, joka mahdollistaa tekoälykehittäjille mallien käytön eri kehysten, työkalujen, ajonaikaympäristöjen ja kääntäjien kanssa.

Tavoitteenamme on ottaa käyttöön generatiivisia tekoälymalleja reunalaitteilla ja käyttää niitä rajallisen laskentatehon tai offline-ympäristöjen yhteydessä. Nyt voimme saavuttaa tämän tavoitteen muuntamalla mallin kvantisoidussa muodossa. Voimme muuntaa kvantisoidun mallin GGUF- tai ONNX-muotoon.

Microsoft Olive voi auttaa sinua muuntamaan SLM:n kvantisoituun ONNX-muotoon. Mallin muuntaminen on hyvin yksinkertaista.

**Asenna Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**Muunna CPU ONNX -tuki**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Huomio*** tämä esimerkki käyttää CPU:ta.

### **Phi-4-mini ONNX -mallin päättely ONNX Runtime GenAI:n avulla**

- **Asenna ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Python-koodi**

*Tämä on ONNX Runtime GenAI 0.5.2 -versio*

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

*Tämä on ONNX Runtime GenAI 0.6.0 -versio*

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

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisilla tekoälyyn perustuvilla käännöspalveluilla. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittistä tietoa varten suositellaan ammattimaisen ihmiskääntäjän käyttöä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.