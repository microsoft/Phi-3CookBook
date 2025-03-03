# **Pagkuquantize ng Phi-3.5 gamit ang Intel OpenVINO**

Ang Intel ay ang pinaka-tradisyonal na tagagawa ng CPU na may maraming gumagamit. Sa pag-usbong ng machine learning at deep learning, sumali rin ang Intel sa kumpetisyon para sa AI acceleration. Para sa model inference, gumagamit ang Intel hindi lamang ng GPUs at CPUs, kundi pati na rin ng NPUs.

Inaasahan naming ma-deploy ang Phi-3.x Family sa end side, na layuning maging pinakamahalagang bahagi ng AI PC at Copilot PC. Ang pag-load ng modelo sa end side ay nakadepende sa kooperasyon ng iba't ibang hardware manufacturers. Ang kabanatang ito ay nakatuon sa application scenario ng Intel OpenVINO bilang isang quantitative model.

## **Ano ang OpenVINO**

Ang OpenVINO ay isang open-source toolkit para sa pag-optimize at pag-deploy ng deep learning models mula cloud papunta sa edge. Pinapabilis nito ang deep learning inference para sa iba't ibang use cases, tulad ng generative AI, video, audio, at wika gamit ang mga modelo mula sa mga sikat na frameworks tulad ng PyTorch, TensorFlow, ONNX, at iba pa. Maaari kang mag-convert at mag-optimize ng mga modelo, at i-deploy ang mga ito sa iba't ibang Intel® hardware at environments, on-premises at on-device, sa browser o sa cloud.

Ngayon, gamit ang OpenVINO, maaari mong mabilis na i-quantize ang GenAI model sa Intel hardware at pabilisin ang model reference.

Sa kasalukuyan, sinusuportahan na ng OpenVINO ang quantization conversion ng Phi-3.5-Vision at Phi-3.5 Instruct.

### **Pag-set up ng Environment**

Siguraduhing naka-install ang sumusunod na mga kinakailangan sa environment, ito ang requirement.txt 

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Pagkuquantize ng Phi-3.5-Instruct gamit ang OpenVINO**

Sa Terminal, pakisubukang patakbuhin ang script na ito

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Pagkuquantize ng Phi-3.5-Vision gamit ang OpenVINO**

Pakisubukang patakbuhin ang script na ito sa Python o Jupyter lab

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

### **🤖 Mga Halimbawa para sa Phi-3.5 gamit ang Intel OpenVINO**

| Labs    | Paliwanag | Pumunta |
| -------- | ------- |  ------- |
| 🚀 Lab-Pakilala sa Phi-3.5 Instruct  | Alamin kung paano gamitin ang Phi-3.5 Instruct sa iyong AI PC    |  [Pumunta](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Pakilala sa Phi-3.5 Vision (larawan) | Alamin kung paano gamitin ang Phi-3.5 Vision upang suriin ang larawan sa iyong AI PC      |  [Pumunta](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Pakilala sa Phi-3.5 Vision (video)   | Alamin kung paano gamitin ang Phi-3.5 Vision upang suriin ang video sa iyong AI PC    |  [Pumunta](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Mga Mapagkukunan**

1. Matuto pa tungkol sa Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyong awtomatikong pagsasalin ng AI. Bagamat sinisikap naming maging tumpak, pakitandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.