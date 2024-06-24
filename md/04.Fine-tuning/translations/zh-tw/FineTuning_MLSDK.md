## 如何使用 Azure ML 系統註冊表中的聊天完成元件來微調模型

在這個範例中，我們將對 Phi-3-mini-4k-instruct 模型進行微調，以使用 ultrachat_200k 資料集完成兩個人之間的對話。

![MLFineTune](../../../../imgs/04/03/MLFineTune.png)

範例將向您展示如何使用 Azure ML SDK 和 Python 進行微調，然後將微調後的模型部署到線上端點以進行即時推論。

### 訓練資料

我們將使用 ultrachat_200k 資料集。這是 UltraChat 資料集的經過大量過濾的版本，用於訓練 Zephyr-7B-β，這是一個最先進的 7B 聊天模型。

### 模型

我們將使用 Phi-3-mini-4k-instruct 模型來展示使用者如何微調模型以完成聊天任務。如果你是從特定模型卡片打開這個筆記本，請記得替換特定的模型名稱。

### 任務

- 選擇一個模型進行微調。
- 選擇並探索訓練資料。
- 配置微調任務。
- 執行微調任務。
- 審查訓練和評估指標。
- 註冊微調後的模型。
- 部署微調後的模型以進行實時推論。
- 清理資源。

## 1. 設定前置條件

- 安裝相依套件
- 連接到 AzureML Workspace。了解更多在設定 SDK 認證。替換 <WORKSPACE_NAME>、<RESOURCE_GROUP> 和 <SUBSCRIPTION_ID>。
- 連接到 azureml 系統註冊表
- 設定一個可選的實驗名稱
- 檢查或建立運算。

