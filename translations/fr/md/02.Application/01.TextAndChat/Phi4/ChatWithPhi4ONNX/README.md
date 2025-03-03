# **Discuter avec Phi-4-mini ONNX**

***ONNX*** est un format ouvert conçu pour représenter les modèles d'apprentissage automatique. ONNX définit un ensemble commun d'opérateurs - les blocs de construction des modèles d'apprentissage automatique et d'apprentissage profond - ainsi qu'un format de fichier commun pour permettre aux développeurs d'IA d'utiliser des modèles avec une variété de frameworks, d'outils, d'environnements d'exécution et de compilateurs.

Nous espérons déployer des modèles d'IA générative sur des appareils en périphérie et les utiliser dans des environnements à puissance de calcul limitée ou hors ligne. Désormais, nous pouvons atteindre cet objectif en convertissant le modèle de manière quantifiée. Nous pouvons convertir le modèle quantifié au format GGUF ou ONNX.

Microsoft Olive peut vous aider à convertir SLM en format ONNX quantifié. La méthode pour effectuer la conversion du modèle est très simple.

**Installer le SDK Microsoft Olive**

```bash

pip install olive-ai

pip install transformers

```

**Convertir pour support CPU ONNX**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** cet exemple utilise le CPU.

### **Inférence du modèle Phi-4-mini ONNX avec ONNX Runtime GenAI**

- **Installer ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Code Python**

*Il s'agit de la version 0.5.2 d'ONNX Runtime GenAI*

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

*Il s'agit de la version 0.6.0 d'ONNX Runtime GenAI*

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

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée basés sur l'intelligence artificielle. Bien que nous fassions de notre mieux pour garantir l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.