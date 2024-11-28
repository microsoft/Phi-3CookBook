## AI Toolkit for VS Code へようこそ

[AI Toolkit for VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) は、Azure AI Studio CatalogやHugging Faceなどのカタログから様々なモデルを集めています。このツールキットは、生成AIツールやモデルを使用したAIアプリの開発における一般的なタスクを簡素化します：
- モデルの発見とプレイグラウンドから始める。
- ローカルコンピューティングリソースを使用したモデルの微調整と推論。
- Azureリソースを使用したリモート微調整と推論。

[Install AI Toolkit for VSCode](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/Aitoolkit.e66b56f619fdbb43d80893a20ec56678138f438ae58bfd34b6726ae4d96a1cc4.ja.png)

**[Private Preview]** モデルの微調整と推論をクラウドで実行するためのAzure Container Appsのワンクリックプロビジョニング。

それでは、AIアプリ開発に進みましょう：

- [ローカル開発](../../../../md/04.Fine-tuning)
    - [準備](../../../../md/04.Fine-tuning)
    - [Condaのアクティベート](../../../../md/04.Fine-tuning)
    - [ベースモデルの微調整のみ](../../../../md/04.Fine-tuning)
    - [モデルの微調整と推論](../../../../md/04.Fine-tuning)
- [**[Private Preview]** リモート開発](../../../../md/04.Fine-tuning)
    - [前提条件](../../../../md/04.Fine-tuning)
    - [リモート開発プロジェクトの設定](../../../../md/04.Fine-tuning)
    - [Azureリソースのプロビジョニング](../../../../md/04.Fine-tuning)
    - [[任意] HuggingfaceトークンをAzure Container App Secretに追加](../../../../md/04.Fine-tuning)
    - [微調整の実行](../../../../md/04.Fine-tuning)
    - [推論エンドポイントのプロビジョニング](../../../../md/04.Fine-tuning)
    - [推論エンドポイントのデプロイ](../../../../md/04.Fine-tuning)
    - [高度な使用方法](../../../../md/04.Fine-tuning)

## ローカル開発
### 準備

1. ホストにNVIDIAドライバーがインストールされていることを確認してください。
2. データセットの利用にHFを使用する場合は`huggingface-cli login`を実行します。
3. `Olive` メモリ使用量を変更するものに関するキー設定の説明。

### Condaのアクティベート
WSL環境を使用しており、共有されているため、手動でconda環境をアクティベートする必要があります。このステップの後、微調整や推論を実行できます。

```bash
conda activate [conda-env-name] 
```

### ベースモデルの微調整のみ
微調整なしでベースモデルを試したい場合は、condaをアクティベートした後にこのコマンドを実行します。

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### モデルの微調整と推論

ワークスペースが開発コンテナで開かれたら、ターミナルを開き（デフォルトのパスはプロジェクトルート）、選択したデータセットに対してLLMを微調整するために以下のコマンドを実行します。

```bash
python finetuning/invoke_olive.py 
```

チェックポイントと最終モデルは `models` folder.

Next run inferencing with the fune-tuned model through chats in a `console`, `web browser` or `prompt flow` に保存されます。

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

`prompt flow` in VS Code, please refer to this [Quick Start](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html).

### Model Fine-tuning

Next, download the following model depending on the availability of a GPU on your device.

To initiate the local fine-tuning session using QLoRA, select a model you want to fine-tune from our catalog.
| Platform(s) | GPU available | Model name | Size (GB) |
|---------|---------|--------|--------|
| Windows | Yes | Phi-3-mini-4k-**directml**-int4-awq-block-128-onnx | 2.13GB |
| Linux | Yes | Phi-3-mini-4k-**cuda**-int4-onnx | 2.30GB |
| Windows<br>Linux | No | Phi-3-mini-4k-**cpu**-int4-rtn-block-32-acc-level-4-onnx | 2.72GB |

**_Note_** You do not need an Azure Account to download the models

The Phi3-mini (int4) model is approximately 2GB-3GB in size. Depending on your network speed, it could take a few minutes to download.

Start by selecting a project name and location.
Next, select a model from the model catalog. You will be prompted to download the project template. You can then click "Configure Project" to adjust various settings.

### Microsoft Olive 

