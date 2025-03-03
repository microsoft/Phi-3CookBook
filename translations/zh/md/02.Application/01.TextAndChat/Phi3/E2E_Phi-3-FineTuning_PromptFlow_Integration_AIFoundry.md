# 微调和集成自定义 Phi-3 模型与 Azure AI Foundry 的 Prompt Flow

本端到端 (E2E) 示例基于 Microsoft 技术社区的指南 “[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)”。它介绍了在 Azure AI Foundry 中微调、部署和集成自定义 Phi-3 模型与 Prompt Flow 的过程。  
与 E2E 示例 “[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)” 不同，该示例需要在本地运行代码，而本教程则完全专注于在 Azure AI/ML Studio 内微调和集成您的模型。

## 概述

在本端到端示例中，您将学习如何微调 Phi-3 模型并将其与 Azure AI Foundry 中的 Prompt Flow 集成。通过利用 Azure AI/ML Studio，您将建立一个部署和使用自定义 AI 模型的工作流。本示例分为三个场景：

**场景 1：设置 Azure 资源并准备微调**  
**场景 2：微调 Phi-3 模型并在 Azure Machine Learning Studio 中部署**  
**场景 3：与 Prompt Flow 集成并在 Azure AI Foundry 中与自定义模型交互**

以下是本端到端示例的概述。

![Phi-3-FineTuning_PromptFlow_Integration 概览.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.zh.png)

### 目录

