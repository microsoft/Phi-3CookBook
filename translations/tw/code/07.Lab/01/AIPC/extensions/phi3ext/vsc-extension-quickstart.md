# 歡迎使用您的 VS Code 擴展

## 資料夾內容

* 此資料夾包含了您的擴展所需的所有檔案。
* `package.json` - 這是宣告您的擴展和命令的清單檔案。
  * 範例插件註冊了一個命令，並定義了它的標題和命令名稱。有了這些資訊，VS Code 可以在命令面板中顯示該命令。目前還不需要載入插件。
* `src/extension.ts` - 這是您實現命令的主要檔案。
  * 該檔案匯出了一個函式 `activate`，這是當您的擴展首次被啟用時（例如執行命令時）被呼叫的函式。在 `activate` 函式內，我們呼叫了 `registerCommand`。
  * 我們將包含命令實現的函式作為第二個參數傳遞給 `registerCommand`。

## 設置

* 安裝推薦的擴展（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 和 dbaeumer.vscode-eslint）

## 立即開始運行

* 按 `F5` 開啟一個載入了您的擴展的新視窗。
* 通過按下命令面板的快捷鍵 (`Ctrl+Shift+P` 或 Mac 上的 `Cmd+Shift+P`)，並輸入 `Hello World`，執行您的命令。
* 在 `src/extension.ts` 中的程式碼設置斷點，來除錯您的擴展。
* 在偵錯主控台中查看您的擴展的輸出。

## 進行修改

* 修改 `src/extension.ts` 中的程式碼後，可以從偵錯工具列重新啟動擴展。
* 您也可以重新載入 (`Ctrl+R` 或 Mac 上的 `Cmd+R`) VS Code 視窗以載入修改後的擴展。

## 探索 API

* 開啟檔案 `node_modules/@types/vscode/index.d.ts`，即可查看我們完整的 API。

## 執行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 通過 **Tasks: Run Task** 命令執行 "watch" 任務。確保此任務正在運行，否則可能無法發現測試。
* 從活動列中的測試視圖開啟，點擊 "Run Test" 按鈕，或使用快捷鍵 `Ctrl/Cmd + ; A`。
* 在測試結果視圖中查看測試結果的輸出。
* 修改 `src/test/extension.test.ts` 或在 `test` 資料夾中創建新的測試檔案。
  * 提供的測試執行器僅會考慮符合名稱模式 `**.test.ts` 的檔案。
  * 您可以在 `test` 資料夾內創建子資料夾，以任意方式組織您的測試。

## 深入探索

* 通過 [打包您的擴展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo) 減少擴展大小並提高啟動速度。
* 在 VS Code 擴展市場上 [發布您的擴展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo)。
* 通過設置 [持續整合](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo) 自動化構建流程。

**免責聲明**：  
本文件是使用基於機器的人工智能翻譯服務翻譯的。我們雖然努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用本翻譯而引起的任何誤解或誤讀不承擔責任。