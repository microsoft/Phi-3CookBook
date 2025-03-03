# **使用 Generative AI extensions for onnxruntime 量化 Phi 系列**

## **什么是 Generative AI extensions for onnxruntime**

该扩展帮助您在 ONNX Runtime（[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)）上运行生成式 AI。它为 ONNX 模型提供生成式 AI 的循环功能，包括使用 ONNX Runtime 推理、logits 处理、搜索与采样以及 KV 缓存管理。开发者可以调用高级的 generate() 方法，或在循环中逐次运行模型生成一个 token，并可选择在循环中更新生成参数。它支持贪婪搜索/束搜索以及 TopP、TopK 采样生成 token 序列，还内置了诸如重复惩罚等 logits 处理功能。此外，您还可以轻松添加自定义评分。

在应用层面，您可以使用 Generative AI extensions for onnxruntime 用 C++/C#/Python 构建应用程序。在模型层面，您可以利用它来合并微调模型并进行相关的量化部署工作。

## **使用 Generative AI extensions for onnxruntime 量化 Phi-3.5**

### **支持的模型**

Generative AI extensions for onnxruntime 支持对 Microsoft Phi、Google Gemma、Mistral 和 Meta LLaMA 的量化转换。

### **Generative AI extensions for onnxruntime 的 Model Builder**

Model Builder 大大加速了创建能够使用 ONNX Runtime generate() API 运行的优化和量化 ONNX 模型的过程。

通过 Model Builder，您可以将模型量化为 INT4、INT8、FP16、FP32，并结合 CPU、CUDA、DirectML、Mobile 等不同的硬件加速方法。

要使用 Model Builder，您需要安装：

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

安装完成后，您可以从终端运行 Model Builder 脚本来进行模型格式和量化转换。

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

了解相关参数：

1. **model_name** 这是 Hugging Face 上的模型名称，例如 microsoft/Phi-3.5-mini-instruct、microsoft/Phi-3.5-vision-instruct 等。也可以是您存储模型的路径。

2. **path_to_output_folder** 量化转换的保存路径。

3. **execution_provider** 不同的硬件加速支持，例如 cpu、cuda、DirectML。

4. **cache_dir_to_save_hf_files** 我们从 Hugging Face 下载模型并将其缓存到本地。

***注意：***

## **如何使用 Model Builder 量化 Phi-3.5**

Model Builder 现在支持 Phi-3.5-Instruct 和 Phi-3.5-Vision 的 ONNX 模型量化。

### **Phi-3.5-Instruct**

**通过 CPU 加速转换为量化的 INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**通过 CUDA 加速转换为量化的 INT4**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. 在终端中设置环境

```bash

mkdir models

cd models 

```

2. 在 models 文件夹中下载 microsoft/Phi-3.5-vision-instruct  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. 请下载以下文件到您的 Phi-3.5-vision-instruct 文件夹：

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. 下载以下文件到 models 文件夹：  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. 打开终端

    转换为支持 FP32 的 ONNX

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **注意：**

1. Model Builder 当前支持 Phi-3.5-Instruct 和 Phi-3.5-Vision 的转换，但不支持 Phi-3.5-MoE。

2. 要使用 ONNX 的量化模型，可以通过 Generative AI extensions for onnxruntime SDK 使用。

3. 我们需要考虑更负责任的 AI，因此在模型量化转换后，建议进行更有效的结果测试。

4. 通过量化 CPU INT4 模型，我们可以将其部署到边缘设备，这在应用场景上更具优势，因此我们围绕 INT4 完成了 Phi-3.5-Instruct 的工作。

## **资源**

1. 了解更多关于 Generative AI extensions for onnxruntime 的信息：  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Generative AI extensions for onnxruntime 的 GitHub 仓库：  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**免责声明**:  
本文件通过基于机器的人工智能翻译服务翻译而成。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文件作为权威来源。对于关键信息，建议寻求专业人工翻译。对于因使用此翻译而引起的任何误解或误读，我们概不负责。