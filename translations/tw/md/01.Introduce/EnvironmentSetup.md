# 在本地开始使用 Phi-3

本指南将帮助你设置本地环境，以使用 Ollama 运行 Phi-3 模型。你可以通过几种不同的方式运行该模型，包括使用 GitHub Codespaces、VS Code Dev Containers 或你的本地环境。

## 环境设置

### GitHub Codespaces

你可以通过使用 GitHub Codespaces 虚拟运行此模板。点击按钮将在你的浏览器中打开基于 Web 的 VS Code 实例：

1. 打开模板（这可能需要几分钟时间）：

    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)

2. 打开一个终端窗口

### VS Code Dev Containers

⚠️ 此选项仅在你的 Docker Desktop 分配了至少 16 GB 内存时可用。如果你的内存少于 16 GB，可以尝试 [GitHub Codespaces 选项](../../../../md/01.Introduce) 或 [在本地设置](../../../../md/01.Introduce)。

一个相关选项是 VS Code Dev Containers，它将使用 [Dev Containers 扩展](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 在你的本地 VS Code 中打开项目：

1. 启动 Docker Desktop（如果尚未安装，请先安装）
2. 打开项目：

    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

3. 在打开的 VS Code 窗口中，一旦项目文件显示出来（这可能需要几分钟时间），打开一个终端窗口。
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

    这将需要几分钟时间来下载模型。

2. 一旦在输出中看到 "success"，你可以从提示中向该模型发送消息。

    ```shell
    >>> Write a haiku about hungry hippos
    ```

3. 几秒钟后，你应该会看到模型的响应流。

4. 要了解使用语言模型的不同技术，打开 Python notebook [ollama.ipynb](../../../../code/01.Introduce/ollama.ipynb) 并运行每个单元格。如果你使用的不是 'phi3:mini' 模型，请根据需要更改文件顶部的 `MODEL_NAME` in the first cell.

5. To have a conversation with the phi3:mini model from Python, open the Python file [chat.py](../../../../code/01.Introduce/chat.py) and run it. You can change the `MODEL_NAME`，你还可以修改系统消息或添加 few-shot 示例。

**免責聲明**:
本文檔已使用機器翻譯服務進行翻譯。我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原語言的原始文檔為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對使用此翻譯所產生的任何誤解或誤釋不承擔責任。