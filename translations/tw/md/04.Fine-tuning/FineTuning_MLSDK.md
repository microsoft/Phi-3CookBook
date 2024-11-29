## 如何使用來自Azure ML系統註冊表的聊天完成組件來微調模型

在這個範例中，我們將使用ultrachat_200k數據集來微調Phi-3-mini-4k-instruct模型，以完成兩個人之間的對話。

![MLFineTune](../../../../translated_images/MLFineTune.d123c711c7564f898ded140931f7c1afda37029a6c396334a66081ba62213083.tw.png)

此範例將向您展示如何使用Azure ML SDK和Python進行微調，然後將微調後的模型部署到在線端點以進行實時推理。

### 訓練數據

我們將使用ultrachat_200k數據集。這是經過嚴格篩選的UltraChat數據集版本，用於訓練Zephyr-7B-β，一個先進的7b聊天模型。

### 模型

我們將使用Phi-3-mini-4k-instruct模型來展示用戶如何微調模型以完成聊天任務。如果您從特定的模型卡打開此筆記本，請記得替換特定的模型名稱。

### 任務

- 選擇要微調的模型。
- 選擇並探索訓練數據。
- 配置微調任務。
- 執行微調任務。
- 查看訓練和評估指標。
- 註冊微調後的模型。
- 部署微調後的模型以進行實時推理。
- 清理資源。

## 1. 設置先決條件

- 安裝依賴項
- 連接到AzureML工作區。了解更多在設置SDK身份驗證。替換<WORKSPACE_NAME>、<RESOURCE_GROUP>和<SUBSCRIPTION_ID>。
- 連接到azureml系統註冊表
- 設置可選的實驗名稱
- 檢查或創建計算資源。

> [!NOTE]
> 要求單個GPU節點可以有多個GPU卡。例如，在Standard_NC24rs_v3的一個節點中有4個NVIDIA V100 GPU，而在Standard_NC12s_v3中有2個NVIDIA V100 GPU。請參考文檔了解此信息。每個節點的GPU卡數量在參數gpus_per_node中設置。正確設置此值將確保節點中所有GPU的利用。推薦的GPU計算SKUs可以在這裡和這裡找到。

### Python庫

運行下面的單元格以安裝依賴項。如果在新環境中運行，這不是可選步驟。

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### 與Azure ML互動

1. 這個Python腳本用於與Azure機器學習（Azure ML）服務互動。以下是它的功能簡介：

    - 它從azure.ai.ml、azure.identity和azure.ai.ml.entities包中導入必要的模塊。它還導入了time模塊。

    - 它嘗試使用DefaultAzureCredential()進行身份驗證，這提供了一個簡化的身份驗證體驗，能夠快速開始開發在Azure雲中運行的應用程序。如果失敗，它會回退到InteractiveBrowserCredential()，這提供了一個交互式登錄提示。

    - 然後它嘗試使用from_config方法創建一個MLClient實例，該方法從默認配置文件（config.json）中讀取配置。如果失敗，它會通過手動提供subscription_id、resource_group_name和workspace_name來創建一個MLClient實例。

    - 它創建另一個MLClient實例，這次是用於名為"azureml"的Azure ML註冊表。這個註冊表是存儲模型、微調管道和環境的地方。

    - 它將experiment_name設置為"chat_completion_Phi-3-mini-4k-instruct"。

    - 它通過將當前時間（自紀元以來的秒數，作為浮點數）轉換為整數，然後轉換為字符串來生成唯一的時間戳。這個時間戳可以用於創建唯一的名稱和版本。

    ```python
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

## 2. 選擇要微調的基礎模型

1. Phi-3-mini-4k-instruct是一個擁有3.8B參數的輕量級、先進的開放模型，基於Phi-2使用的數據集構建。該模型屬於Phi-3模型家族，Mini版本有兩個變體4K和128K，這是它可以支持的上下文長度（以tokens計算）。我們需要微調該模型以便用於我們的特定目的。您可以在AzureML Studio的模型目錄中瀏覽這些模型，按聊天完成任務進行篩選。在這個範例中，我們使用Phi-3-mini-4k-instruct模型。如果您為不同的模型打開此筆記本，請相應地替換模型名稱和版本。

    > [!NOTE]
    > 模型的model id屬性。這將作為輸入傳遞給微調任務。在AzureML Studio模型目錄的模型詳細信息頁面中也可以看到這個資產ID字段。

2. 這個Python腳本與Azure機器學習（Azure ML）服務互動。以下是它的功能簡介：

    - 它將model_name設置為"Phi-3-mini-4k-instruct"。

    - 它使用registry_ml_client對象的models屬性的get方法，從Azure ML註冊表中檢索具有指定名稱的模型的最新版本。get方法被調用時有兩個參數：模型的名稱和指定應檢索模型的最新版本的標籤。

    - 它在控制台中打印一條消息，指示將用於微調的模型的名稱、版本和ID。字符串的format方法用於將模型的名稱、版本和ID插入到消息中。模型的名稱、版本和ID作為foundation_model對象的屬性訪問。

    ```python
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

