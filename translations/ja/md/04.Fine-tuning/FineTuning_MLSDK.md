## Azure ML システムレジストリからチャット補完コンポーネントを使用してモデルを微調整する方法

この例では、ultrachat_200k データセットを使用して、2 人の会話を完了するために Phi-3-mini-4k-instruct モデルを微調整します。

![MLFineTune](../../../../translated_images/MLFineTune.d123c711c7564f898ded140931f7c1afda37029a6c396334a66081ba62213083.ja.png)

この例では、Azure ML SDK と Python を使用して微調整を行い、その後微調整されたモデルをオンラインエンドポイントにデプロイしてリアルタイム推論を行う方法を示します。

### トレーニングデータ

ultrachat_200k データセットを使用します。これは UltraChat データセットの厳選されたバージョンであり、最先端の 7b チャットモデルである Zephyr-7B-β のトレーニングに使用されました。

### モデル

Phi-3-mini-4k-instruct モデルを使用して、ユーザーがチャット補完タスク用にモデルを微調整する方法を示します。特定のモデルカードからこのノートブックを開いた場合は、特定のモデル名を置き換えることを忘れないでください。

### タスク

- 微調整するモデルを選ぶ
- トレーニングデータを選んで探索する
- 微調整ジョブを設定する
- 微調整ジョブを実行する
- トレーニングと評価のメトリクスを確認する
- 微調整されたモデルを登録する
- 微調整されたモデルをリアルタイム推論用にデプロイする
- リソースをクリーンアップする

## 1. 事前準備の設定

- 依存関係をインストールする
- AzureML ワークスペースに接続する。SDK 認証の設定についてはこちらをご覧ください。以下の <WORKSPACE_NAME>, <RESOURCE_GROUP>, <SUBSCRIPTION_ID> を置き換えてください。
- azureml システムレジストリに接続する
- オプションで実験名を設定する
- コンピュートを確認または作成する

> [!NOTE]
> 要件として、単一の GPU ノードには複数の GPU カードが搭載されている場合があります。例えば、Standard_NC24rs_v3 の 1 ノードには 4 つの NVIDIA V100 GPU があり、Standard_NC12s_v3 には 2 つの NVIDIA V100 GPU があります。この情報についてはドキュメントを参照してください。ノードごとの GPU カードの数は以下の gpus_per_node パラメータで設定されます。この値を正しく設定することで、ノード内のすべての GPU を利用することができます。推奨される GPU コンピュート SKU はここやここで見つけることができます。

### Python ライブラリ

以下のセルを実行して依存関係をインストールします。新しい環境で実行する場合、このステップは省略できません。

```bash
pip install azure-ai-ml
pip install azure-identity
pip install datasets==2.9.0
pip install mlflow
pip install azureml-mlflow
```

### Azure ML との対話

1. この Python スクリプトは、Azure Machine Learning (Azure ML) サービスと対話するために使用されます。以下はその内容の概要です：

    - azure.ai.ml、azure.identity、および azure.ai.ml.entities パッケージから必要なモジュールをインポートします。また、time モジュールもインポートします。

    - DefaultAzureCredential() を使用して認証を試みます。これにより、Azure クラウドでアプリケーションを迅速に開発するための簡略化された認証エクスペリエンスが提供されます。これが失敗した場合、InteractiveBrowserCredential() にフォールバックし、インタラクティブなログインプロンプトを提供します。

    - from_config メソッドを使用して、デフォルトの設定ファイル (config.json) から設定を読み取って MLClient インスタンスを作成しようとします。これが失敗した場合、subscription_id、resource_group_name、および workspace_name を手動で提供して MLClient インスタンスを作成します。

    - 今度は "azureml" という名前の Azure ML レジストリ用の別の MLClient インスタンスを作成します。このレジストリにはモデル、微調整パイプライン、および環境が格納されています。

    - experiment_name を "chat_completion_Phi-3-mini-4k-instruct" に設定します。

    - 現在の時刻 (エポックからの秒数を浮動小数点数として) を整数に変換し、それを文字列に変換して一意のタイムスタンプを生成します。このタイムスタンプは、一意の名前やバージョンを作成するために使用できます。

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

## 2. 微調整する基盤モデルを選ぶ

