# 使用 Windows GPU 創建基於 Phi-3.5-Instruct ONNX 的 Prompt Flow 解決方案

以下文件是一個使用 PromptFlow 和 ONNX（Open Neural Network Exchange）開發基於 Phi-3 模型的 AI 應用的範例。

PromptFlow 是一套開發工具，旨在簡化基於大型語言模型（LLM）的 AI 應用的全生命周期開發流程，涵蓋從創意構思、原型設計到測試與評估的每個階段。

通過將 PromptFlow 與 ONNX 結合，開發者可以：

- **優化模型性能**：利用 ONNX 提高模型推理和部署的效率。
- **簡化開發流程**：使用 PromptFlow 管理工作流程並自動化重複性任務。
- **增強團隊協作**：提供統一的開發環境，促進團隊成員之間更好的協作。

**Prompt flow** 是一套開發工具，旨在簡化基於 LLM 的 AI 應用從創意、原型設計、測試、評估到生產部署和監控的全流程開發週期。它讓提示工程變得更加簡單，並幫助您構建具有生產質量的 LLM 應用。

Prompt flow 可以連接到 OpenAI、Azure OpenAI Service，以及可自定義的模型（如 Huggingface、本地 LLM/SLM）。我們希望將 Phi-3.5 的量化 ONNX 模型部署到本地應用中。Prompt flow 可以幫助我們更好地規劃業務，並基於 Phi-3.5 完成本地解決方案。在這個範例中，我們將結合 ONNX Runtime GenAI Library，完成基於 Windows GPU 的 Prompt flow 解決方案。

## **安裝**

### **Windows GPU 的 ONNX Runtime GenAI**

請參考此指引來設定 Windows GPU 的 ONNX Runtime GenAI：[點擊這裡](./ORTWindowGPUGuideline.md)

### **在 VSCode 中設置 Prompt flow**

1. 安裝 Prompt flow VS Code 擴展

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.tw.png)

2. 安裝 Prompt flow VS Code 擴展後，點擊擴展，並選擇 **Installation dependencies**，按照指引在您的環境中安裝 Prompt flow SDK

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.tw.png)

3. 下載 [範例代碼](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf)，並使用 VS Code 開啟此範例

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.tw.png)

4. 打開 **flow.dag.yaml**，選擇您的 Python 環境

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.tw.png)

   打開 **chat_phi3_ort.py**，更改您的 Phi-3.5-instruct ONNX 模型位置

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.tw.png)

5. 運行您的 Prompt flow 進行測試

打開 **flow.dag.yaml**，點擊可視化編輯器

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.tw.png)

點擊後，運行以進行測試

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.tw.png)

6. 您可以在終端運行批處理以檢查更多結果

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

您可以在默認瀏覽器中查看結果

![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.tw.png)

**免責聲明**：  
本文件使用基於機器的人工智能翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文檔的母語版本作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解讀不承擔責任。