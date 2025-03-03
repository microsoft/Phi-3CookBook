# MLflow

[MLflow](https://mlflow.org/) 是一个开源平台，旨在管理端到端的机器学习生命周期。

![MLFlow](../../../../../../translated_images/MlFlowmlops.e5d74ef39e988d267f5da3174105d728e556b25cee7d686689174acb1f07a11a.zh.png)

MLflow 用于管理机器学习生命周期，包括实验、可重复性、部署以及一个集中式模型注册表。目前，MLflow 提供四个组件：

- **MLflow Tracking：** 记录和查询实验、代码、数据配置和结果。
- **MLflow Projects：** 将数据科学代码打包成可在任何平台上重现运行的格式。
- **MLflow Models：** 在多种服务环境中部署机器学习模型。
- **Model Registry：** 在集中式存储库中存储、注释和管理模型。

它具备跟踪实验、将代码打包成可重复运行的形式，以及共享和部署模型的能力。MLflow 集成到 Databricks 中，并支持多种机器学习库，使其具有库无关性。通过提供 REST API 和 CLI，MLflow 可用于任何机器学习库和编程语言。

![MLFlow](../../../../../../translated_images/MLflow2.74e3f1a430b83b5379854d81f4d2d125b6e5a0f35f46b57625761d1f0597bc53.zh.png)

MLflow 的主要功能包括：

- **实验跟踪：** 记录和比较参数及结果。
- **模型管理：** 将模型部署到各种服务和推理平台。
- **模型注册表：** 协作管理 MLflow 模型的生命周期，包括版本控制和注释。
- **项目：** 将机器学习代码打包用于共享或生产环境。

MLflow 还支持 MLOps 循环，包括准备数据、注册和管理模型、打包模型以供执行、部署服务以及监控模型。它旨在简化从原型到生产工作流的过程，特别是在云和边缘环境中。

## 端到端场景 - 构建封装器并将 Phi-3 作为 MLflow 模型使用

在这个端到端示例中，我们将展示两种不同的方法来围绕 Phi-3 小型语言模型（SLM）构建封装器，然后将其作为 MLflow 模型在本地或云端（例如 Azure Machine Learning 工作区）运行。

![MLFlow](../../../../../../translated_images/MlFlow1.03b29de8b4a8f3706a3e7b229c94a81ece6e3ba983c78592ed332f3ef6efcfe0.zh.png)

| 项目 | 描述 | 位置 |
| ------------ | ----------- | -------- |
| Transformer Pipeline | 如果您希望使用 HuggingFace 模型与 MLflow 的实验性 transformers 功能，Transformer Pipeline 是构建封装器的最简单选项。 | [**TransformerPipeline.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| 自定义 Python 封装器 | 在撰写本文时，Transformer Pipeline 尚不支持为 ONNX 格式的 HuggingFace 模型生成 MLflow 封装器，即使使用了实验性的 optimum Python 包。对于这种情况，您可以为 MLflow 模式构建自定义 Python 封装器。 | [**CustomPythonWrapper.ipynb**](../../../../../../code/06.E2E/E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## 项目：Transformer Pipeline

1. 您需要从 MLflow 和 HuggingFace 获取相关的 Python 包：

    ``` Python
    import mlflow
    import transformers
    ```

2. 接下来，您需要通过 HuggingFace 注册表引用目标 Phi-3 模型来初始化一个 transformer pipeline。如 _Phi-3-mini-4k-instruct_ 的模型卡所示，其任务类型为“文本生成”：

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. 现在，您可以将 Phi-3 模型的 transformer pipeline 保存为 MLflow 格式，并提供额外的细节，如目标工件路径、特定模型配置设置和推理 API 类型：

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## 项目：自定义 Python 封装器

1. 在这里我们可以利用微软的 [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) 进行 ONNX 模型的推理以及令牌编码/解码。您需要选择适合目标计算环境的 _onnxruntime_genai_ 包，以下示例针对 CPU：

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

2. 我们的自定义类实现了两个方法：_load_context()_ 用于初始化 **Phi-3 Mini 4K Instruct 的 ONNX 模型**、**生成器参数**和**tokenizer**；_predict()_ 用于根据提供的提示生成输出令牌：

    ``` Python
    class Phi3Model(mlflow.pyfunc.PythonModel):
        def load_context(self, context):
            # Retrieving model from the artifacts
            model_path = context.artifacts["phi3-mini-onnx"]
            model_options = {
                 "max_length": 300,
                 "temperature": 0.2,         
            }
        
            # Defining the model
            self.phi3_model = og.Model(model_path)
            self.params = og.GeneratorParams(self.phi3_model)
            self.params.set_search_options(**model_options)
            
            # Defining the tokenizer
            self.tokenizer = og.Tokenizer(self.phi3_model)
    
        def predict(self, context, model_input):
            # Retrieving prompt from the input
            prompt = model_input["prompt"][0]
            self.params.input_ids = self.tokenizer.encode(prompt)
    
            # Generating the model's response
            response = self.phi3_model.generate(self.params)
    
            return self.tokenizer.decode(response[0][len(self.params.input_ids):])
    ```

3. 现在，您可以使用 _mlflow.pyfunc.log_model()_ 函数为 Phi-3 模型生成一个自定义 Python 封装器（pickle 格式），以及原始 ONNX 模型和所需的依赖项：

    ``` Python
    model_info = mlflow.pyfunc.log_model(
        artifact_path = artifact_path,
        python_model = Phi3Model(),
        artifacts = {
            "phi3-mini-onnx": "cpu_and_mobile/cpu-int4-rtn-block-32-acc-level-4",
        },
        input_example = input_example,
        signature = infer_signature(input_example, ["Run"]),
        extra_pip_requirements = ["torch", "onnxruntime_genai", "numpy"],
    )
    ```

## 生成的 MLflow 模型的签名

1. 在上文 Transformer Pipeline 项目的第 3 步中，我们将 MLflow 模型的任务设置为“_llm/v1/chat_”。这样的指令会生成一个与 OpenAI 的 Chat API 兼容的模型 API 封装器，如下所示：

    ``` Python
    {inputs: 
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs: 
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params: 
      None}
    ```

2. 因此，您可以以以下格式提交您的提示：

    ``` Python
    messages = [{"role": "user", "content": "What is the capital of Spain?"}]
    ```

3. 然后，使用与 OpenAI API 兼容的后处理，例如 _response[0][‘choices’][0][‘message’][‘content’]_，将输出美化为类似以下内容：

    ``` JSON
    Question: What is the capital of Spain?
    
    Answer: The capital of Spain is Madrid. It is the largest city in Spain and serves as the political, economic, and cultural center of the country. Madrid is located in the center of the Iberian Peninsula and is known for its rich history, art, and architecture, including the Royal Palace, the Prado Museum, and the Plaza Mayor.
    
    Usage: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

4. 在上文自定义 Python 封装器项目的第 3 步中，我们允许 MLflow 包根据给定的输入示例生成模型的签名。我们的 MLflow 封装器的签名如下所示：

    ``` Python
    {inputs: 
      ['prompt': string (required)],
    outputs: 
      [string (required)],
    params: 
      None}
    ```

5. 因此，我们的提示需要包含 "prompt" 字典键，类似于以下内容：

    ``` Python
    {"prompt": "<|system|>You are a stand-up comedian.<|end|><|user|>Tell me a joke about atom<|end|><|assistant|>",}
    ```

6. 然后，模型的输出将以字符串格式提供：

    ``` JSON
    Alright, here's a little atom-related joke for you!
    
    Why don't electrons ever play hide and seek with protons?
    
    Because good luck finding them when they're always "sharing" their electrons!
    
    Remember, this is all in good fun, and we're just having a little atomic-level humor!
    ```

**免责声明**：  
本文档使用基于机器的AI翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的原始文档作为权威来源。对于关键信息，建议使用专业的人类翻译服务。对于因使用本翻译而导致的任何误解或误读，我们不承担任何责任。