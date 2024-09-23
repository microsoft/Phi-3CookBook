# カスタム Phi-3 モデルを Azure AI Studio の Prompt Flow で微調整し統合する

このエンドツーエンド (E2E) サンプルは、Microsoft Tech Community のガイド「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Studio](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)」に基づいています。Azure AI Studio でカスタム Phi-3 モデルを微調整、デプロイ、および Prompt Flow と統合するプロセスを紹介します。
このチュートリアルは、ローカルでコードを実行する「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)」とは異なり、Azure AI / ML Studio 内でモデルを微調整および統合することに焦点を当てています。

## 概要

このエンドツーエンド (E2E) サンプルでは、Phi-3 モデルを微調整し、Azure AI Studio の Prompt Flow と統合する方法を学びます。Azure AI / ML Studio を活用することで、カスタム AI モデルをデプロイおよび利用するためのワークフローを確立します。この E2E サンプルは以下の 3 つのシナリオに分かれています：

**シナリオ 1: Azure リソースを設定し、微調整の準備をする**

**シナリオ 2: Phi-3 モデルを微調整し、Azure Machine Learning Studio にデプロイする**

**シナリオ 3: Prompt Flow と統合し、Azure AI Studio でカスタムモデルとチャットする**

以下はこの E2E サンプルの概要です。

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../translated_images/00-01-architecture.fa40b38b29f795863378026c4dcc3007b0938b0b43afaf8c331906d03742b2e6.ja.png)

### 目次

1. **[シナリオ 1: Azure リソースを設定し、微調整の準備をする](../../../../md/06.E2ESamples)**
    - [Azure Machine Learning ワークスペースを作成する](../../../../md/06.E2ESamples)
    - [Azure サブスクリプションで GPU クォータをリクエストする](../../../../md/06.E2ESamples)
    - [ロール割り当てを追加する](../../../../md/06.E2ESamples)
    - [プロジェクトを設定する](../../../../md/06.E2ESamples)
    - [微調整用のデータセットを準備する](../../../../md/06.E2ESamples)

1. **[シナリオ 2: Phi-3 モデルを微調整し、Azure Machine Learning Studio にデプロイする](../../../../md/06.E2ESamples)**
    - [Phi-3 モデルを微調整する](../../../../md/06.E2ESamples)
    - [微調整された Phi-3 モデルをデプロイする](../../../../md/06.E2ESamples)

1. **[シナリオ 3: Prompt Flow と統合し、Azure AI Studio でカスタムモデルとチャットする](../../../../md/06.E2ESamples)**
    - [カスタム Phi-3 モデルを Prompt Flow と統合する](../../../../md/06.E2ESamples)
    - [カスタム Phi-3 モデルとチャットする](../../../../md/06.E2ESamples)

## シナリオ 1: Azure リソースを設定し、微調整の準備をする

### Azure Machine Learning ワークスペースを作成する

1. ポータルページの上部にある**検索バー**に *azure machine learning* と入力し、表示されたオプションから **Azure Machine Learning** を選択します。

    ![Type azure machine learning.](../../../../translated_images/01-01-type-azml.98b3003c07da4dbb6885400f66988b3ae05767edb5e8b8ef480e584abe379ca7.ja.png)

2. ナビゲーションメニューから **+ Create** を選択します。

3. ナビゲーションメニューから **New workspace** を選択します。

    ![Select new workspace.](../../../../translated_images/01-02-select-new-workspace.7648b384cbd786565740c0e5ea203d4710889d5ef23a2abf08428444f6d1a2a6.ja.png)

4. 以下のタスクを実行します：

    - Azure **サブスクリプション**を選択します。
    - 使用する**リソースグループ**を選択します（必要に応じて新しいものを作成します）。
    - **ワークスペース名**を入力します。これは一意の値でなければなりません。
    - 使用する**リージョン**を選択します。
    - 使用する**ストレージアカウント**を選択します（必要に応じて新しいものを作成します）。
    - 使用する**キーコンテナ**を選択します（必要に応じて新しいものを作成します）。
    - 使用する**アプリケーションインサイト**を選択します（必要に応じて新しいものを作成します）。
    - 使用する**コンテナレジストリ**を選択します（必要に応じて新しいものを作成します）。

    ![Fill azure machine learning.](../../../../translated_images/01-03-fill-AZML.a3f644231a76859c7d92134b7dea1dd0d4df1c11cc615351c95be5a2c7056b03.ja.png)