## 3. 創建要與任務一起使用的計算資源

微調任務僅適用於GPU計算。計算資源的大小取決於模型的大小，在大多數情況下，很難識別適合該任務的正確計算資源。在這個單元格中，我們指導用戶選擇適合該任務的計算資源。

> [!NOTE]
> 下列計算資源與最優配置一起使用。對配置的任何更改可能會導致Cuda Out Of Memory錯誤。在這種情況下，嘗試升級到更大的計算資源。

> [!NOTE]
> 在選擇compute_cluster_size時，確保計算資源在您的資源組中可用。如果特定計算資源不可用，您可以請求獲得該計算資源的訪問權限。

### 檢查模型是否支持微調

1. 這個Python腳本與Azure機器學習（Azure ML）模型互動。以下是它的功能簡介：

    - 它導入ast模塊，該模塊提供處理Python抽象語法樹的函數。

    - 它檢查foundation_model對象（代表Azure ML中的模型）是否有名為finetune_compute_allow_list的標籤。Azure ML中的標籤是可以創建並用於篩選和排序模型的鍵值對。

    - 如果存在finetune_compute_allow_list標籤，它使用ast.literal_eval函數將標籤的值（字符串）安全地解析為Python列表。然後將此列表分配給computes_allow_list變量。它會打印一條消息，指示應從列表中創建計算資源。

    - 如果finetune_compute_allow_list標籤不存在，它將computes_allow_list設置為None，並打印一條消息，指示模型的標籤中不包含finetune_compute_allow_list標籤。

    - 總之，這個腳本正在檢查模型元數據中的特定標籤，如果存在，將標籤的值轉換為列表，並相應地向用戶提供反饋。

    ```python
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

### 檢查計算實例

1. 這個Python腳本與Azure機器學習（Azure ML）服務互動，並對計算實例進行多項檢查。以下是它的功能簡介：

    - 它嘗試從Azure ML工作區中檢索名為compute_cluster的計算實例。如果計算實例的配置狀態為"失敗"，它會引發ValueError。

    - 它檢查computes_allow_list是否不為None。如果不是，它會將列表中的所有計算大小轉換為小寫，並檢查當前計算實例的大小是否在列表中。如果不在，則會引發ValueError。

    - 如果computes_allow_list為None，它會檢查計算實例的大小是否在不支持的GPU VM大小列表中。如果是，則會引發ValueError。

    - 它檢索工作區中所有可用計算大小的列表。然後遍歷此列表，對於每個計算大小，它檢查其名稱是否與當前計算實例的大小匹配。如果匹配，它會檢索該計算大小的GPU數量，並將gpu_count_found設置為True。

    - 如果gpu_count_found為True，它會打印計算實例中的GPU數量。如果gpu_count_found為False，它會引發ValueError。

    - 總之，這個腳本對Azure ML工作區中的計算實例進行多項檢查，包括檢查其配置狀態、其大小是否在允許列表或拒絕列表中，以及其擁有的GPU數量。
    
    ```python
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

