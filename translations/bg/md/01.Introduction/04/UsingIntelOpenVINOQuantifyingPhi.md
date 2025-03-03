# **Квантизиране на Phi-3.5 с Intel OpenVINO**

Intel е най-традиционният производител на процесори с много потребители. С възхода на машинното обучение и дълбокото обучение, Intel също се включи в надпреварата за AI ускорение. За моделиране и извод, Intel не използва само GPU и CPU, но също така и NPU.

Ние се стремим да внедрим Phi-3.x семейството на крайната страна, с надеждата да се превърнем в най-важната част от AI PC и Copilot PC. Зареждането на модела на крайната страна зависи от сътрудничеството на различни производители на хардуер. Тази глава е основно фокусирана върху приложния сценарий на Intel OpenVINO като количествен модел.


## **Какво е OpenVINO**

OpenVINO е отворен инструментариум за оптимизиране и внедряване на модели за дълбоко обучение от облака до крайните устройства. Той ускорява извода на дълбокото обучение в различни случаи на употреба, като генеративен AI, видео, аудио и език с модели от популярни рамки като PyTorch, TensorFlow, ONNX и други. Конвертирайте и оптимизирайте модели и ги внедрявайте на различен Intel® хардуер и среди, локално или в облака, в браузъра или на устройството.

Сега с OpenVINO можете бързо да квантизирате GenAI моделите на Intel хардуер и да ускорите извода на модела.

В момента OpenVINO поддържа конвертиране на Phi-3.5-Vision и Phi-3.5 Instruct.

### **Настройка на средата**

Моля, уверете се, че следните зависимости на средата са инсталирани. Това е файлът `requirement.txt`:

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Квантизиране на Phi-3.5-Instruct с OpenVINO**

В терминала, моля, изпълнете този скрипт:

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Квантизиране на Phi-3.5-Vision с OpenVINO**

Моля, изпълнете този скрипт в Python или Jupyter Lab:

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

### **🤖 Примери за Phi-3.5 с Intel OpenVINO**

| Лаборатории    | Описание | Достъп |
| -------- | ------- |  ------- |
| 🚀 Лаборатория - Въведение в Phi-3.5 Instruct  | Научете как да използвате Phi-3.5 Instruct във вашия AI PC    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Лаборатория - Въведение в Phi-3.5 Vision (изображение) | Научете как да използвате Phi-3.5 Vision за анализ на изображения във вашия AI PC      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Лаборатория - Въведение в Phi-3.5 Vision (видео)   | Научете как да използвате Phi-3.5 Vision за анализ на видео във вашия AI PC    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |


## **Ресурси**

1. Научете повече за Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. GitHub хранилище на Intel OpenVINO [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Отказ от отговорност**:  
Този документ е преведен с помощта на автоматизирани AI услуги за превод. Въпреки че се стремим към точност, моля, имайте предвид, че автоматичните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия изходен език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Не носим отговорност за каквито и да било недоразумения или погрешни тълкувания, произтичащи от използването на този превод.