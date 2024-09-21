
osモジュールをインポートして、OS依存の機能をポータブルに利用できるようにします。os.system関数を使って、特定のコマンドライン引数を指定してdownload-dataset.pyスクリプトをシェルで実行します。引数はダウンロードするデータセット（HuggingFaceH4/ultrachat_200k）、ダウンロード先のディレクトリ（ultrachat_200k_dataset）、データセットを分割する割合（5）を指定します。os.system関数は実行したコマンドの終了ステータスを返し、このステータスはexit_status変数に格納されます。exit_statusが0でないかどうかをチェックします。Unix系のオペレーティングシステムでは、終了ステータスが0である場合はコマンドが成功したことを示し、それ以外の数値はエラーを示します。exit_statusが0でない場合、データセットのダウンロード中にエラーが発生したことを示すメッセージと共にExceptionを発生させます。要約すると、このスクリプトはヘルパースクリプトを使ってデータセットをダウンロードするコマンドを実行し、コマンドが失敗した場合は例外を発生させます。
```
# OS依存の機能を利用するためのosモジュールをインポート
import os

# os.system関数を使って、特定のコマンドライン引数を指定してdownload-dataset.pyスクリプトをシェルで実行
# 引数はダウンロードするデータセット（HuggingFaceH4/ultrachat_200k）、ダウンロード先のディレクトリ（ultrachat_200k_dataset）、データセットを分割する割合（5）を指定
# os.system関数は実行したコマンドの終了ステータスを返し、このステータスはexit_status変数に格納
exit_status = os.system(
    "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
)

# exit_statusが0でないかをチェック
# Unix系のオペレーティングシステムでは、終了ステータスが0である場合はコマンドが成功したことを示し、それ以外の数値はエラーを示す
# exit_statusが0でない場合、データセットのダウンロード中にエラーが発生したことを示すメッセージと共にExceptionを発生させる
if exit_status != 0:
    raise Exception("Error downloading dataset")
```
### データをDataFrameにロード
このPythonスクリプトは、JSON Linesファイルをpandas DataFrameにロードし、最初の5行を表示します。以下はその詳細です：

pandasライブラリをインポートします。これは強力なデータ操作と分析のためのライブラリです。

pandasの表示オプションで、カラムの最大幅を0に設定します。これにより、DataFrameが印刷される際に各カラムの全テキストが切り捨てられずに表示されます。

pd.read_json関数を使用して、ultrachat_200k_datasetディレクトリからtrain_sft.jsonlファイルをDataFrameにロードします。lines=True引数は、ファイルがJSON Lines形式であることを示し、各行が個別のJSONオブジェクトであることを意味します。

headメソッドを使用して、DataFrameの最初の5行を表示します。DataFrameが5行未満の場合は、すべての行を表示します。

要約すると、このスクリプトはJSON LinesファイルをDataFrameにロードし、カラムの全テキストを表示した上で最初の5行を表示します。

```
# 強力なデータ操作と分析のためのpandasライブラリをインポート
import pandas as pd

# pandasの表示オプションで、カラムの最大幅を0に設定
# これにより、DataFrameが印刷される際に各カラムの全テキストが切り捨てられずに表示される
pd.set_option("display.max_colwidth", 0)

# pd.read_json関数を使用して、ultrachat_200k_datasetディレクトリからtrain_sft.jsonlファイルをDataFrameにロード
# lines=True引数は、ファイルがJSON Lines形式であることを示し、各行が個別のJSONオブジェクトであることを意味する
df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)

# headメソッドを使用して、DataFrameの最初の5行を表示
# DataFrameが5行未満の場合は、すべての行を表示
df.head()
```
## 5. モデルとデータを入力として微調整ジョブを送信
chat-completionパイプラインコンポーネントを使用するジョブを作成します。微調整のためにサポートされるすべてのパラメータについて詳しく学びましょう。

### 微調整パラメータの定義

微調整パラメータは2つのカテゴリに分けられます - トレーニングパラメータ、最適化パラメータ

トレーニングパラメータは、トレーニングの側面を定義します -

