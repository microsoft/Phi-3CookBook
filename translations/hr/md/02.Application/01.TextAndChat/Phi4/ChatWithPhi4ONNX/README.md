# **Razgovor s Phi-4-mini ONNX**

***ONNX*** je otvoreni format osmišljen za predstavljanje modela strojnog učenja. ONNX definira zajednički skup operatora - osnovne gradivne elemente modela strojnog i dubokog učenja - i zajednički format datoteke kako bi omogućio AI programerima korištenje modela s raznim okvirima, alatima, runtimeovima i kompajlerima.

Nadamo se implementirati generativne AI modele na rubnim uređajima i koristiti ih u okruženjima s ograničenom računalnom snagom ili u offline uvjetima. Sada možemo postići ovaj cilj pretvaranjem modela u kvantizirani oblik. Kvantizirani model možemo pretvoriti u GGUF ili ONNX format.

Microsoft Olive može vam pomoći pretvoriti SLM u kvantizirani ONNX format. Metoda za postizanje konverzije modela vrlo je jednostavna.

**Instalirajte Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**Pretvorba s podrškom za CPU ONNX**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Napomena*** ovaj primjer koristi CPU


### **Inferencija Phi-4-mini ONNX modela s ONNX Runtime GenAI**

- **Instalirajte ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Python kod**

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

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem usluga strojno baziranog AI prevođenja. Iako nastojimo osigurati točnost, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati autoritativnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.