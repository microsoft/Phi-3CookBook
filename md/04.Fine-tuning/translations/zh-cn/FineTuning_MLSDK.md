## 如何使用Azure ML系统注册表中的聊天补全组件来微调模型

在这个示例中，我们将使用ultrachat_200k数据集对Phi-3-mini-4k-instruct模型进行微调，以完成两个人之间的对话。

![MLFineTune](../../../../imgs/04/03/MLFineTune.png)

在这个示例中，我们将展示如何使用Azure ML SDK和Python进行微调，然后将微调后的模型部署到一个在线端点以进行实时推理。

### 训练数据
我们将使用ultrachat_200k数据集。这是UltraChat数据集的一个经过严格筛选的版本，用于训练Zephyr-7B-β，一款最先进的7b聊天模型。

### 模型
我们将使用Phi-3-mini-4k-instruct模型来展示用户如何为聊天补全任务微调模型。如果您从特定的模型卡片打开了此notebook文件，请记住替换特定的模型名称。

### 任务 
- 选择一个模型来微调
- 选择并浏览训练数据
- 配置微调任务
- 运行微调任务
- 检查训练和评估指标
- 注册微调后的模型
- 部署微调后的模型，用于实时推理
- 清除资源


## 1. 设置先决条件
- 安装依赖项
- 连接到 AzureML 工作区。在设置 SDK 身份验证处了解更多信息。请替换下面的 <WORKSPACE_NAME>, <RESOURCE_GROUP> 和 <SUBSCRIPTION_ID>
- 连接到 azureml 系统注册表
- 设置一个可选的实验名称
- 检查或创建计算资源

单个 GPU 节点可以具有多个 GPU 卡。例如，在一个 Standard_NC24rs_v3 节点中有 4 个 NVIDIA V100 GPU，而在 Standard_NC12s_v3 节点中有 2 个 NVIDIA V100 GPU。请参阅文档以获取此信息。每个节点的 GPU 卡数量在下面的 gpus_per_node 参数中设置。正确设置此值将确保节点中所有 GPU 的利用率。推荐的 GPU 计算 SKU 可以在这里和这里找到。

### Python 库

通过运行以下单元格来安装依赖项。如果在新环境中运行，此步骤不是可选的。

```
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```
### 与 Azure ML 交互 

这个 Python 脚本用于与 Azure 机器学习（Azure ML）服务交互。以下是它的功能分解：
它从 azure.ai.ml，azure.identity 和 azure.ai.ml.entities 包中导入必要的模块。它还导入了 time 模块。

它尝试使用 DefaultAzureCredential() 进行身份验证，这提供了简化的身份验证体验，以快速开始开发在 Azure 云中运行的应用程序。如果失败，它将回退到 InteractiveBrowserCredential()，该方法提供交互式登录提示。

然后，它尝试使用 from_config 方法创建一个 MLClient 实例，该方法从默认配置文件（config.json）中读取配置。如果失败，它通过手动提供 subscription_id、resource_group_name 和 workspace_name 创建一个 MLClient 实例。

它创建另一个 MLClient 实例，这次是名为 "azureml" 的 Azure ML 注册表。这个注册表是存储模型、微调管道和环境的地方。

它将 experiment_name 设置为 "chat_completion_Phi-3-mini-4k-instruct"。

它通过将当前时间（自纪元以来的秒数，作为浮点数）转换为整数，然后转换为字符串，生成一个唯一的时间戳。这个时间戳可用于创建唯一的名称和版本。

```
# Import necessary modules from Azure ML and Azure Identity
from azure.ai.ml import MLClient
from azure.identity import (
    DefaultAzureCredential,
    InteractiveBrowserCredential,
)
from azure.ai.ml.entities import AmlCompute
import time  # Import time module

# Try to authenticate using DefaultAzureCredential
try:
    credential = DefaultAzureCredential()
    credential.get_token("https://management.azure.com/.default")
except Exception as ex:  # If DefaultAzureCredential fails, use InteractiveBrowserCredential
    credential = InteractiveBrowserCredential()

# Try to create an MLClient instance using the default config file
try:
    workspace_ml_client = MLClient.from_config(credential=credential)
except:  # If that fails, create an MLClient instance by manually providing the details
    workspace_ml_client = MLClient(
        credential,
        subscription_id="<SUBSCRIPTION_ID>",
        resource_group_name="<RESOURCE_GROUP>",
        workspace_name="<WORKSPACE_NAME>",
    )

# Create another MLClient instance for the Azure ML registry named "azureml"
# This registry is where models, fine-tuning pipelines, and environments are stored
registry_ml_client = MLClient(credential, registry_name="azureml")

# Set the experiment name
experiment_name = "chat_completion_Phi-3-mini-4k-instruct"

# Generate a unique timestamp that can be used for names and versions that need to be unique
timestamp = str(int(time.time()))
```
## 2. 选择一个基础模型进行微调
Phi-3-mini-4k-instruct 是一个基于 Phi-2 的数据集构建的、具有 38 亿参数的轻量级、最先进的开放模型。该模型属于 Phi-3 模型家族，Mini 版本有两种变体：4K 和 128K，这是它所支持的上下文长度（以 tokens 为单位）。为了使用它，我们需要为特定目的微调模型。您可以在 AzureML Studio 的模型目录中浏览这些模型，按 chat-completion 任务进行筛选。在此示例中，我们使用 Phi-3-mini-4k-instruct 模型。如果您为其他模型打开了此Jupyter notebook文件，请相应地替换模型名称和版本。

