
它导入了os模块，该模块提供了一种使用与操作系统相关功能的便捷方式。它使用os.system函数在shell中运行download-dataset.py脚本，并带有特定的命令行参数。参数指定了要下载的数据集（HuggingFaceH4/ultrachat_200k）、下载目录（ultrachat_200k_dataset）以及数据集要分割的百分比（5）。os.system函数返回它执行的命令的退出状态；这个状态存储在exit_status变量中。它检查exit_status是否不为0。在类Unix操作系统中，退出状态为0通常表示命令成功，而其他任何数字表示错误。如果exit_status不为0，它会抛出一个异常，并显示一条消息，指示下载数据集时出错。总之，这个脚本运行一个命令来使用辅助脚本下载数据集，如果命令失败则抛出异常。

```
# 导入os模块，该模块提供了一种使用与操作系统相关功能的便捷方式
import os

# 使用os.system函数在shell中运行download-dataset.py脚本，并带有特定的命令行参数
# 参数指定了要下载的数据集（HuggingFaceH4/ultrachat_200k）、下载目录（ultrachat_200k_dataset）以及数据集要分割的百分比（5）
# os.system函数返回它执行的命令的退出状态；这个状态存储在exit_status变量中
exit_status = os.system(
    "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
)

# 检查exit_status是否不为0
# 在类Unix操作系统中，退出状态为0通常表示命令成功，而其他任何数字表示错误
# 如果exit_status不为0，抛出一个异常，并显示一条消息，指示下载数据集时出错
if exit_status != 0:
    raise Exception("Error downloading dataset")
```

### 加载数据到DataFrame
这个Python脚本将一个JSON Lines文件加载到pandas DataFrame中，并显示前5行。以下是它的工作流程：

它导入了pandas库，这是一个强大的数据处理和分析库。

它将pandas的显示选项中的最大列宽设置为0。这意味着在打印DataFrame时，每一列的完整文本将显示而不会被截断。

它使用pd.read_json函数将ultrachat_200k_dataset目录中的train_sft.jsonl文件加载到DataFrame中。参数lines=True表示该文件是JSON Lines格式，每一行都是一个独立的JSON对象。

它使用head方法显示DataFrame的前5行。如果DataFrame少于5行，它将显示所有行。

总之，这个脚本将一个JSON Lines文件加载到DataFrame中，并显示前5行的完整列文本。

```
# 导入pandas库，这是一个强大的数据处理和分析库
import pandas as pd

# 将pandas的显示选项中的最大列宽设置为0
# 这意味着在打印DataFrame时，每一列的完整文本将显示而不会被截断
pd.set_option("display.max_colwidth", 0)

# 使用pd.read_json函数将ultrachat_200k_dataset目录中的train_sft.jsonl文件加载到DataFrame中
# 参数lines=True表示该文件是JSON Lines格式，每一行都是一个独立的JSON对象
df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)

# 使用head方法显示DataFrame的前5行
# 如果DataFrame少于5行，它将显示所有行
df.head()
```

## 5. 提交微调任务，使用模型和数据作为输入
创建一个使用chat-completion管道组件的任务。了解更多关于微调支持的所有参数。

### 定义微调参数

微调参数可以分为两类——训练参数和优化参数

训练参数定义了训练的各个方面，例如：

- 要使用的优化器和调度器
- 要优化的微调指标
- 训练步骤数、批次大小等
- 优化参数有助于优化GPU内存和有效利用计算资源。

以下是一些属于此类别的参数。每个模型的优化参数不同，并与模型一起打包以处理这些变化。

- 启用deepspeed和LoRA
- 启用混合精度训练
- 启用多节点训练

**注意：** 监督微调可能会导致对齐丢失或灾难性遗忘。我们建议在微调后检查此问题并运行对齐阶段。

### 微调参数

这个Python脚本正在设置微调机器学习模型的参数。以下是它的工作流程：

