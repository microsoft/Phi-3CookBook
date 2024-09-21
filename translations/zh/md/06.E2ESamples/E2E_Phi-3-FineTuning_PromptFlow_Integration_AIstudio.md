# 微调和集成自定义 Phi-3 模型与 Azure AI Studio 中的 Prompt flow

这个端到端（E2E）示例基于 Microsoft Tech Community 的指南 "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Studio](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)"。它介绍了在 Azure AI Studio 中使用 Prompt flow 微调、部署和集成自定义 Phi-3 模型的过程。
与需要在本地运行代码的 E2E 示例 "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)" 不同，本教程完全专注于在 Azure AI / ML Studio 内微调和集成您的模型。

## 概述

在这个 E2E 示例中，您将学习如何在 Azure AI Studio 中微调 Phi-3 模型并将其与 Prompt flow 集成。通过利用 Azure AI / ML Studio，您将建立一个部署和使用自定义 AI 模型的工作流程。这个 E2E 示例分为三个场景：

**场景 1: 设置 Azure 资源并准备微调**

**场景 2: 微调 Phi-3 模型并在 Azure Machine Learning Studio 中部署**

**场景 3: 与 Prompt flow 集成并在 Azure AI Studio 中与自定义模型聊天**

以下是这个 E2E 示例的概述。

![Phi-3-FineTuning_PromptFlow_Integration 概述。](../../../../translated_images/00-01-architecture.fa40b38b29f795863378026c4dcc3007b0938b0b43afaf8c331906d03742b2e6.zh.png)

### 目录

1. **[场景 1: 设置 Azure 资源并准备微调](../../../../md/06.E2ESamples)**
    - [创建 Azure Machine Learning 工作区](../../../../md/06.E2ESamples)
    - [在 Azure 订阅中请求 GPU 配额](../../../../md/06.E2ESamples)
    - [添加角色分配](../../../../md/06.E2ESamples)
    - [设置项目](../../../../md/06.E2ESamples)
    - [准备微调数据集](../../../../md/06.E2ESamples)

1. **[场景 2: 微调 Phi-3 模型并在 Azure Machine Learning Studio 中部署](../../../../md/06.E2ESamples)**
    - [微调 Phi-3 模型](../../../../md/06.E2ESamples)
    - [部署微调后的 Phi-3 模型](../../../../md/06.E2ESamples)

1. **[场景 3: 与 Prompt flow 集成并在 Azure AI Studio 中与自定义模型聊天](../../../../md/06.E2ESamples)**
    - [将自定义 Phi-3 模型与 Prompt flow 集成](../../../../md/06.E2ESamples)
    - [与您的自定义 Phi-3 模型聊天](../../../../md/06.E2ESamples)

## 场景 1: 设置 Azure 资源并准备微调

### 创建 Azure Machine Learning 工作区

1. 在门户页面顶部的 **搜索栏** 中输入 *azure machine learning*，然后从出现的选项中选择 **Azure Machine Learning**。

    ![输入 azure machine learning。](../../../../translated_images/01-01-type-azml.98b3003c07da4dbb6885400f66988b3ae05767edb5e8b8ef480e584abe379ca7.zh.png)

2. 从导航菜单中选择 **+ 创建**。

3. 从导航菜单中选择 **新建工作区**。

    ![选择新建工作区。](../../../../translated_images/01-02-select-new-workspace.7648b384cbd786565740c0e5ea203d4710889d5ef23a2abf08428444f6d1a2a6.zh.png)

4. 执行以下任务：

    - 选择您的 Azure **订阅**。
    - 选择要使用的 **资源组**（如有需要请创建一个新的）。
    - 输入 **工作区名称**。它必须是唯一的值。
    - 选择您要使用的 **区域**。
    - 选择要使用的 **存储帐户**（如有需要请创建一个新的）。
    - 选择要使用的 **密钥保管库**（如有需要请创建一个新的）。
    - 选择要使用的 **应用程序洞察**（如有需要请创建一个新的）。
    - 选择要使用的 **容器注册表**（如有需要请创建一个新的）。

    ![填写 azure machine learning。](../../../../translated_images/01-03-fill-AZML.a3f644231a76859c7d92134b7dea1dd0d4df1c11cc615351c95be5a2c7056b03.zh.png)

