# **الدردشة مع Phi-4-mini ONNX**

***ONNX*** هو تنسيق مفتوح مصمم لتمثيل نماذج التعلم الآلي. يعرّف ONNX مجموعة مشتركة من المشغلين - وهي المكونات الأساسية لنماذج التعلم الآلي والتعلم العميق - بالإضافة إلى تنسيق ملف مشترك يمكّن مطوري الذكاء الاصطناعي من استخدام النماذج مع مجموعة متنوعة من الأطر والأدوات وبيئات التشغيل والمترجمات.

نطمح إلى نشر نماذج الذكاء الاصطناعي التوليدي على الأجهزة الطرفية واستخدامها في بيئات ذات قدرة حوسبة محدودة أو في وضع عدم الاتصال. يمكننا الآن تحقيق هذا الهدف عن طريق تحويل النموذج إلى صيغة مكودة (quantized). يمكننا تحويل النموذج المكود إلى صيغة GGUF أو ONNX.

يمكن لـ Microsoft Olive مساعدتك في تحويل SLM إلى صيغة ONNX المكودة. الطريقة لتحقيق تحويل النموذج بسيطة جدًا.

**تثبيت Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**تحويل دعم CPU ONNX**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***ملاحظة*** هذا المثال يستخدم CPU

### **تشغيل نموذج Phi-4-mini ONNX باستخدام ONNX Runtime GenAI**

- **تثبيت ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **كود Python**

*هذا إصدار ONNX Runtime GenAI 0.5.2*

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

*هذا إصدار ONNX Runtime GenAI 0.6.0*

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

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمات الترجمة الآلية المعتمدة على الذكاء الاصطناعي. بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الرسمي. للحصول على معلومات حاسمة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسير خاطئ ناتج عن استخدام هذه الترجمة.