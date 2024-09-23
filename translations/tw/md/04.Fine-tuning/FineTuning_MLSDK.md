
它匯入了 `os` 模組，這個模組提供了一種跨平台使用作業系統相關功能的方法。它使用 `os.system` 函數在 shell 中執行 `download-dataset.py` 腳本，並帶有特定的命令行參數。這些參數指定了要下載的資料集（HuggingFaceH4/ultrachat_200k）、下載的目錄（ultrachat_200k_dataset）以及資料集要分割的百分比（5）。`os.system` 函數返回它所執行命令的退出狀態；這個狀態被存儲在 `exit_status` 變數中。它檢查 `exit_status` 是否不等於 0。在類 Unix 作業系統中，退出狀態為 0 通常表示命令成功執行，而其他任何數字則表示錯誤。如果 `exit_status` 不等於 0，它會拋出一個異常，並附帶一條訊息，指示下載資料集時出現錯誤。總結來說，這個腳本執行了一個命令來下載資料集，並在命令失敗時拋出異常。

```
# 匯入 os 模組，這個模組提供了一種使用作業系統相關功能的方法
import os

# 使用 os.system 函數在 shell 中執行 download-dataset.py 腳本，並帶有特定的命令行參數
# 這些參數指定了要下載的資料集（HuggingFaceH4/ultrachat_200k）、下載的目錄（ultrachat_200k_dataset）以及資料集要分割的百分比（5）
# os.system 函數返回它所執行命令的退出狀態；這個狀態被存儲在 exit_status 變數中
exit_status = os.system(
    "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
)

# 檢查 exit_status 是否不等於 0
# 在類 Unix 作業系統中，退出狀態為 0 通常表示命令成功執行，而其他任何數字則表示錯誤
# 如果 exit_status 不等於 0，拋出一個異常，並附帶一條訊息，指示下載資料集時出現錯誤
if exit_status != 0:
    raise Exception("Error downloading dataset")
```

### 將資料載入 DataFrame

這個 Python 腳本將一個 JSON Lines 檔案載入 pandas DataFrame 並顯示前 5 行。以下是它的功能分解：

它匯入了 pandas 庫，這是一個強大的資料操作和分析庫。

它將 pandas 的顯示選項中的最大欄寬設置為 0。這意味著當 DataFrame 被列印時，每個欄位的完整文本都會顯示，而不會被截斷。

它使用 `pd.read_json` 函數從 `ultrachat_200k_dataset` 目錄中載入 `train_sft.jsonl` 檔案到 DataFrame 中。`lines=True` 參數表明該檔案是 JSON Lines 格式，其中每行是一個單獨的 JSON 物件。

它使用 `head` 方法顯示 DataFrame 的前 5 行。如果 DataFrame 少於 5 行，它將顯示所有行。

總結來說，這個腳本將一個 JSON Lines 檔案載入 DataFrame，並顯示前 5 行的完整欄位文本。

```
# 匯入 pandas 庫，這是一個強大的資料操作和分析庫
import pandas as pd

# 將 pandas 的顯示選項中的最大欄寬設置為 0
# 這意味著當 DataFrame 被列印時，每個欄位的完整文本都會顯示，而不會被截斷
pd.set_option("display.max_colwidth", 0)

# 使用 pd.read_json 函數從 ultrachat_200k_dataset 目錄中載入 train_sft.jsonl 檔案到 DataFrame 中
# lines=True 參數表明該檔案是 JSON Lines 格式，其中每行是一個單獨的 JSON 物件
df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)

# 使用 head 方法顯示 DataFrame 的前 5 行
# 如果 DataFrame 少於 5 行，它將顯示所有行
df.head()
```

## 5. 使用模型和資料作為輸入提交微調任務

創建一個使用 chat-completion pipeline 組件的任務。了解更多關於微調支持的所有參數。

### 定義微調參數

微調參數可以分為兩類——訓練參數和優化參數。

訓練參數定義了訓練方面的內容，例如：