5. 选择 **查看 + 创建**。

6. 选择 **创建**。

### 在 Azure 订阅中请求 GPU 配额

在本教程中，您将学习如何使用 GPU 微调和部署 Phi-3 模型。对于微调，您将使用 *Standard_NC24ads_A100_v4* GPU，这需要请求配额。对于部署，您将使用 *Standard_NC6s_v3* GPU，这也需要请求配额。

> [!NOTE]
>
> 只有按需付费订阅（标准订阅类型）有资格分配 GPU；当前不支持福利订阅。
>

1. 访问 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 执行以下任务以请求 *Standard NCADSA100v4 Family* 配额：

    - 从左侧选项卡中选择 **配额**。
    - 选择要使用的 **虚拟机系列**。例如，选择 **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**，其中包括 *Standard_NC24ads_A100_v4* GPU。
    - 从导航菜单中选择 **请求配额**。

        ![请求配额。](../../../../translated_images/02-02-request-quota.55f797113d95ad20ca91943eed637488d0aa51d61f3bbe7f080ec466b2ae0666.zh.png)

    - 在请求配额页面中，输入您要使用的 **新核心限制**。例如，24。
    - 在请求配额页面中，选择 **提交** 以请求 GPU 配额。

1. 执行以下任务以请求 *Standard NCSv3 Family* 配额：

    - 从左侧选项卡中选择 **配额**。
    - 选择要使用的 **虚拟机系列**。例如，选择 **Standard NCSv3 Family Cluster Dedicated vCPUs**，其中包括 *Standard_NC6s_v3* GPU。
    - 从导航菜单中选择 **请求配额**。
    - 在请求配额页面中，输入您要使用的 **新核心限制**。例如，24。
    - 在请求配额页面中，选择 **提交** 以请求 GPU 配额。

### 添加角色分配

要微调和部署您的模型，您必须首先创建一个用户分配的托管身份（UAI）并为其分配适当的权限。此 UAI 将在部署期间用于身份验证。

#### 创建用户分配的托管身份（UAI）

1. 在门户页面顶部的 **搜索栏** 中输入 *managed identities*，然后从出现的选项中选择 **Managed Identities**。

    ![输入 managed identities。](../../../../translated_images/03-01-type-managed-identities.2f7b07daa34dc15303b6a3f8c364bc0b7e892dd18aaff361440a030621b540b8.zh.png)

1. 选择 **+ 创建**。

    ![选择创建。](../../../../translated_images/03-02-select-create.0bde775b318f4adba24a7637b31f00f9b685214ed225c5123845a215a260ac71.zh.png)

1. 执行以下任务：

    - 选择您的 Azure **订阅**。
    - 选择要使用的 **资源组**（如有需要请创建一个新的）。
    - 选择您要使用的 **区域**。
    - 输入 **名称**。它必须是唯一的值。

    ![选择创建。](../../../../translated_images/03-03-fill-managed-identities-1.688009e629c1e6952853b94022d3fe97c659c34e29908db17218a5cab6d6add1.zh.png)

1. 选择 **查看 + 创建**。

1. 选择 **+ 创建**。

#### 为托管身份添加贡献者角色分配

1. 导航到您创建的托管身份资源。

1. 从左侧选项卡中选择 **Azure 角色分配**。

1. 从导航菜单中选择 **+ 添加角色分配**。

1. 在添加角色分配页面中，执行以下任务：
    - 将 **范围** 选择为 **资源组**。
    - 选择您的 Azure **订阅**。
    - 选择要使用的 **资源组**。
    - 将 **角色** 选择为 **贡献者**。

    ![填写贡献者角色。](../../../../translated_images/03-04-fill-contributor-role.8bc54b3ac8f64842c82b3379f3c3e9f8d778abf28c00e5b7b471935a86d3ae64.zh.png)

