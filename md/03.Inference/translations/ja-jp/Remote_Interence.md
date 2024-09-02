# ファインチューニングされたモデルを使用したリモート推論

リモート環境でアダプターをトレーニングした後、シンプルなGradioアプリケーションを使用してモデルと対話します。

![Fine-tune complete](../../../../imgs/03/RemoteServer/log-finetuning-res.png)

### Azureリソースのプロビジョニング
リモート推論のためにAzureリソースを設定するには、コマンドパレットから`AI Toolkit: Provision Azure Container Apps for inference`を実行する必要があります。この設定中に、Azureサブスクリプションとリソースグループを選択するように求められます。
![Provision Inference Resource](../../../../imgs/03/RemoteServer/command-provision-inference.png)

デフォルトでは、推論のためのサブスクリプションとリソースグループは、ファインチューニングに使用されたものと一致する必要があります。推論は、同じAzure Container App Environmentを使用し、ファインチューニングステップ中に生成されたAzure Filesに保存されたモデルとモデルアダプターにアクセスします。

## AI Toolkitの使用

### 推論のためのデプロイ
推論コードを修正したり、推論モデルを再ロードしたりする場合は、`AI Toolkit: Deploy for inference`コマンドを実行してください。これにより、最新のコードがACAと同期され、レプリカが再起動されます。

![Deploy for inference](../../../../imgs/03/RemoteServer/command-deploy.png)

デプロイが正常に完了すると、このエンドポイントを使用してモデルを評価する準備が整います。

### 推論APIへのアクセス

VSCodeの通知に表示される"*Go to Inference Endpoint*"ボタンをクリックすることで、推論APIにアクセスできます。あるいは、Web APIエンドポイントは`./infra/inference.config.json`の`ACA_APP_ENDPOINT`および出力パネルにあります。

![App Endpoint](../../../../imgs/03/RemoteServer/notification-deploy.png)

> **注意:** 推論エンドポイントが完全に動作するまでに数分かかる場合があります。

## テンプレートに含まれる推論コンポーネント

| フォルダー | 内容 |
| ------ |--------- |
| `infra` | リモート操作に必要なすべての設定が含まれています。 |
| `infra/provision/inference.parameters.json` | Bicepテンプレートのパラメーターが含まれており、推論のためのAzureリソースのプロビジョニングに使用されます。 |
| `infra/provision/inference.bicep` | 推論のためのAzureリソースのプロビジョニング用テンプレートが含まれています。 |
| `infra/inference.config.json` | `AI Toolkit: Provision Azure Container Apps for inference`コマンドによって生成される設定ファイルです。他のリモートコマンドパレットの入力として使用されます。 |

### AI Toolkitを使用してAzureリソースのプロビジョニングを設定する
[AI Toolkit](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)を設定します。

推論のためのAzure Container Appsのプロビジョニング`コマンド。

設定パラメーターは`./infra/provision/inference.parameters.json`ファイルにあります。詳細は以下の通りです：
| パラメーター | 説明 |
| --------- |------------ |
| `defaultCommands` | これはWeb APIを起動するためのコマンドです。 |
| `maximumInstanceCount` | このパラメーターはGPUインスタンスの最大容量を設定します。 |
| `location` | これはAzureリソースがプロビジョニングされる場所です。デフォルト値は選択したリソースグループの場所と同じです。 |
| `storageAccountName`, `fileShareName` `acaEnvironmentName`, `acaEnvironmentStorageName`, `acaAppName`,  `acaLogAnalyticsName` | これらのパラメーターは、プロビジョニングするAzureリソースの名前を指定します。デフォルトでは、ファインチューニングリソース名と同じになります。新しい未使用のリソース名を入力して独自のカスタム名のリソースを作成するか、既存のAzureリソースの名前を入力してそれを使用することができます。詳細については、[既存のAzureリソースの使用](#using-existing-azure-resources)セクションを参照してください。 |

### 既存のAzureリソースの使用

デフォルトでは、推論プロビジョニングは、ファインチューニングに使用されたのと同じAzure Container App Environment、Storage Account、Azure File Share、およびAzure Log Analyticsを使用します。推論API専用のAzure Container Appが作成されます。

ファインチューニングステップ中にAzureリソースをカスタマイズした場合、または推論のために既存のAzureリソースを使用したい場合は、`./infra/inference.parameters.json`ファイルにそれらの名前を指定してください。その後、コマンドパレットから`AI Toolkit: Provision Azure Container Apps for inference`コマンドを実行します。これにより、指定されたリソースが更新され、欠落しているリソースが作成されます。

例えば、既存のAzureコンテナ環境がある場合、`./infra/finetuning.parameters.json`は次のようになります：

```json
{
    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentParameters.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
      ...
      "acaEnvironmentName": {
        "value": "<your-aca-env-name>"
      },
      "acaEnvironmentStorageName": {
        "value": null
      },
      ...
    }
  }
```

### 手動プロビジョニング
Azureリソースを手動で設定することを好む場合は、`./infra/provision`フォルダーに提供されているBicepファイルを使用できます。AI Toolkitコマンドパレットを使用せずにすでにすべてのAzureリソースを設定および構成している場合は、`inference.config.json`ファイルにリソース名を入力するだけです。

例えば：

```json
{
  "SUBSCRIPTION_ID": "<your-subscription-id>",
  "RESOURCE_GROUP_NAME": "<your-resource-group-name>",
  "STORAGE_ACCOUNT_NAME": "<your-storage-account-name>",
  "FILE_SHARE_NAME": "<your-file-share-name>",
  "ACA_APP_NAME": "<your-aca-name>",
  "ACA_APP_ENDPOINT": "<your-aca-endpoint>"
}
```