注意模型的 model id 属性。这将作为微调任务的输入。这也可以在 AzureML Studio 模型目录中的模型详细信息页面的 Asset ID 字段中找到。

此 Python 脚本正在与 Azure 机器学习（Azure ML）服务进行交互。以下是它的功能分解：

它将 model_name 设置为 "Phi-3-mini-4k-instruct"。

它使用 registry_ml_client 对象的 models 属性的 get 方法从 Azure ML 注册表中检索具有指定名称的最新版本模型。get 方法使用时包含两个参数：模型名称和标签，用于指定应检索模型的最新版本。

它向控制台打印一条消息，指示将用于微调的模型的名称、版本和 ID。字符串的 format 方法用于将模型的名称、版本和 ID 插入到消息中。模型的名称、版本和 ID 作为 foundation_model 对象的属性进行访问。

```
# Set the model name
model_name = "Phi-3-mini-4k-instruct"

# Get the latest version of the model from the Azure ML registry
foundation_model = registry_ml_client.models.get(model_name, label="latest")

# Print the model name, version, and id
# This information is useful for tracking and debugging
print(
    "\n\nUsing model name: {0}, version: {1}, id: {2} for fine tuning".format(
        foundation_model.name, foundation_model.version, foundation_model.id
    )
)
```
## 3. 创建一个与任务一起使用的计算实例
微调任务仅适用于 GPU 计算。计算实例的大小取决于模型的大小，在大多数情况下，确定合适的计算实例对于任务来说是一件棘手的事情。在这里，我们将引导用户为任务选择合适的计算实例。

**注意1** 下面列出的计算实例适用于最优化配置。对配置进行任何更改可能导致 Cuda 内存不足的错误。在这种情况下，请尝试将计算实例升级到更大的计算实例。

**注意2** 在选择下面的 compute_cluster_size 时，请确保计算实例在您的资源组中可用。如果某个特定的计算实例不可用，您可以发出请求以获取计算资源的访问权限。

### 检查模型以支持微调
这个 Python 脚本与 Azure 机器学习（Azure ML）模型进行交互。以下是它的功能分解：

它导入了 ast 模块，该模块提供了处理 Python 抽象语法树的功能。

它检查 foundation_model 对象（代表 Azure ML 中的一个模型）是否具有名为 finetune_compute_allow_list 的标签。在 Azure ML 中，标签是您可以创建并用于过滤和排序模型的键值对。

如果存在 finetune_compute_allow_list 标签，它将使用 ast.literal_eval 函数安全地将标签的值（字符串）解析为 Python 列表。然后将此列表分配给 computes_allow_list 变量。接着，它会打印一条消息，指示应该从列表中创建一个计算实例。

如果 finetune_compute_allow_list 标签不存在，它会将 computes_allow_list 设置为 None，并打印一条消息，表示 finetune_compute_allow_list 标签不是模型标签的一部分。

总之，此脚本检查模型元数据中的特定标签，如果存在，将标签的值转换为列表，并相应地向用户提供反馈。

```
# Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
import ast

# Check if the 'finetune_compute_allow_list' tag is present in the model's tags
if "finetune_compute_allow_list" in foundation_model.tags:
    # If the tag is present, use ast.literal_eval to safely parse the tag's value (a string) into a Python list
    computes_allow_list = ast.literal_eval(
        foundation_model.tags["finetune_compute_allow_list"]
    )  # convert string to python list
    # Print a message indicating that a compute should be created from the list
    print(f"Please create a compute from the above list - {computes_allow_list}")
else:
    # If the tag is not present, set computes_allow_list to None
    computes_allow_list = None
    # Print a message indicating that the 'finetune_compute_allow_list' tag is not part of the model's tags
    print("`finetune_compute_allow_list` is not part of model tags")
```
### 检查计算实例

这个 Python 脚本与 Azure 机器学习（Azure ML）服务进行交互，并对计算实例执行多个检查。以下是它的功能分解：

它尝试从 Azure ML 工作区中检索存储在 compute_cluster 中的计算实例的名称。如果计算实例的配置状态为 "failed"，则抛出 ValueError。

它检查 computes_allow_list 是否不为 None。如果不是，它将列表中所有计算实例大小转换为小写，并检查当前计算实例的大小是否在列表中。如果不在，则抛出 ValueError。

如果 computes_allow_list 为 None，它会检查计算实例的大小是否在一个不支持的 GPU 虚拟机大小列表中。如果是，则抛出 ValueError。

它检索工作区中所有可用计算实例大小的列表。然后遍历此列表，对于每个计算实例大小，它检查其名称是否与当前计算实例的大小匹配。如果匹配，它检索该计算实例大小的 GPU 数量，并将 gpu_count_found 设置为 True。

如果 gpu_count_found 为 True，它会打印计算实例中的 GPU 数量。如果 gpu_count_found 为 False，则抛出 ValueError。

总之，此脚本对 Azure ML 工作区中的计算实例执行多个检查，包括检查其配置状态、其大小与允许列表或拒绝列表的对比以及它拥有的 GPU 数量。

