# 如何使用 Azure ML 系统注册表中的聊天补全组件进行模型微调

在这个示例中，我们将对 Phi-3-mini-4k-instruct 模型进行微调，以完成使用 ultrachat_200k 数据集的两人对话。

![MLFineTune](../../imgs/04/03/MLFineTune.png)

这个示例将展示如何使用 Azure ML SDK 和 Python 进行微调，然后将微调后的模型部署到在线端点以进行实时推理。

## 训练数据
我们将使用 ultrachat_200k 数据集。这是 UltraChat 数据集的一个经过大量过滤的版本，并用于训练 Zephyr-7B-β，一个最先进的 7b 聊天模型。

## 模型
我们将使用 Phi-3-mini-4k-instruct 模型，展示用户如何为聊天补全任务微调模型。如果您是从特定模型卡打开此笔记本，请记得替换具体的模型名称。

## 任务
- 选择一个模型进行微调。
- 选择并探索训练数据。
- 配置微调任务。
- 运行微调任务。
- 查看训练和评估指标。
- 注册微调后的模型。
- 部署微调后的模型以进行实时推理。
- 清理资源。

## 1. 设置前提条件
- 安装依赖项。
- 连接到 AzureML 工作区。了解更多信息请参阅 SDK 身份验证设置。用您自己的信息替换下文代码中的 <WORKSPACE_NAME>、<RESOURCE_GROUP> 和 <SUBSCRIPTION_ID>。
- 连接到 azureml 系统注册表。
- 设置可选的实验名称。
- 检查或创建计算资源。

要求：一个 GPU 节点可以有多个 GPU 卡。例如，在 Standard_NC24rs_v3 的一个节点中有 4 个 NVIDIA V100 GPU，而在 Standard_NC12s_v3 中有 2 个 NVIDIA V100 GPU。有关此信息，请参阅文档。每个节点的 GPU 卡数量在下面的参数 gpus_per_node 中设置。正确设置此值将确保节点中所有 GPU 的利用率。推荐的 GPU 计算 SKU 可以在这里和这里找到。

### Python 库

通过运行下面的单元格安装依赖项。如果在新环境中运行，这是必不可少的一步。

```
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```
### 交互 Azure ML

这个 Python 脚本用于与 Azure 机器学习 (Azure ML) 服务进行交互。以下是它的功能分解：

它从 azure.ai.ml、azure.identity 和 azure.ai.ml.entities 包中导入必要的模块。还导入了 time 模块。

它尝试使用 DefaultAzureCredential() 进行身份验证，这提供了一种简化的身份验证体验，可以快速开始在 Azure 云中运行的应用程序开发。如果失败，它会回退到 InteractiveBrowserCredential()，这提供了一个交互式登录提示。

然后它尝试使用 from_config 方法创建一个 MLClient 实例，该方法从默认配置文件 (config.json) 中读取配置。如果失败，它会通过手动提供 subscription_id、resource_group_name 和 workspace_name 来创建一个 MLClient 实例。

它为名为 "azureml" 的 Azure ML 注册表创建另一个 MLClient 实例。此注册表是存储模型、微调管道和环境的地方。

它将实验名称设置为 "chat_completion_Phi-3-mini-4k-instruct"。

它生成一个唯一的时间戳，通过将当前时间（自纪元以来的秒数，作为浮点数）转换为整数，然后转换为字符串。此时间戳可用于创建唯一的名称和版本。

```
# 从 Azure ML 和 Azure Identity 导入必要的模块
from azure.ai.ml import MLClient
from azure.identity import (
    DefaultAzureCredential,
    InteractiveBrowserCredential,
)
from azure.ai.ml.entities import AmlCompute
import time  # 导入 time 模块

# 尝试使用 DefaultAzureCredential 进行身份验证
try:
    credential = DefaultAzureCredential()
    credential.get_token("https://management.azure.com/.default")
except Exception as ex:  # 如果 DefaultAzureCredential 失败，使用 InteractiveBrowserCredential
    credential = InteractiveBrowserCredential()

# 尝试使用默认配置文件创建 MLClient 实例
try:
    workspace_ml_client = MLClient.from_config(credential=credential)
except:  # 如果失败，请通过手动提供详细信息来创建 MLClient 实例
    workspace_ml_client = MLClient(
        credential,
        subscription_id="<SUBSCRIPTION_ID>",
        resource_group_name="<RESOURCE_GROUP>",
        workspace_name="<WORKSPACE_NAME>",
    )

# 为 Azure ML 注册表创建另一个名为 "azureml "的 MLClient 实例
# 该注册表是存储模型、微调管道和环境的地方
registry_ml_client = MLClient(credential, registry_name="azureml")

# 设置实验名称
experiment_name = "chat_completion_Phi-3-mini-4k-instruct"

# 生成唯一的时间戳，可用于需要唯一的名称和版本
timestamp = str(int(time.time()))
```
## 2. 选择一个基础模型进行微调
Phi-3-mini-4k-instruct 是一个拥有 3.8B 参数的轻量级的先进开放模型，以 Phi-2 使用的数据集为基础构建。该模型属于 Phi-3 模型家族，Mini 版本有两种变体，分别是 4K 和 128K，这是它可以支持的上下文长度（以 token 计）。我们需要根据我们的特定目的对模型进行微调，以便更好的使用它。您可以在 AzureML Studio 的模型目录中浏览这些模型，按聊天补全任务进行筛选。在本示例中，我们使用 Phi-3-mini-4k-instruct 模型。对于其他模型，请替换成相应的模型名及版本。

