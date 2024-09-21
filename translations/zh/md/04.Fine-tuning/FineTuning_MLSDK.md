
它导入了 os 模块，该模块提供了使用与操作系统相关功能的便捷方式。它使用 os.system 函数在 shell 中运行带有特定命令行参数的 download-dataset.py 脚本。参数指定要下载的数据集 (HuggingFaceH4/ultrachat_200k)，下载的目录 (ultrachat_200k_dataset)，以及数据集要拆分的百分比 (5)。os.system 函数返回它执行的命令的退出状态；这个状态被存储在 exit_status 变量中。它检查 exit_status 是否不为 0。在类 Unix 操作系统中，退出状态为 0 通常表示命令成功，而任何其他数字表示错误。如果 exit_status 不为 0，则引发一个异常，提示下载数据集时出错。总之，该脚本使用辅助脚本运行命令下载数据集，如果命令失败，则引发异常。

```
# 导入 os 模块，该模块提供了使用与操作系统相关功能的便捷方式
import os

# 使用 os.system 函数在 shell 中运行带有特定命令行参数的 download-dataset.py 脚本
# 参数指定要下载的数据集 (HuggingFaceH4/ultrachat_200k)，下载的目录 (ultrachat_200k_dataset)，以及数据集要拆分的百分比 (5)
# os.system 函数返回它执行的命令的退出状态；这个状态被存储在 exit_status 变量中
exit_status = os.system(
    "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
)

# 检查 exit_status 是否不为 0
# 在类 Unix 操作系统中，退出状态为 0 通常表示命令成功，而任何其他数字表示错误
# 如果 exit_status 不为 0，则引发一个异常，提示下载数据集时出错
if exit_status != 0:
    raise Exception("Error downloading dataset")
```

### 加载数据到 DataFrame 中
这个 Python 脚本将一个 JSON Lines 文件加载到 pandas DataFrame 中，并显示前 5 行。以下是它的具体操作：

它导入了 pandas 库，这是一个强大的数据操作和分析库。

它将 pandas 的显示选项中的最大列宽设置为 0。这意味着当打印 DataFrame 时，每列的完整文本将被显示而不会被截断。

它使用 pd.read_json 函数将 ultrachat_200k_dataset 目录中的 train_sft.jsonl 文件加载到 DataFrame 中。lines=True 参数表示该文件是 JSON Lines 格式，其中每行是一个单独的 JSON 对象。

它使用 head 方法显示 DataFrame 的前 5 行。如果 DataFrame 少于 5 行，它将显示所有行。

总之，这个脚本将一个 JSON Lines 文件加载到 DataFrame 中，并显示前 5 行的完整列文本。

```
# 导入 pandas 库，这是一个强大的数据操作和分析库
import pandas as pd

# 将 pandas 的显示选项中的最大列宽设置为 0
# 这意味着当打印 DataFrame 时，每列的完整文本将被显示而不会被截断
pd.set_option("display.max_colwidth", 0)

# 使用 pd.read_json 函数将 ultrachat_200k_dataset 目录中的 train_sft.jsonl 文件加载到 DataFrame 中
# lines=True 参数表示该文件是 JSON Lines 格式，其中每行是一个单独的 JSON 对象
df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)

# 使用 head 方法显示 DataFrame 的前 5 行
# 如果 DataFrame 少于 5 行，它将显示所有行
df.head()
```

## 5. 使用模型和数据作为输入提交微调任务
创建使用 chat-completion 管道组件的任务。了解更多关于微调支持的所有参数。

### 定义微调参数

微调参数可以分为两类：训练参数和优化参数

训练参数定义训练方面的内容，例如：

- 使用的优化器、调度器
- 优化微调的指标
- 训练步骤数和批处理大小等
- 优化参数有助于优化 GPU 内存和有效利用计算资源。

以下是属于此类别的一些参数。优化参数因模型而异，并随模型一起打包以处理这些变化。

- 启用 deepspeed 和 LoRA
- 启用混合精度训练
- 启用多节点训练

