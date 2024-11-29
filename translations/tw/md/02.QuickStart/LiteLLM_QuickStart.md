使用 [LiteLLM](https://docs.litellm.ai/) 搭配 Phi-3 模型是一個很好的選擇，尤其是當你想要將它整合到各種應用中時。LiteLLM 作為一個中介軟體，將 API 呼叫轉換為兼容不同模型的請求，包括 Phi-3。

Phi-3 是由 Microsoft 開發的小型語言模型（SLM），設計目的是高效並能在資源受限的機器上運行。它可以在支持 AVX 的 CPU 和僅 4 GB RAM 的情況下運行，是本地推理而不需要 GPU 的好選擇。

以下是使用 LiteLLM 搭配 Phi-3 的一些步驟：

1. **安裝 LiteLLM**：你可以使用 pip 安裝 LiteLLM：
   ```bash
   pip install litellm
   ```

2. **設定環境變數**：配置你的 API 密鑰和其他必要的環境變數。
   ```python
   import os
   os.environ["OPENAI_API_KEY"] = "your-api-key"
   ```

3. **進行 API 呼叫**：使用 LiteLLM 對 Phi-3 模型進行 API 呼叫。
   ```python
   from litellm import completion

   response = completion(
       model="phi-3",
       messages=[{"role": "user", "content": "Hello, how are you?"}]
   )
   print(response)
   ```

4. **整合**：你可以將 LiteLLM 整合到各種平台中，如 Nextcloud Assistant，讓你可以使用 Phi-3 進行文本生成和其他任務。

**完整的 LLMLite 代碼範例**
[LLMLite 的範例代碼筆記本](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/litellm.ipynb)

**免責聲明**：
本文檔是使用基於機器的AI翻譯服務翻譯的。儘管我們努力追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應將原文檔的母語版本視為權威來源。對於關鍵信息，建議尋求專業的人類翻譯。我們對使用此翻譯引起的任何誤解或誤讀不承擔責任。