- 使用するオプティマイザ、スケジューラ
- 微調整を最適化するためのメトリック
- トレーニングステップ数とバッチサイズなど
- 最適化パラメータはGPUメモリの最適化と計算リソースの効果的な使用を助けます。

以下はこのカテゴリに属するいくつかのパラメータです。最適化パラメータはモデルごとに異なり、これらのバリエーションを処理するためにモデルと一緒にパッケージされています。

- deepspeedとLoRAの有効化
- 混合精度トレーニングの有効化
- マルチノードトレーニングの有効化

**Note:** 監督下での微調整はアラインメントの喪失や破滅的な忘却を引き起こす可能性があります。この問題をチェックし、微調整後にアラインメントステージを実行することをお勧めします。

### 微調整パラメータ

このPythonスクリプトは、機械学習モデルの微調整パラメータを設定しています。以下はその詳細です：

デフォルトのトレーニングパラメータを設定します。これには、トレーニングエポック数、トレーニングおよび評価のバッチサイズ、学習率、学習率スケジューラの種類が含まれます。

デフォルトの最適化パラメータを設定します。これには、Layer-wise Relevance Propagation（LoRa）およびDeepSpeedを適用するかどうか、DeepSpeedのステージが含まれます。

トレーニングパラメータと最適化パラメータを1つの辞書に結合し、finetune_parametersという名前を付けます。

foundation_modelにモデル固有のデフォルトパラメータがあるかどうかをチェックします。ある場合は、警告メッセージを表示し、これらのモデル固有のデフォルトでfinetune_parameters辞書を更新します。ast.literal_eval関数を使用して、モデル固有のデフォルトを文字列からPython辞書に変換します。

実行に使用される最終的な微調整パラメータセットを表示します。

要約すると、このスクリプトは機械学習モデルの微調整パラメータを設定および表示し、モデル固有のパラメータでデフォルトを上書きする機能を持っています。

```
# デフォルトのトレーニングパラメータを設定します。これには、トレーニングエポック数、トレーニングおよび評価のバッチサイズ、学習率、学習率スケジューラの種類が含まれます
training_parameters = dict(
    num_train_epochs=3,
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    learning_rate=5e-6,
    lr_scheduler_type="cosine",
)

# デフォルトの最適化パラメータを設定します。これには、Layer-wise Relevance Propagation（LoRa）およびDeepSpeedを適用するかどうか、DeepSpeedのステージが含まれます
optimization_parameters = dict(
    apply_lora="true",
    apply_deepspeed="true",
    deepspeed_stage=2,
)

# トレーニングパラメータと最適化パラメータを1つの辞書に結合し、finetune_parametersという名前を付けます
finetune_parameters = {**training_parameters, **optimization_parameters}

# foundation_modelにモデル固有のデフォルトパラメータがあるかどうかをチェックします
# ある場合は、警告メッセージを表示し、これらのモデル固有のデフォルトでfinetune_parameters辞書を更新します
# ast.literal_eval関数を使用して、モデル固有のデフォルトを文字列からPython辞書に変換します
if "model_specific_defaults" in foundation_model.tags:
    print("Warning! Model specific defaults exist. The defaults could be overridden.")
    finetune_parameters.update(
        ast.literal_eval(  # convert string to python dict
            foundation_model.tags["model_specific_defaults"]
        )
    )

# 実行に使用される最終的な微調整パラメータセットを表示します
print(
    f"The following finetune parameters are going to be set for the run: {finetune_parameters}"
)
```

### トレーニングパイプライン
このPythonスクリプトは、機械学習トレーニングパイプラインの表示名を生成する関数を定義し、この関数を呼び出して表示名を生成し、表示します。以下はその詳細です：

get_pipeline_display_name関数が定義されます。この関数は、トレーニングパイプラインに関連するさまざまなパラメータに基づいて表示名を生成します。

関数内では、デバイスごとのバッチサイズ、勾配累積ステップ数、ノードごとのGPU数、および微調整に使用されるノード数を掛け合わせて、合計バッチサイズを計算します。

