# **Phi-3.5 Kwantiseren met Intel OpenVINO**

Intel is de meest traditionele CPU-fabrikant met veel gebruikers. Met de opkomst van machine learning en deep learning is Intel ook de concurrentie aangegaan op het gebied van AI-versnelling. Voor modelinference gebruikt Intel niet alleen GPU's en CPU's, maar ook NPU's.

We hopen de Phi-3.x Family aan de randzijde te implementeren, met de ambitie om het belangrijkste onderdeel te worden van AI-PC's en Copilot-PC's. Het laden van het model aan de randzijde hangt af van de samenwerking met verschillende hardwarefabrikanten. Dit hoofdstuk richt zich voornamelijk op het toepassingsscenario van Intel OpenVINO als een kwantitatief model.

## **Wat is OpenVINO**

OpenVINO is een open-source toolkit voor het optimaliseren en implementeren van deep learning-modellen van de cloud naar de edge. Het versnelt deep learning-inferentie voor verschillende gebruiksscenario's, zoals generatieve AI, video, audio en taal, met modellen uit populaire frameworks zoals PyTorch, TensorFlow, ONNX en meer. Converteer en optimaliseer modellen en implementeer ze op een mix van Intel®-hardware en omgevingen, zowel lokaal als op apparaten, in de browser of in de cloud.

Met OpenVINO kun je nu snel het GenAI-model kwantiseren op Intel-hardware en de modelreferentie versnellen.

OpenVINO ondersteunt nu kwantisatieconversie van Phi-3.5-Vision en Phi-3.5 Instruct.

### **Omgevingsinstellingen**

Zorg ervoor dat de volgende omgevingsafhankelijkheden zijn geïnstalleerd. Dit is de requirement.txt.

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Phi-3.5-Instruct kwantiseren met OpenVINO**

Voer dit script uit in de terminal:

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Phi-3.5-Vision kwantiseren met OpenVINO**

Voer dit script uit in Python of Jupyter Lab:

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

### **🤖 Voorbeelden voor Phi-3.5 met Intel OpenVINO**

| Labs    | Introductie | Ga |
| -------- | ------- |  ------- |
| 🚀 Lab-Introductie Phi-3.5 Instruct  | Leer hoe je Phi-3.5 Instruct gebruikt op je AI-PC    |  [Ga](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introductie Phi-3.5 Vision (afbeelding) | Leer hoe je Phi-3.5 Vision gebruikt om afbeeldingen te analyseren op je AI-PC      |  [Ga](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introductie Phi-3.5 Vision (video)   | Leer hoe je Phi-3.5 Vision gebruikt om video's te analyseren op je AI-PC    |  [Ga](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Bronnen**

1. Meer informatie over Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Disclaimer**:  
Dit document is vertaald met behulp van machine-gebaseerde AI-vertalingsdiensten. Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.