- 使用的優化器、調度器
- 微調的優化指標
- 訓練步數、批次大小等

優化參數有助於優化 GPU 記憶體並有效使用計算資源。

以下是屬於這類的一些參數。優化參數因模型而異，並與模型一起打包以處理這些變化。

- 啟用 deepspeed 和 LoRA
- 啟用混合精度訓練
- 啟用多節點訓練

**Note:** 監督微調可能會導致對齊喪失或災難性遺忘。我們建議在微調後檢查此問題並進行對齊階段。

### 微調參數

這個 Python 腳本設置了微調機器學習模型的參數。以下是它的功能分解：

它設置了默認的訓練參數，如訓練週期數、訓練和評估的批次大小、學習率和學習率調度器類型。

它設置了默認的優化參數，如是否應用 Layer-wise Relevance Propagation (LoRa) 和 DeepSpeed，以及 DeepSpeed 階段。

它將訓練和優化參數合併到一個名為 `finetune_parameters` 的字典中。

它檢查 `foundation_model` 是否有任何模型特定的默認參數。如果有，它會列印警告訊息並使用這些模型特定的默認值更新 `finetune_parameters` 字典。`ast.literal_eval` 函數用於將模型特定的默認值從字串轉換為 Python 字典。

它列印將用於運行的最終微調參數集。

總結來說，這個腳本設置並顯示了微調機器學習模型的參數，並能夠用模型特定的參數覆蓋默認參數。

```
# 設置默認的訓練參數，如訓練週期數、訓練和評估的批次大小、學習率和學習率調度器類型
training_parameters = dict(
    num_train_epochs=3,
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    learning_rate=5e-6,
    lr_scheduler_type="cosine",
)

# 設置默認的優化參數，如是否應用 Layer-wise Relevance Propagation (LoRa) 和 DeepSpeed，以及 DeepSpeed 階段
optimization_parameters = dict(
    apply_lora="true",
    apply_deepspeed="true",
    deepspeed_stage=2,
)

# 將訓練和優化參數合併到一個名為 finetune_parameters 的字典中
finetune_parameters = {**training_parameters, **optimization_parameters}

# 檢查 foundation_model 是否有任何模型特定的默認參數
# 如果有，列印警告訊息並使用這些模型特定的默認值更新 finetune_parameters 字典
# ast.literal_eval 函數用於將模型特定的默認值從字串轉換為 Python 字典
if "model_specific_defaults" in foundation_model.tags:
    print("Warning! Model specific defaults exist. The defaults could be overridden.")
    finetune_parameters.update(
        ast.literal_eval(  # 將字串轉換為 python 字典
            foundation_model.tags["model_specific_defaults"]
        )
    )

# 列印將用於運行的最終微調參數集
print(
    f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
)
```

### 訓練管道

這個 Python 腳本定義了一個函數來生成機器學習訓練管道的顯示名稱，然後調用這個函數來生成並列印顯示名稱。以下是它的功能分解：

`get_pipeline_display_name` 函數被定義。這個函數根據與訓練管道相關的各種參數生成顯示名稱。

在函數內，它通過將每設備批次大小、梯度累積步數、每節點 GPU 數量和微調使用的節點數量相乘來計算總批次大小。

它檢索各種其他參數，如學習率調度器類型、是否應用 DeepSpeed、DeepSpeed 階段、是否應用 Layer-wise Relevance Propagation (LoRa)、保留的模型檢查點數量限制和最大序列長度。

它構建了一個包含所有這些參數的字串，並以連字符分隔。如果應用了 DeepSpeed 或 LoRa，該字串包括 "ds" 後接 DeepSpeed 階段，或 "lora"。如果沒有，則包括 "nods" 或 "nolora"。

該函數返回這個字串，作為訓練管道的顯示名稱。

在函數定義之後，它被調用來生成顯示名稱，然後列印這個顯示名稱。

總結來說，這個腳本根據各種參數生成機器學習訓練管道的顯示名稱，然後列印這個顯示名稱。

