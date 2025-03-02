## 如何使用 Azure ML 系統註冊表中的聊天完成元件來微調模型

在此範例中，我們將使用 ultrachat_200k 資料集，微調 Phi-3-mini-4k-instruct 模型，以完成兩人之間的對話。

![MLFineTune](../../../../translated_images/MLFineTune.d8292fe1f146b4ff1153c2e5bdbbe5b0e7f96858d5054b525bd55f2641505138.tw.png)

此範例將展示如何使用 Azure ML SDK 和 Python 進行微調，然後將微調後的模型部署到線上端點以進行即時推論。

### 訓練數據

我們將使用 ultrachat_200k 資料集。這是一個經過大量篩選的 UltraChat 資料集版本，並被用於訓練 Zephyr-7B-β，一個先進的 7b 聊天模型。

### 模型

我們將使用 Phi-3-mini-4k-instruct 模型，來展示如何微調模型以執行聊天完成任務。如果您是從特定模型卡打開此筆記本，請記得替換為具體的模型名稱。

### 任務

- 選擇一個模型進行微調。
- 選擇並探索訓練數據。
- 配置微調任務。
- 執行微調任務。
- 檢查訓練和評估指標。
- 註冊微調後的模型。
- 部署微調後的模型以進行即時推論。
- 清理資源。

## 1. 設置先決條件

- 安裝依賴項
- 連接到 AzureML 工作區。了解更多資訊，請參閱設置 SDK 驗證。替換 <WORKSPACE_NAME>、<RESOURCE_GROUP> 和 <SUBSCRIPTION_ID>。
- 連接到 azureml 系統註冊表
- 設置可選的實驗名稱
- 檢查或創建計算資源。

> [!NOTE]
> 要求：單個 GPU 節點可以有多個 GPU 卡。例如，在 Standard_NC24rs_v3 節點中有 4 個 NVIDIA V100 GPU，而在 Standard_NC12s_v3 中有 2 個 NVIDIA V100 GPU。參考文檔以獲取此資訊。每節點的 GPU 卡數量在參數 gpus_per_node 中設置。正確設置此值將確保充分利用節點中的所有 GPU。推薦的 GPU 計算 SKU 可在此處和此處找到。

### Python 庫

通過運行以下程式碼安裝依賴項。如果在新環境中運行，這不是可選步驟。

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### 與 Azure ML 交互

1. 此 Python 腳本用於與 Azure 機器學習 (Azure ML) 服務進行交互。以下是其功能的簡要說明：

    - 它從 azure.ai.ml、azure.identity 和 azure.ai.ml.entities 套件中導入必要的模組。此外還導入了 time 模組。

    - 它嘗試使用 DefaultAzureCredential() 進行身份驗證，這提供了一種簡化的驗證體驗，以快速開始開發在 Azure 雲中運行的應用程式。如果失敗，則回退到 InteractiveBrowserCredential()，這提供了一個交互式登錄提示。

    - 它嘗試使用 from_config 方法創建一個 MLClient 實例，該方法從默認配置文件 (config.json) 中讀取配置。如果失敗，則通過手動提供 subscription_id、resource_group_name 和 workspace_name 創建 MLClient 實例。

    - 它為名為 "azureml" 的 Azure ML 註冊表創建另一個 MLClient 實例。此註冊表用於存儲模型、微調管道和環境。

    - 它將 experiment_name 設置為 "chat_completion_Phi-3-mini-4k-instruct"。

    - 它通過將當前時間（以自 Unix 紀元以來的秒數表示的浮點數）轉換為整數，然後轉換為字符串，生成一個唯一的時間戳。此時間戳可用於創建唯一的名稱和版本。

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

## 2. 選擇一個基礎模型進行微調

