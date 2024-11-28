# Phi-3カスタムモデルをAzure AI FoundryのPrompt Flowで微調整・統合する

このエンドツーエンド（E2E）サンプルは、Microsoft Tech Communityのガイド「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)」に基づいています。Azure AI FoundryでカスタムPhi-3モデルを微調整、デプロイ、統合するプロセスを紹介します。
ローカルでコードを実行するE2Eサンプル「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)」とは異なり、このチュートリアルはAzure AI / ML Studio内でモデルを微調整および統合することに焦点を当てています。

## 概要

このE2Eサンプルでは、Phi-3モデルを微調整し、Azure AI FoundryのPrompt Flowと統合する方法を学びます。Azure AI / ML Studioを活用して、カスタムAIモデルをデプロイおよび利用するためのワークフローを確立します。このE2Eサンプルは、以下の3つのシナリオに分かれています：

**シナリオ1: Azureリソースをセットアップし、微調整の準備をする**

**シナリオ2: Phi-3モデルを微調整し、Azure Machine Learning Studioにデプロイする**

**シナリオ3: Prompt Flowと統合し、Azure AI Foundryでカスタムモデルとチャットする**

以下は、このE2Eサンプルの概要です。

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../translated_images/00-01-architecture.fa40b38b29f795863378026c4dcc3007b0938b0b43afaf8c331906d03742b2e6.ja.png)

### 目次

1. **[シナリオ1: Azureリソースをセットアップし、微調整の準備をする](../../../../md/06.E2ESamples)**
    - [Azure Machine Learningワークスペースを作成する](../../../../md/06.E2ESamples)
    - [AzureサブスクリプションでGPUクォータをリクエストする](../../../../md/06.E2ESamples)
    - [ロール割り当てを追加する](../../../../md/06.E2ESamples)
    - [プロジェクトをセットアップする](../../../../md/06.E2ESamples)
    - [微調整用のデータセットを準備する](../../../../md/06.E2ESamples)

1. **[シナリオ2: Phi-3モデルを微調整し、Azure Machine Learning Studioにデプロイする](../../../../md/06.E2ESamples)**
    - [Phi-3モデルを微調整する](../../../../md/06.E2ESamples)
    - [微調整されたPhi-3モデルをデプロイする](../../../../md/06.E2ESamples)

1. **[シナリオ3: Prompt Flowと統合し、Azure AI Foundryでカスタムモデルとチャットする](../../../../md/06.E2ESamples)**
    - [カスタムPhi-3モデルをPrompt Flowと統合する](../../../../md/06.E2ESamples)
    - [カスタムPhi-3モデルとチャットする](../../../../md/06.E2ESamples)

## シナリオ1: Azureリソースをセットアップし、微調整の準備をする

### Azure Machine Learningワークスペースを作成する

1. ポータルページの上部にある**検索バー**に「*azure machine learning*」と入力し、表示されるオプションから**Azure Machine Learning**を選択します。

    ![Type azure machine learning.](../../../../translated_images/01-01-type-azml.98b3003c07da4dbb6885400f66988b3ae05767edb5e8b8ef480e584abe379ca7.ja.png)

2. ナビゲーションメニューから**+ Create**を選択します。

3. ナビゲーションメニューから**New workspace**を選択します。

    ![Select new workspace.](../../../../translated_images/01-02-select-new-workspace.7648b384cbd786565740c0e5ea203d4710889d5ef23a2abf08428444f6d1a2a6.ja.png)

4. 次のタスクを実行します：

    - Azureの**サブスクリプション**を選択します。
    - 使用する**リソースグループ**を選択します（必要に応じて新しいものを作成）。
    - **ワークスペース名**を入力します。一意の値である必要があります。
    - 使用する**リージョン**を選択します。
    - 使用する**ストレージアカウント**を選択します（必要に応じて新しいものを作成）。
    - 使用する**キーボールト**を選択します（必要に応じて新しいものを作成）。
    - 使用する**アプリケーションインサイト**を選択します（必要に応じて新しいものを作成）。
    - 使用する**コンテナレジストリ**を選択します（必要に応じて新しいものを作成）。

    ![Fill azure machine learning.](../../../../translated_images/01-03-fill-AZML.a3f644231a76859c7d92134b7dea1dd0d4df1c11cc615351c95be5a2c7056b03.ja.png)