它设置了一些默认的训练参数，如训练轮数、训练和评估的批次大小、学习率以及学习率调度器类型。

它设置了一些默认的优化参数，如是否应用层次相关传播（LoRa）和DeepSpeed，以及DeepSpeed阶段。

它将训练和优化参数组合成一个名为finetune_parameters的字典。

它检查foundation_model是否有任何模型特定的默认参数。如果有，它会打印一个警告消息，并使用这些模型特定的默认参数更新finetune_parameters字典。ast.literal_eval函数用于将模型特定的默认参数从字符串转换为Python字典。

它打印将用于运行的最终微调参数集。

总之，这个脚本正在设置和显示微调机器学习模型的参数，并能够使用模型特定的参数覆盖默认参数。

```
# 设置一些默认的训练参数，如训练轮数、训练和评估的批次大小、学习率以及学习率调度器类型
training_parameters = dict(
    num_train_epochs=3,
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    learning_rate=5e-6,
    lr_scheduler_type="cosine",
)

# 设置一些默认的优化参数，如是否应用层次相关传播（LoRa）和DeepSpeed，以及DeepSpeed阶段
optimization_parameters = dict(
    apply_lora="true",
    apply_deepspeed="true",
    deepspeed_stage=2,
)

# 将训练和优化参数组合成一个名为finetune_parameters的字典
finetune_parameters = {**training_parameters, **optimization_parameters}

# 检查foundation_model是否有任何模型特定的默认参数
# 如果有，打印一个警告消息，并使用这些模型特定的默认参数更新finetune_parameters字典
# ast.literal_eval函数用于将模型特定的默认参数从字符串转换为Python字典
if "model_specific_defaults" in foundation_model.tags:
    print("Warning! Model specific defaults exist. The defaults could be overridden.")
    finetune_parameters.update(
        ast.literal_eval(  # 将字符串转换为python字典
            foundation_model.tags["model_specific_defaults"]
        )
    )

# 打印将用于运行的最终微调参数集
print(
    f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
)
```

### 训练管道
这个Python脚本定义了一个生成机器学习训练管道显示名称的函数，然后调用该函数生成并打印显示名称。以下是它的工作流程：

定义了get_pipeline_display_name函数。这个函数根据与训练管道相关的各种参数生成显示名称。

在函数内部，它通过将每个设备的批次大小、梯度累积步骤数、每个节点的GPU数量和用于微调的节点数量相乘来计算总批次大小。

它检索各种其他参数，如学习率调度器类型、是否应用DeepSpeed、DeepSpeed阶段、是否应用层次相关传播（LoRa）、要保留的模型检查点数量限制以及最大序列长度。

它构建了一个包含所有这些参数的字符串，参数之间用连字符分隔。如果应用了DeepSpeed或LoRa，字符串将包含"ds"后跟DeepSpeed阶段，或"lora"。如果没有应用，则分别包含"nods"或"nolora"。

该函数返回此字符串，作为训练管道的显示名称。

在定义函数后，它被调用以生成显示名称，然后打印该显示名称。

总之，这个脚本根据各种参数生成机器学习训练管道的显示名称，然后打印该显示名称。

