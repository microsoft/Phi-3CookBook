[OpenVino Chat 示例](../../../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

此代码将模型导出为 OpenVINO 格式，加载后使用它根据给定的提示生成回复。

1. **导出模型**：
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - 此命令使用 `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`。

2. **导入必要的库**：
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - 这些代码行从 `transformers` library and the `optimum.intel.openvino` 模块中导入类，这些类用于加载和使用模型。

3. **设置模型目录和配置**：
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` 是一个字典，用于配置 OpenVINO 模型以优先低延迟，使用单一推理流，并且不使用缓存目录。

4. **加载模型**：
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - 这一行从指定目录加载模型，并使用之前定义的配置设置。必要时，它还允许远程代码执行。

5. **加载分词器**：
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - 这一行加载分词器，分词器负责将文本转换为模型可以理解的标记。

6. **设置分词器参数**：
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - 此字典指定不应在分词输出中添加特殊标记。

7. **定义提示**：
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - 此字符串设置了一个对话提示，用户请求 AI 助手进行自我介绍。

8. **对提示进行分词**：
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - 此行将提示转换为模型可以处理的标记，并将结果以 PyTorch 张量的形式返回。

9. **生成回复**：
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - 此行使用模型根据输入标记生成回复，最多生成 1024 个新标记。

10. **解码回复**：
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - 此行将生成的标记转换回可读字符串，跳过任何特殊标记，并获取第一个结果。

**免责声明**：  
本文件是使用基于机器的人工智能翻译服务翻译的。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的原始文件作为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用本翻译而导致的任何误解或误读不承担责任。