單個 GPU 節點可以有多個 GPU 卡的需求。例如，在一個 Standard_NC24rs_v3 節點中有 4 個 NVIDIA V100 GPUs，而在 Standard_NC12s_v3 中有 2 個 NVIDIA V100 GPUs。請參考文件以獲取此資訊。每個節點的 GPU 卡數量在下面的參數 gpus_per_node 中設定。正確設定此值將確保節點中所有 GPU 的利用率。推薦的 GPU 計算 SKUs 可以在[這裡](https://example.com)和[這裡](https://example.com)找到。

### Python 函式庫

安裝相依套件，方法是執行以下單元。如果在新環境中執行，這不是可選步驟。

```
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### 與 Azure ML 互動

這個 Python 程式碼用於與 Azure 機器學習（Azure ML）服務互動。以下是它的功能分解：

它從 azure.ai.ml、azure.identity 和 azure.ai.ml.entities 套件匯入必要的模組。它還匯入了 time 模組。

它嘗試使用 DefaultAzureCredential() 進行身份驗證，這提供了一個簡化的身份驗證體驗，以便快速開始開發在 Azure 雲端中執行的應用程式。如果這失敗，它會退回到 InteractiveBrowserCredential()，這提供了一個互動式的登入提示。

然後，它嘗試使用 from_config 方法來建立一個 MLClient 實例，該方法從預設的配置檔案（config.json）中讀取配置。如果這失敗，它會通過手動提供 subscription_id、resource_group_name 和 workspace_name 來建立一個 MLClient 實例。

它建立了另一個 MLClient 實例，這次是為名為 "azureml" 的 Azure ML 註冊表。這個註冊表是存儲模型、微調管道和環境的地方。

它將 experiment_name 設定為 "chat_completion_Phi-3-mini-4k-instruct"。

它通過將當前時間（自紀元以來的秒數，作為浮點數）轉換為整數，然後轉換為字串來生成唯一的時間戳。此時間戳可用於建立唯一的名稱和版本。

```
# 從 Azure ML 和 Azure Identity 匯入必要的模組
from azure.ai.ml import MLClient
from azure.identity import (
    DefaultAzureCredential,
    InteractiveBrowserCredential,
)
from azure.ai.ml.entities import AmlCompute
import time  # 匯入 time 模組

# 嘗試使用 DefaultAzureCredential 進行驗證
try:
    credential = DefaultAzureCredential()
    credential.get_token("https://management.azure.com/.default")
except Exception as ex:  # 如果 DefaultAzureCredential 失敗，使用 InteractiveBrowserCredential
    credential = InteractiveBrowserCredential()

# 嘗試使用預設配置檔案建立一個 MLClient 實例
try:
    workspace_ml_client = MLClient.from_config(credential=credential)
except:  # 如果失敗，通過手動提供詳細資訊來建立一個 MLClient 實例
    workspace_ml_client = MLClient(
        credential,
        subscription_id="<SUBSCRIPTION_ID>",
        resource_group_name="<RESOURCE_GROUP>",
        workspace_name="<WORKSPACE_NAME>",
    )

# 為名為 "azureml" 的 Azure ML registry 建立另一個 MLClient 實例
# 這個 registry 是存儲模型、微調管道和環境的地方
registry_ml_client = MLClient(credential, registry_name="azureml")

# 設定實驗名稱
experiment_name = "chat_completion_Phi-3-mini-4k-instruct"

# 生成一個唯一的時間戳，可用於需要唯一名稱和版本的地方
timestamp = str(int(time.time()))
```

## 2. 選擇一個基礎模型進行微調

Phi-3-mini-4k-instruct 是一個 3.8B 參數的輕量級、先進的開放模型，基於 Phi-2 使用的數據集構建。該模型屬於 Phi-3 模型家族，Mini 版本有兩個變體 4K 和 128K，這是它可以支持的上下文長度（以 tokens 計算），我們需要為我們的特定目的微調該模型以便使用。你可以在 AzureML Studio 的 Model Catalog 中瀏覽這些模型，按 chat-completion 任務進行篩選。在這個範例中，我們使用 Phi-3-mini-4k-instruct 模型。如果你為不同的模型打開了這個 notebook，請相應地更換模型名稱和版本。

請注意模型的 model id 屬性。這將作為輸入傳遞給微調工作。在 AzureML Studio Model Catalog 的模型詳細資訊頁面中，這也可作為 Asset ID 欄位使用。

這個 Python 程式碼正在與 Azure Machine Learning (Azure ML) 服務互動。以下是它的作用分解：

它將 model_name 設定為 "Phi-3-mini-4k-instruct"。

它使用 registry_ml_client 物件的 models 屬性的 get 方法從 Azure ML 註冊表中檢索具有指定名稱的模型的最新版本。get 方法被呼叫時帶有兩個參數：模型的名稱和一個標籤，指定應檢索模型的最新版本。

它會在控制台上列印一條訊息，指示將用於微調的模型的名稱、版本和 ID。字串的 format 方法被用來將模型的名稱、版本和 ID 插入訊息中。模型的名稱、版本和 ID 作為 foundation_model 物件的屬性來訪問。

```
# 設定模型名稱
model_name = "Phi-3-mini-4k-instruct"

# 從 Azure ML 註冊表中獲取最新版本的模型
foundation_model = registry_ml_client.models.get(model_name, label="latest")

# 列印模型名稱、版本和 id
# 這些資訊對於追蹤和除錯很有用
print(
    "\n\n使用模型名稱: {0}, 版本: {1}, id: {2} 進行微調".format(
        foundation_model.name, foundation_model.version, foundation_model.id
    )
)
```

## 3. 建立一個計算來與這個工作一起使用

微調工作僅適用於 GPU 計算。計算的大小取決於模型的大小，在大多數情況下，識別適合工作的計算變得棘手。在此單元中，我們指導使用者選擇適合工作的計算。

**注意1** 下列計算機在最優化配置下工作。任何對配置的更改可能會導致 Cuda 記憶體不足錯誤。在這種情況下，請嘗試將計算機升級到更大的計算機尺寸。

**NOTE2** 在選擇下面的 compute_cluster_size 時，請確保計算資源在您的資源群組中可用。如果某個特定的計算資源不可用，您可以請求獲取該計算資源的訪問權限。

### 檢查模型是否支援微調

這個 Python 程式碼正在與 Azure Machine Learning (Azure ML) 模型互動。以下是它的功能分解:

它匯入了 ast 模組，該模組提供處理 Python 抽象語法樹的函式。

它檢查 foundation_model 物件 (代表 Azure ML 中的一個模型) 是否有一個名為 finetune_compute_allow_list 的標籤。Azure ML 中的標籤是可以建立並用來篩選和排序模型的鍵值對。

如果 finetune_compute_allow_list 標籤存在，它會使用 ast.literal_eval 函式來安全地解析標籤的值（字串）為 Python 清單。然後將此清單分配給 computes_allow_list 變數。接著，它會打印一條訊息，指示應從清單中建立一個計算。

如果 finetune_compute_allow_list 標籤不存在，則將 computes_allow_list 設為 None，並顯示一條訊息，指出 finetune_compute_allow_list 標籤不是模型標籤的一部分。

總結來說，這段程式碼正在檢查模型的 Metadata 中的特定標籤，將標籤的值轉換為列表（如果存在的話），並相應地向用戶提供反饋。

```
# 匯入 ast 模組, 提供處理 Python 抽象語法樹的函式
import ast

# 檢查 'finetune_compute_allow_list' 標籤是否存在於模型的標籤中
if "finetune_compute_allow_list" in foundation_model.tags:
    # 如果標籤存在, 使用 ast.literal_eval 安全地將標籤的值（字串）解析成 Python 列表
    computes_allow_list = ast.literal_eval(
        foundation_model.tags["finetune_compute_allow_list"]
    )  # 將字串轉換為 python 列表
    # 列印訊息, 指示應從列表中建立計算
    print(f"Please create a compute from the above list - {computes_allow_list}")
else:
    # 如果標籤不存在, 將 computes_allow_list 設為 None
    computes_allow_list = None
    # 列印訊息, 指示 'finetune_compute_allow_list' 標籤不在模型的標籤中
    print("`finetune_compute_allow_list` is not part of model tags")
```

### 檢查 Compute Instance

這個 Python 程式碼正在與 Azure Machine Learning (Azure ML) 服務互動，並對計算實例執行多項檢查。以下是它的功能分解：

它嘗試從 Azure ML 工作區中檢索存儲在 compute_cluster 中的計算實例。如果計算實例的佈建狀態為 "failed"，則引發 ValueError。

它會檢查 computes_allow_list 是否不為 None。如果不是，它會將列表中的所有計算大小轉換為小寫，並檢查當前計算實例的大小是否在列表中。如果不是，它會引發 ValueError。

如果 computes_allow_list 為 None，則檢查計算實例的大小是否在不支援的 GPU VM 大小列表中。如果是，則引發 ValueError。

它檢索工作區中所有可用計算大小的列表。然後遍歷此列表，並對每個計算大小檢查其名稱是否與當前計算實例的大小匹配。如果匹配，它會檢索該計算大小的 GPU 數量並將 gpu_count_found 設置為 True。

如果 gpu_count_found 為 True，則會列印計算實例中的 GPU 數量。如果 gpu_count_found 為 False，則會引發 ValueError。

總結來說，此腳本正在對 Azure ML 工作區中的一個計算實例執行多項檢查，包括檢查其佈建狀態、其大小是否在允許列表或拒絕列表中，以及其擁有的 GPU 數量。

```
# 列印例外訊息
print(e)
# 如果工作區中沒有可用的計算大小，則引發 ValueError
raise ValueError(
    f"警告！計算大小 {compute_cluster_size} 在工作區中不可用"
)

# 從 Azure ML 工作區中檢索計算實例
compute = workspace_ml_client.compute.get(compute_cluster)
# 檢查計算實例的配置狀態是否為 "failed"
if compute.provisioning_state.lower() == "failed":
    # 如果配置狀態為 "failed"，則引發 ValueError
    raise ValueError(
        f"配置失敗，計算 '{compute_cluster}' 處於失敗狀態。"
        f"請嘗試建立不同的計算"
    )

# 檢查 computes_allow_list 是否不為 None
if computes_allow_list is not None:
    # 將 computes_allow_list 中的所有計算大小轉換為小寫
    computes_allow_list_lower_case = [x.lower() for x in computes_allow_list]
    # 檢查計算實例的大小是否在 computes_allow_list_lower_case 中
    if compute.size.lower() not in computes_allow_list_lower_case:
        # 如果計算實例的大小不在 computes_allow_list_lower_case 中，則引發 ValueError
        raise ValueError(
            f"VM 大小 {compute.size} 不在允許微調的計算列表中"
        )
else:
    # 定義不支援的 GPU VM 大小列表
    unsupported_gpu_vm_list = [
        "standard_nc6",
        "standard_nc12",
        "standard_nc24",
        "standard_nc24r",
    ]
    # 檢查計算實例的大小是否在 unsupported_gpu_vm_list 中
    if compute.size.lower() in unsupported_gpu_vm_list:
        # 如果計算實例的大小在 unsupported_gpu_vm_list 中，則引發 ValueError
        raise ValueError(
            f"VM 大小 {compute.size} 目前不支援微調"
        )

# 初始化一個標誌以檢查是否已找到計算實例中的 GPU 數量
gpu_count_found = False
# 檢索工作區中所有可用計算大小的列表
workspace_compute_sku_list = workspace_ml_client.compute.list_sizes()
available_sku_sizes = []
# 遍歷可用計算大小的列表
for compute_sku in workspace_compute_sku_list:
    available_sku_sizes.append(compute_sku.name)
    # 檢查計算大小的名稱是否與計算實例的大小匹配
    if compute_sku.name.lower() == compute.size.lower():
        # 如果匹配，則檢索該計算大小的 GPU 數量並將 gpu_count_found 設置為 True
        gpus_per_node = compute_sku.gpus
        gpu_count_found = True
# 如果 gpu_count_found 為 True，則列印計算實例中的 GPU 數量
if gpu_count_found:
    print(f"計算 {compute.size} 中的 GPU 數量: {gpus_per_node}")
else:
    # 如果 gpu_count_found 為 False，則引發 ValueError
    raise ValueError(
        f"未找到計算 {compute.size} 中的 GPU 數量。可用的 skus 是: {available_sku_sizes}。"
        f"這不應該發生。請檢查選定的計算叢集: {compute_cluster} 並重試。"
    )
```

## 4. 選擇資料集以微調模型

我們使用 ultrachat_200k 數據集。該數據集有四個分割，適用於:

監督微調 (sft)。
生成排名 (gen)。每個分割的範例數量如下所示:
train_sft	test_sft	train_gen	test_gen
207865	23110	256032	28304
接下來的幾個單元顯示了微調的基本資料準備:

視覺化一些資料列
我們希望這個範例能夠快速執行，所以保存包含已經修剪過的 5% 資料列的 train_sft 和 test_sft 檔案。這意味著微調過的模型將具有較低的準確性，因此不應用於實際應用中。
download-dataset.py 用於下載 ultrachat_200k 資料集並將資料集轉換為微調管道元件可消耗的格式。由於資料集很大，因此我們這裡只有部分資料集。

執行以下腳本僅下載 5% 的資料。這可以通過將 dataset_split_pc 參數更改為所需的百分比來增加。

**注意:** 一些語言模型有不同的語言程式碼，因此資料集中的欄位名稱應該反映相同的情況。

這是一個資料應該如何顯示的範例
聊天完成資料集以 parquet 格式儲存，每個條目使用以下結構:

這是一個 JSON (JavaScript 物件表示法) 文件，它是一種流行的資料交換格式。它不是可執行的程式碼，而是一種儲存和傳輸資料的方式。以下是其結構的分解：

"prompt": 此鍵包含一個字串值，代表對 AI 助手提出的任務或問題。

"messages": 此鍵保存一個物件陣列。每個物件代表使用者和 AI 助手之間對話中的一則訊息。每個訊息物件有兩個鍵:

"content": 此鍵持有一個字串值，表示訊息的內容。
"role": 此鍵持有一個字串值，表示發送訊息的實體角色。它可以是 "user" 或 "assistant"。
"prompt_id": 此鍵持有一個字串值，表示提示的唯一標識符。

在這個特定的 JSON 文件中，對話顯示一位使用者要求 AI 助手建立一個反烏托邦故事的主角。助手回應後，使用者要求更多資訊。助手同意提供更多資訊。整個對話與一個特定的提示 ID 相關聯。

```
{
    // 提給 AI 助理的任務或問題
    "prompt": "建立一個完整發展的主角，她在暴君統治下的反烏托邦社會中面臨生存挑戰。 ...",

    // 一個物件陣列，每個物件代表使用者和 AI 助理之間對話中的一條訊息
    "messages":[
        {
            // 使用者訊息的內容
            "content": "建立一個完整發展的主角，她在暴君統治下的反烏托邦社會中面臨生存挑戰。 ...",
            // 發送訊息的實體角色
            "role": "user"
        },
        {
            // 助理訊息的內容
            "content": "名字: Ava\n\n Ava 在她16歲時，世界如她所知的那樣崩潰了。政府倒台，留下了一個混亂且無法無天的社會。 ...",
            // 發送訊息的實體角色
            "role": "assistant"
        },
        {
            // 使用者訊息的內容
            "content": "哇，Ava 的故事如此激烈且鼓舞人心！你能給我更多的細節嗎。 ...",
            // 發送訊息的實體角色
            "role": "user"
        },
        {
            // 助理訊息的內容
            "content": "當然可以！ ....",
            // 發送訊息的實體角色
            "role": "assistant"
        }
    ],

    // 提示的唯一標識符
    "prompt_id": "d938b65dfe31f05f80eb8572964c6673eddbd68eff3db6bd234d7f1e3b86c2af"
}
```

### 下載資料

這個 Python 程式碼用來使用名為 download-dataset.py 的輔助程式碼下載一個數據集。以下是它的功能分解：

它匯入了 os 模組，這提供了一種使用作業系統相依功能的可移植方式。

它使用 os.system 函式在 shell 中執行 download-dataset.py 腳本，並帶有特定的命令列參數。這些參數指定要下載的資料集 (HuggingFaceH4/ultrachat_200k)、下載目錄 (ultrachat_200k_dataset) 和要分割的資料集百分比 (5)。os.system 函式返回它所執行命令的退出狀態；此狀態存儲在 exit_status 變數中。

它檢查 exit_status 是否不為 0。在類 Unix 作業系統中，exit_status 為 0 通常表示命令成功，而任何其他數字表示錯誤。如果 exit_status 不為 0，它會引發一個 Exception，並顯示一條訊息，指出下載數據集時發生錯誤。

總結來說，這個腳本正在執行一個命令來使用輔助腳本下載資料集，如果命令失敗則會引發異常。

```
# 匯入 os 模組，提供使用作業系統相關功能的方法
import os

# 使用 os.system 函式在 shell 中執行 download-dataset.py 腳本，並帶有特定的命令列參數
# 參數指定要下載的資料集 (HuggingFaceH4/ultrachat_200k)、下載的目錄 (ultrachat_200k_dataset)，以及要分割的資料集百分比 (5)
# os.system 函式返回它執行的命令的退出狀態；此狀態存儲在 exit_status 變數中
exit_status = os.system(
    "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
)

# 檢查 exit_status 是否不為 0
# 在類 Unix 作業系統中，退出狀態為 0 通常表示命令成功，而任何其他數字表示錯誤
# 如果 exit_status 不為 0，則引發一個異常，並顯示一條消息，指示下載資料集時出現錯誤
if exit_status != 0:
    raise Exception("下載資料集時出現錯誤")
```

### 將資料載入 DataFrame

這個 Python 程式碼正在將一個 JSON Lines 文件載入 pandas DataFrame 並顯示前 5 行。以下是它的功能分解：

它匯入了 pandas 函式庫，這是一個強大的資料操作和分析函式庫。

它將 pandas 的顯示選項的最大列寬設置為 0。這意味著當 DataFrame 被列印時，每列的完整文本將顯示而不會被截斷。

它使用 pd.read_json 函式從 ultrachat_200k_dataset 目錄中載入 train_sft.jsonl 檔案到 DataFrame。lines=True 參數表示檔案是 JSON Lines 格式，其中每一行都是一個獨立的 JSON 物件。

它使用 head 方法顯示 DataFrame 的前 5 行。如果 DataFrame 少於 5 行，它將顯示所有行。

總結來說，這個程式碼正在將一個 JSON Lines 文件載入到一個 DataFrame 並顯示前 5 行的完整欄位文字。

```
# 匯入 pandas 函式庫，它是一個強大的資料操作和分析函式庫
import pandas as pd

# 將 pandas 的顯示選項中的最大欄寬設定為 0
# 這意味著當 DataFrame 被列印時，每一欄的全文都會顯示而不會被截斷
pd.set_option("display.max_colwidth", 0)

# 使用 pd.read_json 函式從 ultrachat_200k_dataset 目錄中載入 train_sft.jsonl 檔案到 DataFrame
# lines=True 參數表示檔案是 JSON Lines 格式，其中每一行是一個獨立的 JSON 物件
df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)

