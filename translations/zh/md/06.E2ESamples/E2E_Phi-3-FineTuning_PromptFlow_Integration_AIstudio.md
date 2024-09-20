# 微调和集成自定义 Phi-3 模型与 Azure AI Studio 中的 Prompt flow

这个端到端 (E2E) 示例基于 Microsoft 技术社区的指南“[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Studio](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)”。它介绍了在 Azure AI Studio 中微调、部署和集成自定义 Phi-3 模型与 Prompt flow 的过程。
与端到端示例“[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)”不同，该教程完全聚焦于在 Azure AI / ML Studio 内部微调和集成你的模型。

## 概述

在这个端到端示例中，你将学习如何微调 Phi-3 模型并将其与 Azure AI Studio 中的 Prompt flow 集成。通过利用 Azure AI / ML Studio，你将建立一个部署和使用自定义 AI 模型的工作流程。这个端到端示例分为三个场景：

**场景 1：设置 Azure 资源并为微调做准备**

**场景 2：微调 Phi-3 模型并在 Azure Machine Learning Studio 中部署**

**场景 3：与 Prompt flow 集成并在 Azure AI Studio 中与自定义模型聊天**

以下是这个端到端示例的概述。

![Phi-3-FineTuning_PromptFlow_Integration 概述.](../../../../translated_images/00-01-architecture.fa40b38b29f795863378026c4dcc3007b0938b0b43afaf8c331906d03742b2e6.zh.png)

### 目录

1. **[场景 1：设置 Azure 资源并为微调做准备](../../../../md/06.E2ESamples)**
    - [创建 Azure Machine Learning 工作区](../../../../md/06.E2ESamples)
    - [在 Azure 订阅中请求 GPU 配额](../../../../md/06.E2ESamples)
    - [添加角色分配](../../../../md/06.E2ESamples)
    - [设置项目](../../../../md/06.E2ESamples)
    - [准备微调数据集](../../../../md/06.E2ESamples)

1. **[场景 2：微调 Phi-3 模型并在 Azure Machine Learning Studio 中部署](../../../../md/06.E2ESamples)**
    - [微调 Phi-3 模型](../../../../md/06.E2ESamples)
    - [部署微调后的 Phi-3 模型](../../../../md/06.E2ESamples)

1. **[场景 3：与 Prompt flow 集成并在 Azure AI Studio 中与自定义模型聊天](../../../../md/06.E2ESamples)**
    - [将自定义 Phi-3 模型与 Prompt flow 集成](../../../../md/06.E2ESamples)
    - [与自定义 Phi-3 模型聊天](../../../../md/06.E2ESamples)

## 场景 1：设置 Azure 资源并为微调做准备

### 创建 Azure Machine Learning 工作区

1. 在门户页面顶部的**搜索栏**中输入 *azure machine learning*，然后从出现的选项中选择 **Azure Machine Learning**。

    ![输入 azure machine learning.](../../../../translated_images/01-01-type-azml.98b3003c07da4dbb6885400f66988b3ae05767edb5e8b8ef480e584abe379ca7.zh.png)

2. 从导航菜单中选择 **+ 创建**。

3. 从导航菜单中选择 **新建工作区**。

    ![选择新建工作区.](../../../../translated_images/01-02-select-new-workspace.7648b384cbd786565740c0e5ea203d4710889d5ef23a2abf08428444f6d1a2a6.zh.png)

4. 执行以下任务：

    - 选择你的 Azure **订阅**。
    - 选择要使用的**资源组**（如果需要，可创建一个新的）。
    - 输入**工作区名称**。它必须是一个唯一值。
    - 选择你想使用的**区域**。
    - 选择要使用的**存储账户**（如果需要，可创建一个新的）。
    - 选择要使用的**密钥保管库**（如果需要，可创建一个新的）。
    - 选择要使用的**应用程序洞察**（如果需要，可创建一个新的）。
    - 选择要使用的**容器注册表**（如果需要，可创建一个新的）。

    ![填写 azure machine learning.](../../../../translated_images/01-03-fill-AZML.a3f644231a76859c7d92134b7dea1dd0d4df1c11cc615351c95be5a2c7056b03.zh.png)