学習率スケジューラの種類、DeepSpeedが適用されているかどうか、DeepSpeedのステージ、Layer-wise Relevance Propagation（LoRa）が適用されているかどうか、保持するモデルチェックポイントの数の制限、および最大シーケンス長などの他のパラメータを取得します。

これらのパラメータをすべて含む文字列をハイフンで区切って構築します。DeepSpeedまたはLoRaが適用されている場合、文字列にはそれぞれDeepSpeedステージまたは"lora"が含まれます。適用されていない場合、それぞれ"nods"または"nolora"が含まれます。

関数はこの文字列を返し、これがトレーニングパイプラインの表示名として機能します。

関数が定義された後、表示名を生成するために呼び出され、その表示名が印刷されます。

要約すると、このスクリプトは、さまざまなパラメータに基づいて機械学習トレーニングパイプラインの表示名を生成し、その表示名を印刷します。

```
# トレーニングパイプラインの表示名を生成する関数を定義
def get_pipeline_display_name():
    # デバイスごとのバッチサイズ、勾配累積ステップ数、ノードごとのGPU数、および微調整に使用されるノード数を掛け合わせて、合計バッチサイズを計算
    batch_size = (
        int(finetune_parameters.get("per_device_train_batch_size", 1))
        * int(finetune_parameters.get("gradient_accumulation_steps", 1))
        * int(gpus_per_node)
        * int(finetune_parameters.get("num_nodes_finetune", 1))
    )
    # 学習率スケジューラの種類を取得
    scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
    # DeepSpeedが適用されているかどうかを取得
    deepspeed = finetune_parameters.get("apply_deepspeed", "false")
    # DeepSpeedのステージを取得
    ds_stage = finetune_parameters.get("deepspeed_stage", "2")
    # DeepSpeedが適用されている場合、表示名に"ds"とDeepSpeedステージを含める; そうでない場合は"nods"を含める
    if deepspeed == "true":
        ds_string = f"ds{ds_stage}"
    else:
        ds_string = "nods"
    # Layer-wise Relevance Propagation（LoRa）が適用されているかどうかを取得
    lora = finetune_parameters.get("apply_lora", "false")
    # LoRaが適用されている場合、表示名に"lora"を含める; そうでない場合は"nolora"を含める
    if lora == "true":
        lora_string = "lora"
    else:
        lora_string = "nolora"
    # モデルチェックポイントの保持数の制限を取得
    save_limit = finetune_parameters.get("save_total_limit", -1)
    # 最大シーケンス長を取得
    seq_len = finetune_parameters.get("max_seq_length", -1)
    # これらのパラメータをすべて含む文字列をハイフンで区切って構築
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

# 関数を呼び出して表示名を生成
pipeline_display_name = get_pipeline_display_name()
# 表示名を印刷
print(f"Display name used for the run: {pipeline_display_name}")
```
### パイプラインの設定

このPythonスクリプトは、Azure Machine Learning SDKを使用して機械学習パイプラインを定義および設定しています。以下はその詳細です：

1. Azure AI ML SDKから必要なモジュールをインポートします。

2. レジストリから"chat_completion_pipeline"という名前のパイプラインコンポーネントを取得します。

3. `@pipeline`デコレータと`create_pipeline`関数を使用してパイプラインジョブを定義します。パイプラインの名前は`pipeline_display_name`に設定されます。

4. `create_pipeline`関数内で、取得したパイプラインコンポーネントをさまざまなパラメータで初期化します。これには、モデルパス、異なるステージの計算クラスター、トレーニングおよびテスト用のデータセット分割、微調整に使用するGPUの数、およびその他の微調整パラメータが含まれます。

5. 微調整ジョブの出力をパイプラインジョブの出力にマッピングします。これにより、微調整されたモデルを簡単に登録できるようになります。モデルの登録は、モデルをオンラインまたはバッチエンドポイントにデプロイするために必要です。

6. `create_pipeline`関数を呼び出してパイプラインのインスタンスを作成します。

