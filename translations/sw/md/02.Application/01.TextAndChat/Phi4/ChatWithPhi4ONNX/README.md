# **Zungumza na Phi-4-mini ONNX**

***ONNX*** ni muundo wa wazi uliotengenezwa kuwakilisha mifano ya ujifunzaji wa mashine. ONNX hufafanua seti ya kawaida ya waendeshaji - vipengele vya msingi vya mifano ya ujifunzaji wa mashine na ujifunzaji wa kina - na muundo wa faili wa kawaida unaowezesha watengenezaji wa AI kutumia mifano na mifumo, zana, mazingira ya utekelezaji, na wakusanyaji tofauti.

Tunalenga kupeleka mifano ya AI inayozalisha kwenye vifaa vya ukingoni na kuitumia katika mazingira yenye nguvu ndogo ya kompyuta au yasiyo na mtandao. Sasa tunaweza kufanikisha lengo hili kwa kubadilisha mfano kwa njia ya upunguzaji wa ukubwa. Tunaweza kubadilisha mfano uliopunguzwa ukubwa kuwa katika muundo wa GGUF au ONNX.

Microsoft Olive inaweza kukusaidia kubadilisha SLM kuwa muundo wa ONNX uliopunguzwa ukubwa. Njia ya kufanikisha ubadilishaji wa mfano ni rahisi sana.

**Sakinisha Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**Badilisha Usaidizi wa CPU ONNX**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** mfano huu unatumia CPU

### **Kutumia Mfano wa Phi-4-mini ONNX Kwa Utekelezaji wa ONNX Runtime GenAI**

- **Sakinisha ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Msimbo wa Python**

*Hii ni toleo la ONNX Runtime GenAI 0.5.2*

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

*Hii ni toleo la ONNX Runtime GenAI 0.6.0*

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

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za tafsiri za kiakili za mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya kiasili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa taarifa muhimu, inashauriwa kutumia tafsiri ya kibinadamu ya kitaalamu. Hatutawajibika kwa kutoelewana au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.