5. 选择 **审核 + 创建**。

6. 选择 **创建**。

### 在 Azure 订阅中请求 GPU 配额

在本教程中，你将学习如何使用 GPU 微调和部署 Phi-3 模型。对于微调，你将使用 *Standard_NC24ads_A100_v4* GPU，这需要一个配额请求。对于部署，你将使用 *Standard_NC6s_v3* GPU，这也需要一个配额请求。

> [!NOTE]
>
> 只有按需付费订阅（标准订阅类型）有资格分配 GPU；目前不支持福利订阅。
>

1. 访问 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 执行以下任务以请求 *Standard NCADSA100v4 Family* 配额：

    - 从左侧选项卡中选择 **配额**。
    - 选择要使用的**虚拟机系列**。例如，选择 **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**，其中包括 *Standard_NC24ads_A100_v4* GPU。
    - 从导航菜单中选择 **请求配额**。

        ![请求配额.](../../../../translated_images/02-02-request-quota.55f797113d95ad20ca91943eed637488d0aa51d61f3bbe7f080ec466b2ae0666.zh.png)

    - 在请求配额页面中，输入你想使用的**新核心限制**。例如，24。
    - 在请求配额页面中，选择 **提交** 以请求 GPU 配额。

1. 执行以下任务以请求 *Standard NCSv3 Family* 配额：

    - 从左侧选项卡中选择 **配额**。
    - 选择要使用的**虚拟机系列**。例如，选择 **Standard NCSv3 Family Cluster Dedicated vCPUs**，其中包括 *Standard_NC6s_v3* GPU。
    - 从导航菜单中选择 **请求配额**。
    - 在请求配额页面中，输入你想使用的**新核心限制**。例如，24。
    - 在请求配额页面中，选择 **提交** 以请求 GPU 配额。

### 添加角色分配

要微调和部署你的模型，首先必须创建一个用户分配的托管身份 (UAI) 并赋予其适当的权限。此 UAI 将用于部署期间的身份验证。

#### 创建用户分配的托管身份 (UAI)

1. 在门户页面顶部的**搜索栏**中输入 *managed identities*，然后从出现的选项中选择 **Managed Identities**。

    ![输入 managed identities.](../../../../translated_images/03-01-type-managed-identities.2f7b07daa34dc15303b6a3f8c364bc0b7e892dd18aaff361440a030621b540b8.zh.png)

1. 选择 **+ 创建**。

    ![选择创建.](../../../../translated_images/03-02-select-create.0bde775b318f4adba24a7637b31f00f9b685214ed225c5123845a215a260ac71.zh.png)

1. 执行以下任务：

    - 选择你的 Azure **订阅**。
    - 选择要使用的**资源组**（如果需要，可创建一个新的）。
    - 选择你想使用的**区域**。
    - 输入**名称**。它必须是一个唯一值。

    ![选择创建.](../../../../translated_images/03-03-fill-managed-identities-1.688009e629c1e6952853b94022d3fe97c659c34e29908db17218a5cab6d6add1.zh.png)

1. 选择 **审核 + 创建**。

1. 选择 **+ 创建**。

#### 为托管身份添加贡献者角色分配

1. 导航到你创建的托管身份资源。

1. 从左侧选项卡中选择 **Azure 角色分配**。

1. 从导航菜单中选择 **+ 添加角色分配**。

1. 在添加角色分配页面中，执行以下任务：
    - 选择**范围**为**资源组**。
    - 选择你的 Azure **订阅**。
    - 选择要使用的**资源组**。
    - 选择**角色**为**贡献者**。

    ![填写贡献者角色.](../../../../translated_images/03-04-fill-contributor-role.8bc54b3ac8f64842c82b3379f3c3e9f8d778abf28c00e5b7b471935a86d3ae64.zh.png)