1. 选择 **保存**。

#### 为托管身份添加存储 Blob 数据读取器角色分配

1. 在门户页面顶部的 **搜索栏** 中输入 *storage accounts*，然后从出现的选项中选择 **Storage accounts**。

    ![输入 storage accounts。](../../../../translated_images/03-05-type-storage-accounts.236987db35ba863124c6de8dd16533fe35b96ee4e2dcb9d67e6b279a285f0e6d.zh.png)

1. 选择与您创建的 Azure Machine Learning 工作区关联的存储帐户。例如，*finetunephistorage*。

1. 执行以下任务以导航到添加角色分配页面：

    - 导航到您创建的 Azure 存储帐户。
    - 从左侧选项卡中选择 **访问控制 (IAM)**。
    - 从导航菜单中选择 **+ 添加**。
    - 从导航菜单中选择 **添加角色分配**。

    ![添加角色。](../../../../translated_images/03-06-add-role.dde49177fe7ce1cd1604f620ca5c8ac6442fc516effb057e9f74645f35f9d038.zh.png)

1. 在添加角色分配页面中，执行以下任务：

    - 在角色页面中，在 **搜索栏** 中输入 *Storage Blob Data Reader* 并从出现的选项中选择 **Storage Blob Data Reader**。
    - 在角色页面中选择 **下一步**。
    - 在成员页面中，将 **分配访问权限给** 选择为 **托管身份**。
    - 在成员页面中选择 **+ 选择成员**。
    - 在选择托管身份页面中，选择您的 Azure **订阅**。
    - 在选择托管身份页面中，将 **托管身份** 选择为 **托管身份**。
    - 在选择托管身份页面中，选择您创建的托管身份。例如，*finetunephi-managedidentity*。
    - 在选择托管身份页面中选择 **选择**。

    ![选择托管身份。](../../../../translated_images/03-08-select-managed-identity.f9a44699bf247a4583e2d377e304de8c3d8a602b7d3fed52b9ae790e64e94fe9.zh.png)

1. 选择 **查看 + 分配**。

#### 为托管身份添加 AcrPull 角色分配

1. 在门户页面顶部的 **搜索栏** 中输入 *container registries*，然后从出现的选项中选择 **Container registries**。

    ![输入 container registries。](../../../../translated_images/03-09-type-container-registries.b5519f1fbf49bff0c0d4c95deecd2ef0c61b4870119886c3661014435e2b7095.zh.png)

1. 选择与 Azure Machine Learning 工作区关联的容器注册表。例如，*finetunephicontainerregistry*。

1. 执行以下任务以导航到添加角色分配页面：

    - 从左侧选项卡中选择 **访问控制 (IAM)**。
    - 从导航菜单中选择 **+ 添加**。
    - 从导航菜单中选择 **添加角色分配**。

1. 在添加角色分配页面中，执行以下任务：

    - 在角色页面中，在 **搜索栏** 中输入 *AcrPull* 并从出现的选项中选择 **AcrPull**。
    - 在角色页面中选择 **下一步**。
    - 在成员页面中，将 **分配访问权限给** 选择为 **托管身份**。
    - 在成员页面中选择 **+ 选择成员**。
    - 在选择托管身份页面中，选择您的 Azure **订阅**。
    - 在选择托管身份页面中，将 **托管身份** 选择为 **托管身份**。
    - 在选择托管身份页面中，选择您创建的托管身份。例如，*finetunephi-managedidentity*。
    - 在选择托管身份页面中选择 **选择**。
    - 选择 **查看 + 分配**。

### 设置项目

为了下载微调所需的数据集，您需要设置一个本地环境。

在本练习中，您将：

- 创建一个文件夹来在其中工作。
- 创建一个虚拟环境。
- 安装所需的软件包。
- 创建一个 *download_dataset.py* 文件来下载数据集。

#### 创建一个文件夹来在其中工作

1. 打开一个终端窗口并输入以下命令在默认路径下创建一个名为 *finetune-phi* 的文件夹。

    ```console
    mkdir finetune-phi
    ```