1. Phi-3-mini-4k-instruct 是一個擁有 3.8B 參數的輕量級先進開放模型，基於 Phi-2 使用的數據集構建。該模型屬於 Phi-3 模型系列，Mini 版本有兩個變體：4K 和 128K，這是它可以支持的上下文長度（以 tokens 為單位）。我們需要針對特定用途微調該模型才能使用它。您可以在 AzureML Studio 的模型目錄中瀏覽這些模型，並通過聊天完成任務進行篩選。在此範例中，我們使用 Phi-3-mini-4k-instruct 模型。如果您是為其他模型打開此筆記本，請根據需要替換模型名稱和版本。

    > [!NOTE]
    > 模型的 model id 屬性將作為微調任務的輸入。在 AzureML Studio 模型目錄的模型詳細信息頁面的 Asset ID 欄位中也可以找到此屬性。

2. 此 Python 腳本與 Azure 機器學習 (Azure ML) 服務進行交互。以下是其功能的簡要說明：

    - 它將 model_name 設置為 "Phi-3-mini-4k-instruct"。

    - 它使用 registry_ml_client 對象的 models 屬性的 get 方法，從 Azure ML 註冊表中檢索具有指定名稱的最新版本模型。get 方法接受兩個參數：模型名稱和指定應檢索模型最新版本的標籤。

    - 它在控制台上打印一條消息，指示將用於微調的模型的名稱、版本和 id。字符串的 format 方法用於將模型的名稱、版本和 id 插入消息中。模型的名稱、版本和 id 作為 foundation_model 對象的屬性訪問。

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

## 3. 創建用於任務的計算資源

微調任務僅適用於 GPU 計算。計算資源的大小取決於模型的大小，在大多數情況下，確定適合任務的計算資源可能會很棘手。在此部分，我們指導用戶選擇適合任務的計算資源。

> [!NOTE]
> 以下列出的計算資源與最優化配置配合使用。對配置的任何更改可能導致 Cuda 記憶體不足錯誤。在這種情況下，請嘗試將計算資源升級到更大的規模。

> [!NOTE]
> 在選擇 compute_cluster_size 時，請確保該計算資源在您的資源群組中可用。如果某個特定計算資源不可用，您可以提出申請以獲得該計算資源的訪問權限。

### 檢查模型是否支持微調

1. 此 Python 腳本與 Azure 機器學習 (Azure ML) 模型進行交互。以下是其功能的簡要說明：

    - 它導入 ast 模組，該模組提供處理 Python 抽象語法樹的函數。

    - 它檢查 foundation_model 對象（代表 Azure ML 中的一個模型）是否具有名為 finetune_compute_allow_list 的標籤。Azure ML 中的標籤是您可以創建並用於篩選和排序模型的鍵值對。

    - 如果存在 finetune_compute_allow_list 標籤，它使用 ast.literal_eval 函數將標籤的值（字符串）安全地解析為 Python 列表。然後將此列表分配給 computes_allow_list 變數。接著，它打印一條消息，指示應從該列表中創建計算資源。

    - 如果 finetune_compute_allow_list 標籤不存在，它將 computes_allow_list 設置為 None，並打印一條消息，指示該標籤不在模型的標籤中。

    - 總之，該腳本正在檢查模型元數據中的特定標籤，如果存在則將標籤的值轉換為列表，並相應地向用戶提供反饋。

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

1. 此 Python 腳本與 Azure 機器學習 (Azure ML) 服務進行交互，並對計算實例進行多項檢查。以下是其功能的簡要說明：

    - 它嘗試從 Azure ML 工作區中檢索名為 compute_cluster 的計算實例。如果計算實例的配置狀態為 "failed"，則引發 ValueError。

    - 它檢查 computes_allow_list 是否為 None。如果不是，它將列表中的所有計算資源大小轉換為小寫，並檢查當前計算實例的大小是否在列表中。如果不在，則引發 ValueError。

    - 如果 computes_allow_list 為 None，它檢查計算實例的大小是否在不支持的 GPU VM 大小列表中。如果是，則引發 ValueError。

    - 它檢索工作區中所有可用計算資源大小的列表。然後遍歷該列表，對於每個計算資源大小，檢查其名稱是否與當前計算實例的大小匹配。如果匹配，它檢索該計算資源大小的 GPU 數量，並將 gpu_count_found 設置為 True。

    - 如果 gpu_count_found 為 True，它打印計算實例中的 GPU 數量。如果 gpu_count_found 為 False，則引發 ValueError。

    - 總之，該腳本正在對 Azure ML 工作區中的計算實例進行多項檢查，包括檢查其配置狀態、其大小是否在允許列表或拒絕列表中，以及其 GPU 的數量。

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