1. 选择 **保存**。

#### 为托管身份添加存储 Blob 数据读取者角色分配

1. 在门户页面顶部的**搜索栏**中输入 *storage accounts*，然后从出现的选项中选择 **Storage accounts**。

    ![输入 storage accounts.](../../../../translated_images/03-05-type-storage-accounts.236987db35ba863124c6de8dd16533fe35b96ee4e2dcb9d67e6b279a285f0e6d.zh.png)

1. 选择与你创建的 Azure Machine Learning 工作区关联的存储账户。例如，*finetunephistorage*。

1. 执行以下任务以导航到添加角色分配页面：

    - 导航到你创建的 Azure 存储账户。
    - 从左侧选项卡中选择 **访问控制 (IAM)**。
    - 从导航菜单中选择 **+ 添加**。
    - 从导航菜单中选择 **添加角色分配**。

    ![添加角色.](../../../../translated_images/03-06-add-role.dde49177fe7ce1cd1604f620ca5c8ac6442fc516effb057e9f74645f35f9d038.zh.png)

1. 在添加角色分配页面中，执行以下任务：

    - 在角色页面中，在**搜索栏**中输入 *Storage Blob Data Reader* 并从出现的选项中选择 **Storage Blob Data Reader**。
    - 在角色页面中选择 **下一步**。
    - 在成员页面中选择**分配访问给** **托管身份**。
    - 在成员页面中选择 **+ 选择成员**。
    - 在选择托管身份页面中，选择你的 Azure **订阅**。
    - 在选择托管身份页面中，选择**托管身份**为**托管身份**。
    - 在选择托管身份页面中，选择你创建的托管身份。例如，*finetunephi-managedidentity*。
    - 在选择托管身份页面中选择 **选择**。

    ![选择托管身份.](../../../../translated_images/03-08-select-managed-identity.f9a44699bf247a4583e2d377e304de8c3d8a602b7d3fed52b9ae790e64e94fe9.zh.png)

1. 选择 **审核 + 分配**。

#### 为托管身份添加 AcrPull 角色分配

1. 在门户页面顶部的**搜索栏**中输入 *container registries*，然后从出现的选项中选择 **Container registries**。

    ![输入 container registries.](../../../../translated_images/03-09-type-container-registries.b5519f1fbf49bff0c0d4c95deecd2ef0c61b4870119886c3661014435e2b7095.zh.png)

1. 选择与你的 Azure Machine Learning 工作区关联的容器注册表。例如，*finetunephicontainerregistry*。

1. 执行以下任务以导航到添加角色分配页面：

    - 从左侧选项卡中选择 **访问控制 (IAM)**。
    - 从导航菜单中选择 **+ 添加**。
    - 从导航菜单中选择 **添加角色分配**。

1. 在添加角色分配页面中，执行以下任务：

    - 在角色页面中，在**搜索栏**中输入 *AcrPull* 并从出现的选项中选择 **AcrPull**。
    - 在角色页面中选择 **下一步**。
    - 在成员页面中选择**分配访问给** **托管身份**。
    - 在成员页面中选择 **+ 选择成员**。
    - 在选择托管身份页面中，选择你的 Azure **订阅**。
    - 在选择托管身份页面中，选择**托管身份**为**托管身份**。
    - 在选择托管身份页面中，选择你创建的托管身份。例如，*finetunephi-managedidentity*。
    - 在选择托管身份页面中选择 **选择**。
    - 选择 **审核 + 分配**。

### 设置项目

为了下载微调所需的数据集，你将设置一个本地环境。

在本练习中，你将：

- 创建一个文件夹在其中工作。
- 创建一个虚拟环境。
- 安装所需的包。
- 创建一个 *download_dataset.py* 文件来下载数据集。

#### 创建一个文件夹在其中工作

1. 打开终端窗口，输入以下命令在默认路径中创建一个名为 *finetune-phi* 的文件夹。

    ```console
    mkdir finetune-phi
    ```

