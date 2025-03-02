# **Quantisering af Phi-3.5 med Intel OpenVINO**

Intel er den mest traditionelle CPU-producent med mange brugere. Med fremkomsten af maskinlæring og dyb læring er Intel også trådt ind i konkurrencen om AI-acceleration. Til modelinference bruger Intel ikke kun GPU'er og CPU'er, men også NPU'er.

Vi håber at kunne implementere Phi-3.x-familien på slutbrugerenheder og gøre den til en central del af AI-PC'er og Copilot-PC'er. Indlæsningen af modellen på slutbrugerenheder afhænger af samarbejdet med forskellige hardwareproducenter. Dette kapitel fokuserer primært på anvendelsesscenariet for Intel OpenVINO som en kvantitativ model.

## **Hvad er OpenVINO**

OpenVINO er et open-source værktøjssæt til optimering og implementering af dyb læringsmodeller fra skyen til kanten. Det accelererer dyb læringsinference på tværs af forskellige anvendelsestilfælde, såsom generativ AI, video, lyd og sprog, med modeller fra populære rammer som PyTorch, TensorFlow, ONNX og flere. Konverter og optimer modeller, og implementer dem på en blanding af Intel® hardware og miljøer, både lokalt og på enheder, i browseren eller i skyen.

Med OpenVINO kan du nu hurtigt kvantisere GenAI-modellen på Intel-hardware og accelerere modelinference.

OpenVINO understøtter nu kvantiseringskonvertering af Phi-3.5-Vision og Phi-3.5-Instruct.

### **Opsætning af miljø**

Sørg for, at følgende miljøafhængigheder er installeret, dette er requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Kvantisering af Phi-3.5-Instruct med OpenVINO**

I Terminal, kør venligst dette script

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Kvantisering af Phi-3.5-Vision med OpenVINO**

Kør venligst dette script i Python eller Jupyter Lab

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

### **🤖 Eksempler for Phi-3.5 med Intel OpenVINO**

| Labs    | Introduktion | Gå til |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduktion til Phi-3.5 Instruct  | Lær hvordan du bruger Phi-3.5 Instruct på din AI-PC    |  [Gå til](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduktion til Phi-3.5 Vision (billede) | Lær hvordan du bruger Phi-3.5 Vision til at analysere billeder på din AI-PC      |  [Gå til](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduktion til Phi-3.5 Vision (video)   | Lær hvordan du bruger Phi-3.5 Vision til at analysere videoer på din AI-PC    |  [Gå til](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Ressourcer**

1. Lær mere om Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå ved brugen af denne oversættelse.