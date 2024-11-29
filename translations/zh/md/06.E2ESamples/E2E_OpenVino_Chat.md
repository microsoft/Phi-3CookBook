[OpenVino Chat Sample](../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

这个代码将模型导出为OpenVINO格式，加载它，并使用它根据给定的提示生成响应。

1. **导出模型**:
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - 这个命令使用 `optimum-cli` tool to export a model to the OpenVINO format, which is optimized for efficient inference.
   - The model being exported is `"microsoft/Phi-3-mini-4k-instruct"`, and it's set up for the task of generating text based on past context.
   - The weights of the model are quantized to 4-bit integers (`int4`), which helps reduce the model size and speed up processing.
   - Other parameters like `group-size`, `ratio`, and `sym` are used to fine-tune the quantization process.
   - The exported model is saved in the directory `./model/phi3-instruct/int4`。

2. **导入必要的库**:
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - 这些代码行从 `transformers` library and the `optimum.intel.openvino` 模块中导入了需要加载和使用模型的类。

3. **设置模型目录和配置**:
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir` specifies where the model files are stored.
   - `ov_config` 是一个字典，用于配置OpenVINO模型以优先考虑低延迟，使用一个推理流，并且不使用缓存目录。

4. **加载模型**:
   ```python
   ov_model = OVModelForCausalLM.from_pretrained(
       model_dir,
       device='GPU.0',
       ov_config=ov_config,
       config=AutoConfig.from_pretrained(model_dir, trust_remote_code=True),
       trust_remote_code=True,
   )
   ```
   - 这行代码从指定目录加载模型，使用之前定义的配置设置。如果需要，还允许远程代码执行。

5. **加载分词器**:
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - 这行代码加载分词器，它负责将文本转换为模型可以理解的标记。

6. **设置分词器参数**:
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - 这个字典指定在分词输出中不添加特殊标记。

7. **定义提示**:
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - 这个字符串设置了一个对话提示，用户要求AI助手介绍自己。

8. **分词提示**:
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - 这行代码将提示转换为模型可以处理的标记，并将结果作为PyTorch张量返回。

9. **生成响应**:
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - 这行代码使用模型根据输入标记生成响应，最多生成1024个新标记。

10. **解码响应**:
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - 这行代码将生成的标记转换回可读字符串，跳过任何特殊标记，并获取第一个结果。

**免责声明**：
本文件使用基于机器的AI翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原始文件的母语版本视为权威来源。对于关键信息，建议进行专业的人类翻译。对于因使用本翻译而引起的任何误解或误读，我们概不负责。