```
# Print the exception message
print(e)
# Raise a ValueError if the compute size is not available in the workspace
raise ValueError(
    f"WARNING! Compute size {compute_cluster_size} not available in workspace"
)

# Retrieve the compute instance from the Azure ML workspace
compute = workspace_ml_client.compute.get(compute_cluster)
# Check if the provisioning state of the compute instance is "failed"
if compute.provisioning_state.lower() == "failed":
    # Raise a ValueError if the provisioning state is "failed"
    raise ValueError(
        f"Provisioning failed, Compute '{compute_cluster}' is in failed state. "
        f"please try creating a different compute"
    )

# Check if computes_allow_list is not None
if computes_allow_list is not None:
    # Convert all compute sizes in computes_allow_list to lowercase
    computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
    # Check if the size of the compute instance is in computes_allow_list_lower_case
    if compute.size.lower() not in computes_allow_list_lower_case:
        # Raise a ValueError if the size of the compute instance is not in computes_allow_list_lower_case
        raise ValueError(
            f"VM size {compute.size} is not in the allow-listed computes for finetuning"
        )
else:
    # Define a list of unsupported GPU VM sizes
    unsupported_gpu_vm_list = [
        "standard_nc6",
        "standard_nc12",
        "standard_nc24",
        "standard_nc24r",
    ]
    # Check if the size of the compute instance is in unsupported_gpu_vm_list
    if compute.size.lower() in unsupported_gpu_vm_list:
        # Raise a ValueError if the size of the compute instance is in unsupported_gpu_vm_list
        raise ValueError(
            f"VM size {compute.size} is currently not supported for finetuning"
        )

# Initialize a flag to check if the number of GPUs in the compute instance has been found
gpu_count_found = False
# Retrieve a list of all available compute sizes in the workspace
workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
available_sku_sizes = []
# Iterate over the list of available compute sizes
for compute_sku in workspace_compute_sku_list:
    available_sku_sizes.append(compute_sku.name)
    # Check if the name of the compute size matches the size of the compute instance
    if compute_sku.name.lower() == compute.size.lower():
        # If it does, retrieve the number of GPUs for that compute size and set gpu_count_found to True
        gpus_per_node = compute_sku.gpus
        gpu_count_found = True
# If gpu_count_found is True, print the number of GPUs in the compute instance
if gpu_count_found:
    print(f"Number of GPU's in compute {compute.size}: {gpus_per_node}")
else:
    # If gpu_count_found is False, raise a ValueError
    raise ValueError(
        f"Number of GPU's in compute {compute.size} not found. Available skus are: {available_sku_sizes}."
        f"This should not happen. Please check the selected compute cluster: {compute_cluster} and try again."
    )
```

## 4. 为模型微调选择数据集

我们使用 ultrachat_200k 数据集。该数据集有四个划分，适用于：

监督式微调（sft）。生成排名（gen）。每个划分的示例数量如下所示:
| | | | |
|-|-|-|-|
| train_sft | test_sft | train_gen | test_gen |
| 207865 | 23110 | 256032 | 28304 |
| | | | |

接下来的几个单元格显示了微调的基本数据准备：

可视化一些数据行
我们希望这个示例运行得快一些，所以保存包含 5% 已裁剪行的 train_sft、test_sft 文件。这意味着微调的模型将具有较低的准确性，因此它不应投入现实世界的使用中。
download-dataset.py 用于下载 ultrachat_200k 数据集并将数据集转换为微调管道组件可消费的格式。此外，由于数据集较大，因此这里只有部分数据集。

运行下面的脚本只会下载 5% 的数据。通过将 dataset_split_pc 参数更改为所需的百分比来增加这个比例。

**注意:** 某些语言模型具有不同的语言代码，因此数据集中的列名应反映相同的内容。

以下是数据应该如何显示的示例，聊天补全数据集以 parquet 格式存储，每个条目使用以下模式：

这是一个 JSON（JavaScript 对象表示法）文档，它是一种流行的数据交换格式。它不是可执行代码，而是存储和传输数据的一种方式。以下是其结构的分解：

"prompt": 此键包含一个字符串值，表示提出给 AI 助手的任务或问题。

"messages": 此键包含一个对象数组。每个对象表示用户与 AI 助手之间的对话中的一条消息。每个消息对象有两个键：

"content": 此键包含一个字符串值，表示消息的内容。
"role": 此键包含一个字符串值，表示发送消息的实体的角色。它可以是“user”或“assistant”。
"prompt_id": 此键包含一个字符串值，表示提示的唯一标识符。

在这个特定的 JSON 文档中，表示一个对话，用户要求 AI 助手为反乌托邦故事创建一个主角。助手回应，然后用户要求提供更多细节。助手同意提供更多细节。整个对话与特定的提示 id 关联。

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

它导入了 os 模块，该模块提供了一种使用操作系统相关功能的便携方式。

它使用 os.system 函数在 shell 中使用特定的命令行参数运行 download-dataset.py 脚本。参数指定要下载的数据集（HuggingFaceH4/ultrachat_200k）、下载目录（ultrachat_200k_dataset）以及要拆分的数据集百分比（5）。os.system 函数返回它执行的命令的退出状态；此状态存储在 exit_status 变量中。

它检查 exit_status 是否不为 0。在类 Unix 操作系统中，退出状态为 0 通常表示命令已成功，而其他任何数字表示错误。如果 exit_status 不为 0，它将引发一个异常，消息指示下载数据集时发生错误。