## 4. 選擇用於微調模型的數據集

1. 我們使用ultrachat_200k數據集。該數據集有四個拆分，適合於監督微調（sft）。生成排名（gen）。每個拆分的示例數量如下所示：

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. 接下來的幾個單元格顯示了微調的基本數據準備：

### 可視化一些數據行

我們希望這個範例能夠快速運行，因此保存包含5%已經修剪行的train_sft、test_sft文件。這意味著微調後的模型將具有較低的準確性，因此不應用於現實世界。
download-dataset.py用於下載ultrachat_200k數據集並將數據集轉換為可微調管道組件消耗的格式。由於數據集很大，因此我們這裡只有部分數據集。

1. 運行下面的腳本僅下載5%的數據。可以通過更改dataset_split_pc參數來增加這個百分比。

    > [!NOTE]
    > 一些語言模型有不同的語言代碼，因此數據集中的列名應反映相同的情況。

1. 這是一個數據應該如何看起來的示例
聊天完成數據集以parquet格式存儲，每個條目使用以下架構：

    - 這是一個JSON（JavaScript Object Notation）文檔，這是一種流行的數據交換格式。它不是可執行代碼，而是一種存儲和傳輸數據的方式。以下是其結構的簡介：

    - "prompt"：這個鍵持有一個字符串值，表示向AI助手提出的任務或問題。

    - "messages"：這個鍵持有一個對象數組。每個對象表示用戶和AI助手之間對話中的一條消息。每個消息對象有兩個鍵：

    - "content"：這個鍵持有一個字符串值，表示消息的內容。
    - "role"：這個鍵持有一個字符串值，表示發送消息的實體的角色。可以是"user"或"assistant"。
    - "prompt_id"：這個鍵持有一個字符串值，表示提示的唯一標識符。

1. 在這個特定的JSON文檔中，表示用戶要求AI助手創建一個反烏托邦故事的主角。助手回應，用戶然後要求更多細節。助手同意提供更多細節。整個對話與特定的提示ID相關聯。

    ```python
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

### 下載數據

1. 這個Python腳本用於使用名為download-dataset.py的輔助腳本下載數據集。以下是它的功能簡介：

    - 它導入os模塊，該模塊提供使用操作系統相關功能的便攜方式。

    - 它使用os.system函數在shell中運行download-dataset.py腳本，並帶有特定的命令行參數。這些參數指定要下載的數據集（HuggingFaceH4/ultrachat_200k）、下載到的目錄（ultrachat_200k_dataset）和數據集拆分的百分比（5）。os.system函數返回其執行的命令的退出狀態；此狀態存儲在exit_status變量中。

    - 它檢查exit_status是否不為0。在類Unix操作系統中，退出狀態為0通常表示命令成功，而其他任何數字表示錯誤。如果exit_status不為0，它會引發一個Exception，並顯示一條消息，指示下載數據集時出現錯誤。

    - 總之，這個腳本運行一個命令以使用輔助腳本下載數據集，如果命令失敗，它會引發一個異常。
    
    ```python
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

### 將數據加載到DataFrame中