5. **Review + Create** を選択します。

6. **Create** を選択します。

### Azure サブスクリプションで GPU クォータをリクエストする

このチュートリアルでは、GPU を使用して Phi-3 モデルを微調整およびデプロイする方法を学びます。微調整には *Standard_NC24ads_A100_v4* GPU を使用し、デプロイには *Standard_NC6s_v3* GPU を使用します。これらの GPU にはクォータリクエストが必要です。

> [!NOTE]
>
> GPU 割り当ての対象となるのは、従量課金制のサブスクリプション（標準のサブスクリプションタイプ）のみであり、特典サブスクリプションは現在サポートされていません。
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) にアクセスします。

1. *Standard NCADSA100v4 Family* クォータをリクエストするために、以下のタスクを実行します：

    - 左側のタブから **Quota** を選択します。
    - 使用する **Virtual machine family** を選択します。例えば、*Standard NCADSA100v4 Family Cluster Dedicated vCPUs* を選択します。これには *Standard_NC24ads_A100_v4* GPU が含まれます。
    - ナビゲーションメニューから **Request quota** を選択します。

        ![Request quota.](../../../../translated_images/02-02-request-quota.55f797113d95ad20ca91943eed637488d0aa51d61f3bbe7f080ec466b2ae0666.ja.png)

    - Request quota ページで、使用したい **New cores limit** を入力します。例えば、24。
    - Request quota ページで、**Submit** を選択して GPU クォータをリクエストします。

1. *Standard NCSv3 Family* クォータをリクエストするために、以下のタスクを実行します：

    - 左側のタブから **Quota** を選択します。
    - 使用する **Virtual machine family** を選択します。例えば、*Standard NCSv3 Family Cluster Dedicated vCPUs* を選択します。これには *Standard_NC6s_v3* GPU が含まれます。
    - ナビゲーションメニューから **Request quota** を選択します。
    - Request quota ページで、使用したい **New cores limit** を入力します。例えば、24。
    - Request quota ページで、**Submit** を選択して GPU クォータをリクエストします。

### ロール割り当てを追加する

モデルを微調整およびデプロイするには、まずユーザー割り当てマネージドアイデンティティ (UAI) を作成し、適切な権限を割り当てる必要があります。この UAI はデプロイ時の認証に使用されます。

#### ユーザー割り当てマネージドアイデンティティ (UAI) を作成する

1. ポータルページの上部にある**検索バー**に *managed identities* と入力し、表示されたオプションから **Managed Identities** を選択します。

    ![Type managed identities.](../../../../translated_images/03-01-type-managed-identities.2f7b07daa34dc15303b6a3f8c364bc0b7e892dd18aaff361440a030621b540b8.ja.png)

1. **+ Create** を選択します。

    ![Select create.](../../../../translated_images/03-02-select-create.0bde775b318f4adba24a7637b31f00f9b685214ed225c5123845a215a260ac71.ja.png)

1. 以下のタスクを実行します：

    - Azure **サブスクリプション**を選択します。
    - 使用する**リソースグループ**を選択します（必要に応じて新しいものを作成します）。
    - 使用する**リージョン**を選択します。
    - **名前**を入力します。これは一意の値でなければなりません。

    ![Select create.](../../../../translated_images/03-03-fill-managed-identities-1.688009e629c1e6952853b94022d3fe97c659c34e29908db17218a5cab6d6add1.ja.png)

1. **Review + create** を選択します。

1. **+ Create** を選択します。

#### マネージドアイデンティティに Contributor ロールを割り当てる

1. 作成したマネージドアイデンティティリソースに移動します。

1. 左側のタブから **Azure role assignments** を選択します。

1. ナビゲーションメニューから **+Add role assignment** を選択します。

1. Add role assignment ページで、以下のタスクを実行します：
    - **Scope** を **Resource group** に設定します。
    - Azure **サブスクリプション**を選択します。
    - 使用する**リソースグループ**を選択します。
    - **Role** を **Contributor** に設定します。

    ![Fill contributor role.](../../../../translated_images/03-04-fill-contributor-role.8bc54b3ac8f64842c82b3379f3c3e9f8d778abf28c00e5b7b471935a86d3ae64.ja.png)

