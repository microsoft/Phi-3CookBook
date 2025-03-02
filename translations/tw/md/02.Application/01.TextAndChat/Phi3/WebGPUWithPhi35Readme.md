# Phi-3.5-Instruct WebGPU RAG 聊天機器人

## 展示 WebGPU 和 RAG 模式的 Demo

使用 Phi-3.5 Onnx Hosted 模型的 RAG 模式採用了檢索增強生成 (Retrieval-Augmented Generation) 方法，結合 Phi-3.5 模型的強大能力與 ONNX 托管的高效 AI 部署方式。此模式在針對特定領域任務進行模型微調時非常關鍵，提供了高品質、成本效益以及長文本理解的平衡。這是 Azure AI 套件的一部分，提供多樣化的模型選擇，便於查找、試用與使用，滿足各行業的客製化需求。

## 什麼是 WebGPU
WebGPU 是一種現代化的網頁圖形 API，旨在直接從網頁瀏覽器高效訪問設備的圖形處理單元 (GPU)。它被設計為 WebGL 的後繼者，並帶來了幾個重要改進：

1. **與現代 GPU 的相容性**：WebGPU 專為當代 GPU 架構而設計，利用 Vulkan、Metal 和 Direct3D 12 等系統 API，實現無縫運行。
2. **性能提升**：支持通用 GPU 計算和更快速的操作，適用於圖形渲染和機器學習任務。
3. **進階功能**：WebGPU 提供對更多先進 GPU 功能的訪問，能夠處理更複雜和動態的圖形及計算工作負載。
4. **降低 JavaScript 負擔**：通過將更多任務交由 GPU 處理，WebGPU 顯著減輕了 JavaScript 的負擔，從而提升性能並帶來更流暢的體驗。

目前，WebGPU 已在 Google Chrome 等瀏覽器中提供支持，並正在努力擴展到其他平台。

### 03.WebGPU
所需環境：

**支持的瀏覽器：**
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly

### 啟用 WebGPU：

- 在 Chrome/Microsoft Edge 中

啟用 `chrome://flags/#enable-unsafe-webgpu` 標誌。

#### 打開您的瀏覽器：
啟動 Google Chrome 或 Microsoft Edge。

#### 訪問標誌頁面：
在地址欄中輸入 `chrome://flags` 並按下 Enter。

#### 搜尋標誌：
在頁面頂部的搜索框中輸入 'enable-unsafe-webgpu'。

#### 啟用標誌：
在搜索結果中找到 #enable-unsafe-webgpu 標誌。

點擊旁邊的下拉選單，選擇 Enabled。

#### 重啟瀏覽器：

啟用標誌後，您需要重啟瀏覽器以使更改生效。點擊頁面底部出現的 Relaunch 按鈕。

- 對於 Linux，用 `--enable-features=Vulkan` 啟動瀏覽器。
- Safari 18 (macOS 15) 預設已啟用 WebGPU。
- 在 Firefox Nightly 中，於地址欄輸入 about:config，然後 `set dom.webgpu.enabled to true`。

### 設定 Microsoft Edge 的 GPU 

以下是在 Windows 中為 Microsoft Edge 設置高性能 GPU 的步驟：

- **打開設定：** 點擊開始選單，選擇設定。
- **系統設定：** 進入系統，然後選擇顯示。
- **圖形設定：** 向下滾動並點擊圖形設定。
- **選擇應用：** 在“選擇應用來設置偏好”下，選擇桌面應用，然後點擊瀏覽。
- **選擇 Edge：** 導航到 Edge 的安裝資料夾（通常是 `C:\Program Files (x86)\Microsoft\Edge\Application`），然後選擇 `msedge.exe`。
- **設置偏好：** 點擊選項，選擇高性能，然後點擊保存。
這將確保 Microsoft Edge 使用您的高性能 GPU 以提升性能。
- **重啟**您的機器以使這些設置生效。

### 範例：請[點擊此鏈接](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**免責聲明**：  
本文件已使用基於機器的人工智能翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵信息，建議尋求專業的人工作翻譯。我們對使用此翻譯所引起的任何誤解或誤讀不承擔責任。