1. Phi-3-mini-4k-instruct は、Phi-2 用に使用されたデータセットに基づいて構築された、3.8B パラメータの軽量で最先端のオープンモデルです。このモデルは Phi-3 モデルファミリーに属しており、Mini バージョンは 4K と 128K の 2 つのバリアントがあり、サポートできるコンテキスト長 (トークン数) が異なります。特定の目的のためにモデルを微調整する必要があります。これらのモデルは、AzureML Studio のモデルカタログでチャット補完タスクでフィルタリングして参照できます。この例では、Phi-3-mini-4k-instruct モデルを使用します。別のモデルのためにこのノートブックを開いた場合は、モデル名とバージョンを適宜置き換えてください。

    > [!NOTE]
    > モデルの id プロパティ。この値は微調整ジョブの入力として渡されます。また、AzureML Studio モデルカタログのモデル詳細ページのアセット ID フィールドとしても利用できます。

2. この Python スクリプトは、Azure Machine Learning (Azure ML) サービスと対話しています。以下はその内容の概要です：

    - model_name を "Phi-3-mini-4k-instruct" に設定します。

    - registry_ml_client オブジェクトの models プロパティの get メソッドを使用して、Azure ML レジストリから指定された名前のモデルの最新バージョンを取得します。get メソッドは 2 つの引数を受け取ります：モデルの名前と、最新バージョンのモデルを取得することを指定するラベル。

    - 微調整に使用するモデルの名前、バージョン、および id をコンソールに表示するメッセージを出力します。format メソッドを使用して、モデルの名前、バージョン、および id をメッセージに挿入します。モデルの名前、バージョン、および id は、foundation_model オブジェクトのプロパティとしてアクセスされます。

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

微調整ジョブは GPU コンピュートでのみ動作します。コンピュートのサイズはモデルの大きさによって異なり、適切なコンピュートを特定するのが難しい場合が多いです。このセルでは、ユーザーがジョブに適したコンピュートを選択するためのガイドを提供します。

> [!NOTE]
> 以下にリストされているコンピュートは、最適化された構成で動作します。構成に変更を加えると、Cuda Out Of Memory エラーが発生する可能性があります。その場合は、より大きなコンピュートサイズにアップグレードしてみてください。

> [!NOTE]
> 以下の compute_cluster_size を選択する際には、リソースグループ内でコンピュートが利用可能であることを確認してください。特定のコンピュートが利用できない場合は、コンピュートリソースへのアクセスをリクエストすることができます。

### 微調整サポートのモデルの確認

1. この Python スクリプトは、Azure Machine Learning (Azure ML) モデルと対話しています。以下はその内容の概要です：

    - ast モジュールをインポートします。これは、Python の抽象構文木を処理するための関数を提供します。

    - foundation_model オブジェクト (Azure ML のモデルを表す) に finetune_compute_allow_list というタグがあるかどうかを確認します。Azure ML のタグは、作成してモデルをフィルタリングおよびソートするために使用できるキーと値のペアです。

    - finetune_compute_allow_list タグが存在する場合、そのタグの値 (文字列) を安全に Python のリストに変換するために ast.literal_eval 関数を使用します。このリストは computes_allow_list 変数に割り当てられます。その後、リストからコンピュートを作成するように指示するメッセージを表示します。

    - finetune_compute_allow_list タグが存在しない場合、computes_allow_list を None に設定し、finetune_compute_allow_list タグがモデルのタグの一部ではないことを示すメッセージを表示します。

    - 要約すると、このスクリプトはモデルのメタデータ内の特定のタグを確認し、そのタグの値をリストに変換して存在する場合はユーザーにフィードバックを提供します。

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

