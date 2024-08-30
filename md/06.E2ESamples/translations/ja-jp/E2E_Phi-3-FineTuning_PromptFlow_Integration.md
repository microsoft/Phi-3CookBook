# カスタム Phi-3 モデルのファインチューニングと Prompt flow との統合

このエンドツーエンド (E2E) サンプルは、Microsoft Tech Community のガイド「[カスタム Phi-3 モデルのファインチューニングと Prompt Flow との統合: ステップバイステップガイド](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)」に基づいています。これは、カスタム Phi-3 モデルのファインチューニング、デプロイ、および Prompt flow との統合のプロセスを紹介します。

## 概要

この E2E サンプルでは、Phi-3 モデルをファインチューニングし、Prompt flow と統合する方法を学びます。Azure Machine Learning と Prompt flow を活用することで、カスタム AI モデルをデプロイして利用するためのワークフローを確立します。この E2E サンプルは、3 つのシナリオに分かれています。

**シナリオ 1: Azure リソースのセットアップとファインチューニングの準備**

**シナリオ 2: Phi-3 モデルのファインチューニングと Azure Machine Learning Studio へのデプロイ**

**シナリオ 3: Prompt flow との統合とカスタムモデルとのチャット**

以下は、この E2E サンプルの概要図です。

![Phi-3-FineTuning_PromptFlow_Integration 概要](../../../../imgs/03/FineTuning-PromptFlow/00-01-architecture.png)

### 目次

