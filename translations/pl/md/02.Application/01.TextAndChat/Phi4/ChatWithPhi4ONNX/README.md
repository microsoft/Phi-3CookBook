# **Rozmowa z Phi-4-mini ONNX**

***ONNX*** to otwarty format stworzony do reprezentowania modeli uczenia maszynowego. ONNX definiuje wspólny zestaw operatorów - elementów składowych modeli uczenia maszynowego i głębokiego uczenia - oraz wspólny format plików, umożliwiając deweloperom AI korzystanie z modeli w różnych frameworkach, narzędziach, środowiskach uruchomieniowych i kompilatorach.

Chcemy wdrażać generatywne modele AI na urządzeniach brzegowych i używać ich w środowiskach o ograniczonej mocy obliczeniowej lub offline. Teraz możemy osiągnąć ten cel, konwertując model w sposób kwantyzowany. Możemy przekonwertować model kwantyzowany do formatu GGUF lub ONNX.

Microsoft Olive może pomóc Ci przekonwertować SLM do kwantyzowanego formatu ONNX. Metoda konwersji modelu jest bardzo prosta.

**Zainstaluj Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**Konwersja obsługi ONNX dla CPU**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** w tym przykładzie używany jest CPU.

### **Wnioskowanie dla modelu Phi-4-mini ONNX z ONNX Runtime GenAI**

- **Zainstaluj ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Kod w Pythonie**

*To jest wersja ONNX Runtime GenAI 0.5.2*

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

*To jest wersja ONNX Runtime GenAI 0.6.0*

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

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za źródło autorytatywne. W przypadku informacji krytycznych zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.