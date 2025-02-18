# Contributing

這個專案歡迎貢獻和建議。大多數的貢獻需要你同意一份
Contributor License Agreement (CLA)，聲明你有權利並且實際上授予我們使用你貢獻的權利。詳情請訪問 [https://cla.opensource.microsoft.com](https://cla.opensource.microsoft.com)

當你提交一個 pull request 時，CLA 機器人會自動判斷你是否需要提供 CLA，並適當地裝飾 PR（例如，狀態檢查，評論）。只需按照機器人提供的指示進行操作。你只需要在所有使用我們 CLA 的 repos 中做一次這個操作。

## 行為準則

這個專案採用了 [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)。
更多信息請閱讀 [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) 或聯繫 [opencode@microsoft.com](mailto:opencode@microsoft.com) 以獲取任何其他問題或評論。

## 建立問題時的注意事項

請不要為一般支援問題打開 GitHub 問題，因為 GitHub 列表應該用於功能請求和錯誤報告。這樣我們可以更容易地追蹤實際的問題或錯誤，並將一般討論與實際代碼分開。

## 如何貢獻

### Pull Requests 指南

在提交 Pull Request (PR) 到 Phi-3 CookBook 資源庫時，請遵循以下指南：

- **Fork 資源庫**：在進行修改之前，請始終 fork 資源庫到你自己的帳戶。

- **分開的 pull requests (PR)**：
  - 將每種類型的更改提交到自己的 pull request 中。例如，錯誤修復和文檔更新應該分別提交。
  - 錯字修正和小的文檔更新可以在適當的情況下合併到一個 PR 中。

- **處理合併衝突**：如果你的 pull request 顯示合併衝突，請更新你的本地 `main` 分支以反映主資源庫，然後再進行修改。

- **翻譯提交**：在提交翻譯 PR 時，確保翻譯文件夾包含原始文件夾中所有文件的翻譯。

### 翻譯指南

> [!IMPORTANT]
>
> 當翻譯這個資源庫中的文本時，請不要使用機器翻譯。只有在你精通的語言中志願翻譯。

如果你精通某種非英語語言，你可以幫助翻譯內容。請按照以下步驟確保你的翻譯貢獻被正確整合，請使用以下指南：

- **創建翻譯文件夾**：導航到相應的部分文件夾並為你貢獻的語言創建翻譯文件夾。例如：
  - 對於介紹部分：`Phi-3CookBook/md/01.Introduce/translations/<language_code>/`
  - 對於快速開始部分：`Phi-3CookBook/md/02.QuickStart/translations/<language_code>/`
  - 對於其他部分（例如 03.Inference，04.Finetuning 等）繼續這個模式

- **更新相對路徑**：在翻譯時，通過在 markdown 文件中的相對路徑開頭添加 `../../` 來調整文件夾結構，以確保鏈接正確工作。例如，改為以下：
  - 將 `(../../imgs/01/phi3aisafety.png)` 改為 `(../../../../imgs/01/phi3aisafety.png)`

- **組織你的翻譯**：每個翻譯文件應放置在相應部分的翻譯文件夾中。例如，如果你將介紹部分翻譯成西班牙語，你應該創建如下：
  - `Phi-3CookBook/md/01.Introduce/translations/es/`

- **提交完整的 PR**：確保一個部分的所有翻譯文件都包含在一個 PR 中。我們不接受部分翻譯。當提交翻譯 PR 時，請確保翻譯文件夾包含原始文件夾中所有文件的翻譯。

### 寫作指南

為了確保所有文件的一致性，請使用以下指南：

- **URL 格式**：將所有 URL 包裹在方括號內，後跟括號，不要在它們周圍或內部添加額外的空格。例如：`[example](https://example.com)`。

- **相對鏈接**：對指向當前目錄中的文件或文件夾的相對鏈接使用 `./`，對指向父目錄的相對鏈接使用 `../`。例如：`[example](../../path/to/file)` 或 `[example](../../../path/to/file)`。

- **非國家特定的地區**：確保你的鏈接不包含國家特定的地區。例如，避免使用 `/en-us/` 或 `/en/`。

- **圖像存儲**：將所有圖像存儲在 `./imgs` 文件夾中。

- **描述性的圖像名稱**：使用英文字母、數字和破折號來描述性地命名圖像。例如：`example-image.jpg`。

## GitHub 工作流程

當你提交一個 pull request 時，將觸發以下工作流程來驗證更改。請按照以下說明確保你的 pull request 通過工作流程檢查：

- [檢查斷開的相對路徑](../..)
- [檢查 URL 沒有地區](../..)

### 檢查斷開的相對路徑

這個工作流程確保你文件中的所有相對路徑都是正確的。

1. 為了確保你的鏈接正常工作，使用 VS Code 執行以下任務：
    - 懸停在文件中的任何鏈接上。
    - 按 **Ctrl + 點擊** 來導航到鏈接。
    - 如果你點擊鏈接並且它在本地無法工作，它將觸發工作流程並且在 GitHub 上也無法工作。

1. 為了解決這個問題，使用 VS Code 提供的路徑建議執行以下任務：
    - 輸入 `./` 或 `../`。
    - VS Code 會根據你輸入的內容提示你選擇可用的選項。
    - 通過點擊所需的文件或文件夾來確保你的路徑是正確的。

一旦你添加了正確的相對路徑，保存並推送你的更改。

### 檢查 URL 沒有地區

這個工作流程確保任何 web URL 不包含國家特定的地區。由於這個資源庫是全球可訪問的，確保 URL 不包含你的國家地區是很重要的。

1. 為了驗證你的 URL 沒有國家地區，執行以下任務：

    - 檢查 URL 中是否有 `/en-us/`，`/en/` 或任何其他語言地區的文本。
    - 如果這些文本不在你的 URL 中，那麼你將通過這個檢查。

1. 為了解決這個問題，執行以下任務：
    - 打開工作流程突出顯示的文件路徑。
    - 從 URL 中刪除國家地區。

一旦你刪除了國家地區，保存並推送你的更改。

### 檢查斷開的 URL

這個工作流程確保你文件中的任何 web URL 都能正常工作並返回 200 狀態碼。

1. 為了驗證你的 URL 是否正確工作，執行以下任務：
    - 檢查你文件中的 URL 狀態。

2. 為了解決任何斷開的 URL，執行以下任務：
    - 打開包含斷開 URL 的文件。
    - 更新 URL 為正確的 URL。

一旦你修復了 URL，保存並推送你的更改。

> [!NOTE]
>
> 可能會有一些情況，即使鏈接是可訪問的，URL 檢查也會失敗。這可能發生在以下幾種情況下：
>
> - **網絡限制**：GitHub actions 服務器可能有網絡限制，無法訪問某些 URL。
> - **超時問題**：響應時間過長的 URL 可能會在工作流程中觸發超時錯誤。
> - **臨時服務器問題**：偶爾的服務器停機或維護可能會使 URL 在驗證期間暫時無法使用。

**免責聲明**：
本文檔是使用基於機器的人工智能翻譯服務進行翻譯的。儘管我們力求準確，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原語言的原始文件為權威來源。對於關鍵信息，建議使用專業的人類翻譯。我們對因使用此翻譯而引起的任何誤解或誤讀不承擔責任。