# 使用 head 方法顯示 DataFrame 的前 5 行
# 如果 DataFrame 少於 5 行，它將顯示所有行
df.head()
```

## 5. 使用模型和資料作為輸入提交微調工作

建立使用聊天完成管道元件的工作。了解更多關於微調所支持的所有參數。

### 定義微調參數

微調參數可以分為兩類 - 訓練參數, 優化參數

訓練參數定義了訓練方面，例如 -

- 優化器、調度器的使用
- 優化微調的指標
- 訓練步驟數量和批次大小等
- 優化參數有助於優化 GPU 記憶體並有效利用計算資源。

以下是屬於此類別的一些參數。優化參數因每個模型而異，並與模型一起打包以處理這些變化。

- 啟用 deepspeed 和 LoRA
- 啟用混合精度訓練
- 啟用多節點訓練

**注意：** 監督微調可能會導致失去對齊或災難性遺忘。我們建議在微調後檢查此問題並執行對齊階段。

### 微調參數

這個 Python 程式碼正在設定參數以微調機器學習模型。以下是它的作用分解：

它設定了預設的訓練參數，例如訓練週期數、訓練和評估的批次大小、學習率和學習率調度器類型。

它設定了預設的優化參數，例如是否應用 Layer-wise Relevance Propagation (LoRa) 和 DeepSpeed，以及 DeepSpeed 階段。

它將訓練和優化參數結合到一個稱為 finetune_parameters 的單一字典中。

它檢查 foundation_model 是否有任何模型特定的預設參數。如果有，它會打印一條警告訊息並使用這些模型特定的預設值更新 finetune_parameters 字典。ast.literal_eval 函式被用來將模型特定的預設值從字串轉換為 Python 字典。

它會列印將用於執行的最終微調參數集。

總結來說，這個程式碼正在設定並顯示用於微調機器學習模型的參數，並且可以用特定模型的參數來覆蓋預設參數。

```
# 設定預設訓練參數，例如訓練週期數、訓練和評估的批次大小、學習率和學習率調度器類型
training_parameters = dict(
    num_train_epochs=3,
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    learning_rate=5e-6,
    lr_scheduler_type="cosine",
)