注意模型的 model id 属性。这将输入给微调任务。在 AzureML Studio 模型目录的模型详细信息页面中也可用作 Asset ID 字段。

这个 Python 脚本与 Azure 机器学习 (Azure ML) 服务进行交互。以下是它的功能分解：

它将 model_name 设置为 "Phi-3-mini-4k-instruct"。

它使用 registry_ml_client 对象的 models 属性的 get 方法从 Azure ML 注册表中检索具有指定名称的模型的最新版本。get 方法带有两个参数：模型的名称和指定应检索最新版本的标签。

它向终端输出一条消息，指示将用于微调的模型的名称、版本和 id。字符串的 format 方法用于将模型的名称、版本和 id 插入到消息中。模型的名称、版本和 id 作为 foundation_model 对象的属性访问。

```
# 设置模型名
model_name = "Phi-3-mini-4k-instruct"

# 从 Azure ML 注册表中获取模型的最新版本
foundation_model = registry_ml_client.models.get(model_name, label="latest")

# 打印型号名称、版本和 ID
# 这些信息有助于跟踪和调试
print(
    "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
        foundation_model.name, foundation_model.version, foundation_model.id
    )
)
```
## 3. 创建一个用于任务的计算资源
微调工作只能使用 GPU 计算。计算资源的大小取决于模型有多大。在大多数情况下，我们难以确认微调需要多少计算资源。在此单元格中，我们将指导用户为调试工作选择合适的计算资源。

**注意1** 下列计算资源适用于最优化的配置。对配置的任何更改可能会导致 Cuda 出现内存不足的错误。如果遇到这种情况，可以尝试升级计算资源的大小。

**注意2** 在选择下面的 compute_cluster_size 时，请确保您的资源组中有可用的计算资源。如果某个计算资源不可用，您可以申请访问计算资源。

### 检查是否支持微调
这个 Python 脚本与 Azure 机器学习 (Azure ML) 模型进行交互。以下是它的功能分解：

它导入 ast 模块，该模块提供处理 Python 抽象语法树的函数。

它检查 foundation_model 对象（代表 Azure ML 模型）是否有名为 finetune_compute_allow_list 的标签。Azure ML 中的标签是键值对，可以创建并用于过滤和排序模型。

如果存在 finetune_compute_allow_list 标签，它使用 ast.literal_eval 函数安全地将标签的值（一个字符串）解析为 Python 列表。然后将此列表赋值给 computes_allow_list 变量。然后，它会打印一条信息，说明应从列表中创建计算。

如果不存在 finetune_compute_allow_list 标签，它将 computes_allow_list 设置为 None，并打印一条消息，指示 finetune_compute_allow_list 标签不是模型标签的一部分。

总之，这个脚本会检查模型元数据中的一个特定标签，将标签的值转换为一个列表（如果存在），并相应地向用户提供反馈。

```
# 导入 ast 模块，该模块提供了处理 Python 抽象语法语法树的函数
import ast

# 检查模型标记中是否有 "finetune_comput_allow_list "标记
if "finetune_compute_allow_list" in foundation_model.tags:
    # 如果标签存在，则使用 ast.literal_eval 将标签值（字符串）安全地解析为 Python 列表
    computes_allow_list = ast.literal_eval(
        foundation_model.tags["finetune_compute_allow_list"]
    )  # convert string to python list
    # 打印一条信息，说明应从列表中创建一个计算器
    print(f"Please create a compute from the above list - {computes_allow_list}")
else:
    # 如果不存在标签，则将 computes_allow_list 设置为 None
    computes_allow_list = None
    # 打印一条信息，说明 "finetune_comput_allow_list "标记不是模型标记的一部分
    print("`finetune_compute_allow_list` is not part of model tags")
```
### 检查计算实例

这个 Python 脚本与 Azure 机器学习 (Azure ML) 服务进行交互，并对计算实例执行多项检查。以下是它的功能分解：

它尝试从 Azure ML 工作区中检索存储在 compute_cluster 中的计算实例。如果计算实例的配置状态为 "failed"，它会引发 ValueError。

它检查 computes_allow_list 是否不为 None。如果不为 None，它会将列表中的所有计算大小转换为小写，并检查当前计算实例的大小是否在列表中。如果不在列表中，它会引发 ValueError。

如果 computes_allow_list 为 None，它会检查计算实例的大小是否在不支持的 GPU 虚拟机大小列表中。如果在列表中，它会引发 ValueError。

它检索工作区中所有可用计算大小的列表。然后它遍历这个列表，对于每个计算大小，它检查其名称是否与当前计算实例的大小匹配。如果匹配，它会检索该计算大小的 GPU 数量，并将 gpu_count_found 设置为 True。

如果 gpu_count_found 为 True，它会打印计算实例中的 GPU 数量。如果 gpu_count_found 为 False，它会引发 ValueError。

总之，这个脚本对 Azure ML 工作区中的计算实例执行多项检查，包括检查其配置状态、大小是否在允许列表或拒绝列表中，以及其 GPU 数量。

