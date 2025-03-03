# **Phi-3.5をIntel OpenVINOで量子化する**

Intelは、多くのユーザーを持つ伝統的なCPUメーカーです。機械学習やディープラーニングの台頭に伴い、IntelもAI加速の競争に参入しました。モデル推論において、IntelはGPUやCPUだけでなく、NPUも活用しています。

私たちはPhi-3.xファミリーをエンドサイドで展開し、AI PCやCopilot PCの最重要な部分となることを目指しています。エンドサイドでのモデルのロードは、異なるハードウェアメーカーとの協力に依存しています。この章では、Intel OpenVINOを使用した量子化モデルの適用シナリオに焦点を当てます。

## **OpenVINOとは**

OpenVINOは、クラウドからエッジまでのディープラーニングモデルを最適化してデプロイするためのオープンソースツールキットです。PyTorch、TensorFlow、ONNXなどの人気フレームワークからのモデルを使用して、生成AI、ビデオ、オーディオ、言語などのさまざまなユースケースでディープラーニング推論を加速します。モデルを変換・最適化し、Intel®ハードウェアと環境の混在にわたって、オンプレミスやデバイス上、ブラウザやクラウドでデプロイできます。

OpenVINOを使用すれば、Intelハードウェア上でGenAIモデルを迅速に量子化し、モデルの推論を加速することが可能です。

現在、OpenVINOはPhi-3.5-VisionおよびPhi-3.5-Instructの量子化変換をサポートしています。

### **環境設定**

以下の環境依存関係がインストールされていることを確認してください。これはrequirement.txtです。

```txt

--extra-index-url https://download.pytorch.org/whl/cpu
optimum-intel>=1.18.2
nncf>=2.11.0
openvino>=2024.3.0
transformers>=4.40
openvino-genai>=2024.3.0.0

```

### **OpenVINOを使用したPhi-3.5-Instructの量子化**

ターミナルで、以下のスクリプトを実行してください。

```bash


export llm_model_id = "microsoft/Phi-3.5-mini-instruct"

export llm_model_path = "your save quantizing Phi-3.5-instruct location"

optimum-cli export openvino --model {llm_model_id} --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6  --sym  --trust-remote-code {llm_model_path}


```

### **OpenVINOを使用したPhi-3.5-Visionの量子化**

PythonまたはJupyter Labで以下のスクリプトを実行してください。

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

### **🤖 Intel OpenVINOを使用したPhi-3.5のサンプル**

| ラボ    | 説明 | 移動 |
| -------- | ------- |  ------- |
| 🚀 Lab-Phi-3.5 Instructの紹介  | Phi-3.5 InstructをAI PCで使用する方法を学ぶ    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-instruct-zh.ipynb)    |
| 🚀 Lab-Phi-3.5 Vision（画像）の紹介 | Phi-3.5 Visionを使用してAI PCで画像を分析する方法を学ぶ      |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-img.ipynb)    |
| 🚀 Lab-Phi-3.5 Vision（動画）の紹介   | Phi-3.5 Visionを使用してAI PCで動画を分析する方法を学ぶ    |  [Go](../../../../../code/09.UpdateSamples/Aug/intel-phi35-vision-video.ipynb)    |

## **リソース**

1. Intel OpenVINOの詳細はこちら [https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html](https://www.intel.com/content/www/us/en/developer/tools/openvino-toolkit/overview.html)

2. Intel OpenVINO GitHubリポジトリ [https://github.com/openvinotoolkit/openvino.genai](https://github.com/openvinotoolkit/openvino.genai)

**免責事項**:  
本書類は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を追求しておりますが、自動翻訳にはエラーや不正確な表現が含まれる場合があります。原文（原言語で記載された文書）が正式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用により生じた誤解や誤った解釈について、当方は一切の責任を負いません。