1. **Save** を選択します。

#### マネージドアイデンティティに Storage Blob Data Reader ロールを割り当てる

1. ポータルページの上部にある**検索バー**に *storage accounts* と入力し、表示されたオプションから **Storage accounts** を選択します。

    ![Type storage accounts.](../../../../translated_images/03-05-type-storage-accounts.236987db35ba863124c6de8dd16533fe35b96ee4e2dcb9d67e6b279a285f0e6d.ja.png)

1. 作成した Azure Machine Learning ワークスペースに関連付けられたストレージアカウントを選択します。例えば、*finetunephistorage*。

1. Add role assignment ページに移動するために以下のタスクを実行します：

    - 作成した Azure ストレージアカウントに移動します。
    - 左側のタブから **Access Control (IAM)** を選択します。
    - ナビゲーションメニューから **+ Add** を選択します。
    - ナビゲーションメニューから **Add role assignment** を選択します。

    ![Add role.](../../../../translated_images/03-06-add-role.dde49177fe7ce1cd1604f620ca5c8ac6442fc516effb057e9f74645f35f9d038.ja.png)

1. Add role assignment ページで、以下のタスクを実行します：

    - Role ページで **Storage Blob Data Reader** と入力し、表示されたオプションから **Storage Blob Data Reader** を選択します。
    - Role ページで **Next** を選択します。
    - Members ページで **Assign access to** を **Managed identity** に設定します。
    - Members ページで **+ Select members** を選択します。
    - Select managed identities ページで Azure **サブスクリプション**を選択します。
    - Select managed identities ページで **Managed identity** を **Manage Identity** に設定します。
    - Select managed identities ページで作成したマネージドアイデンティティを選択します。例えば、*finetunephi-managedidentity*。
    - Select managed identities ページで **Select** を選択します。

    ![Select managed identity.](../../../../translated_images/03-08-select-managed-identity.f9a44699bf247a4583e2d377e304de8c3d8a602b7d3fed52b9ae790e64e94fe9.ja.png)

1. **Review + assign** を選択します。

#### マネージドアイデンティティに AcrPull ロールを割り当てる

1. ポータルページの上部にある**検索バー**に *container registries* と入力し、表示されたオプションから **Container registries** を選択します。

    ![Type container registries.](../../../../translated_images/03-09-type-container-registries.b5519f1fbf49bff0c0d4c95deecd2ef0c61b4870119886c3661014435e2b7095.ja.png)

1. Azure Machine Learning ワークスペースに関連付けられたコンテナレジストリを選択します。例えば、*finetunephicontainerregistry*

1. Add role assignment ページに移動するために以下のタスクを実行します：

    - 左側のタブから **Access Control (IAM)** を選択します。
    - ナビゲーションメニューから **+ Add** を選択します。
    - ナビゲーションメニューから **Add role assignment** を選択します。

1. Add role assignment ページで、以下のタスクを実行します：

    - Role ページで **AcrPull** と入力し、表示されたオプションから **AcrPull** を選択します。
    - Role ページで **Next** を選択します。
    - Members ページで **Assign access to** を **Managed identity** に設定します。
    - Members ページで **+ Select members** を選択します。
    - Select managed identities ページで Azure **サブスクリプション**を選択します。
    - Select managed identities ページで **Managed identity** を **Manage Identity** に設定します。
    - Select managed identities ページで作成したマネージドアイデンティティを選択します。例えば、*finetunephi-managedidentity*。
    - Select managed identities ページで **Select** を選択します。
    - **Review + assign** を選択します。

### プロジェクトを設定する

微調整に必要なデータセットをダウンロードするために、ローカル環境を設定します。

この演習では、以下のことを行います：

- 作業用のフォルダを作成します。
- 仮想環境を作成します。
- 必要なパッケージをインストールします。
- データセットをダウンロードするための *download_dataset.py* ファイルを作成します。

#### 作業用のフォルダを作成する

1. ターミナルウィンドウを開き、以下のコマンドを入力してデフォルトのパスに *finetune-phi* フォルダを作成します。

    ```console
    mkdir finetune-phi
    ```

2. ターミナル内で以下のコマンドを入力して作成した *finetune-phi* フォルダに移動します。

    ```console
    cd finetune-phi
    ```