```
# 定義一個函數來生成訓練管道的顯示名稱
def get_pipeline_display_name():
    # 通過將每設備批次大小、梯度累積步數、每節點 GPU 數量和微調使用的節點數量相乘來計算總批次大小
    batch_size = (
        int(finetune_parameters.get("per_device_train_batch_size", 1))
        * int(finetune_parameters.get("gradient_accumulation_steps", 1))
        * int(gpus_per_node)
        * int(finetune_parameters.get("num_nodes_finetune", 1))
    )
    # 檢索學習率調度器類型
    scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
    # 檢索是否應用 DeepSpeed
    deepspeed = finetune_parameters.get("apply_deepspeed", "false")
    # 檢索 DeepSpeed 階段
    ds_stage = finetune_parameters.get("deepspeed_stage", "2")
    # 如果應用了 DeepSpeed，在顯示名稱中包括 "ds" 後接 DeepSpeed 階段；如果沒有，則包括 "nods"
    if deepspeed == "true":
        ds_string = f"ds{ds_stage}"
    else:
        ds_string = "nods"
    # 檢索是否應用 Layer-wise Relevance Propagation (LoRa)
    lora = finetune_parameters.get("apply_lora", "false")
    # 如果應用了 LoRa，在顯示名稱中包括 "lora"；如果沒有，則包括 "nolora"
    if lora == "true":
        lora_string = "lora"
    else:
        lora_string = "nolora"
    # 檢索保留的模型檢查點數量限制
    save_limit = finetune_parameters.get("save_total_limit", -1)
    # 檢索最大序列長度
    seq_len = finetune_parameters.get("max_seq_length", -1)
    # 通過連字符分隔所有這些參數來構建顯示名稱
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

# 調用函數生成顯示名稱
pipeline_display_name = get_pipeline_display_name()
# 列印顯示名稱
print(f"Display name used for the run: {pipeline_display_name}")
```

### 配置管道

這個 Python 腳本使用 Azure Machine Learning SDK 定義和配置機器學習管道。以下是它的功能分解：

1. 它從 Azure AI ML SDK 匯入必要的模組。

2. 它從註冊表中獲取名為 "chat_completion_pipeline" 的管道組件。

3. 它使用 `@pipeline` 裝飾器和 `create_pipeline` 函數定義一個管道任務。管道的名稱設置為 `pipeline_display_name`。

4. 在 `create_pipeline` 函數內，它初始化獲取的管道組件並設置各種參數，包括模型路徑、不同階段的計算叢集、訓練和測試的資料集分割、微調使用的 GPU 數量以及其他微調參數。

5. 它將微調任務的輸出映射到管道任務的輸出。這樣可以輕鬆註冊微調後的模型，這是將模型部署到在線或批次端點所需的。

6. 它通過調用 `create_pipeline` 函數創建管道實例。

7. 它將管道的 `force_rerun` 設置為 `True`，這意味著不會使用之前任務的緩存結果。

8. 它將管道的 `continue_on_step_failure` 設置為 `False`，這意味著如果任何步驟失敗，管道將停止。

總結來說，這個腳本使用 Azure Machine Learning SDK 定義和配置了一個用於聊天完成任務的機器學習管道。

