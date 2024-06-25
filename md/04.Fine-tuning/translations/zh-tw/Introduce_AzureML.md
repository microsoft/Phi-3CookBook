# **介紹 Azure Machine Learning 服務**

[Azure Machine Learning](https://ml.azure.com?WT.mc_id=aiml-138114-kinfeylo) 是一項用於加速和管理機器學習（ML）專案生命週期的雲端服務。

ML 專業人士、資料科學家和工程師可以在他們的日常工作流程中使用它來：

- 訓練和部署模型。
管理機器學習操作（MLOps）。
- 您可以在 Azure Machine Learning 中建立模型，或使用從開源平台（如 PyTorch、TensorFlow 或 scikit-learn）建構的模型。
- MLOps 工具幫助您監控、重新訓練和重新部署模型。

## Azure Machine Learning 適合誰？

**資料科學家和 ML 工程師**

他們可以使用工具來加速和自動化他們的日常工作流程。
Azure ML 提供公平性、可解釋性、追蹤和審計功能。
應用程式開發人員：
他們可以將模型無縫整合到應用程式或服務中。

**平台開發者**

他們可以使用由耐用的 Azure Resource Manager API 支援的一套強大工具。
這些工具允許建構先進的 ML 工具。

**企業**

在 Microsoft Azure 雲端中工作，企業受益於熟悉的安全性和基於角色的存取控制。
設定專案以控制對受保護資料和特定操作的存取。

## 團隊每個人的生產力

ML 專案通常需要具備多種技能的團隊來建構和維護。

Azure ML 提供工具，使您能夠：

- 通過共享筆記本、計算資源、無伺服器計算、數據和環境與您的團隊合作。
- 開發具有公平性、可解釋性、跟蹤和審計能力的模型，以滿足譜系和審計合規性要求。
- 快速輕鬆地大規模部署 ML 模型，並使用 MLOps 高效管理和治理它們。
- 使用內建的治理、安全性和合規性在任何地方執行機器學習工作負載。

## 跨相容性平台工具

任何在 ML 團隊中的人都可以使用他們偏好的工具來完成工作。
無論你是在執行快速實驗、超參數調整、建構管道，還是管理推論，你都可以使用熟悉的介面，包括:

- Azure Machine Learning Studio
- Python SDK (v2)
- Azure CLI (v2)
- Azure Resource Manager REST APIs

隨著您在開發週期中精煉模型並進行協作，您可以在 Azure Machine Learning studio UI 中分享和查找資產、資源和指標。

## **LLM/SLM in Azure ML**

Azure ML 已經新增了許多 LLM/SLM 相關函式，結合 LLMOps 和 SLMOps 來建立一個企業級的生成式人工智慧技術平台。

### **模型目錄**

企業用戶可以通過 Model Catalog 根據不同的業務場景部署不同的模型，並作為 Model as Service 提供服務，供企業開發者或用戶訪問。

![models](../../../../imgs/04/03/models.png)

Azure Machine Learning studio 中的模型目錄是發現和使用各種模型的中心，使您能夠建構生成式 AI 應用程式。模型目錄具有數百種來自模型提供者的模型，例如 Azure OpenAI service、Mistral、Meta、Cohere、Nvidia、Hugging Face，包括由 Microsoft 訓練的模型。來自 Microsoft 以外提供者的模型是非 Microsoft 產品，根據 Microsoft 的產品條款進行定義，並受模型附帶條款的約束。

### **工作管道**

機器學習管道的核心是將完整的機器學習任務分解為多步驟的工作流程。每一步都是一個可管理的組件，可以單獨開發、優化、配置和自動化。步驟通過定義良好的介面連接。Azure 機器學習管道服務會自動協調管道步驟之間的所有相依性。

在微調 SLM / LLM 時，我們可以通過 Pipeline 管理我們的數據、訓練和生成過程。

![finetuning](../../../../imgs/04/03/finetuning.png)

### **提示流程**

使用 Azure Machine Learning prompt flow 的好處
Azure Machine Learning prompt flow 提供了一系列的好處，幫助使用者從構思過渡到實驗，最終達到生產就緒的 LLM 基礎應用程式:

**Prompt engineering agility**

互動式創作體驗: Azure Machine Learning 提示流提供了流程結構的視覺表示，使用戶能夠輕鬆理解和導航他們的專案。它還提供類似筆記本的程式碼體驗，以便於高效的流程開發和調試。
提示調整的變體: 用戶可以建立和比較多個提示變體，促進迭代改進過程。

評估: 內建評估流程使用戶能夠評估其提示和流程的品質和效果。

全面的資源: Azure Machine Learning prompt flow 包含內建工具、範例和模板的函式庫，這些資源作為開發的起點，激發創意並加速過程。

**企業級 LLM 基礎應用程式的準備**

合作: Azure Machine Learning 提示流程支援團隊合作，允許多個使用者共同協作提示工程專案、分享知識並維護版本控制。

全方位平台: Azure Machine Learning prompt flow 簡化了整個 prompt 工程流程，從開發和評估到部署和監控。用戶可以輕鬆地將他們的 flow 部署為 Azure Machine Learning 端點，並實時監控其性能，確保最佳運行和持續改進。

Azure Machine Learning 企業準備解決方案: Prompt flow 利用 Azure Machine Learning 強大的企業準備解決方案，為流程的開發、實驗和部署提供安全、可延展和可靠的基礎。

使用 Azure Machine Learning prompt flow，用戶可以釋放他們的 prompt 工程敏捷性，有效地協作，並利用企業級解決方案來成功開發和部署基於 LLM 的應用程式。

結合 Azure ML 的計算能力、數據和不同的組件，企業開發人員可以輕鬆建構自己的人工智慧應用程式。