```
# 定义一个生成训练管道显示名称的函数
def get_pipeline_display_name():
    # 通过将每个设备的批次大小、梯度累积步骤数、每个节点的GPU数量和用于微调的节点数量相乘来计算总批次大小
    batch_size = (
        int(finetune_parameters.get("per_device_train_batch_size", 1))
        * int(finetune_parameters.get("gradient_accumulation_steps", 1))
        * int(gpus_per_node)
        * int(finetune_parameters.get("num_nodes_finetune", 1))
    )
    # 检索学习率调度器类型
    scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
    # 检索是否应用DeepSpeed
    deepspeed = finetune_parameters.get("apply_deepspeed", "false")
    # 检索DeepSpeed阶段
    ds_stage = finetune_parameters.get("deepspeed_stage", "2")
    # 如果应用了DeepSpeed，在显示名称中包含"ds"后跟DeepSpeed阶段；如果没有应用，包含"nods"
    if deepspeed == "true":
        ds_string = f"ds{ds_stage}"
    else:
        ds_string = "nods"
    # 检索是否应用层次相关传播（LoRa）
    lora = finetune_parameters.get("apply_lora", "false")
    # 如果应用了LoRa，在显示名称中包含"lora"；如果没有应用，包含"nolora"
    if lora == "true":
        lora_string = "lora"
    else:
        lora_string = "nolora"
    # 检索要保留的模型检查点数量限制
    save_limit = finetune_parameters.get("save_total_limit", -1)
    # 检索最大序列长度
    seq_len = finetune_parameters.get("max_seq_length", -1)
    # 通过连接所有这些参数构建显示名称，参数之间用连字符分隔
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

这个Python脚本使用Azure Machine Learning SDK定义和配置一个机器学习管道。以下是它的工作流程：

1. 它从Azure AI ML SDK中导入必要的模块。

2. 它从注册表中获取名为"chat_completion_pipeline"的管道组件。

3. 它使用`@pipeline`装饰器和`create_pipeline`函数定义一个管道任务。管道的名称设置为`pipeline_display_name`。

4. 在`create_pipeline`函数中，它使用各种参数初始化获取的管道组件，包括模型路径、不同阶段的计算集群、训练和测试的数据集分割、用于微调的GPU数量以及其他微调参数。

5. 它将微调任务的输出映射到管道任务的输出。这是为了便于注册微调后的模型，这对于将模型部署到在线或批处理端点是必要的。

6. 它通过调用`create_pipeline`函数创建管道实例。

7. 它将管道的`force_rerun`设置为`True`，这意味着不会使用先前任务的缓存结果。

8. 它将管道的`continue_on_step_failure`设置为`False`，这意味着如果任何步骤失败，管道将停止。

总之，这个脚本使用Azure Machine Learning SDK定义和配置了一个用于聊天完成任务的机器学习管道。

```
# 从Azure AI ML SDK中导入必要的模块
from azure.ai.ml.dsl import pipeline
from azure.ai.ml import Input

# 从注册表中获取名为"chat_completion_pipeline"的管道组件
pipeline_component_func = registry_ml_client.components.get(
    name="chat_completion_pipeline", label="latest"
)

# 使用@pipeline装饰器和create_pipeline函数定义管道任务
# 管道的名称设置为pipeline_display_name
@pipeline(name=pipeline_display_name)
def create_pipeline():
    # 使用各种参数初始化获取的管道组件
    # 这些参数包括模型路径、不同阶段的计算集群、训练和测试的数据集分割、用于微调的GPU数量以及其他微调参数
    chat_completion_pipeline = pipeline_component_func(
        mlflow_model_path=foundation_model.id,
        compute_model_import=compute_cluster,
        compute_preprocess=compute_cluster,
        compute_finetune=compute_cluster,
        compute_model_evaluation=compute_cluster,
        # 将数据集分割映射到参数
        train_file_path=Input(
            type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
        ),
        test_file_path=Input(
            type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
        ),
        # 训练设置
        number_of_gpu_to_use_finetuning=gpus_per_node,  # 设置为计算中可用的GPU数量
        **finetune_parameters
    )
    return {
        # 将微调任务的输出映射到管道任务的输出
        # 这是为了便于注册微调后的模型
        # 注册模型对于将模型部署到在线或批处理端点是必要的
        "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
    }

# 通过调用create_pipeline函数创建管道实例
pipeline_object = create_pipeline()

# 不使用先前任务的缓存结果
pipeline_object.settings.force_rerun = True

