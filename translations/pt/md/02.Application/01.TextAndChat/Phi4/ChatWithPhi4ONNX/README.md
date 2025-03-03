# **Converse com Phi-4-mini ONNX**

***ONNX*** é um formato aberto criado para representar modelos de aprendizado de máquina. ONNX define um conjunto comum de operadores - os blocos de construção de modelos de aprendizado de máquina e aprendizado profundo - e um formato de arquivo comum para permitir que desenvolvedores de IA utilizem modelos com uma variedade de frameworks, ferramentas, runtimes e compiladores.

Esperamos implantar modelos de IA generativa em dispositivos de borda e utilizá-los em ambientes com poder computacional limitado ou offline. Agora podemos alcançar esse objetivo convertendo o modelo de forma quantizada. Podemos converter o modelo quantizado para o formato GGUF ou ONNX.

O Microsoft Olive pode ajudá-lo a converter SLM para o formato ONNX quantizado. O método para realizar a conversão do modelo é muito simples.

**Instale o Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**Converter Suporte ONNX para CPU**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** este exemplo utiliza CPU

### **Inferência do Modelo Phi-4-mini ONNX com ONNX Runtime GenAI**

- **Instale o ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Código em Python**

*Esta é a versão 0.5.2 do ONNX Runtime GenAI*

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

*Esta é a versão 0.6.0 do ONNX Runtime GenAI*

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

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se uma tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.