```
# 打印异常信息
print(e)
# 如果工作区中没有计算大小，则引发 ValueError 错误
raise ValueError(
    f"WARNING! Compute size {compute_cluster_size} not available in workspace"
)

# 从 Azure ML 工作区读取计算实例
compute = workspace_ml_client.compute.get(compute_cluster)
# 检查计算实例的调配状态是否为 "failed"
if compute.provisioning_state.lower() == "failed":
    # 如果调配状态为 "failed"，则引发 ValueError 错误
    raise ValueError(
        f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
        f"please try creating a different compute"
    )

# 检查 computes_allow_list 是否不为 None
if computes_allow_list is not None:
    # 将 computes_allow_list 中的所有计算大小转换为小写
    computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
    # 检查计算实例的大小是否在 computes_allow_list_lower_case 中
    if compute.size.lower() not in computes_allow_list_lower_case:
        # 如果计算实例的大小不在 computes_allow_list_lower_case 中，则引发 ValueError 错误
        raise ValueError(
            f"VM size {compute.size} is not in the allow-listed computes for finetuning"
        )
else:
    # 定义不支持的 GPU 虚拟机大小列表
    unsupported_gpu_vm_list = [
        "standard_nc6",
        "standard_nc12",
        "standard_nc24",
        "standard_nc24r",
    ]
    # 检查计算实例的大小是否在 unsupported_gpu_vm_list 中
    if compute.size.lower() in unsupported_gpu_vm_list:
        # 如果计算实例的大小在 unsupported_gpu_vm_list 中，则引发 ValueError 错误
        raise ValueError(
            f"VM size {compute.size} is currently not supported for finetuning"
        )

# 初始化一个标志，用于检查是否已找到计算实例中的 GPU 数量
gpu_count_found = False
# 读取工作区中所有可用计算大小的列表
workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
available_sku_sizes = []
# 遍历可用计算大小列表
for compute_sku in workspace_compute_sku_list:
    available_sku_sizes.append(compute_sku.name)
    # 检查计算大小的名称是否与计算实例的大小一致
    if compute_sku.name.lower() == compute.size.lower():
        # 如果是，则检索该计算大小的 GPU 数量，并将 gpu_count_found 设为 True
        gpus_per_node = compute_sku.gpus
        gpu_count_found = True
# 如果 gpu_count_found 为 True，则打印计算实例中 GPU 的数量
if gpu_count_found:
    print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
else:
    # 如果 gpu_count_found 为 False，则引发 ValueError 错误
    raise ValueError(
        f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
        f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
    )
```

## 4. 选择用于微调模型的数据集

我们使用 ultrachat_200k 数据集。数据集被分成了四个部分，用于：

- 监督微调（sft）。
- 生成排名（gen）。

每个部分的数据量如下所示：

| train_sft | test_sft | train_gen | test_gen |
| --------- | -------- | --------- | -------- |
| 207865    | 23110    | 256032    | 28304    |

接下来的几个单元展示了用于微调的基本数据准备：

### 可视化部分数据行

因为这只是个示例，而我们希望它能快速运行，因此我们只保留已修剪的 train_sft, test_sft 数据集的 5%。这代表微调后的准确率会更低，这种操作不应该在生产环境中使用。

download-dataset.py 用于下载 ultrachat_200k 数据集，并将数据集转换为 finetune 管道组件的可消耗格式。此外，由于原始数据集很大，因此我们在此只使用了数据集的一部分。

运行以下脚本只会下载 5% 的数据。可以通过更改 dataset_split_pc 参数来增加这个百分比。

**注意：** 一些语言模型有不同的语言代码，数据集中的列名应该与模型匹配。

这是数据格式的示例，聊天补全数据集以 parquet 格式存储，每个条目使用以下架构：

以 JSON（JavaScript Object Notation）文档格式储存。这是一种流行的数据交换格式。它不是可执行代码，而是一种存储和传输数据的方式。以下是其结构的分解：

- "prompt"：此键包含一个字符串值，表示向 AI 助手提出的任务或问题。
- "messages"：此键包含一个对象数组。每个对象表示用户和 AI 助手之间对话中的一条消息。每个消息对象都有两个键：
  - "content"：此键包含一个字符串值，表示消息的内容。
  - "role"：此键包含一个字符串值，表示发送消息的实体的角色。可以是 "user" 或 "assistant"。
- "prompt_id"：此键包含一个字符串值，表示提示的唯一标识符。

在这个特定的 JSON 文档中，表示了一段对话，其中用户请求 AI 助手为反乌托邦故事创建一个主角。助手响应，然后用户要求更多细节。助手同意提供更多细节。整个对话与特定的提示 id 关联。

```
{
    // The task or question posed to an AI assistant
    "prompt": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
    
    // An array of objects, each representing a message in a conversation between a user and an AI assistant
    "messages":[
        {
            // The content of the user's message
            "content": "Create a fully-developed protagonist who is challenged to survive within a dystopian society under the rule of a tyrant. ...",
            // The role of the entity that sent the message
            "role": "user"
        },
        {
            // The content of the assistant's message
            "content": "Name: Ava\n\n Ava was just 16 years old when the world as she knew it came crashing down. The government had collapsed, leaving behind a chaotic and lawless society. ...",
            // The role of the entity that sent the message
            "role": "assistant"
        },
        {
            // The content of the user's message
            "content": "Wow, Ava's story is so intense and inspiring! Can you provide me with more details.  ...",
            // The role of the entity that sent the message
            "role": "user"
        }, 
        {
            // The content of the assistant's message
            "content": "Certainly! ....",
            // The role of the entity that sent the message
            "role": "assistant"
        }
    ],
    
    // A unique identifier for the prompt
    "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
}
```
### 下载数据
这个 Python 脚本用于使用名为 download-dataset.py 的辅助脚本下载数据集。以下是它的功能分解：

