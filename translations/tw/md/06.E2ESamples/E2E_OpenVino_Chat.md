[OpenVino Chat Sample](../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

這段程式碼將模型匯出為 OpenVINO 格式，載入它，並用來生成給定提示的回應。

1. **匯出模型**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - 這個指令使用 `optimum-cli` 工具將模型匯出為 OpenVINO 格式，這種格式經過優化以提高推理效率。
   - 被匯出的模型是 `"microsoft/Phi-3-mini-4k-instruct"`，並且設定為基於過去上下文生成文字的任務。
   - 模型的權重被量化為 4 位元整數 (`int4`)，這有助於減少模型大小並加快處理速度。
   - 其他參數如 `group-size`、`ratio` 和 `sym` 用於微調量化過程。
   - 匯出的模型被儲存在目錄 `./model/phi3-instruct/int4` 中。

2. **匯入必要的庫**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - 這些行匯入來自 `transformers` 庫和 `optimum.intel.openvino` 模組的類，這些類需要用來載入和使用模型。

3. **設定模型目錄和配置**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` 指定了模型文件的儲存位置。
   - `ov_config` 是一個字典，用來配置 OpenVINO 模型以優先考慮低延遲、使用一個推理流，並且不使用快取目錄。

4. **載入模型**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - 這行從指定目錄載入模型，使用之前定義的配置設定。如果需要，還允許遠端程式碼執行。

5. **載入 Tokenizer**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - 這行載入 Tokenizer，它負責將文字轉換為模型可以理解的 tokens。

6. **設定 Tokenizer 參數**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - 這個字典指定不要在 tokenized 輸出中添加特殊 tokens。

7. **定義提示**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - 這個字串設定了一個對話提示，使用者請求 AI 助手自我介紹。

8. **將提示轉換為 tokens**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - 這行將提示轉換為模型可以處理的 tokens，並以 PyTorch 張量的形式返回結果。

9. **生成回應**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - 這行使用模型根據輸入的 tokens 生成回應，最多生成 1024 個新 tokens。

10. **解碼回應**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - 這行將生成的 tokens 轉換回人類可讀的字串，跳過任何特殊 tokens，並檢索第一個結果。

免責聲明：此翻譯由AI模型從原文翻譯而來，可能不夠完美。請審閱輸出內容並進行必要的修正。