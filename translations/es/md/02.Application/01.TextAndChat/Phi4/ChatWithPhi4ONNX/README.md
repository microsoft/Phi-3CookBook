# **Chat con Phi-4-mini ONNX**

***ONNX*** es un formato abierto diseñado para representar modelos de aprendizaje automático. ONNX define un conjunto común de operadores, que son los bloques de construcción de modelos de aprendizaje automático y aprendizaje profundo, y un formato de archivo común para permitir que los desarrolladores de IA utilicen modelos con una variedad de frameworks, herramientas, entornos de ejecución y compiladores.

Esperamos implementar modelos de IA generativa en dispositivos de borde y usarlos en entornos con poder de cómputo limitado o sin conexión. Ahora podemos lograr este objetivo convirtiendo el modelo de una manera cuantizada. Podemos convertir el modelo cuantizado al formato GGUF o ONNX.

Microsoft Olive puede ayudarte a convertir SLM al formato ONNX cuantizado. El método para lograr la conversión del modelo es muy sencillo.

**Instalar Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**Convertir soporte para CPU ONNX**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Nota*** este ejemplo utiliza CPU.

### **Inferencia del modelo Phi-4-mini ONNX con ONNX Runtime GenAI**

- **Instalar ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Código en Python**

*Esta es la versión 0.5.2 de ONNX Runtime GenAI*

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

*Esta es la versión 0.6.0 de ONNX Runtime GenAI*

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

**Descargo de responsabilidad**:  
Este documento ha sido traducido utilizando servicios de traducción automática basados en inteligencia artificial. Si bien nos esforzamos por lograr precisión, tenga en cuenta que las traducciones automatizadas pueden contener errores o imprecisiones. El documento original en su idioma nativo debe considerarse como la fuente autorizada. Para información crítica, se recomienda una traducción profesional realizada por humanos. No nos hacemos responsables de malentendidos o interpretaciones erróneas que puedan surgir del uso de esta traducción.