总之，此脚本运行一个命令，使用辅助脚本下载数据集，并在命令失败时引发异常。

```
# Import the os module, which provides a way of using operating system dependent functionality
import os

# Use the os.system function to run the download-dataset.py script in the shell with specific command-line arguments
# The arguments specify the dataset to download (HuggingFaceH4/ultrachat_200k), the directory to download it to (ultrachat_200k_dataset), and the percentage of the dataset to split (5)
# The os.system function returns the exit status of the command it executed; this status is stored in the exit_status variable
exit_status = os.system(
    "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
)

# Check if exit_status is not 0
# In Unix-like operating systems, an exit status of 0 usually indicates that a command has succeeded, while any other number indicates an error
# If exit_status is not 0, raise an Exception with a message indicating that there was an error downloading the dataset
if exit_status != 0:
    raise Exception("Error downloading dataset")
```
### 将数据加载到 DataFrame
这个 Python 脚本将一个 JSON Lines 文件加载到 pandas DataFrame 中，并显示前 5 行。以下是它的功能分解：

它导入了 pandas 库，这是一个强大的数据操作和分析库。

它将 pandas 的显示选项的最大列宽设置为 0。这意味着当打印 DataFrame 时，每列的完整文本将不被截断地显示。

它使用 pd.read_json 函数将 train_sft.jsonl 文件从 ultrachat_200k_dataset 目录加载到 DataFrame 中。lines=True 参数表示该文件采用 JSON Lines 格式，其中每行是一个单独的 JSON 对象。

它使用 head 方法显示 DataFrame 的前 5 行。如果 DataFrame 少于 5 行，则显示所有行。

总之，此脚本将一个 JSON Lines 文件加载到 DataFrame 中并显示前 5 行的完整列文本。

```
# Import the pandas library, which is a powerful data manipulation and analysis library
import pandas as pd

# Set the maximum column width for pandas' display options to 0
# This means that the full text of each column will be displayed without truncation when the DataFrame is printed
pd.set_option("display.max_colwidth", 0)

# Use the pd.read_json function to load the train_sft.jsonl file from the ultrachat_200k_dataset directory into a DataFrame
# The lines=True argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)

# Use the head method to display the first 5 rows of the DataFrame
# If the DataFrame has less than 5 rows, it will display all of them
df.head()
```
## 5. 将模型和数据作为数据提交给微调任务
创建使用聊天补全管道组件的任务。了解更多关于微调支持的所有参数的信息。

### 定义微调参数

微调参数可以分为两类 - 训练参数和优化参数。

训练参数定义了训练方面的内容，例如 -

- 要使用的优化器和调度器
- 优化微调的指标
- 训练步数、批量大小等
- 优化参数有助于优化 GPU 内存并有效使用计算资源。

以下是属于这一类别的一些参数。对于每个模型，优化参数都有所不同，并与模型一起打包以处理这些差异。

- 启用 deepspeed 和 LoRA
- 启用混合精度训练
- 启用多节点训练

**注意:** 监督式微调可能导致失去对齐或灾难性遗忘。我们建议在微调后检查这个问题并运行对齐阶段。

### 微调参数

这个 Python 脚本为微调机器学习模型设置参数。以下是它的功能分解：

它设置了默认的训练参数，如训练周期数、训练和评估的批量大小、学习率和学习率调度器类型。

它设置了默认的优化参数，例如，是否应用逐层相关传播（LoRa）和 DeepSpeed，以及 DeepSpeed 阶段。

它将训练和优化参数合并到一个名为 finetune_parameters 的字典中。

它检查 foundation_model 是否有任何模型特定的默认参数。如果有，它会打印一个警告消息，并使用这些模型特定的默认值更新 finetune_parameters 字典。ast.literal_eval 函数用于将模型特定的默认值从字符串转换为 Python 字典。

它打印将用于运行的微调参数的最终集合。

总之，这个脚本用于设置和显示微调机器学习模型的参数，并能够用模型特定的参数覆盖默认参数。

```
# Set up default training parameters such as the number of training epochs, batch sizes for training and evaluation, learning rate, and learning rate scheduler type
training_parameters = dict(
    num_train_epochs=3,
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    learning_rate=5e-6,
    lr_scheduler_type="cosine",
)

# Set up default optimization parameters such as whether to apply Layer-wise Relevance Propagation (LoRa) and DeepSpeed, and the DeepSpeed stage
optimization_parameters = dict(
    apply_lora="true",
    apply_deepspeed="true",
    deepspeed_stage=2,
)

# Combine the training and optimization parameters into a single dictionary called finetune_parameters
finetune_parameters = {**training_parameters, **optimization_parameters}

# Check if the foundation_model has any model-specific default parameters
# If it does, print a warning message and update the finetune_parameters dictionary with these model-specific defaults
# The ast.literal_eval function is used to convert the model-specific defaults from a string to a Python dictionary
if "model_specific_defaults" in foundation_model.tags:
    print("Warning! Model specific defaults exist. The defaults could be overridden.")
    finetune_parameters.update(
        ast.literal_eval(  # convert string to python dict
            foundation_model.tags["model_specific_defaults"]
        )
    )

# Print the final set of fine-tuning parameters that will be used for the run
print(
    f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
)
```

