# 本地開始使用 Phi-3

這份指南將幫助你設置本地環境，以便使用 Ollama 運行 Phi-3 模型。你可以通過多種方式運行該模型，包括使用 GitHub Codespaces、VS Code Dev Containers 或本地環境。

## 環境設置

### GitHub Codespaces

你可以使用 GitHub Codespaces 虛擬運行這個範本。點擊按鈕會在你的瀏覽器中打開基於網頁的 VS Code 實例：

1. 打開範本（這可能需要幾分鐘）：

    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)

2. 打開一個終端窗口

### VS Code Dev Containers

⚠️ 這個選項僅在你的 Docker Desktop 分配了至少 16 GB 的 RAM 時才有效。如果你有少於 16 GB 的 RAM，可以嘗試 [GitHub Codespaces 選項](../../../../md/01.Introduce) 或 [本地設置](../../../../md/01.Introduce)。

另一個相關選項是 VS Code Dev Containers，這將使用 [Dev Containers 擴展](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 在你的本地 VS Code 中打開項目：

1. 啟動 Docker Desktop（如果尚未安裝，請先安裝）
2. 打開項目：

    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

3. 在打開的 VS Code 窗口中，當項目文件顯示出來後（這可能需要幾分鐘），打開一個終端窗口。
4. 繼續 [部署步驟](../../../../md/01.Introduce)

### 本地環境

1. 確保安裝了以下工具：

    * [Ollama](https://ollama.com/)
    * [Python 3.10+](https://www.python.org/downloads/)
    * [OpenAI Python SDK](https://pypi.org/project/openai/)

## 測試模型

1. 要求 Ollama 下載並運行 phi3:mini 模型：

    ```shell
    ollama run phi3:mini
    ```

    這將需要幾分鐘來下載模型。

2. 當你在輸出中看到 "success" 時，可以從提示符向該模型發送消息。

    ```shell
    >>> Write a haiku about hungry hippos
    ```

3. 幾秒鐘後，你應該會看到來自模型的響應流。

4. 要了解使用語言模型的不同技術，打開 Python 筆記本 [ollama.ipynb](../../../../code/01.Introduce/ollama.ipynb) 並運行每個單元格。如果你使用了 'phi3:mini' 以外的模型，請在第一個單元格中更改 `MODEL_NAME`。

5. 要從 Python 與 phi3:mini 模型進行對話，打開 Python 文件 [chat.py](../../../../code/01.Introduce/chat.py) 並運行它。你可以根據需要更改文件頂部的 `MODEL_NAME`，還可以修改系統消息或添加 few-shot 示例。

免责声明：此翻译由AI模型从原文翻译而来，可能不够完美。请审阅输出内容并进行必要的修正。