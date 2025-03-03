[OpenVino Chat 範例](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

這段程式碼將模型匯出為 OpenVINO 格式，載入後使用該模型生成對給定提示的回應。

1. **匯出模型**：
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - 這個指令使用 `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`。

2. **匯入必要的函式庫**：
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - 這些程式碼行從 `transformers` library and the `optimum.intel.openvino` 模組中匯入所需的類別，用於載入和使用模型。

3. **設定模型目錄與配置**：
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` 是一個字典，用來配置 OpenVINO 模型以優化低延遲、使用單一推理流，並且不使用快取目錄。

4. **載入模型**：
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - 這行程式碼從指定的目錄載入模型，並使用先前定義的配置設定。必要時，也允許遠端程式碼執行。

5. **載入 Tokenizer**：
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - 這行程式碼載入 Tokenizer，用於將文字轉換為模型可以理解的 tokens。

6. **設定 Tokenizer 參數**：
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - 這個字典指定在 token 化的輸出中不應加入特殊 tokens。

7. **定義提示**：
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - 這個字串設定了一個對話提示，讓使用者請 AI 助手介紹自己。

8. **將提示進行 Token 化**：
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - 這行程式碼將提示轉換為模型可以處理的 tokens，並以 PyTorch tensors 的形式返回結果。

9. **生成回應**：
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - 這行程式碼使用模型根據輸入 tokens 生成回應，最多生成 1024 個新的 tokens。

10. **解碼回應**：
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - 這行程式碼將生成的 tokens 轉換回可讀的文字字串，忽略任何特殊 tokens，並返回第一個結果。

**免責聲明**：  
本文件已使用機器翻譯AI服務進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用本翻譯而引起的任何誤解或錯誤解讀概不負責。