# **Quantizing Phi-3.5 using Intel OpenVINO**

Intel is the most traditional CPU manufacturer with many users. With the rise of machine learning and deep learning, Intel has also joined the competition for AI acceleration. For model inference, Intel not only uses GPUs and CPUs, but also uses NPUs.

We hope to deploy Phi-3.x Family on the end side, hoping to become the most important part of AI PC and Copilot PC. The loading of the model on the end side depends on the cooperation of different hardware manufacturers. This chapter mainly focuses on the application scenario of Intel OpenVINO as a quantitative model.


## **What‘s OpenVINO**

OpenVINO is an open-source toolkit for optimizing and deploying deep learning models from cloud to edge. It accelerates deep learning inference across various use cases, such as generative AI, video, audio, and language with models from popular frameworks like PyTorch, TensorFlow, ONNX, and more. Convert and optimize models, and deploy across a mix of Intel® hardware and environments, on-premises and on-device, in the browser or in the cloud.

Now with OpenVINO, you can quickly quantize the GenAI model in Intel hardware and accelerate the model reference.

Now OpenVINO supports quantization conversion of Phi-3.5-Vision and Phi-3.5 Instruct

### **Environment Setup**

Please ensure the following environment dependencies are installed, this is requirement.txt 

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Quantizing Phi-3.5-Instruct using OpenVINO**

In Terminal, please run this script


```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Quantizing Phi-3.5-Vision using OpenVINO**

Please run this script in Python or Jupyter lab

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

### **🤖 Samples for Phi-3.5 with Intel OpenVINO**

| Labs    | Introduce | Go |
| -------- | ------- |  ------- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Learn how to use Phi-3.5 Instruct in your AI PC    |  [Go](../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Learn how to use Phi-3.5 Vision to analyze image in your AI PC      |  [Go](../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | Learn how to use Phi-3.5 Vision to analyze image in your AI PC    |  [Go](../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |



## **Resources**

1. Learn more about Intel OpenVINO [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repo [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)