**注意:** 监督微调可能导致对齐丧失或灾难性遗忘。我们建议在微调后检查此问题并运行对齐阶段。

### 微调参数

这个 Python 脚本设置了微调机器学习模型的参数。以下是它的具体操作：

它设置了默认的训练参数，如训练周期数、训练和评估的批处理大小、学习率和学习率调度器类型。

它设置了默认的优化参数，如是否应用层次相关传播 (LoRa) 和 DeepSpeed，以及 DeepSpeed 阶段。

它将训练和优化参数组合成一个名为 finetune_parameters 的字典。

它检查 foundation_model 是否有任何模型特定的默认参数。如果有，它会打印一条警告消息，并使用这些模型特定的默认值更新 finetune_parameters 字典。ast.literal_eval 函数用于将模型特定的默认值从字符串转换为 Python 字典。

它打印将用于运行的最终微调参数集。

总之，这个脚本设置并显示了微调机器学习模型的参数，并能够使用模型特定的参数覆盖默认参数。

```
# 设置默认的训练参数，如训练周期数、训练和评估的批处理大小、学习率和学习率调度器类型
training_parameters = dict(
    num_train_epochs=3,
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    learning_rate=5e-6,
    lr_scheduler_type="cosine",
)

# 设置默认的优化参数，如是否应用层次相关传播 (LoRa) 和 DeepSpeed，以及 DeepSpeed 阶段
optimization_parameters = dict(
    apply_lora="true",
    apply_deepspeed="true",
    deepspeed_stage=2,
)

# 将训练和优化参数组合成一个名为 finetune_parameters 的字典
finetune_parameters = {**training_parameters, **optimization_parameters}

# 检查 foundation_model 是否有任何模型特定的默认参数
# 如果有，打印一条警告消息，并使用这些模型特定的默认值更新 finetune_parameters 字典
# ast.literal_eval 函数用于将模型特定的默认值从字符串转换为 Python 字典
if "model_specific_defaults" in foundation_model.tags:
    print("Warning! Model specific defaults exist. The defaults could be overridden.")
    finetune_parameters.update(
        ast.literal_eval(  # 将字符串转换为 Python 字典
            foundation_model.tags["model_specific_defaults"]
        )
    )

# 打印将用于运行的最终微调参数集
print(
    f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
)
```

### 训练管道
这个 Python 脚本定义了一个函数来生成机器学习训练管道的显示名称，然后调用这个函数生成并打印显示名称。以下是它的具体操作：

定义了 get_pipeline_display_name 函数。该函数根据与训练管道相关的各种参数生成一个显示名称。

在函数内部，它通过将每设备批处理大小、梯度累积步骤数、每节点 GPU 数量和用于微调的节点数量相乘来计算总批处理大小。

它检索各种其他参数，如学习率调度器类型、是否应用 DeepSpeed、DeepSpeed 阶段、是否应用层次相关传播 (LoRa)、保留的模型检查点数量限制和最大序列长度。

它构建了一个包含所有这些参数的字符串，用连字符分隔。如果应用了 DeepSpeed 或 LoRa，字符串将包含 "ds" 后跟 DeepSpeed 阶段，或 "lora"。如果没有，则分别包含 "nods" 或 "nolora"。

该函数返回这个字符串，作为训练管道的显示名称。

在函数定义后，调用它来生成显示名称，然后打印显示名称。

总之，这个脚本根据各种参数生成机器学习训练管道的显示名称，然后打印这个显示名称。