2. 在终端中输入以下命令导航到您创建的 *finetune-phi* 文件夹。

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
> 如果成功，您应该在命令提示符前看到 *(.venv)*。

#### 安装所需的软件包

1. 在终端中输入以下命令安装所需的软件包。

    ```console
    pip install datasets==2.19.1
    ```

#### 创建 `donload_dataset.py`

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

1. 选择您创建的 *finetune-phi* 文件夹，该文件夹位于 *C:\Users\yourUserName\finetune-phi*。

    ![选择您创建的文件夹。](../../../../translated_images/04-01-open-project-folder.f5e2b4ce1cb596eae857303b12909dc0174fd99129d6944c41079f24ee17eed2.zh.png)

1. 在 Visual Studio Code 的左侧窗格中右键单击并选择 **新建文件**，创建一个名为 *download_dataset.py* 的新文件。

    ![创建一个新文件。](../../../../translated_images/04-02-create-new-file.7c51fabe5e84788e34e43f951164471eb07df8363993ce69badc8908f1033613.zh.png)

### 准备微调数据集

在本练习中，您将运行 *download_dataset.py* 文件，将 *ultrachat_200k* 数据集下载到本地环境中。然后，您将使用这些数据集在 Azure Machine Learning 中微调 Phi-3 模型。

在本练习中，您将：

- 向 *download_dataset.py* 文件添加代码以下载数据集。
- 运行 *download_dataset.py* 文件将数据集下载到本地环境中。

#### 使用 *download_dataset.py* 下载数据集

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
        # 如果目录不存在则创建
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # 以写模式打开文件
        with open(filepath, 'w', encoding='utf-8') as f:
            # 遍历数据集中的每条记录
            for record in dataset:
                # 将记录作为 JSON 对象转储并写入文件
                json.dump(record, f)
                # 写入换行符以分隔记录
                f.write('\n')
        
        print(f"数据集已保存到 {filepath}")

    def main():
        """
        加载、拆分和保存数据集的主函数。
        """
        # 使用特定配置和拆分比例加载并拆分 ULTRACHAT_200k 数据集
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

1. 在终端中输入以下命令运行脚本并将数据集下载到本地环境中。

    ```console
    python download_dataset.py
    ```

1. 验证数据集是否已成功保存到本地 *finetune-phi/data* 目录。

> [!NOTE]
>
> #### 关于数据集大小和微调时间的注意事项
>
> 在本教程中，您只使用数据集的 1% (`split='train[:1%]'`)。这显著减少了数据
1. 访问 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 从左侧选项卡中选择 **Compute**。

1. 从导航菜单中选择 **Compute clusters**。

1. 选择 **+ New**。

    ![选择计算资源。](../../../../translated_images/06-01-select-compute.69422609cf19921fb16f550b2566e00870f63ba0caf66b0d26b34e6b0ed21a68.zh.png)

1. 执行以下任务：

    - 选择你想使用的 **Region**。
    - 将 **Virtual machine tier** 选择为 **Dedicated**。
    - 将 **Virtual machine type** 选择为 **GPU**。
    - 将 **Virtual machine size** 筛选器设置为 **Select from all options**。
    - 将 **Virtual machine size** 选择为 **Standard_NC24ads_A100_v4**。

    ![创建集群。](../../../../translated_images/06-02-create-cluster.ad68bcb0914b62972408da8f925632977c54248ff99d2c45761f7e3d33f40fe1.zh.png)

1. 选择 **Next**。

1. 执行以下任务：

    - 输入 **Compute name**。它必须是唯一值。
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

    - 从左侧选项卡中选择 **Model catalog**。
    - 在 **search bar** 中输入 *phi-3-mini-4k*，并从出现的选项中选择 **Phi-3-mini-4k-instruct**。

    ![输入 phi-3-mini-4k。](../../../../translated_images/06-05-type-phi-3-mini-4k.7461addd95ede137f6f018a29681762f85e063477ded6043aafbdf6d742a54e8.zh.png)