# 将continue on step failure设置为False
# 这意味着如果任何步骤失败，管道将停止
pipeline_object.settings.continue_on_step_failure = False
```

### 提交任务

这个Python脚本将机器学习管道任务提交到Azure Machine Learning工作区，然后等待任务完成。以下是它的工作流程：

它调用workspace_ml_client中的jobs对象的create_or_update方法来提交管道任务。要运行的管道由pipeline_object指定，任务运行的实验由experiment_name指定。

然后它调用workspace_ml_client中的jobs对象的stream方法来等待管道任务完成。要等待的任务由pipeline_job对象的name属性指定。

总之，这个脚本将机器学习管道任务提交到Azure Machine Learning工作区，然后等待任务完成。

```
# 将管道任务提交到Azure Machine Learning工作区
# 要运行的管道由pipeline_object指定
# 任务运行的实验由experiment_name指定
pipeline_job = workspace_ml_client.jobs.create_or_update(
    pipeline_object, experiment_name=experiment_name
)

# 等待管道任务完成
# 要等待的任务由pipeline_job对象的name属性指定
workspace_ml_client.jobs.stream(pipeline_job.name)
```

## 6. 在工作区中注册微调后的模型
我们将从微调任务的输出中注册模型。这将跟踪微调模型与微调任务之间的谱系。微调任务进一步跟踪基础模型、数据和训练代码的谱系。

### 注册机器学习模型
这个Python脚本正在注册在Azure Machine Learning管道中训练的机器学习模型。以下是它的工作流程：

它从Azure AI ML SDK中导入必要的模块。

它通过调用workspace_ml_client中的jobs对象的get方法并访问其outputs属性，检查是否有来自管道任务的trained_model输出。

它通过格式化一个字符串并包含管道任务的名称和输出的名称（"trained_model"）来构建训练模型的路径。

它定义了微调模型的名称，通过将"-ultrachat-200k"附加到原始模型名称并将任何斜杠替换为连字符。

它准备注册模型，通过创建一个Model对象，并包含各种参数，如模型的路径、模型的类型（MLflow模型）、模型的名称和版本以及模型的描述。

它通过调用workspace_ml_client中的models对象的create_or_update方法并以Model对象作为参数来注册模型。

它打印注册的模型。

总之，这个脚本正在注册在Azure Machine Learning管道中训练的机器学习模型。
```
# 从 Azure AI ML SDK 导入必要的模块
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes

# 检查管道任务中是否有 `trained_model` 输出
print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)

# 通过格式化字符串构建一个路径，包含管道任务的名称和输出的名称 ("trained_model")
model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
    pipeline_job.name, "trained_model"
)

# 通过在原始模型名称后附加 "-ultrachat-200k" 并将任何斜杠替换为连字符来定义微调模型的名称
finetuned_model_name = model_name + "-ultrachat-200k"
finetuned_model_name = finetuned_model_name.replace("/", "-")

print("path to register model: ", model_path_from_job)

# 通过创建一个包含各种参数的 Model 对象来准备注册模型
# 这些参数包括模型的路径、模型的类型（MLflow 模型）、模型的名称和版本，以及模型的描述
prepare_to_register_model = Model(
    path=model_path_from_job,
    type=AssetTypes.MLFLOW_MODEL,
    name=finetuned_model_name,
    version=timestamp,  # 使用时间戳作为版本以避免版本冲突
    description=model_name + " 微调模型，用于 ultrachat 200k 聊天完成",
)

print("prepare to register model: \n", prepare_to_register_model)

# 通过调用 workspace_ml_client 中 models 对象的 create_or_update 方法并传入 Model 对象作为参数来注册模型
registered_model = workspace_ml_client.models.create_or_update(
    prepare_to_register_model
)