1. 這個Python腳本將JSON Lines文件加載到pandas DataFrame中，並顯示前5行。以下是它的功能簡介：

    - 它導入pandas庫，這是一個功能強大的數據操作和分析庫。

    - 它將pandas的顯示選項中的最大列寬設置為0。這意味著當打印DataFrame時，每列的完整文本將不會被截斷。

    - 它使用pd.read_json函數將ultrachat_200k_dataset目錄中的train_sft.jsonl文件加載到DataFrame中。lines=True參數表示文件為JSON Lines格式，每行是一個單獨的JSON對象。

    - 它使用head方法顯示DataFrame的前5行。如果DataFrame少於5行，它將顯示所有行。

    - 總之，這個腳本將JSON Lines文件加載到DataFrame中，並顯示前5行的完整列文本。
    
    ```python
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

## 5. 使用模型和數據作為輸入提交微調任務

創建使用聊天完成管道組件的任務。了解更多關於微調支持的所有參數。

### 定義微調參數

1. 微調參數可以分為兩類：訓練參數和優化參數

1. 訓練參數定義了訓練方面的內容，例如：

    - 使用的優化器、調度器
    - 用於優化微調的指標
    - 訓練步數和批量大小等
    - 優化參數有助於優化GPU內存和有效使用計算資源。

1. 以下是屬於這一類的一些參數。優化參數因模型而異，並隨模型打包以處理這些變化。

    - 啟用deepspeed和LoRA
    - 啟用混合精度訓練
    - 啟用多節點訓練

> [!NOTE]
> 監督微調可能會導致失去對齊或災難性遺忘。我們建議在微調後檢查這個問題並運行對齊階段。

### 微調參數

1. 這個Python腳本設置了微調機器學習模型的參數。以下是它的功能簡介：

    - 它設置了默認的訓練參數，例如訓練週期數、訓練和評估的批量大小、學習率和學習率調度器類型。

    - 它設置了默認的優化參數，例如是否應用層次相關傳播（LoRa）和DeepSpeed，以及DeepSpeed階段。

    - 它將訓練和優化參數組合到一個名為finetune_parameters的字典中。

    - 它檢查foundation_model是否有任何模型特定的默認參數。如果有，它會打印一條警告消息，並使用這些模型特定的默認參數更新finetune_parameters字典。ast.literal_eval函數用於將模型特定的默認參數從字符串轉換為Python字典。

    - 它打印將用於運行的最終微調參數集。

    - 總之，這個腳本設置並顯示了微調機器學習模型的參數，並能夠使用模型特定的參數覆蓋默認參數。

    ```python
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

### 訓練管道

1. 
根據各種參數設置訓練流水線，然後打印這個顯示名稱。 ```python
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

### 配置流水線

這個Python腳本使用Azure Machine Learning SDK來定義和配置機器學習流水線。以下是它的作用：

1. 它從Azure AI ML SDK導入必要的模塊。
2. 它從註冊表中獲取名為"chat_completion_pipeline"的流水線組件。
3. 它使用`@pipeline` decorator and the function `create_pipeline`. The name of the pipeline is set to `pipeline_display_name`.

1. Inside the `create_pipeline` function, it initializes the fetched pipeline component with various parameters, including the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters.

1. It maps the output of the fine-tuning job to the output of the pipeline job. This is done so that the fine-tuned model can be easily registered, which is required to deploy the model to an online or batch endpoint.

1. It creates an instance of the pipeline by calling the `create_pipeline` function.

1. It sets the `force_rerun` setting of the pipeline to `True`, meaning that cached results from previous jobs will not be used.

1. It sets the `continue_on_step_failure` setting of the pipeline to `False`定義一個流水線任務，意味著如果任何步驟失敗，流水線將停止。
4. 總結來說，這個腳本是使用Azure Machine Learning SDK為聊天完成任務定義和配置一個機器學習流水線。

```python
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

### 提交任務

1. 這個Python腳本向Azure Machine Learning工作區提交一個機器學習流水線任務，然後等待任務完成。以下是它的作用：

    - 它調用workspace_ml_client中的jobs對象的create_or_update方法來提交流水線任務。要運行的流水線由pipeline_object指定，運行任務的實驗由experiment_name指定。
    
    - 然後它調用workspace_ml_client中的jobs對象的stream方法來等待流水線任務完成。要等待的任務由pipeline_job對象的name屬性指定。

    - 總結來說，這個腳本是向Azure Machine Learning工作區提交一個機器學習流水線任務，然後等待任務完成。