1. この Python スクリプトは、Azure Machine Learning (Azure ML) サービスと対話し、コンピュートインスタンスに対していくつかのチェックを行っています。以下はその内容の概要です：

    - compute_cluster に格納されている名前のコンピュートインスタンスを Azure ML ワークスペースから取得しようとします。コンピュートインスタンスのプロビジョニング状態が "failed" の場合、ValueError を発生させます。

    - computes_allow_list が None でないかどうかを確認します。None でない場合、リスト内のすべてのコンピュートサイズを小文字に変換し、現在のコンピュートインスタンスのサイズがリストに含まれているかどうかを確認します。含まれていない場合、ValueError を発生させます。

    - computes_allow_list が None の場合、コンピュートインスタンスのサイズがサポートされていない GPU VM サイズのリストに含まれているかどうかを確認します。含まれている場合、ValueError を発生させます。

    - ワークスペース内のすべての利用可能なコンピュートサイズのリストを取得します。その後、このリストを反復処理し、各コンピュートサイズの名前が現在のコンピュートインスタンスのサイズと一致するかどうかを確認します。一致する場合、そのコンピュートサイズの GPU 数を取得し、gpu_count_found を True に設定します。

    - gpu_count_found が True の場合、コンピュートインスタンス内の GPU の数を表示します。gpu_count_found が False の場合、ValueError を発生させます。

    - 要約すると、このスクリプトは Azure ML ワークスペース内のコンピュートインスタンスに対していくつかのチェックを行っており、プロビジョニング状態、許可リストまたは拒否リストに対するサイズ、GPU 数などを確認しています。

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

## 4. モデルの微調整に使用するデータセットを選ぶ

1. ultrachat_200k データセットを使用します。このデータセットには 4 つの分割があり、監督付き微調整 (sft) に適しています。
生成ランキング (gen)。各分割の例の数は次のとおりです：

    ```bash
    train_sft test_sft  train_gen  test_gen
    207865  23110  256032  28304
    ```

1. 次のいくつかのセルでは、微調整のための基本的なデータ準備を示します：

### データ行の可視化

このサンプルを迅速に実行したいので、既にトリムされた行の 5% を含む train_sft、test_sft ファイルを保存します。これにより、微調整されたモデルの精度が低くなるため、実際の使用には適していません。
download-dataset.py は、ultrachat_200k データセットをダウンロードし、データセットを微調整パイプラインコンポーネントで消費可能な形式に変換するために使用されます。また、データセットが大きいため、ここではデータセットの一部のみを使用します。

1. 以下のスクリプトを実行すると、データの 5% のみがダウンロードされます。これは dataset_split_pc パラメータを変更することで、希望の割合に増やすことができます。

    > [!NOTE]
    > 一部の言語モデルには異なる言語コードがあり、データセット内の列名もそれに対応する必要があります。

1. データがどのように見えるかの例は次のとおりです。
チャット補完データセットは、次のスキーマを使用して各エントリを保存するパーケット形式で保存されます：

    - これは JSON (JavaScript Object Notation) ドキュメントであり、データ交換フォーマットとして広く使用されています。これは実行可能なコードではなく、データを保存および輸送する方法です。以下はその構造の概要です：

    - "prompt": AI アシスタントに対して提示されるタスクや質問を表す文字列値を保持します。

    - "messages": 会話のメッセージを表すオブジェクトの配列を保持します。各メッセージオブジェクトには 2 つのキーがあります：

    - "content": メッセージの内容を表す文字列値を保持します。
    - "role": メッセージを送信したエンティティの役割を表す文字列値を保持します。"user" または "assistant" のいずれかです。
    - "prompt_id": プロンプトの一意の識別子を表す文字列値を保持します。

1. この特定の JSON ドキュメントでは、ユーザーが AI アシスタントにディストピア小説の主人公を作成するように求める会話が表されています。アシスタントが応答し、ユーザーがさらに詳細を求めます。アシスタントは詳細を提供することに同意します。この会話全体が特定のプロンプト ID に関連付けられています。

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

1. この Python スクリプトは、download-dataset.py というヘルパースクリプトを使用してデータセットをダウンロードするために使用されます。以下はその内容の概要です：

    - os モジュールをインポートします。これは、オペレーティングシステム依存の機能をポータブルに使用する方法を提供します。

    - os.system 関数を使用して、特定のコマンドライン引数を持つシェルで download-dataset.py スクリプトを実行します。引数は、ダウンロードするデータセット (HuggingFaceH4/ultrachat_200k)、ダウンロード先のディレクトリ (ultrachat_200k_dataset)、およびデータセットの分割割合 (5) を指定します。os.system 関数は実行したコマンドの終了ステータスを返します。このステータスは exit_status 変数に格納されます。

    - exit_status が 0 でないかどうかを確認します。Unix ライクなオペレーティングシステムでは、終了ステータスが 0 の場合、通常コマンドが成功したことを示し、他の数字はエラーを示します。exit_status が 0 でない場合、データセットのダウンロード中にエラーが発生したことを示すメッセージを持つ例外を発生させます。

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

