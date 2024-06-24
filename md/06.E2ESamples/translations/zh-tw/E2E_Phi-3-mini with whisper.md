## 互動式 Phi 3 Mini 4K 指導聊天機器人搭配 Whisper

### 簡介

The Interactive Phi 3 Mini 4K Instruct Chatbot 是一個工具，允許使用者使用文字或音訊輸入與 Microsoft Phi 3 Mini 4K instruct 展示互動。這個 chatbot 可以用於各種任務，例如翻譯、天氣更新和一般資訊收集。

### 入門指南

要使用此聊天機器人，只需按照以下說明進行操作:

1. 開啟一個新的 [Jupyter notebook 並執行提供的程式碼](E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)
2. 在 notebook 的主視窗中，你會看到一個具有文字輸入框和“Send”按鈕的聊天框介面。
3. 要使用基於文字的聊天機器人，只需將你的訊息輸入文字輸入框並點擊“Send”按鈕。聊天機器人會回應一個可以直接在 notebook 中播放的音訊檔案。

**注意**: 此工具需要 GPU 並存取 Microsoft Phi-3 和 OpenAI Whisper 模型，用於語音識別和翻譯。

### GPU Requirements

要執行此展示，你需要 12Gb 的 GPU 記憶體
在 GPU 上執行 Microsoft-Phi-3-Mini-4K instruct 展示的記憶體需求將取決於多種因素，例如輸入資料（音訊或文字）的大小、翻譯所使用的語言、模型的速度以及 GPU 上可用的記憶體。

一般來說，Whisper 模型設計為在 GPU 上執行。建議的最低 GPU 記憶體量為 8 GB，但如果需要，它可以處理更大的記憶體量。

請注意，對模型執行大量數據或高量請求可能需要更多的 GPU 記憶體和/或可能導致效能問題。建議使用不同配置測試您的使用案例，並監控記憶體使用情況，以確定適合您特定需求的最佳設定。

### Jupyter notebook，使用 Microsoft Phi 3 Mini 4K instruct Demo 從音訊或書面文字輸入生成文字。程式碼定義了幾個函式:

[E2E 範例 Phi-3 和 Whisper](E2E_Phi-3-mini-4k-instruct-Whispser_Demo.ipynb)

1. `tts_file_name(text)`: 此函式根據輸入的文字生成檔案名稱，用於保存生成的音訊檔案。
2. `edge_free_tts(chunks_list,speed,voice_name,save_path)`: 此函式使用 Edge TTS API 從一組輸入文字塊生成音訊檔案。輸入參數包括文字塊列表、語速、語音名稱和保存生成音訊檔案的輸出路徑。
3. `talk(input_text)`: 此函式使用 Edge TTS API 生成音訊檔案，並將其保存到 /content/audio 目錄中的隨機檔案名稱。輸入參數是要轉換為語音的輸入文字。
4. `run_text_prompt(message, chat_history)`: 此函式使用 Microsoft Phi 3 Mini 4K instruct 展示生成音訊檔案，並將其附加到聊天歷史中。輸入參數是訊息輸入和聊天歷史。
5. `run_audio_prompt(audio, chat_history)`: 此函式使用 Whisper 模型 API 將音訊檔案轉換為文字，並將其傳遞給 `run_text_prompt()` 函式。
6. 程式碼啟動了一個 Gradio 應用，允許使用者通過輸入訊息或上傳音訊檔案與 Phi 3 Mini 4K instruct 展示互動。輸出顯示為應用內的文字訊息。

### 疑難排解

安裝 Cuda GPU 驅動程式

1. 確保你的 Linux 應用程式是最新的

```bash
sudo apt update
```

2. 安裝 Cuda 驅動程式

```bash
sudo apt install nvidia-cuda-toolkit
```

3. 註冊 cuda 驅動程式位置

```bash
echo /usr/lib64-nvidia/ >/etc/ld.so.conf.d/libcuda.conf; ldconfig
```

4. 檢查 Nvidia GPU 記憶體大小 (需要 12GB 的 GPU 記憶體)

```bash
nvidia-smi
```

5. 清空快取: 如果你正在使用 PyTorch，你可以呼叫 torch.cuda.empty_cache() 來釋放所有未使用的快取記憶體，以便其他 GPU 應用程式可以使用。

```python
torch.cuda.empty_cache() 
```

6. 檢查 Nvidia Cuda

```bash 
nvcc --version
```

5. 建立一個 Hugging Face token

https://huggingface.co/settings/tokens
- Name = 專案名稱

- 類型 = 撰寫

6. 如果你遇到一個錯誤

```bash 
/sbin/ldconfig.real: 無法建立暫時快取檔案 /etc/ld.so.cache~: 權限被拒絕 
```

執行

```bash
sudo ldconfig
```

