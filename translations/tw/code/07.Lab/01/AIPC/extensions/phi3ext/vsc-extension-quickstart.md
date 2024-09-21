# 歡迎使用你的 VS Code 擴充功能

## 資料夾內容

* 這個資料夾包含了擴充功能所需的所有檔案。
* `package.json` - 這是宣告你的擴充功能和指令的描述檔。
  * 範例插件註冊了一個指令並定義了它的標題和指令名稱。有了這些資訊，VS Code 可以在指令選單中顯示該指令。此時還不需要載入插件。
* `src/extension.ts` - 這是你實現指令的主要檔案。
  * 該檔案匯出了一個函數 `activate`，這是在你的擴充功能首次被啟動時（在此情況下是透過執行指令）被呼叫的函數。在 `activate` 函數內，我們呼叫 `registerCommand`。
  * 我們將包含指令實現的函數作為第二個參數傳遞給 `registerCommand`。

## 設置

* 安裝推薦的擴充功能 (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, 和 dbaeumer.vscode-eslint)

## 馬上開始

* 按下 `F5` 以載入你的擴充功能並開啟一個新視窗。
* 在指令選單中按下 (`Ctrl+Shift+P` 或在 Mac 上按 `Cmd+Shift+P`)，並輸入 `Hello World` 執行你的指令。
* 在 `src/extension.ts` 檔案中設置斷點以調試你的擴充功能。
* 在除錯主控台中查看擴充功能的輸出。

## 進行修改

* 修改 `src/extension.ts` 中的程式碼後，可以從除錯工具列重新啟動擴充功能。
* 你也可以重新載入 (`Ctrl+R` 或在 Mac 上按 `Cmd+R`) VS Code 視窗來載入你的修改。

## 探索 API

* 你可以在打開 `node_modules/@types/vscode/index.d.ts` 檔案時查看我們完整的 API 集合。

## 執行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 通過 **Tasks: Run Task** 指令執行 "watch" 任務。確保它在執行中，否則可能無法發現測試。
* 從活動欄中打開測試視圖並點擊 "Run Test" 按鈕，或使用快捷鍵 `Ctrl/Cmd + ; A`
* 在測試結果視圖中查看測試結果的輸出。
* 修改 `src/test/extension.test.ts` 或在 `test` 資料夾中創建新的測試檔案。
  * 提供的測試運行器將只考慮名稱模式匹配 `**.test.ts` 的檔案。
  * 你可以在 `test` 資料夾中創建資料夾來以任何你想要的方式組織你的測試。

## 更進一步

* 通過[打包你的擴充功能](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo)來減少擴充功能大小並提高啟動時間。
* 在 VS Code 擴充功能市場上[發布你的擴充功能](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo)。
* 通過設置[持續整合](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo)來自動化構建。

免責聲明：本翻譯是由AI模型從原文翻譯而來，可能不完全準確。請檢查翻譯結果並進行必要的修改。