```python
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

## 6. 在工作區中註冊微調後的模型

我們將從微調任務的輸出中註冊模型。這將追踪微調模型與微調任務之間的系譜。微調任務進一步追踪基礎模型、數據和訓練代碼的系譜。

### 註冊機器學習模型

1. 這個Python腳本正在註冊一個在Azure Machine Learning流水線中訓練的機器學習模型。以下是它的作用：

    - 它從Azure AI ML SDK導入必要的模塊。
    
    - 它通過調用workspace_ml_client中jobs對象的get方法並訪問其outputs屬性來檢查是否有可用的訓練模型輸出。
    
    - 它通過格式化一個字符串來構建訓練模型的路徑，該字符串包含流水線任務的名稱和輸出的名稱("trained_model")。
    
    - 它通過在原始模型名稱後附加"-ultrachat-200k"並將任何斜杠替換為連字符來定義微調模型的名稱。
    
    - 它準備註冊模型，通過創建一個Model對象，該對象具有各種參數，包括模型的路徑、模型的類型(MLflow模型)、模型的名稱和版本以及模型的描述。
    
    - 它通過調用workspace_ml_client中models對象的create_or_update方法並將Model對象作為參數來註冊模型。
    
    - 它打印註冊的模型。

    - 總結來說，這個腳本正在註冊一個在Azure Machine Learning流水線中訓練的機器學習模型。

```python
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

## 7. 部署微調後的模型到線上端點

線上端點提供了一個持久的REST API，可以用於與需要使用模型的應用集成。

### 管理端點

1. 這個Python腳本正在為註冊的模型在Azure Machine Learning中創建一個受管的線上端點。以下是它的作用：

    - 它從Azure AI ML SDK導入必要的模塊。
    
    - 它通過在字符串"ultrachat-completion-"後附加一個時間戳來定義線上端點的唯一名稱。
    
    - 它準備創建線上端點，通過創建一個ManagedOnlineEndpoint對象，該對象具有各種參數，包括端點的名稱、端點的描述和身份驗證模式("key")。
    
    - 它通過調用workspace_ml_client的begin_create_or_update方法並將ManagedOnlineEndpoint對象作為參數來創建線上端點。然後通過調用wait方法等待創建操作完成。

    - 總結來說，這個腳本正在為註冊的模型在Azure Machine Learning中創建一個受管的線上端點。

```python
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

> [!NOTE]
> 您可以在這裡找到支持部署的SKU列表 - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### 部署機器學習模型

1. 這個Python腳本正在將註冊的機器學習模型部署到Azure Machine Learning中的受管線上端點。以下是它的作用：

    - 它導入ast模塊，該模塊提供處理Python抽象語法樹的函數。
    
    - 它將部署的實例類型設置為"Standard_NC6s_v3"。
    
    - 它檢查基礎模型中是否存在inference_compute_allow_list標籤。如果存在，它將標籤值從字符串轉換為Python列表並分配給inference_computes_allow_list。如果不存在，則將inference_computes_allow_list設置為None。
    
    - 它檢查指定的實例類型是否在允許列表中。如果不在，它會打印一條消息，要求用戶從允許列表中選擇一個實例類型。
    
    - 它準備創建部署，通過創建一個ManagedOnlineDeployment對象，該對象具有各種參數，包括部署的名稱、端點的名稱、模型的ID、實例類型和數量、存活探測設置以及請求設置。
    
    - 它通過調用workspace_ml_client的begin_create_or_update方法並將ManagedOnlineDeployment對象作為參數來創建部署。然後通過調用wait方法等待創建操作完成。
    
    - 它將端點的流量設置為將100%的流量引導到"demo"部署。
    
    - 它通過調用workspace_ml_client的begin_create_or_update方法並將端點對象作為參數來更新端點。然後通過調用result方法等待更新操作完成。

    - 總結來說，這個腳本正在將註冊的機器學習模型部署到Azure Machine Learning中的受管線上端點。

    ```python
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

