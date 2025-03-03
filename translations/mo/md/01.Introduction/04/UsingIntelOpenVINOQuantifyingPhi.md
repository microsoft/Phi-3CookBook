# **Phi-3.5 ကို Intel OpenVINO အသုံးပြု၍ Quantizing လုပ်ခြင်း**

Intel သည် အသုံးပြုသူအများဆုံး CPU ထုတ်လုပ်သူဖြစ်ပြီး ယခင်ကတည်းက နာမည်ကြီးခဲ့သည်။ Machine Learning နှင့် Deep Learning တိုးတက်လာသည်နှင့်အမျှ AI acceleration အတွက် ယှဉ်ပြိုင်မှုတွင်လည်း Intel ပါဝင်လာခဲ့သည်။ Model inference အတွက် Intel သည် GPU နှင့် CPU များသာမက NPU များကိုလည်း အသုံးပြုသည်။

ကျွန်ုပ်တို့သည် Phi-3.x Family ကို end-side တွင် တင်သွင်းလိုပြီး AI PC နှင့် Copilot PC ၏ အရေးပါဆုံးအစိတ်အပိုင်းဖြစ်လာစေရန် မျှော်လင့်ပါသည်။ Model ကို end-side တွင် တင်သွင်းခြင်းသည် ကွဲပြားသော hardware ထုတ်လုပ်သူများ၏ ပူးပေါင်းဆောင်ရွက်မှုအပေါ် မူတည်ပါသည်။ ဤအခန်းတွင် Intel OpenVINO ကို Quantitative Model အဖြစ် အသုံးပြုသည့် လျှောက်လွှာအခြေအနေကို အဓိကထား ရှင်းပြပါမည်။  

## **OpenVINO ဆိုတာဘာလဲ**

OpenVINO သည် cloud မှ edge အထိ deep learning models များကို optimize လုပ်ပြီး တင်သွင်းရန်အတွက် open-source toolkit တစ်ခုဖြစ်သည်။ ယင်းသည် PyTorch, TensorFlow, ONNX စသည့် framework များမှ models များကို အသုံးပြု၍ generative AI, video, audio, language စသည့် လုပ်ငန်းစဉ်အမျိုးမျိုးတွင် deep learning inference ကို မြန်ဆန်စေပါသည်။ Models များကို ပြောင်းလဲ optimize လုပ်ပြီး Intel® hardware မျိုးစုံနှင့် အခြေအနေများ (on-premises, on-device, browser, cloud) တွင် တင်သွင်းနိုင်ပါသည်။

OpenVINO ဖြင့် ယခုအခါ Intel hardware တွင် GenAI model ကို မြန်ဆန်စွာ quantize လုပ်ပြီး model reference ကို မြှင့်တင်နိုင်ပါသည်။

ယခုအခါ OpenVINO သည် Phi-3.5-Vision နှင့် Phi-3.5 Instruct ၏ quantization conversion ကို ပံ့ပိုးထားပါသည်။

### **ပတ်ဝန်းကျင်ကို ပြင်ဆင်ခြင်း**

အောက်ပါ environment dependencies များကို ထည့်သွင်းထားပါရန် ကျေးဇူးပြု၍ သေချာပါစေ၊ ၎င်းသည် requirement.txt ဖြစ်ပါသည်။

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **OpenVINO ဖြင့် Phi-3.5-Instruct ကို Quantizing လုပ်ခြင်း**

Terminal တွင် အောက်ပါ script ကို run ပါ။

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **OpenVINO ဖြင့် Phi-3.5-Vision ကို Quantizing လုပ်ခြင်း**

Python သို့မဟုတ် Jupyter lab တွင် အောက်ပါ script ကို run ပါ။

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

### **🤖 Intel OpenVINO နှင့်အတူ Phi-3.5 ၏ နမူနာများ**

| Labs    | မိတ်ဆက် | သွားရန် |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | AI PC တွင် Phi-3.5 Instruct ကို အသုံးပြုနည်းကို လေ့လာပါ    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | AI PC တွင် Phi-3.5 Vision ကို အသုံးပြု၍ ပုံများကို ခွဲခြမ်းစိတ်ဖြာနည်းကို လေ့လာပါ      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | AI PC တွင် Phi-3.5 Vision ကို အသုံးပြု၍ ဗီဒီယိုများကို ခွဲခြမ်းစိတ်ဖြာနည်းကို လေ့လာပါ    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **အရင်းအမြစ်များ**

1. Intel OpenVINO အကြောင်းပိုမိုလေ့လာရန် [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

It seems you are asking for a translation to "mo." Could you clarify what "mo" refers to? Are you referring to a specific language or dialect? For example, is it Maori, Mongolian, or something else? Please provide more details so I can assist you accurately!