它导入了 os 模块，该模块提供了一种跨平台的方式来使用操作系统相关的功能。

它使用 os.system 函数在 shell 中运行 download-dataset.py 脚本，并带有特定的命令行参数。这些参数指定了要下载的数据集（HuggingFaceH4/ultrachat_200k），保存目录（ultrachat_200k_dataset），以及拆分数据集的百分比（5）。os.system 函数返回它执行的命令的退出状态；这个状态存储在 exit_status 变量中。

它检查 exit_status 是否为 0。在类 Unix 操作系统中，退出状态为 0 通常表示命令成功，而任何其他数字则表示错误。如果 exit_status 不为 0，它会引发一个异常，并显示一条消息，指示下载数据集时出错。

总之，这个脚本运行一个命令来使用辅助脚本下载数据集，如果命令失败，则引发异常。

```python
# 导入 os 模块，它提供了一种使用操作系统相关功能的方法
import os

# 使用 os.system 函数在 shell 中运行 download-dataset.py 脚本，并带有特定的命令行参数
# 这些参数指定了要下载的数据集（HuggingFaceH4/ultrachat_200k），下载到的目录（ultrachat_200k_dataset），以及数据集拆分的百分比（5）
# os.system 函数返回它执行的命令的退出状态；这个状态存储在 exit_status 变量中
exit_status = os.system(
    "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
)

# 检查 exit_status 是否不为 0
# 在类 Unix 操作系统中，退出状态为 0 通常表示命令成功，而任何其他数字则表示错误
# 如果 exit_status 不为 0，则引发一个异常，并显示一条消息，指示下载数据集时出错
if exit_status != 0:
    raise Exception("下载数据集时出错")
```

### 加载数据到 DataFrame
这个 Python 脚本将一个 JSON Lines 文件加载到 pandas DataFrame 中并显示前 5 行。以下是它的功能分解：

它导入了 pandas 库，这是一个强大的数据操作和分析库。

它将 pandas 的显示选项的最大列宽设置为 0。这意味着在打印 DataFrame 时，将会显示完整的列文本，而不会被截断。

它使用 pd.read_json 函数将 ultrachat_200k_dataset 目录中的 train_sft.jsonl 文件加载到 DataFrame 中。lines=True 参数表明该文件是 JSON Lines 格式，即文件中的每一行都是一个单独的 JSON 对象。

它使用 head 方法显示 DataFrame 的前 5 行。如果 DataFrame 少于 5 行，它会显示所有行。

总之，这个脚本将一个 JSON Lines 文件加载到 DataFrame 中并显示前 5 行的完整列文本。

```python
# 导入 pandas 库，这是一个强大的数据操作和分析库
import pandas as pd

# 将 pandas 的显示选项的最大列宽设置为 0
# 这意味着在打印 DataFrame 时，每列的完整文本将不被截断
pd.set_option("display.max_colwidth", 0)

# 使用 pd.read_json 函数将 ultrachat_200k_dataset 目录中的 train_sft.jsonl 文件加载到 DataFrame 中
# lines=True 参数表明该文件是 JSON Lines 格式，其中每行是一个单独的 JSON 对象
df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)

# 使用 head 方法显示 DataFrame 的前 5 行
# 如果 DataFrame 少于 5 行，它会显示所有行
df.head()
```

## 5. 将模型和数据作为输入，提交微调工作

创建使用聊天补全管道组件的任务。了解更多关于微调支持的所有参数。

### 定义微调参数

微调参数可以分为两类——训练参数和优化参数。

训练参数定义了训练的各个方面，例如：

- 使用的优化器，调度器
- 优化微调的指标
- 训练步骤和批量大小等

优化参数有助于优化 GPU 内存并有效利用计算资源。

以下是一些属于该类别的参数。优化参数因模型而异，并与模型一起打包以处理这些差异。

- 启用 DeepSpeed 和 LoRA
- 启用混合精度训练
- 启用多节点训练

**注意：** 监督微调可能会导致对齐丢失或灾难性的遗忘。我们建议在微调后检查这一问题并执行对齐。

### 微调参数

这个 Python 脚本设置了微调机器学习模型的参数。以下是它的功能分解：

它设置了默认的训练参数，如训练周期数、训练和评估的批量大小、学习率和学习率调度类型。

它设置了默认的优化参数，如是否应用层次相关传播（LoRa）和 DeepSpeed，以及 DeepSpeed 阶段。

它将训练和优化参数组合成一个名为 finetune_parameters 的字典。

它检查 foundation_model 是否有任何模型特定的默认参数。如果有，它会打印一条警告消息，并使用这些模型特定的默认值更新 finetune_parameters 字典。ast.literal_eval 函数用于将模型特定的默认值从字符串转换为 Python 字典。

它打印将用于运行的最终微调参数集。

总之，这个脚本设置并显示微调机器学习模型的参数，并且能够使用模型特定的参数覆盖默认参数。

```python
# 设置默认的训练参数，如训练周期数、训练和评估的批量大小、学习率和学习率调度类型
training_parameters = dict(
    num_train_epochs=3,
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    learning_rate=5e-6,
    lr_scheduler_type="cosine",
)

# 设置默认的优化参数，如是否应用层次相关传播（LoRa）和 DeepSpeed，以及 DeepSpeed 阶段数
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
    print("警告！存在模型特定的默认值。默认值可能会被覆盖。")
    finetune_parameters.update(
        ast.literal_eval(  # 将字符串转换为 Python 字典
            foundation_model.tags["model_specific_defaults"]
        )
    )

# 打印将用于运行的最终微调参数集
print(
    f"将为运行设置以下微调参数：{finetune_parameters}"
)
```