```
# 定义一个函数来生成训练管道的显示名称
def get_pipeline_display_name():
    # 通过将每设备批处理大小、梯度累积步骤数、每节点 GPU 数量和用于微调的节点数量相乘来计算总批处理大小
    batch_size = (
        int(finetune_parameters.get("per_device_train_batch_size", 1))
        * int(finetune_parameters.get("gradient_accumulation_steps", 1))
        * int(gpus_per_node)
        * int(finetune_parameters.get("num_nodes_finetune", 1))
    )
    # 检索学习率调度器类型
    scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
    # 检索是否应用 DeepSpeed
    deepspeed = finetune_parameters.get("apply_deepspeed", "false")
    # 检索 DeepSpeed 阶段
    ds_stage = finetune_parameters.get("deepspeed_stage", "2")
    # 如果应用了 DeepSpeed，在显示名称中包含 "ds" 后跟 DeepSpeed 阶段；如果没有，则包含 "nods"
    if deepspeed == "true":
        ds_string = f"ds{ds_stage}"
    else:
        ds_string = "nods"
    # 检索是否应用层次相关传播 (LoRa)
    lora = finetune_parameters.get("apply_lora", "false")
    # 如果应用了 LoRa，在显示名称中包含 "lora"；如果没有，则包含 "nolora"
    if lora == "true":
        lora_string = "lora"
    else:
        lora_string = "nolora"
    # 检索保留的模型检查点数量限制
    save_limit = finetune_parameters.get("save_total_limit", -1)
    # 检索最大序列长度
    seq_len = finetune_parameters.get("max_seq_length", -1)
    # 通过连接所有这些参数并用连字符分隔来构建显示名称
    return (
        model_name
        + "-"
        + "ultrachat"
        + "-"
        + f"bs{batch_size}"
        + "-"
        + f"{scheduler}"
        + "-"
        + ds_string
        + "-"
        + lora_string
        + f"-save_limit{save_limit}"
        + f"-seqlen{seq_len}"
    )

# 调用函数生成显示名称
pipeline_display_name = get_pipeline_display_name()
# 打印显示名称
print(f"Display name used for the run: {pipeline_display_name}")
```

### 配置管道

这个 Python 脚本使用 Azure Machine Learning SDK 定义和配置一个机器学习管道。以下是它的具体操作：

1. 它从 Azure AI ML SDK 导入必要的模块。

2. 它从注册表中获取名为 "chat_completion_pipeline" 的管道组件。

3. 它使用 `@pipeline` 装饰器和函数 `create_pipeline` 定义一个管道任务。管道的名称设置为 `pipeline_display_name`。

4. 在 `create_pipeline` 函数内部，它使用各种参数初始化获取的管道组件，包括模型路径、不同阶段的计算集群、训练和测试的数据集拆分、用于微调的 GPU 数量以及其他微调参数。

5. 它将微调任务的输出映射到管道任务的输出。这是为了便于注册微调后的模型，这对于将模型部署到在线或批量端点是必要的。

6. 它通过调用 `create_pipeline` 函数创建管道实例。

7. 它将管道的 `force_rerun` 设置为 `True`，这意味着不会使用以前任务的缓存结果。

8. 它将管道的 `continue_on_step_failure` 设置为 `False`，这意味着如果任何步骤失败，管道将停止。

总之，这个脚本使用 Azure Machine Learning SDK 定义和配置了一个用于聊天完成任务的机器学习管道。

```
# 从 Azure AI ML SDK 导入必要的模块
from azure.ai.ml.dsl import pipeline
from azure.ai.ml import Input

# 从注册表中获取名为 "chat_completion_pipeline" 的管道组件
pipeline_component_func = registry_ml_client.components.get(
    name="chat_completion_pipeline", label="latest"
)

# 使用 @pipeline 装饰器和函数 create_pipeline 定义管道任务
# 管道的名称设置为 pipeline_display_name
@pipeline(name=pipeline_display_name)
def create_pipeline():
    # 使用各种参数初始化获取的管道组件
    # 这些参数包括模型路径、不同阶段的计算集群、训练和测试的数据集拆分、用于微调的 GPU 数量以及其他微调参数
    chat_completion_pipeline = pipeline_component_func(
        mlflow_model_path=foundation_model.id,
        compute_model_import=compute_cluster,
        compute_preprocess=compute_cluster,
        compute_finetune=compute_cluster,
        compute_model_evaluation=compute_cluster,
        # 将数据集拆分映射到参数
        train_file_path=Input(
            type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
        ),
        test_file_path=Input(
            type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
        ),
        # 训练设置
        number_of_gpu_to_use_finetuning=gpus_per_node,  # 设置为计算资源中可用的 GPU 数量
        **finetune_parameters
    )
    return {
        # 将微调任务的输出映射到管道任务的输出
        # 这样做是为了便于注册微调后的模型
        # 注册模型是将模型部署到在线或批量端点的必要步骤
        "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
    }

# 通过调用 create_pipeline 函数创建管道实例
pipeline_object = create_pipeline()

# 不使用以前任务的缓存结果
pipeline_object.settings.force_rerun = True

# 设置继续步骤失败为 False
# 这意味着如果任何步骤失败，管道将停止
pipeline_object.settings.continue_on_step_failure = False
```