1. 从导航菜单中选择 **Fine-tune**。

    ![选择微调。](../../../../translated_images/06-06-select-fine-tune.2c678a7f33294c16ae3ad30ce5d4a78600013dc3a0227e8d341a1962f3aff84d.zh.png)

1. 执行以下任务：

    - 将 **Select task type** 选择为 **Chat completion**。
    - 选择 **+ Select data** 上传 **Traning data**。
    - 将验证数据上传类型选择为 **Provide different validation data**。
    - 选择 **+ Select data** 上传 **Validation data**。

    ![填写微调页面。](../../../../translated_images/06-07-fill-finetuning.c76431cc247b6398fb9d33da62841adf87d5eebaa92cd79e80bd7bcbed49f1d3.zh.png)

    > [!TIP]
    >
    > 你可以选择 **Advanced settings** 来自定义配置，如 **learning_rate** 和 **lr_scheduler_type**，以根据你的具体需求优化微调过程。

1. 选择 **Finish**。

1. 在本次练习中，你成功地使用 Azure Machine Learning 微调了 Phi-3 模型。请注意，微调过程可能需要相当长的时间。运行微调任务后，你需要等待其完成。你可以通过导航到 Azure Machine Learning 工作区左侧的 Jobs 选项卡来监控微调任务的状态。在下一系列中，你将部署微调后的模型并将其与 Prompt flow 集成。

    ![查看微调任务。](../../../../translated_images/06-08-output.9f9cf6f9e9e83533b793a5ff3066b09475e299999fead6f98dfb102f48db0061.zh.png)

### 部署微调后的 Phi-3 模型

要将微调后的 Phi-3 模型与 Prompt flow 集成，你需要部署模型以使其可用于实时推理。此过程涉及注册模型、创建在线端点并部署模型。

在本次练习中，你将：

- 在 Azure Machine Learning 工作区注册微调后的模型。
- 创建一个在线端点。
- 部署已注册的微调后的 Phi-3 模型。

#### 注册微调后的模型

1. 访问 [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)。

1. 选择你创建的 Azure Machine Learning 工作区。

    ![选择你创建的工作区。](../../../../translated_images/06-04-select-workspace.5e35488b3bb3e391ead6688243c52fc2aecb8ae7f1c738b91b49580f9db353cf.zh.png)

1. 从左侧选项卡中选择 **Models**。
1. 选择 **+ Register**。
1. 选择 **From a job output**。

    ![注册模型。](../../../../translated_images/07-01-register-model.9b64d29736e0be32343b36a503d7e38c47c22d9edfa554aae179352982fdf96b.zh.png)

1. 选择你创建的任务。

    ![选择任务。](../../../../translated_images/07-02-select-job.712abf18cdae5256776907df3ed30df53d297ff8d475fb64d5c03e92304db6ef.zh.png)

1. 选择 **Next**。

1. 将 **Model type** 选择为 **MLflow**。

1. 确保 **Job output** 已选择；它应该会自动选择。

    ![选择输出。](../../../../translated_images/07-03-select-output.45098161b7ddfda4b8d4d62676da0488a32a16e838ff03f37bfd71b9886da798.zh.png)

1. 选择 **Next**。

1. 选择 **Register**。

    ![选择注册。](../../../../translated_images/07-04-register.3403ed7976f07fbfc27210550cf2f793d9cf778032ea276ecb287bd9df88f188.zh.png)

1. 你可以通过导航到左侧选项卡中的 **Models** 菜单查看已注册的模型。

    ![已注册的模型。](../../../../translated_images/07-05-registered-model.90693749513e55231e8904304e4ea1f9e29ab659bc1926ea69dffd25e77ffb2d.zh.png)

#### 部署微调后的模型

1. 导航到你创建的 Azure Machine Learning 工作区。

1. 从左侧选项卡中选择 **Endpoints**。

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
    - 输入 **Endpoint name**。它必须是唯一值。
    - 输入 **Deployment name**。它必须是唯一值。

    ![填写部署设置。](../../../../translated_images/07-08-deployment-setting.5449edf53b27f5457cc68d2285d355a7d364b01423a51e5af63e7c52374a3a79.zh.png)