```
# 從 Azure AI ML SDK 匯入必要的模組
from azure.ai.ml.dsl import pipeline
from azure.ai.ml import Input

# 從註冊表中獲取名為 "chat_completion_pipeline" 的管道組件
pipeline_component_func = registry_ml_client.components.get(
    name="chat_completion_pipeline", label="latest"
)

# 使用 @pipeline 裝飾器和 create_pipeline 函數定義管道任務
# 管道的名稱設置為 pipeline_display_name
@pipeline(name=pipeline_display_name)
def create_pipeline():
    # 初始化獲取的管道組件並設置各種參數
    # 包括模型路徑、不同階段的計算叢集、訓練和測試的資料集分割、微調使用的 GPU 數量以及其他微調參數
    chat_completion_pipeline = pipeline_component_func(
        mlflow_model_path=foundation_model.id,
        compute_model_import=compute_cluster,
        compute_preprocess=compute_cluster,
        compute_finetune=compute_cluster,
        compute_model_evaluation=compute_cluster,
        # 將資料集分割映射到參數
        train_file_path=Input(
            type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
        ),
        test_file_path=Input(
            type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
        ),
        # 訓練設置
        number_of_gpu_to_use_finetuning=gpus_per_node,  # 設置為計算叢集中可用的 GPU 數量
        **finetune_parameters
    )
    return {
        # 將微調任務的輸出映射到管道任務的輸出
        # 這樣可以輕鬆註冊微調後的模型
        # 註冊模型是將模型部署到在線或批次端點所需的
        "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
    }

# 通過調用 create_pipeline 函數創建管道實例
pipeline_object = create_pipeline()

# 不使用之前任務的緩存結果
pipeline_object.settings.force_rerun = True

# 將 continue on step failure 設置為 False
# 這意味著如果任何步驟失敗，管道將停止
pipeline_object.settings.continue_on_step_failure = False
```

### 提交任務

這個 Python 腳本將機器學習管道任務提交到 Azure Machine Learning 工作區，然後等待任務完成。以下是它的功能分解：

它調用 `workspace_ml_client` 中 `jobs` 物件的 `create_or_update` 方法來提交管道任務。要運行的管道由 `pipeline_object` 指定，任務所在的實驗由 `experiment_name` 指定。

然後它調用 `workspace_ml_client` 中 `jobs` 物件的 `stream` 方法來等待管道任務完成。要等待的任務由 `pipeline_job` 物件的 `name` 屬性指定。

總結來說，這個腳本將機器學習管道任務提交到 Azure Machine Learning 工作區，然後等待任務完成。

```

```
# 從 Azure AI ML SDK 匯入必要的模組
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes

# 檢查 `trained_model` 輸出是否從 pipeline job 可用
print("pipeline job outputs: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)

# 通過格式化字串來構建訓練模型的路徑，包含 pipeline job 的名稱和輸出的名稱 ("trained_model")
model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
    pipeline_job.name, "trained_model"
)

# 定義微調模型的名稱，將原始模型名稱後加上 "-ultrachat-200k"，並將任何斜線替換為連字符
finetuned_model_name = model_name + "-ultrachat-200k"
finetuned_model_name = finetuned_model_name.replace("/", "-")

print("path to register model: ", model_path_from_job)

# 準備註冊模型，創建一個 Model 物件，包含各種參數
# 這些參數包括模型的路徑、模型的類型（MLflow 模型）、模型的名稱和版本，以及模型的描述
prepare_to_register_model = Model(
    path=model_path_from_job,
    type=AssetTypes.MLFLOW_MODEL,
    name=finetuned_model_name,
    version=timestamp,  # 使用時間戳作為版本以避免版本衝突
    description=model_name + " fine tuned model for ultrachat 200k chat-completion",
)

print("prepare to register model: \n", prepare_to_register_model)

# 通過呼叫 workspace_ml_client 中 models 物件的 create_or_update 方法並傳入 Model 物件作為參數來註冊模型
registered_model = workspace_ml_client.models.create_or_update(
    prepare_to_register_model
)

# 列印已註冊的模型
print("registered model: \n", registered_model)
```
## 7. 部署微調後的模型到線上端點
線上端點提供了一個持久的 REST API，可以用來整合需要使用模型的應用程式。

### 管理端點
這段 Python 腳本在 Azure Machine Learning 中為已註冊的模型創建一個管理的線上端點。以下是它的工作原理：

它從 Azure AI ML SDK 中匯入必要的模組。

它通過將時間戳附加到字串 "ultrachat-completion-" 來定義線上端點的唯一名稱。

它準備創建線上端點，通過創建一個 ManagedOnlineEndpoint 物件，並設置多個參數，包括端點名稱、端點描述和驗證模式（"key"）。

它通過調用 workspace_ml_client 的 begin_create_or_update 方法，並以 ManagedOnlineEndpoint 物件作為參數來創建線上端點。然後通過調用 wait 方法等待創建操作完成。

總結來說，這段腳本是在 Azure Machine Learning 中為已註冊的模型創建一個管理的線上端點。

```
# 從 Azure AI ML SDK 匯入必要的模組
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    ProbeSettings,
    OnlineRequestSettings,
)