### 提交任务

这个 Python 脚本将机器学习管道任务提交到 Azure Machine Learning 工作区，然后等待任务完成。以下是它的具体操作：

它调用 workspace_ml_client 中 jobs 对象的 create_or_update 方法来提交管道任务。要运行的管道由 pipeline_object 指定，任务所在的实验由 experiment_name 指定。

然后它调用 workspace_ml_client 中 jobs 对象的 stream 方法来等待管道任务完成。要等待的任务由 pipeline_job 对象的 name 属性指定。

总之，这个脚本将机器学习管道任务提交到 Azure Machine Learning 工作区，然后等待任务完成。

```
# 将管道任务提交到 Azure Machine Learning 工作区
# 要运行的管道由 pipeline_object 指定
# 任务所在的实验由 experiment_name 指定
pipeline_job = workspace_ml_client.jobs.create_or_update(
    pipeline_object, experiment_name=experiment_name
)

# 等待管道任务完成
# 要等待的任务由 pipeline_job 对象的 name 属性指定
workspace_ml_client.jobs.stream(pipeline_job.name)
```

## 6. 将微调后的模型注册到工作区
我们将从微调任务的输出中注册模型。这将跟踪微调模型与微调任务之间的关系。微调任务进一步跟踪基础模型、数据和训练代码的关系。

### 注册机器学习模型
这个 Python 脚本将一个在 Azure Machine Learning 管道中训练的机器学习模型注册到工作区。以下是它的具体操作：

它从 Azure AI ML SDK 导入必要的模块。

它通过调用 workspace_ml_client 中 jobs 对象的 get 方法并访问其 outputs 属性来检查 pipeline_job 是否有 trained_model 输出。

它通过格式化一个包含 pipeline_job 名称和输出名称（"trained_model"）的字符串来构建模型的路径。

它通过将 "-ultrachat-200k" 附加到原始模型名称并将任何斜杠替换为连字符来定义微调模型的名称。

它准备注册模型，通过创建一个 Model 对象，并设置各种参数，包括模型的路径、模型的类型（MLflow 模型）、模型的名称和版本以及模型的描述。

它通过调用 workspace_ml_client 中 models 对象的 create_or_update 方法并传入 Model 对象来注册模型。

它打印注册的模型。

总之，这个脚本将一个在 Azure Machine Learning 管道中训练的机器学习模型注册到工作区。
```
# 从 Azure AI ML SDK 导入必要的模块
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes

# 检查 `trained_model` 输出是否可用
print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)

# 构建一个路径，通过格式化字符串，包含 pipeline job 的名称和输出的名称 ("trained_model")
model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
    pipeline_job.name, "trained_model"
)

# 通过在原始模型名称后附加 "-ultrachat-200k" 并将任何斜杠替换为连字符，定义微调模型的名称
finetuned_model_name = model_name + "-ultrachat-200k"
finetuned_model_name = finetuned_model_name.replace("/", "-")

print("path to register model: ", model_path_from_job)

# 通过创建一个 Model 对象，准备注册模型
# 这些参数包括模型的路径、模型的类型（MLflow 模型）、模型的名称和版本，以及模型的描述
prepare_to_register_model = Model(
    path=model_path_from_job,
    type=AssetTypes.MLFLOW_MODEL,
    name=finetuned_model_name,
    version=timestamp,  # 使用时间戳作为版本以避免版本冲突
    description=model_name + " fine tuned model for ultrachat 200k chat-completion",
)

print("prepare to register model: \n", prepare_to_register_model)

# 通过调用 workspace_ml_client 的 models 对象的 create_or_update 方法，注册模型，参数为 Model 对象
registered_model = workspace_ml_client.models.create_or_update(
    prepare_to_register_model
)

# 打印注册的模型
print("registered model: \n", registered_model)
```
## 7. 部署微调模型到在线端点
在线端点提供了一个持久的REST API，可以用于集成需要使用模型的应用程序。

