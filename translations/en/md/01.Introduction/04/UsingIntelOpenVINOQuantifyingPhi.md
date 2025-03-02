# **Quantizing Phi-3.5 using Intel OpenVINO**

Intel is one of the most established CPU manufacturers with a large user base. With the advent of machine learning and deep learning, Intel has also entered the race for AI acceleration. For model inference, Intel not only relies on GPUs and CPUs but also utilizes NPUs.

Our goal is to deploy the Phi-3.x Family on edge devices, aiming to become a key component of AI PCs and Copilot PCs. Deploying models on edge devices depends on collaboration with different hardware manufacturers. This chapter focuses on the use case of Intel OpenVINO as a quantization model.

## **What’s OpenVINO**

OpenVINO is an open-source toolkit designed for optimizing and deploying deep learning models from cloud to edge. It accelerates deep learning inference across various use cases, including generative AI, video, audio, and language, with models from popular frameworks such as PyTorch, TensorFlow, ONNX, and others. It enables model conversion, optimization, and deployment across a mix of Intel® hardware and environments, whether on-premises, on-device, in browsers, or in the cloud.

With OpenVINO, you can now easily quantize GenAI models on Intel hardware and speed up model inference.

Currently, OpenVINO supports the quantization conversion of Phi-3.5-Vision and Phi-3.5-Instruct.

### **Environment Setup**

Ensure that the following dependencies are installed. These are listed in the requirement.txt file:

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **Quantizing Phi-3.5-Instruct using OpenVINO**

In the terminal, execute the following script:

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **Quantizing Phi-3.5-Vision using OpenVINO**

Run the following script in Python or Jupyter Lab:

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

| Labs    | Description | Link |
| -------- | ----------- | ---- |
| 🚀 Lab-Introduce Phi-3.5 Instruct  | Learn how to use Phi-3.5 Instruct on your AI PC    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (image) | Learn how to use Phi-3.5 Vision for image analysis on your AI PC      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Introduce Phi-3.5 Vision (video)   | Learn how to use Phi-3.5 Vision for video analysis on your AI PC    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **Resources**

1. Learn more about Intel OpenVINO: [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub Repository: [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.