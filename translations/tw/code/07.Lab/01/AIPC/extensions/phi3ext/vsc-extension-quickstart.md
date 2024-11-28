# 歡迎使用 VS Code 擴展

## 資料夾內容

* 這個資料夾包含了你的擴展所需的所有檔案。
* `package.json` - 這是聲明你的擴展和命令的清單檔案。
  * 範例插件註冊了一個命令並定義了它的標題和命令名稱。透過這些資訊，VS Code 可以在命令面板中顯示該命令。它還不需要載入插件。
* `src/extension.ts` - 這是你實現命令的主要檔案。
  * 該檔案匯出了一個函數，`activate`，這個函數會在你的擴展首次被啟動時被呼叫（在這個例子中是透過執行命令）。在 `activate` 函數中，我們呼叫了 `registerCommand`。
  * 我們將包含命令實現的函數作為第二個參數傳遞給 `registerCommand`。

## 設定

* 安裝推薦的擴展（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 和 dbaeumer.vscode-eslint）

## 立即開始使用

* 按 `F5` 開啟一個載入了你擴展的新視窗。
* 透過按下命令面板中的 (`Ctrl+Shift+P` 或 Mac 上的 `Cmd+Shift+P`) 並輸入 `Hello World` 來執行你的命令。
* 在 `src/extension.ts` 中設置斷點來除錯你的擴展。
* 在除錯主控台中找到你的擴展的輸出。

## 進行變更

* 在 `src/extension.ts` 中更改代碼後，你可以從除錯工具列重新啟動擴展。
* 你也可以重新載入 (`Ctrl+R` 或 Mac 上的 `Cmd+R`) VS Code 視窗來載入你的變更。

## 探索 API

* 你可以在開啟 `node_modules/@types/vscode/index.d.ts` 檔案時查看我們完整的 API 集合。

## 執行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 通過 **Tasks: Run Task** 命令執行 "watch" 任務。確保它在運行，否則測試可能無法被發現。
* 從活動欄中打開測試視圖並點擊 "Run Test" 按鈕，或使用快捷鍵 `Ctrl/Cmd + ; A`
* 在測試結果視圖中查看測試結果的輸出。
* 對 `src/test/extension.test.ts` 進行更改或在 `test` 資料夾中創建新的測試檔案。
  * 提供的測試運行器只會考慮符合名稱模式 `**.test.ts` 的檔案。
  * 你可以在 `test` 資料夾中創建資料夾以任何你想要的方式結構化你的測試。

## 更進一步

* 透過[捆綁你的擴展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo)來減少擴展大小並改善啟動時間。
* 在 VS Code 擴展市場上[發布你的擴展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo)。
* 透過設置[持續整合](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo)來自動化構建。

**免責聲明**:
本文檔已使用機器翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對使用此翻譯引起的任何誤解或誤釋不承擔責任。