### 管理端点
这个Python脚本在Azure Machine Learning中为一个注册模型创建一个托管在线端点。以下是它的功能分解：

它从Azure AI ML SDK中导入了必要的模块。

它通过在字符串“ultrachat-completion-”后附加一个时间戳来定义在线端点的唯一名称。

它准备创建在线端点，通过创建一个包含各种参数的ManagedOnlineEndpoint对象，这些参数包括端点的名称、描述和认证模式（“key”）。

它通过调用workspace_ml_client的begin_create_or_update方法并传入ManagedOnlineEndpoint对象作为参数来创建在线端点。然后通过调用wait方法等待创建操作完成。

总的来说，这个脚本是在Azure Machine Learning中为一个注册模型创建一个托管在线端点。

```
# 从Azure AI ML SDK导入必要的模块
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    ProbeSettings,
    OnlineRequestSettings,
)

# 通过在字符串“ultrachat-completion-”后附加一个时间戳来定义在线端点的唯一名称
online_endpoint_name = "ultrachat-completion-" + timestamp

# 准备创建在线端点，通过创建一个包含各种参数的ManagedOnlineEndpoint对象
# 这些参数包括端点的名称、描述和认证模式（“key”）
endpoint = ManagedOnlineEndpoint(
    name=online_endpoint_name,
    description="Online endpoint for "
    + registered_model.name
    + ", fine tuned model for ultrachat-200k-chat-completion",
    auth_mode="key",
)

# 通过调用workspace_ml_client的begin_create_or_update方法并传入ManagedOnlineEndpoint对象作为参数来创建在线端点
# 然后通过调用wait方法等待创建操作完成
workspace_ml_client.begin_create_or_update(endpoint).wait()
```
你可以在这里找到支持部署的SKU列表 - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### 部署机器学习模型

这个Python脚本将一个注册的机器学习模型部署到Azure Machine Learning中的托管在线端点。以下是它的功能分解：

它导入了ast模块，该模块提供处理Python抽象语法树的函数。

它将部署的实例类型设置为“Standard_NC6s_v3”。

它检查基础模型中是否存在inference_compute_allow_list标签。如果存在，它将标签值从字符串转换为Python列表并赋值给inference_computes_allow_list。如果不存在，它将inference_computes_allow_list设置为None。

它检查指定的实例类型是否在允许列表中。如果不在，它会打印一条消息，要求用户从允许列表中选择一个实例类型。

它准备创建部署，通过创建一个包含各种参数的ManagedOnlineDeployment对象，这些参数包括部署的名称、端点的名称、模型的ID、实例类型和数量、存活探测设置以及请求设置。

它通过调用workspace_ml_client的begin_create_or_update方法并传入ManagedOnlineDeployment对象作为参数来创建部署。然后通过调用wait方法等待创建操作完成。

它将端点的流量设置为100%指向“demo”部署。

它通过调用workspace_ml_client的begin_create_or_update方法并传入endpoint对象作为参数来更新端点。然后通过调用result方法等待更新操作完成。

总的来说，这个脚本是在Azure Machine Learning中将一个注册的机器学习模型部署到一个托管在线端点。

