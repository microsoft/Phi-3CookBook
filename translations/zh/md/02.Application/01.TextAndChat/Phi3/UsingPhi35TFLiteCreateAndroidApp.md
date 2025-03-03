# **使用 Microsoft Phi-3.5 tflite 创建 Android 应用**

这是一个使用 Microsoft Phi-3.5 tflite 模型的 Android 示例。

## **📚 知识点**

Android LLM 推理 API 允许您在 Android 应用程序中完全在设备上运行大语言模型（LLMs），可以用来执行多种任务，例如生成文本、以自然语言形式检索信息和总结文档。该任务为多种文本到文本的大语言模型提供了内置支持，因此您可以将最新的设备端生成式 AI 模型应用到您的 Android 应用中。

Google AI Edge Torch 是一个支持将 PyTorch 模型转换为 .tflite 格式的 Python 库，随后可以通过 TensorFlow Lite 和 MediaPipe 运行。这使得 Android、iOS 和物联网设备上的应用程序能够完全在设备上运行模型。AI Edge Torch 提供了广泛的 CPU 支持，并初步支持 GPU 和 NPU。AI Edge Torch 致力于与 PyTorch 紧密集成，基于 torch.export() 构建，并提供对 Core ATen 操作符的良好支持。

## **🪬 指南**

### **🔥 将 Microsoft Phi-3.5 转换为 tflite 支持**

0. 本示例适用于 Android 14 及以上版本

1. 安装 Python 3.10.12

***建议：*** 使用 conda 安装您的 Python 环境

2. Ubuntu 20.04 / 22.04（请重点关注 [google ai-edge-torch](https://github.com/google-ai-edge/ai-edge-torch)）

***建议：*** 使用 Azure Linux 虚拟机或第三方云虚拟机来创建您的环境

3. 打开 Linux bash，安装 Python 库

```bash

git clone https://github.com/google-ai-edge/ai-edge-torch.git

cd ai-edge-torch

pip install -r requirements.txt -U 

pip install tensorflow-cpu -U

pip install -e .

```

4. 从 Hugging Face 下载 Microsoft-3.5-Instruct

```bash

git lfs install

git clone  https://huggingface.co/microsoft/Phi-3.5-mini-instruct

```

5. 将 Microsoft Phi-3.5 转换为 tflite

```bash

python ai-edge-torch/ai_edge_torch/generative/examples/phi/convert_phi3_to_tflite.py --checkpoint_path  Your Microsoft Phi-3.5-mini-instruct path --tflite_path Your Microsoft Phi-3.5-mini-instruct tflite path  --prefill_seq_len 1024 --kv_cache_max_len 1280 --quantize True

```

### **🔥 将 Microsoft Phi-3.5 转换为 Android Mediapipe Bundle**

请先安装 mediapipe

```bash

pip install mediapipe

```

在 [您的 notebook](../../../../../../code/09.UpdateSamples/Aug/Android/convert/convert_phi.ipynb) 中运行以下代码

```python

import mediapipe as mp
from mediapipe.tasks.python.genai import bundler

config = bundler.BundleConfig(
    tflite_model='Your Phi-3.5 tflite model path',
    tokenizer_model='Your Phi-3.5 tokenizer model path',
    start_token='start_token',
    stop_tokens=[STOP_TOKENS],
    output_filename='Your Phi-3.5 task model path',
    enable_bytes_to_unicode_mapping=True or Flase,
)
bundler.create_bundle(config)

```

### **🔥 使用 adb 将任务模型推送到 Android 设备路径**

```bash

adb shell rm -r /data/local/tmp/llm/ # Remove any previously loaded models

adb shell mkdir -p /data/local/tmp/llm/

adb push 'Your Phi-3.5 task model path' /data/local/tmp/llm/phi3.task

```

### **🔥 运行您的 Android 代码**

![demo](../../../../../../translated_images/demo.8981711efb5a9cee5dcd835f66b3b31b94b4f3e527300e15a98a0d48863b9fbd.zh.png)

**免责声明**:  
本文件使用基于机器的人工智能翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的原文作为权威来源。对于关键性信息，建议使用专业人工翻译。我们不对因使用本翻译而产生的任何误解或误读承担责任。