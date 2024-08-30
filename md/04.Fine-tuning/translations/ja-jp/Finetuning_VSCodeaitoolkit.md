## VS Code用AIツールキットへようこそ

[VS Code用AIツールキット](https://github.com/microsoft/vscode-ai-toolkit/tree/main)は、Azure AI Studio CatalogやHugging Faceなどのカタログからさまざまなモデルを集約しています。このツールキットは、以下の方法で生成AIツールとモデルを使用したAIアプリケーションの開発タスクを簡素化します：
- モデルの発見とプレイグラウンドから始める。
- ローカルコンピューティングリソースを使用してモデルの微調整と推論を行う。
- Azureリソースを使用してリモートで微調整と推論を行う。

[VSCode用AIツールキットをインストール](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../imgs/04/00/Aitoolkit.png)


**[プライベートプレビュー]** モデルの微調整と推論をクラウドで実行するためのAzure Container Appsのワンクリックプロビジョニング。

それでは、AIアプリケーション開発に飛び込みましょう：

- [ローカル開発](#ローカル開発)
    - [準備](#準備)
    - [Condaのアクティベート](#condaのアクティベート)
    - [ベースモデルの微調整のみ](#ベースモデルの微調整のみ)
    - [モデルの微調整と推論](#モデルの微調整と推論)
- [**[プライベートプレビュー]** リモート開発](#プライベートプレビュー-リモート開発)
    - [前提条件](#前提条件)
    - [リモート開発プロジェクトの設定](#リモート開発プロジェクトの設定)
    - [Azureリソースのプロビジョニング](#azureリソースのプロビジョニング)
    - [[オプション] HuggingfaceトークンをAzure Container Appのシークレットに追加](#オプション-huggingfaceトークンをazure-container-appのシークレットに追加)
    - [微調整の実行](#微調整の実行)
    - [推論エンドポイントのプロビジョニング](#推論エンドポイントのプロビジョニング)
    - [推論エンドポイントのデプロイ](#推論エンドポイントのデプロイ)
    - [高度な使用法](#高度な使用法)

## ローカル開発
### 準備

1. ホストにNVIDIAドライバがインストールされていることを確認します。
2. データセットの利用にHFを使用している場合は、`huggingface-cli login`を実行します。
3. `Olive`のキー設定の説明は、メモリ使用量を変更するためのものです。

### Condaのアクティベート
WSL環境を使用しており、共有されているため、conda環境を手動でアクティベートする必要があります。このステップを完了した後、微調整や推論を実行できます。

```bash
conda activate [conda-env-name] 
```

### ベースモデルの微調整のみ
ベースモデルを微調整せずに試すには、condaをアクティベートした後にこのコマンドを実行します。

```bash
cd inference

# Webブラウザインターフェースでは、最大新トークン長、温度などのいくつかのパラメータを調整できます。
# ユーザーは、gradioが接続を開始した後に手動でリンク（例：http://0.0.0.0:7860）をブラウザで開く必要があります。
python gradio_chat.py --baseonly
```

### モデルの微調整と推論

開発コンテナでワークスペースを開いたら、ターミナルを開き（デフォルトのパスはプロジェクトのルート）、次のコマンドを実行して選択したデータセットでLLMを微調整します。

```bash
python finetuning/invoke_olive.py 
```

チェックポイントと最終モデルは`models`フォルダに保存されます。

次に、`console`、`web browser`、または`prompt flow`でチャットを通じて微調整されたモデルを使用して推論を実行します。

```bash
cd inference

# コンソールインターフェース。
python console_chat.py

# Webブラウザインターフェースでは、最大新トークン長、温度などのいくつかのパラメータを調整できます。
# ユーザーは、gradioが接続を開始した後に手動でリンク（例：http://127.0.0.1:7860）をブラウザで開く必要があります。
python gradio_chat.py
```

VS Codeで`prompt flow`を使用するには、この[クイックスタート](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html)を参照してください。

### モデルの微調整

次に、デバイスにGPUがあるかどうかに応じて、以下のモデルをダウンロードします。

QLoRAを使用してローカル微調整セッションを開始するには、カタログから微調整したいモデルを選択します。
| プラットフォーム | GPUの有無 | モデル名 | サイズ (GB) |
|---------|---------|--------|--------|
| Windows | はい | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | はい | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | いいえ | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_注意_** モデルをダウンロードするためにAzureアカウントは必要ありません

Phi3-mini（int4）モデルのサイズは約2GB〜3GBです。ネットワーク速度に応じて、ダウンロードには数分かかる場合があります。

まず、プロジェクト名と場所を選択します。
次に、モデルカタログからモデルを選択します。プロジェクトテンプレートをダウンロードするように求められます。その後、「プロジェクトの設定」をクリックしてさまざまな設定を調整できます。

### Microsoft Olive 

[Olive](https://microsoft.github.io/Olive/overview/olive.html)を使用して、カタログからのPyTorchモデルでQLoRA微調整を実行します。すべての設定は、メモリ使用量を最適化してローカルで微調整プロセスを実行するためにデフォルト値に設定されていますが、シナリオに応じて調整できます。

### 微調整のサンプルとリソース

- [微調整の入門ガイド](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [HuggingFaceデータセットを使用した微調整](https://github.com/microsoft/vscode-ai-toolkit/blob/main/walkthrough-hf-dataset.md)
- [シンプルなデータセットを使用した微調整](https://github.com/microsoft/vscode-ai-toolkit/blob/main/walkthrough-simple-dataset.md)


## **[プライベートプレビュー]** リモート開発
### 前提条件
1. リモートAzure Container App環境でモデルの微調整を実行するには、サブスクリプションに十分なGPU容量があることを確認してください。アプリケーションに必要な容量を要求するには、[サポートチケット](https://azure.microsoft.com/support/create-ticket/)を提出してください。GPU容量の詳細については、[こちら](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)をご覧ください。
2. HuggingFaceでプライベートデータセットを使用している場合は、[HuggingFaceアカウント](https://huggingface.co/)を持ち、[アクセス トークンを生成](https://huggingface.co/docs/hub/security-tokens)してください。
3. VS CodeのAIツールキットでリモート微調整と推論機能フラグを有効にします。
   1. *ファイル -> 設定 -> 設定*を選択してVS Codeの設定を開きます。
   2. *拡張機能*に移動し、*AIツールキット*を選択します。
   3. *「リモート微調整と推論を有効にする」*オプションを選択します。
   4. VS Codeを再読み込みして有効にします。

- [リモート微調整](https://github.com/microsoft/vscode-ai-toolkit/blob/main/remote-finetuning.md)

### リモート開発プロジェクトの設定
1. コマンドパレットで`AIツールキット：リソースビューにフォーカス`を実行します。
2. *モデル微調整*に移動してモデルカタログにアクセスします。プロジェクトに名前を付け、コンピュータ上の場所を選択します。次に、*「プロジェクトの設定」*ボタンをクリックします。
3. プロジェクト設定
    1. *「ローカルで微調整」*オプションを有効にしないでください。
    2. Olive設定はデフォルト値で表示されます。必要に応じてこれらの設定を調整して入力してください。
    3. *「プロジェクトの生成」*に進みます。この段階ではWSLを利用し、将来の更新に備えて新しいConda環境を設定します。
4. *「ワークスペースでウィンドウを再起動」*をクリックしてリモート開発プロジェクトを開きます。

> **注意:** プロジェクトは現在、VS CodeのAIツールキットでローカルまたはリモートでのみ動作します。プロジェクト作成中に*「ローカルで微調整」*を選択した場合、WSLでのみ動作し、リモート開発機能はありません。一方、*「ローカルで微調整」*を有効にしない場合、プロジェクトはリモートAzure Container App環境に制限されます。

### Azureリソースのプロビジョニング
開始するには、リモート微調整のためにAzureリソースをプロビジョニングする必要があります。コマンドパレットから`AIツールキット：微調整のためのAzure Container Appsジョブをプロビジョニング`を実行してこれを行います。

出力パネルに表示されるリンクを通じてプロビジョニングの進行状況を監視します。

### [オプション] HuggingfaceトークンをAzure Container Appのシークレットに追加
プライベートHuggingFaceデータセットを使用している場合は、HuggingFaceトークンを環境変数として設定して、Hugging Face Hubで手動でログインする必要がないようにします。
これを行うには、`AIツールキット：微調整のためのAzure Container Appsジョブシークレットを追加`コマンドを使用します。このコマンドを使用して、シークレット名を[`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken)として設定し、Hugging Faceトークンをシークレット値として使用します。

### 微調整の実行
リモート微調整ジョブを開始するには、`AIツールキット：微調整を実行`コマンドを実行します。

システムおよびコンソールログを表示するには、出力パネルのリンクを使用してAzureポータルにアクセスできます（詳細な手順は[Azureでのログの表示とクエリ](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)を参照）。または、`AIツールキット：実行中の微調整ジョブのストリーミングログを表示`コマンドを実行して、VSCodeの出力パネルで直接コンソールログを表示できます。
> **注意:** リソースが不足しているため、ジョブがキューに入る可能性があります。ログが表示されない場合は、`AIツールキット：実行中の微調整ジョブのストリーミングログを表示`コマンドを実行し、しばらく待ってから再度コマンドを実行してストリーミングログに再接続します。

このプロセス中に、QLoRAを使用して微調整を行い、推論中にモデルを使用するためのLoRAアダプタを作成します。
微調整の結果はAzure Filesに保存されます。

### 推論エンドポイントのプロビジョニング
リモート環境でアダプタをトレーニングした後、シンプルなGradioアプリケーションを使用してモデルと対話します。
微調整プロセスと同様に、コマンドパレットから`AIツールキット：推論のためのAzure Container Appsをプロビジョニング`を実行して、リモート推論のためのAzureリソースを設定する必要があります。

デフォルトでは、推論に使用されるサブスクリプションとリソースグループは、微調整に使用されたものと一致する必要があります。推論は、同じAzure Container App環境を使用し、微調整ステップ中に生成されたモデルとモデルアダプタにアクセスします。

### 推論エンドポイントのデプロイ
推論コードを修正したり、推論モデルを再ロードしたりする場合は、`AIツールキット：推論のためにデプロイ`コマンドを実行します。これにより、最新のコードがAzure Container Appと同期され、レプリカが再起動されます。

デプロイが正常に完了すると、VSCode通知に表示される*「推論エンドポイントに移動」*ボタンをクリックして推論APIにアクセスできます。または、Web APIエンドポイントは`./infra/inference.config.json`の`ACA_APP_ENDPOINT`および出力パネルにあります。これで、このエンドポイントを使用してモデルを評価する準備が整いました。

### 高度な使用法
AIツールキットを使用したリモート開発の詳細については、[リモートでのモデル微調整](https://aka.ms/ai-toolkit/remote-provision)および[微調整されたモデルでの推論](https://aka.ms/ai-toolkit/remote-inference)のドキュメントを参照してください。