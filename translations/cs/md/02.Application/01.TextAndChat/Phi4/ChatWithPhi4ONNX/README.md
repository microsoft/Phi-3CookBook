# **Chat s Phi-4-mini ONNX**

***ONNX*** je otevřený formát navržený k reprezentaci modelů strojového učení. ONNX definuje společnou sadu operátorů – základní stavební kameny modelů strojového a hlubokého učení – a společný formát souborů, který umožňuje vývojářům AI používat modely s různými frameworky, nástroji, runtime prostředími a kompilátory.

Doufáme, že budeme schopni nasazovat generativní AI modely na edge zařízeních a používat je v prostředích s omezeným výpočetním výkonem nebo offline. Nyní můžeme tohoto cíle dosáhnout převedením modelu kvantizovaným způsobem. Kvantizovaný model můžeme převést do formátu GGUF nebo ONNX.

Microsoft Olive vám může pomoci převést SLM do kvantizovaného formátu ONNX. Metoda pro dosažení konverze modelu je velmi jednoduchá.

**Nainstalujte Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**Převod podpory ONNX pro CPU**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Poznámka*** tento příklad používá CPU.

### **Inferování modelu Phi-4-mini ONNX pomocí ONNX Runtime GenAI**

- **Nainstalujte ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Python kód**

*Toto je verze ONNX Runtime GenAI 0.5.2*

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

*Toto je verze ONNX Runtime GenAI 0.6.0*

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

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových překladatelských služeb AI. Přestože se snažíme o přesnost, vezměte prosím na vědomí, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za závazný zdroj. Pro důležité informace se doporučuje profesionální překlad od člověka. Nenese zodpovědnost za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.