# 設定預設優化參數，例如是否應用層級相關傳播（LoRa）和 DeepSpeed，以及 DeepSpeed 階段
optimization_parameters = dict(
    apply_lora="true",
    apply_deepspeed="true",
    deepspeed_stage=2,
)

# 將訓練和優化參數合併為一個名為 finetune_parameters 的字典
finetune_parameters = {**training_parameters, **optimization_parameters}

# 檢查 foundation_model 是否有任何模型特定的預設參數
# 如果有，則打印警告訊息並使用這些模型特定的預設值更新 finetune_parameters 字典
# ast.literal_eval 函式用於將模型特定的預設值從字串轉換為 Python 字典
if "model_specific_defaults" in foundation_model.tags:
    print("Warning! Model specific defaults exist. The defaults could be overridden.")
    finetune_parameters.update(
        ast.literal_eval(  # 將字串轉換為 python 字典
            foundation_model.tags["model_specific_defaults"]
        )
    )

# 打印將用於執行的最終微調參數集
print(
    f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
)
```

### 訓練管道

這個 Python 程式碼定義了一個函式來產生機器學習訓練管道的顯示名稱，然後呼叫這個函式來生成並列印顯示名稱。以下是它的功能分解：

get_pipeline_display_name 函式已定義。此函式根據與訓練管道相關的各種參數生成顯示名稱。

在函式內，它通過將每個設備的批次大小、梯度累積步驟的數量、每個節點的 GPU 數量和用於微調的節點數量相乘來計算總批次大小。

它檢索各種其他參數，例如學習率調度器類型、是否應用 DeepSpeed、DeepSpeed 階段、是否應用層級相關性傳播 (LoRa)、保留的模型檢查點數量限制以及最大序列長度。

它構建了一個包含所有這些參數的字串，並以連字符分隔。如果應用了 DeepSpeed 或 LoRa，則字串分別包含 "ds" 後跟 DeepSpeed 階段，或 "lora"。如果沒有，則分別包含 "nods" 或 "nolora"。

函式返回此字串，作為訓練管道的顯示名稱。

函式定義後，會呼叫它來產生顯示名稱，然後列印出來。

總結來說，這段程式碼是根據各種參數生成機器學習訓練管道的顯示名稱，然後打印這個顯示名稱。

```
# 定義一個函式來生成訓練管道的顯示名稱
def get_pipeline_display_name():
    # 通過將每個設備的批次大小、梯度累積步數、每個節點的 GPU 數量和用於微調的節點數量相乘來計算總批次大小
    batch_size = (
        int(finetune_parameters.get("per_device_train_batch_size", 1))
        * int(finetune_parameters.get("gradient_accumulation_steps", 1))
        * int(gpus_per_node)
        * int(finetune_parameters.get("num_nodes_finetune", 1))
    )
    # 獲取學習率調度器類型
    scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
    # 獲取是否應用了 DeepSpeed
    deepspeed = finetune_parameters.get("apply_deepspeed", "false")
    # 獲取 DeepSpeed 階段
    ds_stage = finetune_parameters.get("deepspeed_stage", "2")
    # 如果應用了 DeepSpeed，則在顯示名稱中包含 "ds" 和 DeepSpeed 階段；如果沒有，則包含 "nods"
    if deepspeed == "true":
        ds_string = f"ds{ds_stage}"
    else:
        ds_string = "nods"
    # 獲取是否應用了層次相關傳播（LoRa）
    lora = finetune_parameters.get("apply_lora", "false")
    # 如果應用了 LoRa，則在顯示名稱中包含 "lora"；如果沒有，則包含 "nolora"
    if lora == "true":
        lora_string = "lora"
    else:
        lora_string = "nolora"
    # 獲取要保留的模型檢查點數量限制
    save_limit = finetune_parameters.get("save_total_limit", -1)
    # 獲取最大序列長度
    seq_len = finetune_parameters.get("max_seq_length", -1)
    # 通過連接所有這些參數並用連字符分隔來構建顯示名稱
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