7. パイプラインの`force_rerun`設定を`True`に設定します。これにより、以前のジョブのキャッシュ結果が使用されません。

8. パイプラインの`continue_on_step_failure`設定を`False`に設定します。これにより、ステップが失敗した場合にパイプラインが停止します。

要約すると、このスクリプトはAzure Machine Learning SDKを使用してチャット補完タスク用の機械学習パイプラインを定義および設定しています。

```
# Azure AI ML SDKから必要なモジュールをインポート
from azure.ai.ml.dsl import pipeline
from azure.ai.ml import Input

# レジストリから"chat_completion_pipeline"という名前のパイプラインコンポーネントを取得
pipeline_component_func = registry_ml_client.components.get(
    name="chat_completion_pipeline", label="latest"
)

# @pipelineデコレータとcreate_pipeline関数を使用してパイプラインジョブを定義
# パイプラインの名前はpipeline_display_nameに設定
@pipeline(name=pipeline_display_name)
def create_pipeline():
    # 取得したパイプラインコンポーネントをさまざまなパラメータで初期化
    # これには、モデルパス、異なるステージの計算クラスター、トレーニングおよびテスト用のデータセット分割、微調整
```
# Azure AI ML SDKから必要なモジュールをインポート
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes

# パイプラインジョブから`trained_model`出力が利用可能か確認
print("パイプラインジョブの出力: ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)

# パイプラインジョブの名前と出力名("trained_model")を使って、学習済みモデルへのパスを構築
model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
    pipeline_job.name, "trained_model"
)

# 元のモデル名に"-ultrachat-200k"を追加し、スラッシュをハイフンに置き換えて、ファインチューニングされたモデルの名前を定義
finetuned_model_name = model_name + "-ultrachat-200k"
finetuned_model_name = finetuned_model_name.replace("/", "-")

print("モデル登録のパス: ", model_path_from_job)

# さまざまなパラメータを使ってModelオブジェクトを作成し、モデルを登録する準備
# これにはモデルのパス、モデルのタイプ（MLflowモデル）、モデルの名前とバージョン、モデルの説明が含まれる
prepare_to_register_model = Model(
    path=model_path_from_job,
    type=AssetTypes.MLFLOW_MODEL,
    name=finetuned_model_name,
    version=timestamp,  # バージョンの競合を避けるためにタイムスタンプをバージョンとして使用
    description=model_name + " ultrachat 200kチャット完了用のファインチューニングモデル",
)

print("モデル登録の準備: \n", prepare_to_register_model)

# Modelオブジェクトを引数にして、workspace_ml_clientのmodelsオブジェクトのcreate_or_updateメソッドを呼び出し、モデルを登録
registered_model = workspace_ml_client.models.create_or_update(
    prepare_to_register_model
)

# 登録されたモデルを出力
print("登録されたモデル: \n", registered_model)
```
## 7. 微調整されたモデルをオンラインエンドポイントにデプロイ
オンラインエンドポイントは、モデルを使用するアプリケーションと統合するために使用できる持続可能なREST APIを提供します。

### エンドポイント管理
このPythonスクリプトは、Azure Machine Learningで登録されたモデルのための管理されたオンラインエンドポイントを作成します。以下はその概要です：

Azure AI ML SDKから必要なモジュールをインポートします。

エンドポイントの名前にタイムスタンプを付加して、一意の名前を定義します。

ManagedOnlineEndpointオブジェクトを作成して、エンドポイントの名前、説明、認証モード（"key"）などのパラメータを設定します。

workspace_ml_clientのbegin_create_or_updateメソッドを呼び出して、ManagedOnlineEndpointオブジェクトを引数にしてエンドポイントを作成します。waitメソッドを呼び出して、作成操作が完了するのを待ちます。

要約すると、このスクリプトはAzure Machine Learningで登録されたモデルのための管理されたオンラインエンドポイントを作成しています。

```
# Azure AI ML SDKから必要なモジュールをインポート
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    ProbeSettings,
    OnlineRequestSettings,
)