5. **Review + Create**を選択します。

6. **Create**を選択します。

### AzureサブスクリプションでGPUクォータをリクエストする

このチュートリアルでは、GPUを使用してPhi-3モデルを微調整およびデプロイする方法を学びます。微調整には*Standard_NC24ads_A100_v4* GPUを使用し、デプロイには*Standard_NC6s_v3* GPUを使用します。これらにはクォータリクエストが必要です。

> [!NOTE]
>
> GPU割り当てが可能なのは従量課金制サブスクリプション（標準のサブスクリプションタイプ）のみであり、特典サブスクリプションは現在サポートされていません。
>

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723)を訪問します。

1. *Standard NCADSA100v4 Family*クォータをリクエストするために次のタスクを実行します：

    - 左側のタブから**Quota**を選択します。
    - 使用する**バーチャルマシンファミリー**を選択します。例えば、*Standard_NC24ads_A100_v4* GPUを含む**Standard NCADSA100v4 Family Cluster Dedicated vCPUs**を選択します。
    - ナビゲーションメニューから**Request quota**を選択します。

        ![Request quota.](../../../../translated_images/02-02-request-quota.55f797113d95ad20ca91943eed637488d0aa51d61f3bbe7f080ec466b2ae0666.ja.png)

    - Request quotaページ内で、使用したい**New cores limit**を入力します。例えば、24。
    - Request quotaページ内で、GPUクォータをリクエストするために**Submit**を選択します。

1. *Standard NCSv3 Family*クォータをリクエストするために次のタスクを実行します：

    - 左側のタブから**Quota**を選択します。
    - 使用する**バーチャルマシンファミリー**を選択します。例えば、*Standard_NC6s_v3* GPUを含む**Standard NCSv3 Family Cluster Dedicated vCPUs**を選択します。
    - ナビゲーションメニューから**Request quota**を選択します。
    - Request quotaページ内で、使用したい**New cores limit**を入力します。例えば、24。
    - Request quotaページ内で、GPUクォータをリクエストするために**Submit**を選択します。

### ロール割り当てを追加する

モデルを微調整およびデプロイするためには、まずユーザー割り当てマネージドID（UAI）を作成し、適切な権限を割り当てる必要があります。このUAIはデプロイ時の認証に使用されます。

#### ユーザー割り当てマネージドID（UAI）を作成する

1. ポータルページの上部にある**検索バー**に「*managed identities*」と入力し、表示されるオプションから**Managed Identities**を選択します。

    ![Type managed identities.](../../../../translated_images/03-01-type-managed-identities.2f7b07daa34dc15303b6a3f8c364bc0b7e892dd18aaff361440a030621b540b8.ja.png)

1. **+ Create**を選択します。

    ![Select create.](../../../../translated_images/03-02-select-create.0bde775b318f4adba24a7637b31f00f9b685214ed225c5123845a215a260ac71.ja.png)

1. 次のタスクを実行します：

    - Azureの**サブスクリプション**を選択します。
    - 使用する**リソースグループ**を選択します（必要に応じて新しいものを作成）。
    - 使用する**リージョン**を選択します。
    - **名前**を入力します。一意の値である必要があります。

    ![Select create.](../../../../translated_images/03-03-fill-managed-identities-1.688009e629c1e6952853b94022d3fe97c659c34e29908db17218a5cab6d6add1.ja.png)

1. **Review + create**を選択します。

1. **+ Create**を選択します。

#### マネージドIDにコントリビューターロールを割り当てる

1. 作成したマネージドIDリソースに移動します。

1. 左側のタブから**Azure role assignments**を選択します。

1. ナビゲーションメニューから**+Add role assignment**を選択します。