### 训练管道
这个 Python 脚本定义了一个函数，用于生成机器学习训练管道的显示名称，然后调用此函数生成并打印显示名称。以下是它的功能分解：

定义了 get_pipeline_display_name 函数。此函数根据与训练管道相关的各种参数生成显示名称。

在函数内部，通过将每个设备的批量大小、梯度累积步数、每个节点的 GPU 数量和用于微调的节点数量相乘，计算总批量大小。

它检索各种其他参数，如学习率调度器类型、是否应用 DeepSpeed、DeepSpeed 阶段、是否应用逐层相关传播（LoRa）、要保留的模型检查点数量的限制以及最大序列长度。

它构造了一个包含所有这些参数的字符串，参数之间用短横线分隔。如果应用了 DeepSpeed 或 LoRa，字符串分别包括 "ds" 后跟 DeepSpeed 阶段，或 "lora"。如果没有，则分别包括 "nods" 或 "nolora"。

该函数返回此字符串，该字符串作为训练管道的显示名称。

在定义了函数之后，调用它以生成显示名称，然后打印该名称。

总之，这个脚本根据各种参数生成机器学习训练管道的显示名称，并打印该显示名称。

```
# Define a function to generate a display name for the training pipeline
def get_pipeline_display_name():
    # Calculate the total batch size by multiplying the per-device batch size, the number of gradient accumulation steps, the number of GPUs per node, and the number of nodes used for fine-tuning
    batch_size = (
        int(finetune_parameters.get("per_device_train_batch_size", 1))
        * int(finetune_parameters.get("gradient_accumulation_steps", 1))
        * int(gpus_per_node)
        * int(finetune_parameters.get("num_nodes_finetune", 1))
    )
    # Retrieve the learning rate scheduler type
    scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
    # Retrieve whether DeepSpeed is applied
    deepspeed = finetune_parameters.get("apply_deepspeed", "false")
    # Retrieve the DeepSpeed stage
    ds_stage = finetune_parameters.get("deepspeed_stage", "2")
    # If DeepSpeed is applied, include "ds" followed by the DeepSpeed stage in the display name; if not, include "nods"
    if deepspeed == "true":
        ds_string = f"ds{ds_stage}"
    else:
        ds_string = "nods"
    # Retrieve whether Layer-wise Relevance Propagation (LoRa) is applied
    lora = finetune_parameters.get("apply_lora", "false")
    # If LoRa is applied, include "lora" in the display name; if not, include "nolora"
    if lora == "true":
        lora_string = "lora"
    else:
        lora_string = "nolora"
    # Retrieve the limit on the number of model checkpoints to keep
    save_limit = finetune_parameters.get("save_total_limit", -1)
    # Retrieve the maximum sequence length
    seq_len = finetune_parameters.get("max_seq_length", -1)
    # Construct the display name by concatenating all these parameters, separated by hyphens
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

# Call the function to generate the display name
pipeline_display_name = get_pipeline_display_name()
# Print the display name
print(f"Display name used for the run: {pipeline_display_name}")
```
### 配置管道

这个 Python 脚本使用 Azure Machine Learning SDK 定义和配置机器学习管道。以下是它的功能分解：

1. 它从 Azure AI ML SDK 导入必要的模块。

2. 它从注册表中获取名为 "chat_completion_pipeline" 的管道组件。

3. 它使用 `@pipeline` 装饰器和 `create_pipeline`函数定义一个管道作业。管道的名称设置为 `pipeline_display_name`。

4. 在 `create_pipeline` 函数内部，它使用各种参数初始化获取的管道组件，包括模型路径、不同阶段的计算集群、用于训练和测试的数据集拆分、用于微调的 GPU 数量以及其他微调参数。

5. 它将微调作业的输出映射到管道作业的输出。这样做是为了使微调后的模型可以轻松注册，这是将模型部署到在线或批处理端点所必需的。

6. 通过调用 `create_pipeline` 函数创建管道实例。

7. 它将管道的 `force_rerun` 设置为 `True`, 这意味着不会使用先前作业的缓存结果。

8. 它将管道的 `continue_on_step_failure` 设置为 `False`, 这意味着如果任何步骤失败，管道将停止。

总之，这个脚本使用 Azure Machine Learning SDK为聊天补全任务定义和配置机器学习管道。

```
# Import necessary modules from the Azure AI ML SDK
from azure.ai.ml.dsl import pipeline
from azure.ai.ml import Input

# Fetch the pipeline component named "chat_completion_pipeline" from the registry
pipeline_component_func = registry_ml_client.components.get(
    name="chat_completion_pipeline", label="latest"
)

# Define the pipeline job using the @pipeline decorator and the function create_pipeline
# The name of the pipeline is set to pipeline_display_name
@pipeline(name=pipeline_display_name)
def create_pipeline():
    # Initialize the fetched pipeline component with various parameters
    # These include the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters
    chat_completion_pipeline = pipeline_component_func(
        mlflow_model_path=foundation_model.id,
        compute_model_import=compute_cluster,
        compute_preprocess=compute_cluster,
        compute_finetune=compute_cluster,
        compute_model_evaluation=compute_cluster,
        # Map the dataset splits to parameters
        train_file_path=Input(
            type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
        ),
        test_file_path=Input(
            type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
        ),
        # Training settings
        number_of_gpu_to_use_finetuning=gpus_per_node,  # Set to the number of GPUs available in the compute
        **finetune_parameters
    )
    return {
        # Map the output of the fine tuning job to the output of pipeline job
        # This is done so that we can easily register the fine tuned model
        # Registering the model is required to deploy the model to an online or batch endpoint
        "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
    }

# Create an instance of the pipeline by calling the create_pipeline function
pipeline_object = create_pipeline()

# Don't use cached results from previous jobs
pipeline_object.settings.force_rerun = True

# Set continue on step failure to False
# This means that the pipeline will stop if any step fails
pipeline_object.settings.continue_on_step_failure = False
```
### 提交任务

