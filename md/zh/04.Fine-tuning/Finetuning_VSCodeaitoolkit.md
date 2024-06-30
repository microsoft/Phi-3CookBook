# 欢迎使用 VS Code 的 AI Toolkit

[VS Code 的 AI Toolkit](https://github.com/microsoft/vscode-ai-toolkit/tree/main) 集成了来自 Azure AI Studio 目录和其他目录（如 Hugging Face）的各种模型。该工具包通过以下方式简化了使用生成式 AI 工具和模型构建 AI 应用程序的常见开发任务：
- 从发现模型并用 playground 开始模型开始。
- 使用本地计算资源进行模型微调和推理。
- 使用 Azure 资源进行远程微调和推理。

[安装 VS Code 的 AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../imgs/04/00/Aitoolkit.png)


**[私有预览]** 一键配置 Azure 容器应用以在云中运行模型微调和推理。

现在让我们开始您的 AI 应用程序开发：

- [本地开发](#本地开发)
  - [准备](#准备)
  - [激活 Conda](#激活-conda)
  - [仅基础模型微调](#仅基础模型微调)
  - [模型微调和推理](#模型微调和推理)
  - [模型微调](#模型微调)
  - [Microsoft Olive](#microsoft-olive)
  - [微调示例和资源](#微调示例和资源)
- [[私有预览] 远程开发](#私有预览-远程开发)
  - [先决条件](#先决条件)
  - [设置远程开发项目](#设置远程开发项目)
  - [配置 Azure 资源](#配置-azure-资源)
  - [\[可选\] 将 Huggingface 令牌添加到 Azure 容器应用密钥](#可选-将-huggingface-令牌添加到-azure-容器应用密钥)
  - [运行微调](#运行微调)
  - [配置推理端点](#配置推理端点)
  - [部署推理端点](#部署推理端点)
  - [高级用法](#高级用法)

## 本地开发
### 准备

1. 确保在主机上安装了 NVIDIA 驱动程序。
2. 如果您使用 HF 进行数据集利用，请运行 `huggingface-cli login`。
3. 查看 `Olive` 的设置解释，用于修改内存使用情况。

### 激活 Conda
由于我们使用的是共享的 WSL 环境，您需要手动激活 conda 环境。完成此步骤后，您可以运行微调或推理。

```bash
conda activate [conda-env-name] 
```

### 仅基础模型微调
在激活 conda 后，您可以运行以下命令尝试基础模型而无需微调。

```bash
cd inference

# Web 浏览器界面允许调整一些参数，如最大生成 token 长度、温度等。
# Gradio 建立连接后，用户必须手动在浏览器中打开链接（例如：http://0.0.0.0:7860）。
python gradio_chat.py --baseonly
```

### 模型微调和推理

在开发容器中打开工作区后，打开终端（默认路径为项目根目录），然后运行下面的命令对选定数据集进行 LLM 微调。

```bash
python finetuning/invoke_olive.py 
```

检查点和最终模型将保存在 `models` 文件夹中。

接下来，通过 `终端`、`Web 浏览器` 或 `prompt flow` 使用微调后的模型进行推理。

```bash
cd inference

# 控制台界面。
python console_chat.py

# Web 浏览器界面允许调整一些参数，如最大生成 token 长度、温度等。
# Gradio 建立连接后，用户必须手动在浏览器中打开链接（例如：http://127.0.0.1:7860）。
python gradio_chat.py
```

要在 VS Code 中使用 `prompt flow`，请参阅此[快速入门](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html)。

### 模型微调

接下来，根据您的设备上 GPU 的可用性下载以下模型。

要使用 QLoRA 启动本地微调会话，请从我们的目录中选择要微调的模型。
| 平台 | 有 GPU | 模型名称 | 大小 (GB) |
|---------|---------|--------|--------|
| Windows | 是 | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | 是 | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | 否 | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_注意_** 您不需要 Azure 账户即可下载模型。

Phi3-mini (int4) 模型的大小约为 2GB-3GB，下载时间可能会因您的网络速度而有所不同。

首先选择一个项目名称和位置。
接下来，从模型目录中选择一个模型。系统会提示您下载项目模板。然后您可以点击“配置项目”以调整各种设置。

### Microsoft Olive 

我们使用 [Olive](https://microsoft.github.io/Olive/overview/olive.html) 在我们的目录中运行 PyTorch 模型的 QLoRA 微调。所有设置均已预设为默认值，以优化本地运行微调过程的内存使用，但可以根据您的场景进行调整。

### 微调示例和资源

- [微调入门指南](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [使用 HuggingFace 数据集进行微调](https://github.com/microsoft/vscode-ai-toolkit/blob/main/walkthrough-hf-dataset.md)
- [使用简单数据集进行微调](https://github.com/microsoft/vscode-ai-toolkit/blob/main/walkthrough-simple-dataset.md)


## [私有预览] 远程开发
### 先决条件
1. 要在远程 Azure 容器应用环境中运行模型微调，请确保您的订阅具有足够的 GPU 容量。提交 [支持票证](https://azure.microsoft.com/support/create-ticket/) 以申请应用程序所需的资源。[了解更多关于 GPU 负载的信息](https://learn.microsoft.com/en-us/azure/container-apps/workload-profiles-overview)
2. 如果您在 HuggingFace 上使用私有数据集，请确保您有一个 [HuggingFace 账户](https://huggingface.co/) 并 [生成访问令牌](https://huggingface.co/docs/hub/security-tokens)
3. 在 VS Code 的 AI Toolkit 中启用远程微调和推理功能标志
   1. 选择 *文件 -> 首选项 -> 设置* 打开 VS Code 设置。
   2. 导航到 *扩展* 并选择 *AI Toolkit*。
   3. 选择 *"Enable Remote Fine-tuning And Inference"* 选项。
   4. 重新加载 VS Code 以生效。

- [远程微调](https://github.com/microsoft/vscode-ai-toolkit/blob/main/remote-finetuning.md)

### 设置远程开发项目
1. 执行命令面板 `AI Toolkit: Focus on Resource View`。
2. 导航到 *Configure Project* 以访问模型目录。为您的项目指定一个名称并选择其在机器上的位置。然后点击 *"配置项目"* 按钮。
3. 项目配置
    1. 避免启用 *"Fine-tune locally"* 选项。
    2. Olive 配置将以预设默认值显示。请根据需要调整和填写这些配置。
    3. 继续 *Generate Project*。此阶段利用 WSL，并涉及设置一个新的 Conda 环境，为未来的开发容器更新做准备。
4. 点击 *"Relaunch Window In Workspace"* 以打开您的远程开发项目。

> **注意：** 该项目目前在 VS Code 的 AI Toolkit 中本地或远程运行。如果在项目创建期间选择 *"本地微调"*，它将仅在 WSL 中运行而不具备远程开发能力。相反，如果未启用 *"本地微调"*，则项目将限制在远程 Azure 容器应用环境中。

### 配置 Azure 资源
在开始之前，需要为远程微调配置 Azure 资源。通过从命令面板运行 `AI Toolkit: Provision Azure Container Apps job for fine-tuning` 来完成此操作。

通过输出通道显示的链接监视配置进度。

### [可选] 将 Huggingface 令牌添加到 Azure 容器应用密钥
如果您使用的是私有 HuggingFace 数据集，请将您的 HuggingFace 令牌设置为环境变量，以避免在 Hugging Face Hub 上手动登录。
您可以使用 `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning` 命令来完成此操作。通过此命令，您可以将密钥名称设置为 [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) 并使用您的 Hugging Face 令牌作为密钥值。

### 运行微调
要启动远程微调作业，请执行 `AI Toolkit: Run fine-tuning` 命令。

要查看系统和控制台日志，可以使用输出面板中的链接访问 Azure 门户（更多步骤请参阅 [在 Azure 上查看和查询日志](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)）。或者，您可以通过运行 `AI Toolkit: Show the running fine-tuning job streaming logs` 命令，在 VSCode 输出面板中直接查看控制台日志。
> **注意：** 作业可能由于资源不足而排队。如果日志未显示，请执行 `AI Toolkit: Show the running fine-tuning job streaming logs` 命令，等待一段时间，然后再次执行命令以重新连接到流日志。

在此过程中，将使用 QLoRA 进行微调，并为模型创建 LoRA Adapter以在推理时使用。
微调结果将存储在 Azure 文件中。

### 配置推理端点
在远程环境中训练完Adapter后，使用一个简单的 Gradio 应用程序与模型进行交互。
与微调过程类似，您需要通过执行命令面板中的 `AI Toolkit: Provision Azure Container Apps for inference` 来设置远程推理的 Azure 资源。

默认情况下，用于推理的订阅和资源组应与用于微调的订阅和资源组一致。。推理将使用相同的 Azure 容器应用环境，并访问在微调步骤中生成的存储在 Azure 文件中的模型和模型Adapter。

### 部署推理端点
如果您希望修改推理代码或重新加载推理模型，请执行 `AI Toolkit: Deploy for inference` 命令。这将同步 Azure 容器应用程序到您最新的代码，并重新加载模型。

部署成功后，您可以通过 VSCode 通知中显示的 "*Go to Inference Endpoint*" 按钮访问推理 API。或者，Web API 端点可以在 `./infra/inference.config.json` 中的 `ACA_APP_ENDPOINT` 以及输出面板中找到。现在，您可以使用此端点评估模型。

### 高级用法
有关使用 AI Toolkit 进行远程开发的更多信息，请参阅 [远程微调模型](https://aka.ms/ai-toolkit/remote-provision) 和 [使用微调模型进行推理](https://aka.ms/ai-toolkit/remote-inference) 文档。