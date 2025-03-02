# **使用 Intel OpenVINO 量化 Phi-3.5**

Intel 作為最傳統的 CPU 製造商，擁有大量用戶。隨著機器學習和深度學習的興起，Intel 也加入了 AI 加速的競爭行列。在模型推理方面，Intel 不僅使用 GPU 和 CPU，還使用 NPU。

我們希望能夠將 Phi-3.x 家族部署到終端側，希望成為 AI PC 和 Copilot PC 的重要組成部分。在終端側載入模型需要不同硬件製造商的合作。本章主要聚焦於使用 Intel OpenVINO 作為量化模型的應用場景。

## **什麼是 OpenVINO**

OpenVINO 是一個開源工具包，用於從雲端到邊緣優化和部署深度學習模型。它能加速多種使用場景中的深度學習推理，例如生成式 AI、視頻、音頻和語言，並支持來自主流框架（如 PyTorch、TensorFlow、ONNX 等）的模型。您可以轉換和優化模型，並部署在混合的 Intel® 硬件和環境中，包括本地設備、瀏覽器或雲端。

現在通過 OpenVINO，您可以快速在 Intel 硬件上量化 GenAI 模型並加速模型推理。

目前，OpenVINO 支持 Phi-3.5-Vision 和 Phi-3.5 Instruct 的量化轉換。

### **環境設置**

請確保已安裝以下環境依賴項，這是 requirement.txt

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **使用 OpenVINO 量化 Phi-3.5-Instruct**

在終端中運行以下腳本

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **使用 OpenVINO 量化 Phi-3.5-Vision**

請在 Python 或 Jupyter Lab 中運行以下腳本

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

### **🤖 Phi-3.5 與 Intel OpenVINO 的示例**

| 實驗室    | 介紹 | 前往 |
| -------- | ------- |  ------- |
| 🚀 Lab-介紹 Phi-3.5 Instruct  | 學習如何在您的 AI PC 中使用 Phi-3.5 Instruct    |  [前往](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-介紹 Phi-3.5 Vision (圖片) | 學習如何在您的 AI PC 中使用 Phi-3.5 Vision 分析圖片      |  [前往](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-介紹 Phi-3.5 Vision (視頻)   | 學習如何在您的 AI PC 中使用 Phi-3.5 Vision 分析視頻    |  [前往](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **資源**

1. 了解更多關於 Intel OpenVINO 的信息 [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHub 資源庫 [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**免責聲明**：  
本文件已使用基於機器的人工智能翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原語言撰寫的原始文件作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤釋不承擔責任。