# 呼叫函式來生成顯示名稱
pipeline_display_name = get_pipeline_display_name()
# 列印顯示名稱
print(f"Display name used for the run: {pipeline_display_name}")
```

### 設定 Pipeline

這個 Python 程式碼正在使用 Azure Machine Learning SDK 定義和配置一個機器學習流水線。以下是它的作用分解：

1. 它從 Azure AI ML SDK 匯入必要的模組。

2. 它從註冊表中獲取名為 "chat_completion_pipeline" 的管道元件。

3. 它使用 `@pipeline` 裝飾器和函式 `create_pipeline` 定義一個管道作業。管道的名稱設置為 `pipeline_display_name`。

4. 在 `create_pipeline` 函式內，它初始化了獲取的管道元件，並設置了各種參數，包括模型路徑、不同階段的計算叢集、訓練和測試的數據集拆分、用於微調的 GPU 數量和其他微調參數。

5. 它將微調作業的輸出映射到管道作業的輸出。這樣做是為了使微調後的模型能夠輕鬆註冊，這是將模型部署到在線或批次端點所必需的。

6. 它通過呼叫 `create_pipeline` 函式來建立管道的實例。

7. 它將管道的 `force_rerun` 設定設置為 `True`，這意味著不會使用先前作業的快取結果。

8. 它將管道的 `continue_on_step_failure` 設定設置為 `False`，這意味著如果任何步驟失敗，管道將停止。

總結來說，這個腳本正在使用 Azure 機器學習 SDK 定義和配置一個聊天完成任務的機器學習管道。

```
# 從 Azure AI ML SDK 匯入必要的模組
from azure.ai.ml.dsl import pipeline
from azure.ai.ml import Input

# 從註冊表中獲取名為 "chat_completion_pipeline" 的 pipeline 元件
pipeline_component_func = registry_ml_client.components.get(
    name="chat_completion_pipeline", label="latest"
)