1. Add role assignmentページ内で次のタスクを実行します：
    - **Scope**を**Resource group**に設定します。
    - Azureの**サブスクリプション**を選択します。
    - 使用する**リソースグループ**を選択します。
    - **Role**を**Contributor**に設定します。

    ![Fill contributor role.](../../../../translated_images/03-04-fill-contributor-role.8bc54b3ac8f64842c82b3379f3c3e9f8d778abf28c00e5b7b471935a86d3ae64.ja.png)

1. **Save**を選択します。

#### ストレージBlobデータリーダーロールをマネージドIDに割り当てる

1. ポータルページの上部にある**検索バー**に「*storage accounts*」と入力し、表示されるオプションから**Storage accounts**を選択します。

    ![Type storage accounts.](../../../../translated_images/03-05-type-storage-accounts.236987db35ba863124c6de8dd16533fe35b96ee4e2dcb9d67e6b279a285f0e6d.ja.png)

1. 作成したAzure Machine Learningワークスペースに関連付けられているストレージアカウントを選択します。例えば、*finetunephistorage*。

1. 次のタスクを実行してAdd role assignmentページに移動します：

    - 作成したAzureストレージアカウントに移動します。
    - 左側のタブから**Access Control (IAM)**を選択します。
    - ナビゲーションメニューから**+ Add**を選択します。
    - ナビゲーションメニューから**Add role assignment**を選択します。

    ![Add role.](../../../../translated_images/03-06-add-role.dde49177fe7ce1cd1604f620ca5c8ac6442fc516effb057e9f74645f35f9d038.ja.png)

1. Add role assignmentページ内で次のタスクを実行します：

    - ロールページ内で**検索バー**に「*Storage Blob Data Reader*」と入力し、表示されるオプションから**Storage Blob Data Reader**を選択します。
    - ロールページ内で**Next**を選択します。
    - メンバーページ内で**Assign access to**を**Managed identity**に設定します。
    - メンバーページ内で**+ Select members**を選択します。
    - Select managed identitiesページ内でAzureの**サブスクリプション**を選択します。
    - Select managed identitiesページ内で**Managed identity**を**Manage Identity**に設定します。
    - Select managed identitiesページ内で作成したManage Identityを選択します。例えば、*finetunephi-managedidentity*。
    - Select managed identitiesページ内で**Select**を選択します。

    ![Select managed identity.](../../../../translated_images/03-08-select-managed-identity.f9a44699bf247a4583e2d377e304de8c3d8a602b7d3fed52b9ae790e64e94fe9.ja.png)

1. **Review + assign**を選択します。

#### AcrPullロールをマネージドIDに割り当てる

1. ポータルページの上部にある**検索バー**に「*container registries*」と入力し、表示されるオプションから**Container registries**を選択します。

    ![Type container registries.](../../../../translated_images/03-09-type-container-registries.b5519f1fbf49bff0c0d4c95deecd2ef0c61b4870119886c3661014435e2b7095.ja.png)

1. Azure Machine Learningワークスペースに関連付けられているコンテナレジストリを選択します。例えば、*finetunephicontainerregistry*

1. 次のタスクを実行してAdd role assignmentページに移動します：

    - 左側のタブから**Access Control (IAM)**を選択します。
    - ナビゲーションメニューから**+ Add**を選択します。
    - ナビゲーションメニューから**Add role assignment**を選択します。

1. Add role assignmentページ内で次のタスクを実行します：

    - ロールページ内で**検索バー**に「*AcrPull*」と入力し、表示されるオプションから**AcrPull**を選択します。
    - ロールページ内で**Next**を選択します。
    - メンバーページ内で**Assign access to**を**Managed identity**に設定します。
    - メンバーページ内で**+ Select members**を選択します。
    - Select managed identitiesページ内でAzureの**サブスクリプション**を選択します。
    - Select managed identitiesページ内で**Managed identity**を**Manage Identity**に設定します。
    - Select managed identitiesページ内で作成したManage Identityを選択します。例えば、*finetunephi-managedidentity*。
    - Select managed identitiesページ内で**Select**を選択します。
    - **Review + assign**を選択します。

### プロジェクトをセットアップする

微調整に必要なデータセットをダウンロードするために、ローカル環境をセットアップします。

この演習では、

