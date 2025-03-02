# **Kvantizácia Phi-3.5 pomocou Intel OpenVINO**

Intel je najtradičnejším výrobcom CPU s mnohými používateľmi. S nárastom strojového učenia a hlbokého učenia sa Intel tiež zapojil do súťaže o akceleráciu AI. Na inferenciu modelov Intel využíva nielen GPU a CPU, ale aj NPU.

Dúfame, že nasadíme Phi-3.x rodinu na koncové zariadenia, aby sme sa stali najdôležitejšou súčasťou AI PC a Copilot PC. Načítanie modelu na koncovom zariadení závisí od spolupráce rôznych výrobcov hardvéru. Táto kapitola sa zameriava predovšetkým na aplikačný scenár Intel OpenVINO ako kvantizačného modelu.

## **Čo je OpenVINO**

OpenVINO je open-source nástrojová sada na optimalizáciu a nasadzovanie modelov hlbokého učenia z cloudu na okraj. Umožňuje akcelerovať inferenciu hlbokého učenia v rôznych prípadoch použitia, ako je generatívna AI, video, audio a jazyk, s modelmi z populárnych rámcov ako PyTorch, TensorFlow, ONNX a ďalších. Konvertujte a optimalizujte modely a nasadzujte ich na rôzne Intel® hardvéry a prostredia, či už lokálne, na zariadení, v prehliadači alebo v cloude.

S OpenVINO teraz môžete rýchlo kvantizovať model GenAI na Intel hardvéri a akcelerovať referenciu modelu.

OpenVINO teraz podporuje kvantizačnú konverziu Phi-3.5-Vision a Phi-3.5-Instruct.

### **Nastavenie prostredia**

Uistite sa, že sú nainštalované nasledujúce závislosti prostredia, toto je requirement.txt 

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Kvantizácia Phi-3.5-Instruct pomocou OpenVINO**

V termináli spustite tento skript

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Kvantizácia Phi-3.5-Vision pomocou OpenVINO**

Spustite tento skript v Pythone alebo Jupyter lab

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

### **🤖 Ukážky pre Phi-3.5 s Intel OpenVINO**

| Laboratóriá    | Popis | Prejsť |
| -------- | ------- |  ------- |
| 🚀 Lab-Úvod do Phi-3.5 Instruct  | Naučte sa, ako používať Phi-3.5 Instruct vo vašom AI PC    |  [Prejsť](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Úvod do Phi-3.5 Vision (obraz) | Naučte sa, ako používať Phi-3.5 Vision na analýzu obrázkov vo vašom AI PC      |  [Prejsť](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Úvod do Phi-3.5 Vision (video)   | Naučte sa, ako používať Phi-3.5 Vision na analýzu videa vo vašom AI PC    |  [Prejsť](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Zdroje**

1. Viac informácií o Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. GitHub repozitár Intel OpenVINO [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Upozornenie**:  
Tento dokument bol preložený pomocou služieb strojového prekladu založeného na umelej inteligencii. Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho rodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za žiadne nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.