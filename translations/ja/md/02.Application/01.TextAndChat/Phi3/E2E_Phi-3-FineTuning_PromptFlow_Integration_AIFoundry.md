# Phi-3 カスタムモデルの微調整と Azure AI Foundry における Prompt flow との統合

このエンドツーエンド (E2E) サンプルは、Microsoft Tech Community のガイド「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)」に基づいています。このサンプルでは、Azure AI Foundry においてカスタム Phi-3 モデルを微調整、デプロイ、および Prompt flow と統合するプロセスを紹介します。  
E2E サンプル「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)」ではローカル環境でコードを実行しましたが、このチュートリアルでは Azure AI / ML Studio 内でモデルを微調整および統合することに焦点を当てています。

## 概要

この E2E サンプルでは、Phi-3 モデルの微調整方法と、Azure AI Foundry 内で Prompt flow と統合する方法を学びます。Azure AI / ML Studio を活用することで、カスタム AI モデルをデプロイおよび利用するためのワークフローを構築します。このサンプルは以下の 3 つのシナリオに分かれています。

**シナリオ 1: Azure リソースの設定と微調整の準備**  
**シナリオ 2: Phi-3 モデルの微調整と Azure Machine Learning Studio へのデプロイ**  
**シナリオ 3: Prompt flow との統合と Azure AI Foundry 内でのカスタムモデルとの対話**

以下はこの E2E サンプルの概要です。

![Phi-3-FineTuning_PromptFlow_Integration 概要図.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.ja.png)

### 目次