### データを DataFrame に読み込む

1. この Python スクリプトは、JSON Lines ファイルを pandas DataFrame に読み込み、最初の 5 行を表示します。以下はその内容の概要です：

    - pandas ライブラリをインポートします。これは強力なデータ操作および分析ライブラリです。

    - pandas の表示オプションの最大列幅を 0 に設定します。これにより、DataFrame が印刷されるときに各列の完全なテキストが切り捨てられることなく表示されます。

    - pd.read_json 関数を使用して、ultrachat_200k_dataset ディレクトリから train_sft.jsonl ファイルを DataFrame に読み込みます。lines=True 引数は、ファイルが JSON Lines 形式であることを示
様々なパラメータに基づいてトレーニングパイプラインを作成し、この表示名を印刷します。 ```python
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
1. レジストリから「chat_completion_pipeline」という名前のパイプラインコンポーネントを取得します。
1. `@pipeline` decorator and the function `create_pipeline`. The name of the pipeline is set to `pipeline_display_name`.

1. Inside the `create_pipeline` function, it initializes the fetched pipeline component with various parameters, including the model path, compute clusters for different stages, dataset splits for training and testing, the number of GPUs to use for fine-tuning, and other fine-tuning parameters.

1. It maps the output of the fine-tuning job to the output of the pipeline job. This is done so that the fine-tuned model can be easily registered, which is required to deploy the model to an online or batch endpoint.

1. It creates an instance of the pipeline by calling the `create_pipeline` function.

1. It sets the `force_rerun` setting of the pipeline to `True`, meaning that cached results from previous jobs will not be used.

1. It sets the `continue_on_step_failure` setting of the pipeline to `False`を使用してパイプラインジョブを定義します。これは、ステップのいずれかが失敗した場合にパイプラインが停止することを意味します。
1. 要約すると、このスクリプトはAzure Machine Learning SDKを使用してチャット完了タスクのための機械学習パイプラインを定義および設定しています。

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

### ジョブの提出

1. このPythonスクリプトは、Azure Machine Learningワークスペースに機械学習パイプラインジョブを提出し、そのジョブが完了するのを待ちます。以下はその内容の概要です：

    - workspace_ml_clientのjobsオブジェクトのcreate_or_updateメソッドを呼び出してパイプラインジョブを提出します。実行するパイプラインはpipeline_objectによって指定され、ジョブが実行される実験はexperiment_nameによって指定されます。
    
    - 次に、workspace_ml_clientのjobsオブジェクトのstreamメソッドを呼び出してパイプラインジョブが完了するのを待ちます。待つジョブはpipeline_jobオブジェクトのname属性で指定されます。
    
    - 要約すると、このスクリプトはAzure Machine Learningワークスペースに機械学習パイプラインジョブを提出し、そのジョブが完了するのを待っています。

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

## 6. 微調整されたモデルをワークスペースに登録する

微調整ジョブの出力からモデルを登録します。これにより、微調整されたモデルと微調整ジョブとの間の系統を追跡できます。さらに、微調整ジョブは基礎モデル、データ、トレーニングコードとの系統を追跡します。

### MLモデルの登録

1. このPythonスクリプトは、Azure Machine Learningパイプラインでトレーニングされた機械学習モデルを登録しています。以下はその内容の概要です：

    - Azure AI ML SDKから必要なモジュールをインポートします。
    
    - trained_model出力がパイプラインジョブから利用可能かどうかを、workspace_ml_clientのjobsオブジェクトのgetメソッドを呼び出し、そのoutputs属性にアクセスして確認します。
    
    - パイプラインジョブの名前と出力名（「trained_model」）を使用して、トレーニングされたモデルへのパスを構築します。
    
    - 元のモデル名に「-ultrachat-200k」を追加し、スラッシュをハイフンに置き換えて微調整されたモデルの名前を定義します。
    
    - モデルへのパス、モデルのタイプ（MLflowモデル）、モデルの名前とバージョン、モデルの説明など、様々なパラメータを使用してModelオブジェクトを作成し、モデルの登録準備を行います。
    
    - workspace_ml_clientのmodelsオブジェクトのcreate_or_updateメソッドをModelオブジェクトを引数として呼び出し、モデルを登録します。
    
    - 登録されたモデルを印刷します。

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

## 7. 微調整されたモデルをオンラインエンドポイントにデプロイする

オンラインエンドポイントは、モデルを使用する必要があるアプリケーションと統合するために使用できる耐久性のあるREST APIを提供します。

### エンドポイントの管理

1. このPythonスクリプトは、登録されたモデルのためにAzure Machine Learningで管理されたオンラインエンドポイントを作成しています。以下はその内容の概要です：

    - Azure AI ML SDKから必要なモジュールをインポートします。
    
    - 「ultrachat-completion-」という文字列にタイムスタンプを追加して、オンラインエンドポイントの一意の名前を定義します。
    
    - エンドポイントの名前、説明、認証モード（「key」）など、様々なパラメータを使用してManagedOnlineEndpointオブジェクトを作成し、オンラインエンドポイントの作成準備を行います。
    
    - workspace_ml_clientのbegin_create_or_updateメソッドをManagedOnlineEndpointオブジェクトを引数として呼び出してオンラインエンドポイントを作成し、waitメソッドを呼び出して作成操作が完了するのを待ちます。

1. 要約すると、このスクリプトは、登録されたモデルのためにAzure Machine Learningで管理されたオンラインエンドポイントを作成しています。

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
> デプロイに対応しているSKUのリストはこちらで確認できます - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### MLモデルのデプロイ

1. このPythonスクリプトは、登録された機械学習モデルをAzure Machine Learningの管理されたオンラインエンドポイントにデプロイしています。以下はその内容の概要です：

    - Pythonの抽象構文木（AST）を処理するための関数を提供するastモジュールをインポートします。
    
    - デプロイのインスタンスタイプを「Standard_NC6s_v3」に設定します。
    
    - 基礎モデルにinference_compute_allow_listタグがあるかどうかを確認します。ある場合、そのタグ値を文字列からPythonリストに変換し、inference_computes_allow_listに割り当てます。ない場合、inference_computes_allow_listをNoneに設定します。
    
    - 指定されたインスタンスタイプが許可リストに含まれているかどうかを確認します。含まれていない場合、ユーザーに許可リストからインスタンスタイプを選択するようメッセージを表示します。
    
    - デプロイの名前、エンドポイントの名前、モデルのID、インスタンスタイプとカウント、ライブネスプローブ設定、リクエスト設定など、様々なパラメータを使用してManagedOnlineDeploymentオブジェクトを作成し、デプロイの作成準備を行います。
    
    - workspace_ml_clientのbegin_create_or_updateメソッドをManagedOnlineDeploymentオブジェクトを引数として呼び出してデプロイを作成し、waitメソッドを呼び出して作成操作が完了するのを待ちます。
    
    - エンドポイントのトラフィックを「demo」デプロイに100%割り当てるように設定します。
    
    - workspace_ml_clientのbegin_create_or_updateメソッドをエンドポイントオブジェクトを引数として呼び出してエンドポイントを更新し、resultメソッドを呼び出して更新操作が完了するのを待ちます。

1. 要約すると、このスクリプトは、登録された機械学習モデルをAzure Machine Learningの管理されたオンラインエンドポイントにデプロイしています。

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

テストデータセットからいくつかのサンプルデータを取得し、オンラインエンドポイントに提出して推論を行います。スコアリングされたラベルと実際のラベルを並べて表示します。

### 結果の読み取り

1. このPythonスクリプトは、JSON Linesファイルをpandas DataFrameに読み込み、ランダムサンプルを取り、インデックスをリセットしています。以下はその内容の概要です：

    - ./ultrachat_200k_dataset/test_gen.jsonlファイルをpandas DataFrameに読み込みます。ファイルがJSON Lines形式（各行が個別のJSONオブジェクト）であるため、lines=True引数を使用してread_json関数を使用します。
    
    - DataFrameから1行のランダムサンプルを取ります。sample関数を使用し、n=1引数で選択するランダム行の数を指定します。
    
    - DataFrameのインデックスをリセットします。reset_index関数をdrop=True引数と共に使用して元のインデックスを削除し、新しいデフォルトの整数値のインデックスに置き換えます。
    
    - head関数を引数2と共に使用してDataFrameの最初の2行を表示します。ただし、サンプリング後のDataFrameには1行しか含まれていないため、その1行のみが表示されます。

1. 要約すると、このスクリプトは、JSON Linesファイルをpandas DataFrameに読み込み、1行のランダムサンプルを取り、インデックスをリセットし、最初の行を表示しています。

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

1. このPythonスクリプトは、特定のパラメータを持つJSONオブジェクトを作成し、ファイルに保存しています。以下はその内容の概要です：

    - JSONデータを操作するための関数を提供するjsonモジュールをインポートします。
    
    - 機械学習モデルのパラメータを表すキーと値を持つ辞書parametersを作成します。キーは「temperature」、「top_p」、「do_sample」、「max_new_tokens」で、それぞれの対応する値は0.6、0.9、True、および200です。
    
    - もう一つの辞書test_jsonを作成し、キーは「input_data」と「params」です。「input_data」の値は、キー「input_string」と「parameters」を持つ別の辞書です。「input_string」の値はtest_df DataFrameの最初のメッセージを含むリストです。「parameters」の値は先ほど作成したparameters辞書です。「params」の値は空の辞書です。
    
    - sample_score.jsonという名前のファイルを開きます。

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

1. このPythonスクリプトは、Azure Machine Learningのオンラインエンドポイントを呼び出してJSONファイルをスコアリングしています。以下はその内容の概要です：

    - workspace_ml_clientオブジェクトのonline_endpointsプロパティのinvokeメソッドを呼び出します。このメソッドはオンラインエンドポイントにリクエストを送信し、レスポンスを取得するために使用されます。
    
    - エンドポイントとデプロイの名前をendpoint_nameとdeployment_name引数で指定します。この場合、エンドポイント名はonline_endpoint_name変数に格納され、デプロイ名は「demo」です。
    
    - request_file引数でスコアリングするJSONファイルのパスを指定します。この場合、ファイルは./ultrachat_200k_dataset/sample_score.jsonです。
    
    - エンドポイントからのレスポンスをresponse変数に格納します。
    
    - 生のレスポンスを印刷します。

1. 要約すると、このスクリプトは、Azure Machine Learningのオンラインエンドポイントを呼び出してJSONファイルをスコアリングし、レスポンスを印刷しています。

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

## 9. オンラインエンドポイントを削除する

1. オンラインエンドポイントを削除するのを忘れないでください。そうしないと、エンドポイントで使用されるコンピューティングの課金メーターが動作し続けます。このPythonコード行は、Azure Machine Learningでオンラインエンドポイントを削除しています。以下はその内容の概要です：

    - workspace_ml_clientオブジェクトのonline_endpointsプロパティのbegin_deleteメソッドを呼び出します。このメソッドはオンラインエンドポイントの削除を開始するために使用されます。
    
    - 削除するエンドポイントの名前をname引数で指定します。この場合、エンドポイント名はonline_endpoint_name変数に格納されています。
    
    - waitメソッドを呼び出して削除操作が完了するのを待ちます。これはブロッキング操作であり、削除が完了するまでスクリプトの実行を続行しません。
    
    - 要約すると、このコード行はAzure Machine Learningでオンラインエンドポイントの削除を開始し、その操作が完了するのを待っています。

    ```python
    # Delete the online endpoint in Azure Machine Learning
    # The `begin_delete` method of the `online_endpoints` property of the `workspace_ml_client` object is used to start the deletion of an online endpoint
    # The `name` argument specifies the name of the endpoint to be deleted, which is stored in the `online_endpoint_name` variable
    # The `wait` method is called to wait for the deletion operation to complete. This is a blocking operation, meaning that it will prevent the script from continuing until the deletion is finished
    workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
    ```

**免責事項**:
この文書は機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期していますが、自動翻訳にはエラーや不正確さが含まれる場合がありますのでご注意ください。元の言語での原文が信頼できる情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤訳については、一切の責任を負いかねます。