这个 Python 脚本将机器学习管道任务提交到 Azure 机器学习工作区，然后等待任务完成。以下是它的功能分解：

它调用 workspace_ml_client 中 jobs 对象的 create_or_update 方法提交管道任务。要运行的管道由 pipeline_object 指定，任务运行所在的实验由 experiment_name 指定。

然后，它调用 workspace_ml_client 中 jobs 对象的 stream 方法等待管道任务完成。要等待的任务由 pipeline_job 对象的 name 属性指定。

总之，这个脚本将机器学习管道任务提交到 Azure 机器学习工作区，然后等待任务完成。

```
# Submit the pipeline job to the Azure Machine Learning workspace
# The pipeline to be run is specified by pipeline_object
# The experiment under which the job is run is specified by experiment_name
pipeline_job = workspace_ml_client.jobs.create_or_update(
    pipeline_object, experiment_name=experiment_name
)

# Wait for the pipeline job to complete
# The job to wait for is specified by the name attribute of the pipeline_job object
workspace_ml_client.jobs.stream(pipeline_job.name)
```

## 6. 为微调模型注册工作空间
我们将从微调任务的输出中注册模型。这将在微调模型和微调任务之间跟踪脉络。此外，微调任务还跟踪基础模型、数据和训练代码的脉络。

### 注册 ML 模型
这个 Python 脚本注册了在 Azure 机器学习管道中训练的机器学习模型。以下是它的功能分解:

它从 Azure AI ML SDK 导入必要的模块。

它通过调用 workspace_ml_client 中 jobs 对象的 get 方法并访问其 outputs 属性，检查 trained_model 输出是否可从管道任务中获取。

它通过使用管道任务的名称和输出（"trained_model"）的名称来格式化字符串，构造指向训练模型的路径。

它通过将 "-ultrachat-200k" 附加到原始模型名称并将任何斜线替换为短划线，为微调后的模型定义一个名称。

它通过创建一个 Model 对象并使用各种参数（包括模型路径、模型类型（MLflow 模型）、模型的名称和版本以及模型的描述）来准备注册模型。

它通过将 Model 对象作为参数调用 workspace_ml_client 中 models 对象的 create_or_update 方法来注册模型。

它打印已注册的模型。

总之，这个脚本正在注册一个在 Azure 机器学习管道中训练的机器学习模型。

```
# Import necessary modules from the Azure AI ML SDK
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes

# Check if the `trained_model` output is available from the pipeline job
print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)

# Construct a path to the trained model by formatting a string with the name of the pipeline job and the name of the output ("trained_model")
model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
    pipeline_job.name, "trained_model"
)

# Define a name for the fine-tuned model by appending "-ultrachat-200k" to the original model name and replacing any slashes with hyphens
finetuned_model_name = model_name + "-ultrachat-200k"
finetuned_model_name = finetuned_model_name.replace("/", "-")

print("path to register model: ", model_path_from_job)

# Prepare to register the model by creating a Model object with various parameters
# These include the path to the model, the type of the model (MLflow model), the name and version of the model, and a description of the model
prepare_to_register_model = Model(
    path=model_path_from_job,
    type=AssetTypes.MLFLOW_MODEL,
    name=finetuned_model_name,
    version=timestamp,  # Use timestamp as version to avoid version conflict
    description=model_name + " fine tuned model for ultrachat 200k chat-completion",
)

print("prepare to register model: \n", prepare_to_register_model)

# Register the model by calling the create_or_update method of the models object in the workspace_ml_client with the Model object as the argument
registered_model = workspace_ml_client.models.create_or_update(
    prepare_to_register_model
)

# Print the registered model
print("registered model: \n", registered_model)
```
## 7. 将微调后的模型部署到一个在线端点
在线端点提供了一个持久的 REST API，可用于与需要使用模型的应用程序集成。

### 管理端点
这个 Python 脚本在 Azure 机器学习中为已注册的模型创建一个托管在线端点。以下是它的功能分解：

它从 Azure AI ML SDK 导入必要的模块。

它通过将时间戳附加到字符串 "ultrachat-completion-" 来为在线端点定义一个唯一名称。

它通过创建一个 ManagedOnlineEndpoint 对象并使用各种参数（包括端点名称、端点描述和身份验证模式（“key”））来准备创建在线端点。

它通过将 ManagedOnlineEndpoint 对象作为参数调用 workspace_ml_client 的 begin_create_or_update 方法来创建在线端点。然后，通过调用 wait 方法等待创建操作完成。

总之，这个脚本在 Azure 机器学习中为已注册的模型创建一个托管在线端点。

