[OpenVino Chat Sample](../../../../code/06.E2E/E2E_OpenVino_Chat_Phi3-instruct.ipynb)

这段代码将模型导出为OpenVINO格式，加载它，并使用它根据给定的提示生成响应。

1. **导出模型**：
   ```bash
   optimum-cli export openvino --model "microsoft/Phi-3-mini-4k-instruct" --task text-generation-with-past --weight-format int4 --group-size 128 --ratio 0.6 --sym --trust-remote-code ./model/phi3-instruct/int4
   ```
   - 这个命令使用`optimum-cli`工具将模型导出为OpenVINO格式，该格式针对高效推理进行了优化。
   - 被导出的模型是`"microsoft/Phi-3-mini-4k-instruct"`，并且它被设置为基于过去的上下文生成文本的任务。
   - 模型的权重被量化为4位整数（`int4`），这有助于减小模型大小并加快处理速度。
   - 其他参数如`group-size`、`ratio`和`sym`用于微调量化过程。
   - 导出的模型保存在目录`./model/phi3-instruct/int4`中。

2. **导入必要的库**：
   ```python
   from transformers import AutoConfig, AutoTokenizer
   from optimum.intel.openvino import OVModelForCausalLM
   ```
   - 这些行从`transformers`库和`optimum.intel.openvino`模块中导入了类，这些类是加载和使用模型所需的。

3. **设置模型目录和配置**：
   ```python
   model_dir = './model/phi3-instruct/int4'
   ov_config = {
       "PERFORMANCE_HINT": "LATENCY",
       "NUM_STREAMS": "1",
       "CACHE_DIR": ""
   }
   ```
   - `model_dir`指定了模型文件的存储位置。
   - `ov_config`是一个字典，配置OpenVINO模型优先低延迟，使用一个推理流，并且不使用缓存目录。

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
   - 这行代码使用之前定义的配置设置从指定目录加载模型。它还允许远程代码执行（如果必要的话）。

5. **加载分词器**：
   ```python
   tok = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)
   ```
   - 这行代码加载分词器，分词器负责将文本转换为模型可以理解的tokens。

6. **设置分词器参数**：
   ```python
   tokenizer_kwargs = {
       "add_special_tokens": False
   }
   ```
   - 这个字典指定在分词输出中不添加特殊tokens。

7. **定义提示**：
   ```python
   prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>can you introduce yourself?<|end|><|assistant|>"
   ```
   - 这个字符串设置了一个对话提示，其中用户要求AI助手介绍自己。

8. **对提示进行分词**：
   ```python
   input_tokens = tok(prompt, return_tensors="pt", **tokenizer_kwargs)
   ```
   - 这行代码将提示转换为模型可以处理的tokens，并返回结果作为PyTorch张量。

9. **生成响应**：
   ```python
   answer = ov_model.generate(**input_tokens, max_new_tokens=1024)
   ```
   - 这行代码使用模型根据输入tokens生成响应，最多生成1024个新tokens。

10. **解码响应**：
    ```python
    decoded_answer = tok.batch_decode(answer, skip_special_tokens=True)[0]
    ```
    - 这行代码将生成的tokens转换回人类可读的字符串，跳过任何特殊tokens，并获取第一个结果。

免责声明：该翻译由人工智能模型从原文翻译而来，可能不完美。请审核输出内容并进行必要的修改。