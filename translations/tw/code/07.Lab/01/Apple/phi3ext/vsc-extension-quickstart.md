# 歡迎使用你的 VS Code 擴展

## 資料夾內有什麼

* 這個資料夾包含了你的擴展所需的所有檔案。
* `package.json` - 這是聲明你的擴展和命令的清單檔案。
  * 範例插件註冊了一個命令並定義了其標題和命令名稱。憑藉這些資訊，VS Code 可以在命令面板中顯示該命令。此時還不需要加載插件。
* `src/extension.ts` - 這是你實現命令的主要檔案。
  * 該檔案導出了一個函數 `activate`，該函數在你的擴展首次被激活時（在這種情況下是通過執行命令）被調用。在 `activate` 函數內，我們調用了 `registerCommand`。
  * 我們將包含命令實現的函數作為第二個參數傳遞給 `registerCommand`。

## 設置

* 安裝推薦的擴展 (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, 和 dbaeumer.vscode-eslint)

## 馬上開始

* 按 `F5` 打開一個載入了你的擴展的新窗口。
* 通過按 (`Ctrl+Shift+P` 或在 Mac 上按 `Cmd+Shift+P`) 並輸入 `Hello World` 從命令面板運行你的命令。
* 在 `src/extension.ts` 中設置斷點以調試你的擴展。
* 在調試控制台中找到來自你的擴展的輸出。

## 進行更改

* 在 `src/extension.ts` 中更改代碼後，可以從調試工具欄重新啟動擴展。
* 你也可以重新加載 (`Ctrl+R` 或在 Mac 上按 `Cmd+R`) VS Code 窗口以加載你的更改。

## 探索 API

* 當你打開檔案 `node_modules/@types/vscode/index.d.ts` 時，可以查看我們完整的 API 集。

## 運行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 通過 **Tasks: Run Task** 命令運行 "watch" 任務。確保它在運行，否則可能無法發現測試。
* 從活動欄中打開測試視圖並點擊 "Run Test" 按鈕，或者使用快捷鍵 `Ctrl/Cmd + ; A`
* 在測試結果視圖中查看測試結果的輸出。
* 對 `src/test/extension.test.ts` 進行更改或在 `test` 資料夾內創建新的測試檔案。
  * 提供的測試運行器只會考慮匹配名稱模式 `**.test.ts` 的檔案。
  * 你可以在 `test` 資料夾內創建資料夾來以任何你想要的方式結構化你的測試。

## 更進一步

* 通過 [打包你的擴展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) 減少擴展大小並提高啟動時間。
* 在 VS Code 擴展市場上 [發布你的擴展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 通過設置 [持續集成](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) 自動化構建。

免責聲明：此翻譯由AI模型從原文翻譯而來，可能不完全準確。請審核輸出並進行必要的修改。