```
# Import necessary modules from the Azure AI ML SDK
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    ProbeSettings,
    OnlineRequestSettings,
)

# Define a unique name for the online endpoint by appending a timestamp to the string "ultrachat-completion-"
online_endpoint_name = "ultrachat-completion-" + timestamp

# Prepare to create the online endpoint by creating a ManagedOnlineEndpoint object with various parameters
# These include the name of the endpoint, a description of the endpoint, and the authentication mode ("key")
endpoint = ManagedOnlineEndpoint(
    name=online_endpoint_name,
    description="Online endpoint for "
    + registered_model.name
    + ", fine tuned model for ultrachat-200k-chat-completion",
    auth_mode="key",
)

# Create the online endpoint by calling the begin_create_or_update method of the workspace_ml_client with the ManagedOnlineEndpoint object as the argument
# Then wait for the creation operation to complete by calling the wait method
workspace_ml_client.begin_create_or_update(endpoint).wait()
```
您可以在这里找到SKU支持的部署列表
- [Managed online endpoints SKU list](https://learn.microsoft.com/en-us/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### 部署ML模型

这个 Python 脚本将已注册的机器学习模型部署到 Azure 机器学习中的托管在线端点。以下是它的功能分解：

它导入了 ast 模块，该模块提供了处理 Python 抽象语法树的函数。

它将部署的实例类型设置为 "Standard_NC6s_v3"。

它检查基础模型中是否存在 inference_compute_allow_list 标签。如果存在，它将标签值从字符串转换为 Python 列表，并将其分配给 inference_computes_allow_list。如果不存在，它将 inference_computes_allow_list 设置为 None。

它检查指定的实例类型是否在允许列表中。如果不在，它会打印一条消息，要求用户从允许列表中选择一个实例类型。

它通过使用各种参数（包括部署名称、端点名称、模型 ID、实例类型和数量、活动探测器设置以及请求设置）创建一个 ManagedOnlineDeployment 对象来准备创建部署。

它通过将 ManagedOnlineDeployment 对象作为参数调用 workspace_ml_client 的 begin_create_or_update 方法来创建部署。然后，通过调用 wait 方法等待创建操作完成。

它将端点的流量设置为将 100% 的流量引导至 "demo" 部署。

它通过将端点对象作为参数调用 workspace_ml_client 的 begin_create_or_update 方法来更新端点。然后，通过调用 result 方法等待更新操作完成。

总之，这个脚本将已注册的机器学习模型部署到 Azure 机器学习中的托管在线端点。

```
# Import the ast module, which provides functions to process trees of the Python abstract syntax grammar
import ast

# Set the instance type for the deployment
instance_type = "Standard_NC6s_v3"

# Check if the `inference_compute_allow_list` tag is present in the foundation model
if "inference_compute_allow_list" in foundation_model.tags:
    # If it is, convert the tag value from a string to a Python list and assign it to `inference_computes_allow_list`
    inference_computes_allow_list = ast.literal_eval(
        foundation_model.tags["inference_compute_allow_list"]
    )
    print(f"Please create a compute from the above list - {computes_allow_list}")
else:
    # If it's not, set `inference_computes_allow_list` to `None`
    inference_computes_allow_list = None
    print("`inference_compute_allow_list` is not part of model tags")

# Check if the specified instance type is in the allow list
if (
    inference_computes_allow_list is not None
    and instance_type not in inference_computes_allow_list
):
    print(
        f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
    )

# Prepare to create the deployment by creating a `ManagedOnlineDeployment` object with various parameters
demo_deployment = ManagedOnlineDeployment(
    name="demo",
    endpoint_name=online_endpoint_name,
    model=registered_model.id,
    instance_type=instance_type,
    instance_count=1,
    liveness_probe=ProbeSettings(initial_delay=600),
    request_settings=OnlineRequestSettings(request_timeout_ms=90000),
)

# Create the deployment by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `ManagedOnlineDeployment` object as the argument
# Then wait for the creation operation to complete by calling the `wait` method
workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()

# Set the traffic of the endpoint to direct 100% of the traffic to the "demo" deployment
endpoint.traffic = {"demo": 100}

# Update the endpoint by calling the `begin_create_or_update` method of the `workspace_ml_client` with the `endpoint` object as the argument
# Then wait for the update operation to complete by calling the `result` method
workspace_ml_client.begin_create_or_update(endpoint).result()
```
## 8. 用示例数据测试端点
我们将从测试数据集中获取一些样本数据并提交给在线端点以进行推理。然后，我们将展示得分标签与实际标签并排显示。

### 读取结果
这个 Python 脚本将一个 JSON Lines 文件读取到 pandas DataFrame 中，随机抽取一个样本并重置索引。以下是它的功能分解：

它将文件 ./ultrachat_200k_dataset/test_gen.jsonl 读取到一个 pandas DataFrame 中。由于文件是 JSON Lines 格式，每行是一个单独的 JSON 对象，因此使用 read_json 函数并带有 lines=True 参数。

它从 DataFrame 中随机抽取一行。使用 sample 函数并带有 n=1 参数来指定要选择的随机行数。

它重置 DataFrame 的索引。使用 reset_index 函数并带有 drop=True 参数来删除原始索引并将其替换为默认整数值的新索引。

它使用带有参数 2 的 head 函数显示 DataFrame 的前两行。然而，由于在抽样后 DataFrame 只包含一行，所以这将只显示那一行。

总之，这个脚本将一个 JSON Lines 文件读取到 pandas DataFrame 中，随机抽取一行，重置索引并显示第一行。

```
# Import pandas library
import pandas as pd

# Read the JSON Lines file './ultrachat_200k_dataset/test_gen.jsonl' into a pandas DataFrame
# The 'lines=True' argument indicates that the file is in JSON Lines format, where each line is a separate JSON object
test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)

# Take a random sample of 1 row from the DataFrame
# The 'n=1' argument specifies the number of random rows to select
test_df = test_df.sample(n=1)

# Reset the index of the DataFrame
# The 'drop=True' argument indicates that the original index should be dropped and replaced with a new index of default integer values
# The 'inplace=True' argument indicates that the DataFrame should be modified in place (without creating a new object)
test_df.reset_index(drop=True, inplace=True)

# Display the first 2 rows of the DataFrame
# However, since the DataFrame only contains one row after the sampling, this will only display that one row
test_df.head(2)
```
### 创建 JSON 对象

这个 Python 脚本创建一个具有特定参数的 JSON 对象并将其保存到文件中。以下是它的功能分解：

它导入了 json 模块，该模块提供了处理 JSON 数据的函数。

它创建了一个名为 parameters 的字典，其中的键和值表示机器学习模型的参数。键分别为 "temperature"、"top_p"、"do_sample" 和 "max_new_tokens"，它们对应的值分别为 0.6、0.9、True 和 200。

它创建了另一个名为 test_json 的字典，包含两个键："input_data" 和 "params"。"input_data" 的值是另一个带有 "input_string" 和 "parameters" 键的字典。"input_string" 的值是一个包含 test_df DataFrame 中第一条消息的列表。"parameters" 的值是之前创建的 parameters 字典。"params" 的值是一个空字典。

它打开了一个名为 sample_score.json 的文件。

```
# Import the json module, which provides functions to work with JSON data
import json

# Create a dictionary `parameters` with keys and values that represent parameters for a machine learning model
# The keys are "temperature", "top_p", "do_sample", and "max_new_tokens", and their corresponding values are 0.6, 0.9, True, and 200 respectively
parameters = {
    "temperature": 0.6,
    "top_p": 0.9,
    "do_sample": True,
    "max_new_tokens": 200,
}

# Create another dictionary `test_json` with two keys: "input_data" and "params"
# The value of "input_data" is another dictionary with keys "input_string" and "parameters"
# The value of "input_string" is a list containing the first message from the `test_df` DataFrame
# The value of "parameters" is the `parameters` dictionary created earlier
# The value of "params" is an empty dictionary
test_json = {
    "input_data": {
        "input_string": [test_df["messages"][0]],
        "parameters": parameters,
    },
    "params": {},
}

# Open a file named `sample_score.json` in the `./ultrachat_200k_dataset` directory in write mode
with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
    # Write the `test_json` dictionary to the file in JSON format using the `json.dump` function
    json.dump(test_json, f)
```
### 调用端点

这个 Python 脚本调用 Azure 机器学习中的在线端点以对一个 JSON 文件进行评分。以下是它的功能分解：

它调用 workspace_ml_client 对象的 online_endpoints 属性的 invoke 方法。此方法用于向在线端点发送请求并获取响应。

它使用 endpoint_name 和 deployment_name 参数指定端点名称和部署。在这种情况下，端点名称存储在 online_endpoint_name 变量中，部署名称为 "demo"。

它使用 request_file 参数指定要评分的 JSON 文件的路径。在这种情况下，文件为 ./ultrachat_200k_dataset/sample_score.json。

它将端点的响应存储在 response 变量中。

它打印原始响应信息。

总之，这个脚本调用 Azure 机器学习中的在线端点以评分一个 JSON 文件并打印响应信息。

```
# Invoke the online endpoint in Azure Machine Learning to score the `sample_score.json` file
# The `invoke` method of the `online_endpoints` property of the `workspace_ml_client` object is used to send a request to an online endpoint and get a response
# The `endpoint_name` argument specifies the name of the endpoint, which is stored in the `online_endpoint_name` variable
# The `deployment_name` argument specifies the name of the deployment, which is "demo"
# The `request_file` argument specifies the path to the JSON file to be scored, which is `./ultrachat_200k_dataset/sample_score.json`
response = workspace_ml_client.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    deployment_name="demo",
    request_file="./ultrachat_200k_dataset/sample_score.json",
)

# Print the raw response from the endpoint
print("raw response: \n", response, "\n")
```
## 9.  删除在线端点
别忘了删除在线端点，否则您将继续为端点使用的计算付费。下面的 Python 代码用于删除 Azure 机器学习中的在线端点。以下是它的功能分解：

它调用 workspace_ml_client 对象的 online_endpoints 属性的 begin_delete 方法。此方法用于开始删除在线端点。

它使用 name 参数指定要删除的端点的名称。在这种情况下，端点名称存储在 online_endpoint_name 变量中。

它调用 wait 方法等待删除操作完成。这是一个阻塞操作，意味着它将阻止脚本继续执行，直到删除完成。

总之，这行代码正在开始删除 Azure 机器学习中的一个在线端点，并等待操作完成。

```
# Delete the online endpoint in Azure Machine Learning
# The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
# The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
# The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
```