- 作業するフォルダを作成します。
- 仮想環境を作成します。
- 必要なパッケージをインストールします。
- データセットをダウンロードするための*download_dataset.py*ファイルを作成します。

#### 作業するフォルダを作成する

1. ターミナルウィンドウを開き、デフォルトパスに*finetune-phi*という名前のフォルダを作成するために次のコマンドを入力します。

    ```console
    mkdir finetune-phi
    ```

2. 作成した*finetune-phi*フォルダに移動するために、ターミナル内で次のコマンドを入力します。

    ```console
    cd finetune-phi
    ```

#### 仮想環境を作成する

1. ターミナル内で次のコマンドを入力し、*.venv*という名前の仮想環境を作成します。

    ```console
    python -m venv .venv
    ```

2. ターミナル内で次のコマンドを入力して、仮想環境をアクティブにします。

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> 正常に動作した場合、コマンドプロンプトの前に*(.venv)*が表示されます。

#### 必要なパッケージをインストールする

1. ターミナル内で次のコマンドを入力し、必要なパッケージをインストールします。

    ```console
    pip install datasets==2.19.1
    ```

#### `download_dataset.py`を作成する

> [!NOTE]
> 完全なフォルダ構成：
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. **Visual Studio Code**を開きます。

1. メニューバーから**ファイル**を選択します。

1. **フォルダを開く**を選択します。

1. 作成した*finetune-phi*フォルダを選択します。場所は*C:\Users\yourUserName\finetune-phi*です。

    ![Select the folder that you created.](../../../../translated_images/04-01-open-project-folder.f5e2b4ce1cb596eae857303b12909dc0174fd99129d6944c41079f24ee17eed2.ja.png)

1. Visual Studio Codeの左ペインで右クリックし、**新しいファイル**を選択して*download_dataset.py*という名前の新しいファイルを作成します。

    ![Create a new file.](../../../../translated_images/04-02-create-new-file.7c51fabe5e84788e34e43f951164471eb07df8363993ce69badc8908f1033613.ja.png)

### 微調整用のデータセットを準備する

この演習では、*download_dataset.py*ファイルを実行して*ultrachat_200k*データセットをローカル環境にダウンロードします。次に、このデータセットを使用してAzure Machine LearningでPhi-3モデルを微調整します。

この演習では：

- *
1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) にアクセスします。

1. 左側のタブから **Compute** を選択します。

1. ナビゲーションメニューから **Compute clusters** を選択します。

1. **+ New** を選択します。

    ![Select compute.](../../../../translated_images/06-01-select-compute.69422609cf19921fb16f550b2566e00870f63ba0caf66b0d26b34e6b0ed21a68.ja.png)

1. 次のタスクを実行します:

    - 使用したい **Region** を選択します。
    - **Virtual machine tier** を **Dedicated** に設定します。
    - **Virtual machine type** を **GPU** に設定します。
    - **Virtual machine size** のフィルターを **Select from all options** に設定します。
    - **Virtual machine size** を **Standard_NC24ads_A100_v4** に設定します。

    ![Create cluster.](../../../../translated_images/06-02-create-cluster.ad68bcb0914b62972408da8f925632977c54248ff99d2c45761f7e3d33f40fe1.ja.png)

1. **Next** を選択します。

1. 次のタスクを実行します:

    - **Compute name** を入力します。これは一意の値でなければなりません。
    - **Minimum number of nodes** を **0** に設定します。
    - **Maximum number of nodes** を **1** に設定します。
    - **Idle seconds before scale down** を **120** に設定します。

    ![Create cluster.](../../../../translated_images/06-03-create-cluster.f36399780462ff69f62b9bdf22180d6824b00cdc913fe2a639dde3e4b9eaa43e.ja.png)

1. **Create** を選択します。

#### Phi-3 モデルの微調整

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) にアクセスします。

1. 作成した Azure Machine Learning ワークスペースを選択します。

    ![Select workspace that you created.](../../../../translated_images/06-04-select-workspace.5e35488b3bb3e391ead6688243c52fc2aecb8ae7f1c738b91b49580f9db353cf.ja.png)

