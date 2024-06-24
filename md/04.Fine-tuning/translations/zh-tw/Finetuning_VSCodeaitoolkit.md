## 歡迎使用 VS Code 的 AI 工具包

[AI Toolkit for VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) 將來自 Azure AI Studio Catalog 和其他目錄（如 Hugging Face）的各種模型匯集在一起。該工具包通過以下方式簡化了使用生成式 AI 工具和模型建構 AI 應用程式的常見開發任務:

- 開始使用模型發現和 playground。
- 使用本地計算資源進行模型微調和推論。
- 使用 Azure 資源進行遠端微調和推論。

[安裝 AI Toolkit for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit 精調](../../../../imgs/04/00/Aitoolkit.png)

**[私人預覽]** 一鍵佈建 Azure Container Apps 以在雲端執行模型微調和推論。

現在讓我們進入你的 AI 應用程式開發:

- [Local Development](#local-development)
    - [Preparations](#preparations)
    - [Activate Conda](#activate-conda)
    - [Base model fine-tuning only](#base-model-fine-tuning-only)
    - [Model fine-tuning and inferencing](#model-fine-tuning-and-inferencing)
- [**[Private Preview]** Remote Development](#private-preview-remote-development)
    - [Prerequisites](#prerequisites)
    - [設定一個遠端開發專案](#setting-up-a-remote-development-project)
    - [Provision Azure Resources](#provision-azure-resources)
    - [（選擇性）將 Huggingface Token 添加到 Azure Container App Secret](#optional-add-huggingface-token-to-the-azure-container-app-secret)
    - [Run Fine-tuning](#run-fine-tuning)
    - [Provision Inference Endpoint](#provision-inference-endpoint)
    - [Deploy the Inference Endpoint](#deploy-the-inference-endpoint)
    - [Advanced usage](#advanced-usage)

## 本地開發

### 準備工作

1. 確保 NVIDIA 驅動程式已安裝在主機中。
2. 如果您使用 HF 來利用數據集，請執行 `huggingface-cli login`
3. `Olive` 鍵設定說明，用於修改記憶體使用的任何操作。

### 啟動 Conda

由於我們使用 WSL 環境並且是共享的，你需要手動啟動 conda 環境。完成此步驟後，你可以執行微調或推論。

```bash
conda activate [conda-env-name]
```

### 基礎模型微調僅限

要嘗試基礎模型而不進行微調，您可以在啟動 conda 後執行此命令。

```bash
cd inference

# Web browser 介面允許調整一些參數，如最大新 token 長度、溫度等。
# 使用者必須在 gradio 建立連接後手動在瀏覽器中打開連結（例如 http://0.0.0.0:7860）。
python gradio_chat.py --baseonly
```

### 模型微調和推論

一旦在開發容器中打開工作區，打開終端機（預設路徑是專案根目錄），然後執行以下命令來微調選定數據集上的 LLM。

```bash
python finetuning/invoke_olive.py
```

檢查點和最終模型將保存在 `models` 資料夾中。

接下來透過 `console`、`web browser` 或 `prompt flow` 中的聊天，使用微調後的模型進行推論。

```bash
cd inference

# Console 介面。
python console_chat.py

# 網頁瀏覽器介面允許調整一些參數，如最大新 token 長度、溫度等。
# 使用者必須在 gradio 建立連線後手動在瀏覽器中打開連結 (例如 http://127.0.0.1:7860)。
python gradio_chat.py
```

要在 VS Code 中使用 `prompt flow`，請參考這個 [快速開始](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html)。

### 模型微調

接下來，根據您的裝置上 GPU 的可用性下載以下模型。

要使用 QLoRA 啟動本地微調會話，請從我們的目錄中選擇您想要微調的模型。
| 平台 | 可用 GPU | 模型名稱 | 大小 (GB) |
|---------|---------|--------|--------|
| Windows | 是 | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | 是 | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | 否 | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_注意_** 你不需要 Azure 帳戶即可下載模型

Phi3-mini (int4) 模型大約是 2GB-3GB 的大小。根據您的網路速度，可能需要幾分鐘才能下載。

首先選擇專案名稱和位置。
接下來，從模型目錄中選擇一個模型。系統會提示您下載專案模板。然後，您可以點擊 "Configure Project" 來調整各種設定。

### Microsoft Olive

我們使用 [Olive](https://microsoft.github.io/Olive/overview/olive.html) 在我們目錄中的 PyTorch 模型上執行 QLoRA 微調。所有設定都預設為最佳化的預設值，以最佳化記憶體使用來在本地執行微調過程，但可以根據您的情況進行調整。

### 微調範例和資源

- [微調入門指南](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [使用 HuggingFace 資料集進行微調](https://github.com/microsoft/vscode-ai-toolkit/blob/main/walkthrough-hf-dataset.md)
- [使用簡單資料集進行微調](https://github.com/microsoft/vscode-ai-toolkit/blob/main/walkthrough-simple-dataset.md)

## **[Private Preview]** 遠端開發

### 先決條件

1. 要在遠端 Azure Container App 環境中執行模型微調，請確保您的訂閱有足夠的 GPU 容量。提交一個 [support ticket](https://azure.microsoft.com/support/create-ticket/) 來請求應用程式所需的容量。[獲取更多有關 GPU 容量的資訊](https://learn.microsoft.com/en-us/azure/container-apps/workload-profiles-overview)。
2. 如果您在 HuggingFace 上使用私人數據集，請確保您有一個 [HuggingFace account](https://huggingface.co/) 並 [generate an access token](https://huggingface.co/docs/hub/security-tokens)。
3. 在 VS Code 的 AI Toolkit 中啟用 Remote Fine-tuning and Inference 功能標誌
   1. 通過選擇 *File -> Preferences -> Settings* 打開 VS Code 設定。
   2. 導航到 *Extensions* 並選擇 *AI Toolkit*。
   3. 選擇 *"Enable Remote Fine-tuning And Inference"* 選項。
   4. 重新載入 VS Code 以生效。

- [Remote Fine tuning](https://github.com/microsoft/vscode-ai-toolkit/blob/main/remote-finetuning.md)

### 設定一個遠端開發專案

1. 執行命令面板 `AI Toolkit: Focus on Resource View`。
2. 導覽至 *Model Fine-tuning* 以訪問模型目錄。為您的專案指定一個名稱並選擇其在您機器上的位置。然後，點擊 *"Configure Project"* 按鈕。
3. 專案配置
    1. 避免啟用 *"Fine-tune locally"* 選項。
    2. Olive 配置設定將顯示預設值。請根據需要調整並填寫這些配置。
    3. 移動到 *Generate Project*。此階段利用 WSL 並涉及設定一個新的 Conda 環境，為包括 Dev Containers 在內的未來更新做準備。
4. 點擊 *"Relaunch Window In Workspace"* 以開啟您的遠端開發專案。

> **注意:** 該專案目前可以在本地或遠端的 AI Toolkit for VS Code 中運行。如果您在專案建立過程中選擇 *"本地微調"*，它將僅在 WSL 中運行，無法進行遠端開發。另一方面，如果您不啟用 *"本地微調"*，該專案將限制在遠端的 Azure Container App 環境中。

### 提供 Azure 資源

要開始，您需要為遠端微調配置 Azure 資源。請透過從命令面板執行 `AI Toolkit: Provision Azure Container Apps job for fine-tuning` 來完成此操作。

監控提供進度通過輸出通道中顯示的連結。

### [Optional] Add Huggingface Token to the Azure Container App Secret

如果你正在使用私有 HuggingFace 資料集，請將你的 HuggingFace token 設定為環境變數，以避免在 Hugging Face Hub 上需要手動登入。
你可以使用 `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning command` 來完成此操作。使用此命令，你可以將密鑰名稱設定為 [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) 並使用你的 Hugging Face token 作為密鑰值。

### 執行微調

要開始遠端微調工作，執行 `AI Toolkit: Run fine-tuning` 命令。

要查看系統和控制台日誌，您可以使用輸出面板中的連結訪問 Azure 入口網站（更多步驟請參見 [View and Query Logs on Azure](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)）。或者，您可以通過執行命令 `AI Toolkit: Show the running fine-tuning job streaming logs` 直接在 VSCode 輸出面板中查看控制台日誌。

> **注意:** 由於資源不足，工作可能會被佇列。如果日誌未顯示，執行 `AI Toolkit: Show the running fine-tuning job streaming logs` 命令，等待一會兒，然後再次執行該命令以重新連接到串流日誌。

在此過程中，QLoRA 將用於微調，並將建立 LoRA 適配器供模型在推論期間使用。微調的結果將存儲在 Azure Files 中。

### 提供推論端點

在遠端環境中訓練適配器後，使用一個簡單的 Gradio 應用程式與模型互動。
類似於微調過程，你需要透過執行命令面板中的 `AI Toolkit: Provision Azure Container Apps for inference` 來設定 Azure 資源以進行遠端推論。

預設情況下，用於推論的訂閱和資源群組應與用於微調的相匹配。推論將使用相同的 Azure Container App Environment 並訪問存儲在 Azure Files 中的模型和模型適配器，這些都是在微調步驟中生成的。

### 部署推論端點

如果你希望修改推論程式碼或重新載入推論模型，請執行 `AI Toolkit: Deploy for inference` 指令。這將同步你最新的程式碼與 Azure Container App 並重新啟動複製品。

一旦部署成功完成，您可以通過點擊 VSCode 通知中顯示的 "*Go to Inference Endpoint*" 按鈕來訪問推論 API。或者，可以在 `./infra/inference.config.json` 的 `ACA_APP_ENDPOINT` 和輸出面板中找到 Web API 端點。您現在可以使用此端點評估模型。

### 進階使用

如需有關使用 AI Toolkit 進行遠端開發的更多資訊，請參閱[遠端微調模型](https://aka.ms/ai-toolkit/remote-provision)和[使用微調模型進行推論](https://aka.ms/ai-toolkit/remote-inference)文件。