# 通過將時間戳附加到字串 "ultrachat-completion-" 來定義線上端點的唯一名稱
online_endpoint_name = "ultrachat-completion-" + timestamp

# 準備創建線上端點，創建一個 ManagedOnlineEndpoint 物件並設置多個參數
# 這些參數包括端點名稱、端點描述和驗證模式（"key"）
endpoint = ManagedOnlineEndpoint(
    name=online_endpoint_name,
    description="Online endpoint for "
    + registered_model.name
    + ", fine tuned model for ultrachat-200k-chat-completion",
    auth_mode="key",
)

# 通過調用 workspace_ml_client 的 begin_create_or_update 方法，並以 ManagedOnlineEndpoint 物件作為參數來創建線上端點
# 然後通過調用 wait 方法等待創建操作完成
workspace_ml_client.begin_create_or_update(endpoint).wait()
```
你可以在這裡找到支援部署的 SKU 列表 - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### 部署機器學習模型

這段 Python 腳本正在將已註冊的機器學習模型部署到 Azure Machine Learning 中的管理線上端點。以下是它的工作原理：

它匯入了 ast 模組，該模組提供了處理 Python 抽象語法樹的函數。

它設置了部署的實例類型為 "Standard_NC6s_v3"。

它檢查基礎模型中是否存在 inference_compute_allow_list 標籤。如果存在，則將標籤值從字串轉換為 Python 列表，並賦值給 inference_computes_allow_list。如果不存在，則將 inference_computes_allow_list 設置為 None。

它檢查指定的實例類型是否在允許列表中。如果不在，則打印消息請用戶從允許列表中選擇實例類型。

它準備創建部署，創建一個 ManagedOnlineDeployment 物件並設置多個參數，包括部署名稱、端點名稱、模型 ID、實例類型和數量、活性探測設置以及請求設置。

它通過調用 workspace_ml_client 的 begin_create_or_update 方法，並以 ManagedOnlineDeployment 物件作為參數來創建部署。然後通過調用 wait 方法等待創建操作完成。

它設置端點的流量，將 100% 的流量指向 "demo" 部署。

它通過調用 workspace_ml_client 的 begin_create_or_update 方法，並以端點物件作為參數來更新端點。然後通過調用 result 方法等待更新操作完成。

總結來說，這段腳本正在將已註冊的機器學習模型部署到 Azure Machine Learning 中的管理線上端點。

```
# 匯入 ast 模組，該模組提供了處理 Python 抽象語法樹的函數
import ast

# 設置部署的實例類型
instance_type = "Standard_NC6s_v3"

# 檢查基礎模型中是否存在 `inference_compute_allow_list` 標籤
if "inference_compute_allow_list" in foundation_model.tags:
    # 如果存在，將標籤值從字串轉換為 Python 列表，並賦值給 `inference_computes_allow_list`
    inference_computes_allow_list = ast.literal_eval(
        foundation_model.tags["inference_compute_allow_list"]
    )
    print(f"Please create a compute from the above list - {computes_allow_list}")
else:
    # 如果不存在，則將 `inference_computes_allow_list` 設置為 `None`
    inference_computes_allow_list = None
    print("`inference_compute_allow_list` is not part of model tags")

# 檢查指定的實例類型是否在允許列表中
if (
    inference_computes_allow_list is not None
    and instance_type not in inference_computes_allow_list
):
    print(
        f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
    )

# 準備創建部署，創建一個 `ManagedOnlineDeployment` 物件並設置多個參數
demo_deployment = ManagedOnlineDeployment(
    name="demo",
    endpoint_name=online_endpoint_name,
    model=registered_model.id,
    instance_type=instance_type,
    instance_count=1,
    liveness_probe=ProbeSettings(initial_delay=600),
    request_settings=OnlineRequestSettings(request_timeout_ms=90000),
)