1. 次のタスクを実行します:

    - 左側のタブから **Model catalog** を選択します。
    - **search bar** に *phi-3-mini-4k* と入力し、表示されたオプションから **Phi-3-mini-4k-instruct** を選択します。

    ![Type phi-3-mini-4k.](../../../../translated_images/06-05-type-phi-3-mini-4k.7461addd95ede137f6f018a29681762f85e063477ded6043aafbdf6d742a54e8.ja.png)

1. ナビゲーションメニューから **Fine-tune** を選択します。

    ![Select fine tune.](../../../../translated_images/06-06-select-fine-tune.2c678a7f33294c16ae3ad30ce5d4a78600013dc3a0227e8d341a1962f3aff84d.ja.png)

1. 次のタスクを実行します:

    - **Select task type** を **Chat completion** に設定します。
    - **+ Select data** を選択して **Traning data** をアップロードします。
    - Validation data upload type を **Provide different validation data** に設定します。
    - **+ Select data** を選択して **Validation data** をアップロードします。

    ![Fill fine-tuning page.](../../../../translated_images/06-07-fill-finetuning.c76431cc247b6398fb9d33da62841adf87d5eebaa92cd79e80bd7bcbed49f1d3.ja.png)

    > [!TIP]
    >
    > **Advanced settings** を選択して、**learning_rate** や **lr_scheduler_type** などの設定をカスタマイズし、特定のニーズに応じて微調整プロセスを最適化できます。

1. **Finish** を選択します。

1. この演習では、Azure Machine Learning を使用して Phi-3 モデルの微調整に成功しました。微調整プロセスにはかなりの時間がかかることに注意してください。微調整ジョブを実行した後、完了するまで待つ必要があります。Azure Machine Learning ワークスペースの左側のタブの Jobs タブに移動して、微調整ジョブのステータスを監視できます。次のシリーズでは、微調整されたモデルをデプロイし、Prompt flow と統合します。

    ![See finetuning job.](../../../../translated_images/06-08-output.9f9cf6f9e9e83533b793a5ff3066b09475e299999fead6f98dfb102f48db0061.ja.png)

### 微調整された Phi-3 モデルのデプロイ

微調整された Phi-3 モデルを Prompt flow と統合するには、モデルをデプロイしてリアルタイム推論にアクセスできるようにする必要があります。このプロセスには、モデルの登録、オンラインエンドポイントの作成、およびモデルのデプロイが含まれます。

この演習では、次のことを行います:

- 微調整されたモデルを Azure Machine Learning ワークスペースに登録します。
- オンラインエンドポイントを作成します。
- 登録された微調整 Phi-3 モデルをデプロイします。

#### 微調整されたモデルの登録

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) にアクセスします。

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

1. 左側のタブから **Models** メニューに移動して、登録されたモデルを表示できます。

    ![Registered model.](../../../../translated_images/07-05-registered-model.90693749513e55231e8904304e4ea1f9e29ab659bc1926ea69dffd25e77ffb2d.ja.png)

#### 微調整されたモデルのデプロイ

1. 作成した Azure Machine Learning ワークスペースに移動します。

1. 左側のタブから **Endpoints** を選択します。

1. ナビゲーションメニューから **Real-time endpoints** を選択します。

    ![Create endpoint.](../../../../translated_images/07-06-create-endpoint.28687e4d01bffed741bf461bbb36ceef441ed5d049ca5d091aab511ced67a804.ja.png)

1. **Create** を選択します。

1. 作成した登録済みモデルを選択します。

    ![Select registered model.](../../../../translated_images/07-07-select-registered-model.5190ae13400cc09a6410f891a62e6b2ccc2c2bd7f419b0df4ea964731e72407f.ja.png)

1. **Select** を選択します。

1. 次のタスクを実行します:

    - **Virtual machine** を *Standard_NC6s_v3* に設定します。
    - 使用する **Instance count** を選択します。例えば、*1*。
    - **Endpoint** を **New** に設定してエンドポイントを作成します。
    - **Endpoint name** を入力します。これは一意の値でなければなりません。
    - **Deployment name** を入力します。これも一意の値でなければなりません。

    ![Fill the deployment setting.](../../../../translated_images/07-08-deployment-setting.5449edf53b27f5457cc68d2285d355a7d364b01423a51e5af63e7c52374a3a79.ja.png)

