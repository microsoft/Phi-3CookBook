# **Phi-4-mini ONNX सह चॅट करा**

***ONNX*** हा मशीन लर्निंग मॉडेल्सचे प्रतिनिधित्व करण्यासाठी तयार केलेला एक ओपन फॉरमॅट आहे. ONNX मशीन लर्निंग आणि डीप लर्निंग मॉडेल्सचे बिल्डिंग ब्लॉक्स असलेल्या सामान्य ऑपरेटर्सचा संच आणि एक सामान्य फाइल फॉरमॅट परिभाषित करते, ज्यामुळे AI डेव्हलपर्सना विविध फ्रेमवर्क्स, टूल्स, रनटाइम्स आणि कंपाइलर्ससह मॉडेल्स वापरणे शक्य होते.

आम्ही जनरेटिव्ह AI मॉडेल्सला एज डिव्हाइसेसवर तैनात करण्याची आणि मर्यादित संगणन शक्ती किंवा ऑफलाइन वातावरणात त्यांचा वापर करण्याची आशा करतो. आता आम्ही मॉडेलला क्वांटाइझ्ड प्रकारात रूपांतरित करून हे उद्दिष्ट साध्य करू शकतो. आम्ही क्वांटाइझ्ड मॉडेल GGUF किंवा ONNX फॉरमॅटमध्ये रूपांतरित करू शकतो.

मायक्रोसॉफ्ट ऑलिव्ह तुम्हाला SLM ला क्वांटाइझ्ड ONNX फॉरमॅटमध्ये रूपांतरित करण्यात मदत करू शकते. मॉडेल रूपांतरण साध्य करण्याची पद्धत अतिशय सोपी आहे.

**मायक्रोसॉफ्ट ऑलिव्ह SDK स्थापित करा**

```bash

pip install olive-ai

pip install transformers

```

**CPU ONNX समर्थन रूपांतरित करा**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** या उदाहरणात CPU वापरले आहे.

### **ONNX Runtime GenAI सह Phi-4-mini ONNX मॉडेलचे इनफरन्स**

- **ONNX Runtime GenAI स्थापित करा**

```bash

pip install --pre onnxruntime-genai

```

- **Python कोड**

*हे ONNX Runtime GenAI 0.5.2 आवृत्ती आहे*

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

*हे ONNX Runtime GenAI 0.6.0 आवृत्ती आहे*

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

**अस्वीकरण**:  
हे दस्तऐवज मशीन-आधारित एआय अनुवाद सेवांचा वापर करून अनुवादित केले गेले आहे. आम्ही अचूकतेसाठी प्रयत्नशील असलो तरी, कृपया लक्षात घ्या की स्वयंचलित अनुवादांमध्ये त्रुटी किंवा अचूकतेचा अभाव असू शकतो. मूळ भाषेतील मूळ दस्तऐवज हा प्राधिकृत स्रोत मानला जावा. महत्त्वाच्या माहितीकरिता व्यावसायिक मानव अनुवादाची शिफारस केली जाते. या अनुवादाचा वापर करून उद्भवलेल्या कोणत्याही गैरसमज किंवा चुकीच्या अर्थासाठी आम्ही जबाबदार राहणार नाही.