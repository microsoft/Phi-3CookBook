# 歡迎使用你的 VS Code 擴展

## 資料夾內容

* 這個資料夾包含了你擴展所需的所有檔案。
* `package.json` - 這是宣告你的擴展和命令的清單檔案。
  * 範例插件註冊了一個命令，並定義了其標題和命令名稱。根據這些資訊，VS Code 可以在命令面板中顯示這個命令。此時還不需要載入插件。
* `src/extension.ts` - 這是你將實現命令的主要檔案。
  * 這個檔案匯出了一個函數，`activate`，這個函數在你的擴展第一次被啟動時（在這個例子中是執行命令時）被呼叫。在 `activate` 函數內，我們呼叫 `registerCommand`。
  * 我們將包含命令實現的函數作為第二個參數傳遞給 `registerCommand`。

## 設定

* 安裝推薦的擴展（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 和 dbaeumer.vscode-eslint）

## 立即啟動並運行

* 按下 `F5` 來開啟一個載入了你的擴展的新視窗。
* 透過按下 (`Ctrl+Shift+P` 或在 Mac 上按 `Cmd+Shift+P`) 並輸入 `Hello World` 從命令面板運行你的命令。
* 在 `src/extension.ts` 中設置斷點以調試你的擴展。
* 在調試控制台中查看你的擴展的輸出。

## 進行更改

* 在 `src/extension.ts` 中更改程式碼後，可以從調試工具列重新啟動擴展。
* 你也可以重新載入 (`Ctrl+R` 或在 Mac 上按 `Cmd+R`) VS Code 視窗來載入你的變更。

## 探索 API

* 當你打開 `node_modules/@types/vscode/index.d.ts` 檔案時，你可以看到我們完整的 API 集合。

## 運行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 通過 **Tasks: Run Task** 命令運行 "watch" 任務。確保它正在運行，否則可能無法發現測試。
* 從活動欄中打開測試視圖並點擊 "Run Test" 按鈕，或使用快捷鍵 `Ctrl/Cmd + ; A`
* 在測試結果視圖中查看測試結果的輸出。
* 對 `src/test/extension.test.ts` 進行更改或在 `test` 資料夾中創建新的測試檔案。
  * 提供的測試運行器只會考慮符合名稱模式 `**.test.ts` 的檔案。
  * 你可以在 `test` 資料夾中創建資料夾來以你想要的方式組織你的測試。

## 更進一步

* 透過 [打包你的擴展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) 來減少擴展大小並改善啟動時間。
* 在 VS Code 擴展市場上 [發布你的擴展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 通過設置 [持續整合](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) 來自動化構建。

**免責聲明**:
本文件使用機器翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對使用此翻譯而引起的任何誤解或誤釋不承擔責任。