### 训练管道

这段Python脚本定义了一个函数，用于生成机器学习训练管道的显示名称，然后调用这个函数生成并打印显示名称。以下是它的具体功能：

定义了 `get_pipeline_display_name` 函数。这个函数基于与训练管道相关的各种参数生成一个显示名称。

在函数内部，它通过乘以每个设备的批量大小、梯度累积步骤的数量、每个节点的GPU数量以及用于微调的节点数量来计算总批量大小。

它检索了各种其他参数，如学习率调度器类型、是否应用了DeepSpeed、DeepSpeed阶段、是否应用了逐层相关传播（LoRa）、要保留的模型检查点数量上限以及最大序列长度。

它构建了一个包括所有这些参数的字符串，参数之间用连字符分隔。如果应用了DeepSpeed或LoRa，字符串中分别包括 "ds" 后跟DeepSpeed阶段，或 "lora"。如果没有应用，则分别包括 "nods" 或 "nolora"。

这个函数返回这个字符串，该字符串作为训练管道的显示名称。

在定义函数之后，它被调用以生成显示名称，然后打印该显示名称。

总之，这个脚本基于各种参数生成一个机器学习训练管道的显示名称，然后打印这个显示名称。

```
# 定义一个函数以生成训练管道的显示名称
def get_pipeline_display_name():
    # 通过乘以每个设备的批量大小、梯度累积步骤的数量、每个节点的GPU数量以及用于微调的节点数量来计算总批量大小
    batch_size = (
        int(finetune_parameters.get("per_device_train_batch_size", 1))
        * int(finetune_parameters.get("gradient_accumulation_steps", 1))
        * int(gpus_per_node)
        * int(finetune_parameters.get("num_nodes_finetune", 1))
    )
    # 检索学习率调度器类型
    scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
    # 检索是否使用了DeepSpeed
    deepspeed = finetune_parameters.get("apply_deepspeed", "false")
    # 检索 deepspeed_stage 的值
    ds_stage = finetune_parameters.get("deepspeed_stage", "2")
    # 如果使用了DeepSpeed，显示名称是 ds 加上阶段数；如果没有，则为 "nods"
    if deepspeed == "true":
        ds_string = f"ds{ds_stage}"
    else:
        ds_string = "nods"
    # 检索是否应用了逐层相关传播（LoRa）
    lora = finetune_parameters.get("apply_lora", "false")
    # 如果应用了LoRa，在显示名称为 "lora"；如果没有，则为 "nolora"
    if lora == "true":
        lora_string = "lora"
    else:
        lora_string = "nolora"
    # 检索要保留的模型检查点数量上限
    save_limit = finetune_parameters.get("save_total_limit", -1)
    # 检索最大序列长度
    seq_len = finetune_parameters.get("max_seq_length", -1)
    # 通过连接所有这些参数来构建显示名称，参数之间用连字符分隔
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

这段Python脚本使用Azure Machine Learning SDK定义和配置一个机器学习管道。以下是它的具体功能：

1. 它从Azure AI ML SDK中导入必要的模块。

2. 它从注册表中获取名为 "chat_completion_pipeline" 的管道组件。

3. 它使用 `@pipeline` 装饰器和 `create_pipeline` 函数定义了一个管道作业。管道的名称设置为 `pipeline_display_name`。

4. 在 `create_pipeline` 函数内部，它使用各种参数初始化获取的管道组件，包括模型路径、不同阶段的计算群集、训练和测试的数据集拆分、用于微调的GPU数量以及其他微调参数。

5. 它将微调作业的输出映射到管道作业的输出。这是为了可以轻松注册微调后的模型，这是将模型部署到在线或批处理端点所必需的。

6. 它通过调用 `create_pipeline` 函数创建管道的实例。

7. 它将管道的 `force_rerun` 设置为 `True`，这意味着不会使用先前作业的缓存结果。

8. 它将管道的 `continue_on_step_failure` 设置为 `False`，这意味着如果任何步骤失败，管道将停止。

总之，这个脚本使用Azure Machine Learning SDK定义和配置一个用于聊天补全任务的机器学习管道。

```
# 从Azure AI ML SDK中导入必要的模块
from azure.ai.ml.dsl import pipeline
from azure.ai.ml import Input

# 从注册表中获取名为 "chat_completion_pipeline" 的管道组件
pipeline_component_func = registry_ml_client.components.get(
    name="chat_completion_pipeline", label="latest"
)

# 使用 @pipeline 装饰器和 create_pipeline 函数定义管道作业
# 管道的名称设置为 pipeline_display_name
@pipeline(name=pipeline_display_name)
def create_pipeline():
    # 使用各种参数初始化获取的管道组件
    # 这些参数包括模型路径、不同时期的计算群集、训练和测试的数据集拆分、用于微调的GPU数量以及其他微调参数
    chat_completion_pipeline = pipeline_component_func(
        mlflow_model_path=foundation_model.id,
        compute_model_import=compute_cluster,
        compute_preprocess=compute_cluster,
        compute_finetune=compute_cluster,
        compute_model_evaluation=compute_cluster,
        # 将拆分的数据集映射到参数
        train_file_path=Input(
            type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
        ),
        test_file_path=Input(
            type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
        ),
        # 训练设置
        number_of_gpu_to_use_finetuning=gpus_per_node,  # 设置为可用于计算的GPU数量
        **finetune_parameters
    )
    return {
        # 将微调作业的输出映射到管道作业的输出
        # 这样我们可以轻松注册微调后的模型
        # 注册模型是将模型部署到在线或批处理端点所必需的
        "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
    }