2. 在终端中输入以下命令导航到你创建的 *finetune-phi* 文件夹。

    ```console
    cd finetune-phi
    ```

#### 创建一个虚拟环境

1. 在终端中输入以下命令创建一个名为 *.venv* 的虚拟环境。

    ```console
    python -m venv .venv
    ```

2. 在终端中输入以下命令激活虚拟环境。

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> 如果成功，你应该会看到命令提示符前有 *(.venv)*。

#### 安装所需的包

1. 在终端中输入以下命令安装所需的包。

    ```console
    pip install datasets==2.19.1
    ```

#### 创建 `download_dataset.py`

> [!NOTE]
> 完整的文件夹结构：
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. 打开 **Visual Studio Code**。

1. 从菜单栏中选择 **文件**。

1. 选择 **打开文件夹**。

1. 选择你创建的 *finetune-phi* 文件夹，路径为 *C:\Users\yourUserName\finetune-phi*。

    ![选择你创建的文件夹.](../../../../translated_images/04-01-open-project-folder.f5e2b4ce1cb596eae857303b12909dc0174fd99129d6944c41079f24ee17eed2.zh.png)

1. 在 Visual Studio Code 的左侧窗格中，右键选择 **新建文件** 来创建一个名为 *download_dataset.py* 的新文件。

    ![创建一个新文件.](../../../../translated_images/04-02-create-new-file.7c51fabe5e84788e34e43f951164471eb07df8363993ce69badc8908f1033613.zh.png)

### 准备微调数据集

在本练习中，你将运行 *download_dataset.py* 文件，将 *ultrachat_200k* 数据集下载到本地环境。然后，你将使用这些数据集在 Azure Machine Learning 中微调 Phi-3 模型。

在本练习中，你将：

- 向 *download_dataset.py* 文件添加代码以下载数据集。
- 运行 *download_dataset.py* 文件将数据集下载到本地环境。

#### 使用 *download_dataset.py* 下载你的数据集

1. 在 Visual Studio Code 中打开 *download_dataset.py* 文件。

