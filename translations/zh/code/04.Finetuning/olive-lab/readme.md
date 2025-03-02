# 实验：优化 AI 模型以便设备端推理

## 简介

> [!IMPORTANT]  
> 本实验需要一台安装了相关驱动程序和 CUDA 工具包（版本 12 以上）的 **Nvidia A10 或 A100 GPU**。

> [!NOTE]  
> 这是一个 **35 分钟** 的实验，旨在通过使用 OLIVE 进行设备端推理优化模型的核心概念的动手实践。

## 学习目标

完成本实验后，您将能够使用 OLIVE：

- 使用 AWQ 量化方法对 AI 模型进行量化。
- 针对特定任务微调 AI 模型。
- 生成 LoRA 适配器（微调模型），以便在 ONNX Runtime 上实现高效的设备端推理。

### 什么是 Olive

Olive (*O*NNX *live*) 是一个模型优化工具包，配有 CLI，可以帮助您为 ONNX Runtime +++https://onnxruntime.ai+++ 提供高质量和高性能的模型。

![Olive 流程](../../../../../translated_images/olive-flow.e4682fa65f77777f49e884482fa8dd83eadcb90904fcb41a54093af85c330060.zh.png)

Olive 的输入通常是一个 PyTorch 或 Hugging Face 模型，输出是一个优化后的 ONNX 模型，该模型将在运行 ONNX Runtime 的设备（部署目标）上执行。Olive 会针对由硬件供应商（如 Qualcomm、AMD、Nvidia 或 Intel）提供的部署目标的 AI 加速器（NPU、GPU、CPU）优化模型。

Olive 执行一个 *工作流*，即一系列有序的单独模型优化任务，称为 *passes*。例如：模型压缩、图捕获、量化、图优化等。每个 pass 都有一组可调参数，以实现最佳指标（如准确性和延迟），这些指标由相应的评估器评估。Olive 使用搜索算法逐个或成组地自动调整 pass，以实现优化。

#### Olive 的优势

- **减少试错实验的挫败感和时间**：通过不同的图优化、压缩和量化技术，定义您的质量和性能约束，Olive 会自动为您找到最佳模型。
- **40 多种内置模型优化组件**：涵盖量化、压缩、图优化和微调的前沿技术。
- **易于使用的 CLI**：可用于常见的模型优化任务，例如 `olive quantize`、`olive auto-opt`、`olive finetune`。
- 内置模型打包和部署功能。
- 支持生成 **多 LoRA 服务** 的模型。
- 使用 YAML/JSON 构建工作流，以协调模型优化和部署任务。
- 与 **Hugging Face** 和 **Azure AI** 集成。
- 内置 **缓存机制**，以 **节省成本**。

## 实验步骤
> [!NOTE]  
> 请确保您已按照实验 1 的要求配置了 Azure AI Hub 和项目，并设置了 A100 计算资源。

### 步骤 0：连接到 Azure AI 计算资源

您将通过 **VS Code** 的远程功能连接到 Azure AI 计算资源。

1. 打开 **VS Code** 桌面应用程序：
2. 使用 **Shift+Ctrl+P** 打开 **命令面板**。
3. 在命令面板中搜索 **AzureML - remote: Connect to compute instance in New Window**。
4. 按屏幕提示操作以连接到计算资源。这包括选择您在实验 1 中设置的 Azure 订阅、资源组、项目和计算名称。
5. 连接到 Azure ML 计算节点后，这将在 **VS Code 左下角** 显示 `><Azure ML: Compute Name`。

### 步骤 1：克隆此仓库

在 VS Code 中，您可以使用 **Ctrl+J** 打开新终端并克隆此仓库：

在终端中，您应该看到提示：

```
azureuser@computername:~/cloudfiles/code$ 
```  
克隆解决方案：

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### 步骤 2：在 VS Code 中打开文件夹

在终端中执行以下命令以在相关文件夹中打开 VS Code，这将打开一个新窗口：

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```  

或者，您也可以通过选择 **文件** > **打开文件夹** 来打开文件夹。

### 步骤 3：安装依赖项

在 VS Code 中的 Azure AI 计算实例中打开一个终端窗口（提示：**Ctrl+J**），然后执行以下命令以安装依赖项：

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```  

> [!NOTE]  
> 安装所有依赖项大约需要 5 分钟。

在此实验中，您需要下载和上传模型到 Azure AI 模型目录。为了访问模型目录，您需要使用以下命令登录到 Azure：

```bash
az login
```  

> [!NOTE]  
> 登录时，您将被要求选择订阅。请确保选择为本实验提供的订阅。

### 步骤 4：执行 Olive 命令

在 VS Code 中的 Azure AI 计算实例中打开一个终端窗口（提示：**Ctrl+J**），并确保已激活 `olive-ai` conda 环境：

```bash
conda activate olive-ai
```  

接下来，在命令行中执行以下 Olive 命令：

1. **检查数据**：在此示例中，您将微调 Phi-3.5-Mini 模型，使其专注于回答与旅行相关的问题。以下代码显示数据集的前几条记录，数据集格式为 JSON 行：

    ```bash
    head data/data_sample_travel.jsonl
    ```  

2. **量化模型**：在训练模型之前，首先使用以下命令对其进行量化，该命令采用一种称为 Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++ 的技术。AWQ 通过考虑推理期间产生的激活来量化模型权重。这意味着量化过程会考虑激活中的实际数据分布，从而比传统的权重量化方法更好地保持模型准确性。

    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```  

    AWQ 量化大约需要 **8 分钟**，并将模型大小从约 **7.5GB 减少到 2.5GB**。

    在本实验中，我们将向您展示如何从 Hugging Face 导入模型（例如：`microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` 命令微调量化后的模型。在微调之前对模型进行量化，而不是之后，这样可以获得更好的准确性，因为微调过程会恢复量化带来的一些损失。

    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```  

    微调（100 步）大约需要 **6 分钟**。

3. **优化模型**：模型训练完成后，使用 Olive 的 `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` 参数优化模型 - 在本实验中我们将使用 CPU。

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```  

    优化大约需要 **5 分钟**。

### 步骤 5：模型推理快速测试

为了测试模型的推理能力，在您的文件夹中创建一个名为 **app.py** 的 Python 文件，并复制以下代码：

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```  

使用以下命令执行代码：

```bash
python app.py
```  

### 步骤 6：上传模型到 Azure AI

将模型上传到 Azure AI 模型仓库后，模型可以与开发团队的其他成员共享，并且还支持模型的版本控制。使用以下命令上传模型：

> [!NOTE]  
> 更新 `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `` 中的 `resourceGroup` 和 Azure AI 项目名称，然后运行以下命令：

```
az ml workspace show
```  

或者，您可以访问 +++ai.azure.com+++，选择 **管理中心** > **项目** > **概览**。

更新 `{}` 占位符为您的资源组名称和 Azure AI 项目名称。

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```  
随后，您可以在 https://ml.azure.com/model/list 查看上传的模型并进行部署。

**免责声明**：  
本文件通过基于机器的人工智能翻译服务进行翻译。尽管我们尽力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文所在的语言版本为权威来源。对于关键信息，建议寻求专业人工翻译服务。对于因使用本翻译而引起的任何误解或误读，我们概不负责。