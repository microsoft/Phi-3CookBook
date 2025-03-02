## Azure MLシステムレジストリのチャット補完コンポーネントを使用してモデルを微調整する方法

この例では、ultrachat_200kデータセットを使用して、2人の会話を完了させるためのPhi-3-mini-4k-instructモデルの微調整を行います。

![MLFineTune](../../../../translated_images/MLFineTune.d8292fe1f146b4ff1153c2e5bdbbe5b0e7f96858d5054b525bd55f2641505138.ja.png)

この例では、Azure ML SDKとPythonを使用して微調整を行い、その後、微調整されたモデルをオンラインエンドポイントにデプロイしてリアルタイム推論を行う方法を示します。

### トレーニングデータ

ultrachat_200kデータセットを使用します。このデータセットはUltraChatデータセットの厳選されたバージョンで、最先端の7BチャットモデルであるZephyr-7B-βのトレーニングに使用されました。

### モデル

Phi-3-mini-4k-instructモデルを使用して、チャット補完タスクのためのモデル微調整の方法を示します。このノートブックを特定のモデルカードから開いた場合は、該当するモデル名に置き換えてください。

### タスク

- 微調整するモデルを選択する
- トレーニングデータを選択して探索する
- 微調整ジョブを設定する
- 微調整ジョブを実行する
- トレーニングおよび評価メトリクスを確認する
- 微調整されたモデルを登録する
- 微調整されたモデルをリアルタイム推論のためにデプロイする
- リソースをクリーンアップする

## 1. 事前準備のセットアップ

- 依存関係をインストールする
- AzureMLワークスペースに接続する。SDK認証の設定についてはこちらを参照してください。以下の<WORKSPACE_NAME>、<RESOURCE_GROUP>、<SUBSCRIPTION_ID>を置き換えてください。
- azuremlシステムレジストリに接続する
- オプションで実験名を設定する
- コンピュートを確認または作成する

> [!NOTE]
> 要件: 単一のGPUノードには複数のGPUカードが含まれる場合があります。たとえば、Standard_NC24rs_v3の1ノードには4つのNVIDIA V100 GPUがあり、Standard_NC12s_v3には2つのNVIDIA V100 GPUがあります。この情報についてはドキュメントを参照してください。以下のパラメータgpus_per_nodeでノードごとのGPUカード数を設定します。この値を正しく設定することで、ノード内のすべてのGPUを活用できます。推奨されるGPUコンピュートSKUは[こちら](../../../../md/03.FineTuning/リンク)と[こちら](../../../../md/03.FineTuning/リンク)で確認できます。

### Pythonライブラリ

以下のセルを実行して依存関係をインストールします。新しい環境で実行する場合、この手順は省略できません。

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Azure MLとの対話

1. このPythonスクリプトはAzure Machine Learning (Azure ML)サービスと対話するために使用されます。以下はその内容の概要です：

    - azure.ai.ml、azure.identity、azure.ai.ml.entitiesパッケージから必要なモジュールをインポートします。また、timeモジュールもインポートします。

    - DefaultAzureCredential()を使用して認証を試みます。これはAzureクラウドでのアプリケーション開発を迅速に開始するための簡略化された認証体験を提供します。これが失敗した場合、InteractiveBrowserCredential()にフォールバックします。これにより、インタラクティブなログインプロンプトが提供されます。

    - from_configメソッドを使用してMLClientインスタンスを作成し、デフォルトの設定ファイル（config.json）から構成を読み取ります。これが失敗した場合、subscription_id、resource_group_name、workspace_nameを手動で指定してMLClientインスタンスを作成します。

    - "azureml"という名前のAzure MLレジストリ用にもう1つのMLClientインスタンスを作成します。このレジストリには、モデル、微調整パイプライン、環境が格納されています。

    - 実験名を"chat_completion_Phi-3-mini-4k-instruct"に設定します。

    - 現在の時刻（エポック秒）を浮動小数点数として取得し、整数に変換した後に文字列に変換してユニークなタイムスタンプを生成します。このタイムスタンプは、ユニークな名前やバージョンを作成するために使用できます。

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

## 2. 微調整する基盤モデルを選択する