## 8. 使用樣本數據測試端點

我們將從測試數據集中提取一些樣本數據並提交到線上端點進行推理。然後我們將顯示得分標籤與真實標籤並排顯示。

### 讀取結果

1. 這個Python腳本正在將一個JSON Lines文件讀取到一個pandas DataFrame中，隨機抽取樣本，並重置索引。以下是它的作用：

    - 它將文件./ultrachat_200k_dataset/test_gen.jsonl讀取到一個pandas DataFrame中。由於該文件是JSON Lines格式，每行是一個單獨的JSON對象，因此使用read_json函數並設置lines=True參數。
    
    - 它從DataFrame中隨機抽取1行樣本。使用sample函數並設置n=1參數來指定選擇的隨機行數。
    
    - 它重置DataFrame的索引。使用reset_index函數並設置drop=True參數來刪除原始索引並用新的默認整數值索引替換。
    
    - 它使用head函數並設置參數2來顯示DataFrame的前2行。然而，由於抽樣後DataFrame只包含一行，因此這只會顯示那一行。

    - 總結來說，這個腳本正在將一個JSON Lines文件讀取到一個pandas DataFrame中，隨機抽取1行樣本，重置索引，並顯示第一行。

    ```python
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

### 創建JSON對象

1. 這個Python腳本正在創建一個具有特定參數的JSON對象並將其保存到文件中。以下是它的作用：

    - 它導入json模塊，該模塊提供處理JSON數據的函數。
    
    - 它創建一個字典parameters，其中的鍵和值代表機器學習模型的參數。鍵是"temperature"、"top_p"、"do_sample"和"max_new_tokens"，對應的值分別是0.6、0.9、True和200。
    
    - 它創建另一個字典test_json，包含兩個鍵："input_data"和"params"。"input_data"的值是另一個字典，包含鍵"input_string"和"parameters"。"input_string"的值是一個列表，包含來自test_df DataFrame的第一條消息。"parameters"的值是之前創建的parameters字典。"params"的值是一個空字典。
    
    - 它打開一個名為sample_score.json的文件

    ```python
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

### 調用端點

1. 這個Python腳本正在調用Azure Machine Learning中的線上端點來對JSON文件進行評分。以下是它的作用：

    - 它調用workspace_ml_client對象的online_endpoints屬性的invoke方法。此方法用於向線上端點發送請求並獲取響應。
    
    - 它使用endpoint_name和deployment_name參數指定端點和部署的名稱。在這種情況下，端點名稱存儲在online_endpoint_name變量中，部署名稱為"demo"。
    
    - 它使用request_file參數指定要評分的JSON文件的路徑。在這種情況下，文件是./ultrachat_200k_dataset/sample_score.json。
    
    - 它將端點的響應存儲在response變量中。
    
    - 它打印原始響應。

    - 總結來說，這個腳本正在調用Azure Machine Learning中的線上端點來對JSON文件進行評分並打印響應。

    ```python
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

## 9. 刪除線上端點

1. 不要忘記刪除線上端點，否則將繼續計費端點使用的計算資源。這行Python代碼正在刪除Azure Machine Learning中的一個線上端點。以下是它的作用：

    - 它調用workspace_ml_client對象的online_endpoints屬性的begin_delete方法。此方法用於開始刪除線上端點。
    
    - 它使用name參數指定要刪除的端點名稱。在這種情況下，端點名稱存儲在online_endpoint_name變量中。
    
    - 它調用wait方法等待刪除操作完成。這是一個阻塞操作，意味著它將阻止腳本繼續運行，直到刪除完成。

    - 總結來說，這行代碼正在開始刪除Azure Machine Learning中的一個線上端點並等待操作完成。

    ```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**免責聲明**：
本文件是使用機器翻譯服務進行翻譯的。我們努力確保翻譯的準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件為權威來源。對於關鍵信息，建議使用專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或誤釋不承擔責任。