```
# 导入ast模块，该模块提供处理Python抽象语法树的函数
import ast

# 设置部署的实例类型
instance_type = "Standard_NC6s_v3"

# 检查基础模型中是否存在`inference_compute_allow_list`标签
if "inference_compute_allow_list" in foundation_model.tags:
    # 如果存在，将标签值从字符串转换为Python列表并赋值给`inference_computes_allow_list`
    inference_computes_allow_list = ast.literal_eval(
        foundation_model.tags["inference_compute_allow_list"]
    )
    print(f"Please create a compute from the above list - {computes_allow_list}")
else:
    # 如果不存在，将`inference_computes_allow_list`设置为`None`
    inference_computes_allow_list = None
    print("`inference_compute_allow_list` is not part of model tags")

# 检查指定的实例类型是否在允许列表中
if (
    inference_computes_allow_list is not None
    and instance_type not in inference_computes_allow_list
):
    print(
        f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
    )

# 准备创建部署，通过创建一个包含各种参数的`ManagedOnlineDeployment`对象
demo_deployment = ManagedOnlineDeployment(
    name="demo",
    endpoint_name=online_endpoint_name,
    model=registered_model.id,
    instance_type=instance_type,
    instance_count=1,
    liveness_probe=ProbeSettings(initial_delay=600),
    request_settings=OnlineRequestSettings(request_timeout_ms=90000),
)

# 通过调用`workspace_ml_client`的`begin_create_or_update`方法并传入`ManagedOnlineDeployment`对象作为参数来创建部署
# 然后通过调用`wait`方法等待创建操作完成
workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()

# 将端点的流量设置为100%指向“demo”部署
endpoint.traffic = {"demo": 100}

# 通过调用`workspace_ml_client`的`begin_create_or_update`方法并传入`endpoint`对象作为参数来更新端点
# 然后通过调用`result`方法等待更新操作完成
workspace_ml_client.begin_create_or_update(endpoint).result()
```
## 8. 使用示例数据测试端点
我们将从测试数据集中获取一些示例数据并提交到在线端点进行推理。然后我们将显示得分标签和真实标签。

### 读取结果
这个Python脚本将一个JSON Lines文件读取到一个pandas DataFrame中，随机抽取一行样本，并重置索引。以下是它的功能分解：

它将文件./ultrachat_200k_dataset/test_gen.jsonl读取到一个pandas DataFrame中。由于文件是JSON Lines格式，每行是一个单独的JSON对象，因此使用了lines=True参数。

它从DataFrame中随机抽取一行样本。使用sample函数并指定n=1参数来选择随机行的数量。

它重置DataFrame的索引。使用reset_index函数并指定drop=True参数来丢弃原始索引并用新的默认整数值索引替换。

它使用head函数并指定参数2来显示DataFrame的前两行。然而，由于采样后DataFrame只包含一行，因此只会显示这一行。

总的来说，这个脚本将一个JSON Lines文件读取到一个pandas DataFrame中，随机抽取一行样本，重置索引，并显示第一行。

```
# 导入pandas库
import pandas as pd

# 将JSON Lines文件'./ultrachat_200k_dataset/test_gen.jsonl'读取到一个pandas DataFrame中
# 'lines=True'参数表示文件是JSON Lines格式，每行是一个单独的JSON对象
test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)

# 从DataFrame中随机抽取一行样本
# 'n=1'参数指定选择的随机行数
test_df = test_df.sample(n=1)

# 重置DataFrame的索引
# 'drop=True'参数表示应该丢弃原始索引并用新的默认整数值索引替换
# 'inplace=True'参数表示应该就地修改DataFrame（不创建新对象）
test_df.reset_index(drop=True, inplace=True)

# 显示DataFrame的前两行
# 然而，由于采样后DataFrame只包含一行，因此只会显示这一行
test_df.head(2)
```
### 创建JSON对象

这个Python脚本创建一个带有特定参数的JSON对象并将其保存到文件中。以下是它的功能分解：

它导入了json模块，该模块提供处理JSON数据的函数。

它创建了一个字典parameters，包含表示机器学习模型参数的键和值。键为“temperature”、“top_p”、“do_sample”和“max_new_tokens”，对应的值分别为0.6、0.9、True和200。

