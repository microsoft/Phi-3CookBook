# MLflow

[MLflow](https://mlflow.org/) 是一个开源平台，旨在管理端到端的机器学习生命周期。

![MLFlow](../../imgs/03/MLflow/MlFlowmlops.png)

MLFlow 用于管理机器学习生命周期，包括实验、可重复性、部署和中央模型注册。MLFlow 目前提供四个组件：

- **MLflow Tracking:** 记录和查询实验、代码、数据配置和结果。
- **MLflow Projects:** 以一种格式打包数据科学代码，以便在任何平台上重现运行。
- **Mlflow Models:** 在不同的服务环境中部署机器学习模型。
- **Model Registry:** 在中央存储库中存储、注释和管理模型。

它包括用于跟踪实验、将代码打包成可重现运行以及共享和部署模型的功能。MLFlow 集成到 Databricks 中，并支持多种机器学习库，使其在库使用上没有限制。它可以与任何机器学习库和任何编程语言一起使用，因为它提供了方便的 REST API 和 CLI 。

![MLFlow](../../imgs/03/MLflow/MLflow2.png)

MLFlow 的主要特点包括：

- **实验跟踪:** 记录和比较参数和结果。
- **模型管理:** 将模型部署到各种服务和推理平台。
- **模型注册表:** 协作管理 MLflow 模型的生命周期，包括版本控制和注释。
- **项目:** 打包机器学习代码以便共享或生产使用。

MLFlow 还支持 MLOps 环路，包括准备数据、注册和管理模型、打包模型以供执行、部署服务和监控模型。它旨在简化从原型到生产工作流的过程，特别是在云和边缘环境中。

## 端到端场景 - 构建包装器并将 Phi-3 作为 MLFlow 模型使用

在这个端到端示例中，我们将展示两种不同的方法来围绕 Phi-3 小型语言模型 (SLM) 构建包装器，然后将其作为 MLFlow 模型在本地或云中运行，例如在 Azure 机器学习工作区中。

![MLFlow](../../imgs/03/MLflow/MlFlow1.png)

| 项目 | 描述 | 位置 |
| ------------ | ----------- | -------- |
| Transformer Pipeline | 如果您希望将 HuggingFace 模型与 MLFlow 实验性的 transformers 一起使用，那么用 Transformer Pipeline 构建包装器是最简单选项。 | [**TransformerPipeline.ipynb**](E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| 自定义 Python 包装器 | 在撰写本文时，transformer pipeline 尚不支持 HuggingFace 模型的 ONNX 格式的 MLFlow 包装器生成，即使使用实验性的 optimum Python 包也不行。在这种情况下，您可以为 MLFlow 模式构建自定义 Python 包装器 | [**CustomPythonWrapper.ipynb**](E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## 项目: Transformer Pipeline
1. 您将需要使用 MLFlow 和 HuggingFace 的相关 Python 包：
``` Python
import mlflow
import transformers
```
2. 接下来，您应该通过引用 HuggingFace 目录中的 Phi-3 模型来启动 transformer pipeline。从 *Phi-3-mini-4k-instruct* 的模型卡可以看出，它是“文本生成”类型的模型：
``` Python
pipeline = transformers.pipeline(
    task = "text-generation",
    model = "microsoft/Phi-3-mini-4k-instruct"
)
```
3. 现在，您可以将 Phi-3 模型的 transformer pipeline 保存为 MLFlow 格式，并设置其他信息，例如目标工件路径、特定模型配置设置和推理 API 类型：
``` Python
model_info = mlflow.transformers.log_model(
    transformers_model = pipeline,
    artifact_path = "phi3-mlflow-model",
    model_config = model_config,
    task = "llm/v1/chat"
)
```

## 项目: 自定义 Python 包装器
1. 我们可以在这里利用微软的 [ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai) 来进行 ONNX 模型的推理和 token 编码/解码。您必须使用 onnxruntime_genai 包来进行相关的计算，下面的示例针对 CPU：

``` Python
import mlflow
from mlflow.models import infer_signature
import onnxruntime_genai as og
```

2. 我们的自定义类实现了两个方法：`load_context()` 以初始化 Phi-3 Mini 4K Instruct 的 **ONNX 模型**、**生成器参数**和 **tokenizer**；`predict()` 将会根据输入的提示生成响应。
``` Python
class Phi3Model(mlflow.pyfunc.PythonModel):
    def load_context(self, context):
        # 从工件中检索模型
        model_path = context.artifacts["phi3-mini-onnx"]
        model_options = {
             "max_length": 300,
             "temperature": 0.2,         
        }
    
        # 定义模型
        self.phi3_model = og.Model(model_path)
        self.params = og.GeneratorParams(self.phi3_model)
        self.params.set_search_options(**model_options)
        
        # 定义 tokenizer
        self.tokenizer = og.Tokenizer(self.phi3_model)

    def predict(self, context, model_input):
        # 从输入中检索提示
        prompt = model_input["prompt"][0]
        self.params.input_ids = self.tokenizer.encode(prompt)

        # 生成模型的响应
        response = self.phi3_model.generate(self.params)

        return self.tokenizer.decode(response[0][len(self.params.input_ids):])
```
3. 现在，您可以使用 `mlflow.pyfunc.log_model()` 函数为 Phi-3 模型生成自定义 Python 包装器（pickle 格式），同时也要设置原始 ONNX 模型和所需的依赖项：
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

## 生成的 MLFlow 模型的签名
1. 在上面 Transformer Pipeline 项目的步骤 3 中，我们将 MLFlow 模型的 `task` 设置为`llm/v1/chat`。这样模型就会接受并返回 OpenAI Chat API 风格的输入和输出。其模式如下：

``` Python
{inputs: 
  ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
outputs: 
  ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
params: 
  None}
```

2. 因此，您可以以下列格式提交您的请求：
``` Python
messages = [{"role": "user", "content": "西班牙的首都是哪里？"}]
```
3. 然后，使用与 OpenAI API 兼容的后处理，例如 _response[0][‘choices’][0][‘message’][‘content’]_，将输出美化成如下所示：
``` JSON
问题：西班牙的首都是哪里？

回答：西班牙的首都是马德里。它是西班牙最大的城市，是国家的政治、经济和文化中心。马德里位于伊比利亚半岛的中心，以其丰富的历史、艺术和建筑而闻名，包括皇宫、普拉多博物馆和马约尔广场。

使用情况: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
```
4. 在上面自定义 Python 包装器的步骤 3 中，我们没有指定 `task`，这允许 MLFlow 自行生成模型的签名，基于给定的输入示例。我们的 MLFlow 包装器的签名将如下所示：
``` Python
{inputs: 
  ['prompt': string (required)],
outputs: 
  [string (required)],
params: 
  None}
```
5. 因此，我们的提示需要包含 "prompt" 字典键，类似于这样：
``` Python
{"prompt": "<|system|>你是一名单口喜剧演员。<|end|><|user|>给我讲一个关于原子的笑话<|end|><|assistant|>",}
```
6. 然后，模型的输出将以字符串格式提供：

``` JSON
好吧，给你讲一个小小的原子相关的笑话！

为什么电子从不和质子玩捉迷藏？

因为当它们总是“共享”电子时，祝你好运找到它们！

记住，这只是开个玩笑，我们只是在享受一点原子级的幽默！
```