1. Phi-3-mini-4k-instructは3.8Bパラメータの軽量で最先端のオープンモデルであり、Phi-2で使用されたデータセットを基に構築されています。このモデルはPhi-3モデルファミリーに属しており、Miniバージョンには4Kと128Kの2つのバリアントがあり、サポートできるコンテキスト長（トークン数）が異なります。このモデルを使用するには、特定の目的に合わせて微調整する必要があります。これらのモデルはAzureML Studioのモデルカタログでチャット補完タスクでフィルタリングして閲覧できます。この例ではPhi-3-mini-4k-instructモデルを使用します。異なるモデル用にノートブックを開いた場合は、モデル名とバージョンを適宜置き換えてください。

    > [!NOTE]
    > モデルのプロパティであるmodel idは、微調整ジョブへの入力として渡されます。これはAzureML Studioのモデルカタログ内のモデル詳細ページでAsset IDフィールドとしても確認できます。

2. このPythonスクリプトはAzure Machine Learning (Azure ML)サービスと対話しています。以下はその内容の概要です：

    - model_nameを"Phi-3-mini-4k-instruct"に設定します。

    - registry_ml_clientオブジェクトのmodelsプロパティのgetメソッドを使用して、指定された名前のモデルの最新バージョンをAzure MLレジストリから取得します。getメソッドは、モデル名と最新バージョンを指定するラベルの2つの引数を受け取ります。

    - 微調整に使用するモデルの名前、バージョン、idをコンソールに出力します。formatメソッドを使用して、モデルの名前、バージョン、idをメッセージに挿入します。モデルの名前、バージョン、idはfoundation_modelオブジェクトのプロパティとしてアクセスされます。

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

## 3. ジョブで使用するコンピュートを作成する

微調整ジョブはGPUコンピュートでのみ動作します。コンピュートのサイズはモデルの規模に依存し、多くの場合、ジョブに適したコンピュートを特定するのが難しくなります。このセクションでは、ユーザーがジョブに適したコンピュートを選択できるようガイドします。

> [!NOTE]
> 以下にリストされているコンピュートは最適化された構成で動作します。構成を変更するとCuda Out Of Memoryエラーが発生する可能性があります。その場合は、より大きなコンピュートサイズにアップグレードしてみてください。

> [!NOTE]
> 以下でcompute_cluster_sizeを選択する際、コンピュートがリソースグループ内で利用可能であることを確認してください。特定のコンピュートが利用できない場合は、リソースへのアクセスをリクエストできます。

### 微調整サポートの確認

1. このPythonスクリプトはAzure Machine Learning (Azure ML)モデルと対話しています。以下はその内容の概要です：

    - astモジュールをインポートします。このモジュールはPythonの抽象構文木を処理するための関数を提供します。

    - foundation_modelオブジェクト（Azure ML内のモデルを表す）がfinetune_compute_allow_listというタグを持っているか確認します。Azure MLのタグは、モデルをフィルタリングおよびソートするために使用できるキーと値のペアです。

    - finetune_compute_allow_listタグが存在する場合、その値（文字列）をast.literal_eval関数を使用して安全にPythonリストに変換します。このリストはcomputes_allow_list変数に割り当てられます。その後、このリストからコンピュートを作成するようメッセージを表示します。

    - finetune_compute_allow_listタグが存在しない場合、computes_allow_listをNoneに設定し、モデルのタグにfinetune_compute_allow_listタグが含まれていないことを示すメッセージを表示します。

    - 要約すると、このスクリプトはモデルのメタデータ内の特定のタグを確認し、その値をリストに変換して、ユーザーにフィードバックを提供しています。

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

### コンピュートインスタンスの確認

1. このPythonスクリプトはAzure Machine Learning (Azure ML)サービスと対話し、コンピュートインスタンスに対していくつかのチェックを行います。以下はその内容の概要です：

    - compute_clusterに格納された名前を持つコンピュートインスタンスをAzure MLワークスペースから取得しようとします。コンピュートインスタンスのプロビジョニング状態が"failed"の場合、ValueErrorを発生させます。

    - computes_allow_listがNoneでない場合、そのリスト内のすべてのコンピュートサイズを小文字に変換し、現在のコンピュートインスタンスのサイズがリスト内にあるか確認します。リスト内にない場合、ValueErrorを発生させます。

    - computes_allow_listがNoneの場合、現在のコンピュートインスタンスのサイズがサポートされていないGPU VMサイズのリスト内にあるか確認します。リスト内にある場合、ValueErrorを発生させます。

    - ワークスペース内のすべての利用可能なコンピュートサイズのリストを取得します。このリストを反復処理し、現在のコンピュートインスタンスのサイズと一致するものがあれば、そのサイズに対応するGPUの数を取得し、gpu_count_foundをTrueに設定します。

    - gpu_count_foundがTrueの場合、コンピュートインスタンス内のGPUの数を表示します。gpu_count_foundがFalseの場合、ValueErrorを発生させます。

    - 要約すると、このスクリプトはAzure MLワークスペース内のコンピュートインスタンスに対して、プロビジョニング状態、許可リストまたは禁止リストとの一致、GPUの数などのチェックを行っています。

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