# 打印注册的模型
print("registered model: \n", registered_model)
```
## 7. 部署微调后的模型到在线端点
在线端点提供了一个持久的 REST API，可以用于集成需要使用模型的应用程序。

### 管理端点
这个 Python 脚本在 Azure 机器学习中为已注册的模型创建一个托管的在线端点。以下是它的功能分解：

它从 Azure AI ML SDK 导入必要的模块。

通过将时间戳附加到字符串 "ultrachat-completion-" 后定义一个唯一的在线端点名称。

通过创建一个带有各种参数的 ManagedOnlineEndpoint 对象来准备创建在线端点，这些参数包括端点的名称、描述和认证模式（"key"）。

通过调用 workspace_ml_client 的 begin_create_or_update 方法并将 ManagedOnlineEndpoint 对象作为参数来创建在线端点。然后通过调用 wait 方法等待创建操作完成。

总之，这个脚本是在 Azure 机器学习中为已注册的模型创建一个托管的在线端点。

```
# 从 Azure AI ML SDK 导入必要的模块
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    ProbeSettings,
    OnlineRequestSettings,
)

# 通过将时间戳附加到字符串 "ultrachat-completion-" 后定义一个唯一的在线端点名称
online_endpoint_name = "ultrachat-completion-" + timestamp

# 通过创建一个带有各种参数的 ManagedOnlineEndpoint 对象来准备创建在线端点
# 这些参数包括端点的名称、描述和认证模式（"key"）
endpoint = ManagedOnlineEndpoint(
    name=online_endpoint_name,
    description="Online endpoint for "
    + registered_model.name
    + ", fine tuned model for ultrachat-200k-chat-completion",
    auth_mode="key",
)

# 通过调用 workspace_ml_client 的 begin_create_or_update 方法并将 ManagedOnlineEndpoint 对象作为参数来创建在线端点
# 然后通过调用 wait 方法等待创建操作完成
workspace_ml_client.begin_create_or_update(endpoint).wait()
```
你可以在这里找到支持部署的 SKU 列表 - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### 部署机器学习模型

这个 Python 脚本是将一个已注册的机器学习模型部署到 Azure 机器学习中的托管在线端点。以下是它的功能分解：

它导入了 ast 模块，该模块提供处理 Python 抽象语法树的功能。

它将部署的实例类型设置为 "Standard_NC6s_v3"。

它检查基础模型中是否存在 inference_compute_allow_list 标签。如果存在，则将标签值从字符串转换为 Python 列表，并赋值给 inference_computes_allow_list。如果不存在，则将 inference_computes_allow_list 设置为 None。

它检查指定的实例类型是否在允许列表中。如果不在，则打印一条消息，要求用户从允许列表中选择一个实例类型。

它通过创建一个带有各种参数的 ManagedOnlineDeployment 对象来准备创建部署，这些参数包括部署的名称、端点名称、模型的 ID、实例类型和数量、活性探测设置以及请求设置。

通过调用 workspace_ml_client 的 begin_create_or_update 方法并将 ManagedOnlineDeployment 对象作为参数来创建部署。然后通过调用 wait 方法等待创建操作完成。

它将端点的流量设置为将 100% 的流量指向 "demo" 部署。

通过调用 workspace_ml_client 的 begin_create_or_update 方法并将端点对象作为参数来更新端点。然后通过调用 result 方法等待更新操作完成。

总之，这个脚本是将一个已注册的机器学习模型部署到 Azure 机器学习中的托管在线端点。

```
# 导入 ast 模块，该模块提供处理 Python 抽象语法树的功能
import ast

# 设置部署的实例类型
instance_type = "Standard_NC6s_v3"

# 检查基础模型中是否存在 `inference_compute_allow_list` 标签
if "inference_compute_allow_list" in foundation_model.tags:
    # 如果存在，则将标签值从字符串转换为 Python 列表，并赋值给 `inference_computes_allow_list`
    inference_computes_allow_list = ast.literal_eval(
        foundation_model.tags["inference_compute_allow_list"]
    )
    print(f"Please create a compute from the above list - {computes_allow_list}")
else:
    # 如果不存在，则将 `inference_computes_allow_list` 设置为 `None`
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

