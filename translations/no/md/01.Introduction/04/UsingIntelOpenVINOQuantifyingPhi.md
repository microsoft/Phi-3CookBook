# **Kvantisering av Phi-3.5 med Intel OpenVINO**

Intel er den mest tradisjonelle CPU-produsenten med mange brukere. Med fremveksten av maskinlæring og dyp læring har Intel også sluttet seg til konkurransen om AI-akselerasjon. For modellinferens bruker Intel ikke bare GPUer og CPUer, men også NPUer.

Vi håper å kunne distribuere Phi-3.x-familien på sluttbrukerenhetene, og håper at dette blir den viktigste delen av AI-PC og Copilot-PC. Lastingen av modellen på sluttbrukerenhetene avhenger av samarbeidet mellom ulike maskinvareprodusenter. Dette kapittelet fokuserer hovedsakelig på bruksområdet for Intel OpenVINO som en kvantitativ modell.

## **Hva er OpenVINO**

OpenVINO er et åpen kildekode-verktøysett for å optimalisere og distribuere dyp læringsmodeller fra skyen til kantenheter. Det akselererer dyp læringsinfernens på tvers av ulike bruksområder, som generativ AI, video, lyd og språk, med modeller fra populære rammeverk som PyTorch, TensorFlow, ONNX og flere. Konverter og optimaliser modeller, og distribuer dem på en blanding av Intel®-maskinvare og miljøer, enten lokalt, på enheten, i nettleseren eller i skyen.

Med OpenVINO kan du raskt kvantisere GenAI-modellen på Intel-maskinvare og akselerere modellreferansen.

OpenVINO støtter nå kvantiseringskonvertering av Phi-3.5-Vision og Phi-3.5 Instruct.

### **Oppsett av miljø**

Sørg for at følgende miljøavhengigheter er installert, dette er requirement.txt 

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Kvantisering av Phi-3.5-Instruct med OpenVINO**

I terminalen, kjør dette skriptet:

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Kvantisering av Phi-3.5-Vision med OpenVINO**

Kjør dette skriptet i Python eller Jupyter Lab:

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

| Labs    | Introduksjon | Gå til |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduksjon til Phi-3.5 Instruct  | Lær hvordan du bruker Phi-3.5 Instruct på din AI-PC    |  [Gå til](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduksjon til Phi-3.5 Vision (bilde) | Lær hvordan du bruker Phi-3.5 Vision til å analysere bilder på din AI-PC      |  [Gå til](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduksjon til Phi-3.5 Vision (video)   | Lær hvordan du bruker Phi-3.5 Vision til å analysere videoer på din AI-PC    |  [Gå til](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Ressurser**

1. Lær mer om Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub-repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi bestreber oss på nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på dets opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.