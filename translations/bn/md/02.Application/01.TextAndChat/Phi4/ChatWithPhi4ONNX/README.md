# **Phi-4-mini ONNX এর সাথে চ্যাট করুন**

***ONNX*** একটি ওপেন ফরম্যাট যা মেশিন লার্নিং মডেল উপস্থাপনের জন্য তৈরি করা হয়েছে। ONNX একটি সাধারণ অপারেটরের সেট সংজ্ঞায়িত করে - যা মেশিন লার্নিং এবং ডিপ লার্নিং মডেলের ভিত্তি - এবং একটি সাধারণ ফাইল ফরম্যাট প্রদান করে যাতে এআই ডেভেলপাররা বিভিন্ন ফ্রেমওয়ার্ক, টুল, রানটাইম এবং কম্পাইলারের সাথে মডেল ব্যবহার করতে পারেন।

আমরা চাই এজ ডিভাইসগুলোতে জেনারেটিভ এআই মডেল মোতায়েন করতে এবং সীমিত কম্পিউটিং ক্ষমতা বা অফলাইন পরিবেশে এগুলো ব্যবহার করতে। এখন আমরা এই লক্ষ্য অর্জন করতে পারি মডেলটিকে একটি কোয়ান্টাইজড পদ্ধতিতে রূপান্তর করে। আমরা কোয়ান্টাইজড মডেলটিকে GGUF বা ONNX ফরম্যাটে রূপান্তর করতে পারি।

Microsoft Olive আপনাকে SLM-কে কোয়ান্টাইজড ONNX ফরম্যাটে রূপান্তর করতে সাহায্য করতে পারে। মডেল রূপান্তর করার পদ্ধতিটি খুবই সহজ।

**Microsoft Olive SDK ইনস্টল করুন**

```bash

pip install olive-ai

pip install transformers

```

**CPU ONNX সাপোর্টে রূপান্তর করুন**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** এই উদাহরণে CPU ব্যবহার করা হয়েছে।

### **ONNX Runtime GenAI ব্যবহার করে Phi-4-mini ONNX মডেলের ইনফারেন্স**

- **ONNX Runtime GenAI ইনস্টল করুন**

```bash

pip install --pre onnxruntime-genai

```

- **পাইথন কোড**

*এটি ONNX Runtime GenAI 0.5.2 ভার্সন*

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

*এটি ONNX Runtime GenAI 0.6.0 ভার্সন*

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

**অস্বীকৃতি**:  
এই নথি মেশিন-ভিত্তিক কৃত্রিম বুদ্ধিমত্তা অনুবাদ সেবার মাধ্যমে অনূদিত হয়েছে। আমরা যথাসাধ্য সঠিকতা বজায় রাখার চেষ্টা করি, তবে দয়া করে মনে রাখবেন যে স্বয়ংক্রিয় অনুবাদে ত্রুটি বা অসংগতি থাকতে পারে। নথির মূল ভাষায় রচিত আসল সংস্করণটিকে কর্তৃত্বপূর্ণ উৎস হিসাবে বিবেচনা করা উচিত। গুরুত্বপূর্ণ তথ্যের ক্ষেত্রে, পেশাদার মানব অনুবাদের সুপারিশ করা হয়। এই অনুবাদ ব্যবহারের ফলে কোনো ভুল বোঝাবুঝি বা ভুল ব্যাখ্যার জন্য আমরা দায়ী থাকব না।