# タイムスタンプを付加して、エンドポイントの一意の名前を定義
online_endpoint_name = "ultrachat-completion-" + timestamp

# ManagedOnlineEndpointオブジェクトを作成して、エンドポイントの名前、説明、認証モード（"key"）などのパラメータを設定
endpoint = ManagedOnlineEndpoint(
    name=online_endpoint_name,
    description="Online endpoint for "
    + registered_model.name
    + ", fine tuned model for ultrachat-200k-chat-completion",
    auth_mode="key",
)

# workspace_ml_clientのbegin_create_or_updateメソッドを呼び出してエンドポイントを作成し、waitメソッドを呼び出して作成操作が完了するのを待つ
workspace_ml_client.begin_create_or_update(endpoint).wait()
```
デプロイに対応しているSKUのリストはこちらで確認できます - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### MLモデルのデプロイ

このPythonスクリプトは、Azure Machine Learningで登録された機械学習モデルを管理されたオンラインエンドポイントにデプロイします。以下はその概要です：

astモジュールをインポートします。このモジュールは、Pythonの抽象構文木を処理するための関数を提供します。

デプロイのインスタンスタイプを"Standard_NC6s_v3"に設定します。

foundation_modelにinference_compute_allow_listタグが存在するか確認します。存在する場合、タグの値を文字列からPythonリストに変換し、inference_computes_allow_listに割り当てます。存在しない場合、inference_computes_allow_listをNoneに設定します。

指定されたインスタンスタイプが許可リストに含まれているか確認します。含まれていない場合、ユーザーに許可リストからインスタンスタイプを選択するようメッセージを表示します。

ManagedOnlineDeploymentオブジェクトを作成して、デプロイの名前、エンドポイントの名前、モデルのID、インスタンスタイプと数、稼働状態のプローブ設定、リクエスト設定などのパラメータを設定します。

workspace_ml_clientのbegin_create_or_updateメソッドを呼び出してデプロイを作成し、waitメソッドを呼び出して作成操作が完了するのを待ちます。

エンドポイントのトラフィックを100% "demo" デプロイに向けるように設定します。

workspace_ml_clientのbegin_create_or_updateメソッドを呼び出してエンドポイントを更新し、resultメソッドを呼び出して更新操作が完了するのを待ちます。

要約すると、このスクリプトはAzure Machine Learningで登録された機械学習モデルを管理されたオンラインエンドポイントにデプロイしています。

```
# astモジュールをインポート
import ast

# デプロイのインスタンスタイプを設定
instance_type = "Standard_NC6s_v3"

# foundation_modelに`inference_compute_allow_list`タグが存在するか確認
if "inference_compute_allow_list" in foundation_model.tags:
    # 存在する場合、タグの値を文字列からPythonリストに変換し、`inference_computes_allow_list`に割り当て
    inference_computes_allow_list = ast.literal_eval(
        foundation_model.tags["inference_compute_allow_list"]
    )
    print(f"Please create a compute from the above list - {computes_allow_list}")
else:
    # 存在しない場合、`inference_computes_allow_list`を`None`に設定
    inference_computes_allow_list = None
    print("`inference_compute_allow_list` is not part of model tags")

# 指定されたインスタンスタイプが許可リストに含まれているか確認
if (
    inference_computes_allow_list is not None
    and instance_type not in inference_computes_allow_list
):
    print(
        f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
    )

# ManagedOnlineDeploymentオブジェクトを作成して、デプロイの名前、エンドポイントの名前、モデルのID、インスタンスタイプと数、稼働状態のプローブ設定、リクエスト設定などのパラメータを設定
demo_deployment = ManagedOnlineDeployment(
    name="demo",
    endpoint_name=online_endpoint_name,
    model=registered_model.id,
    instance_type=instance_type,
    instance_count=1,
    liveness_probe=ProbeSettings(initial_delay=600),
    request_settings=OnlineRequestSettings(request_timeout_ms=90000),
)

# workspace_ml_clientのbegin_create_or_updateメソッドを呼び出してデプロイを作成し、waitメソッドを呼び出して作成操作が完了するのを待つ
workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()