## 4. 微調整用データセットを選択する

1. ultrachat_200kデータセットを使用します。このデータセットには、Supervised fine-tuning (sft)やGeneration ranking (gen)に適した4つのスプリットがあります。それぞれのスプリットに含まれる例の数は以下の通りです：

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. 次のいくつかのセルでは、微調整のための基本的なデータ準備を示します：

### データ行の可視化

このサンプルを迅速に実行するため、すでにトリミングされた行の5％を含むtrain_sft、test_sftファイルを保存します。これにより、微調整されたモデルの精度は低くなるため、実際の用途には適しません。
download-dataset.pyは、ultrachat_200kデータセットをダウンロードし、データセットを微調整パイプラインコンポーネントで使用可能な形式に変換するために使用されます。また、データセットが大きいため、ここではデータセットの一部のみを使用しています。

1. 以下のスクリプトを実行すると、データの5％のみがダウンロードされます。この割合はdataset_split_pcパラメータを希望する割合に変更することで増加させることができます。

    > [!NOTE]
    > 一部の言語モデルには異なる言語コードがあり、そのためデータセット内の列名もそれに応じて反映する必要があります。

1. データがどのように見えるべきかの例を以下に示します：
チャット補完データセットはparquet形式で保存されており、各エントリは以下のスキーマを使用しています：

    - JSON（JavaScript Object Notation）形式のドキュメントです。これはデータ交換フォーマットとして広く使用されています。以下はその構造の概要です：

    - "prompt": AIアシスタントに対して提起されたタスクや質問を表す文字列値を保持します。

    - "messages": ユーザーとAIアシスタントの間の会話のメッセージを表すオブジェクトの配列を保持します。各メッセージオブジェクトには以下の2つのキーがあります：
      - "content": メッセージの内容を表す文字列値を保持します。
      - "role": メッセージを送信したエンティティの役割を表す文字列値を保持します（"user"または"assistant"）。

    - "prompt_id": プロンプトの一意識別子を表す文字列値を保持します。

1. この特定のJSONドキュメントでは、ユーザーがAIアシスタントにディストピア物語の主人公を作成するよう依頼し、アシスタントが応答し、その後ユーザーがさらに詳細を求め、アシスタントが詳細を提供することを約束する会話が表現されています。この会話全体は特定のprompt idに関連付けられています。

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

### データのダウンロード

1. このPythonスクリプトは、download-dataset.pyというヘルパースクリプトを使用してデータセットをダウンロードします。以下はその内容の概要です：

    - osモジュールをインポートします。これは、オペレーティングシステムに依存する機能を移植性のある方法で使用するためのものです。

    - os.system関数を使用して、download-dataset.pyスクリプトを特定のコマンドライン引数付きでシェルで実行します。引数は、ダウンロードするデータセット（HuggingFaceH4/ultrachat_200k）、ダウンロード先ディレクトリ（ultrachat_200k_dataset）、およびデータセットの分割割合（5）を指定します。os.system関数は、実行したコマンドの終了ステータスを返します。このステータスはexit_status変数に格納されます。

    - exit_statusが0でない場合を確認します。Unix系のオペレーティングシステムでは、終了ステータスが0である場合、通常はコマンドが成功したことを示し、それ以外の数値はエラーを示します。exit_statusが0でない場合、データセットのダウンロード中にエラーが発生したことを示すメッセージを持つ例外を発生させます。

    - 要約すると、このスクリプトはヘルパースクリプトを使用してデータセットをダウンロードするコマンドを実行し、コマンドが失敗した場合に例外を発生させます。

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

### データをDataFrameにロードする