1. **Deploy** を選択します。

> [!WARNING]
> アカウントに追加料金が発生しないようにするため、Azure Machine Learning ワークスペースで作成したエンドポイントを削除することを忘れないでください。
>

#### Azure Machine Learning ワークスペースでのデプロイステータスの確認

1. 作成した Azure Machine Learning ワークスペースに移動します。

1. 左側のタブから **Endpoints** を選択します。

1. 作成したエンドポイントを選択します。

    ![Select endpoints](../../../../translated_images/07-09-check-deployment.8e4465a7585b3c22db5fc9d5757269a919b5104fdeb5f736fa573ca9b3e16abe.ja.png)

1. このページでは、デプロイメントプロセス中にエンドポイントを管理できます。

> [!NOTE]
> デプロイメントが完了したら、**Live traffic** が **100%** に設定されていることを確認してください。設定されていない場合は、**Update traffic** を選択してトラフィック設定を調整します。トラフィックが 0% に設定されていると、モデルをテストできないことに注意してください。
>
> ![Set traffic.](../../../../translated_images/07-10-set-traffic.1d1b24b39c7ec80451c99fe05298fac636f0cd449e7be282736f6c06a1a70875.ja.png)
>

## シナリオ 3: Prompt flow と統合し、Azure AI Foundry でカスタムモデルとチャット

### カスタム Phi-3 モデルを Prompt flow と統合

微調整されたモデルを正常にデプロイした後、Prompt Flow と統合してリアルタイムアプリケーションでモデルを使用できるようにし、カスタム Phi-3 モデルを使用したさまざまなインタラクティブタスクを可能にします。

この演習では、次のことを行います:

- Azure AI Foundry Hub を作成します。
- Azure AI Foundry Project を作成します。
- Prompt flow を作成します。
- 微調整された Phi-3 モデルのカスタム接続を追加します。
- カスタム Phi-3 モデルとチャットするために Prompt flow を設定します。

> [!NOTE]
> Azure ML Studio を使用して Promptflow と統合することもできます。同じ統合プロセスが Azure ML Studio にも適用されます。

#### Azure AI Foundry Hub の作成

プロジェクトを作成する前に Hub を作成する必要があります。Hub はリソースグループのように機能し、Azure AI Foundry 内で複数のプロジェクトを整理および管理できます。

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo) にアクセスします。

1. 左側のタブから **All hubs** を選択します。

1. ナビゲーションメニューから **+ New hub** を選択します。

    ![Create hub.](../../../../translated_images/08-01-create-hub.1df80696bf3376f0e56ffa90de1fc35962acf2fc3c1a3a6b254015b8b993e55e.ja.png)

1. 次のタスクを実行します:

    - **Hub name** を入力します。これは一意の値でなければなりません。
    - Azure **Subscription** を選択します。
    - 使用する **Resource group** を選択します（必要に応じて新しいものを作成します）。
    - 使用したい **Location** を選択します。
    - 使用する **Connect Azure AI Services** を選択します（必要に応じて新しいものを作成します）。
    - **Connect Azure AI Search** を **Skip connecting** に設定します。

    ![Fill hub.](../../../../translated_images/08-02-fill-hub.fc194526614a5811e7b57e699911be39babdc95aa425b6c4a72f064948865ce3.ja.png)

1. **Next** を選択します。

#### Azure AI Foundry Project の作成

1. 作成した Hub で、左側のタブから **All projects** を選択します。

1. ナビゲーションメニューから **+ New project** を選択します。

    ![Select new project.](../../../../translated_images/08-04-select-new-project.dc11f26658c3c3f9d0fcf3232a954abfc115de5eb74da21d5be229c9c1be2875.ja.png)

1. **Project name** を入力します。これは一意の値でなければなりません。

    ![Create project.](../../../../translated_images/08-05-create-project.61caaa28c1b9b696bf29de6b002bbb2040dbaeb764adab161dcb3472fe789aea.ja.png)

