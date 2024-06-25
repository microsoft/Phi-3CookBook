# **建構你自己的 Visual Studio Code GitHub Copilot Chat 與 Microsoft Phi-3 Family**

你是否在 GitHub Copilot Chat 中使用過工作區代理？你想要建構自己的團隊程式碼代理嗎？這個實作實驗室希望結合開放原始碼模型來建構企業級程式碼業務代理。

## **Foundation**

### **為什麼選擇 Microsoft Phi-3**

Phi-3 是一個系列家族，包括 phi-3-mini、phi-3-small 和 phi-3-medium，基於不同的訓練參數，用於文本生成、對話完成和程式碼產生器。還有基於 Vision 的 phi-3-vision。它適合企業或不同團隊建立離線生成式 AI 解決方案。

推薦閱讀此連結 [https://github.com/microsoft/Phi-3CookBook/blob/main/md/01.Introduce/Phi3Family.md](https://github.com/microsoft/Phi-3CookBook/blob/main/md/01.Introduce/Phi3Family.md)。

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat 擴充功能提供了一個聊天介面，讓你可以與 GitHub Copilot 互動，並直接在 VS Code 中接收與程式碼相關問題的答案，而無需瀏覽文件或搜尋線上論壇。

Copilot Chat 可能會使用語法高亮、縮排和其他格式化功能來增加生成回應的清晰度。根據用戶問題的類型，結果可能包含 Copilot 用於生成回應的上下文連結，例如原始程式碼檔案或文件，或是用於訪問 VS Code 功能的按鈕。

- Copilot Chat 整合到你的開發流程中，並在你需要的地方提供協助：

- 直接從編輯器或終端啟動內聯聊天對話，以在編寫程式碼時獲得幫助

- 使用 Chat 視圖在旁邊擁有一個 AI 助手，隨時為你提供幫助

- 啟動 Quick Chat 以快速提問並回到你正在做的事情

你可以在各種情境中使用 GitHub Copilot Chat，例如:

- 解答有關如何最佳解決問題的程式碼問題

- 解釋他人的程式碼並提出改進建議

- 提出程式碼修正建議

- 產生單元測試案例

- 產生程式碼文件

建議閱讀此連結 [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat)。

###  **Microsoft GitHub Copilot Chat @workspace**

參考 **@workspace** 在 Copilot Chat 中讓你可以詢問有關整個程式碼庫的問題。根據問題，Copilot 智能地檢索相關的檔案和符號，然後在其答案中以連結和程式碼範例的形式引用。

為了回答你的問題，**@workspace** 會搜尋開發者在 VS Code 中瀏覽程式碼庫時會使用的相同來源:

- 工作區中的所有檔案，除了被 .gitignore 檔案忽略的檔案

- 具有嵌套資料夾和檔案名稱的目錄結構

- GitHub 的程式碼搜尋索引，如果工作區是 GitHub 儲存庫並且被程式碼搜尋索引

- 工作區中的符號和定義

- 當前選定的文字或在活動編輯器中可見的文字

注意: .gitignore 會被忽略，如果你有一個文件開啟或在被忽略的文件中選擇了文字。

推薦閱讀此連結 [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context)。

## **了解更多關於這個實驗室**

GitHub Copilot 大大提高了企業的程式設計效率，每個企業都希望自訂 GitHub Copilot 的相關功能。許多企業根據自己的業務場景和開放原始碼模型，定制了類似 GitHub Copilot 的擴展。對於企業來說，自訂的擴展更容易控制，但這也影響了使用者體驗。畢竟，GitHub Copilot 在處理一般場景和專業性方面具有更強的功能。如果能保持一致的體驗，並自訂企業自己的擴展會更好。GitHub Copilot Chat 提供了相關的 API 供企業在 Chat 體驗中擴展。保持一致的體驗並擁有自訂功能是更好的使用者體驗。

這個實驗室主要使用 Phi-3 模型結合本地 NPU 和 Azure 混合來建構一個自訂的 Agent 在 GitHub Copilot Chat ***@PHI3*** 中，以協助企業開發人員完成程式碼產生***(@PHI3 /gen)***並根據圖像生成程式碼***(@PHI3 /img)***。

![PHI3](../../../../../imgs/07/01/cover.png)

### ***注意:***

此實驗室目前在 Intel CPU 和 Apple Silicon 的 AIPC 中實現。我們將繼續更新 Qualcomm 版本的 NPU。

## **Lab**

 Name | Description | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - Installations(✅) | 設定和安裝相關環境和安裝工具 | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Run Prompt flow with Phi-3-mini (✅) | 結合 AIPC / Apple Silicon，使用本地 NPU 通過 Phi-3-mini 建立程式碼產生器 | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Deploy Phi-3-vision on Azure Machine Learning Service(✅) | 通過部署 Azure Machine Learning Service 的 Model Catalog - Phi-3-vision 影像生成程式碼 | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - Create a @phi-3 agent in GitHub Copilot Chat(✅)  | 在 GitHub Copilot Chat 中建立自訂 Phi-3 agent 以完成程式碼產生、圖形生成程式碼、RAG 等 | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| Sample Code (✅)  | 下載範例程式碼 | [Go](../../../../../code/07.Lab/01/AIPC/) | [Go](../../../../../code/07.Lab/01/Apple/)

## **資源**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. 了解更多關於 GitHub Copilot 的資訊 [https://learn.microsoft.com/en-us/training/paths/copilot/](https://learn.microsoft.com/en-us/training/paths/copilot/)

3. 了解更多關於 GitHub Copilot Chat 的資訊 [https://learn.microsoft.com/en-us/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/en-us/training/paths/accelerate-app-development-using-github-copilot/)

4. 了解更多關於 GitHub Copilot Chat API 的資訊 [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat)

5. 了解更多關於 Azure AI Studio 的資訊 [https://learn.microsoft.com/en-us/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/en-us/training/paths/create-custom-copilots-ai-studio/)

6. 了解更多關於 Azure AI Studio 的 Model Catalog 的資訊 [https://learn.microsoft.com/en-us/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/en-us/azure/ai-studio/how-to/model-catalog-overview)