1. このPythonスクリプトは、JSON Linesファイルをpandas DataFrameにロードし、最初の5行を表示します。以下はその内容の概要です：

    - pandasライブラリをインポートします。これは、強力なデータ操作と分析ライブラリです。

    - pandasの表示オプションの最大列幅を0に設定します。これにより、DataFrameが表示されるときに各列のテキスト全体が切り捨てられずに表示されます。

    - pd.read_json関数を使用して、ultrachat_200k_datasetディレクトリ内のtrain_sft.jsonlファイルをDataFrameにロードします。lines=True引数は、ファイルがJSON Lines形式であることを示します。この形式では、各行が個別のJSONオブジェクトです。

    - headメソッドを使用して、DataFrameの最初の5行を表示します。DataFrameに5行未満しかない場合は、すべての行を表示します。

    - 要約すると、このスクリプトはJSON LinesファイルをDataFrameにロードし、最初の5行を完全な列テキストで表示します。

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

## 5. モデルとデータを入力として微調整ジョブを送信する

チャット補完パイプラインコンポーネントを使用するジョブを作成します。サポートされるすべてのパラメータについてはこちらを参照してください。

### 微調整パラメ
トレーニングパイプラインをさまざまなパラメータに基づいて構築し、その表示名を出力します。  
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

### パイプラインの設定  

このPythonスクリプトは、Azure Machine Learning SDKを使用して機械学習パイプラインを定義および設定しています。以下はその内容の概要です：  

1. Azure AI ML SDKから必要なモジュールをインポートします。  
1. レジストリから "chat_completion_pipeline" という名前のパイプラインコンポーネントを取得します。  
1. `@pipeline` decorator and the function `create_pipeline`. The name of the pipeline is set to `pipeline_display_name`.

1. Inside the `create_pipeline` function, it initializes the fetched pipeline component with various parameters, including the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters.

1. It maps the output of the fine-tuning job to the output of the pipeline job. This is done so that the fine-tuned model can be easily registered, which is required to deploy the model to an online or batch endpoint.

1. It creates an instance of the pipeline by calling the `create_pipeline` function.

1. It sets the `force_rerun` setting of the pipeline to `True`, meaning that cached results from previous jobs will not be used.

1. It sets the `continue_on_step_failure` setting of the pipeline to `False` を使用してパイプラインジョブを定義します。これにより、ステップが失敗した場合にパイプラインが停止するよう設定されます。  
1. 要約すると、このスクリプトはAzure Machine Learning SDKを使用してチャット補完タスク用の機械学習パイプラインを定義および設定しています。  

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

### ジョブの送信  

1. このPythonスクリプトは、Azure Machine Learningのワークスペースに機械学習パイプラインジョブを送信し、ジョブが完了するまで待機します。以下はその内容の概要です：  

   - `workspace_ml_client` オブジェクトの `jobs` プロパティの `create_or_update` メソッドを呼び出し、パイプラインジョブを送信します。実行するパイプラインは `pipeline_object` で指定され、ジョブが実行される実験は `experiment_name` で指定されます。  
   - 次に、`workspace_ml_client` オブジェクトの `jobs` プロパティの `stream` メソッドを呼び出し、パイプラインジョブが完了するのを待ちます。待機するジョブは `pipeline_job` オブジェクトの `name` 属性で指定されます。  
   - 要約すると、このスクリプトはAzure Machine Learningのワークスペースに機械学習パイプラインジョブを送信し、ジョブが完了するのを待機します。  

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

## 6. 微調整済みモデルをワークスペースに登録する  

微調整ジョブの出力からモデルを登録します。これにより、微調整済みモデルと微調整ジョブの間の系譜が追跡されます。さらに、微調整ジョブは基盤モデル、データ、トレーニングコードとの系譜も追跡します。  

### 機械学習モデルの登録  

1. このPythonスクリプトは、Azure Machine Learningパイプラインでトレーニングされた機械学習モデルを登録しています。以下はその内容の概要です：  

   - Azure AI ML SDKから必要なモジュールをインポートします。  
   - `workspace_ml_client` オブジェクトの `jobs` プロパティの `get` メソッドを呼び出し、その `outputs` 属性にアクセスすることで、パイプラインジョブからの `trained_model` 出力が利用可能かどうかを確認します。  
   - パイプラインジョブの名前と出力名 ("trained_model") を使用して、トレーニング済みモデルへのパスを構築します。  
   - 元のモデル名に "-ultrachat-200k" を追加し、スラッシュをハイフンに置き換えることで、微調整済みモデルの名前を定義します。  
   - モデルへのパス、モデルの種類 (MLflowモデル)、モデルの名前とバージョン、モデルの説明など、さまざまなパラメータを含むModelオブジェクトを作成して登録の準備をします。  
   - `workspace_ml_client` オブジェクトの `models` プロパティの `create_or_update` メソッドを呼び出し、Modelオブジェクトを引数として渡すことでモデルを登録します。  
   - 登録されたモデルを出力します。  

