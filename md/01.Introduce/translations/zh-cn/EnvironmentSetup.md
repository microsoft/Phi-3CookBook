## 打开项目

我们提供了一个 Ollama Python Playground

该项目旨在通过 GitHub Codespaces 方便任何人在浏览器中完全尝试 SLM（小型语言模型）。

1. 点击仓库顶部的 `Code` 按钮，使用浏览器打开 Codespace。
2. 一旦 Codespace 加载完毕，它应该会有 [ollama](https://ollama.com/)。
3. 向 Ollama 请求运行您选择的 SLM. 例如，运行 [phi3] (https://ollama.com/library/phi3) 模型:

    ```shell
    ollama run phi3:mini
    ```

    这将花费几分钟时间将模型下载到 Codespace。
4. 一旦您在输出中看到“成功”，您就可以从提示符向该模型发送消息。

    ```shell
    >>> Write a haiku about hungry hippos
    ```

5. 经过几秒钟，您应该会看到模型传入的响应流。
6. 要了解与语言模型相关的不同技术，请打开 Python notebook 文件`ollama.ipynb` 并运行每个单元格。如果您使用的模型不是 'phi3:mini'，请更改第一个单元格中的`MODEL_NAME` 。
7. 要使用 Python 与模型进行对话，请打开 Python 文件 `chat.py` 并运行它。您可以根据需要更改文件顶部的 `MODEL_NAME`，并且如果需要，还可以修改系统消息或添加少量示例。

您有一些选择来开始使用此模板。上手最快的方法是使用 GitHub Codespaces，因为它会为您设置所有工具，但您也可以在本地进行设置。 [设置本地环境](#local-environment).

### GitHub Codespaces

您可以通过使用 GitHub Codespaces 在虚拟环境中运行此模板。此按钮将在您的浏览器中打开一个基于 Web 的 VS Code 实例:

1. 打开模板（这可能需要几分钟时间）:

    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)

2. 打开一个终端窗口
3. 继续进行部署步骤 [deployment steps](#deployment)

### VS Code Dev Containers

一个可用的选项是 VS Code Dev Containers，它将使用 [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 扩展在本地 VS Code 中打开项目:

1. 启动Docker Desktop（如果尚未安装，请安装它）
2. 打开项目:

    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

3. 在打开的VS Code窗口中，一旦项目文件显示出来(这可能需要几分钟)，打开一个终端窗口。
4. 继续进行部署步骤 [deployment steps](#deployment)

### Local Environment

1. 确保您已经安装以下工具:

    * [Python 3.10+](https://www.python.org/downloads/)
    * [Docker Desktop](https://www.docker.com/products/docker-desktop/)
    * [Git](https://git-scm.com/downloads)
    * [OpenAI Python SDK](https://pypi.org/project/openai/)

2. 打开项目文件夹

3. 安装OpenAI的Python库:

    ```shell
    pip install openai
    ```