1. 我們使用 ultrachat_200k 資料集。該資料集有四個分割，適合於監督微調（sft）和生成排名（gen）。每個分割的示例數量如下所示：

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. 接下來的幾個程式碼塊展示了用於微調的基本數據準備：

### 可視化一些數據行

我們希望此示例能快速運行，因此保存包含已修剪行的 5% 的 train_sft 和 test_sft 文件。這意味著微調後的模型將具有較低的準確性，因此不應用於實際應用場景。
download-dataset.py 用於下載 ultrachat_200k 資料集，並將資料集轉換為微調管道元件可消費的格式。此外，由於資料集較大，因此此處僅包含部分資料集。

1. 運行以下腳本僅下載 5% 的數據。可以通過更改 dataset_split_pc 參數到所需的百分比來增加。

    > [!NOTE]
    > 某些語言模型有不同的語言代碼，因此資料集中的欄位名稱應反映這些差異。

1. 以下是數據應該如何呈現的示例：
聊天完成資料集以 parquet 格式存儲，每個條目使用以下架構：

    - 這是一個 JSON（JavaScript 物件表示法）文檔，這是一種流行的數據交換格式。它不是可執行代碼，而是一種存儲和傳輸數據的方式。以下是其結構的說明：

    - "prompt"：此鍵包含一個字符串值，表示給 AI 助手的任務或問題。

    - "messages"：此鍵包含一個物件陣列。每個物件表示用戶與 AI 助手之間對話中的一條消息。每個消息物件有兩個鍵：

    - "content"：此鍵包含一個字符串值，表示消息的內容。
    - "role"：此鍵包含一個字符串值，表示發送消息的實體的角色。可以是 "user" 或 "assistant"。
    - "prompt_id"：此鍵包含一個字符串值，表示提示的唯一標識符。

1. 在此特定 JSON 文檔中，對話表示用戶請求 AI 助手為反烏托邦故事創建主角。助手回應後，用戶進一步要求更多細節。助手同意提供更多細節。整個對話與一個特定的 prompt_id 關聯。

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

1. 此 Python 腳本用於通過名為 download-dataset.py 的輔助腳本下載資料集。以下是其功能的簡要說明：

    - 它導入 os 模組，該模組提供使用與操作系統相關功能的便攜方式。

    - 它使用 os.system 函數在 shell 中運行 download-dataset.py 腳本並指定命令行參數。參數指定要下載的資料集 (HuggingFaceH4/ultrachat_200k)、下載目錄 (ultrachat_200k_dataset) 和資料集分割百分比 (5)。os.system 函數返回其執行命令的退出狀態；此狀態存儲在 exit_status 變數中。

    - 它檢查 exit_status 是否為 0。如果不是 0，則引發 Exception 並顯示一條消息，指示下載資料集時出現錯誤。

    - 總之，此腳本運行命令以使用輔助腳本下載資料集，並在命令失敗時引發異常。

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

### 將數據加載到 DataFrame 中

1. 此 Python 腳本將 JSON Lines 文件加載到 pandas DataFrame 中並顯示前 5 行。以下是其功能的簡要說明：

    - 它導入 pandas 庫，這是一個功能強大的數據操作和分析庫。

    - 它將 pandas 的顯示選項中的最大欄位寬度設置為 0。這意味著當打印 DataFrame 時，將顯示每個欄位的完整文本而不會被截斷。

    - 它使用 pd.read_json 函數將 ultrachat_200k_dataset 目錄中的 train_sft.jsonl 文件加載到 DataFrame 中。lines=True 參數表示該文件是 JSON Lines 格式，每行是一個單獨的 JSON 對象。

    - 它使用 head 方法顯示 DataFrame 的前 5 行。如果 DataFrame 少於 5 行，則顯示所有行。

    - 總之，此腳本將 JSON Lines 文件加載到 DataFrame 並顯示前 5 行，帶有完整的欄位文本。

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

