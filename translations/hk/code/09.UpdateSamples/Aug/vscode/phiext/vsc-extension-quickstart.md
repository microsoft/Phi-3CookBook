# 歡迎使用你的 VS Code 擴展

## 資料夾內容

* 呢個資料夾包含咗你擴展所需嘅所有檔案。
* `package.json` - 呢個係宣告你擴展同指令嘅清單檔案。
  * 範例插件會註冊一個指令，並定義佢嘅標題同指令名稱。有咗呢啲資訊，VS Code 可以喺指令面板顯示呢個指令，但仲未需要載入插件。
* `src/extension.ts` - 呢個係你提供指令實現嘅主要檔案。
  * 呢個檔案會匯出一個函數 `activate`，呢個函數喺你嘅擴展第一次被啟動時（執行指令時）會被調用。喺 `activate` 函數入面，我哋會調用 `registerCommand`。
  * 我哋將包含指令實現嘅函數作為第二個參數傳畀 `registerCommand`。

## 設置

* 安裝推薦嘅擴展（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 同 dbaeumer.vscode-eslint）。

## 即刻開始使用

* 按 `F5` 打開一個已載入你擴展嘅新視窗。
* 喺指令面板執行你嘅指令，按 (`Ctrl+Shift+P` 或 Mac 上嘅 `Cmd+Shift+P`) 然後輸入 `Hello World`。
* 喺 `src/extension.ts` 裡面嘅代碼設置斷點，調試你嘅擴展。
* 喺調試控制台查看你擴展嘅輸出。

## 修改代碼

* 改咗 `src/extension.ts` 嘅代碼後，可以喺調試工具欄重新啟動擴展。
* 亦可以重載 (`Ctrl+R` 或 Mac 上嘅 `Cmd+R`) VS Code 視窗，重新載入你嘅更改。

## 探索 API

* 打開 `node_modules/@types/vscode/index.d.ts` 檔案，即可查看完整嘅 API 集合。

## 執行測試

* 安裝 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)。
* 通過 **Tasks: Run Task** 指令運行 "watch" 任務。確保任務已經運行，否則可能無法發現測試。
* 喺活動欄打開測試視圖，點擊 "Run Test" 按鈕，或者使用快捷鍵 `Ctrl/Cmd + ; A`。
* 喺測試結果視圖查看測試結果輸出。
* 修改 `src/test/extension.test.ts` 或喺 `test` 資料夾內創建新測試檔案。
  * 提供嘅測試運行器只會考慮名稱模式符合 `**.test.ts` 嘅檔案。
  * 你可以喺 `test` 資料夾內創建資料夾，隨意組織你嘅測試。

## 更進一步

* 通過 [打包擴展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) 減少擴展體積並提升啟動速度。
* 喺 VS Code 擴展市場 [發佈你嘅擴展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 通過設置 [持續集成](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) 自動化構建流程。

**免責聲明**：  
本文件使用機器翻譯AI服務進行翻譯。我們致力於追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵信息，建議尋求專業的人手翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解讀概不負責。