# 使用 @pipeline 裝飾器和函式 create_pipeline 定義 pipeline 作業
# pipeline 的名稱設置為 pipeline_display_name
@pipeline(name=pipeline_display_name)
def create_pipeline():
    # 使用各種參數初始化獲取的 pipeline 元件
    # 這些參數包括模型路徑、不同階段的計算叢集、訓練和測試的數據集拆分、用於微調的 GPU 數量以及其他微調參數
    chat_completion_pipeline = pipeline_component_func(
        mlflow_model_path=foundation_model.id,
        compute_model_import=compute_cluster,
        compute_preprocess=compute_cluster,
        compute_finetune=compute_cluster,
        compute_model_evaluation=compute_cluster,
        # 將數據集拆分映射到參數
        train_file_path=Input(
            type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
        ),
        test_file_path=Input(
            type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
        ),
        # 訓練設置
        number_of_gpu_to_use_finetuning=gpus_per_node,  # 設置為計算中可用的 GPU 數量
        **finetune_parameters
    )
    return {
        # 將微調作業的輸出映射到 pipeline 作業的輸出
        # 這樣我們可以輕鬆註冊微調後的模型
        # 註冊模型是將模型部署到在線或批次端點所必需的
        "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
    }

# 通過調用 create_pipeline 函式創建 pipeline 實例
pipeline_object = create_pipeline()

# 不使用先前作業的緩存結果
pipeline_object.settings.force_rerun = True

# 設置步驟失敗時繼續執行為 False
# 這意味著如果任何步驟失敗，pipeline 將停止
pipeline_object.settings.continue_on_step_failure = False
```

### 提交工作

這個 Python 程式碼正在向 Azure Machine Learning 工作區提交一個機器學習管道工作，然後等待工作完成。以下是它的作用分解：

它呼叫 workspace_ml_client 中 jobs 物件的 create_or_update 方法來提交管線工作。要執行的管線由 pipeline_object 指定，執行工作的實驗由 experiment_name 指定。

然後，它會呼叫 workspace_ml_client 中 jobs 物件的 stream 方法來等待管道工作完成。要等待的工作由 pipeline_job 物件的 name 屬性指定。

總結來說，這個腳本正在提交一個機器學習管道工作到 Azure 機器學習工作區，然後等待工作完成。

```
# 提交管道作業到 Azure 機器學習工作區
# 要執行的管道由 pipeline_object 指定
# 作業執行的實驗由 experiment_name 指定
pipeline_job = workspace_ml_client.jobs.create_or_update(
    pipeline_object, experiment_name=experiment_name
)

# 等待管道作業完成
# 要等待的作業由 pipeline_job 物件的 name 屬性指定
workspace_ml_client.jobs.stream(pipeline_job.name)
```

## 6. 在工作區中註冊微調模型

我們將從微調工作的輸出中註冊模型。這將追蹤微調模型和微調工作之間的關聯。微調工作進一步追蹤到基礎模型、數據和訓練程式碼的關聯。

### 註冊 ML 模型

這個 Python 程式碼正在註冊一個在 Azure Machine Learning 管道中訓練的機器學習模型。以下是它的功能分解:

它從 Azure AI ML SDK 匯入必要的模組。

它透過呼叫 workspace_ml_client 中 jobs 物件的 get 方法並存取其 outputs 屬性來檢查 pipeline 作業是否有可用的 trained_model 輸出。

它通過使用管道作業的名稱和輸出（"trained_model"）的名稱來格式化字串，構建通向訓練模型的路徑。

它通過將 "-ultrachat-200k" 附加到原始模型名稱並將任何斜杠替換為連字符來定義微調模型的名稱。

它準備透過建立一個 Model 物件來註冊模型，包含各種參數，包括模型的路徑、模型的類型（MLflow 模型）、模型的名稱和版本，以及模型的描述。

它透過呼叫 workspace_ml_client 中 models 物件的 create_or_update 方法，並以 Model 物件作為參數來註冊模型。

它會列印已註冊的模型。

總結來說，這個腳本正在註冊一個在 Azure 機器學習管道中訓練的機器學習模型。

```
# 從 Azure AI ML SDK 匯入必要的模組
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes

# 檢查 `trained_model` 輸出是否可從 pipeline job 取得
print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)

# 透過格式化字串來構建訓練模型的路徑，包含 pipeline job 的名稱和輸出名稱 ("trained_model")
model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
    pipeline_job.name, "trained_model"
)

# 定義微調模型的名稱，透過在原始模型名稱後附加 "-ultrachat-200k" 並將任何斜線替換為連字符
finetuned_model_name = model_name + "-ultrachat-200k"
finetuned_model_name = finetuned_model_name.replace("/", "-")

print("path to register model: ", model_path_from_job)

# 準備註冊模型，透過建立一個 Model 物件並設定各種參數
# 包括模型的路徑、模型的類型（MLflow 模型）、模型的名稱和版本，以及模型的描述
prepare_to_register_model = Model(
    path=model_path_from_job,
    type=AssetTypes.MLFLOW_MODEL,
    name=finetuned_model_name,
    version=timestamp,  # 使用時間戳作為版本以避免版本衝突
    description=model_name + " fine tuned model for ultrachat 200k chat-completion",
)

print("prepare to register model: \n", prepare_to_register_model)

# 透過呼叫 workspace_ml_client 中 models 物件的 create_or_update 方法並傳入 Model 物件作為參數來註冊模型
registered_model = workspace_ml_client.models.create_or_update(
    prepare_to_register_model
)

# 列印已註冊的模型
print("registered model: \n", registered_model)
```

## 7. 部署微調模型到線上端點

線上端點提供一個持久的 REST API，可以用來整合需要使用模型的應用程式。

### 管理端點

這個 Python 程式碼正在 Azure Machine Learning 中為註冊模型建立一個受管理的在線端點。以下是它的功能分解:

它從 Azure AI ML SDK 匯入必要的模組。

它通過在字串 "ultrachat-completion-" 後附加時間戳來定義線上端點的唯一名稱。

它準備透過建立一個 ManagedOnlineEndpoint 物件來建立線上端點，該物件包含各種參數，包括端點的名稱、端點的描述和驗證模式（"key"）。

它通過呼叫 workspace_ml_client 的 begin_create_or_update 方法並以 ManagedOnlineEndpoint 物件作為參數來建立線上端點。然後通過呼叫 wait 方法等待建立操作完成。

總結來說，此程式碼正在 Azure Machine Learning 中為已註冊的模型建立一個受管理的線上端點。

```
# 從 Azure AI ML SDK 匯入必要的模組
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    ProbeSettings,
    OnlineRequestSettings,
)