1. **Create a project** を選択します。

#### 微調整された Phi-3 モデルのカスタム接続を追加

カスタム Phi-3 モデルを Prompt flow と統合するには、モデルのエンドポイントとキーをカスタム接続に保存する必要があります。この設定により、Prompt flow でカスタム Phi-3 モデルにアクセスできます。

#### 微調整された Phi-3 モデルの API キーとエンドポイント URI の設定

1. [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo) にアクセスします。

1. 作成した Azure Machine Learning ワークスペースに移動します。

1. 左側のタブから **Endpoints** を選択します。

    ![Select endpoints.](../../../../translated_images/08-06-select-endpoints.75d3bdd7f0b17da0367370d1293f7e7f7b2a65fb7e17390997be0460e8f0b82b.ja.png)

1. 作成したエンドポイントを選択します。

    ![Select endpoints.](../../../../translated_images/08-07-select-endpoint-created.851b32efc6058e5863aa62ae8d576a6c20792e24f1862dc6857b9f24a2949f96.ja.png)

1. ナビゲーションメニューから **Consume** を選択します。

1. **REST endpoint** と **Primary key** をコピーします。
![Copy api key and endpoint uri.](../../../../translated_images/08-08-copy-endpoint-key.947512a4c95b5dd9fc5a606bad4244bf9b136929c1fab06570c463311ef29df1.ja.png)

#### カスタム接続の追加

1. [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo)にアクセスします。

1. 作成したAzure AI Foundryプロジェクトに移動します。

1. 作成したプロジェクトで、左側のタブから**設定**を選択します。

1. **+ 新しい接続**を選択します。

    ![Select new connection.](../../../../translated_images/08-09-select-new-connection.b5e93c85028739875916f34a1821b0b086f0e993b8d7d7388c100e3a38b70bbd.ja.png)

1. ナビゲーションメニューから**カスタムキー**を選択します。

    ![Select custom keys.](../../../../translated_images/08-10-select-custom-keys.077f17a1a49b8f76e446453b6a68c09c2aa08291818d98edcf39e3013c5b45ac.ja.png)

1. 次のタスクを実行します：

    - **+ キーと値のペアを追加**を選択します。
    - キー名には**endpoint**を入力し、Azure ML Studioからコピーしたエンドポイントを値フィールドに貼り付けます。
    - 再度**+ キーと値のペアを追加**を選択します。
    - キー名には**key**を入力し、Azure ML Studioからコピーしたキーを値フィールドに貼り付けます。
    - キーを追加した後、キーが公開されないように**is secret**を選択します。

    ![Add connection.](../../../../translated_images/08-11-add-connection.01279deb77ede4d195b17ecabae70979976834892e9dbb3354f504bb6edaa6e1.ja.png)

1. **接続を追加**を選択します。

#### Prompt flowの作成

Azure AI Foundryにカスタム接続を追加しました。次に、以下の手順でPrompt flowを作成しましょう。その後、このPrompt flowをカスタム接続に接続し、調整済みモデルをPrompt flow内で使用できるようにします。

1. 作成したAzure AI Foundryプロジェクトに移動します。

1. 左側のタブから**Prompt flow**を選択します。

1. ナビゲーションメニューから**+ 作成**を選択します。

    ![Select Promptflow.](../../../../translated_images/08-12-select-promptflow.5e0527f1e5102c604e0e8a34f2321e28f8c815ec2908ae7038f012a088ff2bbc.ja.png)

1. ナビゲーションメニューから**チャットフロー**を選択します。

    ![Select chat flow.](../../../../translated_images/08-13-select-flow-type.e3fb41375041faa4d058304c319329d5f45f87139143b384f056bb500076ca73.ja.png)

1. 使用する**フォルダ名**を入力します。

    ![Enter name.](../../../../translated_images/08-14-enter-name.90db481f18468cfd78b281825cb5484ab7236cfa29d59d287b7b0f423516e6ea.ja.png)

1. **作成**を選択します。

#### カスタムPhi-3モデルとチャットするためのPrompt flowの設定

