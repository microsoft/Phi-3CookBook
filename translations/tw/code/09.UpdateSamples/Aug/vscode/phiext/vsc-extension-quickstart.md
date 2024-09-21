# 歡迎使用你的 VS Code 擴展

## 資料夾內有什麼

* 這個資料夾包含了你的擴展所需的所有文件。
* `package.json` - 這是你聲明擴展和命令的清單文件。
  * 範例插件註冊了一個命令，並定義了它的標題和命令名稱。透過這些資訊，VS Code 可以在命令面板中顯示該命令。此時還不需要加載插件。
* `src/extension.ts` - 這是你實現命令的主要文件。
  * 這個文件匯出了一個函數 `activate`，這個函數會在你的擴展首次被啟動時（在這個例子中是通過執行命令）被調用。在 `activate` 函數內，我們調用了 `registerCommand`。
  * 我們將包含命令實現的函數作為第二個參數傳遞給 `registerCommand`。

## 設置

* 安裝推薦的擴展 (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, 和 dbaeumer.vscode-eslint)

## 立即開始

* 按 `F5` 打開一個加載了你擴展的新視窗。
* 在命令面板中執行你的命令，方法是按 (`Ctrl+Shift+P` 或 Mac 上的 `Cmd+Shift+P`)，然後輸入 `Hello World`。
* 在 `src/extension.ts` 中設置斷點以調試你的擴展。
* 在調試控制台中查看你的擴展的輸出。

## 進行更改

* 你可以在 `src/extension.ts` 中更改代碼後，從調試工具欄重新啟動擴展。
* 你也可以重新加載 (`Ctrl+R` 或 Mac 上的 `Cmd+R`) VS Code 視窗來加載你的更改。

## 探索 API

* 當你打開文件 `node_modules/@types/vscode/index.d.ts` 時，你可以查看我們完整的 API 集合。

## 運行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 通過 **Tasks: Run Task** 命令運行 "watch" 任務。確保它正在運行，否則可能無法發現測試。
* 從活動欄打開測試視圖，點擊 "Run Test" 按鈕，或使用快捷鍵 `Ctrl/Cmd + ; A`
* 在測試結果視圖中查看測試結果的輸出。
* 對 `src/test/extension.test.ts` 進行更改或在 `test` 資料夾內創建新的測試文件。
  * 提供的測試運行器只會考慮名稱模式匹配 `**.test.ts` 的文件。
  * 你可以在 `test` 資料夾內創建文件夾，以任何你想要的方式組織你的測試。

## 更進一步

* 通過 [打包你的擴展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) 來減少擴展大小並改善啟動時間。
* 在 VS Code 擴展市場上 [發布你的擴展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 通過設置 [持續集成](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) 自動化構建。

