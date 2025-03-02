# **Phi-4-mini ONNX सँग कुराकानी गर्नुहोस्**

***ONNX*** एउटा खुला ढाँचा हो जुन मेसिन लर्निङ मोडेललाई प्रतिनिधित्व गर्नका लागि बनाइएको हो। ONNX ले मेसिन लर्निङ र डिप लर्निङ मोडेलका लागि आधारभूत निर्माण खण्डका रूपमा सामान्य सेटका अपरेटरहरू र सामान्य फाइल ढाँचा परिभाषित गर्छ। यसले एआई विकासकर्ताहरूलाई विभिन्न फ्रेमवर्क, उपकरण, रनटाइम, र कम्पाइलरहरूसँग मोडेल प्रयोग गर्न सक्षम बनाउँछ। 

हामी जेनेरेटिभ एआई मोडेलहरूलाई एज डिभाइसहरूमा तैनाथ गर्न र सीमित कम्प्युटिङ पावर वा अफलाइन वातावरणमा प्रयोग गर्न चाहन्छौं। अब हामी यो लक्ष्यलाई मोडेललाई क्वान्टाइज्ड तरिकामा रूपान्तरण गरेर हासिल गर्न सक्छौं। हामी क्वान्टाइज्ड मोडेललाई GGUF वा ONNX ढाँचामा रूपान्तरण गर्न सक्छौं।

Microsoft Olive ले SLM लाई क्वान्टाइज्ड ONNX ढाँचामा रूपान्तरण गर्न मद्दत गर्दछ। मोडेल रूपान्तरण हासिल गर्ने विधि धेरै सरल छ।

**Microsoft Olive SDK स्थापना गर्नुहोस्**

```bash

pip install olive-ai

pip install transformers

```

**CPU ONNX समर्थन रूपान्तरण गर्नुहोस्**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** यो उदाहरण CPU प्रयोग गर्दछ।

### **ONNX Runtime GenAI प्रयोग गरेर Phi-4-mini ONNX मोडेल इन्फरेन्स गर्नुहोस्**

- **ONNX Runtime GenAI स्थापना गर्नुहोस्**

```bash

pip install --pre onnxruntime-genai

```

- **Python कोड**

*यो ONNX Runtime GenAI 0.5.2 संस्करण हो*

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

*यो ONNX Runtime GenAI 0.6.0 संस्करण हो*

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
यो दस्तावेज मेसिन-आधारित एआई अनुवाद सेवाहरू प्रयोग गरेर अनुवाद गरिएको हो। हामी शुद्धताका लागि प्रयास गर्छौं, तर कृपया जानकार हुनुहोस् कि स्वचालित अनुवादमा त्रुटिहरू वा असमानताहरू हुन सक्छ। यसको मौलिक भाषामा रहेको मूल दस्तावेजलाई प्राधिकृत स्रोत मानिनुपर्छ। महत्वपूर्ण जानकारीका लागि, व्यावसायिक मानव अनुवाद सिफारिस गरिन्छ। यस अनुवादको प्रयोगबाट उत्पन्न कुनै पनि गलतफहमी वा गलत व्याख्याका लागि हामी जिम्मेवार हुनेछैनौं।  