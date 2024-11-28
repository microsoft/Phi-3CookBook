# Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper

## 概述

Interactive Phi 3 Mini 4K Instruct Chatbot 是一個工具，讓用戶可以使用文字或語音輸入與 Microsoft Phi 3 Mini 4K instruct demo 互動。這個聊天機器人可以用於多種任務，如翻譯、天氣更新和一般信息收集。

### 開始使用

要使用這個聊天機器人，只需按照以下步驟操作：

1. 打開一個新的 [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. 在筆記本的主窗口中，你會看到一個帶有文本輸入框和“發送”按鈕的聊天框界面。
3. 要使用基於文本的聊天機器人，只需在文本輸入框中輸入你的消息，然後點擊“發送”按鈕。聊天機器人會回應一個可以直接在筆記本中播放的音頻文件。

**注意**：此工具需要 GPU 和訪問 Microsoft Phi-3 和 OpenAI Whisper 模型，這些模型用於語音識別和翻譯。

### GPU 要求

要運行這個演示，你需要 12GB 的 GPU 記憶體。

在 GPU 上運行 **Microsoft-Phi-3-Mini-4K instruct** 演示的記憶體需求將取決於多種因素，例如輸入數據（音頻或文本）的大小、翻譯所用的語言、模型的速度和 GPU 上的可用記憶體。

一般來說，Whisper 模型是設計在 GPU 上運行的。運行 Whisper 模型的推薦最低 GPU 記憶體量是 8 GB，但如果需要，它可以處理更大的記憶體量。

重要的是，要注意在模型上運行大量數據或高量請求可能需要更多的 GPU 記憶體和/或可能引起性能問題。建議使用不同的配置測試你的用例，並監控記憶體使用情況，以確定適合你具體需求的最佳設置。

## 使用 Whisper 的 Interactive Phi 3 Mini 4K Instruct Chatbot 的端到端示例

標題為 [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) 的 Jupyter 筆記本演示了如何使用 Microsoft Phi 3 Mini 4K instruct Demo 從音頻或書面文本輸入生成文本。筆記本定義了幾個函數：

1. `tts_file_name(text)`：此函數根據輸入文本生成一個文件名，用於保存生成的音頻文件。
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`：此函數使用 Edge TTS API 從一系列輸入文本塊生成音頻文件。輸入參數包括文本塊列表、語速、語音名稱和保存生成音頻文件的輸出路徑。
1. `talk(input_text)`：此函數使用 Edge TTS API 生成音頻文件，並將其保存到 /content/audio 目錄中的隨機文件名。輸入參數是要轉換為語音的輸入文本。
1. `run_text_prompt(message, chat_history)`：此函數使用 Microsoft Phi 3 Mini 4K instruct demo 從消息輸入生成音頻文件，並將其附加到聊天記錄中。
1. `run_audio_prompt(audio, chat_history)`：此函數使用 Whisper 模型 API 將音頻文件轉換為文本，並將其傳遞給 `run_text_prompt()` 函數。
1. 代碼啟動了一個 Gradio 應用，允許用戶通過輸入消息或上傳音頻文件與 Phi 3 Mini 4K instruct demo 互動。輸出以文本消息的形式顯示在應用中。

## 疑難解答

安裝 Cuda GPU 驅動程序

1. 確保你的 Linux 應用程序是最新的

    ```bash
    sudo apt update
    ```

1. 安裝 Cuda 驅動程序

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. 註冊 cuda 驅動程序位置

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. 檢查 Nvidia GPU 記憶體大小（需要 12GB 的 GPU 記憶體）

    ```bash
    nvidia-smi
    ```

1. 清空緩存：如果你使用的是 PyTorch，可以調用 torch.cuda.empty_cache() 來釋放所有未使用的緩存記憶體，以便其他 GPU 應用程序使用

    ```python
    torch.cuda.empty_cache() 
    ```

1. 檢查 Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. 執行以下任務以創建 Hugging Face 令牌。

    - 導航到 [Hugging Face Token Settings page](https://huggingface.co/settings/tokens)。
    - 選擇 **New token**。
    - 輸入你想使用的項目 **Name**。
    - 將 **Type** 設置為 **Write**。

> **注意**
>
> 如果你遇到以下錯誤：
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 要解決此問題，請在終端內鍵入以下命令。
>
> ```bash
> sudo ldconfig
> ```

**免責聲明**: 
本文件是使用基於機器的人工智能翻譯服務翻譯的。我們雖然努力追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原語言的原始文件為權威來源。對於關鍵信息，建議進行專業人工翻譯。我們對使用本翻譯所產生的任何誤解或誤讀不承擔責任。