#### 仮想環境を作成する

1. ターミナル内で以下のコマンドを入力して *.venv* という名前の仮想環境を作成します。

    ```console
    python -m venv .venv
    ```

2. ターミナル内で以下のコマンドを入力して仮想環境をアクティブにします。

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> 成功すると、コマンドプロンプトの前に *(.venv)* が表示されます。

#### 必要なパッケージをインストールする

1. ターミナル内で以下のコマンドを入力して必要なパッケージをインストールします。

    ```console
    pip install datasets==2.19.1
    ```

#### `download_dataset.py` を作成する

> [!NOTE]
> 完全なフォルダ構造：
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code** を開きます。

1. メニューバーから **File** を選択します。

1. **Open Folder** を選択します。

1. 作成した *finetune-phi* フォルダを選択します。これは *C:\Users\yourUserName\finetune-phi* にあります。

    ![Select the folder that you created.](../../../../translated_images/04-01-open-project-folder.f5e2b4ce1cb596eae857303b12909dc0174fd99129d6944c41079f24ee17eed2.ja.png)

1. Visual Studio Code の左ペインで右クリックして **New File** を選択し、*download_dataset.py* という名前の新しいファイルを作成します。

    ![Create a new file.](../../imgs/03/FineTuning-PromptFlow-AIStudio/04-02-create-new
1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) を訪問します。

1. 左側のタブから **Compute** を選択します。

1. ナビゲーションメニューから **Compute clusters** を選択します。

1. **+ New** を選択します。

    ![Select compute.](../../../../translated_images/06-01-select-compute.69422609cf19921fb16f550b2566e00870f63ba0caf66b0d26b34e6b0ed21a68.ja.png)

1. 以下のタスクを実行します:

    - 使用したい **Region** を選択します。
    - **Virtual machine tier** を **Dedicated** に設定します。
    - **Virtual machine type** を **GPU** に設定します。
    - **Virtual machine size** フィルターを **Select from all options** に設定します。
    - **Virtual machine size** を **Standard_NC24ads_A100_v4** に設定します。

    ![Create cluster.](../../../../translated_images/06-02-create-cluster.ad68bcb0914b62972408da8f925632977c54248ff99d2c45761f7e3d33f40fe1.ja.png)

1. **Next** を選択します。

1. 以下のタスクを実行します:

    - **Compute name** を入力します。これは一意の値でなければなりません。
    - **Minimum number of nodes** を **0** に設定します。
    - **Maximum number of nodes** を **1** に設定します。
    - **Idle seconds before scale down** を **120** に設定します。

    ![Create cluster.](../../../../translated_images/06-03-create-cluster.f36399780462ff69f62b9bdf22180d6824b00cdc913fe2a639dde3e4b9eaa43e.ja.png)

1. **Create** を選択します。

#### Phi-3 モデルのファインチューニング

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) を訪問します。

1. 作成した Azure Machine Learning ワークスペースを選択します。

    ![Select workspace that you created.](../../../../translated_images/06-04-select-workspace.5e35488b3bb3e391ead6688243c52fc2aecb8ae7f1c738b91b49580f9db353cf.ja.png)

1. 以下のタスクを実行します:

    - 左側のタブから **Model catalog** を選択します。
    - **検索バー** に *phi-3-mini-4k* と入力し、表示されるオプションから **Phi-3-mini-4k-instruct** を選択します。

    ![Type phi-3-mini-4k.](../../../../translated_images/06-05-type-phi-3-mini-4k.7461addd95ede137f6f018a29681762f85e063477ded6043aafbdf6d742a54e8.ja.png)

1. ナビゲーションメニューから **Fine-tune** を選択します。

    ![Select fine tune.](../../../../translated_images/06-06-select-fine-tune.2c678a7f33294c16ae3ad30ce5d4a78600013dc3a0227e8d341a1962f3aff84d.ja.png)

1. 以下のタスクを実行します:

    - **Select task type** を **Chat completion** に設定します。
    - **+ Select data** を選択して **Traning data** をアップロードします。
    - Validation data のアップロードタイプを **Provide different validation data** に設定します。
    - **+ Select data** を選択して **Validation data** をアップロードします。

    ![Fill fine-tuning page.](../../../../translated_images/06-07-fill-finetuning.c76431cc247b6398fb9d33da62841adf87d5eebaa92cd79e80bd7bcbed49f1d3.ja.png)

    > [!TIP]
    >
    > **Advanced settings** を選択して、**learning_rate** や **lr_scheduler_type** などの設定をカスタマイズし、特定のニーズに合わせてファインチューニングプロセスを最適化できます。

