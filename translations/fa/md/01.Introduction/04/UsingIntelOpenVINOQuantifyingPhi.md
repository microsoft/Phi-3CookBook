# **کوانتیزه کردن Phi-3.5 با استفاده از Intel OpenVINO**

اینتل یکی از قدیمی‌ترین تولیدکنندگان CPU با کاربران بسیار زیاد است. با ظهور یادگیری ماشین و یادگیری عمیق، اینتل نیز وارد رقابت در زمینه شتاب‌دهی هوش مصنوعی شده است. برای استنتاج مدل‌ها، اینتل نه تنها از GPU و CPU استفاده می‌کند، بلکه از NPU نیز بهره می‌برد.

ما امیدواریم خانواده Phi-3.x را در سمت کاربر نهایی مستقر کنیم و به بخش مهمی از AI PC و Copilot PC تبدیل شویم. بارگذاری مدل در سمت کاربر نهایی به همکاری تولیدکنندگان مختلف سخت‌افزار بستگی دارد. این فصل عمدتاً بر روی سناریوی کاربردی Intel OpenVINO به عنوان یک مدل کوانتیزه شده تمرکز دارد.

## **OpenVINO چیست؟**

OpenVINO یک جعبه ابزار متن‌باز برای بهینه‌سازی و استقرار مدل‌های یادگیری عمیق از فضای ابری تا دستگاه‌های لبه است. این ابزار استنتاج یادگیری عمیق را در موارد استفاده مختلف مانند هوش مصنوعی مولد، ویدئو، صدا و زبان با مدل‌هایی از چارچوب‌های محبوبی مانند PyTorch، TensorFlow، ONNX و غیره تسریع می‌کند. مدل‌ها را تبدیل و بهینه کنید و آن‌ها را در ترکیبی از سخت‌افزارهای اینتل و محیط‌ها، به صورت محلی یا روی دستگاه، در مرورگر یا در فضای ابری مستقر کنید.

اکنون با OpenVINO، می‌توانید مدل GenAI را به سرعت در سخت‌افزار اینتل کوانتیزه کرده و استنتاج مدل را تسریع کنید.

در حال حاضر، OpenVINO از تبدیل کوانتیزه Phi-3.5-Vision و Phi-3.5-Instruct پشتیبانی می‌کند.

### **راه‌اندازی محیط**

لطفاً اطمینان حاصل کنید که وابستگی‌های محیط زیر نصب شده‌اند. این فایل requirement.txt است.

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **کوانتیزه کردن Phi-3.5-Instruct با استفاده از OpenVINO**

در ترمینال، این اسکریپت را اجرا کنید:

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **کوانتیزه کردن Phi-3.5-Vision با استفاده از OpenVINO**

این اسکریپت را در Python یا Jupyter Lab اجرا کنید:

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

### **🤖 نمونه‌هایی برای Phi-3.5 با Intel OpenVINO**

| آزمایشگاه‌ها | معرفی | بروید |
| -------- | ------- |  ------- |
| 🚀 معرفی آزمایشگاه Phi-3.5 Instruct  | یاد بگیرید چگونه از Phi-3.5 Instruct در AI PC خود استفاده کنید    |  [بروید](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 معرفی آزمایشگاه Phi-3.5 Vision (تصویر) | یاد بگیرید چگونه از Phi-3.5 Vision برای تحلیل تصویر در AI PC خود استفاده کنید      |  [بروید](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 معرفی آزمایشگاه Phi-3.5 Vision (ویدئو)   | یاد بگیرید چگونه از Phi-3.5 Vision برای تحلیل ویدئو در AI PC خود استفاده کنید    |  [بروید](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **منابع**

1. اطلاعات بیشتر درباره Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. مخزن GitHub مربوط به Intel OpenVINO [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**سلب مسئولیت**:  
این سند با استفاده از خدمات ترجمه ماشینی مبتنی بر هوش مصنوعی ترجمه شده است. در حالی که ما تلاش می‌کنیم دقت را حفظ کنیم، لطفاً توجه داشته باشید که ترجمه‌های خودکار ممکن است حاوی اشتباهات یا نادرستی باشند. سند اصلی به زبان بومی خود باید به عنوان منبع معتبر در نظر گرفته شود. برای اطلاعات حیاتی، ترجمه حرفه‌ای انسانی توصیه می‌شود. ما هیچ مسئولیتی در قبال سوءتفاهم‌ها یا برداشت‌های نادرست ناشی از استفاده از این ترجمه نداریم.