# 通过创建一个带有各种参数的 `ManagedOnlineDeployment` 对象来准备创建部署
demo_deployment = ManagedOnlineDeployment(
    name="demo",
    endpoint_name=online_endpoint_name,
    model=registered_model.id,
    instance_type=instance_type,
    instance_count=1,
    liveness_probe=ProbeSettings(initial_delay=600),
    request_settings=OnlineRequestSettings(request_timeout_ms=90000),
)

# 通过调用 `workspace_ml_client` 的 `begin_create_or_update` 方法并将 `ManagedOnlineDeployment` 对象作为参数来创建部署
# 然后通过调用 `wait` 方法等待创建操作完成
workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()

# 将端点的流量设置为将 100% 的流量指向 "demo" 部署
endpoint.traffic = {"demo": 100}

# 通过调用 `workspace_ml_client` 的 `begin_create_or_update` 方法并将 `endpoint` 对象作为参数来更新端点
# 然后通过调用 `result` 方法等待更新操作完成
workspace_ml_client.begin_create_or_update(endpoint).result()
```
## 8. 使用示例数据测试端点
我们将从测试数据集中获取一些示例数据并提交到在线端点进行推理。然后我们将显示评分标签和真实标签。

### 读取结果
这个 Python 脚本将一个 JSON Lines 文件读入 pandas DataFrame，随机抽取一个样本，并重置索引。以下是它的功能分解：

它将文件 ./ultrachat_200k_dataset/test_gen.jsonl 读入 pandas DataFrame。使用 read_json 函数并带有 lines=True 参数，因为文件是 JSON Lines 格式，每行是一个独立的 JSON 对象。

从 DataFrame 中随机抽取一行。使用 sample 函数并带有 n=1 参数来指定要选择的随机行数。

重置 DataFrame 的索引。使用 reset_index 函数并带有 drop=True 参数来删除原始索引并用默认的整数值索引替换。

使用 head 函数并带有参数 2 显示 DataFrame 的前两行。然而，由于抽样后 DataFrame 只有一行，这将只显示这一行。

总之，这个脚本是将一个 JSON Lines 文件读入 pandas DataFrame，随机抽取一行，重置索引，并显示这一行。

```
# 导入 pandas 库
import pandas as pd

# 将 JSON Lines 文件 './ultrachat_200k_dataset/test_gen.jsonl' 读入 pandas DataFrame
# 'lines=True' 参数表示文件是 JSON Lines 格式，每行是一个独立的 JSON 对象
test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)

# 从 DataFrame 中随机抽取一行
# 'n=1' 参数指定要选择的随机行数
test_df = test_df.sample(n=1)

# 重置 DataFrame 的索引
# 'drop=True' 参数表示应删除原始索引并用默认的整数值索引替换
# 'inplace=True' 参数表示应在原地修改 DataFrame（不创建新对象）
test_df.reset_index(drop=True, inplace=True)

# 显示 DataFrame 的前两行
# 然而，由于抽样后 DataFrame 只有一行，这将只显示这一行
test_df.head(2)
```
### 创建 JSON 对象

这个 Python 脚本是创建一个带有特定参数的 JSON 对象并将其保存到文件中。以下是它的功能分解：

它导入了 json 模块，该模块提供处理 JSON 数据的功能。

它创建了一个名为 parameters 的字典，其中包含代表机器学习模型参数的键值对。键是 "temperature", "top_p", "do_sample", 和 "max_new_tokens"，对应的值分别是 0.6, 0.9, True, 和 200。

它创建了另一个名为 test_json 的字典，包含两个键："input_data" 和 "params"。"input_data" 的值是另一个字典，包含键 "input_string" 和 "parameters"。"input_string" 的值是一个包含 test_df DataFrame 中第一条消息的列表。"parameters" 的值是之前创建的 parameters 字典。"params" 的值是一个空字典。

它打开一个名为 sample_score.json 的文件

```
# 导入 json 模块，该模块提供处理 JSON 数据的功能
import json

