# 歡迎使用您的 VS Code 擴展

## 資料夾內容

* 此資料夾包含您擴展所需的所有檔案。
* `package.json` - 這是宣告您的擴展和指令的清單檔案。
  * 範例插件註冊了一個指令並定義了它的標題和指令名稱。透過這些資訊，VS Code 可以在指令面板中顯示該指令。目前尚不需要載入插件。
* `src/extension.ts` - 這是您提供指令實作的主要檔案。
  * 此檔案匯出了一個函式 `activate`，該函式會在您的擴展首次被啟動時（例如執行該指令時）被呼叫。在 `activate` 函式內，我們呼叫了 `registerCommand`。
  * 我們將包含指令實作的函式作為第二個參數傳遞給 `registerCommand`。

## 設定

* 安裝推薦的擴展（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 和 dbaeumer.vscode-eslint）

## 立即啟動

* 按下 `F5` 開啟一個載入您擴展的新視窗。
* 在指令面板中按下 (`Ctrl+Shift+P` 或 `Cmd+Shift+P` 對於 Mac) 並輸入 `Hello World` 執行您的指令。
* 在 `src/extension.ts` 中設定中斷點以除錯您的擴展。
* 在除錯主控台中查看您的擴展輸出。

## 進行修改

* 修改 `src/extension.ts` 後，您可以從除錯工具列重新啟動擴展。
* 您也可以重新載入 (`Ctrl+R` 或 `Cmd+R` 對於 Mac) VS Code 視窗以載入您的變更。

## 探索 API

* 您可以在開啟檔案 `node_modules/@types/vscode/index.d.ts` 時，查看我們完整的 API 集合。

## 執行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 通過 **Tasks: Run Task** 指令執行 "watch" 任務。請確保此任務正在執行，否則可能無法偵測到測試。
* 從活動欄的 Testing 檢視中點擊 "Run Test" 按鈕，或者使用快捷鍵 `Ctrl/Cmd + ; A`。
* 在測試結果檢視中查看測試結果的輸出。
* 修改 `src/test/extension.test.ts` 或在 `test` 資料夾中新增測試檔案。
  * 提供的測試執行器只會考慮符合名稱模式 `**.test.ts` 的檔案。
  * 您可以在 `test` 資料夾中建立子資料夾，以任何您喜歡的方式組織測試。

## 更進一步

* 透過[打包您的擴展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) 減少擴展大小並提升啟動速度。
* 在 VS Code 擴展市集上[發佈您的擴展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 設置[持續整合](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) 自動化構建流程。

**免責聲明**：  
本文件使用基於機器的人工智能翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤讀不承擔責任。