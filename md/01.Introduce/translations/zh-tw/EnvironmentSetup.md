## 開啟專案

我們已經提供了一個 Ollama Python Playground

這個專案被設計為在 GitHub Codespaces 中開啟，作為任何人都可以完全在瀏覽器中嘗試 SLMs（小型語言模型）的一種簡單方式。

1. 使用倉庫頂部的 `Code` 按鈕在瀏覽器中打開 Codespace。
2. 一旦 Codespace 加載完成，它應該有 [ollama](https://ollama.com/)。
3. 讓 Ollama 執行你選擇的 SLM。例如，要執行 [phi3](https://ollama.com/library/phi3) 模型：

    ```shell
    ollama run phi3:mini
    ```

    這將需要幾分鐘的時間將模型下載到 Codespace。
4. 當你在輸出中看到 "success" 時，你可以從提示中向該模型發送消息。

    ```shell
    >>> Write a haiku about hungry hippos
    ```

5. 幾秒鐘後，你應該會看到來自模型的響應流。
6. 要了解語言模型使用的不同技術，打開 Python 筆記本 `ollama.ipynb` 並執行每個單元格。如果你使用了 'phi3:mini' 以外的模型，請更改第一個單元格中的 `MODEL_NAME`。
7. 要從 Python 與模型進行對話，打開 Python 文件 `chat.py` 並執行它。你可以根據需要更改文件頂部的 `MODEL_NAME`，還可以修改系統消息或添加少量範例。

你有幾個選項可以開始使用這個模板。最快的方式是使用 GitHub Codespaces，因為它會為你設定所有工具，但你也可以[在本地環境設定](#local-environment)。

### GitHub Codespaces

您可以使用 GitHub Codespaces 虛擬執行此模板。該按鈕將在您的瀏覽器中打開一個基於網頁的 VS Code 實例:

1. 開啟範本 (這可能需要幾分鐘):

    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)

2. 打開一個終端視窗
3. 繼續進行[部署步驟](#deployment)。

### VS Code Dev Containers

一個相關的選項是 VS Code Dev Containers，它將使用 [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) 在本地 VS Code 中打開專案:

1. 啟動 Docker Desktop (如果尚未安裝，請安裝)
2. 打開專案:

    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

3. 在打開的 VS Code 視窗中，當專案檔案顯示出來時（這可能需要幾分鐘），打開一個終端視窗。
4. 繼續進行[部署步驟](#deployment)。

### 本地環境

1. 確保已安裝以下工具:

    * [Python 3.10+](https://www.python.org/downloads/)
    * [Docker Desktop](https://www.docker.com/products/docker-desktop/)
    * [Git](https://git-scm.com/downloads)
    * [OpenAI Python SDK](https://pypi.org/project/openai/)

2. 打開專案資料夾

3. 安裝 OpenAI Python 函式庫:

    ```shell
    pip install openai
    ```