1. 选择 **Deploy**。

> [!WARNING]
> 为避免对你的账户产生额外费用，请确保在 Azure Machine Learning 工作区中删除创建的端点。
>

#### 检查 Azure Machine Learning 工作区中的部署状态

1. 导航到你创建的 Azure Machine Learning 工作区。

1. 从左侧选项卡中选择 **Endpoints**。

1. 选择你创建的端点。

    ![选择端点](../../../../translated_images/07-09-check-deployment.8e4465a7585b3c22db5fc9d5757269a919b5104fdeb5f736fa573ca9b3e16abe.zh.png)

1. 在此页面上，你可以在部署过程中管理端点。

> [!NOTE]
> 部署完成后，确保 **Live traffic** 设置为 **100%**。如果没有，请选择 **Update traffic** 来调整流量设置。请注意，如果流量设置为 0%，你将无法测试模型。
>
> ![设置流量。](../../../../translated_images/07-10-set-traffic.1d1b24b39c7ec80451c99fe05298fac636f0cd449e7be282736f6c06a1a70875.zh.png)
>

## 场景 3：与 Prompt flow 集成并在 Azure AI Studio 中与自定义模型聊天

### 将自定义 Phi-3 模型与 Prompt flow 集成

成功部署微调后的模型后，你现在可以将其与 Prompt Flow 集成，以在实时应用程序中使用你的模型，从而启用各种与自定义 Phi-3 模型的交互任务。

在本次练习中，你将：

- 创建 Azure AI Studio Hub。
- 创建 Azure AI Studio 项目。
- 创建 Prompt flow。
- 为微调后的 Phi-3 模型添加自定义连接。
- 设置 Prompt flow 以与自定义 Phi-3 模型聊天。

> [!NOTE]
> 你也可以使用 Azure ML Studio 与 Promptflow 集成。同样的集成过程可以应用于 Azure ML Studio。

#### 创建 Azure AI Studio Hub

在创建项目之前，你需要创建一个 Hub。Hub 类似于资源组，允许你在 Azure AI Studio 中组织和管理多个项目。

1. 访问 [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)。

1. 从左侧选项卡中选择 **All hubs**。

1. 从导航菜单中选择 **+ New hub**。

    ![创建 hub。](../../../../translated_images/08-01-create-hub.1df80696bf3376f0e56ffa90de1fc35962acf2fc3c1a3a6b254015b8b993e55e.zh.png)

1. 执行以下任务：

    - 输入 **Hub name**。它必须是唯一值。
    - 选择你的 Azure **Subscription**。
    - 选择要使用的 **Resource group**（如有需要可创建一个新的）。
    - 选择你想使用的 **Location**。
    - 选择要使用的 **Connect Azure AI Services**（如有需要可创建一个新的）。
    - 将 **Connect Azure AI Search** 选择为 **Skip connecting**。

    ![填写 hub。](../../../../translated_images/08-02-fill-hub.fc194526614a5811e7b57e699911be39babdc95aa425b6c4a72f064948865ce3.zh.png)

1. 选择 **Next**。

#### 创建 Azure AI Studio 项目

1. 在你创建的 Hub 中，从左侧选项卡中选择 **All projects**。

1. 从导航菜单中选择 **+ New project**。

    ![选择新项目。](../../../../translated_images/08-04-select-new-project.dc11f26658c3c3f9d0fcf3232a954abfc115de5eb74da21d5be229c9c1be2875.zh.png)

1. 输入 **Project name**。它必须是唯一值。

    ![创建项目。](../../../../translated_images/08-05-create-project.61caaa28c1b9b696bf29de6b002bbb2040dbaeb764adab161dcb3472fe789aea.zh.png)

1. 选择 **Create a project**。

#### 为微调后的 Phi-3 模型添加自定义连接

要将你的自定义 Phi-3 模型与 Prompt flow 集成，你需要在自定义连接中保存模型的端点和密钥。此设置确保在 Prompt flow 中访问你的自定义 Phi-3 模型。

