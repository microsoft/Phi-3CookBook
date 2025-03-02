# **Phi-3.5:n kvantisointi Intel OpenVINO:lla**

Intel on perinteinen prosessorivalmistaja, jolla on laaja käyttäjäkunta. Koneoppimisen ja syväoppimisen yleistyessä myös Intel on lähtenyt mukaan AI-kiihdytyksen kilpailuun. Mallien inferenssissä Intel hyödyntää paitsi GPU:ita ja CPU:ita, myös NPU:ita.

Haluamme ottaa Phi-3.x-perheen käyttöön loppukäyttäjän laitteilla, jotta siitä tulisi keskeinen osa AI PC:tä ja Copilot PC:tä. Mallin lataaminen loppukäyttäjän laitteelle edellyttää yhteistyötä eri laitevalmistajien kanssa. Tässä luvussa keskitytään erityisesti Intel OpenVINO:n käyttöön kvantitatiivisena mallina.

## **Mikä on OpenVINO**

OpenVINO on avoimen lähdekoodin työkalu, joka on suunniteltu syväoppimismallien optimointiin ja käyttöönottoon pilvestä reunalaitteisiin. Se nopeuttaa syväoppimisen inferenssiä eri käyttötapauksissa, kuten generatiivisessa tekoälyssä, video-, ääni- ja kielimallien avulla. Se tukee suosittuja kehityskehyksiä, kuten PyTorch, TensorFlow ja ONNX. OpenVINO mahdollistaa mallien muuntamisen, optimoinnin ja käyttöönoton erilaisilla Intel®-laitteilla ja ympäristöissä, olipa kyseessä paikallinen laite, selain tai pilvi.

OpenVINO:n avulla voit nyt nopeasti kvantisoida generatiivisen tekoälymallin Intel-laitteilla ja nopeuttaa mallin käyttöä.

OpenVINO tukee nyt Phi-3.5-Vision- ja Phi-3.5-Instruct-mallien kvantisointimuunnosta.

### **Ympäristön asennus**

Varmista, että seuraavat ympäristöriippuvuudet on asennettu. Tämä on requirement.txt:

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Phi-3.5-Instructin kvantisointi OpenVINO:lla**

Aja seuraava skripti Terminalissa:

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Phi-3.5-Visionin kvantisointi OpenVINO:lla**

Aja tämä skripti Pythonissa tai Jupyter Labissa:

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

### **🤖 Esimerkit Phi-3.5:lle Intel OpenVINO:lla**

| Laboratoriot    | Kuvaus | Linkki |
| -------- | ------- |  ------- |
| 🚀 Lab-Phi-3.5 Instructin esittely  | Opi käyttämään Phi-3.5 Instruct -mallia AI PC:ssäsi    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Phi-3.5 Vision (kuva) | Opi käyttämään Phi-3.5 Vision -mallia kuvien analysointiin AI PC:ssäsi      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Phi-3.5 Vision (video)   | Opi käyttämään Phi-3.5 Vision -mallia videoiden analysointiin AI PC:ssäsi    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Resurssit**

1. Lisätietoja Intel OpenVINO:sta: [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo: [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisilla tekoälykäännöspalveluilla. Pyrimme tarkkuuteen, mutta huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Tärkeissä tiedoissa suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä aiheutuvista väärinkäsityksistä tai virheellisistä tulkinnoista.