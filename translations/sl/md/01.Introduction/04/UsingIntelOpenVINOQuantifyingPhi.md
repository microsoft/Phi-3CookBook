# **Kvadratizacija Phi-3.5 z Intel OpenVINO**

Intel je najbolj tradicionalni proizvajalec procesorjev z mnogimi uporabniki. Z vzponom strojnega in globokega učenja se je tudi Intel vključil v tekmovanje za pospeševanje umetne inteligence. Za izvajanje modelov Intel uporablja ne le GPU-je in CPU-je, temveč tudi NPU-je.

Upamo, da bomo družino Phi-3.x lahko uvedli na končnih napravah in postali ključni del AI PC-jev in Copilot PC-jev. Nalaganje modela na končnih napravah je odvisno od sodelovanja različnih proizvajalcev strojne opreme. To poglavje se osredotoča predvsem na uporabo Intel OpenVINO kot kvantitativnega modela.


## **Kaj je OpenVINO**

OpenVINO je odprtokodno orodje za optimizacijo in uvajanje modelov globokega učenja od oblaka do roba. Pospešuje izvajanje globokega učenja v različnih primerih uporabe, kot so generativna umetna inteligenca, video, zvok in jezik, z modeli iz priljubljenih ogrodij, kot so PyTorch, TensorFlow, ONNX in druga. Pretvorite in optimizirajte modele ter jih uvajajte na različni Intel® strojni opremi in v različnih okoljih – lokalno, na napravah, v brskalniku ali v oblaku.

Z OpenVINO lahko zdaj hitro kvadratizirate modele generativne umetne inteligence na Intelovi strojni opremi in pospešite izvajanje modelov.

OpenVINO zdaj podpira pretvorbo kvantizacije za Phi-3.5-Vision in Phi-3.5 Instruct.

### **Nastavitev okolja**

Prepričajte se, da so nameščene naslednje odvisnosti okolja, to je `requirement.txt`

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Kvadratizacija Phi-3.5-Instruct z OpenVINO**

V terminalu zaženite naslednji skript:

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Kvadratizacija Phi-3.5-Vision z OpenVINO**

Zaženite ta skript v Pythonu ali Jupyter Labu:

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

### **🤖 Primeri za Phi-3.5 z Intel OpenVINO**

| Laboratoriji    | Opis | Pojdi |
| -------- | ------- |  ------- |
| 🚀 Laboratorij - Uvod v Phi-3.5 Instruct  | Naučite se uporabljati Phi-3.5 Instruct na vašem AI PC-ju    |  [Pojdi](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Laboratorij - Uvod v Phi-3.5 Vision (slika) | Naučite se uporabljati Phi-3.5 Vision za analizo slik na vašem AI PC-ju      |  [Pojdi](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Laboratorij - Uvod v Phi-3.5 Vision (video)   | Naučite se uporabljati Phi-3.5 Vision za analizo videa na vašem AI PC-ju    |  [Pojdi](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |



## **Viri**

1. Več o Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub repozitorij [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden s pomočjo strojnih AI prevajalskih storitev. Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalen človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki bi nastale zaradi uporabe tega prevoda.