# 通过调用 create_pipeline 函数创建管道的实例
pipeline_object = create_pipeline()

# 不要使用先前作业的缓存结果
pipeline_object.settings.force_rerun = True

# 将继续在步骤失败时的设置为 False
# 这意味着如果任何步骤失败，管道将停止
pipeline_object.settings.continue_on_step_failure = False
```

### 提交作业

这段Python脚本将一个机器学习管道作业提交到Azure Machine Learning工作区，然后等待作业完成。以下是它的具体功能：

它调用 `workspace_ml_client` 中 `jobs` 对象的 `create_or_update` 方法提交管道作业。要运行的管道由 `pipeline_object` 指定，作业所在的实验由 `experiment_name` 指定。

然后它调用 `workspace_ml_client` 中 `jobs` 对象的 `stream` 方法等待管道作业完成。要等待的作业由 `pipeline_job` 对象的 `name` 属性指定。

总之，这个脚本将一个机器学习管道作业提交到Azure Machine Learning工作区，然后等待作业完成。

```
# 将管道作业提交到Azure Machine Learning工作区
# 要运行的管道由 pipeline_object 指定
# 作业所在的实验由 experiment_name 指定
pipeline_job = workspace_ml_client.jobs.create_or_update(
    pipeline_object, experiment_name=experiment_name
)

# 等待管道作业完成
# 要等待的作业由 pipeline_job 对象的 name 属性指定
workspace_ml_client.jobs.stream(pipeline_job.name)
```

## 6. 在工作区中注册微调后的模型
我们将从微调任务的输出中注册模型。这将跟踪微调模型和微调任务之间的谱系。微调任务还会进一步跟踪基础模型、数据和训练代码的谱系。

### 注册机器学习模型
此 Python 脚本用于注册在 Azure 机器学习管道中训练的机器学习模型。以下是它的具体功能：

它从 Azure AI ML SDK 中导入必要的模块。

它通过调用 workspace_ml_client 的 jobs 对象的 get 方法并访问其 outputs 属性，检查管道任务中是否有可用的 trained_model 输出。

它通过格式化字符串，使用管道任务的名称和输出名称（"trained_model"）构造到训练模型的路径。

它通过在原始模型名称后附加 "-ultrachat-200k" 并将任何斜杠替换为连字符，定义微调模型的名称。

它通过创建一个带有各种参数的 Model 对象来准备注册模型，这些参数包括模型的路径、模型的类型（MLflow 模型）、模型的名称和版本以及模型的描述。

它通过调用 workspace_ml_client 的 models 对象的 create_or_update 方法并传递 Model 对象来注册模型。

它打印已注册的模型。

总之，这个脚本用于注册在 Azure 机器学习管道中训练的机器学习模型。

```
# 从 Azure AI ML SDK 中导入必要的模块
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes

# 检查管道任务中是否有可用的 `trained_model` 输出
print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)

# 通过格式化字符串，使用管道任务的名称和输出名称（"trained_model"）构造到训练模型的路径
model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
    pipeline_job.name, "trained_model"
)

# 通过在原始模型名称后附加 "-ultrachat-200k" 并将任何斜杠替换为连字符，定义微调模型的名称
finetuned_model_name = model_name + "-ultrachat-200k"
finetuned_model_name = finetuned_model_name.replace("/", "-")

print("path to register model: ", model_path_from_job)

# 通过创建一个带有各种参数的 Model 对象来准备注册模型
# 这些参数包括模型的路径、模型的类型（MLflow 模型）、模型的名称和版本以及模型的描述
prepare_to_register_model = Model(
    path=model_path_from_job,
    type=AssetTypes.MLFLOW_MODEL,
    name=finetuned_model_name,
    version=timestamp,  # 使用时间戳作为版本以避免版本冲突
    description=model_name + " fine tuned model for ultrachat 200k chat-completion",
)

print("prepare to register model: \n", prepare_to_register_model)

# 通过调用 workspace_ml_client 的 models 对象的 create_or_update 方法并传递 Model 对象来注册模型
registered_model = workspace_ml_client.models.create_or_update(
    prepare_to_register_model
)

# 打印已注册的模型
print("registered model: \n", registered_model)
```

## 7. 将微调后的模型部署到在线端点
在线端点提供一个持久的 REST API，可以用于与需要使用模型的应用集成。

### 管理端点
此 Python 脚本在 Azure 机器学习中为已注册的模型创建一个托管在线端点。以下是它的具体功能：

它从 Azure AI ML SDK 中导入必要的模块。

它通过在字符串 "ultrachat-completion-" 后附加时间戳，定义在线端点的唯一名称。

它通过创建一个带有各种参数的 ManagedOnlineEndpoint 对象来准备创建在线端点，这些参数包括端点的名称、端点的描述和认证模式（"key"）。

它通过调用 workspace_ml_client 的 begin_create_or_update 方法并传递 ManagedOnlineEndpoint 对象来创建在线端点。然后通过调用 wait 方法等待创建操作完成。

总之，这个脚本在 Azure 机器学习中为已注册的模型创建一个托管在线端点。

```
# 从 Azure AI ML SDK 中导入必要的模块
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    ProbeSettings,
    OnlineRequestSettings,
)

