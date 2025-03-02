# **Intel OpenVINO ile Phi-3.5'i Kuantize Etme**

Intel, en köklü CPU üreticilerinden biri olup geniş bir kullanıcı kitlesine sahiptir. Makine öğrenimi ve derin öğrenimin yükselişiyle birlikte Intel de yapay zeka hızlandırma yarışına katıldı. Model çıkarımı için Intel yalnızca GPU ve CPU'ları değil, aynı zamanda NPU'ları da kullanıyor.

Phi-3.x Ailesi'ni uç noktada konuşlandırmayı umuyoruz ve bunun AI PC ve Copilot PC'nin en önemli parçası olmasını hedefliyoruz. Uç noktada modelin yüklenmesi, farklı donanım üreticilerinin iş birliğine bağlıdır. Bu bölüm, esas olarak Intel OpenVINO'nun bir kuantize model olarak uygulama senaryosuna odaklanmaktadır.

## **OpenVINO Nedir?**

OpenVINO, buluttan uç cihaza kadar derin öğrenme modellerini optimize etmek ve dağıtmak için açık kaynaklı bir araç setidir. PyTorch, TensorFlow, ONNX ve daha fazlası gibi popüler çerçevelerden gelen modellerle üretici yapay zeka, video, ses ve dil gibi çeşitli kullanım durumlarında derin öğrenme çıkarımını hızlandırır. Modelleri dönüştürün, optimize edin ve Intel® donanımı ve ortamlarının bir karışımında, yerinde ya da cihaz üzerinde, tarayıcıda ya da bulutta konuşlandırın.

Artık OpenVINO ile Intel donanımında GenAI modelini hızla kuantize edebilir ve model referansını hızlandırabilirsiniz.

Şu anda OpenVINO, Phi-3.5-Vision ve Phi-3.5 Instruct modellerinin kuantizasyon dönüşümünü desteklemektedir.

### **Ortam Kurulumu**

Lütfen aşağıdaki ortam bağımlılıklarının yüklü olduğundan emin olun, bu requirement.txt dosyasıdır:

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **OpenVINO ile Phi-3.5-Instruct Kuantizasyonu**

Terminalde, lütfen bu betiği çalıştırın:

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **OpenVINO ile Phi-3.5-Vision Kuantizasyonu**

Lütfen bu betiği Python veya Jupyter Lab'de çalıştırın:

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

### **🤖 Intel OpenVINO ile Phi-3.5 Örnekleri**

| Laboratuvarlar    | Tanıtım | Git |
| -------- | ------- |  ------- |
| 🚀 Lab-Phi-3.5 Instruct Tanıtımı  | Phi-3.5 Instruct'ı AI PC'nizde nasıl kullanacağınızı öğrenin    |  [Git](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Phi-3.5 Vision Tanıtımı (görüntü) | Phi-3.5 Vision'ı AI PC'nizde görüntü analizi yapmak için nasıl kullanacağınızı öğrenin      |  [Git](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Phi-3.5 Vision Tanıtımı (video)   | Phi-3.5 Vision'ı AI PC'nizde video analizi yapmak için nasıl kullanacağınızı öğrenin    |  [Git](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Kaynaklar**

1. Intel OpenVINO hakkında daha fazla bilgi edinin: [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Deposu: [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Feragatname**:  
Bu belge, makine tabanlı yapay zeka çeviri hizmetleri kullanılarak çevrilmiştir. Doğruluk için çaba göstersek de, otomatik çevirilerin hata veya yanlışlıklar içerebileceğini lütfen unutmayın. Belgenin orijinal diliyle hazırlanmış hali, yetkili kaynak olarak kabul edilmelidir. Kritik bilgiler için profesyonel insan çevirisi önerilir. Bu çevirinin kullanımından kaynaklanan yanlış anlama veya yanlış yorumlamalardan sorumlu değiliz.