# 创建一个名为 `parameters` 的字典，其中包含代表机器学习模型参数的键值对
# 键是 "temperature", "top_p", "do_sample", 和 "max_new_tokens"，对应的值分别是 0.6, 0.9, True, 和 200
parameters = {
    "temperature": 0.6,
    "top_p": 0.9,
    "do_sample": True,
    "max_new_tokens": 200,
}

# 创建另一个名为 `test_json` 的字典，包含两个键："input_data" 和 "params"
# "input_data" 的值是另一个字典，包含键 "input_string" 和 "parameters"
# "input_string" 的值是一个包含 `test_df` DataFrame 中第一条消息的列表
# "parameters" 的值是之前创建的 `parameters` 字典
# "params" 的值是一个空字典
test_json = {
    "input_data": {
        "input_string": [test_df["messages"][0]],
        "parameters": parameters,
    },
    "params": {},
}

# 打开一个名为 `sample_score.json` 的文件，在 `./ultrachat_200k_dataset` 目录下，以写模式打开
with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
    # 使用 `json.dump` 函数将 `test_json` 字典以 JSON 格式写入文件
    json.dump(test_json, f)
```
### 调用端点

这个 Python 脚本是在 Azure 机器学习中调用一个在线端点来评分一个 JSON 文件。以下是它的功能分解：

它调用 workspace_ml_client 对象的 online_endpoints 属性的 invoke 方法。该方法用于向在线端点发送请求并获取响应。

它通过 endpoint_name 和 deployment_name 参数指定端点和部署的名称。在这种情况下，端点名称存储在 online_endpoint_name 变量中，部署名称是 "demo"。

它通过 request_file 参数指定要评分的 JSON 文件的路径。在这种情况下，文件是 ./ultrachat_200k_dataset/sample_score.json。

它将端点的响应存储在 response 变量中。

它打印原始响应。

总之，这个脚本是在 Azure 机器学习中调用一个在线端点来评分一个 JSON 文件并打印响应。

```
# 调用 Azure 机器学习中的在线端点来评分 `sample_score.json` 文件
# `workspace_ml_client` 对象的 `online_endpoints` 属性的 `invoke` 方法用于向在线端点发送请求并获取响应
# `endpoint_name` 参数指定端点的名称，存储在 `online_endpoint_name` 变量中
# `deployment_name` 参数指定部署的名称，是 "demo"
# `request_file` 参数指定要评分的 JSON 文件的路径，是 `./ultrachat_200k_dataset/sample_score.json`
response = workspace_ml_client.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    deployment_name="demo",
    request_file="./ultrachat_200k_dataset/sample_score.json",
)

# 打印端点的原始响应
print("raw response: \n", response, "\n")
```
## 9. 删除在线端点
不要忘记删除在线端点，否则你会让端点使用的计算资源继续计费。这个 Python 代码行是在 Azure 机器学习中删除一个在线端点。以下是它的功能分解：

它调用 workspace_ml_client 对象的 online_endpoints 属性的 begin_delete 方法。该方法用于开始删除在线端点。

它通过 name 参数指定要删除的端点名称。在这种情况下，端点名称存储在 online_endpoint_name 变量中。

它调用 wait 方法来等待删除操作完成。这是一个阻塞操作，意味着它会阻止脚本继续运行，直到删除完成。

总之，这行代码是在 Azure 机器学习中开始删除一个在线端点并等待操作完成。

```
# 删除 Azure 机器学习中的在线端点
# `workspace_ml_client` 对象的 `online_endpoints` 属性的 `begin_delete` 方法用于开始删除在线端点
# `name` 参数指定要删除的端点名称，存储在 `online_endpoint_name` 变量中
# `wait` 方法用于等待删除操作完成。这是一个阻塞操作，意味着它会阻止脚本继续运行，直到删除完成
workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
```

免责声明：此翻译由人工智能模型从原文翻译而来，可能不够完美。请检查输出内容并进行必要的修改。