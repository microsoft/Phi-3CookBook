# **Phi-3.5 kvantálása Intel OpenVINO-val**

Az Intel az egyik legtradicionálisabb CPU-gyártó, amelynek rengeteg felhasználója van. A gépi tanulás és mélytanulás térnyerésével az Intel is csatlakozott az AI-gyorsításért folytatott versenyhez. Modellinferencia során az Intel nemcsak GPU-kat és CPU-kat, hanem NPU-kat is használ.

Célunk, hogy a Phi-3.x családot az eszközoldalon telepítsük, és ezzel az AI PC-k és Copilot PC-k legfontosabb részévé váljunk. Az eszközoldalon történő modellbetöltés a különböző hardvergyártók együttműködésén múlik. Ez a fejezet főként az Intel OpenVINO mint kvantitatív modell alkalmazási forgatókönyvére összpontosít.

## **Mi az az OpenVINO?**

Az OpenVINO egy nyílt forráskódú eszközkészlet, amely a mélytanulási modellek optimalizálására és telepítésére szolgál, a felhőtől az edge-ig. Felgyorsítja a mélytanulási inferenciát különféle felhasználási esetekben, például generatív AI, videó, hang és nyelv terén, olyan népszerű keretrendszerek modelljeivel, mint a PyTorch, TensorFlow, ONNX és mások. Konvertálja és optimalizálja a modelleket, majd telepítse őket különböző Intel® hardverekre és környezetekbe, helyben vagy eszközoldalon, böngészőben vagy felhőben.

Az OpenVINO segítségével most gyorsan kvantálhatja a generatív AI-modellt Intel hardveren, és felgyorsíthatja a modellreferenciát.

Az OpenVINO most támogatja a Phi-3.5-Vision és a Phi-3.5 Instruct kvantálási konverzióját.

### **Környezet beállítása**

Győződjön meg róla, hogy a következő környezeti függőségek telepítve vannak. Ez a requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Phi-3.5-Instruct kvantálása OpenVINO-val**

Terminálban futtassa a következő szkriptet:

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Phi-3.5-Vision kvantálása OpenVINO-val**

Futtassa a következő szkriptet Pythonban vagy Jupyter labban:

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

### **🤖 Minták Phi-3.5-höz Intel OpenVINO-val**

| Laborok    | Bemutatás | Indítás |
| -------- | ------- |  ------- |
| 🚀 Lab-Phi-3.5 Instruct bemutatása  | Tanulja meg, hogyan használja a Phi-3.5 Instruct-ot az AI PC-jén |  [Indítás](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Phi-3.5 Vision (kép) bemutatása | Tanulja meg, hogyan használja a Phi-3.5 Vision-t képelemzésre az AI PC-jén |  [Indítás](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Phi-3.5 Vision (videó) bemutatása   | Tanulja meg, hogyan használja a Phi-3.5 Vision-t videóelemzésre az AI PC-jén |  [Indítás](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Források**

1. Tudjon meg többet az Intel OpenVINO-ról: [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo: [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítási szolgáltatások segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő a hiteles forrásnak. Kritikus információk esetén javasolt a professzionális, emberi fordítás igénybevétele. Nem vállalunk felelősséget a fordítás használatából eredő félreértésekért vagy téves értelmezésekért.