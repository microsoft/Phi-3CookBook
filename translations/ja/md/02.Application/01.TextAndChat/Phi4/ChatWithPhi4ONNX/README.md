# **Phi-4-mini ONNXと対話する**

***ONNX*** は、機械学習モデルを表現するために設計されたオープンフォーマットです。ONNXは、機械学習や深層学習モデルの構成要素となる共通の演算子セットと、AI開発者がさまざまなフレームワーク、ツール、ランタイム、コンパイラでモデルを使用できるようにする共通のファイル形式を定義しています。

私たちは、エッジデバイス上で生成AIモデルを展開し、計算能力が限られた環境やオフライン環境で使用することを目指しています。この目標は、モデルを量子化することで達成可能です。量子化されたモデルをGGUFまたはONNX形式に変換することができます。

Microsoft Oliveを使用すると、SLMを量子化されたONNX形式に変換することができます。モデル変換を実現する方法は非常に簡単です。

**Microsoft Olive SDKをインストールする**

```bash

pip install olive-ai

pip install transformers

```

**CPU ONNXサポートを変換する**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** この例ではCPUを使用しています。

### **ONNX Runtime GenAIを使ったPhi-4-mini ONNXモデルの推論**

- **ONNX Runtime GenAIをインストールする**

```bash

pip install --pre onnxruntime-genai

```

- **Pythonコード**

*こちらはONNX Runtime GenAIバージョン0.5.2です*

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

*こちらはONNX Runtime GenAIバージョン0.6.0です*

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

**免責事項**:  
この文書は、機械翻訳AIサービスを使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な部分が含まれる可能性があります。元の言語で記載された原文が信頼できる唯一の情報源として考慮されるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の使用により生じた誤解や誤認について、当方は一切の責任を負いません。