# **كمية عائلة Phi باستخدام إضافات الذكاء الاصطناعي التوليدي لـ onnxruntime**

## **ما هي إضافات الذكاء الاصطناعي التوليدي لـ onnxruntime**

تساعد هذه الإضافات في تشغيل الذكاء الاصطناعي التوليدي باستخدام ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). توفر هذه الإضافات حلقة الذكاء الاصطناعي التوليدي لنماذج ONNX، بما في ذلك الاستدلال باستخدام ONNX Runtime، ومعالجة logits، والبحث وأخذ العينات، وإدارة ذاكرة التخزين المؤقت KV. يمكن للمطورين استدعاء طريقة generate() عالية المستوى، أو تشغيل كل تكرار للنموذج في حلقة، حيث يتم توليد رمز واحد في كل مرة، مع إمكانية تحديث معلمات التوليد داخل الحلقة. تدعم الإضافات البحث الجشع/الحزمة، وأخذ العينات باستخدام TopP وTopK لتوليد تسلسلات الرموز، بالإضافة إلى معالجة logits المدمجة مثل عقوبات التكرار. كما يمكنك بسهولة إضافة تقييمات مخصصة.

على مستوى التطبيقات، يمكنك استخدام إضافات الذكاء الاصطناعي التوليدي لـ onnxruntime لبناء تطبيقات باستخدام C++/ C# / Python. وعلى مستوى النماذج، يمكنك استخدامها لدمج النماذج المخصصة وإجراء أعمال نشر كمية ذات صلة.

## **كمية Phi-3.5 باستخدام إضافات الذكاء الاصطناعي التوليدي لـ onnxruntime**

### **النماذج المدعومة**

تدعم إضافات الذكاء الاصطناعي التوليدي لـ onnxruntime تحويل الكمية لنماذج Microsoft Phi وGoogle Gemma وMistral وMeta LLaMA.

### **منشئ النماذج في إضافات الذكاء الاصطناعي التوليدي لـ onnxruntime**

يسرّع منشئ النماذج بشكل كبير عملية إنشاء نماذج ONNX المحسّنة والمكمّنة التي تعمل باستخدام واجهة generate() لـ ONNX Runtime.

من خلال منشئ النماذج، يمكنك تقليل كمية النموذج إلى INT4، INT8، FP16، FP32، ودمج طرق تسريع الأجهزة المختلفة مثل CPU وCUDA وDirectML وMobile، إلخ.

لاستخدام منشئ النماذج، تحتاج إلى تثبيت:

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

بعد التثبيت، يمكنك تشغيل سكربت منشئ النماذج من خلال الطرفية لإجراء تحويل صيغة النموذج والكمية.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

فهم المعلمات ذات الصلة:

1. **model_name** هذا هو النموذج الموجود على Hugging Face، مثل microsoft/Phi-3.5-mini-instruct، microsoft/Phi-3.5-vision-instruct، إلخ. يمكن أن يكون أيضًا المسار الذي تخزّن فيه النموذج.

2. **path_to_output_folder** مسار حفظ تحويل الكمية.

3. **execution_provider** دعم تسريع الأجهزة المختلفة، مثل cpu، cuda، DirectML.

4. **cache_dir_to_save_hf_files** نقوم بتنزيل النموذج من Hugging Face وتخزينه مؤقتًا محليًا.

***ملاحظة:***

## **كيفية استخدام منشئ النماذج لتقليل كمية Phi-3.5**

يدعم منشئ النماذج الآن كمية نموذج ONNX لكل من Phi-3.5 Instruct وPhi-3.5-Vision.

### **Phi-3.5-Instruct**

**تحويل مع تسريع CPU لكمية INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**تحويل مع تسريع CUDA لكمية INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. إعداد البيئة في الطرفية:

```bash

mkdir models

cd models 

```

2. تنزيل microsoft/Phi-3.5-vision-instruct في مجلد النماذج  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. يرجى تنزيل هذه الملفات إلى مجلد Phi-3.5-vision-instruct الخاص بك:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. تنزيل هذا الملف إلى مجلد النماذج:  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. الانتقال إلى الطرفية:

    تحويل دعم ONNX مع FP32:

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **ملاحظة:**

1. يدعم منشئ النماذج حاليًا تحويل Phi-3.5-Instruct وPhi-3.5-Vision، ولكنه لا يدعم Phi-3.5-MoE.

2. لاستخدام نموذج ONNX المكمّن، يمكنك استخدامه من خلال SDK الخاص بإضافات الذكاء الاصطناعي التوليدي لـ onnxruntime.

3. يجب علينا مراعاة الذكاء الاصطناعي المسؤول بشكل أكبر، لذلك بعد تحويل كمية النموذج، يُوصى بإجراء اختبارات نتائج فعالة.

4. من خلال تقليل كمية نموذج CPU INT4، يمكننا نشره على الأجهزة الطرفية، مما يوفر سيناريوهات تطبيق أفضل. لذلك، أكملنا Phi-3.5-Instruct حول INT4.

## **المصادر**

1. لمعرفة المزيد عن إضافات الذكاء الاصطناعي التوليدي لـ onnxruntime: [https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. مستودع GitHub لإضافات الذكاء الاصطناعي التوليدي لـ onnxruntime: [https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**إخلاء مسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمات الترجمة الآلية بالاعتماد على الذكاء الاصطناعي. بينما نسعى لتحقيق الدقة، يرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. بالنسبة للمعلومات الحساسة أو الهامة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ نتيجة لاستخدام هذه الترجمة.