1. **Finish** を選択します。

1. この演習では、Azure Machine Learning を使用して Phi-3 モデルのファインチューニングに成功しました。ファインチューニングプロセスはかなりの時間がかかることがあります。ファインチューニングジョブを実行した後、その完了を待つ必要があります。Azure Machine Learning Workspace の左側のタブの Jobs に移動して、ファインチューニングジョブのステータスを監視できます。次のシリーズでは、ファインチューニングされたモデルをデプロイし、Prompt flow と統合します。

    ![See finetuning job.](../../../../translated_images/06-08-output.9f9cf6f9e9e83533b793a5ff3066b09475e299999fead6f98dfb102f48db0061.ja.png)

### ファインチューニングされた Phi-3 モデルのデプロイ

ファインチューニングされた Phi-3 モデルを Prompt flow と統合するには、モデルをデプロイしてリアルタイム推論にアクセスできるようにする必要があります。このプロセスには、モデルの登録、オンラインエンドポイントの作成、およびモデルのデプロイが含まれます。

この演習では、以下を行います:

- ファインチューニングされたモデルを Azure Machine Learning ワークスペースに登録します。
- オンラインエンドポイントを作成します。
- 登録されたファインチューニングされた Phi-3 モデルをデプロイします。

#### ファインチューニングされたモデルの登録

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) を訪問します。

1. 作成した Azure Machine Learning ワークスペースを選択します。

    ![Select workspace that you created.](../../../../translated_images/06-04-select-workspace.5e35488b3bb3e391ead6688243c52fc2aecb8ae7f1c738b91b49580f9db353cf.ja.png)

1. 左側のタブから **Models** を選択します。
1. **+ Register** を選択します。
1. **From a job output** を選択します。

    ![Register model.](../../../../translated_images/07-01-register-model.9b64d29736e0be32343b36a503d7e38c47c22d9edfa554aae179352982fdf96b.ja.png)

1. 作成したジョブを選択します。

    ![Select job.](../../../../translated_images/07-02-select-job.712abf18cdae5256776907df3ed30df53d297ff8d475fb64d5c03e92304db6ef.ja.png)

1. **Next** を選択します。

1. **Model type** を **MLflow** に設定します。

1. **Job output** が選択されていることを確認します。自動的に選択されているはずです。

    ![Select output.](../../../../translated_images/07-03-select-output.45098161b7ddfda4b8d4d62676da0488a32a16e838ff03f37bfd71b9886da798.ja.png)

1. **Next** を選択します。

1. **Register** を選択します。

    ![Select register.](../../../../translated_images/07-04-register.3403ed7976f07fbfc27210550cf2f793d9cf778032ea276ecb287bd9df88f188.ja.png)

1. 左側のタブから **Models** メニューに移動して、登録されたモデルを確認できます。

    ![Registered model.](../../../../translated_images/07-05-registered-model.90693749513e55231e8904304e4ea1f9e29ab659bc1926ea69dffd25e77ffb2d.ja.png)

#### ファインチューニングされたモデルのデプロイ

1. 作成した Azure Machine Learning ワークスペースに移動します。

1. 左側のタブから **Endpoints** を選択します。

1. ナビゲーションメニューから **Real-time endpoints** を選択します。

    ![Create endpoint.](../../../../translated_images/07-06-create-endpoint.28687e4d01bffed741bf461bbb36ceef441ed5d049ca5d091aab511ced67a804.ja.png)

1. **Create** を選択します。

1. 作成した登録済みモデルを選択します。

    ![Select registered model.](../../../../translated_images/07-07-select-registered-model.5190ae13400cc09a6410f891a62e6b2ccc2c2bd7f419b0df4ea964731e72407f.ja.png)

1. **Select** を選択します。

