Phi-3-mini WebGPU RAG 聊天機器人

## WebGPU 和 RAG 模式展示
使用 Phi-3 Onnx Hosted 模型的 RAG 模式利用了檢索增強生成的方法，結合了 Phi-3 模型的力量和 ONNX 託管的高效 AI 部署。這種模式在調整模型以應對特定領域任務方面非常重要，提供了質量、成本效益和長上下文理解的混合。這是 Azure AI 套件的一部分，提供了易於查找、試用和使用的多種模型，滿足各行業的定制需求。Phi-3 模型，包括 Phi-3-mini、Phi-3-small 和 Phi-3-medium，都可以在 Azure AI 模型目錄中找到，可以自行管理進行微調和部署，也可以通過像 HuggingFace 和 ONNX 這樣的平台展示微軟對可訪問和高效 AI 解決方案的承諾。

## 什麼是 WebGPU 
WebGPU 是一個現代的網頁圖形 API，旨在提供直接從網頁瀏覽器訪問設備的圖形處理單元 (GPU) 的高效途徑。它是 WebGL 的繼任者，提供了幾個主要改進：

1. **兼容現代 GPU**：WebGPU 專為現代 GPU 架構設計，利用 Vulkan、Metal 和 Direct3D 12 等系統 API。
2. **增強性能**：它支持通用 GPU 計算和更快的操作，適合圖形渲染和機器學習任務。
3. **高級功能**：WebGPU 提供了更多高級 GPU 功能的訪問，支持更複雜和動態的圖形和計算工作負載。
4. **減少 JavaScript 工作量**：通過將更多任務卸載到 GPU，WebGPU 大大減少了 JavaScript 的工作量，提升了性能和流暢度。

目前，WebGPU 已在 Google Chrome 瀏覽器中支持，並正在擴展到其他平台。

### 03.WebGPU
所需環境：

**支持的瀏覽器：** 
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly.

### 啟用 WebGPU：

- 在 Chrome/Microsoft Edge 中

啟用 `chrome://flags/#enable-unsafe-webgpu` 標誌。

#### 打開瀏覽器：
啟動 Google Chrome 或 Microsoft Edge。

#### 訪問標誌頁面：
在地址欄中輸入 `chrome://flags` 並按下 Enter。

#### 搜索標誌：
在頁面頂部的搜索框中輸入 'enable-unsafe-webgpu'。

#### 啟用標誌：
在結果列表中找到 #enable-unsafe-webgpu 標誌。

點擊旁邊的下拉菜單並選擇 Enabled。

#### 重啟瀏覽器：

啟用標誌後，需要重啟瀏覽器以使更改生效。點擊頁面底部出現的 Relaunch 按鈕。

- 對於 Linux，用 `--enable-features=Vulkan` 啟動瀏覽器。
- Safari 18 (macOS 15) 默認啟用 WebGPU。
- 在 Firefox Nightly 中，輸入 about:config 在地址欄並 `set dom.webgpu.enabled to true`。

### 設置 GPU 以便在 Microsoft Edge 上使用

以下是設置高性能 GPU 以便在 Windows 上使用 Microsoft Edge 的步驟：

- **打開設置：** 點擊開始菜單並選擇設置。
- **系統設置：** 進入系統然後顯示。
- **圖形設置：** 向下滾動並點擊圖形設置。
- **選擇應用：** 在 “選擇一個應用來設置偏好” 下，選擇桌面應用然後瀏覽。
- **選擇 Edge：** 導航到 Edge 安裝文件夾（通常是 `C:\Program Files (x86)\Microsoft\Edge\Application`）並選擇 `msedge.exe`。
- **設置偏好：** 點擊選項，選擇高性能，然後點擊保存。
這將確保 Microsoft Edge 使用高性能 GPU 以獲得更好的性能。
- **重啟** 計算機以使這些設置生效。

### 打開你的 Codespace:
導航到你的 GitHub 存儲庫。
點擊代碼按鈕並選擇打開 Codespaces。

如果你還沒有 Codespace，可以點擊新建 codespace 創建一個。

**注意** 在你的 codespace 中安裝 Node 環境
從 GitHub Codespace 運行 npm demo 是測試和開發項目的好方法。以下是幫助你開始的步驟指南：

### 設置環境：
一旦打開 Codespace，確保你已經安裝了 Node.js 和 npm。你可以通過運行以下命令來檢查：
```
node -v
```
```
npm -v
```

如果沒有安裝，可以通過以下命令安裝：
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### 導航到你的項目目錄：
使用終端導航到 npm 項目所在的目錄：
```
cd path/to/your/project
```

### 安裝依賴：
運行以下命令來安裝 package.json 文件中列出的所有必要依賴：

```
npm install
```

### 運行 Demo：
一旦安裝了依賴項，可以運行 demo 腳本。這通常在 package.json 的 scripts 部分中指定。例如，如果你的 demo 腳本名為 start，可以運行：

```
npm run build
```
```
npm run dev
```

### 訪問 Demo：
如果你的 demo 涉及到 web 服務器，Codespaces 會提供一個 URL 來訪問它。查找通知或檢查 Ports 標籤來找到 URL。

**注意：** 模型需要在瀏覽器中緩存，因此可能需要一些時間來加載。

### RAG Demo
上傳 markdown 文件 `intro_rag.md` 來完成 RAG 解決方案。如果使用 codespaces，可以下載位於 `01.InferencePhi3/docs/` 的文件。

### 選擇你的文件：
點擊“選擇文件”按鈕來選擇你要上傳的文檔。

### 上傳文檔：
選擇文件後，點擊“上傳”按鈕來加載你的文檔以進行 RAG（檢索增強生成）。

### 開始聊天：
一旦文檔上傳完畢，可以根據文檔內容使用 RAG 開始聊天會話。

免責聲明：此翻譯由AI模型從原文翻譯而來，可能不完美。請審核輸出並進行任何必要的修正。