創建使用聊天完成管道元件的任務。了解更多支持的微調參數。

### 定義微調參數

1. 微調參數可分為兩類：訓練參數和優化參數。

1. 訓練參數定義了訓練方面，例如：

    - 要使用的優化器和調度器
    - 用於優化微調的指標
    - 訓練步數、批次大小等
    - 優化參數幫助優化 GPU 記憶體並有效利用計算資源。

1. 以下是屬於此類別的一些參數。優化參數因模型而異，並與模型一起打包以處理這些差異。

    - 啟用 DeepSpeed 和 LoRA
    - 啟用混合精度訓練
    - 啟用多節點訓練

> [!NOTE]
> 監督微調可能導致對齊喪失或災難性遺忘。我們建議在微調後檢查此問題並運行對齊階段。

### 微調參數

1. 此 Python 腳本設置了微調機器學習模型的參數。以下是其功能的簡要說明：

    - 設置了預設的訓練參數，例如訓練週期數、訓練和評估的批次大小、學習率以及學習率調度類型。

    - 設置了預設的優化參數，例如是否應用 Layer-wise Relevance Propagation (LoRa) 和 DeepSpeed，以及 DeepSpeed 階段。

    - 將訓練和優化參數合併到名為 finetune_parameters 的單一字典中。

    - 檢查 foundation_model 是否具有任何模型特定的預設參數。如果有，則打印警告消息並使用這些模型特定的預設值更新 finetune_parameters 字典。使用 ast.literal_eval 函數將模型特定的預設值從字符串轉換為 Python 字典。

    - 打印將用於運行的最終微調參數集。

    - 總之，此腳本設置並顯示微調機器學習模型的參數，並能夠用模型特定的參數覆蓋預設
### 訓練管道