1. 以下のタスクを実行します:

    - **Virtual machine** を *Standard_NC6s_v3* に設定します。
    - 使用したい **Instance count** を選択します。例えば、*1*。
    - **Endpoint** を **New** に設定してエンドポイントを作成します。
    - **Endpoint name** を入力します。これは一意の値でなければなりません。
    - **Deployment name** を入力します。これも一意の値でなければなりません。

    ![Fill the deployment setting.](../../../../translated_images/07-08-deployment-setting.5449edf53b27f5457cc68d2285d355a7d364b01423a51e5af63e7c52374a3a79.ja.png)

1. **Deploy** を選択します。

> [!WARNING]
> アカウントへの追加料金を避けるために、Azure Machine Learning ワークスペースで作成したエンドポイントを削除することを忘れないでください。
>

#### Azure Machine Learning ワークスペースでデプロイメントステータスを確認

1. 作成した Azure Machine Learning ワークスペースに移動します。

1. 左側のタブから **Endpoints** を選択します。

1. 作成したエンドポイントを選択します。

    ![Select endpoints](../../../../translated_images/07-09-check-deployment.8e4465a7585b3c22db5fc9d5757269a919b5104fdeb5f736fa573ca9b3e16abe.ja.png)

1. このページで、デプロイメントプロセス中にエンドポイントを管理できます。

> [!NOTE]
> デプロイメントが完了したら、**Live traffic** が **100%** に設定されていることを確認してください。設定されていない場合は、**Update traffic** を選択してトラフィック設定を調整してください。トラフィックが0%に設定されていると、モデルをテストできません。
>
> ![Set traffic.](../../../../translated_images/07-10-set-traffic.1d1b24b39c7ec80451c99fe05298fac636f0cd449e7be282736f6c06a1a70875.ja.png)
>

## シナリオ 3: Prompt flow と統合し、Azure AI Studio でカスタムモデルとチャットする

### カスタム Phi-3 モデルを Prompt flow と統合

ファインチューニングされたモデルのデプロイに成功した後、Prompt Flow と統合してリアルタイムアプリケーションでモデルを使用できます。これにより、カスタム Phi-3 モデルを使用したさまざまなインタラクティブタスクが可能になります。

この演習では、以下を行います:

- Azure AI Studio Hub を作成します。
- Azure AI Studio Project を作成します。
- Prompt flow を作成します。
- ファインチューニングされた Phi-3 モデルのカスタム接続を追加します。
- Prompt flow を設定してカスタム Phi-3 モデルとチャットします。

> [!NOTE]
> Promptflow を使用して Azure ML Studio と統合することもできます。同じ統合プロセスを Azure ML Studio に適用できます。

#### Azure AI Studio Hub の作成

Project を作成する前に Hub を作成する必要があります。Hub はリソースグループのようなもので、Azure AI Studio 内で複数のプロジェクトを整理して管理できます。

1. [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) を訪問します。

1. 左側のタブから **All hubs** を選択します。

1. ナビゲーションメニューから **+ New hub** を選択します。

    ![Create hub.](../../../../translated_images/08-01-create-hub.1df80696bf3376f0e56ffa90de1fc35962acf2fc3c1a3a6b254015b8b993e55e.ja.png)

1. 以下のタスクを実行します:

    - **Hub name** を入力します。これは一意の値でなければなりません。
    - Azure の **Subscription** を選択します。
    - 使用する **Resource group** を選択します（必要に応じて新しいものを作成します）。
    - 使用したい **Location** を選択します。
    - 使用する **Connect Azure AI Services** を選択します（必要に応じて新しいものを作成します）。
    - **Connect Azure AI Search** を **Skip connecting** に設定します。

    ![Fill hub.](../../../../translated_images/08-02-fill-hub.fc194526614a5811e7b57e699911be39babdc95aa425b6c4a72f064948865ce3.ja.png)

1. **Next** を選択します。

#### Azure AI Studio Project の作成

1. 作成した Hub で、左側のタブから **All projects** を選択します。

1. ナビゲーションメニューから **+ New project** を選択します。

    ![Select new project.](../../../../translated_images/08-04-select-new-project.dc11f26658c3c3f9d0fcf3232a954abfc115de5eb74da21d5be229c9c1be2875.ja.png)

1. **Project name** を入力します。これは一意の値でなければなりません。

    ![Create project.](../../../../translated_images/08-05-create-project.61caaa28c1b9b696bf29de6b002bbb2040dbaeb764adab161dcb3472fe789aea.ja.png)

