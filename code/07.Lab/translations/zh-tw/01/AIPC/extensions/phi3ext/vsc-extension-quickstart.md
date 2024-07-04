# 歡迎使用你的 VS Code 擴充功能

## 資料夾裡有什麼

* 此資料夾包含所有擴充功能所需的檔案。
* `package.json` - 這是宣告擴充功能和命令的 manifest 檔案。
  * 範例插件註冊了一個命令並定義了其標題和命令名稱。憑藉這些資訊，VS Code 可以在命令面板中顯示該命令。它還不需要載入插件。
* `src/extension.ts` - 這是您將提供命令實作的主要檔案。
  * 該檔案匯出了一個函式，`activate`，這是在您的擴充功能首次被啟動時（在此情況下是透過執行命令）呼叫的。在 `activate` 函式內，我們呼叫 `registerCommand`。
  * 我們將包含命令實作的函式作為第二個參數傳遞給 `registerCommand`。

## 設定

* 安裝推薦的擴充功能 (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, 和 dbaeumer.vscode-eslint)

## Get up and running straight away

* 按下 `F5` 以開啟載入擴充功能的新視窗。
* 從命令面板執行你的命令，按下 (`Ctrl+Shift+P` 或在 Mac 上按 `Cmd+Shift+P`) 並輸入 `Hello World`。
* 在 `src/extension.ts` 中的程式碼設置斷點以除錯你的擴充功能。
* 在除錯主控台中找到你的擴充功能的輸出。

## 進行變更

* 你可以在變更 `src/extension.ts` 中的程式碼後，從偵錯工具列重新啟動擴充功能。
* 你也可以重新載入（在 Mac 上按 `Ctrl+R` 或 `Cmd+R`）VS Code 視窗以載入你的變更。

## 探索 API

* 你可以在打開檔案 `node_modules/@types/vscode/index.d.ts` 時開啟我們 API 的完整集合。

## 執行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.exteznsion-test-runner)
* 通過 **Tasks: Run Task** 命令執行 "watch" 任務。確保這個任務正在執行，否則可能無法發現測試。
* 從活動欄中打開測試視圖並點擊 "Run Test" 按鈕，或者使用快捷鍵 `Ctrl/Cmd + ; A`
* 在測試結果視圖中查看測試結果的輸出。
* 對 `src/test/extension.test.ts` 進行更改或在 `test` 資料夾內建立新的測試檔案。
  * 提供的測試執行器只會考慮符合名稱模式 `**.test.ts` 的檔案。
  * 你可以在 `test` 資料夾內建立資料夾，以任何你想要的方式結構化你的測試。

## 更進一步

* 通過[捆綁你的擴展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)來減少擴展大小並改善啟動時間。
* 在 VS Code 擴展市場上[發布你的擴展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 通過設定[持續整合](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)來自動化建構。