# 通過調用 `workspace_ml_client` 的 `begin_create_or_update` 方法，並以 `ManagedOnlineDeployment` 物件作為參數來創建部署
# 然後通過調用 `wait` 方法等待創建操作完成
workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()

# 設置端點的流量，將 100% 的流量指向 "demo" 部署
endpoint.traffic = {"demo": 100}

# 通過調用 `workspace_ml_client` 的 `begin_create_or_update` 方法，並以 `endpoint` 物件作為參數來更新端點
# 然後通過調用 `result` 方法等待更新操作完成
workspace_ml_client.begin_create_or_update(endpoint).result()
```
## 8. 使用範例數據測試端點
我們將從測試數據集中提取一些範例數據並提交到線上端點進行推理。然後我們將顯示得分標籤和真實標籤。

### 讀取結果
這段 Python 腳本正在將一個 JSON Lines 文件讀取到 pandas DataFrame 中，隨機取樣並重置索引。以下是它的工作原理：

它將文件 ./ultrachat_200k_dataset/test_gen.jsonl 讀取到 pandas DataFrame 中。由於該文件是 JSON Lines 格式，每行都是一個單獨的 JSON 對象，因此使用 read_json 函數並設置 lines=True 參數。

它從 DataFrame 中隨機取樣 1 行。使用 sample 函數並設置 n=1 參數來指定隨機選擇的行數。

它重置 DataFrame 的索引。使用 reset_index 函數並設置 drop=True 參數來丟棄原始索引並用默認的整數索引替換。

它使用 head 函數並設置參數 2 來顯示 DataFrame 的前 2 行。然而，由於取樣後 DataFrame 只包含一行，因此只會顯示那一行。

總結來說，這段腳本正在將一個 JSON Lines 文件讀取到 pandas DataFrame 中，隨機取樣 1 行，重置索引並顯示第一行。

```
# 匯入 pandas 庫
import pandas as pd

# 將 JSON Lines 文件 './ultrachat_200k_dataset/test_gen.jsonl' 讀取到 pandas DataFrame 中
# 'lines=True' 參數表示該文件是 JSON Lines 格式，每行都是一個單獨的 JSON 對象
test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)

# 從 DataFrame 中隨機取樣 1 行
# 'n=1' 參數指定隨機選擇的行數
test_df = test_df.sample(n=1)

# 重置 DataFrame 的索引
# 'drop=True' 參數表示應丟棄原始索引並用默認的整數索引替換
# 'inplace=True' 參數表示應直接修改 DataFrame 而不創建新對象
test_df.reset_index(drop=True, inplace=True)

# 顯示 DataFrame 的前 2 行
# 然而，由於取樣後 DataFrame 只包含一行，因此只會顯示那一行
test_df.head(2)
```
### 創建 JSON 對象

這段 Python 腳本正在創建一個包含特定參數的 JSON 對象並將其保存到文件中。以下是它的工作原理：

它匯入了 json 模組，該模組提供了處理 JSON 數據的函數。

它創建了一個字典 parameters，其中包含代表機器學習模型參數的鍵值對。這些鍵包括 "temperature"、"top_p"、"do_sample" 和 "max_new_tokens"，對應的值分別是 0.6、0.9、True 和 200。

它創建了另一個字典 test_json，包含兩個鍵："input_data" 和 "params"。"input_data" 的值是另一個字典，包含鍵 "input_string" 和 "parameters"。"input_string" 的值是一個列表，包含來自 test_df DataFrame 的第一條消息。"parameters" 的值是先前創建的 parameters 字典。"params" 的值是一個空字典。

它打開了一個名為 sample_score.json 的文件，將 test_json 字典以 JSON 格式寫入該文件。

```
# 匯入 json 模組，該模組提供了處理 JSON 數據的函數
import json