# エンドポイントのトラフィックを100% "demo" デプロイに向けるように設定
endpoint.traffic = {"demo": 100}

# workspace_ml_clientのbegin_create_or_updateメソッドを呼び出してエンドポイントを更新し、resultメソッドを呼び出して更新操作が完了するのを待つ
workspace_ml_client.begin_create_or_update(endpoint).result()
```
## 8. サンプルデータでエンドポイントをテスト
テストデータセットからいくつかのサンプルデータを取得し、オンラインエンドポイントに送信して推論を行います。推論結果と実際のラベルを並べて表示します。

### 結果の読み取り
このPythonスクリプトは、JSON Linesファイルをpandas DataFrameに読み込み、ランダムサンプルを取得し、インデックスをリセットします。以下はその概要です：

./ultrachat_200k_dataset/test_gen.jsonlファイルをpandas DataFrameに読み込みます。read_json関数をlines=True引数とともに使用します。このファイルはJSON Lines形式で、各行が個別のJSONオブジェクトになっています。

DataFrameから1行のランダムサンプルを取得します。sample関数をn=1引数とともに使用して、選択するランダム行の数を指定します。

DataFrameのインデックスをリセットします。reset_index関数をdrop=True引数とともに使用して、元のインデックスを削除し、新しいデフォルトの整数値のインデックスに置き換えます。

head関数を使用してDataFrameの最初の2行を表示します。ただし、サンプリング後のDataFrameは1行しか含まれていないため、この1行のみが表示されます。

要約すると、このスクリプトはJSON Linesファイルをpandas DataFrameに読み込み、1行のランダムサンプルを取得し、インデックスをリセットし、最初の行を表示します。

```
# pandasライブラリをインポート
import pandas as pd

# JSON Linesファイル'./ultrachat_200k_dataset/test_gen.jsonl'をpandas DataFrameに読み込む
# 'lines=True'引数は、ファイルが各行が個別のJSONオブジェクトであるJSON Lines形式であることを示します
test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)

# DataFrameから1行のランダムサンプルを取得
# 'n=1'引数は、選択するランダム行の数を指定します
test_df = test_df.sample(n=1)

# DataFrameのインデックスをリセット
# 'drop=True'引数は、元のインデックスを削除し、新しいデフォルトの整数値のインデックスに置き換えることを示します
# 'inplace=True'引数は、DataFrameをその場で修正することを示します（新しいオブジェクトを作成せずに）
test_df.reset_index(drop=True, inplace=True)

# DataFrameの最初の2行を表示
# ただし、サンプリング後のDataFrameは1行しか含まれていないため、この1行のみが表示されます
test_df.head(2)
```
### JSONオブジェクトの作成

このPythonスクリプトは、特定のパラメータを持つJSONオブジェクトを作成し、それをファイルに保存します。以下はその概要です：

jsonモジュールをインポートします。このモジュールは、JSONデータを操作するための関数を提供します。

パラメータを持つ辞書parametersを作成します。キーは"temperature"、"top_p"、"do_sample"、"max_new_tokens"で、それぞれの値は0.6、0.9、True、200です。

もう一つの辞書test_jsonを作成します。この辞書には"input_data"と"params"の2つのキーがあります。"input_data"の値は、"input_string"と"parameters"のキーを持つ辞書です。"input_string"の値はtest_df DataFrameの最初のメッセージを含むリストです。"parameters"の値は先ほど作成したparameters辞書です。"params"の値は空の辞書です。

sample_score.jsonという名前のファイルを開きます。

```
# JSONデータを操作するための関数を提供するjsonモジュールをインポート
import json

# パラメータを持つ辞書`parameters`を作成
# キーは"temperature"、"top_p"、"do_sample"、"max_new_tokens"で、それぞれの値は0.6、0.9、True、200です
parameters = {
    "temperature": 0.6,
    "top_p": 0.9,
    "do_sample": True,
    "max_new_tokens": 200,
}

