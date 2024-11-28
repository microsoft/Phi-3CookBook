# 使用 OpenAI SDK 與 Azure AI 和 Azure ML 中的 Phi-3

使用 `openai` SDK 來消費 Azure AI 和 Azure ML 中的 Phi-3 部署。Azure AI 和 Azure ML 中的 Phi-3 模型系列提供與 OpenAI Chat Completion API 兼容的 API。它允許客戶和用戶從 OpenAI 模型無縫過渡到 Phi-3 大型語言模型 (LLMs)。

該 API 可以直接與 OpenAI 的客戶端庫或第三方工具（如 LangChain 或 LlamaIndex）一起使用。

下面的例子展示了如何使用 OpenAI Python 庫進行這種過渡。請注意，Phi-3 僅支持聊天完成 API。

要使用 OpenAI SDK 與 Phi-3 模型，你需要按照幾個步驟來設置你的環境並進行 API 調用。這裡有一個入門指南：

1. **安裝 OpenAI SDK**：首先，如果你還沒有安裝 OpenAI Python 包，你需要安裝它。
   ```bash
   pip install openai
   ```

2. **設置你的 API 密鑰**：確保你有 OpenAI API 密鑰。你可以將它設置在環境變量中或直接在代碼中。
   ```python
   import openai

   openai.api_key = "your-api-key"
   ```

3. **進行 API 調用**：使用 OpenAI SDK 與 Phi-3 模型交互。這裡有一個完成請求的例子：
   ```python
   response = openai.Completion.create(
       model="phi-3",
       prompt="Hello, how are you?",
       max_tokens=50
   )

   print(response.choices[0].text.strip())
   ```

4. **處理回應**：根據你的應用程序需要處理來自模型的回應。

這裡有一個更詳細的例子：
```python
import openai

# Set your API key
openai.api_key = "your-api-key"

# Define the prompt
prompt = "Write a short story about a brave knight."

# Make the API call
response = openai.Completion.create(
    model="phi-3",
    prompt=prompt,
    max_tokens=150
)

# Print the response
print(response.choices[0].text.strip())
```

這將根據提供的提示生成一個短篇故事。你可以調整 `max_tokens` 參數來控制輸出的長度。

[參見 Phi-3 模型的完整 Notebook 示例](https://github.com/Azure/azureml-examples/blob/main/sdk/python/foundation-models/phi-3/openaisdk.ipynb)

查看 [Phi-3 模型系列的文檔](https://learn.microsoft.com/azure/ai-studio/how-to/deploy-models-phi-3?WT.mc_id=aiml-137032-kinfeylo) 了解有關 AI Studio 和 ML Studio 的詳細信息，包括如何提供推理端點、區域可用性、定價和推理架構參考。

**免責聲明**：
本文件是使用機器翻譯服務翻譯的。我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對使用此翻譯引起的任何誤解或誤讀不承擔責任。