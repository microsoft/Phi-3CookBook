# 歡迎使用你的 VS Code 擴展

## 文件夾內容

* 呢個文件夾包含咗所有你擴展所需嘅文件。
* `package.json` - 呢個係宣告你擴展同指令嘅 manifest 文件。
  * 呢個範例插件會註冊一個指令，並定義咗佢嘅標題同指令名稱。有咗呢啲資訊，VS Code 可以喺指令面板顯示呢個指令，但仲未需要載入插件。
* `src/extension.ts` - 呢個係你提供指令實現嘅主要文件。
  * 呢個文件會匯出一個函數 `activate`，當你嘅擴展第一次被啟動時（例如執行指令時）會執行呢個函數。喺 `activate` 函數入面，我哋會呼叫 `registerCommand`。
  * 我哋會將包含指令實現嘅函數作為第二個參數傳入 `registerCommand`。

## 設置

* 安裝推薦嘅擴展 (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, 同埋 dbaeumer.vscode-eslint)

## 即刻開始運行

* 按 `F5` 打開一個載入咗你擴展嘅新窗口。
* 喺指令面板執行你嘅指令，按 (`Ctrl+Shift+P` 或者 Mac 上按 `Cmd+Shift+P`) 並輸入 `Hello World`。
* 喺 `src/extension.ts` 裏面嘅代碼設置斷點，調試你嘅擴展。
* 喺調試控制台睇你擴展嘅輸出。

## 修改

* 修改 `src/extension.ts` 入面嘅代碼之後，可以喺調試工具欄重新啟動擴展。
* 亦可以重新載入 (`Ctrl+R` 或者 Mac 上按 `Cmd+R`) VS Code 窗口以載入你嘅更改。

## 探索 API

* 當你打開 `node_modules/@types/vscode/index.d.ts` 文件時，可以睇到我哋 API 嘅完整集合。

## 執行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 通過 **Tasks: Run Task** 指令運行 "watch" 任務。確保呢個任務係運行緊，否則可能搵唔到測試。
* 喺活動欄打開 Testing 視圖，點擊 "Run Test" 按鈕，或者使用快捷鍵 `Ctrl/Cmd + ; A`。
* 喺 Test Results 視圖睇測試結果嘅輸出。
* 修改 `src/test/extension.test.ts` 或者喺 `test` 文件夾內創建新測試文件。
  * 提供嘅測試運行器只會考慮文件名匹配 `**.test.ts` 嘅文件。
  * 你可以喺 `test` 文件夾內創建文件夾，以任何方式結構化你嘅測試。

## 更進一步

* 通過 [bundling your extension](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) 減少擴展大小並改進啟動時間。
* 喺 VS Code 擴展市場 [Publish your extension](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 通過設置 [Continuous Integration](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) 自動化構建流程。

**免責聲明**:  
本文件使用機器人工智能翻譯服務進行翻譯。雖然我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文的母語版本作為權威來源。對於關鍵信息，建議使用專業的人工作翻譯。我們對於使用此翻譯而引起的任何誤解或誤讀概不負責。