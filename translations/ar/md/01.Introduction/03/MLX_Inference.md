# **استخدام Phi-3 مع إطار عمل Apple MLX**

## **ما هو إطار عمل MLX**

MLX هو إطار عمل خاص بأبحاث تعلم الآلة على أجهزة Apple silicon، مقدم من فريق أبحاث تعلم الآلة في Apple.

تم تصميم MLX من قبل باحثي تعلم الآلة لباحثي تعلم الآلة. يهدف الإطار إلى أن يكون سهل الاستخدام، ولكنه في الوقت نفسه فعال في تدريب ونشر النماذج. تصميم الإطار نفسه بسيط من الناحية المفاهيمية. نسعى لجعل عملية توسيع وتحسين MLX سهلة للباحثين بهدف استكشاف الأفكار الجديدة بسرعة.

يمكن تسريع نماذج اللغات الكبيرة (LLMs) على أجهزة Apple Silicon باستخدام MLX، ويمكن تشغيل النماذج محليًا بسهولة كبيرة.

## **استخدام MLX لتشغيل Phi-3-mini**

### **1. إعداد بيئة MLX الخاصة بك**

1. Python 3.11.x  
2. تثبيت مكتبة MLX  

```bash

pip install mlx-lm

```

### **2. تشغيل Phi-3-mini في الطرفية باستخدام MLX**

```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

النتيجة (بيئتي هي Apple M1 Max، 64GB) هي:

![Terminal](../../../../../translated_images/01.0d0f100b646a4e4c4f1cd36c1a05727cd27f1e696ed642c06cf6e2c9bbf425a4.ar.png)

### **3. تصغير حجم Phi-3-mini باستخدام MLX في الطرفية**

```bash

python -m mlx_lm.convert --hf-path microsoft/Phi-3-mini-4k-instruct

```

***ملاحظة:*** يمكن تصغير حجم النموذج باستخدام mlx_lm.convert، والتصغير الافتراضي هو INT4. هذا المثال يقوم بتصغير Phi-3-mini إلى INT4.

يمكن تصغير حجم النموذج باستخدام mlx_lm.convert، والتصغير الافتراضي هو INT4. هذا المثال يقوم بتصغير Phi-3-mini إلى INT4. بعد التصغير، سيتم تخزينه في الدليل الافتراضي ./mlx_model.

يمكننا اختبار النموذج المصغر باستخدام MLX من الطرفية:

```bash

python -m mlx_lm.generate --model ./mlx_model/ --max-token 2048 --prompt  "<|user|>\nCan you introduce yourself<|end|>\n<|assistant|>"

```

النتيجة هي:

![INT4](../../../../../translated_images/02.04e0be1f18a90a58ad47e0c9d9084ac94d0f1a8c02fa707d04dd2dfc7e9117c6.ar.png)

### **4. تشغيل Phi-3-mini باستخدام MLX في Jupyter Notebook**

![Notebook](../../../../../translated_images/03.0cf0092fe143357656bb5a7bc6427c41d8528d772d38a82d0b2693e2a3eeb16e.ar.png)

***ملاحظة:*** يرجى قراءة هذا المثال [اضغط هنا](../../../../../code/03.Inference/MLX/MLX_DEMO.ipynb)

## **الموارد**

1. تعرف على إطار عمل Apple MLX [https://ml-explore.github.io](https://ml-explore.github.io/mlx/build/html/index.html)

2. مستودع Apple MLX على GitHub [https://github.com/ml-explore](https://github.com/ml-explore)

**إخلاء المسؤولية**:  
تم ترجمة هذا المستند باستخدام خدمات الترجمة الآلية المدعومة بالذكاء الاصطناعي. بينما نسعى لتحقيق الدقة، يُرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو عدم دقة. يجب اعتبار المستند الأصلي بلغته الأصلية هو المصدر الرسمي والموثوق. بالنسبة للمعلومات الحساسة أو الهامة، يُوصى بالاستعانة بترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة ناتجة عن استخدام هذه الترجمة.