# 定義一個唯一的線上端點名稱，通過在字串 "ultrachat-completion-" 後附加一個時間戳
online_endpoint_name = "ultrachat-completion-" + timestamp

# 準備建立線上端點，通過建立一個帶有各種參數的 ManagedOnlineEndpoint 物件
# 這些參數包括端點的名稱、端點的描述和認證模式（"key"）
endpoint = ManagedOnlineEndpoint(
    name=online_endpoint_name,
    description="Online endpoint for "
    + registered_model.name
    + ", fine tuned model for ultrachat-200k-chat-completion",
    auth_mode="key",
)

# 通過呼叫 workspace_ml_client 的 begin_create_or_update 方法並以 ManagedOnlineEndpoint 物件作為參數來建立線上端點
# 然後通過呼叫 wait 方法等待建立操作完成
workspace_ml_client.begin_create_or_update(endpoint).wait()
```

您可以在此處找到支援部署的 SKU 清單 - [Managed online endpoints SKU list](https://learn.microsoft.com/en-us/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### 部署 ML 模型

這個 Python 程式碼正在將註冊的機器學習模型部署到 Azure Machine Learning 中的受管理線上端點。以下是它的作用分解：

它匯入了 ast 模組，該模組提供了處理 Python 抽象語法樹的函式。

它將部署的實例類型設置為 "Standard_NC6s_v3"。

它檢查 foundation model 中是否存在 inference_compute_allow_list 標籤。如果存在，則將標籤值從字串轉換為 Python 清單並賦值給 inference_computes_allow_list。如果不存在，則將 inference_computes_allow_list 設置為 None。

它檢查指定的實例類型是否在允許清單中。如果不在，它會打印一條訊息，要求使用者從允許清單中選擇一個實例類型。

它準備透過建立一個帶有各種參數的 ManagedOnlineDeployment 物件來創建部署，包括部署的名稱、端點的名稱、模型的 ID、實例類型和數量、活性探測設置以及請求設置。

它通過呼叫 workspace_ml_client 的 begin_create_or_update 方法並以 ManagedOnlineDeployment 物件作為參數來建立部署。然後通過呼叫 wait 方法等待建立操作完成。

它將端點的流量設置為將 100% 的流量直接導向 "展示" 部署。

它透過呼叫 workspace_ml_client 的 begin_create_or_update 方法並將 endpoint 物件作為參數來更新 endpoint。然後透過呼叫 result 方法等待更新操作完成。

總結來說，這個腳本正在將一個註冊的機器學習模型部署到 Azure 機器學習中的受管理線上端點。

```
# 匯入 ast 模組，該模組提供處理 Python 抽象語法樹的函式
import ast

# 設定部署的實例類型
instance_type = "Standard_NC6s_v3"

# 檢查 foundation model 中是否存在 `inference_compute_allow_list` 標籤
if "inference_compute_allow_list" in foundation_model.tags:
    # 如果存在，將標籤值從字串轉換為 Python 清單並賦值給 `inference_computes_allow_list`
    inference_computes_allow_list = ast.literal_eval(
        foundation_model.tags["inference_compute_allow_list"]
    )
    print(f"Please create a compute from the above list - {computes_allow_list}")
else:
    # 如果不存在，將 `inference_computes_allow_list` 設為 `None`
    inference_computes_allow_list = None
    print("`inference_compute_allow_list` is not part of model tags")

# 檢查指定的實例類型是否在允許清單中
if (
    inference_computes_allow_list is not None
    and instance_type not in inference_computes_allow_list
):
    print(
        f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
    )

# 準備建立部署，通過建立一個帶有各種參數的 `ManagedOnlineDeployment` 物件
demo_deployment = ManagedOnlineDeployment(
    name="demo",
    endpoint_name=online_endpoint_name,
    model=registered_model.id,
    instance_type=instance_type,
    instance_count=1,
    liveness_probe=ProbeSettings(initial_delay=600),
    request_settings=OnlineRequestSettings(request_timeout_ms=90000),
)

# 通過呼叫 `workspace_ml_client` 的 `begin_create_or_update` 方法並將 `ManagedOnlineDeployment` 物件作為參數來建立部署
# 然後通過呼叫 `wait` 方法等待建立操作完成
workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()

# 設定端點的流量以將 100% 的流量導向 "demo" 部署
endpoint.traffic = {"demo": 100}

# 通過呼叫 `workspace_ml_client` 的 `begin_create_or_update` 方法並將 `endpoint` 物件作為參數來更新端點
# 然後通過呼叫 `result` 方法等待更新操作完成
workspace_ml_client.begin_create_or_update(endpoint).result()
```

## 8. 測試端點與範例資料

我們將從測試數據集中提取一些範例數據並提交到線上端點進行推論。然後我們將顯示得分標籤與真實標籤並排顯示。

### 閱讀結果

這個 Python 程式碼正在將一個 JSON Lines 文件讀取到 pandas DataFrame 中，隨機取樣並重置索引。以下是它的功能分解：

它讀取檔案 ./ultrachat_200k_dataset/test_gen.jsonl 到 pandas DataFrame 中。使用 read_json 函式並帶有 lines=True 參數，因為該檔案是 JSON Lines 格式，每一行都是一個單獨的 JSON 物件。

它從 DataFrame 中隨機抽取 1 行。sample 函式與 n=1 參數一起使用，以指定要選擇的隨機行數。

它會重置 DataFrame 的索引。reset_index 函式與 drop=True 參數一起使用，以刪除原始索引並將其替換為新的預設整數值索引。

它使用 head 函式和參數 2 顯示 DataFrame 的前兩行。然而，由於 DataFrame 在取樣後僅包含一行，這將只顯示那一行。

總結來說，這個腳本會將 JSON Lines 文件讀取到 pandas DataFrame 中，隨機抽取一行，重設索引，並顯示第一行。

```
# 匯入 pandas 函式庫
import pandas as pd

