# **שוחח עם Phi-4-mini ONNX**

***ONNX*** הוא פורמט פתוח שנבנה כדי לייצג מודלים של למידת מכונה. ONNX מגדיר סט משותף של אופרטורים - אבני הבניין של מודלים של למידת מכונה ולמידה עמוקה - ופורמט קבצים משותף שמאפשר למפתחי AI להשתמש במודלים עם מגוון מסגרות, כלים, זמן ריצה ומהדרים.

אנו שואפים לפרוס מודלים של AI גנרטיבי על מכשירי קצה ולהשתמש בהם בסביבות עם כוח חישוב מוגבל או במצבים לא מקוונים. כעת ניתן להשיג מטרה זו על ידי המרת המודל בצורה כמותית. ניתן להמיר את המודל הכמותי לפורמט GGUF או ONNX.

Microsoft Olive יכולה לעזור לך להמיר SLM לפורמט ONNX כמותי. השיטה להמרת המודל היא פשוטה מאוד.

**התקנת Microsoft Olive SDK**

```bash

pip install olive-ai

pip install transformers

```

**המרת תמיכה ב-CPU ONNX**

```bash

olive auto-opt --model_name_or_path Your Phi-4-mini location --output_path Your onnx ouput location --device cpu --provider CPUExecutionProvider --precision int4 --use_model_builder --log_level 1

```

***Note*** דוגמה זו משתמשת ב-CPU

### **ביצוע הסקה למודל Phi-4-mini ONNX באמצעות ONNX Runtime GenAI**

- **התקנת ONNX Runtime GenAI**

```bash

pip install --pre onnxruntime-genai

```

- **קוד פייתון**

*זוהי גרסה 0.5.2 של ONNX Runtime GenAI*

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

*זוהי גרסה 0.6.0 של ONNX Runtime GenAI*

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

**כתב ויתור**:  
מסמך זה תורגם באמצעות שירותי תרגום מבוססי בינה מלאכותית. למרות שאנו שואפים לדיוק, יש להיות מודעים לכך שתרגומים אוטומטיים עשויים להכיל שגיאות או אי-דיוקים. המסמך המקורי בשפתו המקורית צריך להיחשב כמקור הסמכותי. למידע קריטי, מומלץ להשתמש בתרגום מקצועי על ידי אדם. איננו נושאים באחריות לאי-הבנות או לפרשנויות שגויות הנובעות משימוש בתרגום זה.  