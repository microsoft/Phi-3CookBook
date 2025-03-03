# **استخدام Intel OpenVINO لتكميم Phi-3.5**

تُعد شركة Intel واحدة من أقدم مصنعي المعالجات المركزية ولديها عدد كبير من المستخدمين. ومع ظهور التعلم الآلي والتعلم العميق، انضمت Intel أيضًا إلى المنافسة في مجال تسريع الذكاء الاصطناعي. لا تقتصر Intel على استخدام وحدات المعالجة المركزية (CPUs) ووحدات معالجة الرسومات (GPUs) فقط، بل تستخدم أيضًا وحدات معالجة الشبكات العصبية (NPUs).

نطمح لنشر عائلة Phi-3.x على الأجهزة الطرفية، بهدف أن تصبح جزءًا مهمًا من أجهزة الكمبيوتر الذكية وأجهزة الكمبيوتر المساعدة (Copilot PCs). يعتمد تحميل النموذج على الأجهزة الطرفية على تعاون مختلف مصنعي الأجهزة. يركز هذا الفصل بشكل رئيسي على سيناريو تطبيق Intel OpenVINO كنموذج تكميم.

## **ما هو OpenVINO**

OpenVINO هو مجموعة أدوات مفتوحة المصدر تهدف إلى تحسين ونشر نماذج التعلم العميق من السحابة إلى الأطراف. يسرّع OpenVINO استنتاجات التعلم العميق عبر استخدامات متعددة، مثل الذكاء الاصطناعي التوليدي، الفيديو، الصوت، واللغة باستخدام نماذج من أطر عمل شائعة مثل PyTorch، TensorFlow، ONNX، وغيرها. يمكن من خلاله تحويل النماذج وتحسينها ونشرها عبر مجموعة متنوعة من أجهزة Intel® وبيئاتها، سواءً كانت في الموقع أو على الأجهزة أو في المتصفح أو السحابة.

الآن، مع OpenVINO، يمكنك بسرعة تكميم نموذج الذكاء الاصطناعي التوليدي (GenAI) على أجهزة Intel وتسريع استنتاج النموذج.

يدعم OpenVINO حاليًا تحويل Phi-3.5-Vision وPhi-3.5-Instruct إلى نماذج مكممة.

### **إعداد البيئة**

يرجى التأكد من تثبيت التبعيات البيئية التالية. هذا هو ملف requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **تكميم Phi-3.5-Instruct باستخدام OpenVINO**

في الطرفية، قم بتشغيل هذا السكربت:

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **تكميم Phi-3.5-Vision باستخدام OpenVINO**

يرجى تشغيل هذا السكربت باستخدام Python أو Jupyter Lab:

```python

import requests
from pathlib import Path
from ov_phi3_vision import convert_phi3_model
import nncf

if not Path("ov_phi3_vision.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/ov_phi3_vision.py")
    open("ov_phi3_vision.py", "w").write(r.text)


if not Path("gradio_helper.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/notebooks/phi-3-vision/gradio_helper.py")
    open("gradio_helper.py", "w").write(r.text)

if not Path("notebook_utils.py").exists():
    r = requests.get(url="https://raw.githubusercontent.com/openvinotoolkit/openvino_notebooks/latest/utils/notebook_utils.py")
    open("notebook_utils.py", "w").write(r.text)



model_id = "microsoft/Phi-3.5-vision-instruct"
out_dir = Path("../model/phi-3.5-vision-128k-instruct-ov")
compression_configuration = {
    "mode": nncf.CompressWeightsMode.INT4_SYM,
    "group_size": 64,
    "ratio": 0.6,
}
if not out_dir.exists():
    convert_phi3_model(model_id, out_dir, compression_configuration)

```

### **🤖 أمثلة لاستخدام Phi-3.5 مع Intel OpenVINO**

| المختبرات    | الوصف | الانتقال |
| -------- | ------- |  ------- |
| 🚀 مختبر - مقدمة عن Phi-3.5 Instruct  | تعلم كيفية استخدام Phi-3.5 Instruct على جهاز الكمبيوتر الذكي الخاص بك    |  [انتقال](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 مختبر - مقدمة عن Phi-3.5 Vision (الصورة) | تعلم كيفية استخدام Phi-3.5 Vision لتحليل الصور على جهاز الكمبيوتر الذكي الخاص بك      |  [انتقال](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 مختبر - مقدمة عن Phi-3.5 Vision (الفيديو)   | تعلم كيفية استخدام Phi-3.5 Vision لتحليل الفيديو على جهاز الكمبيوتر الذكي الخاص بك    |  [انتقال](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **الموارد**

1. تعرف على المزيد حول Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. مستودع GitHub الخاص بـ Intel OpenVINO [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**إخلاء المسؤولية**:  
تمت ترجمة هذا المستند باستخدام خدمات الترجمة الآلية المعتمدة على الذكاء الاصطناعي. بينما نسعى لتحقيق الدقة، يُرجى العلم أن الترجمات الآلية قد تحتوي على أخطاء أو معلومات غير دقيقة. يجب اعتبار المستند الأصلي بلغته الأصلية المصدر الموثوق. للحصول على معلومات حساسة أو حاسمة، يُوصى باللجوء إلى ترجمة بشرية احترافية. نحن غير مسؤولين عن أي سوء فهم أو تفسيرات خاطئة تنشأ عن استخدام هذه الترجمة.