# 歡迎使用你的 VS Code 擴充功能

## 資料夾裡有什麼

* 這個資料夾包含了你的擴充功能所需的所有檔案。
* `package.json` - 這是聲明你的擴充功能和命令的清單檔案。
  * 範例插件註冊了一個命令並定義了其標題和命令名稱。透過這些資訊，VS Code 可以在命令面板中顯示該命令。目前還不需要載入插件。
* `src/extension.ts` - 這是主要檔案，你將在這裡實現你的命令。
  * 這個檔案匯出了一個函數 `activate`，當你的擴充功能第一次被啟動時（在這個例子中是執行命令時）會被呼叫。在 `activate` 函數內我們呼叫 `registerCommand`。
  * 我們將包含命令實現的函數作為第二個參數傳遞給 `registerCommand`。

## 設置

* 安裝推薦的擴充功能（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 和 dbaeumer.vscode-eslint）

## 立即開始使用

* 按 `F5` 來開啟一個載入了你的擴充功能的新視窗。
* 從命令面板中按下 (`Ctrl+Shift+P` 或在 Mac 上按 `Cmd+Shift+P`) 並輸入 `Hello World` 來執行你的命令。
* 在 `src/extension.ts` 中設置斷點來調試你的擴充功能。
* 在除錯主控台中找到你的擴充功能的輸出。

## 進行修改

* 修改 `src/extension.ts` 中的程式碼後，你可以從除錯工具列重新啟動擴充功能。
* 你也可以重新載入 (`Ctrl+R` 或在 Mac 上按 `Cmd+R`) VS Code 視窗來載入你的變更。

## 探索 API

* 你可以在開啟 `node_modules/@types/vscode/index.d.ts` 檔案時查看我們完整的 API 集合。

## 執行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 透過 **Tasks: Run Task** 命令執行 "watch" 任務。確保這個任務在運行，否則可能無法發現測試。
* 從活動欄中打開測試視圖並點擊 "Run Test" 按鈕，或使用快捷鍵 `Ctrl/Cmd + ; A`
* 在測試結果視圖中查看測試結果的輸出。
* 修改 `src/test/extension.test.ts` 或在 `test` 資料夾內創建新的測試檔案。
  * 提供的測試運行器只會考慮名稱模式匹配 `**.test.ts` 的檔案。
  * 你可以在 `test` 資料夾內創建資料夾以任何你想要的方式組織你的測試。

## 更進一步

* 透過 [打包你的擴充功能](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) 來減少擴充功能的大小並改善啟動時間。
* 在 VS Code 擴充功能市場上 [發佈你的擴充功能](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 透過設置 [持續整合](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) 來自動化構建。

**免責聲明**:
本文檔是使用機器翻譯服務翻譯的。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原語言的原始文件為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對使用此翻譯引起的任何誤解或誤釋不承擔任何責任。