# **Quantizzazione di Phi-3.5 con Intel OpenVINO**

Intel è il produttore di CPU più tradizionale con un'ampia base di utenti. Con l'ascesa del machine learning e del deep learning, anche Intel ha deciso di entrare nella competizione per l'accelerazione dell'IA. Per l'inferenza dei modelli, Intel utilizza non solo GPU e CPU, ma anche NPU.

L'obiettivo è distribuire la famiglia Phi-3.x sul lato endpoint, sperando di diventare una parte fondamentale degli AI PC e Copilot PC. Il caricamento del modello sul lato endpoint dipende dalla collaborazione con diversi produttori di hardware. Questo capitolo si concentra principalmente sull'applicazione di Intel OpenVINO come modello quantizzato.

## **Cos'è OpenVINO**

OpenVINO è un toolkit open-source per ottimizzare e distribuire modelli di deep learning dal cloud all'edge. Accelera l'inferenza di deep learning in diversi casi d'uso, come AI generativa, video, audio e linguaggio, utilizzando modelli provenienti da framework popolari come PyTorch, TensorFlow, ONNX e altri. Consente di convertire e ottimizzare i modelli e di distribuirli su una combinazione di hardware Intel® e ambienti diversi, sia on-premise che on-device, nel browser o nel cloud.

Con OpenVINO, è ora possibile quantizzare rapidamente il modello GenAI sull'hardware Intel e accelerare il riferimento del modello.

Attualmente, OpenVINO supporta la conversione quantizzata di Phi-3.5-Vision e Phi-3.5-Instruct.

### **Configurazione dell'Ambiente**

Assicurati che le seguenti dipendenze ambientali siano installate. Questo è il file `requirements.txt`:

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Quantizzazione di Phi-3.5-Instruct con OpenVINO**

Nel terminale, esegui questo script:

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Quantizzazione di Phi-3.5-Vision con OpenVINO**

Esegui questo script in Python o Jupyter Lab:

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

### **🤖 Esempi per Phi-3.5 con Intel OpenVINO**

| Laboratori    | Descrizione | Vai |
| ------------- | ----------- | --- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Scopri come utilizzare Phi-3.5 Instruct nel tuo AI PC    |  [Vai](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (immagine) | Scopri come utilizzare Phi-3.5 Vision per analizzare immagini nel tuo AI PC      |  [Vai](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | Scopri come utilizzare Phi-3.5 Vision per analizzare video nel tuo AI PC    |  [Vai](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Risorse**

1. Scopri di più su Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Repository GitHub di Intel OpenVINO [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Disclaimer (Avvertenza)**:  
Questo documento è stato tradotto utilizzando servizi di traduzione automatizzati basati sull'intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di tenere presente che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.