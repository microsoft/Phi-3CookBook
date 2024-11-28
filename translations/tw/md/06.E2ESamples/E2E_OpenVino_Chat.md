[OpenVino Chat Sample](../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

這段程式碼會將模型匯出為 OpenVINO 格式，載入並使用它來生成對給定提示的回應。

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
   - 這幾行程式碼從 `transformers` library and the `optimum.intel.openvino` 模組中匯入類別，這些類別是載入和使用模型所需的。

3. **設定模型目錄和配置**：
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` 是一個字典，用來配置 OpenVINO 模型，使其優先考慮低延遲、使用一個推理流並且不使用快取目錄。

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
   - 這行程式碼從指定的目錄中載入模型，使用之前定義的配置設定。如果需要，還允許遠端程式碼執行。

5. **載入分詞器**：
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - 這行程式碼載入分詞器，負責將文字轉換為模型可以理解的標記。

6. **設定分詞器參數**：
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - 這個字典指定在標記化輸出中不應添加特殊標記。

7. **定義提示**：
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - 這個字串設置了一個對話提示，使用者請求 AI 助理介紹自己。

8. **標記化提示**：
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - 這行程式碼將提示轉換為模型可以處理的標記，並以 PyTorch 張量的形式返回結果。

9. **生成回應**：
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - 這行程式碼使用模型根據輸入標記生成回應，最多生成 1024 個新標記。

10. **解碼回應**：
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - 這行程式碼將生成的標記轉換回人類可讀的字串，跳過任何特殊標記，並取得第一個結果。

**免責聲明**：
本文件是使用機器翻譯服務進行翻譯的。雖然我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對使用本翻譯所產生的任何誤解或誤釋不承擔責任。