1. **[シナリオ 1: Azure リソースのセットアップとファインチューニングの準備](#scenario-1-set-up-azure-resources-and-prepare-for-fine-tuning)**
    - [Azure Machine Learning ワークスペースの作成](#create-an-azure-machine-learning-workspace)
    - [Azure サブスクリプションでの GPU クォータのリクエスト](#request-gpu-quotas-in-azure-subscription)
    - [ロールの割り当て](#add-role-assignment)
    - [プロジェクトのセットアップ](#set-up-project)
    - [ファインチューニング用データセットの準備](#prepare-dataset-for-fine-tuning)

1. **[シナリオ 2: Phi-3 モデルのファインチューニングと Azure Machine Learning Studio へのデプロイ](#scenario-2-fine-tune-phi-3-model-and-deploy-in-azure-machine-learning-studio)**
    - [Azure CLI のセットアップ](#set-up-azure-cli)
    - [Phi-3 モデルのファインチューニング](#fine-tune-the-phi-3-model)
    - [ファインチューニングされたモデルのデプロイ](#deploy-the-fine-tuned-model)

1. **[シナリオ 3: Prompt flow との統合とカスタムモデルとのチャット](#scenario-3-integrate-with-prompt-flow-and-chat-with-your-custom-model)**
    - [カスタム Phi-3 モデルを Prompt flow と統合](#integrate-the-custom-phi-3-model-with-prompt-flow)
    - [カスタムモデルとのチャット](#chat-with-your-custom-model)

## シナリオ 1: Azure リソースのセットアップとファインチューニングの準備

### Azure Machine Learning ワークスペースの作成

1. ポータルページの上部にある **検索バー** に *azure machine learning* と入力し、表示されるオプションから **Azure Machine Learning** を選択します。

    ![azure machine learning と入力](../../../../imgs/03/FineTuning-PromptFlow/01-01-type-azml.png)

1. ナビゲーションメニューから **+ Create** を選択します。

1. ナビゲーションメニューから **New workspace** を選択します。

    ![new workspace を選択](../../../../imgs/03/FineTuning-PromptFlow/01-02-select-new-workspace.png)

1. 次のタスクを実行します。

    - Azure **Subscription** を選択します。
    - 使用する **Resource group** を選択します（必要に応じて新しいものを作成します）。
    - **Workspace Name** を入力します。これは一意の値である必要があります。
    - 使用する **Region** を選択します。
    - 使用する **Storage account** を選択します（必要に応じて新しいものを作成します）。
    - 使用する **Key vault** を選択します（必要に応じて新しいものを作成します）。
    - 使用する **Application insights** を選択します（必要に応じて新しいものを作成します）。
    - 使用する **Container registry** を選択します（必要に応じて新しいものを作成します）。

    ![AZML を入力](../../../../imgs/03/FineTuning-PromptFlow/01-03-fill-AZML.png)

1. **Review + Create** を選択します。

1. **Create** を選択します。

### Azure サブスクリプションでの GPU クォータのリクエスト

この E2E サンプルでは、ファインチューニングに *Standard_NC24ads_A100_v4 GPU* を使用し、デプロイに *Standard_E4s_v3* CPU を使用します。GPU クォータのリクエストが必要です。

> [!NOTE]
>
> GPU 割り当ては、従量課金制サブスクリプション（標準サブスクリプションタイプ）のみが対象です。特典サブスクリプションは現在サポートされていません。
>
> 特典サブスクリプション（Visual Studio Enterprise Subscription など）を使用している場合や、ファインチューニングとデプロイプロセスを迅速にテストしたい場合、このチュートリアルでは CPU を使用した最小データセットでのファインチューニングのガイダンスも提供しています。ただし、GPU を使用したファインチューニング結果は、より大きなデータセットを使用する場合に大幅に向上します。

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) にアクセスします。

1. 次のタスクを実行して *Standard NCADSA100v4 Family* クォータをリクエストします。

    - 左側のタブから **Quota** を選択します。
    - 使用する **Virtual machine family** を選択します。たとえば、*Standard_NC24ads_A100_v4* GPU を含む **Standard NCADSA100v4 Family Cluster Dedicated vCPUs** を選択します。
    - ナビゲーションメニューから **Request quota** を選択します。

        ![クォータをリクエスト](../../../../imgs/03/FineTuning-PromptFlow/01-04-request-quota.png)

    - Request quota ページで、使用する **New cores limit** を入力します。たとえば、24。
    - Request quota ページで、**Submit** を選択して GPU クォータをリクエストします。

> [!NOTE]
> 適切な GPU または CPU を選択するには、[Sizes for Virtual Machines in Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist) ドキュメントを参照してください。

### ロールの割り当て

モデルをファインチューニングしてデプロイするには、まずユーザー割り当てマネージドID (UAI) を作成し、適切な権限を割り当てる必要があります。この UAI は、デプロイ中の認証に使用されます。

#### ユーザー割り当てマネージドID (UAI) の作成

1. ポータルページの上部にある **検索バー** に *managed identities* と入力し、表示されるオプションから **Managed Identities** を選択します。

    ![managed identities と入力](../../../../imgs/03/FineTuning-PromptFlow/01-05-type-managed-identities.png)

1. **+ Create** を選択します。

    ![create を選択](../../../../imgs/03/FineTuning-PromptFlow/01-06-select-create.png)

1. 次のタスクを実行します。

    - Azure **Subscription** を選択します。
    - 使用する **Resource group** を選択します（必要に応じて新しいものを作成します）。
    - 使用する **Region** を選択します。
    - **Name** を入力します。これは一意の値である必要があります。

1. **Review + create** を選択します。

1. **+ Create** を選択します。

#### マネージドIDに対する貢献者ロールの割り当て

1. 作成したマネージドIDリソースに移動します。

1. 左側のタブから **Azure role assignments** を選択します。

1. ナビゲーションメニューから **+Add role assignment** を選択します。

1. Add role assignment ページで、次のタスクを実行します。
    - **Scope** を **Resource group** に設定します。
    - Azure **Subscription** を選択します。
    - 使用する **Resource group** を選択します。
    - **Role** を **Contributor** に設定します。

    ![貢献者ロールを入力](../../../../imgs/03/FineTuning-PromptFlow/01-07-fill-contributor-role.png)

1. **Save** を選択します。

#### マネージドIDに対するストレージ Blob データリーダーロールの割り当て

1. ポータルページの上部にある **検索バー** に *storage accounts* と入力し、表示されるオプションから **Storage accounts** を選択します。

    ![storage accounts と入力](../../../../imgs/03/FineTuning-PromptFlow/01-08-type-storage-accounts.png)

1. 作成した Azure Machine Learning ワークスペースに関連付けられたストレージアカウントを選択します。たとえば、*finetunephistorage*。

1. 次のタスクを実行して Add role assignment ページに移動します。

    - 作成した Azure ストレージアカウントに移動します。
    - 左側のタブから **Access Control (IAM)** を選択します。
    - ナビゲーションメニューから **+ Add** を選択します。
    - ナビゲーションメニューから **Add role assignment** を選択します。

    ![ロールを追加](../../../../imgs/03/FineTuning-PromptFlow/01-09-add-role.png)

1. Add role assignment ページで、次のタスクを実行します。

    - Role ページで、**Storage Blob Data Reader** と入力し、表示されるオプションから **Storage Blob Data Reader** を選択します。
    - Role ページで、**Next** を選択します。
    - Members ページで、**Assign access to** を **Managed identity** に設定します。
    - Members ページで、**+ Select members** を選択します。
    - Select managed identities ページで、Azure **Subscription** を選択します。
    - Select managed identities ページで、**Managed identity** を **Manage Identity** に設定します。
    - Select managed identities ページで、作成したマネージドIDを選択します。たとえば、*finetunephi-managedidentity*。
    - Select managed identities ページで、**Select** を選択します。

    ![マネージドIDを選択](../../../../imgs/03/FineTuning-PromptFlow/01-10-select-managed-identity.png)

1. **Review + assign** を選択します。

#### マネージドIDに対する AcrPull ロールの割り当て

1. ポータルページの上部にある **検索バー** に *container registries* と入力し、表示されるオプションから **Container registries** を選択します。

    ![container registries と入力](../../../../imgs/03/FineTuning-PromptFlow/01-11-type-container-registries.png)

1. Azure Machine Learning ワークスペースに関連付けられたコンテナレジストリを選択します。たとえば、*finetunephicontainerregistries*。

1. 次のタスクを実行して Add role assignment ページに移動します。

    - 左側のタブから **Access Control (IAM)** を選択します。
    - ナビゲーションメニューから **+ Add** を選択します。
    - ナビゲーションメニューから **Add role assignment** を選択します。

1. Add role assignment ページで、次のタスクを実行します。

    - Role ページで、**AcrPull** と入力し、表示されるオプションから **AcrPull** を選択します。
    - Role ページで、**Next** を選択します。
    - Members ページで、**Assign access to** を **Managed identity** に設定します。
    - Members ページで、**+ Select members** を選択します。
    - Select managed identities ページで、Azure **Subscription** を選択します。
    - Select managed identities ページで、**Managed identity** を **Manage Identity** に設定します。
    - Select managed identities ページで、作成したマネージドIDを選択します。たとえば、*finetunephi-managedidentity*。
    - Select managed identities ページで、**Select** を選択します。
    - **Review + assign** を選択します。

### プロジェクトのセットアップ

次に、作業用のフォルダを作成し、仮想環境を設定して、ユーザーと対話し、Azure Cosmos DB に保存されたチャット履歴を使用するプログラムを開発します。

#### 作業フォルダの作成

1. ターミナルウィンドウを開き、次のコマンドを入力して、デフォルトのパスに *finetune-phi* という名前のフォルダを作成します。

    ```console
    mkdir finetune-phi
    ```

1. ターミナルで次のコマンドを入力して、作成した *finetune-phi* フォルダに移動します。

    ```console
    cd finetune-phi
    ```

#### 仮想環境の作成

1. ターミナルで次のコマンドを入力して、*.venv* という名前の仮想環境を作成します。

    ```console
    python -m venv .venv
    ```

1. ターミナルで次のコマンドを入力して、仮想環境をアクティブにします。

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> 成功した場合、コマンドプロンプトの前に *(.venv)* が表示されます。

#### 必要なパッケージのインストール

1. ターミナルで次のコマンドを入力して、必要なパッケージをインストールします。

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### プロジェクトファイルの作成

この演習では、プロジェクトに必要なファイルを作成します。これらのファイルには、データセットのダウンロード、Azure Machine Learning 環境の設定、Phi-3 モデルのファインチューニング、およびファインチューニングされたモデルのデプロイのためのスクリプトが含まれます。また、ファインチューニング環境を設定するための *conda.yml* ファイルも作成します。

この演習では、次のことを行います。

- データセットをダウンロードするための *download_dataset.py* ファイルを作成します。
- Azure Machine Learning 環境を設定するための *setup_ml.py* ファイルを作成します。
- データセットを使用して Phi-3 モデルをファインチューニングするための *fine_tune.py* ファイルを *finetuning_dir* フォルダに作成します。
- ファインチューニング環境を設定するための *conda.yml* ファイルを作成します。
- ファインチューニングされたモデルをデプロイするための *deploy_model.py* ファイルを作成します。
- ファインチューニングされたモデルを統合し、Prompt flow を使用してモデルを実行するための *integrate_with_promptflow.py* ファイルを作成します。
- Prompt flow のワークフロー構造を設定するための *flow.dag.yml* ファイルを作成します。
- Azure 情報を入力するための *config.py* ファイルを作成します。

> [!NOTE]
>
> 完全なフォルダ構造:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        ├── finetuning_dir
> .        │      └── fine_tune.py
> .        ├── conda.yml
> .        ├── config.py
> .        ├── deploy_model.py
> .        ├── download_dataset.py
> .        ├── flow.dag.yml
> .        ├── integrate_with_promptflow.py
> .        └── setup_ml.py
> ```

1. **Visual Studio Code** を開きます。

1. メニューバーから **File** を選択します。

1. **Open Folder** を選択します。

1. 作成した *finetune-phi* フォルダを選択します。場所は *C:\Users\yourUserName\finetune-phi* です。

    ![プロジェクトフォルダを開く](../../../../imgs/03/FineTuning-PromptFlow/01-12-open-project-folder.png)

1. Visual Studio Code の左側のペインで右クリックし、**New File** を選択して、*download_dataset.py* という名前の新しいファイルを作成します。

1. Visual Studio Code の左側のペインで右クリックし、**New File** を選択して、*setup_ml.py* という名前の新しいファイルを作成します。

1. Visual Studio Code の左側のペインで右クリックし、**New File** を選択して、*deploy_model.py* という名前の新しいファイルを作成します。

    ![新しいファイルを作成](../../../../imgs/03/FineTuning-PromptFlow/01-13-create-new-file.png)

1. Visual Studio Code の左側のペインで右クリックし、**New Folder** を選択して、*finetuning_dir* という名前の新しいフォルダを作成します。

1. *finetuning_dir* フォルダに、*fine_tune.py* という名前の新しいファイルを作成します。

#### *conda.yml* ファイルの作成と設定

1. Visual Studio Code の左側のペインで右クリックし、**New File** を選択して、*conda.yml* という名前の新しいファイルを作成します。

1. *conda.yml* ファイルに次のコードを追加して、Phi-3 モデルのファインチューニング環境を設定します。

    ```yml
    name: phi-3-training-env
    channels:
      - defaults
      - conda-forge
    dependencies:
      - python=3.10
      - pip
      - numpy<2.0
      - pip:
          - torch~=2.0
          - torchvision~=0.18
          - trl==0.8.6
          - transformers~=4.41
          - datasets~=2.19
          - azureml-core~=1.30
          - azure-storage-blob==12.19
          - azure-ai-ml~=1.16
          - azure-identity~=1.16
          - accelerate~=0.30
          - mlflow==2.14.3
          - azureml-mlflow==1.56.0
    ```

#### *config.py* ファイルの作成と設定

1. Visual Studio Code の左側のペインで右クリックし、**New File** を選択して、*config.py* という名前の新しいファイルを作成します。

1. *config.py* ファイルに次のコードを追加して、Azure 情報を含めます。

    ```python
    # Azure 設定
    AZURE_SUBSCRIPTION_ID = "your_subscription_id"
    AZURE_RESOURCE_GROUP_NAME = "your_resource_group_name" # "TestGroup"

    # Azure Machine Learning 設定
    AZURE_ML_WORKSPACE_NAME = "your_workspace_name" # "finetunephi-workspace"

    # Azure Managed Identity 設定
    AZURE_MANAGED_IDENTITY_CLIENT_ID = "your_azure_managed_identity_client_id"
    AZURE_MANAGED_IDENTITY_NAME = "your_azure_managed_identity_name" # "finetunephi-mangedidentity"
    AZURE_MANAGED_IDENTITY_RESOURCE_ID = f"/subscriptions/{AZURE_SUBSCRIPTION_ID}/resourceGroups/{AZURE_RESOURCE_GROUP_NAME}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{AZURE_MANAGED_IDENTITY_NAME}"

    # データセットファイルパス
    TRAIN_DATA_PATH = "data/train_data.jsonl"
    TEST_DATA_PATH = "data/test_data.jsonl"

    # ファインチューニングされたモデル設定
    AZURE_MODEL_NAME = "your_fine_tuned_model_name" # "finetune-phi-model"
    AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name" # "finetune-phi-endpoint"
    AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name" # "finetune-phi-deployment"

    AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"
    AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri" # "https://{your-endpoint-name}.{your-region}.inference.ml.azure.com/score"
    ```

#### Azure 環境変数の追加

1. 次のタスクを実行して Azure サブスクリプション ID を追加します。

    - ポータルページの上部にある **検索バー** に *subscriptions* と入力し、表示されるオプションから **Subscriptions** を選択します。
    - 現在使用している Azure サブスクリプションを選択します。
    - サブスクリプション ID をコピーして *config.py* ファイルに貼り付けます。

    ![サブスクリプション ID を見つける](../../../../imgs/03/FineTuning-PromptFlow/01-14-find-subscriptionid.png)

1. 次のタスクを実行して Azure ワークスペース名を追加します。

    - 作成した Azure Machine Learning リソースに移動します。
    - アカウント名をコピーして *config.py* ファイルに貼り付けます。

    ![Azure Machine Learning 名を見つける](../../../../imgs/03/FineTuning-PromptFlow/01-15-find-AZML-name.png)

1. 次のタスクを実行して Azure リソースグループ名を追加します。

    - 作成した Azure Machine Learning リソースに移動します。
    - Azure リソースグループ名をコピーして *config.py* ファイルに貼り付けます。

    ![リソースグループ名を見つける](../../../../imgs/03/FineTuning-PromptFlow/01-16-find-AZML-resourcegroup.png)

1. 次のタスクを実行して Azure マネージドID名を追加します。

    - 作成したマネージドIDリソースに移動します。
    - Azure マネージドID名をコピーして *config.py* ファイルに貼り付けます。

    ![UAI を見つける](../../../../imgs/03/FineTuning-PromptFlow/01-17-find-uai.png)

### ファインチューニング用データセットの準備

この演習では、*download_dataset.py* ファイルを実行して *ULTRACHAT_200k* データセットをローカル環境にダウンロードします。次に、これらのデータセットを使用して Azure Machine Learning で Phi-3 モデルをファインチューニングします。

#### *download_dataset.py* を使用してデータセットをダウンロード

1. Visual Studio Code で *download_dataset.py* ファイルを開きます。

1. *download_dataset.py* に次のコードを追加します。

    ```python
    import json
    import os
    from datasets import load_dataset
    from config import (
        TRAIN_DATA_PATH,
        TEST_DATA_PATH)

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        データセットをロードして分割します。
        """
        # 指定された名前、構成、および分割比でデータセットをロードします
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"元のデータセットサイズ: {len(dataset)}")

        # データセットをトレーニングセットとテストセットに分割します（80% トレーニング、20% テスト）
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"トレーニングデータセットサイズ: {len(split_dataset['train'])}")
        print(f"テストデータセットサイズ: {len(split_dataset['test'])}")

        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        データセットを JSONL ファイルに保存します。
        """
        # ディレクトリが存在しない場合は作成します
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # ファイルを書き込みモードで開きます
        with open(filepath, 'w', encoding='utf-8') as f:
            # データセット内の各レコードを反復処理します
            for record in dataset:
                # レコードを JSON オブジェクトとしてダンプし、ファイルに書き込みます
                json.dump(record, f)
                # レコードを区切るために改行文字を書き込みます
                f.write('\n')

        print(f"データセットが {filepath} に保存されました")

    def main():
        """
        データセットをロード、分割、および保存するメイン関数。
        """
        # 特定の構成と分割比で ULTRACHAT_200k データセットをロードおよび分割します
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')

        # 分割からトレーニングデータセットとテストデータセットを抽出します
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # トレーニングデータセットを JSONL ファイルに保存します
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)

        # テストデータセットを別の JSONL ファイルに保存します
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **最小データセットを使用して CPU でファインチューニングするためのガイダンス**
>
> CPU を使用してファインチューニングする場合、このアプローチは特典サブスクリプション（Visual Studio Enterprise Subscription など）を持つユーザーや、ファインチューニングとデプロイプロセスを迅速にテストしたい場合に最適です。
>
> `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` を `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')` に置き換えます。
>

1. ターミナルで次のコマンドを入力してスクリプトを実行し、データセットをローカル環境にダウンロードします。

    ```console
    python download_data.py
    ```

1. データセットがローカルの *finetune-phi/data* ディレクトリに正常に保存されたことを確認します。

> [!NOTE]
>
> **データセットのサイズとファインチューニング時間**
>
> この E2E サンプルでは、データセットの 1% のみを使用します（`train_sft[:1%]`）。これにより、データ量が大幅に減少し、アップロードとファインチューニングのプロセスが高速化されます。データセットの割合を調整して、トレーニング時間とモデルパフォーマンスのバランスを見つけることができます。小さなデータセットのサブセットを使用することで、ファインチューニングに必要な時間を短縮し、プロセスをより管理しやすくします。

## シナリオ 2: Phi-3 モデルのファインチューニングと Azure Machine Learning Studio へのデプロイ

### Azure CLI のセットアップ

Azure CLI を設定して環境を認証する必要があります。Azure CLI を使用すると、コマンドラインから直接 Azure リソースを管理でき、Azure Machine Learning がこれらのリソースにアクセスするために必要な資格情報を提供します。開始するには、[Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) をインストールします。

1. ターミナルウィンドウを開き、次のコマンドを入力して Azure アカウントにログインします。

    ```console
    az login
    ```

1. 使用する Azure アカウントを選択します。

1. 使用する Azure サブスクリプションを選択します。

    ![Azure CLI を使用してログイン](../../../../imgs/03/FineTuning-PromptFlow/02-01-login-using-azure-cli.png)

> [!TIP]
>
> Azure にサインインする際に問題が発生した場合は、デバイスコードを使用してみてください。ターミナルウィンドウを開き、次のコマンドを入力して Azure アカウントにサインインします。
>
> ```console
> az login --use-device-code
> ```
>

### Phi-3 モデルのファインチューニング

この演習では、提供されたデータセットを使用して Phi-3 モデルをファインチューニングします。まず、*fine_tune.py* ファイルでファインチューニングプロセスを定義します。次に、Azure Machine Learning 環境を設定し、*setup_ml.py* ファイルを実行してファインチューニングプロセスを開始します。このスクリプトは、ファインチューニングが Azure Machine Learning 環境内で行われることを保証します。

*setup_ml.py* を実行することで、ファインチューニングプロセスが Azure Machine Learning 環境内で実行されます。

#### *fine_tune.py* ファイルにコードを追加

1. *finetuning_dir* フォルダに移動し、Visual Studio Code で *fine_tune.py* ファイルを開きます。

1. *fine_tune.py* に次のコードを追加します。

    ```python
    import argparse
    import sys
    import logging
    import os
    from datasets import load_dataset
    import torch
    import mlflow
    from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
    from trl import SFTTrainer

    # MLflow での INVALID_PARAMETER_VALUE エラーを回避するために、MLflow 統合を無効にします
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # ログ設定
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
        level=logging.WARNING
    )
    logger = logging.getLogger(__name__)

    def initialize_model_and_tokenizer(model_name, model_kwargs):
        """
        指定された事前学習済みモデル名と引数を使用してモデルとトークナイザーを初期化します。
        """
        model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.model_max_length = 2048
        tokenizer.pad_token = tokenizer.unk_token
        tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids(tokenizer.pad_token)
        tokenizer.padding_side = 'right'
        return model, tokenizer

    def apply_chat_template(example, tokenizer):
        """
        チャットテンプレートを適用して、例のメッセージをトークナイズします。
        """
        messages = example["messages"]
        if messages[0]["role"] != "system":
            messages.insert(0, {"role": "system", "content": ""})
        example["text"] = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=False
        )
        return example

    def load_and_preprocess_data(train_filepath, test_filepath, tokenizer):
        """
        データセットをロードして前処理します。
        """
        train_dataset = load_dataset('json', data_files=train_filepath, split='train')
        test_dataset = load_dataset('json', data_files=test_filepath, split='train')
        column_names = list(train_dataset.features)

        train_dataset = train_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="トレーニングデータセットにチャットテンプレートを適用中",
        )

        test_dataset = test_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="テストデータセットにチャットテンプレートを適用中",
        )

        return train_dataset, test_dataset

    def train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, output_dir):
        """
        モデルをトレーニングして評価します。
        """
        training_args = TrainingArguments(
            bf16=True,
            do_eval=True,
            output_dir=output_dir,
            eval_strategy="epoch",
            learning_rate=5.0e-06,
            logging_steps=20,
            lr_scheduler_type="cosine",
            num_train_epochs=3,
            overwrite_output_dir=True,
            per_device_eval_batch_size=4,
            per_device_train_batch_size=4,
            remove_unused_columns=True,
            save_steps=500,
            seed=0,
            gradient_checkpointing=True,
            gradient_accumulation_steps=1,
            warmup_ratio=0.2,
        )

        trainer = SFTTrainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=test_dataset,
            max_seq_length=2048,
            dataset_text_field="text",
            tokenizer=tokenizer,
            packing=True
        )

        train_result = trainer.train()
        trainer.log_metrics("train", train_result.metrics)

        mlflow.transformers.log_model(
            transformers_model={"model": trainer.model, "tokenizer": tokenizer},
            artifact_path=output_dir,
        )

        tokenizer.padding_side = 'left'
        eval_metrics = trainer.evaluate()
        eval_metrics["eval_samples"] = len(test_dataset)
        trainer.log_metrics("eval", eval_metrics)

    def main(train_file, eval_file, model_output_dir):
        """
        モデルをファインチューニングするメイン関数。
        """
        model_kwargs = {
            "use_cache": False,
            "trust_remote_code": True,
            "torch_dtype": torch.bfloat16,
            "device_map": None,
            "attn_implementation": "eager"
        }
        pretrained_model_name = "microsoft/Phi-3-mini-4k-instruct"

        with mlflow.start_run():
            model, tokenizer = initialize_model_and_tokenizer(pretrained_model_name, model_kwargs)
            train_dataset, test_dataset = load_and_preprocess_data(train_file, eval_file, tokenizer)
            train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, model_output_dir)

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--train-file", type=str, required=True, help="トレーニングデータのパス")
        parser.add_argument("--eval-file", type=str, required=True, help="評価データのパス")
        parser.add_argument("--model_output_dir", type=str, required=True, help="ファインチューニングされたモデルを保存するディレクトリ")
        args = parser.parse_args()
        main(args.train_file, args.eval_file, args.model_output_dir)

    ```

1. *fine_tune.py* ファイルを保存して閉じます。

#### *setup_ml.py* ファイルにコードを追加

1. Visual Studio Code で *setup_ml.py* ファイルを開きます。

1. *setup_ml.py* に次のコードを追加します。

    ```python
    import logging
    from azure.ai.ml import MLClient, command, Input
    from azure.ai.ml.entities import Environment, AmlCompute
    from azure.identity import AzureCliCredential
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        TRAIN_DATA_PATH,
        TEST_DATA_PATH
    )

    # 定数

    # CPU インスタンスを使用する場合は、以下の行をコメント解除します
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
    # CONDA_FILE = "conda.yml"

    # GPU インスタンスを使用する場合は、以下の行をコメント解除します
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"
    CONDA_FILE = "conda.yml"

    LOCATION = "eastus2" # 計算クラスターの場所に置き換えます
    FINETUNING_DIR = "./finetuning_dir" # ファインチューニングスクリプトのパス
    TRAINING_ENV_NAME = "phi-3-training-environment" # トレーニング環境の名前
    MODEL_OUTPUT_DIR = "./model_output" # azure ml のモデル出力ディレクトリのパス

    # プロセスを追跡するためのログ設定
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s - %(levellevel)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.WARNING
    )

    def get_ml_client():
        """
        Azure CLI 資格情報を使用して ML クライアントを初期化します。
        """
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def create_or_get_environment(ml_client):
        """
        Create or update the training environment in Azure ML.
        """
        env = Environment(
            image=DOCKER_IMAGE_NAME,  # 環境の Docker イメージ
            conda_file=CONDA_FILE,  # Conda 環境ファイル
            name=TRAINING_ENV_NAME,  # 環境の名前
        )
        return ml_client.environments.create_or_update(env)

    def create_or_get_compute_cluster(ml_client, compute_name, COMPUTE_INSTANCE_TYPE, location):
        """
        Create or update the compute cluster in Azure ML.
        """
        try:
            compute_cluster = ml_client.compute.get(compute_name)
            logger.info(f"Compute cluster '{compute_name}' already exists. Reusing it for the current run.")
        except Exception:
            logger.info(f"Compute cluster '{compute_name}' does not exist. Creating a new one with size {COMPUTE_INSTANCE_TYPE}.")
            compute_cluster = AmlCompute(
                name=compute_name,
                size=COMPUTE_INSTANCE_TYPE,
                location=location,
                tier="Dedicated",  # 計算クラスタの階層
                min_instances=0,  # 最小インスタンス数
                max_instances=1  # インスタンスの最大数
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # クラスタの作成を待つ
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # fine_tune.pyへのパス
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # トレーニング環境
            compute=compute_name,  # 使用する計算クラスタ
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # トレーニングデータファイルへのパス
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # 評価データファイルへのパス
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # MLクライアントの初期化
        ml_client = get_ml_client()

        # 環境の作成
        env = create_or_get_environment(ml_client)

        # 既存のコンピュートクラスタを作成または取得する
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # ファインチューニングジョブの作成と提出
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # ジョブの送信
        ml_client.jobs.stream(returned_job.name)  # ジョブログをストリームする

        # ジョブ名をキャプチャする
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()


    ```

1. COMPUTE_INSTANCE_TYPE`、`COMPUTE_NAME`、`LOCATION`は、それぞれの詳細情報に置き換えてください。

    ```python
   # トレーニングにGPUインスタンスを使用するには、以下の行のコメントを外します
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # コンピュートクラスタの場所に置き換えてください
    ```

> [!TIP]
>
> **CPUを使った最小限のデータセットによるファインチューニングのガイダンス**
>
> ファインチューニングにCPUを使用したい場合、この方法は、特典付きサブスクリプション（Visual Studio Enterpriseサブスクリプションなど）を利用している場合や、ファインチューニングとデプロイメントプロセスを迅速にテストする場合に最適です。
>
> 1. conda.yml*ファイルを開きます。
> 1. torchvision~=0.18`はGPU環境としか互換性がないので削除します。
> 1. setup_ml*ファイルを開きます。
> 1. COMPUTE_INSTANCE_TYPE`、`COMPUTE_NAME`、`DOCKER_IMAGE_NAME`を以下のように置き換えます。Standard_E16s_v3*にアクセスできない場合は、同等のCPUインスタンスを使用するか、新しいクォータを要求することができる。
> 1. LOCATION`を特定の詳細情報に置き換える。
>
>    ```python
>    # トレーニングにCPUインスタンスを使用するには、以下の行のコメントを外します
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    CONDA_FILE = "conda.yml"
>    LOCATION = "eastus2" # コンピュートクラスタの場所に置き換えてください
>    ```
>

1. 以下のコマンドを入力して、*setup_ml.py*スクリプトを実行し、Azure Machine Learningのファインチューニングプロセスを開始する。

    ```python
    python setup_ml.py
    ```

1. この演習では、Azure Machine Learning を使用して Phi-3 モデルのファインチューニングに成功しました。setup_ml.py*スクリプトを実行することで、Azure Machine Learning環境をセットアップし、*fine_tune.py*ファイルで定義されたファインチューニングプロセスを開始しました。ファインチューニングプロセスにはかなりの時間がかかることに注意してください。python setup_ml.py` コマンドを実行した後、処理が完了するまで待つ必要があります。ターミナルに表示されるリンクから Azure Machine Learning ポータルにアクセスすることで、ファインチューニングジョブのステータスを監視することができます。

    ![See finetuning job.](../../../../imgs/03/FineTuning-PromptFlow/02-02-see-finetuning-job.png)

### ファインチューニングされたモデルのデプロイ

ファインチューニングしたPhi-3モデルをPrompt Flowに統合するには、モデルをデプロイしてリアルタイム推論にアクセスできるようにする必要があります。このプロセスには、モデルの登録、オンラインエンドポイントの作成、モデルのデプロイが含まれます。

#### デプロイメント用のモデル名、エンドポイント名、デプロイメント名を設定します

1. *config.py* ファイルを開きます。

1. AZURE_MODEL_NAME = 「your_fine_tuned_model_name」`を任意のモデル名に置き換えます。

1. AZURE_ENDPOINT_NAME = 「your_fine_tuned_model_endpoint_name」` を希望のエンドポイント名に置き換えます。

1. AZURE_DEPLOYMENT_NAME = 「your_fine_tuned_model_deployment_name」` を希望のデプロイメント名に置き換えます。

#### *deploy_model.py* ファイルにコードを追加する

deploy_model.py*ファイルを実行すると、デプロイプロセス全体が自動化されます。モデルを登録し、エンドポイントを作成し、モデル名、エンドポイント名、デプロイメント名を含む config.py ファイルで指定された設定に基づいてデプロイメントを実行します。

1. Visual Studio Code で *deploy_model.py* ファイルを開きます。

1. 次のコードを *deploy_model.py* に追加します。

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # 設定のインポート
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        AZURE_MANAGED_IDENTITY_RESOURCE_ID,
        AZURE_MANAGED_IDENTITY_CLIENT_ID,
        AZURE_MODEL_NAME,
        AZURE_ENDPOINT_NAME,
        AZURE_DEPLOYMENT_NAME
    )

    # 定数
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # ログの設定
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def get_ml_client():
        """Initialize and return the ML Client."""
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def register_model(ml_client, model_name, job_name):
        """Register a new model."""
        model_path = f"azureml://jobs/{job_name}/outputs/artifacts/paths/model_output"
        logger.info(f"Registering model {model_name} from job {job_name} at path {model_path}.")
        run_model = Model(
            path=model_path,
            name=model_name,
            description="Model created from run.",
            type=AssetTypes.MLFLOW_MODEL,
        )
        model = ml_client.models.create_or_update(run_model)
        logger.info(f"Registered model ID: {model.id}")
        return model

    def delete_existing_endpoint(ml_client, endpoint_name):
        """Delete existing endpoint if it exists."""
        try:
            endpoint_result = ml_client.online_endpoints.get(name=endpoint_name)
            logger.info(f"Deleting existing endpoint {endpoint_name}.")
            ml_client.online_endpoints.begin_delete(name=endpoint_name).result()
            logger.info(f"Deleted existing endpoint {endpoint_name}.")
        except Exception as e:
            logger.info(f"No existing endpoint {endpoint_name} found to delete: {e}")

    def create_or_update_endpoint(ml_client, endpoint_name, description=""):
        """Create or update an endpoint."""
        delete_existing_endpoint(ml_client, endpoint_name)
        logger.info(f"Creating new endpoint {endpoint_name}.")
        endpoint = ManagedOnlineEndpoint(
            name=endpoint_name,
            description=description,
            identity=IdentityConfiguration(
                type="user_assigned",
                user_assigned_identities=[ManagedIdentityConfiguration(resource_id=AZURE_MANAGED_IDENTITY_RESOURCE_ID)]
            )
        )
        endpoint_result = ml_client.online_endpoints.begin_create_or_update(endpoint).result()
        logger.info(f"Created new endpoint {endpoint_name}.")
        return endpoint_result

    def create_or_update_deployment(ml_client, endpoint_name, deployment_name, model):
        """Create or update a deployment."""

        logger.info(f"Creating deployment {deployment_name} for endpoint {endpoint_name}.")
        deployment = ManagedOnlineDeployment(
            name=deployment_name,
            endpoint_name=endpoint_name,
            model=model.id,
            instance_type=COMPUTE_INSTANCE_TYPE,
            instance_count=1,
            environment_variables=deployment_env_vars,
            request_settings=OnlineRequestSettings(
                max_concurrent_requests_per_instance=3,
                request_timeout_ms=180000,
                max_queue_wait_ms=120000
            ),
            liveness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
            readiness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
        )
        deployment_result = ml_client.online_deployments.begin_create_or_update(deployment).result()
        logger.info(f"Created deployment {deployment.name} for endpoint {endpoint_name}.")
        return deployment_result

    def set_traffic_to_deployment(ml_client, endpoint_name, deployment_name):
        """Set traffic to the specified deployment."""
        try:
            # 現在のエンドポイントの詳細を取得
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)

            # デバッグ用に現在のトラフィック割り当てをログに記録
            logger.info(f"Current traffic allocation: {endpoint.traffic}")

            # デプロイのトラフィック割り当てを設定する
            endpoint.traffic = {deployment_name: 100}

            # 新しいトラフィック割り当てでエンドポイントを更新する
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()

            # デバッグ用に更新されたトラフィック割り当てをログに記録
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # 処理中に発生したエラーをログに記録する
            logger.error(f"Failed to set traffic to deployment: {e}")
            raise


    def main():
        ml_client = get_ml_client()

        registered_model = register_model(ml_client, AZURE_MODEL_NAME, JOB_NAME)
        logger.info(f"Registered model ID: {registered_model.id}")

        endpoint = create_or_update_endpoint(ml_client, AZURE_ENDPOINT_NAME, "Endpoint for finetuned Phi-3 model")
        logger.info(f"Endpoint {AZURE_ENDPOINT_NAME} is ready.")

        try:
            deployment = create_or_update_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME, registered_model)
            logger.info(f"Deployment {AZURE_DEPLOYMENT_NAME} is created for endpoint {AZURE_ENDPOINT_NAME}.")

            set_traffic_to_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME)
            logger.info(f"Traffic is set to deployment {AZURE_DEPLOYMENT_NAME} at endpoint {AZURE_ENDPOINT_NAME}.")
        except Exception as e:
            logger.error(f"Failed to create or update deployment: {e}")

    if __name__ == "__main__":
        main()

    ```

1. `JOB_NAME` を取得するために、以下のタスクを実行します：

    - 作成した Azure Machine Learning リソースに移動する。
    - **Studio web URL** を選択し、Azure Machine Learning ワークスペースを開く。
    - 左側のタブから **Jobs** を選択する。
    - ファインチューニングを行う実験を選択する。例えば、*finetunephi*。
    - 作成したジョブを選択する。
    - 作成したジョブ名をコピーして、*deploy_model.py* ファイルの `JOB_NAME = 「your-job-name」` に貼り付けます。

1. `COMPUTE_INSTANCE_TYPE` を具体的な内容に置き換える。

1. 以下のコマンドを入力して、*deploy_model.py* スクリプトを実行し、Azure Machine Learning のデプロイプロセスを開始する。

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> アカウントへの追加請求を避けるには、Azure Machine Learning ワークスペースで作成したエンドポイントを必ず削除してください。
>

#### Azure Machine Learning Workspaceでのデプロイ状況の確認

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)にアクセスする。

1. 作成した Azure Machine Learning ワークスペースに移動する。

1. Azure Machine Learning ワークスペースを開くには、**Studio web URL** を選択します。

1. 左側のタブから **Endpoints** を選択します。

    ![エンドポイントを選択する。](../../../../imgs/03/FineTuning-PromptFlow/02-03-select-endpoints.png)

1. 作成したエンドポイントを選択します。

    ![作成したエンドポイントを選択する。](../../../../imgs/03/FineTuning-PromptFlow/02-04-select-endpoint-created.png)

1. このページでは、配置プロセス中に作成されたエンドポイントを管理できます。

## シナリオ 3: カスタムモデルでプロンプトフローとチャットを統合する

### カスタムPhi-3モデルと Prompt flow の統合

ファインチューニングしたモデルのデプロイに成功したら、Prompt flow と統合してリアルタイムアプリケーションでモデルを使用することができます。

#### ファインチューニングされたPhi-3モデルのapiキーとエンドポイントURIを設定する

1. 作成した Azure Machine learning ワークスペースに移動する。
1. 左側のタブから **Endpoints** を選択する。
1. 作成したエンドポイントを選択します。
1. ナビゲーションメニューから **Consume** を選択します。
1. AZURE_ML_ENDPOINT=「your_fine_tuned_model_endpoint_uri」`を**RESTエンドポイント**に置き換えて、**RESTエンドポイント**を**config.py*ファイルにコピー＆ペーストします。
1. **プライマリキー** をコピーして *config.py* ファイルに貼り付け、`AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` を **プライマリキー**に置き換えます。

    ![apiキーとエンドポイントURIをコピーする。](../../../../imgs/03/FineTuning-PromptFlow/02-05-copy-apikey-endpoint.png)

#### *flow.dag.yml* ファイルにコードを追加する。

1. Visual Studio Code で *flow.dag.yml* ファイルを開きます。

1. 以下のコードを *flow.dag.yml* に追加します。

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

#### *integrate_with_promptflow.py* ファイルにコードを追加します。

1. Visual Studio Code で *integrate_with_promptflow.py* ファイルを開きます。

1. 以下のコードを *integrate_with_promptflow.py* に追加します。

    ```python
    import logging
    import requests
    from promptflow.core import tool
    import asyncio
    import platform
    from config import (
        AZURE_ML_ENDPOINT,
        AZURE_ML_API_KEY
    )

    # ログの設定
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_azml_endpoint(input_data: list, endpoint_url: str, api_key: str) -> str:
        """
        Azure ML エンドポイントに、与えられた入力データでリクエストを送信します。
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": [input_data],
            "params": {
                "temperature": 0.7,
                "max_new_tokens": 128,
                "do_sample": True,
                "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            result = response.json()[0]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    def setup_asyncio_policy():
        """
        Windows用のasyncioイベントループポリシーを設定する。
        """
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            logger.info("Set Windows asyncio event loop policy.")

    @tool
    def my_python_tool(input_data: str) -> str:
        """
        入力データを処理し、Azure ML エンドポイントに問い合わせるツール関数です。
        """
        setup_asyncio_policy()
        return query_azml_endpoint(input_data, AZURE_ML_ENDPOINT, AZURE_ML_API_KEY)

    ```

### カスタムモデルとチャット

1. 以下のコマンドを入力して、*deploy_model.py* スクリプトを実行し、Azure Machine Learning でデプロイプロセスを開始します。

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. これが結果の例です: これで、カスタムしたファイ3モデルとチャットができるようになりました。ファインチューニングに使用したデータに基づいて質問することをお勧めします。

    ![Prompt flow の例。](../../imgs/03/FineTuning-PromptFlow/02-06-promptflow-example.png)
