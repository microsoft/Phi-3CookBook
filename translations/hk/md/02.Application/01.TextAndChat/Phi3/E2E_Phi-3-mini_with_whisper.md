# 互動式 Phi 3 Mini 4K 指令聊天機器人與 Whisper

## 概覽

互動式 Phi 3 Mini 4K 指令聊天機器人是一個工具，讓用戶可以使用文字或語音輸入與 Microsoft Phi 3 Mini 4K 指令示範進行互動。這個聊天機器人可用於多種任務，例如翻譯、天氣更新和一般資訊查詢。

### 快速開始

要使用這個聊天機器人，請按照以下步驟操作：

1. 開啟新的 [E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)。
2. 在 notebook 的主視窗中，你會看到一個聊天框介面，包含文字輸入框和一個「發送」按鈕。
3. 要使用基於文字的聊天機器人，只需在文字輸入框中輸入你的訊息，然後點擊「發送」按鈕。聊天機器人會回應一個可以直接在 notebook 中播放的音頻檔案。

**注意**：此工具需要 GPU，以及 Microsoft Phi-3 和 OpenAI Whisper 模型的存取，這些模型用於語音識別和翻譯。

### GPU 要求

運行此示範需要 12GB 的 GPU 記憶體。

運行 **Microsoft-Phi-3-Mini-4K 指令** 示範的 GPU 記憶體需求會取決於多種因素，例如輸入數據的大小（音頻或文字）、翻譯語言、模型的運行速度以及 GPU 的可用記憶體。

一般來說，Whisper 模型設計為在 GPU 上運行。建議的最低 GPU 記憶體為 8 GB，但如果需要，可以處理更大的記憶體量。

需要注意的是，運行大量數據或高頻率請求可能需要更多 GPU 記憶體，或者可能導致性能問題。建議根據你的使用案例測試不同的配置，並監控記憶體使用情況，以確定適合的設置。

## 互動式 Phi 3 Mini 4K 指令聊天機器人與 Whisper 的 E2E 範例

名為 [Interactive Phi 3 Mini 4K Instruct Chatbot with Whisper](https://github.com/microsoft/Phi-3CookBook/blob/main/code/06.E2E/E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb) 的 jupyter notebook 展示了如何使用 Microsoft Phi 3 Mini 4K 指令示範，通過音頻或文字輸入生成文字。該 notebook 定義了幾個函數：

1. `tts_file_name(text)`：此函數根據輸入文字生成一個檔名，用於保存生成的音頻檔案。
2. `edge_free_tts(chunks_list,speed,voice_name,save_path)`：此函數使用 Edge TTS API，從輸入文字塊的列表生成音頻檔案。輸入參數包括文字塊列表、語速、語音名稱以及保存生成音頻檔案的輸出路徑。
3. `talk(input_text)`：此函數使用 Edge TTS API 生成音頻檔案，並將其保存到 /content/audio 目錄中的隨機檔名。輸入參數是要轉換為語音的文字。
4. `run_text_prompt(message, chat_history)`：此函數使用 Microsoft Phi 3 Mini 4K 指令示範從訊息輸入生成音頻檔案，並將其附加到聊天歷史記錄中。
5. `run_audio_prompt(audio, chat_history)`：此函數使用 Whisper 模型 API 將音頻檔案轉換為文字，並將其傳遞給 `run_text_prompt()` 函數。
6. 程式碼啟動了一個 Gradio 應用程式，允許用戶通過輸入訊息或上傳音頻檔案與 Phi 3 Mini 4K 指令示範進行互動。輸出將以文字訊息的形式顯示在應用程式中。

## 疑難排解

安裝 Cuda GPU 驅動程式

1. 確保你的 Linux 應用程式已更新

    ```bash
    sudo apt update
    ```

2. 安裝 Cuda 驅動程式

    ```bash
    sudo apt install nvidia-cuda-toolkit
    ```

3. 註冊 Cuda 驅動程式位置

    ```bash
    echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
    ```

4. 檢查 Nvidia GPU 記憶體大小（需要 12GB 的 GPU 記憶體）

    ```bash
    nvidia-smi
    ```

5. 清空快取：如果你使用的是 PyTorch，可以呼叫 torch.cuda.empty_cache() 釋放所有未使用的快取記憶體，讓其他 GPU 應用程式使用。

    ```python
    torch.cuda.empty_cache() 
    ```

6. 檢查 Nvidia Cuda

    ```bash
    nvcc --version
    ```

7. 執行以下步驟來創建 Hugging Face token。

    - 前往 [Hugging Face Token 設定頁面](https://huggingface.co/settings/tokens?WT.mc_id=aiml-137032-kinfeylo)。
    - 選擇 **New token**。
    - 輸入你想使用的專案 **名稱**。
    - 將 **類型** 選為 **Write**。

> **注意**
>
> 如果你遇到以下錯誤：
>
> ```bash
> /sbin/ldconfig.real: Can't create temporary cache file /etc/ld.so.cache~: Permission denied 
> ```
>
> 解決方法：在終端中輸入以下指令。
>
> ```bash
> sudo ldconfig
> ```

**免責聲明**：  
本文件已使用機器翻譯人工智能服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀不承擔責任。