1. 要約すると、このスクリプトはAzure Machine Learningパイプラインでトレーニングされた機械学習モデルを登録しています。  

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

## 7. 微調整済みモデルをオンラインエンドポイントにデプロイする  

オンラインエンドポイントは、モデルを使用するアプリケーションと統合するための持続可能なREST APIを提供します。  

### エンドポイントの管理  

1. このPythonスクリプトは、登録済みモデルのためにAzure Machine Learningで管理されたオンラインエンドポイントを作成しています。以下はその内容の概要です：  

   - Azure AI ML SDKから必要なモジュールをインポートします。  
   - 現在のタイムスタンプを "ultrachat-completion-" という文字列に追加することで、オンラインエンドポイントの一意の名前を定義します。  
   - エンドポイントの名前、説明、認証モード ("key") を含むさまざまなパラメータを指定して、ManagedOnlineEndpointオブジェクトを作成します。  
   - `workspace_ml_client` オブジェクトの `begin_create_or_update` メソッドを呼び出し、ManagedOnlineEndpointオブジェクトを引数として渡すことでオンラインエンドポイントを作成します。その後、`wait` メソッドを呼び出して作成操作が完了するのを待ちます。  

1. 要約すると、このスクリプトは登録済みモデルのためにAzure Machine Learningで管理されたオンラインエンドポイントを作成しています。  

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
> デプロイに対応しているSKUの一覧はこちらで確認できます - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)  

### 機械学習モデルのデプロイ  

1. このPythonスクリプトは、登録済みの機械学習モデルをAzure Machine Learningの管理されたオンラインエンドポイントにデプロイしています。以下はその内容の概要です：  

   - Pythonの抽象構文木を処理するための関数を提供するastモジュールをインポートします。  
   - デプロイに使用するインスタンスタイプを "Standard_NC6s_v3" に設定します。  
   - 基盤モデルに `inference_compute_allow_list` タグが存在するか確認します。存在する場合、その値を文字列からPythonリストに変換し、`inference_computes_allow_list` に割り当てます。存在しない場合、`inference_computes_allow_list` をNoneに設定します。  
   - 指定されたインスタンスタイプが許可リストに含まれているか確認します。含まれていない場合、ユーザーに許可リストからインスタンスタイプを選択するよう促すメッセージを表示します。  
   - デプロイの名前、エンドポイントの名前、モデルのID、インスタンスタイプとカウント、稼働状況プローブ設定、リクエスト設定など、さまざまなパラメータを指定してManagedOnlineDeploymentオブジェクトを作成し、デプロイの準備をします。  
   - `workspace_ml_client` オブジェクトの `begin_create_or_update` メソッドを呼び出し、ManagedOnlineDeploymentオブジェクトを引数として渡すことでデプロイを作成します。その後、`wait` メソッドを呼び出して作成操作が完了するのを待ちます。  
   - エンドポイントのトラフィックを "demo" デプロイに100%割り当てるよう設定します。  
   - `workspace_ml_client` オブジェクトの `begin_create_or_update` メソッドを呼び出し、エンドポイントオブジェクトを引数として渡すことでエンドポイントを更新します。その後、`result` メソッドを呼び出して更新操作が完了するのを待ちます。  

1. 要約すると、このスクリプトは登録済みの機械学習モデルをAzure Machine Learningの管理されたオンラインエンドポイントにデプロイしています。  

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

## 8. サンプルデータを使用してエンドポイントをテストする  

テストデータセットからサンプルデータを取得し、オンラインエンドポイントに送信して推論を行います。その後、スコアリングされたラベルと正解ラベルを並べて表示します。  

### 結果の読み込み  

