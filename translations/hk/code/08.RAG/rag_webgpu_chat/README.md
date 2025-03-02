Phi-3-mini WebGPU RAG 聊天機械人

## 用於展示 WebGPU 和 RAG 模式的演示
利用 Phi-3 Onnx 託管模型的 RAG 模式採用了檢索增強生成（Retrieval-Augmented Generation）的方法，結合了 Phi-3 模型的強大功能和 ONNX 託管，實現高效的 AI 部署。這個模式對於針對特定領域的任務進行模型微調非常有用，提供了質量、成本效益和長上下文理解的結合。它是 Azure AI 套件的一部分，提供多樣的模型選擇，方便用戶查找、試用和使用，滿足各行業的定制需求。Phi-3 模型，包括 Phi-3-mini、Phi-3-small 和 Phi-3-medium，可以在 Azure AI 模型目錄中找到，並可進行自我管理的微調和部署，或通過 HuggingFace 和 ONNX 平台進行部署，展示了微軟致力於提供便捷高效的 AI 解決方案的承諾。

## 什麼是 WebGPU
WebGPU 是一個現代的網頁圖形 API，旨在從網頁瀏覽器直接高效地訪問設備的圖形處理單元（GPU）。它被設計為 WebGL 的後繼者，並提供了幾個關鍵改進：

1. **與現代 GPU 的兼容性**：WebGPU 專為現代 GPU 架構設計，利用了系統 API，如 Vulkan、Metal 和 Direct3D 12。
2. **增強的性能**：它支持通用 GPU 計算和更快速的操作，適用於圖形渲染和機器學習任務。
3. **高級功能**：WebGPU 提供了對更高級 GPU 功能的訪問，支持更複雜和動態的圖形及計算工作負載。
4. **減少 JavaScript 工作負載**：通過將更多任務交由 GPU 處理，WebGPU 顯著減少了 JavaScript 的工作量，提升性能並提供更流暢的體驗。

目前，WebGPU 已在如 Google Chrome 等瀏覽器中得到支持，並且正在努力擴展到其他平台。

### 03.WebGPU
所需環境：

**支持的瀏覽器：**  
- Google Chrome 113+  
- Microsoft Edge 113+  
- Safari 18（macOS 15）  
- Firefox Nightly  

### 啟用 WebGPU：

- 在 Chrome/Microsoft Edge 中

啟用 `chrome://flags/#enable-unsafe-webgpu` 標誌。

#### 打開瀏覽器：
啟動 Google Chrome 或 Microsoft Edge。

#### 訪問標誌頁面：
在地址欄中輸入 `chrome://flags`，然後按 Enter。

#### 搜索標誌：
在頁面頂部的搜索框中輸入 'enable-unsafe-webgpu'。

#### 啟用標誌：
在結果列表中找到 #enable-unsafe-webgpu 標誌。

點擊旁邊的下拉菜單，選擇 Enabled。

#### 重啟瀏覽器：

啟用標誌後，需要重啟瀏覽器以使更改生效。點擊頁面底部出現的重新啟動按鈕。

- 對於 Linux，用 `--enable-features=Vulkan` 啟動瀏覽器。  
- Safari 18（macOS 15）默認啟用了 WebGPU。  
- 在 Firefox Nightly 中，進入地址欄輸入 about:config，然後 `set dom.webgpu.enabled to true`。

### 在 Microsoft Edge 上設置 GPU 

以下是在 Windows 上為 Microsoft Edge 設置高性能 GPU 的步驟：

- **打開設置：** 點擊開始菜單並選擇設置。  
- **系統設置：** 進入系統，然後選擇顯示。  
- **圖形設置：** 向下滾動並點擊圖形設置。  
- **選擇應用程序：** 在“選擇應用程序以設置首選項”下，選擇桌面應用程序，然後點擊瀏覽。  
- **選擇 Edge：** 導航到 Edge 的安裝文件夾（通常是 `C:\Program Files (x86)\Microsoft\Edge\Application`），然後選擇 `msedge.exe`。  
- **設置首選項：** 點擊選項，選擇高性能，然後點擊保存。  
這將確保 Microsoft Edge 使用您的高性能 GPU 以獲得更好的性能。  
- **重啟**您的計算機以使這些設置生效。

### 打開您的 Codespace：
導航到您的 GitHub 存儲庫。  
點擊 Code 按鈕，然後選擇 Open with Codespaces。

如果您尚未創建 Codespace，可以點擊 New codespace 來創建一個。

**注意** 在您的 Codespace 中安裝 Node 環境  
從 GitHub Codespace 運行 npm 演示是一個測試和開發項目的好方法。以下是幫助您入門的逐步指南：

### 設置您的環境：
一旦您的 Codespace 打開，確保您已安裝 Node.js 和 npm。您可以通過運行以下命令檢查：  
```
node -v
```  
```
npm -v
```  

如果尚未安裝，可以使用以下命令進行安裝：  
```
sudo apt-get update
```  
```
sudo apt-get install nodejs npm
```  

### 導航到您的項目目錄：
使用終端導航到您的 npm 項目所在的目錄：  
```
cd path/to/your/project
```  

### 安裝依賴項：
運行以下命令以安裝 package.json 文件中列出的所有必要依賴項：  

```
npm install
```  

### 運行演示：
安裝依賴項後，您可以運行您的演示腳本。這通常在 package.json 的 scripts 部分中指定。例如，如果您的演示腳本名為 start，您可以運行：  

```
npm run build
```  
```
npm run dev
```  

### 訪問演示：
如果您的演示涉及到一個網絡服務器，Codespaces 將提供一個 URL 供您訪問。請查看通知或檢查 Ports 標籤以找到 URL。

**注意：** 模型需要在瀏覽器中緩存，因此可能需要一些時間加載。

### RAG 演示
上傳 markdown 文件 `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### 選擇您的文件：
點擊“Choose File”按鈕選擇您要上傳的文檔。

### 上傳文檔：
選擇文件後，點擊“Upload”按鈕加載您的文檔以用於 RAG（檢索增強生成）。

### 開始聊天：
文檔上傳後，您可以根據文檔內容使用 RAG 開始聊天會話。

**免責聲明**:  
本文件是使用機器翻譯AI服務進行翻譯的。我們致力於確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解讀概不負責。