# **Intel OpenVINO کے ذریعے Phi-3.5 کو کوانٹائز کرنا**

Intel سب سے روایتی CPU بنانے والا ہے جس کے بہت سے صارفین ہیں۔ مشین لرننگ اور ڈیپ لرننگ کے عروج کے ساتھ، Intel نے بھی AI ایکسیلیریشن کے مقابلے میں حصہ لیا ہے۔ ماڈل انفرنس کے لیے، Intel نہ صرف GPUs اور CPUs استعمال کرتا ہے بلکہ NPUs بھی استعمال کرتا ہے۔

ہم امید کرتے ہیں کہ Phi-3.x فیملی کو اینڈ سائیڈ پر ڈپلائے کریں تاکہ یہ AI PC اور Copilot PC کا سب سے اہم حصہ بن سکے۔ اینڈ سائیڈ پر ماڈل کی لوڈنگ مختلف ہارڈویئر مینوفیکچررز کے تعاون پر منحصر ہے۔ یہ باب خاص طور پر Intel OpenVINO کے بطور ایک کوانٹائز ماڈل کے ایپلیکیشن سیناریو پر مرکوز ہے۔  

## **OpenVINO کیا ہے؟**

OpenVINO ایک اوپن سورس ٹول کٹ ہے جو ڈیپ لرننگ ماڈلز کو کلاؤڈ سے ایج تک آپٹمائز اور ڈپلائے کرنے کے لیے استعمال ہوتا ہے۔ یہ مختلف یوز کیسز میں ڈیپ لرننگ انفرنس کو تیز کرتا ہے، جیسے کہ جنریٹیو AI، ویڈیو، آڈیو، اور زبان، مشہور فریم ورک جیسے PyTorch، TensorFlow، ONNX وغیرہ کے ماڈلز کے ساتھ۔ ماڈلز کو کنورٹ اور آپٹمائز کریں، اور Intel® ہارڈویئر اور ماحولیات کے مکس میں، آن پرمیسس اور آن ڈیوائس، براؤزر یا کلاؤڈ میں ڈپلائے کریں۔

اب OpenVINO کے ذریعے، آپ Intel ہارڈویئر میں GenAI ماڈل کو جلدی کوانٹائز کر سکتے ہیں اور ماڈل ریفرنس کو تیز کر سکتے ہیں۔

اب OpenVINO Phi-3.5-Vision اور Phi-3.5-Instruct کے کوانٹائز کنورژن کو سپورٹ کرتا ہے۔

### **ماحول کی ترتیب**

براہ کرم یقینی بنائیں کہ درج ذیل ماحول کی ڈیپینڈینسیز انسٹال ہیں، یہ requirement.txt ہے  

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **OpenVINO کے ذریعے Phi-3.5-Instruct کو کوانٹائز کرنا**

ٹرمینل میں، براہ کرم یہ اسکرپٹ چلائیں  

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **OpenVINO کے ذریعے Phi-3.5-Vision کو کوانٹائز کرنا**

براہ کرم یہ اسکرپٹ Python یا Jupyter lab میں چلائیں  

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

### **🤖 Intel OpenVINO کے ساتھ Phi-3.5 کے لیے نمونے**

| لیبز    | تعارف | جائیں |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | سیکھیں کہ اپنے AI PC میں Phi-3.5 Instruct کو کیسے استعمال کریں    |  [جائیں](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (تصویر) | سیکھیں کہ اپنے AI PC میں Phi-3.5 Vision کے ذریعے تصویر کا تجزیہ کیسے کریں      |  [جائیں](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (ویڈیو)   | سیکھیں کہ اپنے AI PC میں Phi-3.5 Vision کے ذریعے ویڈیو کا تجزیہ کیسے کریں    |  [جائیں](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **وسائل**

1. Intel OpenVINO کے بارے میں مزید جانیں [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub ریپو [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)  

**ڈسکلیمر**:  
یہ دستاویز مشین پر مبنی AI ترجمہ خدمات کا استعمال کرتے ہوئے ترجمہ کی گئی ہے۔ اگرچہ ہم درستگی کے لیے کوشاں ہیں، براہ کرم آگاہ رہیں کہ خودکار ترجمے میں غلطیاں یا عدم درستگیاں ہو سکتی ہیں۔ اصل دستاویز کو اس کی مقامی زبان میں مستند ذریعہ سمجھا جانا چاہیے۔ اہم معلومات کے لیے، پیشہ ور انسانی ترجمہ کی سفارش کی جاتی ہے۔ اس ترجمے کے استعمال سے پیدا ہونے والی کسی بھی غلط فہمی یا غلط تشریح کے لیے ہم ذمہ دار نہیں ہیں۔