1. このPythonスクリプトは、JSON Linesファイルをpandas DataFrameに読み込み、ランダムサンプルを取得してインデックスをリセットします。以下はその内容の概要です：  

   - ファイル `./ultrachat_200k_dataset/test_gen.jsonl` をpandas DataFrameに読み込みます。ファイルがJSON Lines形式（一行ごとに個別のJSONオブジェクトが存在）であるため、`read_json` 関数を `lines=True` 引数付きで使用します。  
   - DataFrameから1行のランダムサンプルを取得します。`sample` 関数を `n=1` 引数付きで使用して、ランダムに選択する行数を指定します。  
   - DataFrameのインデックスをリセットします。`reset_index` 関数を `drop=True` 引数付きで使用して、元のインデックスを削除し、デフォルトの整数値の新しいインデックスに置き換えます。  
   - `head` 関数に引数2を指定してDataFrameの最初の2行を表示します。ただし、サンプリング後のDataFrameには1行しか含まれないため、その1行のみが表示されます。  

1. 要約すると、このスクリプトはJSON Linesファイルをpandas DataFrameに読み込み、1行のランダムサンプルを取得してインデックスをリセットし、その最初の行を表示します。  

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

### JSONオブジェクトの作成  

1. このPythonスクリプトは、特定のパラメータを持つJSONオブジェクトを作成し、ファイルに保存します。以下はその内容の概要です：  

   - JSONデータを扱うための関数を提供するjsonモジュールをインポートします。  
   - キーと値で構成される辞書 `parameters` を作成します。この辞書は機械学習モデルのパラメータを表し、キーは "temperature"、"top_p"、"do_sample"、"max_new_tokens"、対応する値はそれぞれ0.6、0.9、True、200です。  
   - もう一つの辞書 `test_json` を作成し、キー "input_data" と "params" を持たせます。"input_data" の値はさらに辞書で、キー "input_string" と "parameters" を持ちます。"input_string" の値は `test_df` DataFrameの最初のメッセージを含むリストで、"parameters" の値は先ほど作成した `parameters` 辞書です。"params" の値は空の辞書です。  
   - ファイル `sample_score.json` を開きます。  

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

### エンドポイントの呼び出し  

1. このPythonスクリプトは、Azure Machine Learningのオンラインエンドポイントを呼び出してJSONファイルをスコアリングします。以下はその内容の概要です：  

   - `workspace_ml_client` オブジェクトの `online_endpoints` プロパティの `invoke` メソッドを呼び出します。このメソッドはオンラインエンドポイントにリクエストを送信し、レスポンスを取得するために使用されます。  
   - エンドポイント名とデプロイ名を `endpoint_name` および `deployment_name` 引数で指定します。この場合、エンドポイント名は `online_endpoint_name` 変数に格納され、デプロイ名は "demo" です。  
   - スコアリングするJSONファイルのパスを `request_file` 引数で指定します。この場合、ファイルは `./ultrachat_200k_dataset/sample_score.json` です。  
   - エンドポイントからのレスポンスを `response` 変数に格納します。  
   - 生のレスポンスを出力します。  

1. 要約すると、このスクリプトはAzure Machine Learningのオンラインエンドポイントを呼び出してJSONファイルをスコアリングし、レスポンスを出力します。  

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

## 9. オンラインエンドポイントの削除  

1. オンラインエンドポイントを削除するのを忘れないでください。削除しないと、エンドポイントで使用されるコンピュートリソースの課金が継続します。このPythonコードは、Azure Machine Learningでオンラインエンドポイントを削除しています。以下はその内容の概要です：  

   - `workspace_ml_client` オブジェクトの `online_endpoints` プロパティの `begin_delete` メソッドを呼び出します。このメソッドはオンラインエンドポイントの削除を開始するために使用されます。  
   - 削除するエンドポイントの名前を `name` 引数で指定します。この場合、エンドポイント名は `online_endpoint_name` 変数に格納されています。  
   - `wait` メソッドを呼び出して削除操作が完了するのを待ちます。これはブロッキング操作であり、削除が完了するまでスクリプトの実行を停止します。  
   - 要約すると、このコードはAzure Machine Learningでオンラインエンドポイントの削除を開始し、その操作が完了するのを待機します。  

```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```  

**免責事項**:  
本書類は、AIによる機械翻訳サービスを使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があることをご承知おきください。原文（元の言語で書かれた文書）が正式な情報源として優先されるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の利用に起因する誤解や誤訳について、当方は一切の責任を負いません。