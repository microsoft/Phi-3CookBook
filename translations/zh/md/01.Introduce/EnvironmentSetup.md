# 本地开始使用 Phi-3

本指南将帮助您使用 Ollama 设置本地环境以运行 Phi-3 模型。您可以通过几种不同的方式运行该模型，包括使用 GitHub Codespaces、VS Code Dev Containers 或本地环境。

## 环境设置

### GitHub Codespaces

您可以使用 GitHub Codespaces 虚拟运行此模板。点击按钮将在浏览器中打开基于 Web 的 VS Code 实例：

1. 打开模板（这可能需要几分钟）：

    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)

2. 打开一个终端窗口

### VS Code Dev Containers

⚠️ 该选项仅在您的 Docker Desktop 分配了至少 16 GB 的 RAM 时才可用。如果您的 RAM 少于 16 GB，可以尝试 [GitHub Codespaces 选项](../../../../md/01.Introduce) 或 [本地设置](../../../../md/01.Introduce)。

另一个相关选项是 VS Code Dev Containers，它将使用 [Dev Containers 扩展](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 在本地 VS Code 中打开项目：

1. 启动 Docker Desktop（如果尚未安装，请先安装）
2. 打开项目：

    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

3. 在打开的 VS Code 窗口中，项目文件显示后（这可能需要几分钟），打开一个终端窗口。
4. 继续 [部署步骤](../../../../md/01.Introduce)

### 本地环境

1. 确保安装了以下工具：

    * [Ollama](https://ollama.com/)
    * [Python 3.10+](https://www.python.org/downloads/)
    * [OpenAI Python SDK](https://pypi.org/project/openai/)

## 测试模型

1. 让 Ollama 下载并运行 phi3:mini 模型：

    ```shell
    ollama run phi3:mini
    ```

    这将需要几分钟来下载模型。

2. 当您在输出中看到 "success" 时，可以在提示符中向该模型发送消息。

    ```shell
    >>> Write a haiku about hungry hippos
    ```

3. 几秒钟后，您应该会看到模型的响应流入。

4. 要了解与语言模型一起使用的不同技术，请打开 Python 笔记本 [ollama.ipynb](../../../../code/01.Introduce/ollama.ipynb) 并运行每个单元格。如果您使用了 'phi3:mini' 以外的模型，请在第一个单元格中更改 `MODEL_NAME`。

5. 要从 Python 与 phi3:mini 模型进行对话，请打开 Python 文件 [chat.py](../../../../code/01.Introduce/chat.py) 并运行它。您可以根据需要更改文件顶部的 `MODEL_NAME`，还可以修改系统消息或添加 few-shot 示例。

免责声明：此翻译由AI模型从原文翻译而来，可能不完美。请审阅输出内容并进行必要的修改。