基於不同的參數建立訓練管道，並打印出此顯示名稱。  
```python
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

此 Python 腳本使用 Azure Machine Learning SDK 定義並配置機器學習管道。以下是它的主要功能分解：  

1. 它從 Azure AI ML SDK 中匯入必要的模組。  
2. 它從註冊表中提取名為 "chat_completion_pipeline" 的管道元件。  
3. 它使用以下參數定義一個管道工作：  
   `@pipeline` decorator and the function `create_pipeline`. The name of the pipeline is set to `pipeline_display_name`.

1. Inside the `create_pipeline` function, it initializes the fetched pipeline component with various parameters, including the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters.

1. It maps the output of the fine-tuning job to the output of the pipeline job. This is done so that the fine-tuned model can be easily registered, which is required to deploy the model to an online or batch endpoint.

1. It creates an instance of the pipeline by calling the `create_pipeline` function.

1. It sets the `force_rerun` setting of the pipeline to `True`, meaning that cached results from previous jobs will not be used.

1. It sets the `continue_on_step_failure` setting of the pipeline to `False`，這表示如果任一步驟失敗，管道將停止執行。  

簡而言之，此腳本使用 Azure Machine Learning SDK 定義並配置了一個針對聊天完成任務的機器學習管道。  
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

### 提交工作

1. 此 Python 腳本將機器學習管道工作提交到 Azure Machine Learning 工作區，並等待工作完成。以下是它的主要功能分解：  

   - 它調用 `workspace_ml_client` 中 `jobs` 物件的 `create_or_update` 方法來提交管道工作。要運行的管道由 `pipeline_object` 指定，工作所屬的實驗由 `experiment_name` 指定。  
   - 它隨後調用 `workspace_ml_client` 中 `jobs` 物件的 `stream` 方法來等待管道工作完成。要等待的工作由 `pipeline_job` 物件的 `name` 屬性指定。  

簡而言之，此腳本將機器學習管道工作提交到 Azure Machine Learning 工作區，並等待工作完成。  
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

## 6. 將微調後的模型註冊到工作區

我們將從微調工作的輸出中註冊模型。這將追蹤微調模型與微調工作的關聯。微調工作進一步追蹤基礎模型、數據和訓練代碼的關聯。  

### 註冊機器學習模型

1. 此 Python 腳本將一個在 Azure Machine Learning 管道中訓練的機器學習模型進行註冊。以下是它的主要功能分解：  

   - 它從 Azure AI ML SDK 中匯入必要的模組。  
   - 它通過調用 `workspace_ml_client` 中 `jobs` 物件的 `get` 方法並訪問其 `outputs` 屬性，檢查管道工作是否提供了 `trained_model` 的輸出。  
   - 它通過格式化字符串構建訓練模型的路徑，該路徑包含管道工作的名稱和輸出名稱 ("trained_model")。  
   - 它為微調模型定義名稱，將 "-ultrachat-200k" 附加到原始模型名稱，並將任何斜線替換為連字符。  
   - 它準備註冊模型，通過創建一個 `Model` 物件，包含模型路徑、模型類型 (MLflow 模型)、模型名稱和版本，以及模型描述等參數。  
   - 它通過調用 `workspace_ml_client` 中 `models` 物件的 `create_or_update` 方法，並將 `Model` 物件作為參數來註冊模型。  
   - 它打印出註冊的模型。  

簡而言之，此腳本將一個在 Azure Machine Learning 管道中訓練的機器學習模型進行註冊。  
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

## 7. 將微調後的模型部署到線上端點

線上端點提供一個持久的 REST API，可用於與需要使用模型的應用程式整合。  

### 管理端點

1. 此 Python 腳本為註冊的模型在 Azure Machine Learning 中創建一個管理線上端點。以下是它的主要功能分解：  

   - 它從 Azure AI ML SDK 中匯入必要的模組。  
   - 它通過將時間戳附加到字符串 "ultrachat-completion-" 來定義線上端點的唯一名稱。  
   - 它準備創建線上端點，通過創建一個 `ManagedOnlineEndpoint` 物件，包含端點名稱、端點描述以及身份驗證模式 ("key") 等參數。  
   - 它通過調用 `workspace_ml_client` 的 `begin_create_or_update` 方法，並將 `ManagedOnlineEndpoint` 物件作為參數來創建線上端點。隨後，它通過調用 `wait` 方法等待創建操作完成。  

簡而言之，此腳本為註冊的模型在 Azure Machine Learning 中創建了一個管理線上端點。  
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
> 您可以在此處找到支持部署的 SKU 列表 - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)  

### 部署機器學習模型

1. 此 Python 腳本將一個註冊的機器學習模型部署到 Azure Machine Learning 中的管理線上端點。以下是它的主要功能分解：  

   - 它匯入 `ast` 模組，該模組提供處理 Python 抽象語法樹的功能。  
   - 它將部署的實例類型設置為 "Standard_NC6s_v3"。  
   - 它檢查基礎模型中是否存在 `inference_compute_allow_list` 標籤。如果存在，則將標籤值從字符串轉換為 Python 列表，並將其賦值給 `inference_computes_allow_list`。如果不存在，則將 `inference_computes_allow_list` 設置為 None。  
   - 它檢查指定的實例類型是否在允許列表中。如果不在，則打印消息，要求用戶從允許列表中選擇實例類型。  
   - 它準備創建部署，通過創建一個 `ManagedOnlineDeployment` 物件，包含部署名稱、端點名稱、模型 ID、實例類型與數量、存活探測設置以及請求設置等參數。  
   - 它通過調用 `workspace_ml_client` 的 `begin_create_or_update` 方法，並將 `ManagedOnlineDeployment` 物件作為參數來創建部署。隨後，它通過調用 `wait` 方法等待創建操作完成。  
   - 它將端點的流量設置為 100% 導向到 "demo" 部署。  
   - 它通過調用 `workspace_ml_client` 的 `begin_create_or_update` 方法，並將端點物件作為參數來更新端點。隨後，它通過調用 `result` 方法等待更新操作完成。  

簡而言之，此腳本將一個註冊的機器學習模型部署到 Azure Machine Learning 中的管理線上端點。  
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

## 8. 使用測試數據測試端點

我們將從測試數據集中提取一些測試數據，並提交到線上端點進行推理。我們隨後將顯示得分標籤與真實標籤並排展示。  

### 讀取結果

1. 此 Python 腳本將 JSON Lines 文件讀取到 pandas DataFrame 中，隨機取樣並重置索引。以下是它的主要功能分解：  

   - 它將檔案 `./ultrachat_200k_dataset/test_gen.jsonl` 讀取到 pandas DataFrame 中。由於檔案是 JSON Lines 格式，每行都是一個單獨的 JSON 對象，因此使用 `read_json` 函數，並設置參數 `lines=True`。  
   - 它從 DataFrame 中隨機選取 1 行。使用 `sample` 函數，並設置參數 `n=1` 來指定選取的行數。  
   - 它重置 DataFrame 的索引。使用 `reset_index` 函數，並設置參數 `drop=True` 來丟棄原始索引並用默認整數值替換。  
   - 它使用 `head` 函數設置參數 2 來顯示 DataFrame 的前兩行。然而，由於取樣後 DataFrame 僅包含一行，因此只會顯示這一行。  

簡而言之，此腳本將 JSON Lines 文件讀取到 pandas DataFrame 中，隨機取樣 1 行，重置索引，並顯示第一行。  
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

### 創建 JSON 對象

1. 此 Python 腳本創建一個具有特定參數的 JSON 對象，並將其保存到文件中。以下是它的主要功能分解：  

   - 它匯入 `json` 模組，該模組提供處理 JSON 數據的功能。  
   - 它創建一個字典 `parameters`，包含機器學習模型的參數鍵值對。鍵包括 "temperature"、"top_p"、"do_sample" 和 "max_new_tokens"，對應的值分別為 0.6、0.9、True 和 200。  
   - 它創建另一個字典 `test_json`，包含兩個鍵："input_data" 和 "params"。其中，"input_data" 的值是一個字典，包含鍵 "input_string" 和 "parameters"。"input_string" 的值是一個列表，包含來自 `test_df` DataFrame 的第一條消息。"parameters" 的值是之前創建的 `parameters` 字典。"params" 的值則是一個空字典。  
   - 它打開一個名為 `sample_score.json` 的文件。  

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

1. 此 Python 腳本調用 Azure Machine Learning 的線上端點來對 JSON 文件進行推理。以下是它的主要功能分解：  

   - 它調用 `workspace_ml_client` 的 `online_endpoints` 屬性中的 `invoke` 方法。該方法用於向線上端點發送請求並獲取響應。  
   - 它通過參數 `endpoint_name` 和 `deployment_name` 指定端點和部署的名稱。在此情況下，端點名稱存儲在 `online_endpoint_name` 變數中，部署名稱為 "demo"。  
   - 它通過參數 `request_file` 指定需要推理的 JSON 文件的路徑。在此情況下，文件為 `./ultrachat_200k_dataset/sample_score.json`。  
   - 它將端點的響應存儲在變數 `response` 中。  
   - 它打印原始響應。  

簡而言之，此腳本調用 Azure Machine Learning 的線上端點對 JSON 文件進行推理，並打印響應。  
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

1. 別忘了刪除線上端點，否則端點使用的計算資源將持續計費。此行 Python 代碼用於刪除 Azure Machine Learning 中的線上端點。以下是它的主要功能分解：  

   - 它調用 `workspace_ml_client` 的 `online_endpoints` 屬性中的 `begin_delete` 方法。該方法用於開始刪除線上端點的操作。  
   - 它通過參數 `name` 指定需要刪除的端點名稱。在此情況下，端點名稱存儲在 `online_endpoint_name` 變數中。  
   - 它調用 `wait` 方法等待刪除操作完成。這是一個阻塞操作，意味著腳本在刪除完成之前將無法繼續執行。  

簡而言之，此行代碼用於開始刪除 Azure Machine Learning 中的線上端點，並等待操作完成。  
```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```  

**免責聲明**：  
本文件使用基於機器的人工智能翻譯服務進行翻譯。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文文件作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或誤讀不承擔責任。