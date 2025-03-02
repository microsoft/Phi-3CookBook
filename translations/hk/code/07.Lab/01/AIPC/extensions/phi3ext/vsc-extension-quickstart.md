# 歡迎使用你的 VS Code 擴展

## 文件夾內有啲乜嘢

* 呢個文件夾包含咗你擴展所需嘅所有文件。
* `package.json` - 呢個係宣告你擴展同指令嘅清單文件。
  * 範例插件會註冊一個指令，並定義佢嘅標題同指令名稱。有咗呢啲資訊，VS Code 就可以喺指令面板中顯示該指令，但係暫時仲未需要載入插件。
* `src/extension.ts` - 呢個係主要文件，你會喺呢度實現你嘅指令。
  * 呢個文件會導出一個函數 `activate`，當你嘅擴展第一次被啟動時（例如執行指令時）會調用呢個函數。喺 `activate` 函數內，我哋會調用 `registerCommand`。
  * 我哋將包含指令實現嘅函數作為第二個參數傳遞俾 `registerCommand`。

## 設置

* 安裝推薦嘅擴展（amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, 同 dbaeumer.vscode-eslint）。

## 即刻上手

* 按 `F5` 打開一個載入咗你擴展嘅新窗口。
* 喺指令面板中執行你嘅指令，按 (`Ctrl+Shift+P` 或 Mac 上嘅 `Cmd+Shift+P`)，然後輸入 `Hello World`。
* 喺 `src/extension.ts` 裡面嘅代碼設置斷點，嚟調試你嘅擴展。
* 喺調試控制台中搵到你擴展嘅輸出。

## 進行更改

* 喺 `src/extension.ts` 裡面改代碼之後，可以喺調試工具欄重新啟動擴展。
* 你亦可以重載 (`Ctrl+R` 或 Mac 上嘅 `Cmd+R`) VS Code 窗口，嚟載入你嘅更改。

## 探索 API

* 你可以喺打開 `node_modules/@types/vscode/index.d.ts` 文件時查看我哋 API 嘅完整集合。

## 執行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 通過 **Tasks: Run Task** 命令運行 "watch" 任務。確保呢個任務係運行緊，否則測試可能唔會被發現。
* 喺活動欄中打開 Testing 視圖，然後點擊 "Run Test" 按鈕，或者使用快捷鍵 `Ctrl/Cmd + ; A`。
* 喺 Test Results 視圖中查看測試結果嘅輸出。
* 修改 `src/test/extension.test.ts` 或喺 `test` 文件夾中創建新嘅測試文件。
  * 提供嘅測試運行器只會考慮符合名稱模式 `**.test.ts` 嘅文件。
  * 你可以喺 `test` 文件夾中創建文件夾，按你嘅需要結構化測試。

## 更進一步

* [打包你嘅擴展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo)，減少擴展大小並提升啟動速度。
* 喺 VS Code 擴展市場上 [發佈你嘅擴展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo)。
* 通過設置 [持續集成](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo) 嚟自動化構建。

**免責聲明**:  
本文件使用機器人工智能翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解釋不承擔責任。