1. 将以下代码添加到 *download_dataset.py* 文件中。

    ```python
    import json
    import os
    from datasets import load_dataset

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        加载并拆分数据集。
        """
        # 使用指定的名称、配置和拆分比例加载数据集
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"原始数据集大小: {len(dataset)}")
        
        # 将数据集拆分为训练集和测试集（80% 训练，20% 测试）
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"训练数据集大小: {len(split_dataset['train'])}")
        print(f"测试数据集大小: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        将数据集保存到 JSONL 文件。
        """
        # 如果目录不存在，则创建目录
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # 以写模式打开文件
        with open(filepath, 'w', encoding='utf-8') as f:
            # 遍历数据集中的每条记录
            for record in dataset:
                # 将记录作为 JSON 对象写入文件
                json.dump(record, f)
                # 写入换行符以分隔记录
                f.write('\n')
        
        print(f"数据集已保存到 {filepath}")

    def main():
        """
        加载、拆分和保存数据集的主函数。
        """
        # 使用特定配置和拆分比例加载和拆分 ULTRACHAT_200k 数据集
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # 从拆分中提取训练集和测试集
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # 将训练数据集保存到 JSONL 文件
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # 将测试数据集保存到单独的 JSONL 文件
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. 在终端中输入以下命令运行脚本并将数据集下载到本地环境。

    ```console
    python download_dataset.py
    ```

1. 验证数据集是否成功保存到本地 *finetune-phi/data* 目录中。

> [!NOTE]
>
> #### 关于数据集大小和微调时间的说明
>
> 在本教程中，你只使用数据集的 1% (`split='train[:1%]'`)。这大大减少了数据量，加快了上传和微调过程。你可以调整百分比以找到训练时间和模型性能之间的最佳平衡。使用较小的数据集子集可以减少微调所
1. 访问 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 从左侧标签中选择 **Compute**。

1. 从导航菜单中选择 **Compute clusters**。

1. 选择 **+ New**。

    ![选择计算资源。](../../../../translated_images/06-01-select-compute.69422609cf19921fb16f550b2566e00870f63ba0caf66b0d26b34e6b0ed21a68.zh.png)

1. 执行以下任务：

    - 选择你想使用的 **Region**。
    - 将 **Virtual machine tier** 选择为 **Dedicated**。
    - 将 **Virtual machine type** 选择为 **GPU**。
    - 将 **Virtual machine size** 筛选器选择为 **Select from all options**。
    - 将 **Virtual machine size** 选择为 **Standard_NC24ads_A100_v4**。

    ![创建集群。](../../../../translated_images/06-02-create-cluster.ad68bcb0914b62972408da8f925632977c54248ff99d2c45761f7e3d33f40fe1.zh.png)

1. 选择 **Next**。

1. 执行以下任务：

    - 输入 **Compute name**。它必须是一个唯一值。
    - 将 **Minimum number of nodes** 选择为 **0**。
    - 将 **Maximum number of nodes** 选择为 **1**。
    - 将 **Idle seconds before scale down** 选择为 **120**。

    ![创建集群。](../../../../translated_images/06-03-create-cluster.f36399780462ff69f62b9bdf22180d6824b00cdc913fe2a639dde3e4b9eaa43e.zh.png)

1. 选择 **Create**。

#### 微调 Phi-3 模型

1. 访问 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 选择你创建的 Azure Machine Learning 工作区。

    ![选择你创建的工作区。](../../../../translated_images/06-04-select-workspace.5e35488b3bb3e391ead6688243c52fc2aecb8ae7f1c738b91b49580f9db353cf.zh.png)

1. 执行以下任务：

    - 从左侧标签中选择 **Model catalog**。
    - 在 **搜索栏** 中输入 *phi-3-mini-4k*，然后从出现的选项中选择 **Phi-3-mini-4k-instruct**。

    ![输入 phi-3-mini-4k。](../../../../translated_images/06-05-type-phi-3-mini-4k.7461addd95ede137f6f018a29681762f85e063477ded6043aafbdf6d742a54e8.zh.png)

1. 从导航菜单中选择 **Fine-tune**。

    ![选择微调。](../../../../translated_images/06-06-select-fine-tune.2c678a7f33294c16ae3ad30ce5d4a78600013dc3a0227e8d341a1962f3aff84d.zh.png)

1. 执行以下任务：

    - 将 **Select task type** 选择为 **Chat completion**。
    - 选择 **+ Select data** 上传 **Training data**。
    - 将验证数据上传类型选择为 **Provide different validation data**。
    - 选择 **+ Select data** 上传 **Validation data**。

    ![填写微调页面。](../../../../translated_images/06-07-fill-finetuning.c76431cc247b6398fb9d33da62841adf87d5eebaa92cd79e80bd7bcbed49f1d3.zh.png)

    > [!TIP]
    >
    > 你可以选择 **Advanced settings** 自定义配置，如 **learning_rate** 和 **lr_scheduler_type**，以根据你的具体需求优化微调过程。

1. 选择 **Finish**。

1. 在此练习中，你成功使用 Azure Machine Learning 微调了 Phi-3 模型。请注意，微调过程可能需要相当长的时间。运行微调任务后，你需要等待其完成。你可以通过导航到 Azure Machine Learning 工作区左侧的 Jobs 标签来监控微调任务的状态。在下一系列中，你将部署微调后的模型并将其与 Prompt flow 集成。

    ![查看微调任务。](../../../../translated_images/06-08-output.9f9cf6f9e9e83533b793a5ff3066b09475e299999fead6f98dfb102f48db0061.zh.png)

### 部署微调后的 Phi-3 模型

要将微调后的 Phi-3 模型与 Prompt flow 集成，你需要部署模型以使其可用于实时推理。此过程涉及注册模型、创建在线端点并部署模型。

在此练习中，你将：

- 在 Azure Machine Learning 工作区中注册微调后的模型。
- 创建在线端点。
- 部署注册的微调后的 Phi-3 模型。

#### 注册微调后的模型

1. 访问 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 选择你创建的 Azure Machine Learning 工作区。

    ![选择你创建的工作区。](../../../../translated_images/06-04-select-workspace.5e35488b3bb3e391ead6688243c52fc2aecb8ae7f1c738b91b49580f9db353cf.zh.png)

1. 从左侧标签中选择 **Models**。
1. 选择 **+ Register**。
1. 选择 **From a job output**。

    ![注册模型。](../../../../translated_images/07-01-register-model.9b64d29736e0be32343b36a503d7e38c47c22d9edfa554aae179352982fdf96b.zh.png)

1. 选择你创建的任务。

    ![选择任务。](../../../../translated_images/07-02-select-job.712abf18cdae5256776907df3ed30df53d297ff8d475fb64d5c03e92304db6ef.zh.png)

1. 选择 **Next**。

1. 将 **Model type** 选择为 **MLflow**。

1. 确保选择了 **Job output**；它应该是自动选择的。

    ![选择输出。](../../../../translated_images/07-03-select-output.45098161b7ddfda4b8d4d62676da0488a32a16e838ff03f37bfd71b9886da798.zh.png)

1. 选择 **Next**。

1. 选择 **Register**。

    ![选择注册。](../../../../translated_images/07-04-register.3403ed7976f07fbfc27210550cf2f793d9cf778032ea276ecb287bd9df88f188.zh.png)

1. 你可以通过导航到左侧标签中的 **Models** 菜单来查看已注册的模型。

    ![已注册的模型。](../../../../translated_images/07-05-registered-model.90693749513e55231e8904304e4ea1f9e29ab659bc1926ea69dffd25e77ffb2d.zh.png)

#### 部署微调后的模型

1. 导航到你创建的 Azure Machine Learning 工作区。

1. 从左侧标签中选择 **Endpoints**。

1. 从导航菜单中选择 **Real-time endpoints**。

    ![创建端点。](../../../../translated_images/07-06-create-endpoint.28687e4d01bffed741bf461bbb36ceef441ed5d049ca5d091aab511ced67a804.zh.png)

1. 选择 **Create**。

1. 选择你创建的已注册模型。

    ![选择已注册的模型。](../../../../translated_images/07-07-select-registered-model.5190ae13400cc09a6410f891a62e6b2ccc2c2bd7f419b0df4ea964731e72407f.zh.png)

1. 选择 **Select**。

1. 执行以下任务：

    - 将 **Virtual machine** 选择为 *Standard_NC6s_v3*。
    - 选择你想使用的 **Instance count**。例如，*1*。
    - 将 **Endpoint** 选择为 **New** 以创建一个端点。
    - 输入 **Endpoint name**。它必须是一个唯一值。
    - 输入 **Deployment name**。它必须是一个唯一值。

    ![填写部署设置。](../../../../translated_images/07-08-deployment-setting.5449edf53b27f5457cc68d2285d355a7d364b01423a51e5af63e7c52374a3a79.zh.png)

1. 选择 **Deploy**。

> [!WARNING]
> 为了避免你的账户产生额外费用，请确保删除在 Azure Machine Learning 工作区中创建的端点。
>

#### 在 Azure Machine Learning 工作区中检查部署状态

1. 导航到你创建的 Azure Machine Learning 工作区。

1. 从左侧标签中选择 **Endpoints**。

1. 选择你创建的端点。

    ![选择端点](../../../../translated_images/07-09-check-deployment.8e4465a7585b3c22db5fc9d5757269a919b5104fdeb5f736fa573ca9b3e16abe.zh.png)

1. 在此页面上，你可以在部署过程中管理端点。

> [!NOTE]
> 部署完成后，确保 **Live traffic** 设置为 **100%**。如果不是，请选择 **Update traffic** 以调整流量设置。请注意，如果流量设置为 0%，你将无法测试模型。
>
> ![设置流量。](../../../../translated_images/07-10-set-traffic.1d1b24b39c7ec80451c99fe05298fac636f0cd449e7be282736f6c06a1a70875.zh.png)
>

## 场景 3：在 Azure AI Studio 中与 Prompt flow 和你的自定义模型聊天

### 将自定义 Phi-3 模型与 Prompt flow 集成

成功部署微调后的模型后，你现在可以将其与 Prompt Flow 集成，以便在实时应用中使用你的模型，从而启用与自定义 Phi-3 模型的各种交互任务。

在此练习中，你将：

- 创建 Azure AI Studio Hub。
- 创建 Azure AI Studio Project。
- 创建 Prompt flow。
- 为微调后的 Phi-3 模型添加自定义连接。
- 设置 Prompt flow 与你的自定义 Phi-3 模型进行聊天。

> [!NOTE]
> 你也可以使用 Azure ML Studio 与 Promptflow 集成。相同的集成过程可以应用于 Azure ML Studio。

#### 创建 Azure AI Studio Hub

在创建 Project 之前，你需要创建一个 Hub。Hub 类似于资源组，允许你在 Azure AI Studio 中组织和管理多个 Project。

1. 访问 [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)。

1. 从左侧标签中选择 **All hubs**。

1. 从导航菜单中选择 **+ New hub**。

    ![创建 hub。](../../../../translated_images/08-01-create-hub.1df80696bf3376f0e56ffa90de1fc35962acf2fc3c1a3a6b254015b8b993e55e.zh.png)

1. 执行以下任务：

    - 输入 **Hub name**。它必须是一个唯一值。
    - 选择你的 Azure **Subscription**。
    - 选择要使用的 **Resource group**（如有需要，创建一个新的）。
    - 选择你想使用的 **Location**。
    - 选择要使用的 **Connect Azure AI Services**（如有需要，创建一个新的）。
    - 将 **Connect Azure AI Search** 选择为 **Skip connecting**。

    ![填写 hub。](../../../../translated_images/08-02-fill-hub.fc194526614a5811e7b57e699911be39babdc95aa425b6c4a72f064948865ce3.zh.png)

1. 选择 **Next**。

#### 创建 Azure AI Studio Project

1. 在你创建的 Hub 中，从左侧标签中选择 **All projects**。

1. 从导航菜单中选择 **+ New project**。

    ![选择新项目。](../../../../translated_images/08-04-select-new-project.dc11f26658c3c3f9d0fcf3232a954abfc115de5eb74da21d5be229c9c1be2875.zh.png)

1. 输入 **Project name**。它必须是一个唯一值。

    ![创建项目。](../../../../translated_images/08-05-create-project.61caaa28c1b9b696bf29de6b002bbb2040dbaeb764adab161dcb3472fe789aea.zh.png)

1. 选择 **Create a project**。

#### 为微调后的 Phi-3 模型添加自定义连接

要将你的自定义 Phi-3 模型与 Prompt flow 集成，你需要在自定义连接中保存模型的端点和密钥。此设置确保在 Prompt flow 中访问你的自定义 Phi-3 模型。

#### 设置微调后的 Phi-3 模型的 API 密钥和端点 URI

1. 访问 [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo)。

1. 导航到你创建的 Azure Machine Learning 工作区。

1. 从左侧标签中选择 **Endpoints**。

    ![选择端点。](../../../../translated_images/08-06-select-endpoints.75d3bdd7f0b17da0367370d1293f7e7f7b2a65fb7e17390997be0460e8f0b82b.zh.png)

1. 选择你创建的端点。

    ![选择端点。](../../../../translated_images/08-07-select-endpoint-created.851b32efc6058e5863aa62ae8d576a6c20792e24f1862dc6857b9f24a2949f96.zh.png)

1. 从导航菜单中选择 **Consume**。

1. 复制你的 **REST endpoint** 和 **Primary key**。


免责声明：此翻译由AI模型从原文翻译而来，可能不完美。请审阅输出并进行任何必要的修改。