We use [Olive](https://microsoft.github.io/Olive/why-olive.html) to run QLoRA fine-tuning on a PyTorch model from our catalog. All of the settings are preset with the default values to optimize to run the fine-tuning process locally with optimized use of memory, but it can be adjusted for your scenario.

### Fine Tuning Samples and Resoures

- [Fine tuning Getting Started Guide](https://learn.microsoft.com/windows/ai/toolkit/toolkit-fine-tune)
- [Fine tuning with a HuggingFace Dataset](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-hf-dataset.md)
- [Fine tuning with Simple DataSet](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/walkthrough-simple-dataset.md)

## **[Private Preview]** Remote Development

### Prerequisites

1. To run the model fine-tuning in your remote Azure Container App Environment, make sure your subscription has enough GPU capacity. Submit a [support ticket](https://azure.microsoft.com/support/create-ticket/) to request the required capacity for your application. [Get More Info about GPU capacity](https://learn.microsoft.com/azure/container-apps/workload-profiles-overview)
2. If you are using private dataset on HuggingFace, make sure you have a [HuggingFace account](https://huggingface.co/) and [generate an access token](https://huggingface.co/docs/hub/security-tokens)
3. Enable Remote Fine-tuning and Inference feature flag in the AI Toolkit for VS Code
   1. Open the VS Code Settings by selecting *File -> Preferences -> Settings*.
   2. Navigate to *Extensions* and select *AI Toolkit*.
   3. Select the *"Enable Remote Fine-tuning And Inference"* option.
   4. Reload VS Code to take effect.

- [Remote Fine tuning](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### Setting Up a Remote Development Project
1. Execute the command palette `AI Toolkit: Focus on Resource View`.
2. Navigate to *Model Fine-tuning* to access the model catalog. Assign a name to your project and select its location on your machine. Then, hit the *"Configure Project"* button.
3. Project Configuration
    1. Avoid enabling the *"Fine-tune locally"* option.
    2. The Olive configuration settings will appear with pre-set default values. Please adjust and fill in these configurations as required.
    3. Move on to *Generate Project*. This stage leverages WSL and involves setting up a new Conda environment, preparing for future updates that include Dev Containers.
4. Click on *"Relaunch Window In Workspace"* to open your remote development project.

> **Note:** The project currently works either locally or remotely within the AI Toolkit for VS Code. If you choose *"Fine-tune locally"* during project creation, it will operate exclusively in WSL without remote development capabilities. On the other hand, if you forego enabling *"Fine-tune locally"*, the project will be restricted to the remote Azure Container App environment.

### Provision Azure Resources
To get started, you need to provision the Azure Resource for remote fine-tuning. Do this by running the `AI Toolkit: Provision Azure Container Apps job for fine-tuning` from the command palette.

Monitor the progress of the provision through the link displayed in the output channel.

### [Optional] Add Huggingface Token to the Azure Container App Secret
If you're using private HuggingFace dataset, set your HuggingFace token as an environment variable to avoid the need for manual login on the Hugging Face Hub.
You can do this using the `AI Toolkit: Add Azure Container Apps Job secret for fine-tuning command`. With this command, you can set the secret name as [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) and use your Hugging Face token as the secret value.

### Run Fine-tuning
To start the remote fine-tuning job, execute the `AI Toolkit: Run fine-tuning` command.

To view the system and console logs, you can visit the Azure portal using the link in the output panel (more steps at [View and Query Logs on Azure](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)). Or, you can view the console logs directly in the VSCode output panel by running the command `AI Toolkit: Show the running fine-tuning job streaming logs`. 
> **Note:** The job might be queued due to insufficient resources. If the log is not displayed, execute the `AI Toolkit: Show the running fine-tuning job streaming logs` command, wait for a while and then execute the command again to re-connect to the streaming log.

During this process, QLoRA will be used for fine-tuning, and will create LoRA adapters for the model to use during inference.
The results of the fine-tuning will be stored in the Azure Files.

### Provision Inference Endpoint
After the adapters are trained in the remote environment, use a simple Gradio application to interact with the model.
Similar to the fine-tuning process, you need to set up the Azure Resources for remote inference by executing the `AI Toolkit: Provision Azure Container Apps for inference` from the command palette.

By default, the subscription and the resource group for inference should match those used for fine-tuning. The inference will use the same Azure Container App Environment and access the model and model adapter stored in Azure Files, which were generated during the fine-tuning step. 


### Deploy the Inference Endpoint
If you wish to revise the inference code or reload the inference model, please execute the `AI Toolkit: Deploy for inference` command. This will synchronize your latest code with Azure Container App and restart the replica.  

Once deployment is successfully completed, you can access the inference API by clicking on the "*Go to Inference Endpoint*" button displayed in the VSCode notification. Or, the web API endpoint can be found under `ACA_APP_ENDPOINT` in `./infra/inference.config.json` と出力パネルで使用できます。このエンドポイントを使用してモデルを評価する準備が整いました。

### 高度な使用方法
AI Toolkitを使用したリモート開発の詳細については、[Fine-Tuning models remotely](https://aka.ms/ai-toolkit/remote-provision) および [Inferencing with the fine-tuned model](https://aka.ms/ai-toolkit/remote-inference) のドキュメントを参照してください。

**免責事項**:
この文書は機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期していますが、自動翻訳にはエラーや不正確な点が含まれる可能性があることをご了承ください。権威ある情報源としては、元の言語での文書を考慮してください。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤訳について、当社は一切の責任を負いません。