## 欢迎使用 VS Code 的 AI 工具包

[AI Toolkit for VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) 将 Azure AI Studio Catalog 和其他目录（如 Hugging Face）的各种模型汇集在一起。该工具包通过以下方式简化了使用生成式 AI 工具和模型构建 AI 应用程序的常见开发任务： 
- 从模型发现和Playground开始。
- 使用本地计算资源进行模型微调和推理。
- 使用 Azure 资源进行远程微调和推理。

[安装 VS Code 的 AI 工具包](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../imgs/04/00/Aitoolkit.png)


**[ 私有预览 ]** 一键配置 Azure 容器应用程序，以在云端运行模型微调和推理。

现在让我们开始您的AI应用开发之旅:

- [欢迎使用 VS Code 的 AI 工具包](#欢迎使用-vs-code-的-ai-工具包)
- [本地开发](#本地开发)
  - [准备工作](#准备工作)
  - [激活 Conda](#激活-conda)
  - [只进行基础模型微调](#只进行基础模型微调)
  - [模型的微调和推理](#模型的微调和推理)
  - [模型微调](#模型微调)
  - [Microsoft Olive](#microsoft-olive)
  - [微调示例和资源](#微调示例和资源)
- [**\[ 私有预览 \]** 远程开发](#-私有预览--远程开发)
  - [先决条件](#先决条件)
  - [创建一个远程开发的项目](#创建一个远程开发的项目)
  - [Azure 资源准备](#azure-资源准备)
  - [\[可选\] 将 Huggingface Token添加到 Azure 容器应用程序的秘钥中](#可选-将-huggingface-token添加到-azure-容器应用程序的秘钥中)
  - [运行微调](#运行微调)
  - [配置推理端点](#配置推理端点)
  - [部署推理端点](#部署推理端点)
  - [高级用法](#高级用法)

## 本地开发
### 准备工作

1. 确保主机已安装 NVIDIA 驱动程序。
2. 如果您使用 HF 进行数据集使用，请运行 `huggingface-cli login`。
3. 关于修改内存使用的所有设置，可以查阅 `Olive` 中的设置. 

### 激活 Conda
由于我们正在使用 WSL（Windows Subsystem for Linux）环境，并且它是共享的，因此需要手动激活 conda 环境。完成此步骤后，您可以进行微调或推理。

```bash
conda activate [conda-env-name] 
```

### 只进行基础模型微调
要尝试只进行基础模型的微调，可以在激活conda后运行此命令。

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### 模型的微调和推理

一旦在开发容器中打开工作空间，请打开终端（默认路径为项目根目录），然后运行以下命令以在选定数据集上微调 LLM（大型语言模型）。

```bash
python finetuning/invoke_olive.py 
```

检查点和最终模型将保存在 `models` 文件夹中.

接下来，在 `console`, `web browser` 或 `prompt flow` 中通过对话运行已微调模型的推理。

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

在VS Code中使用 `prompt flow`, 请参考这篇文档 [Quick Start](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html)。

### 模型微调

接下来，根据设备上 GPU 的可用性，下载以下模型。

要使用 QLoRA 启动本地微调会话，请从我们的目录中选择要微调的模型。
| 平台 | GPU 可用性 | 模型名称 | 模型大小 (GB) |
|---------|---------|--------|--------|
| Windows | 是 | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | 是 | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | 否 | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_注意_** 您无需使用Azure账户来下载模型。

Phi3-mini（int4）模型的大小约为 2GB-3GB。根据您的网络速度，下载可能需要几分钟的时间。

首先选择项目名称和位置。接下来，从模型目录中选择一个模型。您将被提示下载项目模板。然后，您可以单击“配置项目”以调整各种设置。


### Microsoft Olive 

我们使用 [Olive](https://microsoft.github.io/Olive/overview/olive.html) 在我们目录的 PyTorch 模型上运行 QLoRA 微调。所有设置都预设为默认值，以优化内存使用并在本地运行微调过程，但可以根据您的场景进行调整。

### 微调示例和资源

- [Fine tuning Getting Started Guide](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [Fine tuning with a HuggingFace Dataset](https://github.com/microsoft/vscode-ai-toolkit/blob/main/walkthrough-hf-dataset.md)
- [Fine tuning with Simple DataSet](https://github.com/microsoft/vscode-ai-toolkit/blob/main/walkthrough-simple-dataset.md)


## **[ 私有预览 ]** 远程开发
### 先决条件
1. 要在远程 Azure 容器应用环境中运行模型微调，请确保您的订阅具有足够的 GPU 容量。提交 [支持工单](https://azure.microsoft.com/support/create-ticket/) 以请求应用程序所需的容量。了解有关 GPU 容量的更多信息，请参考 [Get More Info about GPU capacity](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)。
2. 如果您在 HuggingFace 上使用私有数据集，请确保您拥有HuggingFace账户 [HuggingFace account](https://huggingface.co/) 并 [生成访问令牌](https://huggingface.co/docs/hub/security-tokens)。
3. 在 VS Code 的 AI 工具包中启用远程微调和推理功能标志。
   1. 通过选择 *File -> Preferences -> Settings* 来打开 VS Code 设置。
   2. 导航至 *Extensions* 并选择 *AI Toolkit*。
   3. 选择 *"Enable Remote Fine-tuning And Inference"* 选项。
   4. 重新加载 VS Code 以生效。

- [Remote Fine tuning](https://github.com/microsoft/vscode-ai-toolkit/blob/main/remote-finetuning.md)

### 创建一个远程开发的项目
1. 在命令面板中执行 `AI Toolkit: Focus on Resource View`。
2. 导航到 *Model Fine-tuning* 以访问模型目录。为您的项目分配一个名称，并选择在您的计算机上的位置。然后点击 *"Configure Project"* 按钮。
3. 项目配置
    1. 避免启用 *"Fine-tune locally"* 选项。
    2. Olive 配置将显示预设的默认值。请根据需要调整并填写这些配置。
    3. 导航到 *Generate Project*。这个阶段利用 WSL，并涉及设置一个新的 Conda 环境，为未来包含 Dev Containers 的更新做准备。
4. 点击 *"Relaunch Window In Workspace"* 以打开您的远程开发项目。

> **注意:** 项目当前在 AI 工具包的 VS Code 中仅在本地或远程工作。如果在项目创建过程中选择 *"Fine-tune locally"*，它将仅在 WSL 中运行，而不具有远程开发功能。另一方面，如果您放弃启用 *"Fine-tune locally"*, 项目将仅限于远程 Azure 容器应用环境。

### Azure 资源准备
要开始使用，您需要为远程微调提供 Azure 资源。通过从命令面板运行 `AI Toolkit: Provision Azure Container Apps job for fine-tuning` 来实现这一点。

通过输出通道中显示的链接监控配置的进度。

### [可选] 将 Huggingface Token添加到 Azure 容器应用程序的秘钥中
如果您使用的是私有 HuggingFace 数据集，请将 HuggingFace 令牌设置为环境变量，以避免在 Hugging Face Hub 上进行手动登录。
您可以使用 `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning command` 命令来实现这一点。使用此命令，您可以将秘钥名称设置为 [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken)，并将您的 Hugging Face 令牌用作秘钥值。

### 运行微调
要启动远程微调任务，请执行 `AI Toolkit: Run fine-tuning` 命令。

要查看系统和控制台日志，您可以使用输出面板中的链接访问 Azure 门户（在 Azure 上查看和查询日志中有更多步骤 [View and Query Logs on Azure](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure))。 或者，您可以通过运行命令 `AI Toolkit: Show the running fine-tuning job streaming logs`，直接在 VS Code 输出面板中查看控制台日志。
> **注意:** 由于资源不足，任务可能会排队。如果日志未显示，请执行 `AI Toolkit: Show the running fine-tuning job streaming logs` 命令，稍等片刻，然后再次执行命令以重新连接到流日志。

在此过程中，QLoRA 将用于微调，并为在推理过程中使用模型而创建 LoRA 适配器。微调结果将存储在 Azure Files中。 

### 配置推理端点
在远程环境中训练适配器后，使用简单的 Gradio 应用程序与模型进行交互。与微调过程类似，您需要通过执行命令面板中的 `AI Toolkit: Provision Azure Container Apps for inference` 命令来设置远程推理的 Azure 资源。 
   
默认情况下，推理所使用的订阅和资源组应与微调过程中使用的相匹配。推理将使用相同的 Azure 容器应用程序环境，并访问存储在 Azure Files中的模型和模型适配器，这些文件是在微调步骤中生成的。


### 部署推理端点
如果您希望修改推理代码或重新加载推理模型，请执行 `AI Toolkit: Deploy for inference` 命令。这将使您的最新代码与 Azure 容器应用程序同步并重新启动副本。

部署成功完成后，您可以通过单击 VSCode 通知中显示的 "*Go to Inference Endpoint*" 按钮访问推理 API。或者，可以在 `./infra/inference.config.json` 文件中的 `ACA_APP_ENDPOINT` 和输出面板中找到 Web API 端点。现在，您可以使用此端点来评估模型了。

### 高级用法
有关使用 AI Toolkit 进行远程开发的更多信息，请参阅远程微调模型 [Fine-Tuning models remotely](https://aka.ms/ai-toolkit/remote-provision) 和 推理与微调模型 [Inferencing with the fine-tuned model](https://aka.ms/ai-toolkit/remote-inference) 文档。