1. **[场景 1：设置 Azure 资源并准备微调](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [创建 Azure Machine Learning 工作区](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [在 Azure 订阅中请求 GPU 配额](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [添加角色分配](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [设置项目](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [准备用于微调的数据集](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[场景 2：微调 Phi-3 模型并在 Azure Machine Learning Studio 中部署](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [微调 Phi-3 模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [部署微调后的 Phi-3 模型](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[场景 3：与 Prompt Flow 集成并在 Azure AI Foundry 中与自定义模型交互](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [将自定义 Phi-3 模型与 Prompt Flow 集成](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [与您的自定义 Phi-3 模型交互](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

## 场景 1：设置 Azure 资源并准备微调

### 创建 Azure Machine Learning 工作区

1. 在门户页面顶部的**搜索栏**中输入 *azure machine learning*，然后从出现的选项中选择 **Azure Machine Learning**。

    ![输入 azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.zh.png)

2. 从导航菜单中选择 **+ 创建**。

3. 从导航菜单中选择 **新工作区**。

    ![选择新工作区.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.zh.png)

4. 执行以下任务：

    - 选择您的 Azure **订阅**。
    - 选择要使用的 **资源组**（如有需要可新建）。
    - 输入 **工作区名称**，必须是唯一值。
    - 选择您希望使用的 **区域**。
    - 选择要使用的 **存储账户**（如有需要可新建）。
    - 选择要使用的 **密钥保管库**（如有需要可新建）。
    - 选择要使用的 **应用程序洞察**（如有需要可新建）。
    - 选择要使用的 **容器注册表**（如有需要可新建）。

    ![填写 azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.zh.png)

5. 选择 **查看 + 创建**。

6. 选择 **创建**。

### 在 Azure 订阅中请求 GPU 配额

在本教程中，您将学习如何使用 GPU 微调和部署 Phi-3 模型。  
对于微调，您将使用 *Standard_NC24ads_A100_v4* GPU，这需要配额请求。  
对于部署，您将使用 *Standard_NC6s_v3* GPU，这也需要配额请求。

> [!NOTE]  
> 仅“按需付费”订阅（标准订阅类型）有资格分配 GPU；目前不支持福利订阅。

1. 访问 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 执行以下任务以请求 *Standard NCADSA100v4 Family* 配额：

    - 从左侧选项卡中选择 **配额**。
    - 选择要使用的 **虚拟机系列**。例如，选择 **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**，其中包括 *Standard_NC24ads_A100_v4* GPU。
    - 从导航菜单中选择 **请求配额**。

        ![请求配额.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.zh.png)

    - 在“请求配额”页面中，输入您希望使用的 **新核心限制**。例如，24。
    - 在“请求配额”页面中，选择 **提交** 以请求 GPU 配额。

1. 执行以下任务以请求 *Standard NCSv3 Family* 配额：

    - 从左侧选项卡中选择 **配额**。
    - 选择要使用的 **虚拟机系列**。例如，选择 **Standard NCSv3 Family Cluster Dedicated vCPUs**，其中包括 *Standard_NC6s_v3* GPU。
    - 从导航菜单中选择 **请求配额**。
    - 在“请求配额”页面中，输入您希望使用的 **新核心限制**。例如，24。
    - 在“请求配额”页面中，选择 **提交** 以请求 GPU 配额。

### 添加角色分配

为了微调和部署您的模型，您需要首先创建一个用户分配的托管标识（UAI）并为其分配适当的权限。此 UAI 将在部署过程中用于身份验证。

#### 创建用户分配的托管标识 (UAI)

1. 在门户页面顶部的**搜索栏**中输入 *managed identities*，然后从出现的选项中选择 **托管标识**。

    ![输入 managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.zh.png)

1. 选择 **+ 创建**。

    ![选择创建.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.zh.png)

1. 执行以下任务：

    - 选择您的 Azure **订阅**。
    - 选择要使用的 **资源组**（如有需要可新建）。
    - 选择您希望使用的 **区域**。
    - 输入 **名称**，必须是唯一值。

    ![填写托管标识.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.zh.png)

1. 选择 **查看 + 创建**。

1. 选择 **+ 创建**。

#### 为托管标识添加“参与者”角色分配

1. 导航到您创建的托管标识资源。

1. 从左侧选项卡中选择 **Azure 角色分配**。

1. 从导航菜单中选择 **+ 添加角色分配**。

1. 在“添加角色分配”页面中，执行以下任务：  
    - 将 **范围** 选择为 **资源组**。  
    - 选择您的 Azure **订阅**。  
    - 选择要使用的 **资源组**。  
    - 将 **角色** 选择为 **参与者**。  

    ![填写参与者角色.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.zh.png)

2. 选择 **保存**。

#### 为托管标识添加“存储 Blob 数据读取器”角色分配

1. 在门户页面顶部的**搜索栏**中输入 *storage accounts*，然后从出现的选项中选择 **存储账户**。

    ![输入 storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.zh.png)

1. 选择与您创建的 Azure Machine Learning 工作区关联的存储账户。例如，*finetunephistorage*。

1. 执行以下任务以导航到“添加角色分配”页面：

    - 导航到您创建的 Azure 存储账户。  
    - 从左侧选项卡中选择 **访问控制 (IAM)**。  
    - 从导航菜单中选择 **+ 添加**。  
    - 从导航菜单中选择 **添加角色分配**。

    ![添加角色.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.zh.png)

1. 在“添加角色分配”页面中，执行以下任务：  
    - 在“角色”页面中，在**搜索栏**中输入 *Storage Blob Data Reader* 并从出现的选项中选择 **Storage Blob Data Reader**。  
    - 在“角色”页面中选择 **下一步**。  
    - 在“成员”页面中，将 **访问分配给** 选择为 **托管标识**。  
    - 在“成员”页面中选择 **+ 选择成员**。  
    - 在“选择托管标识”页面中，选择您的 Azure **订阅**。  
    - 在“选择托管标识”页面中，选择 **托管标识** 为 **Manage Identity**。  
    - 在“选择托管标识”页面中，选择您创建的托管标识。例如，*finetunephi-managedidentity*。  
    - 在“选择托管标识”页面中选择 **选择**。

    ![选择托管标识.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.zh.png)

1. 选择 **查看 + 分配**。

#### 为托管标识添加“AcrPull”角色分配

1. 在门户页面顶部的**搜索栏**中输入 *container registries*，然后从出现的选项中选择 **容器注册表**。

    ![输入 container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.zh.png)

1. 选择与 Azure Machine Learning 工作区关联的容器注册表。例如，*finetunephicontainerregistry*。

1. 执行以下任务以导航到“添加角色分配”页面：

    - 从左侧选项卡中选择 **访问控制 (IAM)**。  
    - 从导航菜单中选择 **+ 添加**。  
    - 从导航菜单中选择 **添加角色分配**。

1. 在“添加角色分配”页面中，执行以下任务：  
    - 在“角色”页面中，在**搜索栏**中输入 *AcrPull* 并从出现的选项中选择 **AcrPull**。  
    - 在“角色”页面中选择 **下一步**。  
    - 在“成员”页面中，将 **访问分配给** 选择为 **托管标识**。  
    - 在“成员”页面中选择 **+ 选择成员**。  
    - 在“选择托管标识”页面中，选择您的 Azure **订阅**。  
    - 在“选择托管标识”页面中，选择 **托管标识** 为 **Manage Identity**。  
    - 在“选择托管标识”页面中，选择您创建的托管标识。例如，*finetunephi-managedidentity*。  
    - 在“选择托管标识”页面中选择 **选择**。  
    - 选择 **查看 + 分配**。

### 设置项目

为了下载微调所需的数据集，您需要设置一个本地环境。

在本练习中，您将：

- 创建一个文件夹以在其中工作。  
- 创建一个虚拟环境。  
- 安装所需的软件包。  
- 创建一个 *download_dataset.py* 文件以下载数据集。

#### 创建工作文件夹

1. 打开终端窗口，输入以下命令在默认路径下创建一个名为 *finetune-phi* 的文件夹。

    ```console
    mkdir finetune-phi
    ```

2. 在终端中输入以下命令，导航到您创建的 *finetune-phi* 文件夹。

    ```console
    cd finetune-phi
    ```

#### 创建虚拟环境

1. 在终端中输入以下命令，创建一个名为 *.venv* 的虚拟环境。

    ```console
    python -m venv .venv
    ```

2. 在终端中输入以下命令，激活虚拟环境。

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]  
> 如果操作成功，您应该会在命令提示符前看到 *(.venv)*。

#### 安装所需的软件包

1. 在终端中输入以下命令，安装所需的软件包。

    ```console
    pip install datasets==2.19.1
    ```

#### 创建 `download_dataset.py`

> [!NOTE]  
> 完整文件夹结构：  
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. 打开 **Visual Studio Code**。

1. 从菜单栏中选择 **文件**。

1. 选择 **打开文件夹**。

1. 选择您创建的 *finetune-phi* 文件夹，该文件夹位于 *C:\Users\yourUserName\finetune-phi*。

    ![选择您创建的文件夹.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.zh.png)

1. 在 Visual Studio Code 的左侧窗格中，右键单击并选择 **新建文件**，创建一个名为 *download_dataset.py* 的新文件。

    ![创建新文件.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.zh.png)

### 准备用于微调的数据集

在本练习中，您将运行 *download_dataset.py* 文件，将 *ultrachat_200k* 数据集下载到本地环境中。然后，您将使用该数据集在 Azure Machine Learning 中微调 Phi-3 模型。

在本练习中，您将：

- 将代码添加到 *download_dataset.py* 文件中以下载数据集。  
- 运行 *download_dataset.py* 文件，将数据集下载到本地环境中。

#### 使用 *download_dataset.py* 下载数据集

1. 在 Visual Studio Code 中打开 *download_dataset.py* 文件。

1. 将以下代码添加到 *download_dataset.py* 文件中。

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Load the dataset with the specified name, configuration, and split ratio
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Split the dataset into train and test sets (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Open the file in write mode
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterate over each record in the dataset
            for record in dataset:
                # Dump the record as a JSON object and write it to the file
                json.dump(record, f)
                # Write a newline character to separate records
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Load and split the ULTRACHAT_200k dataset with a specific configuration and split ratio
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extract the train and test datasets from the split
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Save the train dataset to a JSONL file
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. 在终端中输入以下命令，运行脚本并将数据集下载到本地环境中。

    ```console
    python download_dataset.py
    ```

1. 验证数据集是否已成功保存到本地 *finetune-phi/data* 目录中。

> [!NOTE]  
>
> #### 关于数据集大小和微调时间的说明  
>
> 在本教程中，您仅使用数据集的 1% (`split='train[:1%]'`)。这显著减少了数据量，加快了上传和微调过程。您可以调整比例以找到训练时间与模型性能之间的平衡。使用较小的数据集子集可以减少微调所需的时间，使过程更易于管理。

## 场景 2：微调 Phi-3 模型并在 Azure Machine Learning Studio 中部署

### 微调 Phi-3 模型

在本练习中，您将在 Azure Machine Learning Studio 中微调 Phi-3 模型。

在本练习中，您将：

- 创建用于微调的计算集群。  
- 在 Azure Machine Learning Studio 中微调 Phi-3 模型。

#### 创建用于微调的计算集群
1. 访问 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 从左侧标签中选择 **Compute**。

1. 从导航菜单中选择 **Compute clusters**。

1. 选择 **+ New**。

    ![选择计算资源。](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.zh.png)

1. 执行以下操作：

    - 选择您想使用的 **Region**。
    - 将 **Virtual machine tier** 设置为 **Dedicated**。
    - 将 **Virtual machine type** 设置为 **GPU**。
    - 将 **Virtual machine size** 筛选器设置为 **Select from all options**。
    - 将 **Virtual machine size** 设置为 **Standard_NC24ads_A100_v4**。

    ![创建集群。](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.zh.png)

1. 选择 **Next**。

1. 执行以下操作：

    - 输入 **Compute name**，必须是唯一值。
    - 将 **Minimum number of nodes** 设置为 **0**。
    - 将 **Maximum number of nodes** 设置为 **1**。
    - 将 **Idle seconds before scale down** 设置为 **120**。

    ![创建集群。](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.zh.png)

1. 选择 **Create**。

#### 微调 Phi-3 模型

1. 访问 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 选择您创建的 Azure Machine Learning 工作区。

    ![选择您创建的工作区。](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.zh.png)

1. 执行以下操作：

    - 从左侧标签中选择 **Model catalog**。
    - 在 **搜索栏** 中输入 *phi-3-mini-4k*，然后从出现的选项中选择 **Phi-3-mini-4k-instruct**。

    ![输入 phi-3-mini-4k。](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.zh.png)

1. 从导航菜单中选择 **Fine-tune**。

    ![选择微调。](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.zh.png)

1. 执行以下操作：

    - 将 **Select task type** 设置为 **Chat completion**。
    - 选择 **+ Select data** 上传 **Training data**。
    - 将验证数据上传类型设置为 **Provide different validation data**。
    - 选择 **+ Select data** 上传 **Validation data**。

    ![填写微调页面。](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.zh.png)

    > [!TIP]
    >
    > 您可以选择 **Advanced settings** 来自定义配置，例如 **learning_rate** 和 **lr_scheduler_type**，以根据您的具体需求优化微调过程。

1. 选择 **Finish**。

1. 在本练习中，您成功使用 Azure Machine Learning 微调了 Phi-3 模型。请注意，微调过程可能需要较长时间。运行微调作业后，您需要等待其完成。您可以通过导航到 Azure Machine Learning 工作区左侧的 Jobs 标签来监控微调作业的状态。在接下来的系列中，您将部署微调后的模型并将其与 Prompt flow 集成。

    ![查看微调作业。](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.zh.png)

### 部署微调后的 Phi-3 模型

为了将微调后的 Phi-3 模型与 Prompt flow 集成，您需要部署模型以使其可用于实时推理。此过程包括注册模型、创建在线端点以及部署模型。

在本练习中，您将：

- 在 Azure Machine Learning 工作区中注册微调后的模型。
- 创建一个在线端点。
- 部署已注册的微调 Phi-3 模型。

#### 注册微调后的模型

1. 访问 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 选择您创建的 Azure Machine Learning 工作区。

    ![选择您创建的工作区。](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.zh.png)

1. 从左侧标签中选择 **Models**。
1. 选择 **+ Register**。
1. 选择 **From a job output**。

    ![注册模型。](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.zh.png)

1. 选择您创建的作业。

    ![选择作业。](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.zh.png)

1. 选择 **Next**。

1. 将 **Model type** 设置为 **MLflow**。

1. 确保 **Job output** 已选择；它应该是自动选择的。

    ![选择输出。](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.zh.png)

2. 选择 **Next**。

3. 选择 **Register**。

    ![选择注册。](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.zh.png)

4. 您可以通过导航到左侧标签中的 **Models** 菜单查看已注册的模型。

    ![已注册模型。](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.zh.png)

#### 部署微调后的模型

1. 导航到您创建的 Azure Machine Learning 工作区。

1. 从左侧标签中选择 **Endpoints**。

1. 从导航菜单中选择 **Real-time endpoints**。

    ![创建端点。](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.zh.png)

1. 选择 **Create**。

1. 选择您已注册的模型。

    ![选择已注册的模型。](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.zh.png)

1. 选择 **Select**。

1. 执行以下操作：

    - 将 **Virtual machine** 设置为 *Standard_NC6s_v3*。
    - 选择您想使用的 **Instance count**，例如 *1*。
    - 将 **Endpoint** 设置为 **New** 以创建一个端点。
    - 输入 **Endpoint name**，必须是唯一值。
    - 输入 **Deployment name**，必须是唯一值。

    ![填写部署设置。](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.zh.png)

1. 选择 **Deploy**。

> [!WARNING]
> 为避免账户产生额外费用，请确保删除 Azure Machine Learning 工作区中创建的端点。
>

#### 在 Azure Machine Learning 工作区中检查部署状态

1. 导航到您创建的 Azure Machine Learning 工作区。

1. 从左侧标签中选择 **Endpoints**。

1. 选择您创建的端点。

    ![选择端点](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.zh.png)

1. 在此页面中，您可以在部署过程中管理端点。

> [!NOTE]
> 部署完成后，请确保 **Live traffic** 设置为 **100%**。如果不是，请选择 **Update traffic** 来调整流量设置。请注意，如果流量设置为 0%，您将无法测试模型。
>
> ![设置流量。](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.zh.png)
>

## 场景 3：与 Prompt flow 集成并在 Azure AI Foundry 中与您的自定义模型进行对话

### 将自定义 Phi-3 模型与 Prompt flow 集成

成功部署您的微调模型后，您现在可以将其与 Prompt flow 集成，以便在实时应用中使用您的模型，从而实现与自定义 Phi-3 模型的多种交互任务。

在本练习中，您将：

- 创建 Azure AI Foundry Hub。
- 创建 Azure AI Foundry Project。
- 创建 Prompt flow。
- 为微调后的 Phi-3 模型添加自定义连接。
- 设置 Prompt flow 以与您的自定义 Phi-3 模型对话。

> [!NOTE]
> 您还可以使用 Azure ML Studio 与 Promptflow 集成。相同的集成过程也适用于 Azure ML Studio。

#### 创建 Azure AI Foundry Hub

在创建 Project 之前，您需要先创建一个 Hub。Hub 类似于资源组，允许您在 Azure AI Foundry 中组织和管理多个 Project。

1. 访问 [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)。

1. 从左侧标签中选择 **All hubs**。

1. 从导航菜单中选择 **+ New hub**。

    ![创建 Hub。](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.zh.png)

1. 执行以下操作：

    - 输入 **Hub name**，必须是唯一值。
    - 选择您的 Azure **Subscription**。
    - 选择要使用的 **Resource group**（如有需要，请创建一个新的）。
    - 选择您想使用的 **Location**。
    - 选择要使用的 **Connect Azure AI Services**（如有需要，请创建一个新的）。
    - 将 **Connect Azure AI Search** 设置为 **Skip connecting**。

    ![填写 Hub 信息。](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.zh.png)

1. 选择 **Next**。

#### 创建 Azure AI Foundry Project

1. 在您创建的 Hub 中，从左侧标签中选择 **All projects**。

1. 从导航菜单中选择 **+ New project**。

    ![选择新项目。](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.zh.png)

1. 输入 **Project name**，必须是唯一值。

    ![创建项目。](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.zh.png)

1. 选择 **Create a project**。

#### 为微调后的 Phi-3 模型添加自定义连接

要将您的自定义 Phi-3 模型与 Prompt flow 集成，您需要将模型的端点和密钥保存到自定义连接中。此设置确保您可以在 Prompt flow 中访问您的自定义 Phi-3 模型。

#### 设置微调后的 Phi-3 模型的 API 密钥和端点 URI

1. 访问 [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo)。

1. 导航到您创建的 Azure Machine Learning 工作区。

1. 从左侧标签中选择 **Endpoints**。

    ![选择端点。](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.zh.png)

1. 选择您创建的端点。

    ![选择端点。](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.zh.png)

1. 从导航菜单中选择 **Consume**。

1. 复制您的 **REST endpoint** 和 **Primary key**。
![复制 API 密钥和端点 URI。](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.zh.png)

#### 添加自定义连接

1. 访问 [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)。

1. 导航到你创建的 Azure AI Foundry 项目。

1. 在你创建的项目中，从左侧选项卡中选择 **Settings**。

1. 选择 **+ New connection**。

    ![选择新连接。](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.zh.png)

1. 从导航菜单中选择 **Custom keys**。

    ![选择自定义密钥。](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.zh.png)

1. 执行以下操作：

    - 选择 **+ Add key value pairs**。
    - 在键名中输入 **endpoint**，并将从 Azure ML Studio 复制的端点粘贴到值字段中。
    - 再次选择 **+ Add key value pairs**。
    - 在键名中输入 **key**，并将从 Azure ML Studio 复制的密钥粘贴到值字段中。
    - 添加密钥后，选择 **is secret** 以防止密钥暴露。

    ![添加连接。](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.zh.png)

1. 选择 **Add connection**。

#### 创建 Prompt flow

你已在 Azure AI Foundry 中添加了一个自定义连接。现在，让我们按照以下步骤创建一个 Prompt flow。随后，你将把该 Prompt flow 连接到自定义连接，以便在 Prompt flow 中使用微调后的模型。

1. 导航到你创建的 Azure AI Foundry 项目。

1. 从左侧选项卡中选择 **Prompt flow**。

1. 从导航菜单中选择 **+ Create**。

    ![选择 Prompt flow。](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.zh.png)

1. 从导航菜单中选择 **Chat flow**。

    ![选择聊天流。](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.zh.png)

1. 输入 **Folder name**。

    ![输入名称。](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.zh.png)

2. 选择 **Create**。

#### 设置 Prompt flow 与自定义 Phi-3 模型进行聊天

你需要将微调后的 Phi-3 模型集成到一个 Prompt flow 中。然而，现有的 Prompt flow 并未设计用于此目的。因此，你需要重新设计 Prompt flow，以便实现自定义模型的集成。

1. 在 Prompt flow 中，执行以下操作以重建现有流程：

    - 选择 **Raw file mode**。
    - 删除 *flow.dag.yml* 文件中的所有现有代码。
    - 将以下代码添加到 *flow.dag.yml* 文件中。

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

    - 选择 **Save**。

    ![选择原始文件模式。](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.zh.png)

1. 将以下代码添加到 *integrate_with_promptflow.py* 文件中，以在 Prompt flow 中使用自定义 Phi-3 模型。

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": {
                "input_string": [
                    {"role": "user", "content": input_data}
                ],
                "parameters": {
                    "temperature": 0.7,
                    "max_new_tokens": 128
                }
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![粘贴 Prompt flow 代码。](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.zh.png)

> [!NOTE]
> 有关在 Azure AI Foundry 中使用 Prompt flow 的更多详细信息，可以参考 [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)。

1. 选择 **Chat input** 和 **Chat output** 以启用与模型的聊天功能。

    ![输入输出。](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.zh.png)

1. 现在你已准备好与自定义 Phi-3 模型进行聊天。在下一个练习中，你将学习如何启动 Prompt flow 并使用它与微调后的 Phi-3 模型进行交互。

> [!NOTE]
>
> 重建的流程应类似于下图所示：
>
> ![流程示例。](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.zh.png)
>

### 与自定义 Phi-3 模型聊天

现在你已微调并将自定义 Phi-3 模型集成到 Prompt flow 中，可以开始与它交互了。本练习将指导你设置和启动与模型的聊天。通过这些步骤，你将能够充分利用微调后的 Phi-3 模型来完成各种任务和对话。

- 使用 Prompt flow 与自定义 Phi-3 模型聊天。

#### 启动 Prompt flow

1. 选择 **Start compute sessions** 以启动 Prompt flow。

    ![启动计算会话。](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.zh.png)

1. 选择 **Validate and parse input** 以更新参数。

    ![验证输入。](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.zh.png)

1. 选择 **connection** 的 **Value**，即你创建的自定义连接。例如，*connection*。

    ![连接。](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.zh.png)

#### 与自定义模型聊天

1. 选择 **Chat**。

    ![选择聊天。](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.zh.png)

1. 以下是结果示例：现在你可以与自定义 Phi-3 模型聊天。建议基于用于微调的数据提出问题。

    ![使用 Prompt flow 聊天。](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.zh.png)

**免责声明**：  
本文件使用基于机器的人工智能翻译服务进行翻译。尽管我们努力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的原始文件作为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用此翻译而引起的任何误解或误读，我们概不负责。