它创建了另一个字典test_json，包含两个键：“input_data”和“params”。“input_data”的值是另一个包含“input_string”和“parameters”键的字典。“input_string”的值是一个包含来自test_df DataFrame的第一条消息的列表。“parameters”的值是之前创建的parameters字典。“params”的值是一个空字典。

它打开一个名为sample_score.json的文件，并将test_json字典以JSON格式写入文件中。

```
# 导入json模块，该模块提供处理JSON数据的函数
import json

# 创建一个字典`parameters`，包含表示机器学习模型参数的键和值
# 键为"temperature"、"top_p"、"do_sample"和"max_new_tokens"，对应的值分别为0.6、0.9、True和200
parameters = {
    "temperature": 0.6,
    "top_p": 0.9,
    "do_sample": True,
    "max_new_tokens": 200,
}

# 创建另一个字典`test_json`，包含两个键："input_data"和"params"
# "input_data"的值是另一个包含"input_string"和"parameters"键的字典
# "input_string"的值是一个包含来自`test_df` DataFrame的第一条消息的列表
# "parameters"的值是之前创建的`parameters`字典
# "params"的值是一个空字典
test_json = {
    "input_data": {
        "input_string": [test_df["messages"][0]],
        "parameters": parameters,
    },
    "params": {},
}

# 打开一个名为`sample_score.json`的文件，并将`test_json`字典以JSON格式写入文件中
with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
    json.dump(test_json, f)
```
### 调用端点

这个Python脚本调用Azure Machine Learning中的一个在线端点来对一个JSON文件进行评分。以下是它的功能分解：

它调用workspace_ml_client对象的online_endpoints属性的invoke方法。该方法用于向在线端点发送请求并获取响应。

它通过endpoint_name和deployment_name参数指定端点和部署的名称。在本例中，端点名称存储在online_endpoint_name变量中，部署名称为“demo”。

它通过request_file参数指定要评分的JSON文件的路径。在本例中，文件路径为./ultrachat_200k_dataset/sample_score.json。

它将端点的响应存储在response变量中。

它打印原始响应。

总的来说，这个脚本调用Azure Machine Learning中的一个在线端点来对一个JSON文件进行评分并打印响应。

```
# 调用Azure Machine Learning中的在线端点来对`sample_score.json`文件进行评分
# `invoke`方法用于向在线端点发送请求并获取响应
# `endpoint_name`参数指定端点的名称，存储在`online_endpoint_name`变量中
# `deployment_name`参数指定部署的名称，为"demo"
# `request_file`参数指定要评分的JSON文件的路径，为`./ultrachat_200k_dataset/sample_score.json`
response = workspace_ml_client.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    deployment_name="demo",
    request_file="./ultrachat_200k_dataset/sample_score.json",
)

# 打印端点的原始响应
print("raw response: \n", response, "\n")
```
## 9. 删除在线端点
别忘了删除在线端点，否则你会为端点使用的计算资源继续计费。以下这行Python代码是在Azure Machine Learning中删除一个在线端点。以下是它的功能分解：

它调用workspace_ml_client对象的online_endpoints属性的begin_delete方法。该方法用于启动在线端点的删除操作。

它通过name参数指定要删除的端点的名称。在本例中，端点名称存储在online_endpoint_name变量中。

它调用wait方法等待删除操作完成。这是一个阻塞操作，意味着在删除完成之前脚本将不会继续执行。

总的来说，这行代码是在Azure Machine Learning中启动在线端点的删除操作并等待操作完成。

```
# 删除Azure Machine Learning中的在线端点
# `begin_delete`方法用于启动在线端点的删除操作
# `name`参数指定要删除的端点的名称，存储在`online_endpoint_name`变量中
# `wait`方法用于等待删除操作完成。这是一个阻塞操作，意味着在删除完成之前脚本将不会继续执行
workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
```

免责声明：本翻译由AI模型从原文翻译而来，可能并不完美。请审阅输出并进行必要的修改。