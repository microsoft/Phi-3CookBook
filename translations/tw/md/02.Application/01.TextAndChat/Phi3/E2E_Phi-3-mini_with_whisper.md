# 互動式 Phi 3 Mini 4K 指令聊天機器人搭配 Whisper

## 概覽

互動式 Phi 3 Mini 4K 指令聊天機器人是一個工具，讓使用者能夠透過文字或語音輸入與 Microsoft Phi 3 Mini 4K 指令示範互動。此聊天機器人可用於各種任務，例如翻譯、天氣更新和一般資訊搜尋。

### 快速入門

要使用此聊天機器人，請按照以下步驟操作：

1. 開啟新的 [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. 在 notebook 的主視窗中，您會看到一個帶有文字輸入框和「發送」按鈕的聊天介面。
3. 若要使用文字型聊天機器人，只需將您的訊息輸入到文字輸入框中，然後點擊「發送」按鈕。聊天機器人將回傳一個可以直接在 notebook 中播放的音訊檔案。

**注意**：此工具需要 GPU 以及 Microsoft Phi-3 和 OpenAI Whisper 模型的存取權，這些模型用於語音識別和翻譯。

### GPU 要求

執行此示範需要 12GB 的 GPU 記憶體。

執行 **Microsoft-Phi-3-Mini-4K 指令**示範對 GPU 記憶體的需求取決於多種因素，例如輸入數據的大小（語音或文字）、翻譯使用的語言、模型的運行速度以及 GPU 的可用記憶體。

一般來說，Whisper 模型設計用於 GPU 上運行。執行 Whisper 模型的建議最低 GPU 記憶體為 8 GB，但如果需要，它也可以處理更大的記憶體。

需要注意的是，若在模型上處理大量數據或高頻率的請求，可能需要更多的 GPU 記憶體，並可能導致性能問題。建議根據不同配置測試您的使用案例，並監控記憶體使用情況，以確定最佳的設置。

## 互動式 Phi 3 Mini 4K 指令聊天機器人搭配 Whisper 的 E2E 範例

名為 [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) 的 jupyter notebook 展示了如何使用 Microsoft Phi 3 Mini 4K 指令示範，透過語音或文字輸入生成文字。此 notebook 定義了以下幾個函數：

1. `tts_file_name(text)`：此函數根據輸入文字生成檔案名稱，用於保存生成的音訊檔案。
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`：此函數使用 Edge TTS API 從輸入文字片段列表生成音訊檔案。輸入參數包括文字片段列表、語速、語音名稱以及保存音訊檔案的輸出路徑。
1. `talk(input_text)`：此函數使用 Edge TTS API 生成音訊檔案，並將其保存到 /content/audio 目錄中的隨機檔名。輸入參數為要轉換為語音的文字。
1. `run_text_prompt(message, chat_history)`：此函數使用 Microsoft Phi 3 Mini 4K 指令示範，根據訊息輸入生成音訊檔案，並將其附加到聊天記錄中。
1. `run_audio_prompt(audio, chat_history)`：此函數使用 Whisper 模型 API 將音訊檔案轉換為文字，並將其傳遞給 `run_text_prompt()` 函數。
1. 此程式碼啟動了一個 Gradio 應用，讓使用者可以透過輸入文字訊息或上傳音訊檔案與 Phi 3 Mini 4K 指令示範互動。輸出將以文字訊息的形式顯示在應用中。

## 疑難排解

安裝 Cuda GPU 驅動程式

1. 確保您的 Linux 應用程式已更新

    ```bash
    sudo apt update
    ```

1. 安裝 Cuda 驅動程式

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. 註冊 Cuda 驅動程式位置

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. 檢查 Nvidia GPU 記憶體大小（需要 12GB GPU 記憶體）

    ```bash
    nvidia-smi
    ```

1. 清空快取：如果您使用的是 PyTorch，可以呼叫 torch.cuda.empty_cache() 來釋放所有未使用的快取記憶體，以便其他 GPU 應用程式使用。

    ```python
    torch.cuda.empty_cache() 
    ```

1. 檢查 Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. 執行以下任務以建立 Hugging Face token。

    - 前往 [Hugging Face Token 設定頁面](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo)。
    - 選擇 **New token**。
    - 輸入您想使用的專案**名稱**。
    - 將 **Type** 設定為 **Write**。

> **注意**
>
> 如果您遇到以下錯誤：
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 為了解決此問題，請在終端機中輸入以下命令：
>
> ```bash
> sudo ldconfig
> ```

**免責聲明**：  
本文件使用機器翻譯人工智慧服務進行翻譯。我們雖然努力確保準確性，但請注意，自動翻譯可能會包含錯誤或不準確之處。應以原文檔的母語版本為最終權威來源。如涉及關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀概不負責。