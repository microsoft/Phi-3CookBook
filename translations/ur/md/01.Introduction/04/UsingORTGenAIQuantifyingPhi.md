# **Generative AI کی مدد سے Phi فیملی کو Quantize کرنا onnxruntime کے لیے**

## **Generative AI extensions for onnxruntime کیا ہیں؟**

یہ ایکسٹینشنز آپ کو ONNX Runtime کے ساتھ Generative AI چلانے میں مدد دیتی ہیں ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai))۔ یہ ONNX ماڈلز کے لیے Generative AI لوپ فراہم کرتی ہیں، جن میں ONNX Runtime کے ساتھ انفرنس، logits پروسیسنگ، سرچ اور سیمپلنگ، اور KV کیش مینجمنٹ شامل ہیں۔ ڈویلپرز generate() کا ایک اعلیٰ سطحی میتھڈ کال کر سکتے ہیں یا ماڈل کے ہر iteration کو ایک لوپ میں چلا سکتے ہیں، ایک وقت میں ایک ٹوکن جنریٹ کر سکتے ہیں، اور لوپ کے اندر جنریشن پیرامیٹرز کو اپڈیٹ کر سکتے ہیں۔ یہ greedy/beam سرچ اور TopP، TopK سیمپلنگ کو ٹوکن سیکوئنسز بنانے کے لیے سپورٹ کرتی ہے اور repetition penalties جیسے built-in logits پروسیسنگ فراہم کرتی ہے۔ آپ آسانی سے اپنی مرضی کی اسکورنگ بھی شامل کر سکتے ہیں۔

ایپلیکیشن لیول پر، آپ Generative AI extensions for onnxruntime کو C++/C#/Python استعمال کرتے ہوئے ایپلیکیشنز بنانے کے لیے استعمال کر سکتے ہیں۔ ماڈل لیول پر، آپ اسے فائن ٹیونڈ ماڈلز کو مرج کرنے اور متعلقہ quantitative deployment کام کرنے کے لیے استعمال کر سکتے ہیں۔

## **Generative AI extensions for onnxruntime کی مدد سے Phi-3.5 کو Quantize کرنا**

### **سپورٹڈ ماڈلز**

Generative AI extensions for onnxruntime مائیکروسافٹ Phi، گوگل Gemma، Mistral، اور Meta LLaMA کے quantization conversion کو سپورٹ کرتی ہیں۔

### **Generative AI extensions for onnxruntime میں ماڈل بلڈر**

ماڈل بلڈر ONNX Runtime کے generate() API کے ساتھ چلنے والے optimized اور quantized ONNX ماڈلز کو بنانے کے عمل کو تیز کرتا ہے۔

ماڈل بلڈر کے ذریعے، آپ ماڈل کو INT4، INT8، FP16، FP32 میں quantize کر سکتے ہیں اور مختلف ہارڈویئر ایکسیلریشن طریقوں جیسے CPU، CUDA، DirectML، Mobile وغیرہ کو یکجا کر سکتے ہیں۔

ماڈل بلڈر استعمال کرنے کے لیے، آپ کو انسٹال کرنا ہوگا:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

انسٹالیشن کے بعد، آپ ٹرمینل سے ماڈل بلڈر اسکرپٹ چلا کر ماڈل کی فارمیٹ اور quantization conversion کر سکتے ہیں۔

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

متعلقہ پیرامیٹرز کو سمجھیں:

1. **model_name** یہ Hugging Face پر موجود ماڈل ہے، جیسے microsoft/Phi-3.5-mini-instruct، microsoft/Phi-3.5-vision-instruct وغیرہ۔ یہ وہ راستہ بھی ہو سکتا ہے جہاں آپ نے ماڈل محفوظ کیا ہے۔

2. **path_to_output_folder** Quantized conversion کو محفوظ کرنے کا راستہ۔

3. **execution_provider** مختلف ہارڈویئر ایکسیلریشن سپورٹ، جیسے CPU، CUDA، DirectML۔

4. **cache_dir_to_save_hf_files** ہم Hugging Face سے ماڈل ڈاؤنلوڈ کرتے ہیں اور اسے مقامی طور پر کیش کرتے ہیں۔

***نوٹ:***

## **ماڈل بلڈر کے ذریعے Phi-3.5 کو Quantize کرنے کا طریقہ**

ماڈل بلڈر اب Phi-3.5 Instruct اور Phi-3.5-Vision کے لیے ONNX ماڈل quantization کو سپورٹ کرتا ہے۔

### **Phi-3.5-Instruct**

**Quantized INT4 کے لیے CPU ایکسیلریٹڈ کنورژن**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Quantized INT4 کے لیے CUDA ایکسیلریٹڈ کنورژن**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. ٹرمینل میں ماحول سیٹ کریں:

```bash

mkdir models

cd models 

```

2. microsoft/Phi-3.5-vision-instruct کو ماڈلز فولڈر میں ڈاؤنلوڈ کریں:
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. براہ کرم یہ فائلیں اپنے Phi-3.5-vision-instruct فولڈر میں ڈاؤنلوڈ کریں:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. اس فائل کو ماڈلز فولڈر میں ڈاؤنلوڈ کریں:
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. ٹرمینل پر جائیں:

    FP32 کے ساتھ ONNX سپورٹ میں کنورٹ کریں:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **نوٹ:**

1. ماڈل بلڈر فی الحال Phi-3.5-Instruct اور Phi-3.5-Vision کے کنورژن کو سپورٹ کرتا ہے، لیکن Phi-3.5-MoE کو نہیں۔

2. ONNX کے quantized ماڈل کو استعمال کرنے کے لیے، آپ اسے Generative AI extensions for onnxruntime SDK کے ذریعے استعمال کر سکتے ہیں۔

3. ہمیں مزید ذمہ دار AI پر غور کرنا ہوگا، لہذا ماڈل quantization کنورژن کے بعد، زیادہ مؤثر نتیجہ ٹیسٹنگ کی سفارش کی جاتی ہے۔

4. CPU INT4 ماڈل کو quantize کر کے، ہم اسے Edge Devices پر ڈپلائے کر سکتے ہیں، جس کے بہتر ایپلیکیشن سیناریوز ہیں، لہذا ہم نے INT4 کے ارد گرد Phi-3.5-Instruct مکمل کیا ہے۔

## **وسائل**

1. Generative AI extensions for onnxruntime کے بارے میں مزید جانیں:
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime کا GitHub ریپو:
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**ڈسکلیمر**:  
یہ دستاویز مشین پر مبنی AI ترجمہ خدمات کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کی کوشش کرتے ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی مقامی زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمے کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