調整済みのPhi-3モデルをPrompt flowに統合する必要があります。しかし、既存のPrompt flowはこの目的に設計されていないため、カスタムモデルの統合を可能にするためにPrompt flowを再設計する必要があります。

1. Prompt flowで、既存のフローを再構築するために次のタスクを実行します：

    - **生ファイルモード**を選択します。
    - *flow.dag.yml*ファイル内の既存のコードをすべて削除します。
    - 次のコードを*flow.dag.yml*ファイルに追加します。

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

    - **保存**を選択します。

    ![Select raw file mode.](../../../../translated_images/08-15-select-raw-file-mode.28d80142df9d540c66c37d17825cec921bb1f7b54e386223bb4ad38df10e5e2d.ja.png)

1. カスタムPhi-3モデルをPrompt flowで使用するために、次のコードを*integrate_with_promptflow.py*ファイルに追加します。

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

    ![Paste prompt flow code.](../../../../translated_images/08-16-paste-promptflow-code.c27a93ed6134adbe7ce618ffad7300923f3c02defedef0b5598eab5a6ee2afc2.ja.png)

> [!NOTE]
> Azure AI FoundryでPrompt flowを使用する方法の詳細については、[Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow)を参照してください。

1. **チャット入力**、**チャット出力**を選択して、モデルとのチャットを有効にします。

    ![Input Output.](../../../../translated_images/08-17-select-input-output.d188ea79fc21d29e615b6cc50d638214a2dcbc3b3ccb16009aa67698227d2765.ja.png)

1. これで、カスタムPhi-3モデルとのチャットの準備が整いました。次の演習では、Prompt flowを開始し、調整済みのPhi-3モデルとチャットする方法を学びます。

> [!NOTE]
>
> 再構築されたフローは、以下の画像のようになります：
>
> ![Flow example.](../../../../translated_images/08-18-graph-example.48c427864370ac7dd02e500bc3a0ff49785d4480e489b4dfe25e529da99f193f.ja.png)
>

### カスタムPhi-3モデルとのチャット

カスタムPhi-3モデルを調整し、Prompt flowに統合したので、いよいよそれとの対話を開始する準備が整いました。この演習では、Prompt flowを使用してモデルとのチャットを設定し、開始する手順を案内します。これらの手順に従うことで、調整済みのPhi-3モデルの機能をさまざまなタスクや会話に最大限に活用できるようになります。

- Prompt flowを使用してカスタムPhi-3モデルとチャットします。

#### Prompt flowの開始

1. **コンピュートセッションの開始**を選択して、Prompt flowを開始します。

    ![Start compute session.](../../../../translated_images/09-01-start-compute-session.9d080c30a6fc78a8b23ac54e7c8b11aeecc005d3da03cb0f9bd8afc298151ffa.ja.png)

1. **入力の検証と解析**を選択して、パラメータを更新します。

    ![Validate input.](../../../../translated_images/09-02-validate-input.db05a40e29a21b333848b7c03542b0ec521ce9c6fbe12fba51c2addcb1c07c68.ja.png)

1. 作成したカスタム接続の**接続**の**値**を選択します。例えば、*connection*。

    ![Connection.](../../../../translated_images/09-03-select-connection.de0137da33c86e581425cef4a25957d86140d1605968f6f7c98207b8e715cca8.ja.png)

#### カスタムモデルとのチャット

1. **チャット**を選択します。

    ![Select chat.](../../../../translated_images/09-04-select-chat.87b90a2f41e38714f40dedde608d349bfaca00a75f08166816dddb92de711e32.ja.png)

1. ここに結果の例があります：これでカスタムPhi-3モデルとチャットできます。調整に使用したデータに基づいて質問することをお勧めします。

    ![Chat with prompt flow.](../../../../translated_images/09-05-chat-with-promptflow.46c9fdf0e6de0e15e9618f654830e52bd8ead4aec0de57bb960206321d2bd0bd.ja.png)

**免責事項**:
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期すよう努めておりますが、自動翻訳には誤りや不正確さが含まれる場合がありますのでご注意ください。元の言語で書かれた原文を権威ある情報源とみなしてください。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤解について、当社は一切の責任を負いません。