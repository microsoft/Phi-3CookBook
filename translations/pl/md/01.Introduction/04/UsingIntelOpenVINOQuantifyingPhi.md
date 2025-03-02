# **Kwantyzacja Phi-3.5 za pomocą Intel OpenVINO**

Intel to najbardziej tradycyjny producent procesorów, z wieloma użytkownikami na całym świecie. Wraz z rozwojem uczenia maszynowego i głębokiego uczenia, Intel również dołączył do rywalizacji o akcelerację AI. Do wnioskowania modeli Intel wykorzystuje nie tylko GPU i CPU, ale także NPU.

Mamy nadzieję wdrożyć rodzinę Phi-3.x po stronie końcowej, dążąc do tego, by stać się najważniejszą częścią AI PC i Copilot PC. Wczytanie modelu po stronie końcowej zależy od współpracy różnych producentów sprzętu. Ten rozdział koncentruje się głównie na zastosowaniu Intel OpenVINO jako narzędzia do kwantyzacji modeli.

## **Czym jest OpenVINO**

OpenVINO to otwartoźródłowy zestaw narzędzi do optymalizacji i wdrażania modeli głębokiego uczenia od chmury po urządzenia brzegowe. Przyspiesza wnioskowanie w różnych przypadkach użycia, takich jak generatywna AI, wideo, audio i język, z wykorzystaniem modeli z popularnych frameworków, takich jak PyTorch, TensorFlow, ONNX i inne. Umożliwia konwersję i optymalizację modeli oraz wdrażanie na różnych urządzeniach Intel® i w różnych środowiskach — lokalnie, na urządzeniach, w przeglądarce lub w chmurze.

Dzięki OpenVINO możesz teraz szybko kwantyzować model GenAI na sprzęcie Intel i przyspieszać jego wnioskowanie.

OpenVINO obecnie wspiera konwersję kwantyzacyjną Phi-3.5-Vision oraz Phi-3.5-Instruct.

### **Konfiguracja środowiska**

Upewnij się, że zainstalowano następujące zależności środowiskowe. Oto plik requirement.txt:

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Kwantyzacja Phi-3.5-Instruct za pomocą OpenVINO**

W terminalu uruchom ten skrypt:

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Kwantyzacja Phi-3.5-Vision za pomocą OpenVINO**

Uruchom ten skrypt w Pythonie lub Jupyter Lab:

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

### **🤖 Przykłady dla Phi-3.5 z Intel OpenVINO**

| Laboratoria    | Opis | Link |
| -------- | ------- |  ------- |
| 🚀 Lab-Wprowadzenie do Phi-3.5 Instruct  | Naucz się, jak używać Phi-3.5 Instruct na swoim AI PC    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Wprowadzenie do Phi-3.5 Vision (obraz) | Naucz się, jak używać Phi-3.5 Vision do analizy obrazów na swoim AI PC      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Wprowadzenie do Phi-3.5 Vision (wideo)   | Naucz się, jak używać Phi-3.5 Vision do analizy wideo na swoim AI PC    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Zasoby**

1. Dowiedz się więcej o Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Repozytorium Intel OpenVINO na GitHubie [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku istotnych informacji zaleca się skorzystanie z profesjonalnego tłumaczenia przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.