1. **[シナリオ 1: Azure リソースの設定と微調整の準備](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Azure Machine Learning ワークスペースを作成する](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [Azure サブスクリプションで GPU クォータをリクエストする](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [ロール割り当てを追加する](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [プロジェクトをセットアップする](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [微調整用のデータセットを準備する](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[シナリオ 2: Phi-3 モデルを微調整して Azure Machine Learning Studio にデプロイする](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [Phi-3 モデルを微調整する](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [微調整した Phi-3 モデルをデプロイする](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

1. **[シナリオ 3: Prompt flow との統合と Azure AI Foundry 内でのカスタムモデルとの対話](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
    - [カスタム Phi-3 モデルを Prompt flow と統合する](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
    - [カスタム Phi-3 モデルと対話する](../../../../../../md/02.Application/01.TextAndChat/Phi3)  

## シナリオ 1: Azure リソースの設定と微調整の準備

### Azure Machine Learning ワークスペースを作成する

1. ポータルページ上部の **検索バー** に「*azure machine learning*」と入力し、表示されるオプションから **Azure Machine Learning** を選択します。

    ![azure machine learning と入力する.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.ja.png)

2. ナビゲーションメニューから **+ 作成** を選択します。

3. ナビゲーションメニューから **新しいワークスペース** を選択します。

    ![新しいワークスペースを選択する.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.ja.png)

4. 以下のタスクを実行します。

    - Azure **サブスクリプション** を選択します。
    - 使用する **リソースグループ** を選択します（必要に応じて新しいものを作成します）。
    - **ワークスペース名** を入力します。一意の値である必要があります。
    - 使用する **リージョン** を選択します。
    - 使用する **ストレージアカウント** を選択します（必要に応じて新しいものを作成します）。
    - 使用する **Key Vault** を選択します（必要に応じて新しいものを作成します）。
    - 使用する **Application Insights** を選択します（必要に応じて新しいものを作成します）。
    - 使用する **コンテナレジストリ** を選択します（必要に応じて新しいものを作成します）。

    ![azure machine learning の情報を入力する.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.ja.png)

5. **確認 + 作成** を選択します。

6. **作成** を選択します。

### Azure サブスクリプションで GPU クォータをリクエストする

このチュートリアルでは、GPU を使用して Phi-3 モデルを微調整およびデプロイします。微調整には *Standard_NC24ads_A100_v4* GPU を使用し、デプロイには *Standard_NC6s_v3* GPU を使用します。それぞれの GPU のクォータリクエストが必要です。

> [!NOTE]
>
> GPU 割り当てが可能なのは Pay-As-You-Go サブスクリプション（標準サブスクリプションタイプ）のみで、現在は特典サブスクリプションはサポートされていません。

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) にアクセスします。

1. *Standard NCADSA100v4 Family* クォータをリクエストするため、以下のタスクを実行します。

    - 左側のタブから **クォータ** を選択します。
    - 使用する **仮想マシンファミリ** を選択します。たとえば、*Standard NCADSA100v4 Family Cluster Dedicated vCPUs* を選択します。このファミリには *Standard_NC24ads_A100_v4* GPU が含まれます。
    - ナビゲーションメニューから **クォータリクエスト** を選択します。

        ![クォータをリクエストする.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.ja.png)

    - クォータリクエストページで、使用したい **新しいコア制限** を入力します（例: 24）。
    - クォータリクエストページで **送信** を選択して GPU クォータをリクエストします。

1. *Standard NCSv3 Family* クォータをリクエストするため、以下のタスクを実行します。

    - 左側のタブから **クォータ** を選択します。
    - 使用する **仮想マシンファミリ** を選択します。たとえば、*Standard NCSv3 Family Cluster Dedicated vCPUs* を選択します。このファミリには *Standard_NC6s_v3* GPU が含まれます。
    - ナビゲーションメニューから **クォータリクエスト** を選択します。
    - クォータリクエストページで、使用したい **新しいコア制限** を入力します（例: 24）。
    - クォータリクエストページで **送信** を選択して GPU クォータをリクエストします。

### ロール割り当てを追加する

モデルを微調整およびデプロイするには、まずユーザー割り当てマネージド ID (UAI) を作成し、適切な権限を割り当てる必要があります。この UAI はデプロイ時の認証に使用されます。

#### ユーザー割り当てマネージド ID (UAI) を作成する

1. ポータルページ上部の **検索バー** に「*managed identities*」と入力し、表示されるオプションから **Managed Identities** を選択します。

    ![managed identities と入力する.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.ja.png)

1. **+ 作成** を選択します。

    ![作成を選択する.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.ja.png)

1. 以下のタスクを実行します。

    - Azure **サブスクリプション** を選択します。
    - 使用する **リソースグループ** を選択します（必要に応じて新しいものを作成します）。
    - 使用する **リージョン** を選択します。
    - **名前** を入力します。一意の値である必要があります。

    ![managed identities を作成する情報を入力する.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.ja.png)

1. **確認 + 作成** を選択します。

1. **作成** を選択します。

#### マネージド ID に Contributor ロールを割り当てる

1. 作成したマネージド ID リソースに移動します。

1. 左側のタブから **Azure ロール割り当て** を選択します。

1. ナビゲーションメニューから **+ ロール割り当てを追加** を選択します。

1. **ロール割り当てを追加** ページで以下のタスクを実行します:
    - **スコープ** を **リソースグループ** に設定します。
    - Azure **サブスクリプション** を選択します。
    - 使用する **リソースグループ** を選択します。
    - **ロール** を **Contributor** に設定します。

    ![Contributor ロールを設定する.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.ja.png)

2. **保存** を選択します。

#### マネージド ID に Storage Blob Data Reader ロールを割り当てる

1. ポータルページ上部の **検索バー** に「*storage accounts*」と入力し、表示されるオプションから **Storage accounts** を選択します。

    ![storage accounts と入力する.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.ja.png)

1. 作成した Azure Machine Learning ワークスペースに関連付けられているストレージアカウントを選択します（例: *finetunephistorage*）。

1. 以下のタスクを実行して **ロール割り当てを追加** ページに移動します:

    - 作成した Azure ストレージアカウントに移動します。
    - 左側のタブから **アクセス制御 (IAM)** を選択します。
    - ナビゲーションメニューから **+ 追加** を選択します。
    - ナビゲーションメニューから **ロール割り当てを追加** を選択します。

    ![ロールを追加する.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.ja.png)

1. **ロール割り当てを追加** ページで以下のタスクを実行します:

    - **ロール** ページで **Storage Blob Data Reader** と入力し、表示されるオプションから **Storage Blob Data Reader** を選択します。
    - **ロール** ページで **次へ** を選択します。
    - **メンバー** ページで **アクセスを割り当てる対象** を **Managed identity** に設定します。
    - **メンバー** ページで **+ メンバーを選択** を選択します。
    - **マネージド ID を選択** ページで Azure **サブスクリプション** を選択します。
    - **マネージド ID を選択** ページで **マネージド ID** を **Manage Identity** に設定します。
    - **マネージド ID を選択** ページで作成したマネージド ID を選択します（例: *finetunephi-managedidentity*）。
    - **マネージド ID を選択** ページで **選択** を選択します。

    ![マネージド ID を選択する.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.ja.png)

1. **確認 + 割り当て** を選択します。

#### マネージド ID に AcrPull ロールを割り当てる

1. ポータルページ上部の **検索バー** に「*container registries*」と入力し、表示されるオプションから **Container registries** を選択します。

    ![container registries と入力する.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.ja.png)

1. Azure Machine Learning ワークスペースに関連付けられているコンテナレジストリを選択します（例: *finetunephicontainerregistry*）。

1. 以下のタスクを実行して **ロール割り当てを追加** ページに移動します:

    - 左側のタブから **アクセス制御 (IAM)** を選択します。
    - ナビゲーションメニューから **+ 追加** を選択します。
    - ナビゲーションメニューから **ロール割り当てを追加** を選択します。

1. **ロール割り当てを追加** ページで以下のタスクを実行します:

    - **ロール** ページで **AcrPull** と入力し、表示されるオプションから **AcrPull** を選択します。
    - **ロール** ページで **次へ** を選択します。
    - **メンバー** ページで **アクセスを割り当てる対象** を **Managed identity** に設定します。
    - **メンバー** ページで **+ メンバーを選択** を選択します。
    - **マネージド ID を選択** ページで Azure **サブスクリプション** を選択します。
    - **マネージド ID を選択** ページで **マネージド ID** を **Manage Identity** に設定します。
    - **マネージド ID を選択** ページで作成したマネージド ID を選択します（例: *finetunephi-managedidentity*）。
    - **マネージド ID を選択** ページで **選択** を選択します。
    - **確認 + 割り当て** を選択します。

### プロジェクトをセットアップする

微調整に必要なデータセットをダウンロードするため、ローカル環境をセットアップします。

この演習では以下を行います:

- 作業用フォルダを作成する。
- 仮想環境を作成する。
- 必要なパッケージをインストールする。
- データセットをダウンロードするための *download_dataset.py* ファイルを作成する。

#### 作業用フォルダを作成する

1. ターミナルウィンドウを開き、以下のコマンドを入力してデフォルトのパスに *finetune-phi* という名前のフォルダを作成します。

    ```console
    mkdir finetune-phi
    ```

2. 作成した *finetune-phi* フォルダに移動するには、以下のコマンドを入力します。

    ```console
    cd finetune-phi
    ```

#### 仮想環境を作成する

1. 以下のコマンドを入力して *.venv* という名前の仮想環境を作成します。

    ```console
    python -m venv .venv
    ```

2. 仮想環境を有効化するには、以下のコマンドを入力します。

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> 成功すると、コマンドプロンプトの前に *(.venv)* が表示されます。

#### 必要なパッケージをインストールする

1. 以下のコマンドを入力して必要なパッケージをインストールします。

    ```console
    pip install datasets==2.19.1
    ```

#### `download_dataset.py` を作成する

> [!NOTE]
> 完全なフォルダ構造:
>
> @@CODE_BLOCK_5
1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) を開きます。

1. 左側のタブから **Compute** を選択します。

1. ナビゲーションメニューから **Compute clusters** を選択します。

1. **+ New** を選択します。

    ![Compute を選択します。](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.ja.png)

1. 以下のタスクを実行します：

    - 使用したい **Region** を選択します。
    - **Virtual machine tier** を **Dedicated** に設定します。
    - **Virtual machine type** を **GPU** に設定します。
    - **Virtual machine size** のフィルタを **Select from all options** に設定します。
    - **Virtual machine size** を **Standard_NC24ads_A100_v4** に設定します。

    ![クラスターを作成します。](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.ja.png)

1. **Next** を選択します。

1. 以下のタスクを実行します：

    - **Compute name** を入力します。一意の値である必要があります。
    - **Minimum number of nodes** を **0** に設定します。
    - **Maximum number of nodes** を **1** に設定します。
    - **Idle seconds before scale down** を **120** に設定します。

    ![クラスターを作成します。](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.ja.png)

1. **Create** を選択します。

#### Phi-3 モデルのファインチューニング

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) を開きます。

1. 作成した Azure Machine Learning ワークスペースを選択します。

    ![作成したワークスペースを選択します。](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.ja.png)

1. 以下のタスクを実行します：

    - 左側のタブから **Model catalog** を選択します。
    - **検索バー**に *phi-3-mini-4k* と入力し、表示されるオプションから **Phi-3-mini-4k-instruct** を選択します。

    ![phi-3-mini-4k と入力します。](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.ja.png)

1. ナビゲーションメニューから **Fine-tune** を選択します。

    ![ファインチューニングを選択します。](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.ja.png)

1. 以下のタスクを実行します：

    - **Select task type** を **Chat completion** に設定します。
    - **+ Select data** を選択して **Traning data** をアップロードします。
    - 検証データのアップロードタイプを **Provide different validation data** に設定します。
    - **+ Select data** を選択して **Validation data** をアップロードします。

    ![ファインチューニングページを記入します。](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.ja.png)

    > [!TIP]
    >
    > **Advanced settings** を選択して、**learning_rate** や **lr_scheduler_type** などの設定をカスタマイズし、ファインチューニングプロセスを最適化することができます。

1. **Finish** を選択します。

1. この演習では、Azure Machine Learning を使用して Phi-3 モデルのファインチューニングを成功させました。ファインチューニングプロセスにはかなりの時間がかかる場合があります。ジョブを実行した後は完了するまで待つ必要があります。Azure Machine Learning ワークスペースの左側の **Jobs** タブに移動して、ファインチューニングジョブのステータスを監視できます。次のシリーズでは、ファインチューニングされたモデルをデプロイし、Prompt flow と統合します。

    ![ファインチューニングジョブを確認します。](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.ja.png)

### ファインチューニングされた Phi-3 モデルのデプロイ

ファインチューニングされた Phi-3 モデルを Prompt flow と統合するには、モデルをデプロイしてリアルタイム推論にアクセス可能にする必要があります。このプロセスには、モデルの登録、オンラインエンドポイントの作成、およびモデルのデプロイが含まれます。

この演習では以下を行います：

- ファインチューニングされたモデルを Azure Machine Learning ワークスペースに登録します。
- オンラインエンドポイントを作成します。
- 登録されたファインチューニング済み Phi-3 モデルをデプロイします。

#### ファインチューニングされたモデルの登録

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) を開きます。

1. 作成した Azure Machine Learning ワークスペースを選択します。

    ![作成したワークスペースを選択します。](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.ja.png)

1. 左側のタブから **Models** を選択します。
1. **+ Register** を選択します。
1. **From a job output** を選択します。

    ![モデルを登録します。](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.ja.png)

1. 作成したジョブを選択します。

    ![ジョブを選択します。](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.ja.png)

1. **Next** を選択します。

1. **Model type** を **MLflow** に設定します。

1. **Job output** が選択されていることを確認します（自動的に選択されているはずです）。

    ![出力を選択します。](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.ja.png)

2. **Next** を選択します。

3. **Register** を選択します。

    ![登録を選択します。](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.ja.png)

4. 左側のタブから **Models** メニューに移動して、登録されたモデルを確認できます。

    ![登録されたモデル。](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.ja.png)

#### ファインチューニングされたモデルのデプロイ

1. 作成した Azure Machine Learning ワークスペースに移動します。

1. 左側のタブから **Endpoints** を選択します。

1. ナビゲーションメニューから **Real-time endpoints** を選択します。

    ![エンドポイントを作成します。](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.ja.png)

1. **Create** を選択します。

1. 登録されたモデルを選択します。

    ![登録されたモデルを選択します。](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.ja.png)

1. **Select** を選択します。

1. 以下のタスクを実行します：

    - **Virtual machine** を *Standard_NC6s_v3* に設定します。
    - 使用する **Instance count** を選択します（例：*1*）。
    - **Endpoint** を **New** に設定して新しいエンドポイントを作成します。
    - **Endpoint name** を入力します。一意の値である必要があります。
    - **Deployment name** を入力します。一意の値である必要があります。

    ![デプロイ設定を記入します。](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.ja.png)

1. **Deploy** を選択します。

> [!WARNING]
> アカウントに追加の課金が発生しないように、Azure Machine Learning ワークスペースで作成したエンドポイントを削除することを忘れないでください。
>

#### Azure Machine Learning ワークスペースでデプロイステータスを確認する

1. 作成した Azure Machine Learning ワークスペースに移動します。

1. 左側のタブから **Endpoints** を選択します。

1. 作成したエンドポイントを選択します。

    ![エンドポイントを選択します。](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.ja.png)

1. このページでは、デプロイプロセス中にエンドポイントを管理できます。

> [!NOTE]
> デプロイが完了したら、**Live traffic** が **100%** に設定されていることを確認してください。設定されていない場合は、**Update traffic** を選択してトラフィック設定を調整してください。トラフィックが 0% に設定されている場合、モデルをテストすることはできません。
>
> ![トラフィックを設定します。](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.ja.png)
>

## シナリオ 3: Prompt flow と統合し、カスタムモデルを Azure AI Foundry で使用する

### カスタム Phi-3 モデルを Prompt flow と統合する

ファインチューニング済みモデルをデプロイした後、Prompt Flow に統合してリアルタイムアプリケーションでモデルを使用できるようになります。これにより、カスタム Phi-3 モデルを使用してさまざまなインタラクティブタスクを実行することが可能になります。

この演習では以下を行います：

- Azure AI Foundry Hub を作成します。
- Azure AI Foundry Project を作成します。
- Prompt flow を作成します。
- ファインチューニング済み Phi-3 モデル用のカスタム接続を追加します。
- Prompt flow を設定してカスタム Phi-3 モデルとチャットします。

> [!NOTE]
> Azure ML Studio を使用して Promptflow と統合することもできます。同じ統合プロセスを Azure ML Studio に適用することが可能です。

#### Azure AI Foundry Hub を作成する

Project を作成する前に Hub を作成する必要があります。Hub はリソースグループのような役割を果たし、Azure AI Foundry 内で複数の Project を整理および管理できます。

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) を開きます。

1. 左側のタブから **All hubs** を選択します。

1. ナビゲーションメニューから **+ New hub** を選択します。

    ![Hub を作成します。](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.ja.png)

1. 以下のタスクを実行します：

    - **Hub name** を入力します。一意の値である必要があります。
    - 使用する Azure **Subscription** を選択します。
    - 使用する **Resource group** を選択します（必要に応じて新規作成します）。
    - 使用したい **Location** を選択します。
    - 使用する **Connect Azure AI Services** を選択します（必要に応じて新規作成します）。
    - **Connect Azure AI Search** を **Skip connecting** に設定します。

    ![Hub を記入します。](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.ja.png)

1. **Next** を選択します。

#### Azure AI Foundry Project を作成する

1. 作成した Hub で、左側のタブから **All projects** を選択します。

1. ナビゲーションメニューから **+ New project** を選択します。

    ![新しいプロジェクトを選択します。](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.ja.png)

1. **Project name** を入力します。一意の値である必要があります。

    ![プロジェクトを作成します。](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.ja.png)

1. **Create a project** を選択します。

#### ファインチューニング済み Phi-3 モデル用のカスタム接続を追加する

カスタム Phi-3 モデルを Prompt flow に統合するには、モデルのエンドポイントとキーをカスタム接続に保存する必要があります。この設定により、Prompt flow でカスタム Phi-3 モデルにアクセスできるようになります。

#### ファインチューニング済み Phi-3 モデルの API キーとエンドポイント URI を設定する

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) を開きます。

1. 作成した Azure Machine Learning ワークスペースに移動します。

1. 左側のタブから **Endpoints** を選択します。

    ![エンドポイントを選択します。](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.ja.png)

1. 作成したエンドポイントを選択します。

    ![作成したエンドポイントを選択します。](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.ja.png)

1. ナビゲーションメニューから **Consume** を選択します。

1. **REST endpoint** と **Primary key** をコピーします。
![APIキーとエンドポイントURIをコピーします。](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.ja.png)

#### カスタム接続を追加する

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)を開きます。

1. 作成したAzure AI Foundryプロジェクトに移動します。

1. 作成したプロジェクトで、左側のタブから**Settings**を選択します。

1. **+ New connection**を選択します。

    ![新しい接続を選択します。](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.ja.png)

1. ナビゲーションメニューから**Custom keys**を選択します。

    ![カスタムキーを選択します。](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.ja.png)

1. 以下の作業を行います：

    - **+ Add key value pairs**を選択します。
    - キー名に**endpoint**を入力し、Azure ML Studioからコピーしたエンドポイントを値フィールドに貼り付けます。
    - 再度**+ Add key value pairs**を選択します。
    - キー名に**key**を入力し、Azure ML Studioからコピーしたキーを値フィールドに貼り付けます。
    - キーを追加した後、**is secret**を選択してキーが公開されないようにします。

    ![接続を追加します。](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.ja.png)

1. **Add connection**を選択します。

#### Prompt flowを作成する

Azure AI Foundryにカスタム接続を追加しました。次に、以下の手順を使用してPrompt flowを作成します。その後、このPrompt flowをカスタム接続に接続し、Prompt flow内でファインチューニング済みモデルを使用できるようにします。

1. 作成したAzure AI Foundryプロジェクトに移動します。

1. 左側のタブから**Prompt flow**を選択します。

1. ナビゲーションメニューから**+ Create**を選択します。

    ![Prompt flowを選択します。](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.ja.png)

1. ナビゲーションメニューから**Chat flow**を選択します。

    ![Chat flowを選択します。](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.ja.png)

1. 使用する**Folder name**を入力します。

    ![名前を入力します。](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.ja.png)

2. **Create**を選択します。

#### カスタムPhi-3モデルとチャットするためのPrompt flowを設定する

ファインチューニング済みのPhi-3モデルをPrompt flowに統合する必要があります。ただし、提供されている既存のPrompt flowはこの目的には設計されていません。そのため、カスタムモデルを統合できるようにPrompt flowを再設計する必要があります。

1. Prompt flow内で、以下の作業を行い既存のフローを再構築します：

    - **Raw file mode**を選択します。
    - *flow.dag.yml*ファイル内の既存のコードをすべて削除します。
    - 以下のコードを*flow.dag.yml*ファイルに追加します。

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

    - **Save**を選択します。

    ![Raw file modeを選択します。](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.ja.png)

1. カスタムPhi-3モデルをPrompt flowで使用するために、以下のコードを*integrate_with_promptflow.py*ファイルに追加します。

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
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
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Prompt flowコードを貼り付けます。](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.ja.png)

> [!NOTE]
> Azure AI FoundryでPrompt flowを使用する方法についての詳細は、[Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)を参照してください。

1. **Chat input**と**Chat output**を選択し、モデルとのチャットを有効にします。

    ![Input Outputを選択します。](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.ja.png)

1. これでカスタムPhi-3モデルとのチャットが可能になりました。次の演習では、Prompt flowを起動し、ファインチューニング済みPhi-3モデルとのチャットを行う方法を学びます。

> [!NOTE]
>
> 再構築されたフローは以下の画像のようになります：
>
> ![フロー例。](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.ja.png)
>

### カスタムPhi-3モデルとのチャット

ファインチューニングを行い、カスタムPhi-3モデルをPrompt flowに統合したので、これでモデルと対話を開始する準備が整いました。この演習では、Prompt flowを使用してモデルとのチャットを設定し開始する手順を説明します。これにより、ファインチューニング済みPhi-3モデルの機能をさまざまなタスクや会話で最大限に活用できるようになります。

- Prompt flowを使用してカスタムPhi-3モデルとチャットします。

#### Prompt flowを開始する

1. **Start compute sessions**を選択してPrompt flowを開始します。

    ![コンピュートセッションを開始します。](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.ja.png)

1. **Validate and parse input**を選択してパラメータを更新します。

    ![入力を検証します。](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.ja.png)

1. **connection**の**Value**に作成したカスタム接続を選択します。例：*connection*。

    ![接続を選択します。](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.ja.png)

#### カスタムモデルとチャットする

1. **Chat**を選択します。

    ![チャットを選択します。](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.ja.png)

1. 以下は結果の例です：これでカスタムPhi-3モデルとチャットできます。ファインチューニングに使用したデータに基づいた質問をすることをお勧めします。

    ![Prompt flowでチャットします。](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.ja.png)

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確さが含まれる可能性があります。元の言語で記載された原文を信頼できる情報源としてご参照ください。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や解釈の誤りについて、当方は一切の責任を負いかねます。