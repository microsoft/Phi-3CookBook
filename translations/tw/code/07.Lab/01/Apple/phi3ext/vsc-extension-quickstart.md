# 歡迎使用您的 VS Code 擴展

## 資料夾內容

* 此資料夾包含了擴展所需的所有檔案。
* `package.json` - 這是宣告您的擴展和命令的清單檔案。
  * 範例插件會註冊一個命令並定義其標題和命令名稱。根據這些資訊，VS Code 可以在命令面板中顯示該命令，但目前不需要載入插件。
* `src/extension.ts` - 這是主要檔案，您將在此實現命令的功能。
  * 該檔案匯出一個名為 `activate` 的函數，該函數會在您的擴展首次啟動時被呼叫（在此範例中是透過執行命令啟動）。在 `activate` 函數內，我們呼叫了 `registerCommand`。
  * 我們將包含命令實現的函數作為第二個參數傳遞給 `registerCommand`。

## 設置

* 安裝推薦的擴展 (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner 和 dbaeumer.vscode-eslint)

## 快速開始

* 按 `F5` 開啟一個載入您擴展的新視窗。
* 在命令面板中按下 (`Ctrl+Shift+P` 或 Mac 上的 `Cmd+Shift+P`) 並輸入 `Hello World` 來執行您的命令。
* 在 `src/extension.ts` 中的程式碼設置斷點以調試您的擴展。
* 在偵錯主控台中查看擴展的輸出。

## 進行修改

* 修改 `src/extension.ts` 中的程式碼後，您可以從偵錯工具列重新啟動擴展。
* 您也可以重新載入 (`Ctrl+R` 或 Mac 上的 `Cmd+R`) VS Code 視窗來載入您的修改。

## 探索 API

* 開啟檔案 `node_modules/@types/vscode/index.d.ts` 以查看我們完整的 API 集。

## 執行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 透過 **Tasks: Run Task** 指令執行 "watch" 任務。確保該任務正在執行，否則可能無法發現測試。
* 從活動列打開測試視圖，然後點擊 "Run Test" 按鈕，或者使用快捷鍵 `Ctrl/Cmd + ; A`。
* 在測試結果視圖中查看測試結果的輸出。
* 修改 `src/test/extension.test.ts` 或在 `test` 資料夾內建立新的測試檔案。
  * 提供的測試執行器僅會考慮名稱模式符合 `**.test.ts` 的檔案。
  * 您可以在 `test` 資料夾內建立子資料夾，以任何您喜歡的方式結構化測試。

## 深入探索

* [打包您的擴展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)，減少擴展大小並改善啟動時間。
* 在 VS Code 擴展市集中 [發佈您的擴展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 透過設置 [持續整合](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) 自動化構建流程。

**免責聲明**：  
本文件使用基於機器的人工智能翻譯服務進行翻譯。我們雖然力求準確，但請注意，自動翻譯可能會包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對於使用此翻譯而產生的任何誤解或誤讀概不負責。