#### 设置微调后的 Phi-3 模型的 API 密钥和端点 URI

1. 访问 [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo)。

1. 导航到你创建的 Azure Machine learning 工作区。

1. 从左侧选项卡中选择 **Endpoints**。

    ![选择端点。](../../../../translated_images/08-06-select-endpoints.75d3bdd7f0b17da0367370d1293f7e7f7b2a65fb7e17390997be0460e8f0b82b.zh.png)

1. 选择你创建的端点。

    ![选择已创建的端点。](../../../../translated_images/08-07-select-endpoint-created.851b32efc6058e5863aa62ae8d576a6c20792e24f1862dc6857b9f24a2949f96.zh.png)

1. 从导航菜单中选择 **Consume**。

1. 复制你的 **REST endpoint** 和 **Primary key**。
![复制 API 密钥和终端 URI。](../../../../translated_images/08-08-copy-endpoint-key.947512a4c95b5dd9fc5a606bad4244bf9b136929c1fab06570c463311ef29df1.zh.png)

#### 添加自定义连接

1. 访问 [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)。

1. 导航到你创建的 Azure AI Studio 项目。

1. 在你创建的项目中，从左侧标签中选择 **Settings**。

1. 选择 **+ New connection**。

    ![选择新连接。](../../../../translated_images/08-09-select-new-connection.b5e93c85028739875916f34a1821b0b086f0e993b8d7d7388c100e3a38b70bbd.zh.png)

1. 从导航菜单中选择 **Custom keys**。

    ![选择自定义密钥。](../../../../translated_images/08-10-select-custom-keys.077f17a1a49b8f76e446453b6a68c09c2aa08291818d98edcf39e3013c5b45ac.zh.png)

1. 执行以下任务：

    - 选择 **+ Add key value pairs**。
    - 在密钥名称中输入 **endpoint** 并将你从 Azure ML Studio 复制的终端粘贴到值字段中。
    - 再次选择 **+ Add key value pairs**。
    - 在密钥名称中输入 **key** 并将你从 Azure ML Studio 复制的密钥粘贴到值字段中。
    - 添加密钥后，选择 **is secret** 以防止密钥暴露。

    ![添加连接。](../../../../translated_images/08-11-add-connection.01279deb77ede4d195b17ecabae70979976834892e9dbb3354f504bb6edaa6e1.zh.png)

1. 选择 **Add connection**。

#### 创建 Prompt flow

你已经在 Azure AI Studio 中添加了自定义连接。现在，让我们按照以下步骤创建一个 Prompt flow。然后，你将把这个 Prompt flow 连接到自定义连接，以便在 Prompt flow 中使用微调后的模型。

1. 导航到你创建的 Azure AI Studio 项目。

1. 从左侧标签中选择 **Prompt flow**。

1. 从导航菜单中选择 **+ Create**。

    ![选择 Promptflow。](../../../../translated_images/08-12-select-promptflow.5e0527f1e5102c604e0e8a34f2321e28f8c815ec2908ae7038f012a088ff2bbc.zh.png)

1. 从导航菜单中选择 **Chat flow**。

    ![选择聊天流。](../../../../translated_images/08-13-select-flow-type.e3fb41375041faa4d058304c319329d5f45f87139143b384f056bb500076ca73.zh.png)

1. 输入 **Folder name** 以供使用。

    ![输入名称。](../../../../translated_images/08-14-enter-name.90db481f18468cfd78b281825cb5484ab7236cfa29d59d287b7b0f423516e6ea.zh.png)

1. 选择 **Create**。

#### 设置 Prompt flow 与你的自定义 Phi-3 模型聊天

你需要将微调后的 Phi-3 模型集成到 Prompt flow 中。然而，现有的 Prompt flow 并不是为此目的设计的。因此，你必须重新设计 Prompt flow 以实现自定义模型的集成。

1. 在 Prompt flow 中，执行以下任务以重建现有流：

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

    ![选择原始文件模式。](../../../../translated_images/08-15-select-raw-file-mode.28d80142df9d540c66c37d17825cec921bb1f7b54e386223bb4ad38df10e5e2d.zh.png)