1. **Create a project** を選択します。

#### ファインチューニングされた Phi-3 モデルのカスタム接続を追加

カスタム Phi-3 モデルを Prompt flow と統合するには、モデルのエンドポイントとキーをカスタム接続に保存する必要があります。この設定により、Prompt flow でカスタム Phi-3 モデルにアクセスできるようになります。

#### ファインチューニングされた Phi-3 モデルの API キーとエンドポイント URI を設定

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) を訪問します。

1. 作成した Azure Machine Learning ワークスペースに移動します。

1. 左側のタブから **Endpoints** を選択します。

    ![Select endpoints.](../../../../translated_images/08-06-select-endpoints.75d3bdd7f0b17da0367370d1293f7e7f7b2a65fb7e17390997be0460e8f0b82b.ja.png)

1. 作成したエンドポイントを選択します。

    ![Select endpoints.](../../../../translated_images/08-07-select-endpoint-created.851b32efc6058e5863aa62ae8d576a6c20792e24f1862dc6857b9f24a2949f96.ja.png)

1. ナビゲーションメニューから **Consume** を選択します。

1. **REST endpoint** と **Primary key** をコピーします。
![APIキーとエンドポイントURIをコピー](../../../../translated_images/08-08-copy-endpoint-key.947512a4c95b5dd9fc5a606bad4244bf9b136929c1fab06570c463311ef29df1.ja.png)

#### カスタム接続を追加

1. [Azure AI Studio](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)にアクセスします。

1. 作成したAzure AI Studioプロジェクトに移動します。

1. 作成したプロジェクトで、左側のタブから**Settings**を選択します。

1. **+ New connection**を選択します。

    ![新しい接続を選択](../../../../translated_images/08-09-select-new-connection.b5e93c85028739875916f34a1821b0b086f0e993b8d7d7388c100e3a38b70bbd.ja.png)

1. ナビゲーションメニューから**Custom keys**を選択します。

    ![カスタムキーを選択](../../../../translated_images/08-10-select-custom-keys.077f17a1a49b8f76e446453b6a68c09c2aa08291818d98edcf39e3013c5b45ac.ja.png)

1. 以下のタスクを実行します：

    - **+ Add key value pairs**を選択します。
    - キー名に**endpoint**を入力し、Azure ML Studioからコピーしたエンドポイントを値フィールドに貼り付けます。
    - 再度**+ Add key value pairs**を選択します。
    - キー名に**key**を入力し、Azure ML Studioからコピーしたキーを値フィールドに貼り付けます。
    - キーを追加した後、**is secret**を選択してキーが露出しないようにします。

    ![接続を追加](../../../../translated_images/08-11-add-connection.01279deb77ede4d195b17ecabae70979976834892e9dbb3354f504bb6edaa6e1.ja.png)

1. **Add connection**を選択します。

#### プロンプトフローを作成

Azure AI Studioにカスタム接続を追加しました。次に、以下の手順に従ってプロンプトフローを作成します。その後、このプロンプトフローをカスタム接続に接続して、プロンプトフロー内で微調整されたモデルを使用できるようにします。

1. 作成したAzure AI Studioプロジェクトに移動します。

1. 左側のタブから**Prompt flow**を選択します。

1. ナビゲーションメニューから**+ Create**を選択します。

    ![プロンプトフローを選択](../../../../translated_images/08-12-select-promptflow.5e0527f1e5102c604e0e8a34f2321e28f8c815ec2908ae7038f012a088ff2bbc.ja.png)

1. ナビゲーションメニューから**Chat flow**を選択します。

    ![チャットフローを選択](../../../../translated_images/08-13-select-flow-type.e3fb41375041faa4d058304c319329d5f45f87139143b384f056bb500076ca73.ja.png)

1. 使用する**Folder name**を入力します。

    ![名前を入力](../../../../translated_images/08-14-enter-name.90db481f18468cfd78b281825cb5484ab7236cfa29d59d287b7b0f423516e6ea.ja.png)

1. **Create**を選択します。

#### カスタムPhi-3モデルとチャットするためのプロンプトフローの設定

微調整されたPhi-3モデルをプロンプトフローに統合する必要があります。しかし、既存のプロンプトフローはこの目的のために設計されていません。そのため、カスタムモデルの統合を可能にするためにプロンプトフローを再設計する必要があります。

