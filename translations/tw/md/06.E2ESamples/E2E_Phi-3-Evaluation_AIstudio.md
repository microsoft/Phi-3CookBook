# 在 Azure AI Foundry 中評估微調過的 Phi-3 / Phi-3.5 模型，聚焦於 Microsoft 的負責任 AI 原則

這個端到端 (E2E) 範例基於 Microsoft Tech Community 的指南 "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)".

## 概述

### 如何在 Azure AI Foundry 中評估微調過的 Phi-3 / Phi-3.5 模型的安全性和性能？

微調模型有時可能會導致意外或不希望的回應。為了確保模型保持安全和有效，評估模型生成有害內容的潛力以及生成準確、相關和連貫回應的能力是很重要的。在本教程中，您將學習如何評估在 Azure AI Foundry 中整合 Prompt flow 的微調 Phi-3 / Phi-3.5 模型的安全性和性能。

以下是 Azure AI Foundry 的評估過程。

![教程架構。](../../../../translated_images/architecture.1eb9d143d0771c6065f16c0f66a9eb233f466cdf9db0b0afe11adcbd57eb06ce.tw.png)

*圖片來源: [生成式 AI 應用的評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> 欲了解更多詳細信息和探索有關 Phi-3 / Phi-3.5 的其他資源，請訪問 [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)。

### 先決條件

- [Python](https://www.python.org/downloads)
- [Azure 訂閱](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- 微調過的 Phi-3 / Phi-3.5 模型

### 目錄

1. [**情境 1: 介紹 Azure AI Foundry 的 Prompt flow 評估**](../../../../md/06.E2ESamples)

    - [安全性評估介紹](../../../../md/06.E2ESamples)
    - [性能評估介紹](../../../../md/06.E2ESamples)

1. [**情境 2: 在 Azure AI Foundry 中評估 Phi-3 / Phi-3.5 模型**](../../../../md/06.E2ESamples)

    - [開始之前](../../../../md/06.E2ESamples)
    - [部署 Azure OpenAI 以評估 Phi-3 / Phi-3.5 模型](../../../../md/06.E2ESamples)
    - [使用 Azure AI Foundry 的 Prompt flow 評估微調過的 Phi-3 / Phi-3.5 模型](../../../../md/06.E2ESamples)

1. [恭喜！](../../../../md/06.E2ESamples)

## **情境 1: 介紹 Azure AI Foundry 的 Prompt flow 評估**

### 安全性評估介紹

為了確保您的 AI 模型是道德且安全的，依據 Microsoft 的負責任 AI 原則進行評估是至關重要的。在 Azure AI Foundry 中，安全性評估允許您評估模型對越獄攻擊的脆弱性及其生成有害內容的潛力，這直接與這些原則一致。

![安全性評估。](../../../../translated_images/safety-evaluation.5ad906c4618e4c8736fdeeff54a52dac8ae6d0756b15824e430177fba7b6a8b4.tw.png)

*圖片來源: [生成式 AI 應用的評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft 的負責任 AI 原則

在開始技術步驟之前，了解 Microsoft 的負責任 AI 原則是一個設計用來指導 AI 系統負責任開發、部署和運行的倫理框架是很重要的。這些原則指導 AI 系統的負責任設計、開發和部署，確保 AI 技術以公平、透明和包容的方式構建。這些原則是評估 AI 模型安全性的基礎。

Microsoft 的負責任 AI 原則包括：

- **公平和包容性**: AI 系統應該公平對待每個人，避免對相似情況下的群體產生不同的影響。例如，當 AI 系統提供醫療建議、貸款申請或就業建議時，它們應該對有相似症狀、財務狀況或專業資格的人提供相同的建議。

- **可靠性和安全性**: 為了建立信任，AI 系統需要可靠、安全和一致地運行。這些系統應該能夠按照最初的設計運行，安全地應對意外情況，並抵禦有害的操縱。它們的行為和能夠處理的條件範圍反映了開發人員在設計和測試期間預期的情況和條件。

- **透明度**: 當 AI 系統幫助做出對人們生活有重大影響的決定時，人們需要理解這些決定是如何做出的。例如，銀行可能會使用 AI 系統來決定某人是否具有信用資格。一家公司可能會使用 AI 系統來確定最合適的候選人。

- **隱私和安全**: 隨著 AI 的普及，保護隱私和確保個人和商業信息的安全變得越來越重要和複雜。由於數據訪問對 AI 系統做出準確和知情的預測和決定至關重要，隱私和數據安全需要密切關注。

- **問責性**: 設計和部署 AI 系統的人必須對其系統的運行方式負責。組織應該依據行業標準制定問責規範。這些規範可以確保 AI 系統不是對影響人們生活的任何決定的最終權威。它們還可以確保人類對高度自動化的 AI 系統保持有意義的控制。

![填充中心。](../../../../translated_images/responsibleai2.ae6f996d95dcc46b3b3087c0e4f4f4b74c64e961083009ecca7a0a3998b3f716.tw.png)

*圖片來源: [什麼是負責任 AI？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> 欲了解更多有關 Microsoft 的負責任 AI 原則，請訪問 [什麼是負責任 AI？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)。

#### 安全性指標

在本教程中，您將使用 Azure AI Foundry 的安全性指標來評估微調過的 Phi-3 模型的安全性。這些指標幫助您評估模型生成有害內容的潛力及其對越獄攻擊的脆弱性。安全性指標包括：

- **與自我傷害相關的內容**: 評估模型是否有生成與自我傷害相關內容的傾向。
- **仇恨和不公平內容**: 評估模型是否有生成仇恨或不公平內容的傾向。
- **暴力內容**: 評估模型是否有生成暴力內容的傾向。
- **性內容**: 評估模型是否有生成不適當性內容的傾向。

評估這些方面確保 AI 模型不會生成有害或冒犯性內容，與社會價值觀和監管標準保持一致。

![基於安全性進行評估。](../../../../translated_images/evaluate-based-on-safety.63d79ac01570713002d5d858bfbb8f4d7295557ae8829d0c379485d67a3fcd1c.tw.png)

### 性能評估介紹

為了確保您的 AI 模型按預期運行，評估其性能是很重要的。在 Azure AI Foundry 中，性能評估允許您評估模型生成準確、相關和連貫回應的效果。

![性能評估。](../../../../translated_images/performance-evaluation.259c44647c74a80761cdcbaab2202142f99a5a0d28326c8a1eb6dc2765f5ef77.tw.png)

*圖片來源: [生成式 AI 應用的評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### 性能指標

在本教程中，您將使用 Azure AI Foundry 的性能指標來評估微調過的 Phi-3 / Phi-3.5 模型的性能。這些指標幫助您評估模型生成準確、相關和連貫回應的效果。性能指標包括：

- **基礎性**: 評估生成的回答與輸入來源信息的一致性。
- **相關性**: 評估生成的回應對給定問題的相關性。
- **連貫性**: 評估生成的文本流暢性、自然讀寫性和類似人類語言的程度。
- **流利度**: 評估生成文本的語言能力。
- **GPT 相似性**: 比較生成的回應與真實答案的相似性。
- **F1 分數**: 計算生成回應與源數據之間共享詞語的比例。

這些指標幫助您評估模型生成準確、相關和連貫回應的效果。

![基於性能進行評估。](../../../../translated_images/evaluate-based-on-performance.33ccf1c52f210af8e76d9cab863716d3f67db3d765254371a30136cc8f852b37.tw.png)

## **情境 2: 在 Azure AI Foundry 中評估 Phi-3 / Phi-3.5 模型**

### 開始之前

本教程是先前博客文章的後續，"[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" 和 "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)"。在這些文章中，我們詳細介紹了在 Azure AI Foundry 中微調 Phi-3 / Phi-3.5 模型並將其整合到 Prompt flow 中的過程。

在本教程中，您將部署一個 Azure OpenAI 模型作為評估器在 Azure AI Foundry 中使用，並使用它來評估您的微調 Phi-3 / Phi-3.5 模型。

在開始本教程之前，請確保您具備以下先決條件，如先前教程中所述：

1. 已準備好評估微調 Phi-3 / Phi-3.5 模型的數據集。
1. 已微調並部署到 Azure 機器學習的 Phi-3 / Phi-3.5 模型。
1. 在 Azure AI Foundry 中與您的微調 Phi-3 / Phi-3.5 模型整合的 Prompt flow。

> [!NOTE]
> 您將使用 *test_data.jsonl* 文件，該文件位於從先前博客文章下載的 **ULTRACHAT_200k** 數據集的數據文件夾中，作為評估微調 Phi-3 / Phi-3.5 模型的數據集。

#### 在 Azure AI Foundry 中將自定義 Phi-3 / Phi-3.5 模型與 Prompt flow 整合（代碼優先方法）

> [!NOTE]
> 如果您按照低代碼方法進行，請參考 "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)" 中的描述，您可以跳過此練習並進行下一步。
> 但是，如果您按照 "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" 中描述的代碼優先方法微調並部署您的 Phi-3 / Phi-3.5 模型，則將模型連接到 Prompt flow 的過程略有不同。您將在此練習中學習這個過程。

要繼續，您需要將微調過的 Phi-3 / Phi-3.5 模型整合到 Azure AI Foundry 的 Prompt flow 中。

#### 創建 Azure AI Foundry Hub

在創建項目之前，您需要創建一個 Hub。Hub 類似於資源組，允許您在 Azure AI Foundry 中組織和管理多個項目。

1. 登錄 [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 從左側選項卡選擇 **All hubs**。

1. 從導航菜單中選擇 **+ New hub**。

    ![創建 hub。](../../../../translated_images/create-hub.8d452311ef5b4b9188df89f7cff7797c67ec8f391282235b19b988e167f3e920.tw.png)

1. 執行以下任務：

    - 輸入 **Hub name**。它必須是唯一的值。
    - 選擇您的 Azure **Subscription**。
    - 選擇要使用的 **Resource group**（如果需要，創建一個新的）。
    - 選擇您要使用的 **Location**。
    - 選擇要使用的 **Connect Azure AI Services**（如果需要，創建一個新的）。
    - 選擇 **Connect Azure AI Search** 為 **Skip connecting**。
![填寫 hub.](../../../../translated_images/fill-hub.8b19834866ef631a2fd031584c77b78c0438a385bdee8f981361b14bbc46f5e1.tw.png)

1. 選擇 **Next**。

#### 建立 Azure AI Foundry 專案

1. 在你建立的 Hub 中，從左側選單選擇 **All projects**。

1. 從導航選單中選擇 **+ New project**。

    ![選擇新專案.](../../../../translated_images/select-new-project.1a925c25ca3bc47b2b16feefc5a76f5c29e211ac464ea5c3cdfe389868d87da7.tw.png)

1. 輸入 **Project name**，必須是唯一的值。

    ![建立專案.](../../../../translated_images/create-project.ff239752937343b4cb38156740ebda92bc1d8b16299183c245f3e3661432db31.tw.png)

1. 選擇 **Create a project**。

#### 新增自訂連線以微調 Phi-3 / Phi-3.5 模型

要將自訂的 Phi-3 / Phi-3.5 模型與 Prompt flow 整合，你需要將模型的端點和金鑰儲存在自訂連線中。這樣的設置確保在 Prompt flow 中可以訪問你的自訂 Phi-3 / Phi-3.5 模型。

#### 設定微調 Phi-3 / Phi-3.5 模型的 api key 和 endpoint uri

1. 訪問 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 導航到你建立的 Azure Machine learning workspace。

1. 從左側選單選擇 **Endpoints**。

    ![選擇端點.](../../../../translated_images/select-endpoints.3027748aed379990fd8ee9bf27f70ff11918955bb1a10269e2f34f6931b26955.tw.png)

1. 選擇你建立的端點。

    ![選擇已建立的端點.](../../../../translated_images/select-endpoint-created.560a5cadfbbb58b66abb2fb61b4450b22060371910af1b45c358bde548234ebc.tw.png)

1. 從導航選單中選擇 **Consume**。

1. 複製你的 **REST endpoint** 和 **Primary key**。

    ![複製 api key 和 endpoint uri.](../../../../translated_images/copy-endpoint-key.56de01742992f2402d57139849304b5b049fb468fb38abc7982b7dfc311daf9e.tw.png)

#### 新增自訂連線

1. 訪問 [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 導航到你建立的 Azure AI Foundry 專案。

1. 在你建立的專案中，從左側選單選擇 **Settings**。

1. 選擇 **+ New connection**。

    ![選擇新連線.](../../../../translated_images/select-new-connection.a1ff72172d07054308a3fc7b7b86e25e9ca1c879f0a382b9a2be2c80bb2ebcc5.tw.png)

1. 從導航選單中選擇 **Custom keys**。

    ![選擇自訂金鑰.](../../../../translated_images/select-custom-keys.b17eb3b15eae28126a4eeda8f53396b9a6f773745f2dd68c464252575a77b5d3.tw.png)

1. 執行以下任務：

    - 選擇 **+ Add key value pairs**。
    - 對於金鑰名稱，輸入 **endpoint** 並將從 Azure ML Studio 複製的端點貼入值欄位。
    - 再次選擇 **+ Add key value pairs**。
    - 對於金鑰名稱，輸入 **key** 並將從 Azure ML Studio 複製的金鑰貼入值欄位。
    - 添加金鑰後，選擇 **is secret** 以防止金鑰暴露。

    ![新增連線.](../../../../translated_images/add-connection.c01c94851c9eece708711456a4853355b9532b0cb1f970e24f165e7e1d6c0a03.tw.png)

1. 選擇 **Add connection**。

#### 建立 Prompt flow

你已在 Azure AI Foundry 中新增了自訂連線。現在，讓我們使用以下步驟建立一個 Prompt flow。然後，你將把這個 Prompt flow 連接到自訂連線，以便在 Prompt flow 中使用微調的模型。

1. 導航到你建立的 Azure AI Foundry 專案。

1. 從左側選單選擇 **Prompt flow**。

1. 從導航選單中選擇 **+ Create**。

    ![選擇 Promptflow.](../../../../translated_images/select-promptflow.766ad0f2403e2bd6f374bee40a607321e3e2b416629063acf3204a983fb4bcaa.tw.png)

1. 從導航選單中選擇 **Chat flow**。

    ![選擇聊天流程.](../../../../translated_images/select-flow-type.0e18b84032da1200e48a702e5140c1775b1eb6de9cf222c6a8007840fa278e97.tw.png)

1. 輸入要使用的 **Folder name**。

    ![輸入名稱.](../../../../translated_images/enter-name.43919b211b1e8e0184536dc09184190e7e8c56bf960d4b5601443efddc757db4.tw.png)

1. 選擇 **Create**。

#### 設置 Prompt flow 與你的自訂 Phi-3 / Phi-3.5 模型進行聊天

你需要將微調的 Phi-3 / Phi-3.5 模型整合到 Prompt flow 中。然而，現有的 Prompt flow 不適合這個目的。因此，你必須重新設計 Prompt flow 以實現自訂模型的整合。

1. 在 Prompt flow 中，執行以下任務以重建現有的流程：

    - 選擇 **Raw file mode**。
    - 刪除 *flow.dag.yml* 文件中的所有現有代碼。
    - 將以下代碼添加到 *flow.dag.yml* 中。

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - 選擇 **Save**。

    ![選擇原始文件模式.](../../../../translated_images/select-raw-file-mode.2084d7f905df40f69cc5ebe48efa2318e92fd069358625a92993ef614f189d84.tw.png)

1. 將以下代碼添加到 *integrate_with_promptflow.py* 中，以在 Prompt flow 中使用自訂 Phi-3 / Phi-3.5 模型。

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![粘貼 prompt flow 代碼.](../../../../translated_images/paste-promptflow-code.667abbdf848fd03153828c0aa70dde58a851e09b1ba4c69bc6f686d2005656aa.tw.png)

> [!NOTE]
> 有關在 Azure AI Foundry 中使用 Prompt flow 的更多詳細信息，你可以參考 [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)。

1. 選擇 **Chat input**、**Chat output** 以啟用與模型的聊天功能。

    ![選擇輸入輸出.](../../../../translated_images/select-input-output.d4803eae144b03579db4a23def15c68bb50527017cdc4aa9f72c8679588a0f4c.tw.png)

1. 現在你已準備好與你的自訂 Phi-3 / Phi-3.5 模型進行聊天。在下一個練習中，你將學習如何啟動 Prompt flow 並使用它與微調的 Phi-3 / Phi-3.5 模型進行聊天。

> [!NOTE]
>
> 重建的流程應如下圖所示：
>
> ![流程範例](../../../../translated_images/graph-example.5b309021deca5b503270e50888da4784256730c210ed757f799f9bff0a12bb19.tw.png)
>

#### 啟動 Prompt flow

1. 選擇 **Start compute sessions** 以啟動 Prompt flow。

    ![啟動計算會話.](../../../../translated_images/start-compute-session.75300f481218ca70eae80304255956c71a9b6be31a18b43264118c19c0b1a016.tw.png)

1. 選擇 **Validate and parse input** 以更新參數。

    ![驗證輸入.](../../../../translated_images/validate-input.a6c90e55ce6117ea44e2acd88b8a20bc31136bf6c574b0a6c9217867201025c9.tw.png)

1. 選擇你建立的自訂連線的 **connection** 值。例如，*connection*。

    ![連接.](../../../../translated_images/select-connection.6573a1269969a14c83c397334051f71057ec9a243e95ea1b849483bd7481ff6a.tw.png)

#### 與你的自訂 Phi-3 / Phi-3.5 模型進行聊天

1. 選擇 **Chat**。

    ![選擇聊天.](../../../../translated_images/select-chat.25eab3d62b0a6c4960f0ae1b5d6efd6b5847cc20d468fd28cb1f0d656936cc22.tw.png)

1. 這是一個結果範例：現在你可以與你的自訂 Phi-3 / Phi-3.5 模型進行聊天。建議根據微調所用的數據提出問題。

    ![與 prompt flow 聊天.](../../../../translated_images/chat-with-promptflow.105b5a3b70ff64725c1d4cd2e9c6b55301219c7d68c9bec59106a49fb8bf40f2.tw.png)

### 部署 Azure OpenAI 以評估 Phi-3 / Phi-3.5 模型

要在 Azure AI Foundry 中評估 Phi-3 / Phi-3.5 模型，你需要部署一個 Azure OpenAI 模型。這個模型將用於評估 Phi-3 / Phi-3.5 模型的性能。

#### 部署 Azure OpenAI

1. 登錄 [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 導航到你建立的 Azure AI Foundry 專案。

    ![選擇專案.](../../../../translated_images/select-project-created.7b3c97c3883c3a95d547173b41e579cd748df940749c3d9616fe03ef46a3eda2.tw.png)

1. 在你建立的專案中，從左側選單選擇 **Deployments**。

1. 從導航選單中選擇 **+ Deploy model**。

1. 選擇 **Deploy base model**。

    ![選擇部署.](../../../../translated_images/deploy-openai-model.f09a74e1f976b52f85fdef711372452b9faed270e9d015887e09f44b41bbc163.tw.png)

1. 選擇你想使用的 Azure OpenAI 模型。例如，**gpt-4o**。

    ![選擇你想使用的 Azure OpenAI 模型.](../../../../translated_images/select-openai-model.29fbbd802d6a9aa941097ae80a0ffe256239e636190b7c1e49f28d3d66143a0d.tw.png)

1. 選擇 **Confirm**。

### 使用 Azure AI Foundry 的 Prompt flow 評估微調的 Phi-3 / Phi-3.5 模型

### 開始新的評估

1. 訪問 [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723)。

1. 導航到你建立的 Azure AI Foundry 專案。

    ![選擇專案.](../../../../translated_images/select-project-created.7b3c97c3883c3a95d547173b41e579cd748df940749c3d9616fe03ef46a3eda2.tw.png)

1. 在你建立的專案中，從左側選單選擇 **Evaluation**。

1. 從導航選單中選擇 **+ New evaluation**。
![Select evaluation.](../../../../translated_images/select-evaluation.7d8a8228ebdf3f3b46bf5cf6ab5bdcb4565132ba6b28126d9757aaf3abade725.tw.png)

1. 選擇 **Prompt flow** 評估。

    ![Select Prompt flow evaluation.](../../../../translated_images/promptflow-evaluation.ff4265fafd69c7f5ded1b5275cacecbd5f3272a6358c1f784f62e64bcb9e949f.tw.png)

1. 執行以下任務：

    - 輸入評估名稱，必須是唯一的值。
    - 選擇 **Question and answer without context** 作為任務類型，因為本教程使用的 **UlTRACHAT_200k** 數據集不包含上下文。
    - 選擇你想要評估的 prompt flow。

    ![Prompt flow evaluation.](../../../../translated_images/evaluation-setting1.d3b22a8343f8265807e2b507fa7eec9d86a9cefd4a67bc39ba2022d572f13e1d.tw.png)

1. 選擇 **Next**。

1. 執行以下任務：

    - 選擇 **Add your dataset** 上傳數據集。例如，你可以上傳測試數據集文件，如 *test_data.json1*，這是下載 **ULTRACHAT_200k** 數據集時包含的文件。
    - 選擇與你的數據集匹配的 **Dataset column**。例如，如果你使用 **ULTRACHAT_200k** 數據集，選擇 **${data.prompt}** 作為數據集列。

    ![Prompt flow evaluation.](../../../../translated_images/evaluation-setting2.32749fa51bc4fdb32f75dfd09b96bee74454c51ce3084bcc6f95b7286177a657.tw.png)

1. 選擇 **Next**。

1. 執行以下任務來配置性能和質量指標：

    - 選擇你想使用的性能和質量指標。
    - 選擇你為評估創建的 Azure OpenAI 模型。例如，選擇 **gpt-4o**。

    ![Prompt flow evaluation.](../../../../translated_images/evaluation-setting3-1.db76b89d94911c84ece6ce793593a4289278e1b24520e38ecd8372f4b9dc1167.tw.png)

1. 執行以下任務來配置風險和安全指標：

    - 選擇你想使用的風險和安全指標。
    - 選擇計算缺陷率的門檻值。例如，選擇 **Medium**。
    - 對於 **question**，選擇 **Data source** 為 **{$data.prompt}**。
    - 對於 **answer**，選擇 **Data source** 為 **{$run.outputs.answer}**。
    - 對於 **ground_truth**，選擇 **Data source** 為 **{$data.message}**。

    ![Prompt flow evaluation.](../../../../translated_images/evaluation-setting3-2.eb9892654970af140ebb74fcc99e06dad7eca3d38365e3f2cbe90101392f41ee.tw.png)

1. 選擇 **Next**。

1. 選擇 **Submit** 開始評估。

1. 評估將需要一些時間完成。你可以在 **Evaluation** 標籤中監控進度。

### 查看評估結果

> [!NOTE]
> 下列結果旨在說明評估過程。在本教程中，我們使用了一個在相對較小數據集上微調的模型，這可能會導致次優結果。實際結果可能會根據數據集的大小、質量和多樣性以及模型的具體配置有很大差異。

一旦評估完成，你可以查看性能和安全指標的結果。

1. 性能和質量指標：

    - 評估模型在生成連貫、流暢和相關回應方面的有效性。

    ![Evaluation result.](../../../../translated_images/evaluation-result-gpu.5b6e301e6d1af6044819f4d3c8443cbc44fb7db54ebce208b4288744ca25e6e8.tw.png)

1. 風險和安全指標：

    - 確保模型的輸出是安全的，符合負責任的 AI 原則，避免任何有害或冒犯的內容。

    ![Evaluation result.](../../../../translated_images/evaluation-result-gpu-2.d867d40ee9dfebc40c878288b8dc8727721a2fec995904b1475c513f0960e8e0.tw.png)

1. 你可以向下滾動查看 **Detailed metrics result**。

    ![Evaluation result.](../../../../translated_images/detailed-metrics-result.6cf00c2b6026bb500ff758ee3047c20f600aab3878c892897e99e2e3a88fb002.tw.png)

1. 通過對你的自定義 Phi-3 / Phi-3.5 模型進行性能和安全指標的評估，你可以確認模型不僅有效，而且遵循負責任的 AI 實踐，使其準備好進行實際部署。

## 恭喜！

### 你已完成本教程

你已成功評估了在 Azure AI Foundry 中與 Prompt flow 集成的微調 Phi-3 模型。這是確保你的 AI 模型不僅性能優越，還符合微軟負責任的 AI 原則的重要步驟，幫助你構建值得信賴和可靠的 AI 應用程序。

![Architecture.](../../../../translated_images/architecture.1eb9d143d0771c6065f16c0f66a9eb233f466cdf9db0b0afe11adcbd57eb06ce.tw.png)

## 清理 Azure 資源

清理你的 Azure 資源以避免對你的帳戶產生額外費用。請前往 Azure 入口網站並刪除以下資源：

- Azure 機器學習資源。
- Azure 機器學習模型端點。
- Azure AI Foundry 項目資源。
- Azure AI Foundry Prompt flow 資源。

### 下一步

#### 文件

- [microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)
- [使用負責任的 AI 儀表板評估 AI 系統](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [生成式 AI 的評估和監控指標](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry 文件](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow 文件](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### 培訓內容

- [微軟負責任 AI 方法介紹](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Azure AI Foundry 介紹](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### 參考

- [microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)
- [什麼是負責任的 AI？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [宣佈 Azure AI 中的新工具，幫助你構建更安全和可信的生成式 AI 應用程序](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [生成式 AI 應用程序的評估](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**免責聲明**:
本文件已使用機器翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原始語言的文件視為權威來源。對於關鍵信息，建議進行專業的人類翻譯。我們不對使用本翻譯引起的任何誤解或誤釋承擔責任。