1. 将以下代码添加到 *integrate_with_promptflow.py* 文件中，以在 Prompt flow 中使用自定义 Phi-3 模型。

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # 日志设置
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        使用自定义连接发送请求到 Phi-3 模型终端，带有给定的输入数据。
        """

        # "connection" 是自定义连接的名称，"endpoint" 和 "key" 是自定义连接中的密钥
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
            
            # 记录完整的 JSON 响应
            logger.debug(f"完整的 JSON 响应：{response.json()}")

            result = response.json()["output"]
            logger.info("成功从 Azure ML 终端接收到响应。")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"查询 Azure ML 终端时出错：{e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        处理输入数据并查询 Phi-3 模型的工具函数。
        """
        return query_phi3_model(input_data, connection)

    ```

    ![粘贴 Prompt flow 代码。](../../../../translated_images/08-16-paste-promptflow-code.c27a93ed6134adbe7ce618ffad7300923f3c02defedef0b5598eab5a6ee2afc2.zh.png)

> [!NOTE]
> 有关在 Azure AI Studio 中使用 Prompt flow 的更多详细信息，你可以参考 [Azure AI Studio 中的 Prompt flow](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)。

1. 选择 **Chat input** 和 **Chat output** 以启用与模型的聊天功能。

    ![输入输出。](../../../../translated_images/08-17-select-input-output.d188ea79fc21d29e615b6cc50d638214a2dcbc3b3ccb16009aa67698227d2765.zh.png)

1. 现在你已经准备好与自定义 Phi-3 模型聊天了。在下一个练习中，你将学习如何启动 Prompt flow 并使用它与微调后的 Phi-3 模型聊天。

> [!NOTE]
>
> 重建后的流应如下图所示：
>
> ![流示例。](../../../../translated_images/08-18-graph-example.48c427864370ac7dd02e500bc3a0ff49785d4480e489b4dfe25e529da99f193f.zh.png)
>

### 与你的自定义 Phi-3 模型聊天

现在你已经微调并集成了自定义 Phi-3 模型到 Prompt flow 中，你已经准备好开始与它互动。这个练习将指导你设置并启动与模型的聊天过程。通过遵循这些步骤，你将能够充分利用微调后的 Phi-3 模型的各种功能和对话能力。

- 使用 Prompt flow 与你的自定义 Phi-3 模型聊天。

#### 启动 Prompt flow

1. 选择 **Start compute sessions** 以启动 Prompt flow。

    ![启动计算会话。](../../../../translated_images/09-01-start-compute-session.9d080c30a6fc78a8b23ac54e7c8b11aeecc005d3da03cb0f9bd8afc298151ffa.zh.png)

1. 选择 **Validate and parse input** 以更新参数。

    ![验证输入。](../../../../translated_images/09-02-validate-input.db05a40e29a21b333848b7c03542b0ec521ce9c6fbe12fba51c2addcb1c07c68.zh.png)

1. 选择 **connection** 的 **Value** 以连接到你创建的自定义连接。例如，*connection*。

    ![连接。](../../../../translated_images/09-03-select-connection.de0137da33c86e581425cef4a25957d86140d1605968f6f7c98207b8e715cca8.zh.png)

#### 与你的自定义模型聊天

1. 选择 **Chat**。

    ![选择聊天。](../../../../translated_images/09-04-select-chat.87b90a2f41e38714f40dedde608d349bfaca00a75f08166816dddb92de711e32.zh.png)

1. 以下是结果示例：现在你可以与自定义 Phi-3 模型聊天了。建议根据用于微调的数据进行提问。

    ![使用 Prompt flow 聊天。](../../../../translated_images/09-05-chat-with-promptflow.46c9fdf0e6de0e15e9618f654830e52bd8ead4aec0de57bb960206321d2bd0bd.zh.png)

免责声明：本翻译由人工智能模型从原文翻译而来，可能不够完美。请审阅输出内容并进行必要的修正。