# 通过在字符串 "ultrachat-completion-" 后附加时间戳，定义在线端点的唯一名称
online_endpoint_name = "ultrachat-completion-" + timestamp

# 通过创建一个带有各种参数的 ManagedOnlineEndpoint 对象来准备创建在线端点
# 这些参数包括端点的名称、端点的描述和认证模式（"key"）
endpoint = ManagedOnlineEndpoint(
    name=online_endpoint_name,
    description="Online endpoint for "
    + registered_model.name
    + ", fine tuned model for ultrachat-200k-chat-completion",
    auth_mode="key",
)

# 通过调用 workspace_ml_client 的 begin_create_or_update 方法并传递 ManagedOnlineEndpoint 对象来创建在线端点
# 然后通过调用 wait 方法等待创建操作完成
workspace_ml_client.begin_create_or_update(endpoint).wait()
```

您可以在这里找到支持部署的 SKU 列表 - [托管在线端点 SKU 列表](https://learn.microsoft.com/zh-cn/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### 部署机器学习模型

此 Python 脚本将已注册的机器学习模型部署到 Azure 机器学习中的托管在线端点。以下是它的具体功能：

它导入 ast 模块，该模块提供处理 Python 抽象语法树的函数。

它将部署的实例类型设置为 "Standard_NC6s_v3"。

它检查基础模型中是否存在 inference_compute_allow_list 标签。如果存在，它将标签值从字符串转换为 Python 列表并分配给 inference_computes_allow_list。如果不存在，则将 inference_computes_allow_list 设置为 None。

它检查指定的实例类型是否在允许列表中。如果不在，则打印一条消息，要求用户从允许列表中选择一个实例类型。

它通过创建一个带有各种参数的 ManagedOnlineDeployment 对象来准备创建部署，这些参数包括部署的名称、端点的名称、模型的 ID、实例类型和数量、存活探测设置以及请求设置。

它通过调用 workspace_ml_client 的 begin_create_or_update 方法并传递 ManagedOnlineDeployment 对象来创建部署。然后通过调用 wait 方法等待创建操作完成。

它将端点的流量设置为将 100% 的流量导向 "demo" 部署。

它通过调用 workspace_ml_client 的 begin_create_or_update 方法并传递端点对象来更新端点。然后通过调用 result 方法等待更新操作完成。

总之，这个脚本将已注册的机器学习模型部署到 Azure 机器学习中的托管在线端点。

```
# 导入 ast 模块，该模块提供处理 Python 抽象语法树的函数
import ast

# 将部署的实例类型设置为 "Standard_NC6s_v3"
instance_type = "Standard_NC6s_v3"

# 检查基础模型中是否存在 `inference_compute_allow_list` 标签
if "inference_compute_allow_list" in foundation_model.tags:
    # 如果存在，将标签值从字符串转换为 Python 列表并分配给 `inference_computes_allow_list`
    inference_computes_allow_list = ast.literal_eval(
        foundation_model.tags["inference_compute_allow_list"]
    )
    print(f"Please create a compute from the above list - {computes_allow_list}")
else:
    # 如果不存在，将 `inference_computes_allow_list` 设置为 `None`
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

# 通过调用 `workspace_ml_client` 的 `begin_create_or_update` 方法并传递 `ManagedOnlineDeployment` 对象来创建部署
# 然后通过调用 `wait` 方法等待创建操作完成
workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()

# 将端点的流量设置为将 100% 的流量导向 "demo" 部署
endpoint.traffic = {"demo": 100}

# 通过调用 `workspace_ml_client` 的 `begin_create_or_update` 方法并传递端点对象来更新端点
# 然后通过调用 `result` 方法等待更新操作完成
workspace_ml_client.begin_create_or_update(endpoint).result()
```

## 8. 使用示例数据测试端点
我们将从测试数据集中获取一些示例数据并提交到在线端点进行推理。然后我们将显示预测标签和实际标签。

### 读取结果

这个 Python 脚本将 JSON Lines 文件读取到一个 pandas DataFrame 中，随机抽取一个样本，并重置索引。以下是它的具体操作步骤：

它将文件 `./ultrachat_200k_dataset/test_gen.jsonl` 读取到一个 pandas DataFrame 中。由于文件是 JSON Lines 格式的，其中每一行都是一个独立的 JSON 对象，因此使用 `read_json` 函数并带有 `lines=True` 参数。

它从 DataFrame 中随机抽取一个样本行。使用 `sample` 函数并带有 `n=1` 参数来指定要选择的随机行数。

它重置 DataFrame 的索引。使用 `reset_index` 函数并带有 `drop=True` 参数来删除原始索引，并用新的默认整数值索引替换。

它使用 `head` 函数并带有参数 `2` 显示 DataFrame 的前两行。然而，由于在抽样后 DataFrame 只包含一行，因此只会显示这一行。

总结一下，这个脚本将 JSON Lines 文件读取到 pandas DataFrame 中，随机抽取一行样本，重置索引，并显示第一行。

```python
# 导入 pandas 库
import pandas as pd

# 将 JSON Lines 文件 './ultrachat_200k_dataset/test_gen.jsonl' 读取到 pandas DataFrame 中
# 'lines=True' 参数表示文件是 JSON Lines 格式，其中每一行都是一个独立的 JSON 对象
test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)