# 創建一個字典 `parameters`，其中包含代表機器學習模型參數的鍵值對
# 這些鍵包括 "temperature"、"top_p"、"do_sample" 和 "max_new_tokens"，對應的值分別是 0.6、0.9、True 和 200
parameters = {
    "temperature": 0.6,
    "top_p": 0.9,
    "do_sample": True,
    "max_new_tokens": 200,
}

# 創建另一個字典 `test_json`，包含兩個鍵："input_data" 和 "params"
# "input_data" 的值是另一個字典，包含鍵 "input_string" 和 "parameters"
# "input_string" 的值是一個列表，包含來自 `test_df` DataFrame 的第一條消息
# "parameters" 的值是先前創建的 `parameters` 字典
# "params" 的值是一個空字典
test_json = {
    "input_data": {
        "input_string": [test_df["messages"][0]],
        "parameters": parameters,
    },
    "params": {},
}

# 以寫入模式打開名為 `sample_score.json` 的文件
with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
    # 使用 `json.dump` 函數將 `test_json` 字典以 JSON 格式寫入文件
    json.dump(test_json, f)
```
### 調用端點

這段 Python 腳本正在調用 Azure Machine Learning 中的線上端點來對 JSON 文件進行評分。以下是它的工作原理：

它調用 workspace_ml_client 對象的 online_endpoints 屬性的 invoke 方法。這個方法用來向線上端點發送請求並獲取響應。

它通過 endpoint_name 和 deployment_name 參數指定端點和部署的名稱。在這個例子中，端點名稱存儲在 online_endpoint_name 變數中，部署名稱是 "demo"。

它通過 request_file 參數指定要評分的 JSON 文件的路徑。在這個例子中，文件是 ./ultrachat_200k_dataset/sample_score.json。

它將來自端點的響應存儲在 response 變數中。

它打印原始響應。

總結來說，這段腳本正在調用 Azure Machine Learning 中的線上端點來對 JSON 文件進行評分並打印響應。

```
# 調用 Azure Machine Learning 中的線上端點來對 `sample_score.json` 文件進行評分
# `invoke` 方法屬於 `workspace_ml_client` 對象的 `online_endpoints` 屬性，用來向線上端點發送請求並獲取響應
# `endpoint_name` 參數指定端點的名稱，存儲在 `online_endpoint_name` 變數中
# `deployment_name` 參數指定部署的名稱，這裡是 "demo"
# `request_file` 參數指定要評分的 JSON 文件的路徑，這裡是 `./ultrachat_200k_dataset/sample_score.json`
response = workspace_ml_client.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    deployment_name="demo",
    request_file="./ultrachat_200k_dataset/sample_score.json",
)

# 打印來自端點的原始響應
print("raw response: \n", response, "\n")
```
## 9. 刪除線上端點
別忘了刪除線上端點，否則端點使用的計算資源會繼續計費。這行 Python 代碼正在刪除 Azure Machine Learning 中的線上端點。以下是它的工作原理：

它調用 workspace_ml_client 對象的 online_endpoints 屬性的 begin_delete 方法。這個方法用來開始刪除線上端點。

它通過 name 參數指定要刪除的端點名稱。在這個例子中，端點名稱存儲在 online_endpoint_name 變數中。

它調用 wait 方法來等待刪除操作完成。這是一個阻塞操作，意味著在刪除完成之前腳本不會繼續執行。

總結來說，這行代碼正在開始刪除 Azure Machine Learning 中的線上端點並等待操作完成。

```
# 刪除 Azure Machine Learning 中的線上端點
# `begin_delete` 方法屬於 `workspace_ml_client` 對象的 `online_endpoints` 屬性，用來開始刪除線上端點
# `name` 參數指定要刪除的端點名稱，存儲在 `online_endpoint_name` 變數中
# `wait` 方法用來等待刪除操作完成，這是一個阻塞操作，意味著在刪除完成之前腳本不會繼續執行
workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
```

免責聲明：此翻譯由AI模型從原文翻譯而來，可能不夠完美。請檢查輸出並進行必要的修改。