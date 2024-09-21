# 在 Azure AI 和 Azure ML 中使用 OpenAI SDK 與 Phi-3

使用 `openai` SDK 來消費 Azure AI 和 Azure ML 中的 Phi-3 部署。Azure AI 和 Azure ML 中的 Phi-3 模型家族提供與 OpenAI Chat Completion API 兼容的 API。這讓客戶和用戶能夠無縫地從 OpenAI 模型轉換到 Phi-3 大型語言模型（LLM）。

這個 API 可以直接與 OpenAI 的客戶端庫或第三方工具（如 LangChain 或 LlamaIndex）一起使用。

下面的示例展示了如何使用 OpenAI Python 庫進行這種轉換。請注意，Phi-3 僅支持聊天完成 API。

要使用 OpenAI SDK 與 Phi-3 模型，您需要按照幾個步驟來設置您的環境並進行 API 調用。以下是入門指南：

1. **安裝 OpenAI SDK**：首先，如果您尚未安裝 OpenAI Python 包，您需要安裝它。
   ```bash
   pip install openai
   ```

2. **設置您的 API 密鑰**：確保您擁有 OpenAI API 密鑰。您可以將其設置在環境變量中或直接在代碼中。
   ```python
   import openai

   openai.api_key = "your-api-key"
   ```

3. **進行 API 調用**：使用 OpenAI SDK 與 Phi-3 模型交互。以下是如何進行完成請求的示例：
   ```python
   response = openai.Completion.create(
       model="phi-3",
       prompt="Hello, how are you?",
       max_tokens=50
   )

   print(response.choices[0].text.strip())
   ```

4. **處理響應**：根據您的應用需求處理模型的響應。

這裡有一個更詳細的示例：
```python
import openai

# 設置您的 API 密鑰
openai.api_key = "your-api-key"

# 定義提示
prompt = "Write a short story about a brave knight."

# 進行 API 調用
response = openai.Completion.create(
    model="phi-3",
    prompt=prompt,
    max_tokens=150
)

# 打印響應
print(response.choices[0].text.strip())
```

這將根據提供的提示生成一個短篇故事。您可以調整 `max_tokens` 參數來控制輸出的長度。

[參見 Phi-3 模型的完整 Notebook 示例](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/openaisdk.ipynb)

查看 [文檔](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo) 了解 AI Studio 和 ML Studio 中 Phi-3 模型家族的詳細信息，包括如何配置推理端點、區域可用性、定價和推理模式參考。

