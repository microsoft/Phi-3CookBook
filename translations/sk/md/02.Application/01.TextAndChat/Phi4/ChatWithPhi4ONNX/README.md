# **Chat s Phi-4-mini ONNX**

***ONNX*** je otvorený formát určený na reprezentáciu modelov strojového učenia. ONNX definuje spoločnú sadu operátorov - stavebné bloky modelov strojového a hlbokého učenia - a spoločný formát súborov, ktorý umožňuje vývojárom AI používať modely s rôznymi frameworkmi, nástrojmi, runtime prostrediami a kompilátormi.

Dúfame, že nasadíme generatívne AI modely na zariadeniach na okraji siete a budeme ich používať v prostredí s obmedzeným výpočtovým výkonom alebo offline. Tento cieľ môžeme dosiahnuť konvertovaním modelu kvantizovaným spôsobom. Kvantizovaný model môžeme previesť do formátu GGUF alebo ONNX.

Microsoft Olive vám môže pomôcť previesť SLM do kvantizovaného formátu ONNX. Metóda na dosiahnutie konverzie modelu je veľmi jednoduchá.

**Nainštalujte Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**Konverzia pre podporu CPU ONNX**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Poznámka*** tento príklad používa CPU.

### **Inference Phi-4-mini ONNX modelu s ONNX Runtime GenAI**

- **Nainštalujte ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Python kód**

*Toto je verzia ONNX Runtime GenAI 0.5.2*

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

*Toto je verzia ONNX Runtime GenAI 0.6.0*

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

**Upozornenie**:  
Tento dokument bol preložený pomocou služieb strojového prekladu založeného na umelej inteligencii. Aj keď sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.