1. プロンプトフロー内で、以下のタスクを実行して既存のフローを再構築します：

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

    ![Raw file modeを選択](../../../../translated_images/08-15-select-raw-file-mode.28d80142df9d540c66c37d17825cec921bb1f7b54e386223bb4ad38df10e5e2d.ja.png)

1. *integrate_with_promptflow.py*ファイルに以下のコードを追加して、プロンプトフロー内でカスタムPhi-3モデルを使用します。

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # ログ設定
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        カスタム接続を使用して、与えられた入力データでPhi-3モデルのエンドポイントにリクエストを送信します。
        """

        # "connection"はカスタム接続の名前、"endpoint"、"key"はカスタム接続のキーです
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
            
            # JSONレスポンス全体をログに記録
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Azure MLエンドポイントからのレスポンスを正常に受信しました。")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Azure MLエンドポイントへのクエリ中にエラーが発生しました: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        入力データを処理し、Phi-3モデルにクエリを送信するためのツール関数。
        """
        return query_phi3_model(input_data, connection)

    ```

    ![プロンプトフローコードを貼り付け](../../../../translated_images/08-16-paste-promptflow-code.c27a93ed6134adbe7ce618ffad7300923f3c02defedef0b5598eab5a6ee2afc2.ja.png)

> [!NOTE]
> Azure AI Studioでプロンプトフローを使用する詳細情報については、[Azure AI Studioのプロンプトフロー](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)を参照してください。

1. **Chat input**、**Chat output**を選択して、モデルとのチャットを有効にします。

    ![入力 出力](../../../../translated_images/08-17-select-input-output.d188ea79fc21d29e615b6cc50d638214a2dcbc3b3ccb16009aa67698227d2765.ja.png)

1. これで、カスタムPhi-3モデルとチャットする準備が整いました。次の演習では、プロンプトフローを開始して、微調整されたPhi-3モデルとチャットする方法を学びます。

> [!NOTE]
>
> 再構築されたフローは以下の画像のようになります：
>
> ![フロー例](../../../../translated_images/08-18-graph-example.48c427864370ac7dd02e500bc3a0ff49785d4480e489b4dfe25e529da99f193f.ja.png)
>

### カスタムPhi-3モデルとのチャット

微調整されたカスタムPhi-3モデルをプロンプトフローに統合したので、いよいよそれと対話を開始する準備が整いました。この演習では、モデルとのチャットを設定し開始する手順をガイドします。これらの手順に従うことで、微調整されたPhi-3モデルの能力をさまざまなタスクや会話で最大限に活用できるようになります。

- プロンプトフローを使用してカスタムPhi-3モデルとチャットする。

#### プロンプトフローを開始

1. **Start compute sessions**を選択してプロンプトフローを開始します。

    ![計算セッションを開始](../../../../translated_images/09-01-start-compute-session.9d080c30a6fc78a8b23ac54e7c8b11aeecc005d3da03cb0f9bd8afc298151ffa.ja.png)

1. **Validate and parse input**を選択してパラメータを更新します。

    ![入力を検証](../../../../translated_images/09-02-validate-input.db05a40e29a21b333848b7c03542b0ec521ce9c6fbe12fba51c2addcb1c07c68.ja.png)

1. 作成したカスタム接続の**connection**の**Value**を選択します。例えば、*connection*。

    ![接続](../../../../translated_images/09-03-select-connection.de0137da33c86e581425cef4a25957d86140d1605968f6f7c98207b8e715cca8.ja.png)

#### カスタムモデルとチャット

1. **Chat**を選択します。

    ![チャットを選択](../../../../translated_images/09-04-select-chat.87b90a2f41e38714f40dedde608d349bfaca00a75f08166816dddb92de711e32.ja.png)

1. これが結果の一例です：これでカスタムPhi-3モデルとチャットできます。微調整に使用したデータに基づいた質問をすることをお勧めします。

    ![プロンプトフローとチャット](../../../../translated_images/09-05-chat-with-promptflow.46c9fdf0e6de0e15e9618f654830e52bd8ead4aec0de57bb960206321d2bd0bd.ja.png)

免責事項: この翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない可能性があります。 出力を確認し、必要な修正を行ってください。