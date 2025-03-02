# **Phi-4-mini ONNX के साथ चैट करें**

***ONNX*** एक ओपन फॉर्मेट है जिसे मशीन लर्निंग मॉडल्स को रिप्रेज़ेंट करने के लिए बनाया गया है। ONNX मशीन लर्निंग और डीप लर्निंग मॉडल्स के निर्माण खंडों - ऑपरेटर्स - का एक सामान्य सेट और एक सामान्य फाइल फॉर्मेट परिभाषित करता है, जिससे AI डेवलपर्स विभिन्न फ्रेमवर्क्स, टूल्स, रनटाइम्स और कंपाइलर्स के साथ मॉडल्स का उपयोग कर सकते हैं।

हम जनरेटिव AI मॉडल्स को एज डिवाइसेस पर डिप्लॉय करना और उन्हें सीमित कंप्यूटिंग पावर या ऑफलाइन वातावरण में उपयोग करना चाहते हैं। अब हम इस लक्ष्य को मॉडल को क्वांटाइज़ तरीके से कन्वर्ट करके प्राप्त कर सकते हैं। हम क्वांटाइज़ मॉडल को GGUF या ONNX फॉर्मेट में कन्वर्ट कर सकते हैं।

Microsoft Olive आपकी मदद कर सकता है SLM को क्वांटाइज़ ONNX फॉर्मेट में कन्वर्ट करने में। मॉडल कन्वर्ज़न प्राप्त करने का तरीका बहुत ही सरल है।

**Microsoft Olive SDK इंस्टॉल करें**

```bash

pip install olive-ai

pip install transformers

```

**CPU ONNX सपोर्ट कन्वर्ट करें**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** इस उदाहरण में CPU का उपयोग किया गया है।

### **Phi-4-mini ONNX मॉडल का ONNX Runtime GenAI के साथ इनफरेंस करें**

- **ONNX Runtime GenAI इंस्टॉल करें**

```bash

pip install --pre onnxruntime-genai

```

- **Python कोड**

*यह ONNX Runtime GenAI 0.5.2 वर्ज़न है*

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

*यह ONNX Runtime GenAI 0.6.0 वर्ज़न है*

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
यह दस्तावेज़ मशीन-आधारित एआई अनुवाद सेवाओं का उपयोग करके अनुवादित किया गया है। जबकि हम सटीकता के लिए प्रयासरत हैं, कृपया ध्यान दें कि स्वचालित अनुवाद में त्रुटियाँ या अशुद्धियाँ हो सकती हैं। मूल दस्तावेज़, जो इसकी मूल भाषा में है, को आधिकारिक स्रोत माना जाना चाहिए। महत्वपूर्ण जानकारी के लिए, पेशेवर मानव अनुवाद की सिफारिश की जाती है। इस अनुवाद के उपयोग से उत्पन्न किसी भी गलतफहमी या गलत व्याख्या के लिए हम उत्तरदायी नहीं हैं।