# 从 DataFrame 中随机抽取一行样本
# 'n=1' 参数指定要选择的随机行数
test_df = test_df.sample(n=1)

# 重置 DataFrame 的索引
# 'drop=True' 参数表示应该删除原始索引并用新的默认整数值索引替换
# 'inplace=True' 参数表示应该直接修改 DataFrame（而不是创建一个新对象）
test_df.reset_index(drop=True, inplace=True)

# 显示 DataFrame 的前两行
# 由于在抽样后 DataFrame 只包含一行，因此只会显示这一行
test_df.head(2)
```

### 创建 JSON 对象

这个 Python 脚本创建一个带有特定参数的 JSON 对象并将其保存到一个文件中。以下是它的具体操作步骤：

它导入 `json` 模块，该模块提供了处理 JSON 数据的函数。

它创建一个字典 `parameters`，其中包含代表机器学习模型参数的键值对。键包括 "temperature"、"top_p"、"do_sample" 和 "max_new_tokens"，相应的值分别为 0.6、0.9、True 和 200。

它创建另一个字典 `test_json`，包含两个键："input_data" 和 "params"。"input_data" 的值是另一个字典，包含键 "input_string" 和 "parameters"。"input_string" 的值是一个列表，包含来自 `test_df` DataFrame 的第一条消息。"parameters" 的值是先前创建的 `parameters` 字典。"params" 的值是一个空字典。

它打开一个名为 `sample_score.json` 的文件，并将 `test_json` 字典以 JSON 格式写入文件中。

```python
# 导入 json 模块，该模块提供了处理 JSON 数据的函数
import json

# 创建一个字典 `parameters`，其中包含代表机器学习模型参数的键值对
# 键包括 "temperature"、"top_p"、"do_sample" 和 "max_new_tokens"，相应的值分别为 0.6、0.9、True 和 200
parameters = {
    "temperature": 0.6,
    "top_p": 0.9,
    "do_sample": True,
    "max_new_tokens": 200,
}

# 创建另一个字典 `test_json`，包含两个键："input_data" 和 "params"
# "input_data" 的值是另一个字典，包含键 "input_string" 和 "parameters"
# "input_string" 的值是一个列表，包含来自 `test_df` DataFrame 的第一条消息
# "parameters" 的值是先前创建的 `parameters` 字典
# "params" 的值是一个空字典
test_json = {
    "input_data": {
        "input_string": [test_df["messages"][0]],
        "parameters": parameters,
    },
    "params": {},
}

# 打开一个名为 `./ultrachat_200k_dataset/sample_score.json` 的文件，写入模式
with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
    # 使用 `json.dump` 函数将 `test_json` 字典以 JSON 格式写入文件中
    json.dump(test_json, f)
```

### 调用端点

这个 Python 脚本在 Azure 机器学习中调用一个在线端点来对 JSON 文件进行评分。以下是它的具体操作步骤：

它调用 `workspace_ml_client` 对象的 `online_endpoints` 属性的 `invoke` 方法。该方法用于向在线端点发送请求并获得响应。

它使用 `endpoint_name` 和 `deployment_name` 参数指定端点和部署的名称。在此示例中，端点名称存储在 `online_endpoint_name` 变量中，部署名称为 "demo"。

它使用 `request_file` 参数指定要评分的 JSON 文件的路径。在此示例中，文件路径为 `./ultrachat_200k_dataset/sample_score.json`。

它将端点的响应存储在 `response` 变量中。

它打印原始响应。

总结一下，这个脚本在 Azure 机器学习中调用一个在线端点来对 JSON 文件进行评分，并打印响应。

```python
# 调用 Azure 机器学习中的在线端点对 `sample_score.json` 文件进行评分
# 使用 `workspace_ml_client` 对象的 `online_endpoints` 属性的 `invoke` 方法向在线端点发送请求并获得响应
# `endpoint_name` 参数指定端点的名称，存储在 `online_endpoint_name` 变量中
# `deployment_name` 参数指定部署的名称，这里是 "demo"
# `request_file` 参数指定要评分的 JSON 文件的路径，这里是 `./ultrachat_200k_dataset/sample_score.json`
response = workspace_ml_client.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    deployment_name="demo",
    request_file="./ultrachat_200k_dataset/sample_score.json",
)

# 打印端点的原始响应
print("raw response: \n", response, "\n")
```

### 删除在线端点

不要忘记删除在线端点，否则将会继续为端点使用的计算资源计费。这段 Python 代码用于删除 Azure 机器学习中的在线端点。以下是它的具体操作步骤：

它调用 `workspace_ml_client` 对象的 `online_endpoints` 属性的 `begin_delete` 方法。该方法用于开始删除在线端点的操作。

它使用 `name` 参数指定要删除的端点的名称。此示例中，端点名称存储在 `online_endpoint_name` 变量中。

它调用 `wait` 方法等待删除操作完成。这是一个阻塞操作，意味着在删除完成之前，脚本将不会继续执行。

总结一下，这行代码开始删除 Azure 机器学习中的在线端点，并等待操作完成。

```python
# 删除 Azure 机器学习中的在线端点
# 使用 `workspace_ml_client` 对象的 `online_endpoints` 属性的 `begin_delete` 方法开始删除在线端点的操作
# `name` 参数指定要删除的端点的名称，存储在 `online_endpoint_name` 变量中
# 调用 `wait` 方法等待删除操作完成。这是一个阻塞操作，意味着在删除完成之前，脚本将不会继续执行
workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
```