# 將 JSON Lines 檔案 './ultrachat_200k_dataset/test_gen.jsonl' 讀取到 pandas DataFrame 中
# 'lines=True' 參數表示檔案是 JSON Lines 格式，每行是一個單獨的 JSON 物件
test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)

# 從 DataFrame 中隨機抽取 1 行
# 'n=1' 參數指定要選擇的隨機行數
test_df = test_df.sample(n=1)

# 重設 DataFrame 的索引
# 'drop=True' 參數表示應該丟棄原始索引並替換為新的預設整數值索引
# 'inplace=True' 參數表示應該直接修改 DataFrame（不建立新的物件）
test_df.reset_index(drop=True, inplace=True)

# 顯示 DataFrame 的前 2 行
# 但是，由於抽樣後 DataFrame 只包含一行，因此這將只顯示那一行
test_df.head(2)
```

### 建立 JSON 物件

這個 Python 程式碼正在建立一個具有特定參數的 JSON 物件並將其保存到檔案中。以下是它的功能分解:

它匯入了 json 套件，該套件提供了處理 JSON 資料的函式。

它建立了一個字典參數，其中包含代表機器學習模型參數的鍵和值。這些鍵是 "temperature"、"top_p"、"do_sample" 和 "max_new_tokens"，它們對應的值分別是 0.6、0.9、True 和 200。

它建立了另一個字典 test_json，包含兩個鍵："input_data" 和 "params"。"input_data" 的值是另一個字典，包含鍵 "input_string" 和 "parameters"。"input_string" 的值是一個列表，包含來自 test_df DataFrame 的第一條訊息。"parameters" 的值是之前建立的參數字典。"params" 的值是一個空字典。

它打開了一個名為 sample_score.json 的文件

```
# 匯入 json 模組，提供處理 JSON 資訊的函式
import json

# 建立一個字典 `parameters`，包含機器學習模型的參數鍵值對
# 鍵為 "temperature"、"top_p"、"do_sample" 和 "max_new_tokens"，對應的值分別為 0.6、0.9、True 和 200
parameters = {
    "temperature": 0.6,
    "top_p": 0.9,
    "do_sample": True,
    "max_new_tokens": 200,
}

# 建立另一個字典 `test_json`，包含兩個鍵："input_data" 和 "params"
# "input_data" 的值是另一個字典，包含鍵 "input_string" 和 "parameters"
# "input_string" 的值是一個列表，包含來自 `test_df` DataFrame 的第一條訊息
# "parameters" 的值是之前建立的 `parameters` 字典
# "params" 的值是一個空字典
test_json = {
    "input_data": {
        "input_string": [test_df["messages"][0]],
        "parameters": parameters,
    },
    "params": {},
}

# 以寫入模式打開位於 `./ultrachat_200k_dataset` 目錄中的名為 `sample_score.json` 的檔案
with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
    # 使用 `json.dump` 函式將 `test_json` 字典以 JSON 格式寫入檔案
    json.dump(test_json, f)
```

### 呼叫端點

這個 Python 程式碼正在呼叫 Azure Machine Learning 中的一個線上端點來評分一個 JSON 文件。以下是它的作用分解:

它呼叫 workspace_ml_client 物件的 online_endpoints 屬性的 invoke 方法。此方法用於向線上端點發送請求並獲取回應。

它指定了端點的名稱和部署，使用 endpoint_name 和 deployment_name 參數。在這種情況下，端點名稱存儲在 online_endpoint_name 變數中，部署名稱是 "展示"。

它指定了要使用 request_file 參數評分的 JSON 文件的路徑。在這種情況下，文件是 ./ultrachat_200k_dataset/sample_score.json。

它將來自端點的回應儲存在 response 變數中。

它會列印原始回應。

總結來說，這個腳本正在呼叫 Azure Machine Learning 的一個線上端點來評分一個 JSON 檔案並列印回應。

```
# 呼叫 Azure Machine Learning 中的線上端點來評分 `sample_score.json` 檔案
# 使用 `workspace_ml_client` 物件的 `online_endpoints` 屬性的 `invoke` 方法來發送請求到線上端點並獲取回應
# `endpoint_name` 參數指定端點的名稱，該名稱存儲在 `online_endpoint_name` 變數中
# `deployment_name` 參數指定部署的名稱，即 "demo"
# `request_file` 參數指定要評分的 JSON 檔案的路徑，即 `./ultrachat_200k_dataset/sample_score.json`
response = workspace_ml_client.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    deployment_name="demo",
    request_file="./ultrachat_200k_dataset/sample_score.json",
)

# 列印來自端點的原始回應
print("raw response: \n", response, "\n")
```

## 9. 刪除線上端點

不要忘記刪除線上端點，否則你會讓計費表因端點使用的計算資源而持續執行。這行 Python 程式碼正在刪除 Azure 機器學習中的線上端點。以下是它的作用分解：

它呼叫了 workspace_ml_client 物件的 online_endpoints 屬性的 begin_delete 方法。此方法用於開始刪除線上端點。

它使用 name 參數指定要刪除的端點名稱。在這種情況下，端點名稱存儲在 online_endpoint_name 變數中。

它呼叫 wait 方法來等待刪除操作完成。這是一個阻塞操作，意味著它會阻止腳本繼續執行直到刪除完成。

總結來說，這行程式碼正在啟動刪除 Azure 機器學習中的線上端點，並等待操作完成。

```
# 刪除 Azure Machine Learning 中的線上端點
# `workspace_ml_client` 物件的 `online_endpoints` 屬性的 `begin_delete` 方法用於開始刪除線上端點
# `name` 參數指定要刪除的端點名稱，該名稱存儲在 `online_endpoint_name` 變數中
# 呼叫 `wait` 方法以等待刪除操作完成。這是一個阻塞操作，意味著它會阻止腳本繼續執行，直到刪除完成
workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
```

