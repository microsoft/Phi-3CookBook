# **与 Phi-4-mini ONNX 聊天**

***ONNX*** 是一种开放格式，用于表示机器学习模型。ONNX 定义了一组通用的操作符——机器学习和深度学习模型的构建模块——以及一种通用的文件格式，使 AI 开发者能够在多种框架、工具、运行时和编译器之间使用模型。

我们希望将生成式 AI 模型部署到边缘设备上，并在有限的计算能力或离线环境中使用它们。现在，通过量化的方式转换模型，我们可以实现这一目标。我们可以将量化后的模型转换为 GGUF 或 ONNX 格式。

Microsoft Olive 可以帮助您将 SLM 转换为量化的 ONNX 格式。实现模型转换的方法非常简单。

**安装 Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**转换为支持 CPU 的 ONNX 格式**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***注意*** 这个示例使用 CPU。

### **使用 ONNX Runtime GenAI 推理 Phi-4-mini ONNX 模型**

- **安装 ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **Python 代码**

*这是 ONNX Runtime GenAI 0.5.2 版本*

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

*这是 ONNX Runtime GenAI 0.6.0 版本*

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

**免责声明**：  
本文档通过基于机器的人工智能翻译服务翻译而成。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文的母语版本作为权威来源。对于关键信息，建议寻求专业人工翻译服务。对于因使用本翻译而引起的任何误解或误读，我们概不负责。