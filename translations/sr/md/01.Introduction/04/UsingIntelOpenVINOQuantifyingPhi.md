# **Kvantizacija Phi-3.5 koristeći Intel OpenVINO**

Intel je najtradicionalniji proizvođač CPU-a sa mnogim korisnicima. Sa porastom mašinskog učenja i dubokog učenja, Intel se takođe pridružio trci za AI akceleracijom. Za inferenciju modela, Intel koristi ne samo GPU-ove i CPU-ove, već i NPU-ove.

Nadamo se da ćemo implementirati Phi-3.x porodicu na krajnjoj strani, sa ciljem da postane najvažniji deo AI PC-a i Copilot PC-a. Učitavanje modela na krajnjoj strani zavisi od saradnje različitih proizvođača hardvera. Ovo poglavlje se uglavnom fokusira na primenu Intel OpenVINO-a kao kvantizovanog modela.

## **Šta je OpenVINO**

OpenVINO je open-source alat za optimizaciju i implementaciju modela dubokog učenja od oblaka do ivice (edge). Ubrzava inferenciju dubokog učenja kroz različite slučajeve upotrebe, kao što su generativna AI, video, audio i jezik, koristeći modele iz popularnih okvira kao što su PyTorch, TensorFlow, ONNX i drugi. Omogućava konverziju i optimizaciju modela, te njihovu implementaciju na raznovrsnom Intel® hardveru i okruženjima, bilo lokalno, na uređaju, u pregledaču ili u oblaku.

Sada, uz OpenVINO, možete brzo kvantizovati GenAI model na Intel hardveru i ubrzati referencu modela.

OpenVINO sada podržava konverziju kvantizacije za Phi-3.5-Vision i Phi-3.5 Instruct.

### **Postavljanje okruženja**

Molimo vas da osigurate da su instalirane sledeće zavisnosti okruženja, ovo je requirement.txt:

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Kvantizacija Phi-3.5-Instruct koristeći OpenVINO**

U Terminalu, pokrenite ovaj skript:

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Kvantizacija Phi-3.5-Vision koristeći OpenVINO**

Pokrenite ovaj skript u Python-u ili Jupyter Lab-u:

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

### **🤖 Primeri za Phi-3.5 sa Intel OpenVINO**

| Laboratorije    | Opis | Idi |
| -------- | ------- |  ------- |
| 🚀 Lab-Uvod u Phi-3.5 Instruct  | Naučite kako da koristite Phi-3.5 Instruct na svom AI PC-u    |  [Idi](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Uvod u Phi-3.5 Vision (slike) | Naučite kako da koristite Phi-3.5 Vision za analizu slika na svom AI PC-u      |  [Idi](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Uvod u Phi-3.5 Vision (video)   | Naučite kako da koristite Phi-3.5 Vision za analizu videa na svom AI PC-u    |  [Idi](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Resursi**

1. Saznajte više o Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub repozitorijum [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења заснованих на вештачкој интелигенцији. Иако се трудимо да обезбедимо тачност, имајте у виду да аутоматизовани преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква погрешна тумачења или неспоразуме који могу настати употребом овог превода.