Phi-3-mini WebGPU RAG 聊天機器人

## 展示 WebGPU 和 RAG 模式的 Demo
結合 Phi-3 Onnx Hosted 模型的 RAG 模式，採用了檢索增強生成（Retrieval-Augmented Generation）方法，將 Phi-3 模型的能力與 ONNX 託管相結合，以實現高效的 AI 部署。此模式在針對特定領域任務進行模型微調方面非常有用，提供了品質、成本效益以及長文本理解的平衡。它是 Azure AI 套件的一部分，提供一系列易於查找、試用和使用的模型，滿足各行業的定制需求。Phi-3 模型，包括 Phi-3-mini、Phi-3-small 和 Phi-3-medium，可在 Azure AI Model Catalog 上獲取，並能自我管理部署或通過 HuggingFace 和 ONNX 平台部署，展現了 Microsoft 對於可訪問且高效 AI 解決方案的承諾。

## 什麼是 WebGPU
WebGPU 是一種現代化的網頁圖形 API，旨在直接從網頁瀏覽器高效訪問設備的圖形處理單元（GPU）。它被設計為 WebGL 的繼任者，具有以下幾個主要改進：

1. **兼容現代 GPU**：WebGPU 專為當代 GPU 架構設計，利用 Vulkan、Metal 和 Direct3D 12 等系統 API 無縫運作。
2. **性能提升**：支持通用 GPU 計算和更快的操作，適合圖形渲染和機器學習任務。
3. **高級功能**：WebGPU 提供了更多高級 GPU 功能的訪問，支持更複雜和動態的圖形與計算工作負載。
4. **減少 JavaScript 工作量**：通過將更多任務卸載至 GPU，WebGPU 顯著減少了 JavaScript 的工作量，從而提升性能並帶來更流暢的體驗。

目前，WebGPU 已在 Google Chrome 等瀏覽器中支持，並正在努力擴展至其他平台。

### 03.WebGPU
所需環境：

**支持的瀏覽器：**
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18（macOS 15）
- Firefox Nightly。

### 啟用 WebGPU：

- 在 Chrome/Microsoft Edge 中 

啟用 `chrome://flags/#enable-unsafe-webgpu` 標誌。

#### 打開瀏覽器：
啟動 Google Chrome 或 Microsoft Edge。

#### 訪問標誌頁面：
在地址欄中輸入 `chrome://flags` 並按 Enter。

#### 搜索標誌：
在頁面頂部的搜索框中輸入 'enable-unsafe-webgpu'。

#### 啟用標誌：
在結果列表中找到 #enable-unsafe-webgpu 標誌。

點擊旁邊的下拉菜單，選擇 Enabled。

#### 重啟瀏覽器：

啟用標誌後，您需要重啟瀏覽器以使更改生效。點擊頁面底部出現的重新啟動按鈕。

- 對於 Linux，用 `--enable-features=Vulkan` 啟動瀏覽器。
- Safari 18（macOS 15）默認啟用了 WebGPU。
- 在 Firefox Nightly 中，輸入 about:config 至地址欄並 `set dom.webgpu.enabled to true`。

### 為 Microsoft Edge 設置 GPU 

以下是在 Windows 上為 Microsoft Edge 配置高性能 GPU 的步驟：

- **打開設置：** 點擊「開始」菜單並選擇「設置」。
- **系統設置：** 前往「系統」，然後選擇「顯示」。
- **圖形設置：** 向下滾動並點擊「圖形設置」。
- **選擇應用：** 在「選擇應用以設置首選項」下，選擇「桌面應用」，然後點擊「瀏覽」。
- **選擇 Edge：** 瀏覽到 Edge 的安裝文件夾（通常是 `C:\Program Files (x86)\Microsoft\Edge\Application`），然後選擇 `msedge.exe`。
- **設置首選項：** 點擊「選項」，選擇「高性能」，然後點擊「保存」。
這將確保 Microsoft Edge 使用您的高性能 GPU 以提升性能。
- **重啟**您的計算機以使這些設置生效。

### 打開您的 Codespace：
前往 GitHub 上的倉庫。
點擊「Code」按鈕並選擇「Open with Codespaces」。

如果您尚未創建 Codespace，可以點擊「New codespace」來創建。

**注意** 在您的 Codespace 中安裝 Node 環境
從 GitHub Codespace 運行 npm demo 是測試和開發項目的好方法。以下是逐步指南：

### 配置您的環境：
打開 Codespace 後，確保您已安裝 Node.js 和 npm。您可以通過運行以下命令檢查：
```
node -v
```
```
npm -v
```

如果未安裝，可以使用以下命令安裝：
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### 導航到您的項目目錄：
使用終端導航到 npm 項目所在的目錄：
```
cd path/to/your/project
```

### 安裝依賴項：
運行以下命令以安裝 package.json 文件中列出的所有必要依賴項：

```
npm install
```

### 運行 Demo：
依賴項安裝完成後，您可以運行 demo 腳本。這通常在 package.json 的 scripts 部分中指定。例如，如果您的 demo 腳本名為 start，可以運行：

```
npm run build
```
```
npm run dev
```

### 訪問 Demo：
如果您的 demo 涉及一個 web 服務器，Codespaces 將提供一個 URL 來訪問它。查找通知或檢查「Ports」標籤以找到 URL。

**注意：** 模型需要在瀏覽器中緩存，因此加載可能需要一些時間。

### RAG Demo
上傳 markdown 文件 `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### 選擇您的文件：
點擊「選擇文件」按鈕來選擇您想上傳的文檔。

### 上傳文檔：
選擇文件後，點擊「上傳」按鈕以加載文檔進行 RAG（檢索增強生成）。

### 開始聊天：
文檔上傳完成後，您可以基於文檔內容使用 RAG 開始聊天會話。

**免責聲明**:  
本文件使用基於機器的人工智慧翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤讀不承擔責任。