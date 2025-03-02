# Phi-3.5-Instruct WebGPU RAG Chatbot

## 示範展示 WebGPU 同 RAG 模式

RAG 模式結合咗 Phi-3.5 Onnx Hosted 模型，用 Retrieval-Augmented Generation 方法，將 Phi-3.5 模型嘅強大能力同 ONNX hosting 結合，提供高效嘅 AI 部署。呢個模式喺模型微調方面非常重要，特別係針對行業專屬任務，兼顧咗質量、成本效益同長文本理解能力。呢個模式係 Azure AI 套件嘅一部分，提供多款易於發現、試用同使用嘅模型，滿足唔同行業嘅自定化需求。

## 咩係 WebGPU 
WebGPU 係一個現代化嘅網頁圖形 API，設計用嚟直接喺網頁瀏覽器入面高效訪問設備嘅圖形處理單元 (GPU)。佢係 WebGL 嘅繼任者，提供以下幾個主要改進：

1. **兼容現代 GPU**：WebGPU 專為現代 GPU 架構設計，利用咗系統 API，例如 Vulkan、Metal 同 Direct3D 12。
2. **性能提升**：支持通用 GPU 計算同更快嘅操作，適合用於圖形渲染同機器學習任務。
3. **高級功能**：WebGPU 提供更高級嘅 GPU 功能，支持更複雜同動態嘅圖形同計算工作。
4. **減少 JavaScript 工作量**：透過將更多任務交俾 GPU 處理，WebGPU 大幅減少咗 JavaScript 嘅工作量，從而帶嚟更好嘅性能同更流暢嘅體驗。

WebGPU 而家已經喺 Google Chrome 等瀏覽器支持，並且仍然努力擴展到其他平台。

### 03.WebGPU
所需環境：

**支持嘅瀏覽器：**
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly

### 啟用 WebGPU:

- 喺 Chrome/Microsoft Edge 

啟用 `chrome://flags/#enable-unsafe-webgpu` 標誌。

#### 打開瀏覽器：
啟動 Google Chrome 或 Microsoft Edge。

#### 訪問 Flags 頁面：
喺地址欄輸入 `chrome://flags`，然後按 Enter。

#### 搜尋標誌：
喺頁面頂部嘅搜索框入面輸入 'enable-unsafe-webgpu'。

#### 啟用標誌：
喺結果列表入面搵到 #enable-unsafe-webgpu 標誌。

點擊旁邊嘅下拉菜單，選擇 Enabled。

#### 重新啟動瀏覽器：

啟用標誌之後，你需要重新啟動瀏覽器先可以生效。點擊頁面底部出現嘅 Relaunch 按鈕。

- 對於 Linux，用 `--enable-features=Vulkan` 啟動瀏覽器。
- Safari 18 (macOS 15) 預設啟用咗 WebGPU。
- 喺 Firefox Nightly，喺地址欄輸入 about:config，然後 `set dom.webgpu.enabled to true`。

### 喺 Microsoft Edge 設置 GPU 

以下係喺 Windows 上為 Microsoft Edge 設置高性能 GPU 嘅步驟：

- **打開設置：** 點擊開始菜單，選擇設置。
- **系統設置：** 進入系統，然後選擇顯示。
- **圖形設置：** 向下滾動，點擊圖形設置。
- **選擇應用：** 喺“選擇一個應用設置偏好”下，選擇桌面應用，然後點擊瀏覽。
- **選擇 Edge：** 瀏覽到 Edge 安裝文件夾（通常係 `C:\Program Files (x86)\Microsoft\Edge\Application`），然後選擇 `msedge.exe`。
- **設置偏好：** 點擊選項，選擇高性能，然後點擊保存。
咁樣可以確保 Microsoft Edge 使用你嘅高性能 GPU，從而獲得更好嘅性能。
- **重新啟動** 你嘅設備以使設置生效。

### 示例：請 [點擊呢條鏈接](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**免責聲明**：  
本文件經由機器翻譯AI服務進行翻譯。雖然我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件為最具權威性的版本。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀概不負責。