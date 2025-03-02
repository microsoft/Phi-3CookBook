# **Bercakap dengan Phi-4-mini ONNX**

***ONNX*** adalah format terbuka yang dirancang untuk merepresentasikan model pembelajaran mesin. ONNX mendefinisikan satu set operator umum - elemen dasar dari model pembelajaran mesin dan pembelajaran mendalam - serta format file umum untuk memungkinkan pengembang AI menggunakan model dengan berbagai kerangka kerja, alat, runtime, dan kompiler.

Kami berharap dapat menerapkan model AI generatif pada perangkat edge dan menggunakannya dalam lingkungan dengan daya komputasi terbatas atau offline. Sekarang, kami dapat mencapai tujuan ini dengan mengonversi model secara terkuantisasi. Kami dapat mengonversi model yang telah dikuantisasi ke format GGUF atau ONNX.

Microsoft Olive dapat membantu Anda mengonversi SLM ke format ONNX yang telah dikuantisasi. Metode untuk mencapai konversi model ini sangat sederhana.

**Pasang Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**Konversi Dukungan ONNX untuk CPU**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Catatan*** contoh ini menggunakan CPU.

### **Inferensi Model Phi-4-mini ONNX Dengan ONNX Runtime GenAI**

- **Pasang ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Kode Python**

*Ini adalah versi ONNX Runtime GenAI 0.5.2*

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

*Ini adalah versi ONNX Runtime GenAI 0.6.0*

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

**Penafian**:  
Dokumen ini telah diterjemahkan menggunakan layanan terjemahan berbasis AI. Meskipun kami berupaya untuk memastikan akurasi, harap disadari bahwa terjemahan otomatis mungkin mengandung kesalahan atau ketidakakuratan. Dokumen asli dalam bahasa aslinya harus dianggap sebagai sumber yang berwenang. Untuk informasi yang bersifat kritis, disarankan untuk menggunakan jasa terjemahan manusia profesional. Kami tidak bertanggung jawab atas kesalahpahaman atau salah penafsiran yang timbul dari penggunaan terjemahan ini.