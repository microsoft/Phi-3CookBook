# 互動式 Phi 3 Mini 4K 指導聊天機器人與 Whisper

## 概述

互動式 Phi 3 Mini 4K 指導聊天機器人是一個工具，允許用戶使用文字或音頻輸入與 Microsoft Phi 3 Mini 4K 指導示範進行互動。這個聊天機器人可以用於多種任務，如翻譯、天氣更新和一般信息收集。

### 入門指南

要使用這個聊天機器人，請按照以下步驟操作：

1. 打開一個新的 [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. 在筆記本的主窗口中，你會看到一個聊天框界面，帶有一個文字輸入框和一個“發送”按鈕。
3. 要使用基於文字的聊天機器人，只需將你的消息輸入到文字輸入框中，然後點擊“發送”按鈕。聊天機器人會回應一個音頻文件，該文件可以直接在筆記本中播放。

**注意**：此工具需要 GPU 以及訪問 Microsoft Phi-3 和 OpenAI Whisper 模型，用於語音識別和翻譯。

### GPU 要求

要運行此示範，你需要 12GB 的 GPU 記憶體。

在 GPU 上運行 **Microsoft-Phi-3-Mini-4K instruct** 示範的記憶體需求將取決於幾個因素，例如輸入數據的大小（音頻或文字）、翻譯使用的語言、模型的速度以及 GPU 上的可用記憶體。

一般來說，Whisper 模型設計用於在 GPU 上運行。運行 Whisper 模型的推薦最低 GPU 記憶體量為 8 GB，但如果需要，它可以處理更大的記憶體量。

需要注意的是，在模型上運行大量數據或高量請求可能需要更多的 GPU 記憶體，並且可能會導致性能問題。建議使用不同的配置測試你的使用案例，並監控記憶體使用情況，以確定適合你特定需求的最佳設置。

## 互動式 Phi 3 Mini 4K 指導聊天機器人與 Whisper 的 E2E 範例

標題為 [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) 的 jupyter 筆記本演示了如何使用 Microsoft Phi 3 Mini 4K 指導示範從音頻或書面文字輸入生成文字。筆記本定義了幾個函數：

1. `tts_file_name(text)`: 這個函數基於輸入的文字生成一個文件名，用於保存生成的音頻文件。
1. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: 這個函數使用 Edge TTS API 從一個輸入文字塊列表生成音頻文件。輸入參數包括文字塊列表、語速、語音名稱和保存生成音頻文件的輸出路徑。
1. `talk(input_text)`: 這個函數使用 Edge TTS API 生成一個音頻文件，並將其保存到 /content/audio 目錄中的一個隨機文件名。輸入參數是要轉換為語音的輸入文字。
1. `run_text_prompt(message, chat_history)`: 這個函數使用 Microsoft Phi 3 Mini 4K 指導示範從消息輸入生成音頻文件，並將其附加到聊天記錄中。
1. `run_audio_prompt(audio, chat_history)`: 這個函數使用 Whisper 模型 API 將音頻文件轉換為文字，並將其傳遞給 `run_text_prompt()` 函數。
1. 代碼啟動了一個 Gradio 應用程序，允許用戶通過鍵入消息或上傳音頻文件與 Phi 3 Mini 4K 指導示範進行互動。輸出以文本消息的形式顯示在應用程序中。

## 故障排除

安裝 Cuda GPU 驅動

1. 確保你的 Linux 應用程序是最新的

    ```bash
    sudo apt update
    ```

1. 安裝 Cuda 驅動

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

1. 註冊 cuda 驅動位置

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

1. 檢查 Nvidia GPU 記憶體大小（需要 12GB 的 GPU 記憶體）

    ```bash
    nvidia-smi
    ```

1. 清空緩存：如果你使用 PyTorch，你可以調用 torch.cuda.empty_cache() 來釋放所有未使用的緩存記憶體，以便其他 GPU 應用程序使用

    ```python
    torch.cuda.empty_cache() 
    ```

1. 檢查 Nvidia Cuda

    ```bash
    nvcc --version
    ```

1. 執行以下任務以創建 Hugging Face token。

    - 瀏覽至 [Hugging Face Token Settings page](https://huggingface.co/settings/tokens)。
    - 選擇 **New token**。
    - 輸入你想使用的項目 **Name**。
    - 選擇 **Type** 為 **Write**。

> **Note**
>
> 如果你遇到以下錯誤：
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 要解決此問題，請在終端中輸入以下命令。
>
> ```bash
> sudo ldconfig
> ```

免责声明：此翻译由AI模型从原文翻译而来，可能不够完美。请检查输出内容并进行必要的修正。