# もう一つの辞書`test_json`を作成
# この辞書には"input_data"と"params"の2つのキーがあります
# "input_data"の値は、"input_string"と"parameters"のキーを持つ辞書です
# "input_string"の値はtest_df DataFrameの最初のメッセージを含むリストです
# "parameters"の値は先ほど作成した`parameters`辞書です
# "params"の値は空の辞書です
test_json = {
    "input_data": {
        "input_string": [test_df["messages"][0]],
        "parameters": parameters,
    },
    "params": {},
}

# ./ultrachat_200k_datasetディレクトリにあるsample_score.jsonという名前のファイルを開く
with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
    # json.dump関数を使用して、`test_json`辞書をJSON形式でファイルに書き込む
    json.dump(test_json, f)
```
### エンドポイントの呼び出し

このPythonスクリプトは、Azure Machine Learningのオンラインエンドポイントを呼び出してJSONファイルをスコアリングします。以下はその概要です：

workspace_ml_clientオブジェクトのonline_endpointsプロパティのinvokeメソッドを呼び出します。このメソッドは、オンラインエンドポイントにリクエストを送信してレスポンスを取得するために使用されます。

endpoint_nameおよびdeployment_name引数でエンドポイントとデプロイの名前を指定します。この場合、エンドポイント名はonline_endpoint_name変数に格納され、デプロイ名は"demo"です。

request_file引数でスコアリングするJSONファイルのパスを指定します。この場合、ファイルは./ultrachat_200k_dataset/sample_score.jsonです。

エンドポイントからのレスポンスをresponse変数に格納します。

生のレスポンスを出力します。

要約すると、このスクリプトはAzure Machine Learningのオンラインエンドポイントを呼び出してJSONファイルをスコアリングし、レスポンスを出力します。

```
# Azure Machine Learningのオンラインエンドポイントを呼び出してsample_score.jsonファイルをスコアリング
# workspace_ml_clientオブジェクトのonline_endpointsプロパティのinvokeメソッドを使用して、オンラインエンドポイントにリクエストを送信してレスポンスを取得
# endpoint_name引数でエンドポイントの名前を指定し、これはonline_endpoint_name変数に格納
# deployment_name引数でデプロイの名前を指定し、これは"demo"
# request_file引数でスコアリングするJSONファイルのパスを指定し、これは./ultrachat_200k_dataset/sample_score.json
response = workspace_ml_client.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    deployment_name="demo",
    request_file="./ultrachat_200k_dataset/sample_score.json",
)

# エンドポイントからの生のレスポンスを出力
print("raw response: \n", response, "\n")
```
## 9. オンラインエンドポイントの削除
オンラインエンドポイントを削除しないと、エンドポイントで使用されるコンピュートの課金メーターが動き続けるので注意してください。このPythonコードは、Azure Machine Learningでオンラインエンドポイントを削除します。以下はその概要です：

workspace_ml_clientオブジェクトのonline_endpointsプロパティのbegin_deleteメソッドを呼び出します。このメソッドは、オンラインエンドポイントの削除を開始するために使用されます。

name引数で削除するエンドポイントの名前を指定します。この場合、エンドポイント名はonline_endpoint_name変数に格納されています。

waitメソッドを呼び出して削除操作が完了するのを待ちます。これはブロッキング操作であり、削除が完了するまでスクリプトの実行を続行しません。

要約すると、このコードはAzure Machine Learningでオンラインエンドポイントの削除を開始し、操作が完了するのを待ちます。

```
# Azure Machine Learningでオンラインエンドポイントを削除
# workspace_ml_clientオブジェクトのonline_endpointsプロパティのbegin_deleteメソッドを使用して、オンラインエンドポイントの削除を開始
# name引数で削除するエンドポイントの名前を指定し、これはonline_endpoint_name変数に格納
# waitメソッドを呼び出して削除操作が完了するのを待つ。これはブロッキング操作であり、削除が完了するまでスクリプトの実行を続行しません
workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
```

免責事項：この翻訳はAIモデルによって元の文章から翻訳されたものであり、完璧ではない可能性があります。
出力を確認し、必要な修正を行ってください。