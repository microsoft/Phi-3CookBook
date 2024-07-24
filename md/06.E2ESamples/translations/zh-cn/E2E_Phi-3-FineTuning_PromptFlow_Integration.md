# 微调和集成自定义 Phi-3 模型与 Prompt flow

本端到端（E2E）的示例基于 Microsoft Tech Community 上的指南“[微调和集成自定义 Phi-3 模型与 Prompt Flow：逐步指南](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)”。它介绍了使用 Prompt flow 微调、部署和集成自定义 Phi-3 模型的全过程。

## 概述

在这个 E2E 示例中，您将学习如何微调 Phi-3 模型并将其与 Prompt flow 集成。通过利用 Azure Machine Learning 和 Prompt flow，您将建立一个部署和使用自定义 AI 模型的工作流程。这个 E2E 示例分为三个场景：

**场景 1：设置 Azure 资源和准备环境**

**场景 2：微调 Phi-3 模型并在 Azure Machine Learning Studio 中部署**

**场景 3：与 Prompt flow 集成并与您的自定义模型聊天**

以下是这个 E2E 示例的概述图。

![Phi-3-FineTuning_PromptFlow_Integration 概述](../../../../imgs/03/FineTuning-PromptFlow/00-01-architecture.png)

### 目录

1. **[场景 1：设置 Azure 资源和准备环境](#scenario-1-set-up-azure-resources-and-prepare-the-environment)**
    - [在 Azure 订阅中申请 GPU 配额](#request-gpu-quotas-in-azure-subscription)
    - [创建 Azure Machine Learning 工作区](#create-an-azure-machine-learning-workspace)
    - [添加角色分配](#add-role-assignment)
    - [设置项目](#set-up-project)
    - [准备微调数据集](#prepare-dataset-for-fine-tuning)

1. **[场景 2：微调 Phi-3 模型并在 Azure Machine Learning Studio 中部署](#scenario-2-fine-tune-phi-3-model-and-deploy-in-azure-machine-learning-studio)**
    - [设置 Azure CLI](#set-up-azure-cli)
    - [部署微调的模型](#deploy-the-fine-tuned-model)

1. **[场景 3：与 Prompt flow 集成并与您的自定义模型聊天](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model)**
    - [将自定义 Phi-3 模型与 Prompt flow 集成](#integrate-the-custom-phi-3-model-with-prompt-flow)
    - [与您的自定义模型聊天](#chat-with-your-custom-model)

## 场景 1：设置 Azure 资源和准备环境

### 在 Azure 订阅中申请 GPU 配额

在这个 E2E 示例中，您将使用 *Standard_NC6s_v3 GPU* 进行微调，这需要申请配额，而部署使用的 *Standard_E4s_v3* CPU 不需要申请配额。

1. 在门户页面顶部的 **搜索栏** 中输入 *subscriptions*，然后从出现的选项中选择 **Subscriptions**。

1. 选择您要使用的订阅。

1. 执行以下任务以申请 GPU 配额：

    - 从左侧标签选择 **Usage + quotas**。
    - 选择您要使用的 **Region**。
    - 选择要使用的 **Quota name**。例如，选择 Standard NCSv3 Family vCPUs，它包括 *Standard_NC6s_v3* GPU。
    - 选择 **New Quota Request**。
    - 选择 **Enter a new limit**。
    - 在 New Quota Request 页面，输入您要使用的 **New limit**。
    - 在 New Quota Request 页面，选择 **Submit** 以申请 GPU 配额。

### 创建 Azure Machine Learning 工作区

1. 在门户页面顶部的 **搜索栏** 中输入 *azure machine learning*，然后从出现的选项中选择 **Azure Machine Learning**。

    ![输入 azure machine learning](../../../../imgs/03/FineTuning-PromptFlow/01-01-type-azml.png)

1. 从导航菜单选择 **+ Create**。

1. 从导航菜单选择 **New workspace**。

    ![选择 new workspace](../../../../imgs/03/FineTuning-PromptFlow/01-02-select-new-workspace.png)

1. 执行以下任务：

    - 选择您的 Azure **Subscription**。
    - 选择要使用的 **Resource group**（如果需要，可新建一个）。
    - 输入 **Workspace Name**。它必须是唯一值。
    - 选择您要使用的 **Region**。
    - 选择要使用的 **Storage account**（如果需要，可新建一个）。
    - 选择要使用的 **Key vault**（如果需要，可新建一个）。
    - 选择要使用的 **Application insights**（如果需要，可新建一个）。
    - 将 **Container registry** 设为 **None**。

1. 选择 **Review + Create**。

1. 选择 **Create**。

### 添加角色分配

要微调和部署您的模型，您必须首先创建一个用户分配托管身份（UAI）并赋予其适当的权限。这个 UAI 将用于部署期间的身份验证。

#### 创建用户分配托管身份（UAI）

1. 在门户页面顶部的 **搜索栏** 中输入 *managed identities*，然后从出现的选项中选择 **Managed Identities**。

    ![输入 managed identities。](../../../../imgs/03/FineTuning-PromptFlow/01-05-type-managed-identities.png)

1. 选择 **+ Create**。

    ![选择 create。](../../../../imgs/03/FineTuning-PromptFlow/01-06-select-create.png)

1. 执行以下任务：

    - 选择您的 Azure **Subscription**。
    - 选择要使用的 **Resource group**（如果需要，可新建一个）。
    - 选择您要使用的 **Region**。
    - 输入 **Name**。它必须是唯一值。

1. 选择 **Review + create**。

1. 选择 **+ Create**。

#### 向托管身份添加贡献者角色分配

1. 导航到您创建的托管身份资源。

1. 从左侧标签选择 **Azure role assignments**。

1. 从导航菜单选择 **+Add role assignment**。

1. 在 Add role assignment 页面，执行以下任务：
    - 将 **Scope** 设为 **Resource group**。
    - 选择您的 Azure **Subscription**。
    - 选择要使用的 **Resource group**。
    - 将 **Role** 设为 **Contributor**。

    ![填写贡献者角色。](../../../../imgs/03/FineTuning-PromptFlow/01-07-fill-contributor-role.png)

1. 选择 **Save**。

#### 向托管身份添加存储 Blob 数据读取者角色分配

1. 在门户页面顶部的 **搜索栏** 中输入 *storage accounts*，然后从出现的选项中选择 **Storage accounts**。

    ![输入 storage accounts。](../../../../imgs/03/FineTuning-PromptFlow/01-08-type-storage-accounts.png)

1. 选择与您创建的 Azure Machine Learning 工作区关联的存储帐户。例如，*finetunephistorage*。

1. 执行以下任务以导航到 Add role assignment 页面：

    - 导航到您创建的 Azure 存储帐户。
    - 从左侧标签选择 **Access Control (IAM)**。
    - 从导航菜单选择 **+ Add**。
    - 从导航菜单选择 **Add role assignment**。

    ![添加角色。](../../../../imgs/03/FineTuning-PromptFlow/01-09-add-role.png)

1. 在 Add role assignment 页面，执行以下任务：

    - 在 Role 页面，输入 *Storage Blob Data Reader* 并从出现的选项中选择 **Storage Blob Data Reader**。
    - 在 Role 页面，选择 **Next**。
    - 在 Members 页面，将 **Assign access to** 设为 **Managed identity**。
    - 在 Members 页面，选择 **+ Select members**。
    - 在 Select managed identities 页面，选择您的 Azure **Subscription**。
    - 在 Select managed identities 页面，将 **Managed identity** 设为 **Manage Identity**。
    - 在 Select managed identities 页面，选择您创建的托管身份。例如，*finetunephi-managedidentity*。
    - 在 Select managed identities 页面，选择 **Select**。

        ![选择托管身份。](../../../../imgs/03/FineTuning-PromptFlow/01-10-select-managed-identity.png)

    - 选择 **Review + assign**。

#### 向托管身份添加 AcrPull 角色分配

1. 在门户页面顶部的 **搜索栏** 中输入 *container registries*，然后从出现的选项中选择 **Container registries**。

    ![输入 container registries。](../../../../imgs/03/FineTuning-PromptFlow/01-11-type-container-registries.png)

1. 选择与 Azure Machine Learning 工作区关联的容器注册表。例如，*finetunephicontainerregistries*。

1. 执行以下任务以导航到 Add role assignment 页面：

    - 从左侧标签选择 **Access Control (IAM)**。
    - 从导航菜单选择 **+ Add**。
    - 从导航菜单选择 **Add role assignment**。

1. 在 Add role assignment 页面，执行以下任务：

    - 在 Role 页面，输入 *AcrPull* 并从出现的选项中选择 **AcrPull**。
    - 在 Role 页面，选择 **Next**。
    - 在 Members 页面，将 **Assign access to** 设为 **Managed identity**。
    - 在 Members 页面，选择 **+ Select members**。
    - 在 Select managed identities 页面，选择您的 Azure **Subscription**。
    - 在 Select managed identities 页面，将 **Managed identity** 设为 **Manage Identity**。
    - 在 Select managed identities 页面，选择您创建的托管身份。例如，*finetunephi-managedidentity*。
    - 在 Select managed identities 页面，选择 **Select**。
    - 选择 **Review + assign**。

### 设置项目

现在，您将创建一个工作文件夹并设置一个虚拟环境，以开发与用户交互的程序，并使用存储在 Azure Cosmos DB 中的聊天记录来提供响应。

#### 创建工作文件夹

1. 打开终端窗口并输入以下命令，在默认路径下创建一个名为 *finetune-phi* 的文件夹。

    ```console
    mkdir finetune-phi
    ```

1. 在终端中输入以下命令，导航到您创建的 *finetune-phi* 文件夹。

    ```console
    cd finetune-phi
    ```

#### 创建虚拟环境

1. 在终端中输入以下命令，创建一个名为 *.venv* 的虚拟环境。

    ```console
    python -m venv .venv
    ```

1. 在终端中输入以下命令，激活虚拟环境。

    ```console
    .venv\Scripts\activate.bat
    ```

> **注意**
>
> 如果成功，您应该会在命令提示符前看到 *(.venv)*。

#### 安装所需的软件包

1. 在终端中输入以下命令，安装所需的软件包。

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### 创建项目文件

在这个练习中，您将为我们的项目创建必要的文件。这些文件包括下载数据集的脚本、设置 Azure Machine Learning 环境的脚本、微调 Phi-3 模型的脚本以及部署微调模型的脚本。您还将创建一个 *conda.yml* 文件来设置微调环境。

在这个练习中，您将：

- 创建一个 *download_dataset.py* 文件来下载数据集。
- 创建一个 *setup_ml.py* 文件来设置 Azure Machine Learning 环境。
- 在 *finetuning_dir* 文件夹中创建一个 *fine_tune.py* 文件，使用数据集微调 Phi-3 模型。
- 创建一个 *conda.yml* 文件来设置微调环境。
- 创建一个 *deploy_model.py* 文件来部署微调的模型。
- 创建一个 *integrate_with_promptflow.py* 文件，集成微调的模型并使用 Prompt Flow 执行模型。
- 创建一个 *flow.dag.yml* 文件，设置 Promptflow 的工作流程结构。
- 创建一个 *config.py* 文件来输入 Azure 信息。

> **注意**
>
> 完整的文件夹结构：
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        ├── finetuning_dir
> .        │      └── fine_tune.py
> .        ├── conda.yml
> .        ├── config.py
> .        ├── deploy_model.py
> .        ├── download_dataset.py
> .        ├── flow.dag.yml
> .        ├── integrate_with_promptflow.py
> .        └── setup_ml.py
> ```

1. 打开 **Visual Studio Code**。

1. 从菜单栏选择 **File**。

1. 选择 **Open Folder**。

1. 选择您创建的 *finetune-phi* 文件夹，位置为 *C:\Users\yourUserName\finetune-phi*。

    ![打开项目文件夹。](../../../../imgs/03/FineTuning-PromptFlow/01-12-open-project-folder.png)

1. 在 Visual Studio Code 的左侧窗格中右键单击并选择 **New File**，创建一个名为 *download_dataset.py* 的新文件。

1. 在 Visual Studio Code 的左侧窗格中右键单击并选择 **New File**，创建一个名为 *setup_ml.py* 的新文件。

1. 在 Visual Studio Code 的左侧窗格中右键单击并选择 **New File**，创建一个名为 *deploy_model.py* 的新文件。

    ![创建新文件。](../../../../imgs/03/FineTuning-PromptFlow/01-13-create-new-file.png)

1. 在 Visual Studio Code 的左侧窗格中右键单击并选择 **New Folder**，创建一个名为 *finetuning_dir* 的新文件夹。

1. 在 *finetuning_dir* 文件夹中，创建一个名为 *fine_tune.py* 的新文件。

#### 创建和配置 *conda.yml* 文件

1. 在 Visual Studio Code 的左侧窗格中右键单击并选择 **New File**，创建一个名为 *conda.yml* 的新文件。

1. 将以下代码添加到 *conda.yml* 文件中，以设置 Phi-3 模型的微调环境。

    ```yml
      name: phi-3-training-env
      channels:
        - defaults
        - conda-forge
      dependencies:
        - python=3.10
        - pip
        - numpy<2.0
        - pip:
            - torch~=2.0
            - torchvision~=0.18
            - trl==0.8.6
            - transformers~=4.41
            - datasets~=2.19
            - azureml-core~=1.30
            - azure-storage-blob==12.19
            - azure-ai-ml~=1.16
            - azure-identity~=1.16
            - accelerate~=0.30
            - mlflow==2.13.0
            - azureml-mlflow==1.56.0
    ```
    
### 创建和配置 *config.py* 文件

1. 在 Visual Studio Code 的左侧窗格中，右键单击并选择 **New File** 创建一个名为 *config.py* 的新文件。

1. 将以下代码添加到 *config.py* 文件中，以包含你的 Azure 信息。

    ```python
    # Azure 设置
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name"  # "TestGroup"

    # Azure Machine Learning 设置
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name"  # "finetunephi-workspace"

    # Azure Managed Identity 设置
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name"  # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # 数据集文件路径
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # 微调模型设置
    AZURE_MODEL_NAME = "your_fine_tuned_model_name"  # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"  # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"  # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"  # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### 添加 Azure 环境变量

1. 执行以下任务以添加 Azure 订阅 ID：

    - 在门户页面顶部的 **搜索栏** 中键入 *subscriptions*，然后从出现的选项中选择 **Subscriptions**。
    - 选择你当前使用的 Azure 订阅。
    - 复制你的订阅 ID 并粘贴到 *config.py* 文件中。

    ![查找订阅 ID。](../../../../imgs/03/FineTuning-PromptFlow/01-14-find-subscriptionid.png)

1. 执行以下任务以添加 Azure 工作区名称：

    - 导航到你创建的 Azure Machine Learning 资源。
    - 复制你的账户名称并粘贴到 *config.py* 文件中。

    ![查找 Azure Machine Learning 名称。](../../../../imgs/03/FineTuning-PromptFlow/01-15-find-AZML-name.png)

1. 执行以下任务以添加 Azure 资源组名称：

    - 导航到你创建的 Azure Machine Learning 资源。
    - 复制你的 Azure 资源组名称并粘贴到 *config.py* 文件中。

    ![查找资源组名称。](../../../../imgs/03/FineTuning-PromptFlow/01-16-find-AZML-resourcegroup.png)

1. 执行以下任务以添加 Azure 托管身份名称：

    - 导航到你创建的托管身份资源。
    - 复制你的 Azure 托管身份名称并粘贴到 *config.py* 文件中。

    ![查找 UAI。](../../../../imgs/03/FineTuning-PromptFlow/01-17-find-uai.png)

### 准备用于微调的数据集

在这个练习中，你将运行 *download_data.py* 文件以下载 *wikitext* 数据集到你的本地环境。然后，你将使用这些数据集在 Azure Machine Learning 中微调 Phi-3 模型。

#### 使用 *download_data.py* 下载你的数据集

1. 在 Visual Studio Code 中打开 *download_data.py* 文件。

2. 将以下代码添加到 *download_data.py* 文件中。

    ```python
    import json
    import os
    from datasets import load_dataset
    from config import (
        TRAIN_DATA_PATH,
        TEST_DATA_PATH)

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        加载并拆分数据集。
        """
        # 使用指定的名称和配置加载数据集
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"原始数据集大小: {len(dataset)}")
        
        # 将数据集拆分为训练和测试集（80% 训练，20% 测试）
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"训练数据集大小: {len(split_dataset['train'])}")
        print(f"测试数据集大小: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        将数据集保存为 JSONL 文件。
        """
        # 如果目录不存在，则创建目录
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # 以写入模式打开文件
        with open(filepath, 'w', encoding='utf-8') as f:
            # 遍历数据集中的每条记录
            for record in dataset:
                # 将记录作为 JSON 对象转储并写入文件
                json.dump(record, f)
                # 写入一个换行符以分隔记录
                f.write('\n')
        
        print(f"数据集已保存到 {filepath}")

    def main():
        """
        加载、拆分和保存数据集的主函数。
        """
        # 使用特定配置和拆分比例加载并拆分数据集
        dataset = load_and_split_dataset("wikitext", 'wikitext-2-v1', 'train[:1%]')
        
        # 从拆分中提取训练和测试数据集
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # 将训练数据集保存为 JSONL 文件
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # 将测试数据集保存到单独的 JSONL 文件中
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> **提示**
>
> **使用最小数据集和 CPU 进行微调的指导**
>
> 如果你想使用 CPU 进行微调，这种方法非常适合那些有福利订阅（如 Visual Studio Enterprise Subscription）的人，或者快速测试微调和部署过程。
>
> 将 `dataset = load_and_split_dataset("wikitext", 'wikitext-2-v1', 'train[:1%]')` 替换为 `dataset = load_and_split_dataset("wikitext", 'wikitext-2-v1', 'train[:10]')`
>

3. 在终端中输入以下命令运行脚本并将数据集下载到你的本地环境。

    ```console
    python download_data.py
    ```

4. 验证数据集是否已成功保存到你的本地 *finetune-phi/data* 目录。

> **注意**
>
> **数据集大小和微调时间**
>
> 在这个 E2E 示例中，你仅使用 1% 的数据集（`split='train[:1%]'`）。这显著减少了数据量，加快了上传和微调过程。你可以调整百分比以找到训练时间和模型性能之间的最佳平衡。使用较小的数据集子集可以减少微调所需时间，使过程更易于管理。

## 场景 2：微调 Phi-3 模型并在 Azure Machine Learning Studio 中部署

### 设置 Azure CLI

你需要设置 Azure CLI 以验证你的环境。Azure CLI 允许你直接从命令行管理 Azure 资源，并提供 Azure Machine Learning 访问这些资源所需的凭据。开始安装 [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. 打开终端窗口并输入以下命令登录到你的 Azure 账户。

    ```console
    az login
    ```

2. 选择你要使用的 Azure 账户。

3. 选择你要使用的 Azure 订阅。

    ![查找资源组名称。](../../../../imgs/03/FineTuning-PromptFlow/02-01-login-using-azure-cli.png)

> **提示**
>
> 如果你在登录 Azure 时遇到问题，请尝试使用设备代码。打开终端窗口并输入以下命令登录到你的 Azure 账户：
>
> ```console
> az login --use-device-code
> ```
>

### 微调 Phi-3 模型

在这个练习中，你将使用提供的数据集微调 Phi-3 模型。首先，你将在 *fine_tune.py* 文件中定义微调过程。然后，你将配置 Azure Machine Learning 环境并通过运行 *setup_ml.py* 文件启动微调过程。此脚本确保微调在 Azure Machine Learning 环境中进行。

通过运行 *setup_ml.py*，你将使微调过程在 Azure Machine Learning 环境中运行。

#### 向 *fine_tune.py* 文件添加代码

1. 导航到 *finetuning_dir* 文件夹并在 Visual Studio Code 中打开 *fine_tune.py* 文件。

2. 将以下代码添加到 *fine_tune.py* 文件中。

    ```python
    import argparse
    import sys
    import logging
    import os
    from datasets import Dataset
    import torch
    import mlflow
    from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
    from trl import SFTTrainer

    # 为了避免 MLflow 中的 INVALID_PARAMETER_VALUE 错误，禁用 MLflow 集成
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    logger = logging.getLogger(__name__)

    # 日志设置
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
        level=logging.WARNING
    )

    # 模型和标记器设置
    pretrained_model_name = "microsoft/Phi-3-mini-4k-instruct"
    model_kwargs = dict(
        use_cache=False,
        trust_remote_code=True,
        torch_dtype=torch.bfloat16,
        device_map=None,
        attn_implementation="eager"
    )

    def initialize_model_and_tokenizer(pretrained_model_name, model_kwargs):
        """
        使用给定的预训练模型名称和参数初始化模型和标记器。
        """
        model = AutoModelForCausalLM.from_pretrained(pretrained_model_name, **model_kwargs)
        tokenizer = AutoTokenizer.from_pretrained(pretrained_model_name)
        tokenizer.model_max_length = 2048
        tokenizer.pad_token = tokenizer.unk_token
        tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids(tokenizer.pad_token)
        tokenizer.padding_side = 'right'
        return model, tokenizer

    def preprocess_function(examples, tokenizer):
        """
        用于对数据集进行标记化的预处理函数。
        """
        tokens = tokenizer(examples['text'], padding="max_length", truncation=True, max_length=512)
        tokens['labels'] = tokens['input_ids'].copy()
        return tokens

    def load_and_preprocess_data(train_filepath, test_filepath, tokenizer):
        """
        加载并预处理数据集。
        """
        train_dataset = Dataset.from_json(train_filepath)
        test_dataset = Dataset.from_json(test_filepath)
        train_dataset = train_dataset.map(lambda examples: preprocess_function(examples, tokenizer), batched=True)
        test_dataset = test_dataset.map(lambda examples: preprocess_function(examples, tokenizer), batched=True)
        return train_dataset, test_dataset

    def main(train_file, eval_file, model_output_dir):
        """
        微调模型的主函数。
        """
        with mlflow.start_run():
            model, tokenizer = initialize_model_and_tokenizer(pretrained_model_name, model_kwargs)
            train_dataset, test_dataset = load_and_preprocess_data(train_file, eval_file, tokenizer)

            # 微调设置
            finetuning_settings = {
                "bf16": True,
                "do_eval": True,
                "output_dir": model_output_dir,
                "eval_strategy": "epoch",
                "learning_rate": 1e-4,
                "logging_steps": 20,
                "lr_scheduler_type": "linear",
                "num_train_epochs": 3,
                "overwrite_output_dir": True,
                "per_device_eval_batch_size": 4,
                "per_device_train_batch_size": 4,
                "remove_unused_columns": True,
                "save_steps": 500,
                "seed": 0,
                "gradient_checkpointing": True,
                "gradient_accumulation_steps": 1,
                "warmup_ratio": 0.2,
            }

            training_args = TrainingArguments(
                **finetuning_settings
            )
            trainer = SFTTrainer(
                model=model,
                args=training_args,
                train_dataset=train_dataset,
                eval_dataset=test_dataset,
                max_seq_length=2048,
                dataset_text_field="text",
                tokenizer=tokenizer,
                packing=True
            )

            train_result = trainer.train()

            metrics = train_result.metrics

            trainer.log_metrics("train", metrics)

            mlflow.transformers.log_model(
                transformers_model={"model": trainer.model, "tokenizer": tokenizer},
                artifact_path=model_output_dir,  # 这是在 MLflow 运行中保存模型文件的相对路径
            )

            # 评估
            tokenizer.padding_side = 'left'
            metrics = trainer.evaluate()
            metrics["eval_samples"] = len(test_dataset)
            trainer.log_metrics("eval", metrics)


    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--train-file", type=str, required=True, help="训练数据的路径")
        parser.add_argument("--eval-file", type=str, required=True, help="评估数据的路径")
        parser.add_argument("--model_output_dir", type=str, required=True, help="保存微调模型的目录")
        args = parser.parse_args()
        main(args.train_file, args.eval_file, args.model_output_dir)

    ```

3. 保存并关闭 *fine_tune.py* 文件。

#### 在 *setup_ml.py* 文件中添加代码

1. 在 Visual Studio Code 中打开 *setup_ml.py* 文件。

2. 将以下代码添加到 *setup_ml.py* 文件中。

    ```python
    import logging
    from azure.ai.ml import MLClient, command, Input
    from azure.ai.ml.entities import Environment, AmlCompute
    from azure.identity import AzureCliCredential
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        TRAIN_DATA_PATH,
        TEST_DATA_PATH
    )

    # 常量

    # 取消注释以下几行代码以使用 CPU 实例进行训练
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
    # CONDA_FILE = "conda.yml"

    # 取消注释以下几行代码以使用 GPU 实例进行训练
    COMPUTE_INSTANCE_TYPE = "Standard_NC6s_v3"
    COMPUTE_NAME = "gpu-nc6s-v3"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"
    CONDA_FILE = "conda.yml"

    LOCATION = "eastus2" # 用你的计算集群位置替换
    FINETUNING_DIR = "./finetuning_dir" # 微调脚本路径
    TRAINING_ENV_NAME = "phi-3-training-environment" # 训练环境名称
    MODEL_OUTPUT_DIR = "./model_output" # azure ml 中模型输出目录的路径

    # 日志设置以跟踪过程
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.WARNING
    )

    def get_ml_client():
        """
        使用 Azure CLI 凭证初始化 ML 客户端。
        """
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def create_or_get_environment(ml_client):
        """
        在 Azure ML 中创建或更新训练环境。
        """
        env = Environment(
            image=DOCKER_IMAGE_NAME,  # 环境的 Docker 镜像
            conda_file=CONDA_FILE,  # Conda 环境文件
            name=TRAINING_ENV_NAME,  # 环境名称
        )
        return ml_client.environments.create_or_update(env)

    def create_or_get_compute_cluster(ml_client, compute_name, COMPUTE_INSTANCE_TYPE, location):
        """
        在 Azure ML 中创建或更新计算集群。
        """
        try:
            compute_cluster = ml_client.compute.get(compute_name)
            logger.info(f"计算集群 '{compute_name}' 已存在。在当前运行中重用它。")
        except Exception:
            logger.info(f"计算集群 '{compute_name}' 不存在。将创建一个新的集群，大小为 {COMPUTE_INSTANCE_TYPE}。")
            compute_cluster = AmlCompute(
                name=compute_name,
                size=COMPUTE_INSTANCE_TYPE,
                location=location,
                tier="Dedicated",  # 计算集群的层级
                min_instances=0,  # 最小实例数
                max_instances=1  # 最大实例数
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # 等待集群创建完成
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        在 Azure ML 中设置微调作业。
        """
        return command(
            code=FINETUNING_DIR,  # fine_tune.py 的路径
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # 训练环境
            compute=compute_name,  # 使用的计算集群
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # 训练数据文件路径
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # 评估数据文件路径
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        在 Azure ML 中设置并运行微调作业的主函数。
        """
        # 初始化 ML 客户端
        ml_client = get_ml_client()

        # 创建环境
        env = create_or_get_environment(ml_client)
        
        # 创建或获取现有的计算集群
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # 创建并提交微调作业
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # 提交作业
        ml_client.jobs.stream(returned_job.name)  # 流式传输作业日志
        
        # 捕获作业名称
        job_name = returned_job.name
        print(f"作业名称: {job_name}")

    if __name__ == "__main__":
        main()

    ```

3. 用你的具体细节替换 `COMPUTE_INSTANCE_TYPE`、`COMPUTE_NAME` 和 `LOCATION`。

    ```python
   # 取消注释以下几行代码以使用 GPU 实例进行训练
    COMPUTE_INSTANCE_TYPE = "Standard_NC6s_v3"
    COMPUTE_NAME = "gpu-nc6s-v3"
    ...
    LOCATION = "eastus2" # 用你的计算集群位置替换
    ```

> **提示**
>
> **使用 CPU 的最小数据集进行微调的指导**
>
> 如果你想使用 CPU 进行微调，这种方法对于有订阅福利（如 Visual Studio Enterprise Subscription）的人或快速测试微调和部署过程非常理想。
>
> 1. 打开 *conda.yml* 文件。
> 1. 删除 `torchvision~=0.18`，因为它只与 GPU 环境兼容。
> 1. 打开 *setup_ml* 文件。
> 1. 用以下内容替换 `COMPUTE_INSTANCE_TYPE`、`COMPUTE_NAME` 和 `DOCKER_IMAGE_NAME`。如果你无法访问 *Standard_E16s_v3*，可以使用等效的 CPU 实例或请求新的配额。
> 1. 用你的具体细节替换 `LOCATION`。
>
>    ```python
>    # 取消注释以下几行代码以使用 CPU 实例进行训练
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    CONDA_FILE = "conda.yml"
>    LOCATION = "eastus2" # 用你的计算集群位置替换
>    ```
>

1. 输入以下命令运行 *setup_ml.py* 脚本并在 Azure Machine Learning 中启动微调过程。

    ```python
    python setup_ml.py
    ```

1. 在本练习中，你成功地使用 Azure Machine Learning 微调了 Phi-3 模型。通过运行 *setup_ml.py* 脚本，你已经设置了 Azure Machine Learning 环境并启动了 *fine_tune.py* 文件中定义的微调过程。请注意，微调过程可能需要相当长的时间。运行 `python setup_ml.py` 命令后，你需要等待过程完成。你可以按照终端中提供的链接监控微调作业的状态，链接将引导你到 Azure Machine Learning 门户。

    ![查看微调作业](../../../../imgs/03/FineTuning-PromptFlow/02-02-see-finetuning-job.png)

### 部署微调后的模型

要将微调后的 Phi-3 模型集成到 Prompt Flow 中，你需要部署模型以便进行实时推理。这个过程包括注册模型、创建在线端点以及部署模型。

#### 设置模型名称、端点名称和部署名称

1. 打开 *config.py* 文件。

1. 将 `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` 替换为你想要的模型名称。

1. 将 `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` 替换为你想要的端点名称。

1. 将 `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` 替换为你想要的部署名称。

#### 在 *deploy_model.py* 文件中添加代码

运行 *deploy_model.py* 文件可以自动化整个部署过程。它会根据在 config.py 文件中指定的设置（包括模型名称、端点名称和部署名称）注册模型、创建端点并执行部署。

1. 在 Visual Studio Code 中打开 *deploy_model.py* 文件。

1. 将以下代码添加到 *deploy_model.py* 中。

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # 配置导入
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_WORKSPACE_NAME,
        AZURE_MANAGED_IDENTITY_RESOURCE_ID,
        AZURE_MANAGED_IDENTITY_CLIENT_ID,
        AZURE_MODEL_NAME,
        AZURE_ENDPOINT_NAME,
        AZURE_DEPLOYMENT_NAME
    )

    # 常量
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # 日志设置
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def get_ml_client():
        """初始化并返回 ML Client。"""
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_WORKSPACE_NAME)

    def register_model(ml_client, model_name, job_name):
        """注册一个新模型。"""
        model_path = f"azureml://jobs/{job_name}/outputs/artifacts/paths/model_output"
        logger.info(f"从作业 {job_name} 的路径 {model_path} 注册模型 {model_name}。")
        run_model = Model(
            path=model_path,
            name=model_name,
            description="从运行中创建的模型。",
            type=AssetTypes.MLFLOW_MODEL,
        )
        model = ml_client.models.create_or_update(run_model)
        logger.info(f"注册的模型 ID: {model.id}")
        return model

    def delete_existing_endpoint(ml_client, endpoint_name):
        """删除现有端点（如果存在）。"""
        try:
            endpoint_result = ml_client.online_endpoints.get(name=endpoint_name)
            logger.info(f"删除现有端点 {endpoint_name}。")
            ml_client.online_endpoints.begin_delete(name=endpoint_name).result()
            logger.info(f"已删除现有端点 {endpoint_name}。")
        except Exception as e:
            logger.info(f"未找到要删除的现有端点 {endpoint_name}: {e}")

    def create_or_update_endpoint(ml_client, endpoint_name, description=""):
        """创建或更新端点。"""
        delete_existing_endpoint(ml_client, endpoint_name)
        logger.info(f"创建新端点 {endpoint_name}。")
        endpoint = ManagedOnlineEndpoint(
            name=endpoint_name,
            description=description,
            identity=IdentityConfiguration(
                type="user_assigned",
                user_assigned_identities=[ManagedIdentityConfiguration(resource_id=AZURE_MANAGED_IDENTITY_RESOURCE_ID)]
            )
        )
        endpoint_result = ml_client.online_endpoints.begin_create_or_update(endpoint).result()
        logger.info(f"已创建新端点 {endpoint_name}。")
        return endpoint_result

    def create_or_update_deployment(ml_client, endpoint_name, deployment_name, model):
        """创建或更新部署。"""

        logger.info(f"为端点 {endpoint_name} 创建部署 {deployment_name}。")
        deployment = ManagedOnlineDeployment(
            name=deployment_name,
            endpoint_name=endpoint_name,
            model=model.id,
            instance_type=COMPUTE_INSTANCE_TYPE,
            instance_count=1,
            environment_variables=deployment_env_vars,
            request_settings=OnlineRequestSettings(
                max_concurrent_requests_per_instance=3,
                request_timeout_ms=180000,
                max_queue_wait_ms=120000
            ),
            liveness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
            readiness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
        )
        deployment_result = ml_client.online_deployments.begin_create_or_update(deployment).result()
        logger.info(f"为端点 {endpoint_name} 创建了部署 {deployment.name}。")
        return deployment_result

    def set_traffic_to_deployment(ml_client, endpoint_name, deployment_name):
        """将流量设置到指定的部署。"""
        try:
            # 获取当前端点详细信息
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # 记录当前的流量分配以进行调试
            logger.info(f"当前流量分配: {endpoint.traffic}")
            
            # 设置部署的流量分配
            endpoint.traffic = {deployment_name: 100}
            
            # 使用新的流量分配更新端点
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # 记录更新后的流量分配以进行调试
            logger.info(f"更新后的流量分配: {updated_endpoint.traffic}")
            logger.info(f"将流量设置到端点 {endpoint_name} 的部署 {deployment_name}。")
            return updated_endpoint
        except Exception as e:
            # 记录在过程中发生的任何错误
            logger.error(f"设置流量到部署失败: {e}")
            raise


    def main():
        ml_client = get_ml_client()

        registered_model = register_model(ml_client, AZURE_MODEL_NAME, JOB_NAME)
        logger.info(f"注册的模型 ID: {registered_model.id}")

        endpoint = create_or_update_endpoint(ml_client, AZURE_ENDPOINT_NAME, "Endpoint for finetuned Phi-3 model")
        logger.info(f"端点 {AZURE_ENDPOINT_NAME} 已准备好。")

        try:
            deployment = create_or_update_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME, registered_model)
            logger.info(f"为端点 {AZURE_ENDPOINT_NAME} 创建了部署 {AZURE_DEPLOYMENT_NAME}。")

            set_traffic_to_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME)
            logger.info(f"将流量设置到端点 {AZURE_ENDPOINT_NAME} 的部署 {AZURE_DEPLOYMENT_NAME}。")
        except Exception as e:
            logger.error(f"创建或更新部署失败: {e}")

    if __name__ == "__main__":
        main()

    ```

1. 执行以下任务以获取 `JOB_NAME`：

    - 导航到你创建的 Azure Machine Learning 资源。
    - 选择 **Studio web URL** 以打开 Azure Machine Learning 工作区。
    - 从左侧标签中选择 **Jobs**。
    - 选择用于微调的实验。例如，*finetunephi*。
    - 选择你创建的作业。
    - 将作业名称复制并粘贴到 *deploy_model.py* 文件中的 `JOB_NAME = "your-job-name"`。

1. 将 `COMPUTE_INSTANCE_TYPE` 替换为你的具体细节。

1. 输入以下命令运行 *deploy_model.py* 脚本并开始在 Azure Machine Learning 中进行部署。

    ```python
    python deploy_model.py
    ```

> **警告**
> 为避免对你的账户产生额外费用，请确保在 Azure Machine Learning 工作区中删除已创建的端点。
>

#### 在 Azure Machine Learning 工作区检查部署状态

1. 导航到您创建的 Azure Machine Learning 资源。

1. 选择 **Studio web URL** 以打开 Azure Machine Learning 工作区。

1. 从左侧标签中选择 **Endpoints** 。

    ![选择 endpoints。](../../../../imgs/03/FineTuning-PromptFlow/02-03-select-endpoints.png)

1. 选择您创建的 endpoint。

    ![选择您创建的 endpoints。](../../../../imgs/03/FineTuning-PromptFlow/02-04-select-endpoint-created.png)

1. 在此页面上，您可以管理部署过程中创建的 endpoints。

## 场景 3：与 Prompt flow 集成并与您的自定义模型聊天

### 将自定义 Phi-3 模型与 Prompt flow 集成

在成功部署您的微调模型后，您现在可以将其与 Prompt flow 集成，以便在实时应用中使用您的模型，从而启用各种与您的自定义 Phi-3 模型的交互任务。

#### 设置微调 Phi-3 模型的 api key 和 endpoint uri

1. 导航到您创建的 Azure Machine Learning 工作区。
1. 从左侧标签中选择 **Endpoints**。
1. 选择您创建的 endpoint。
1. 从导航菜单中选择 **Consume**。
1. 将您的 **REST endpoint** 复制并粘贴到 *config.py* 文件中，用您的 **REST endpoint** 替换 `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"`。
1. 将您的 **Primary key** 复制并粘贴到 *config.py* 文件中，用您的 **Primary key** 替换 `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"`。

    ![复制 api key 和 endpoint uri。](../../../../imgs/03/FineTuning-PromptFlow/02-05-copy-apikey-endpoint.png)

#### 向 *flow.dag.yml* 文件添加代码

1. 在 Visual Studio Code 中打开 *flow.dag.yml* 文件。

1. 将以下代码添加到 *flow.dag.yml* 中。

    ```yml
    inputs:
      input_data:
        type: string
        default: "Who founded Microsoft?"

    outputs:
      answer:
        type: string
        reference: ${integrate_with_promptflow.output}

    nodes:
    - name: integrate_with_promptflow
      type: python
      source:
        type: code
        path: integrate_with_promptflow.py
      inputs:
        input_data: ${inputs.input_data}
    ```

#### 向 *integrate_with_promptflow.py* 文件添加代码

1. 在 Visual Studio Code 中打开 *integrate_with_promptflow.py* 文件。

1. 将以下代码添加到 *integrate_with_promptflow.py* 中。

    ```python
    import logging
    import requests
    from promptflow.core import tool
    import asyncio
    import platform
    from config import (
        AZURE_ML_ENDPOINT,
        AZURE_ML_API_KEY
    )

    # 日志设置
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_azml_endpoint(input_data: list, endpoint_url: str, api_key: str) -> str:
        """
        使用给定的输入数据向 Azure ML endpoint 发送请求。
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": [input_data],
            "params": {
                "temperature": 0.7,
                "max_new_tokens": 128,
                "do_sample": True,
                "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            result = response.json()[0]
            logger.info("成功从 Azure ML Endpoint 接收响应。")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"查询 Azure ML Endpoint 时出错：{e}")
            raise

    def setup_asyncio_policy():
        """
        为 Windows 设置 asyncio 事件循环策略。
        """
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            logger.info("设置 Windows asyncio 事件循环策略。")

    @tool
    def my_python_tool(input_data: str) -> str:
        """
        工具函数，用于处理输入数据并查询 Azure ML endpoint。
        """
        setup_asyncio_policy()
        return query_azml_endpoint(input_data, AZURE_ML_ENDPOINT, AZURE_ML_API_KEY)

    ```

### 与您的自定义模型聊天

1. 输入以下命令以运行 *deploy_model.py* 脚本，并在 Azure Machine Learning 中启动部署过程。

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. 以下是结果示例：现在您可以与您的自定义 Phi-3 模型进行聊天。建议根据用于微调的数据提出问题。

    ![Prompt flow 示例。](../../../../imgs/03/FineTuning-PromptFlow/02-06-promptflow-example.png)
