# **Kvantizace Phi-3.5 pomocí Intel OpenVINO**

Intel je nejtradičnější výrobce procesorů s mnoha uživateli. S rozvojem strojového učení a hlubokého učení se Intel také zapojil do soutěže o akceleraci AI. Pro inferenci modelů Intel nevyužívá pouze GPU a CPU, ale také NPU.

Chceme nasadit rodinu Phi-3.x na koncová zařízení s cílem stát se klíčovou součástí AI PC a Copilot PC. Načítání modelu na koncových zařízeních závisí na spolupráci různých výrobců hardwaru. Tato kapitola se zaměřuje především na scénář použití Intel OpenVINO jako kvantizačního modelu.

## **Co je OpenVINO**

OpenVINO je open-source nástrojová sada pro optimalizaci a nasazení modelů hlubokého učení od cloudu po edge zařízení. Zrychluje inferenci hlubokého učení v různých případech použití, jako je generativní AI, video, audio a jazyk, a to s modely z populárních frameworků, jako jsou PyTorch, TensorFlow, ONNX a další. Umožňuje převod a optimalizaci modelů a jejich nasazení na různých zařízeních Intel® a prostředích, ať už lokálně, na zařízení, v prohlížeči nebo v cloudu.

S OpenVINO nyní můžete rychle kvantizovat GenAI modely na hardwaru Intel a zrychlit referenci modelů.

OpenVINO nyní podporuje kvantizační konverzi modelů Phi-3.5-Vision a Phi-3.5-Instruct.

### **Nastavení prostředí**

Ujistěte se, že máte nainstalované následující závislosti prostředí, toto je requirement.txt:

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Kvantizace Phi-3.5-Instruct pomocí OpenVINO**

V terminálu spusťte tento skript:

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Kvantizace Phi-3.5-Vision pomocí OpenVINO**

Tento skript spusťte v Pythonu nebo Jupyter labu:

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

### **🤖 Ukázky pro Phi-3.5 s Intel OpenVINO**

| Laboratoře | Popis | Odkaz |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Naučte se, jak používat Phi-3.5 Instruct ve vašem AI PC    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (obraz) | Naučte se, jak používat Phi-3.5 Vision pro analýzu obrazu ve vašem AI PC      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | Naučte se, jak používat Phi-3.5 Vision pro analýzu videa ve vašem AI PC    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Zdroje**

1. Další informace o Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. GitHub repozitář Intel OpenVINO [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových překladatelských služeb založených na umělé inteligenci. Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro kritické informace se doporučuje profesionální překlad provedený člověkem. Neodpovídáme za žádná nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.