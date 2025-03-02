[OpenVino Chat Sample](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

呢段程式碼會將模型匯出到 OpenVINO 格式，然後載入並用嚟根據提供嘅提示生成回應。

1. **匯出模型**：
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - 呢個指令用咗 `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`。

2. **匯入所需嘅函式庫**：
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - 呢幾行會從 `transformers` library and the `optimum.intel.openvino` 模組匯入所需嘅類別，用嚟載入同使用模型。

3. **設定模型目錄同配置**：
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` 係一個字典，用嚟配置 OpenVINO 模型，優化低延遲、使用單一推理串流，並且唔使用緩存目錄。

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
   - 呢行會根據之前定義嘅配置設定，從指定目錄載入模型。同時亦容許必要時進行遠端程式碼執行。

5. **載入 Tokenizer**：
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - 呢行會載入 tokenizer，佢負責將文字轉換成模型可以理解嘅 token。

6. **設定 Tokenizer 參數**：
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - 呢個字典指定咗唔應該將特殊符號加入到 token 化嘅輸出中。

7. **定義提示**：
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - 呢段字串設定咗一個對話提示，用家要求 AI 助手介紹自己。

8. **將提示進行 Token 化**：
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - 呢行將提示轉換成模型可以處理嘅 token，並將結果以 PyTorch tensor 格式返回。

9. **生成回應**：
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - 呢行用模型根據輸入嘅 token 生成回應，最多可以生成 1024 個新 token。

10. **解碼回應**：
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - 呢行將生成嘅 token 轉返成可讀嘅文字，略過任何特殊符號，並取得第一個結果。

**免責聲明**：  
本文件使用機器翻譯人工智能服務進行翻譯。我們致力於提供準確的翻譯，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用本翻譯而引起的任何誤解或錯誤解讀概不負責。