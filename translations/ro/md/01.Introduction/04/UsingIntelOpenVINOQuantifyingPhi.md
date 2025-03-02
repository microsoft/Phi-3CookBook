# **Cuantizarea Phi-3.5 folosind Intel OpenVINO**

Intel este cel mai tradițional producător de procesoare, având mulți utilizatori. Odată cu creșterea popularității învățării automate și a învățării profunde, Intel a intrat și el în competiția pentru accelerarea AI. Pentru inferența modelelor, Intel nu folosește doar GPU-uri și CPU-uri, ci și NPU-uri.

Ne dorim să implementăm Familia Phi-3.x pe partea de dispozitive finale, cu speranța de a deveni o parte esențială a PC-urilor AI și Copilot PC-urilor. Încărcarea modelului pe partea de dispozitive finale depinde de colaborarea dintre diferiți producători de hardware. Acest capitol se concentrează în principal pe scenariul de aplicare al Intel OpenVINO ca model cantitativ.

## **Ce este OpenVINO**

OpenVINO este un toolkit open-source pentru optimizarea și implementarea modelelor de învățare profundă de la cloud la edge. Accelerează inferența învățării profunde pentru diverse cazuri de utilizare, cum ar fi AI generativ, video, audio și limbaj, cu modele din framework-uri populare precum PyTorch, TensorFlow, ONNX și altele. Permite conversia și optimizarea modelelor și implementarea acestora pe o combinație de hardware și medii Intel®, fie local, fie pe dispozitive, în browser sau în cloud.

Acum, cu OpenVINO, poți cuantiza rapid modelul GenAI pe hardware Intel și accelera referința modelului.

În prezent, OpenVINO suportă conversia cuantizată pentru Phi-3.5-Vision și Phi-3.5 Instruct.

### **Configurarea mediului**

Asigură-te că următoarele dependențe de mediu sunt instalate, acesta este requirement.txt:

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Cuantizarea Phi-3.5-Instruct folosind OpenVINO**

În Terminal, rulează acest script:

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Cuantizarea Phi-3.5-Vision folosind OpenVINO**

Rulează acest script în Python sau Jupyter Lab:

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

### **🤖 Exemple pentru Phi-3.5 cu Intel OpenVINO**

| Laboratoare    | Descriere | Acces |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Învață cum să folosești Phi-3.5 Instruct pe PC-ul tău AI    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (imagine) | Învață cum să folosești Phi-3.5 Vision pentru a analiza imagini pe PC-ul tău AI      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | Învață cum să folosești Phi-3.5 Vision pentru a analiza imagini pe PC-ul tău AI    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Resurse**

1. Află mai multe despre Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Repo-ul GitHub pentru Intel OpenVINO [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Declinare de responsabilitate**:  
Acest document a fost tradus utilizând servicii de traducere automate bazate pe inteligență artificială. Deși depunem eforturi pentru acuratețe, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original în limba sa natală trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.