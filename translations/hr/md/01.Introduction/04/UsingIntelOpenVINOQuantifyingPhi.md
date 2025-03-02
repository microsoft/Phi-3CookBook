# **Kvantizacija Phi-3.5 koristeći Intel OpenVINO**

Intel je najtradicionalniji proizvođač CPU-a s mnogo korisnika. S porastom strojnog učenja i dubokog učenja, Intel se također pridružio utrci za AI akceleracijom. Za izvođenje modela, Intel koristi ne samo GPU-ove i CPU-ove, već i NPU-ove.

Nadamo se implementirati Phi-3.x obitelj na krajnjoj strani, s ciljem da postane najvažniji dio AI PC-a i Copilot PC-a. Učitavanje modela na krajnjoj strani ovisi o suradnji različitih proizvođača hardvera. Ovo poglavlje se uglavnom fokusira na primjenu Intel OpenVINO-a kao kvantizacijskog modela.


## **Što je OpenVINO**

OpenVINO je alat otvorenog koda za optimizaciju i implementaciju modela dubokog učenja od oblaka do ruba. Ubrzava izvođenje dubokog učenja u raznim slučajevima uporabe, poput generativnog AI-a, videa, zvuka i jezika, koristeći modele iz popularnih okvira poput PyTorch-a, TensorFlow-a, ONNX-a i drugih. Omogućuje pretvorbu i optimizaciju modela te implementaciju na različitim Intel® hardverskim platformama i okruženjima, bilo lokalno, na uređaju, u pregledniku ili u oblaku.

Sada, uz OpenVINO, možete brzo kvantizirati GenAI model na Intel hardveru i ubrzati izvođenje modela.

Trenutno OpenVINO podržava kvantizacijsku pretvorbu Phi-3.5-Vision i Phi-3.5-Instruct.

### **Postavljanje okruženja**

Molimo osigurajte da su instalirane sljedeće ovisnosti okruženja, ovo je requirement.txt 

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Kvantizacija Phi-3.5-Instruct koristeći OpenVINO**

U Terminalu, pokrenite ovaj skript


```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Kvantizacija Phi-3.5-Vision koristeći OpenVINO**

Pokrenite ovaj skript u Pythonu ili Jupyter labu

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

### **🤖 Primjeri za Phi-3.5 s Intel OpenVINO**

| Laboratoriji    | Uvod | Idi |
| -------- | ------- |  ------- |
| 🚀 Lab-Uvod u Phi-3.5 Instruct  | Naučite kako koristiti Phi-3.5 Instruct na svom AI PC-u    |  [Idi](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Uvod u Phi-3.5 Vision (slika) | Naučite kako koristiti Phi-3.5 Vision za analizu slika na svom AI PC-u      |  [Idi](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Uvod u Phi-3.5 Vision (video)   | Naučite kako koristiti Phi-3.5 Vision za analizu videa na svom AI PC-u    |  [Idi](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |



## **Resursi**

1. Saznajte više o Intel OpenVINO-u [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub repozitorij [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden pomoću usluga strojno baziranog AI prevođenja. Iako nastojimo postići točnost, imajte na umu da automatizirani prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na njegovom izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane čovjeka. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja nastala korištenjem ovog prijevoda.