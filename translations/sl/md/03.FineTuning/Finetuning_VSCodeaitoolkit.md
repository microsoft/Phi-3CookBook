## Dobrodošli v AI Toolkit za VS Code

[AI Toolkit za VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) združuje različne modele iz Azure AI Studio Kataloga in drugih katalogov, kot je Hugging Face. Orodje poenostavi pogoste naloge razvoja AI aplikacij z uporabo generativnih AI orodij in modelov prek:
- Začetek z odkrivanjem modelov in preizkušanjem.
- Fino prilagajanje in inferenco modelov z uporabo lokalnih računalniških virov.
- Oddaljeno fino prilagajanje in inferenco z uporabo Azure virov.

[Namesti AI Toolkit za VSCode](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/Aitoolkit.fc953930f4b4027110910d62005d87c6ac76941120d31139a2d9b0de2d4b64b8.sl.png)

**[Zasebni predogled]** En klik za zagotavljanje Azure Container Apps za izvajanje finega prilagajanja in inferenciranja modelov v oblaku.

Zdaj pa se podajmo v razvoj vaše AI aplikacije:

- [Dobrodošli v AI Toolkit za VS Code](../../../../md/03.FineTuning)
- [Lokalni razvoj](../../../../md/03.FineTuning)
  - [Priprave](../../../../md/03.FineTuning)
  - [Aktivacija Conda](../../../../md/03.FineTuning)
  - [Samo fino prilagajanje osnovnega modela](../../../../md/03.FineTuning)
  - [Fino prilagajanje in inferenca modela](../../../../md/03.FineTuning)
  - [Fino prilagajanje modela](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [Primeri in viri za fino prilagajanje](../../../../md/03.FineTuning)
- [**\[Zasebni predogled\]** Oddaljeni razvoj](../../../../md/03.FineTuning)
  - [Predpogoji](../../../../md/03.FineTuning)
  - [Nastavitev oddaljenega razvojnega projekta](../../../../md/03.FineTuning)
  - [Zagotavljanje Azure virov](../../../../md/03.FineTuning)
  - [\[Neobvezno\] Dodaj Huggingface Token v skrivnost Azure Container App](../../../../md/03.FineTuning)
  - [Izvedba finega prilagajanja](../../../../md/03.FineTuning)
  - [Zagotavljanje inferenčne točke](../../../../md/03.FineTuning)
  - [Namestitev inferenčne točke](../../../../md/03.FineTuning)
  - [Napredna uporaba](../../../../md/03.FineTuning)

## Lokalni razvoj
### Priprave

1. Prepričajte se, da je NVIDIA gonilnik nameščen na gostitelju.
2. Zaženite `huggingface-cli login`, če uporabljate HF za uporabo podatkovnih zbirk.
3. `Olive` pojasnila nastavitev ključev za vse, kar spreminja uporabo pomnilnika.

### Aktivacija Conda
Ker uporabljamo okolje WSL in je deljeno, morate ročno aktivirati okolje conda. Po tem koraku lahko zaženete fino prilagajanje ali inferenco.

```bash
conda activate [conda-env-name] 
```

### Samo fino prilagajanje osnovnega modela
Če želite preizkusiti osnovni model brez finega prilagajanja, lahko po aktivaciji conda zaženete ta ukaz.

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### Fino prilagajanje in inferenca modela

Ko je delovni prostor odprt v razvojni posodi, odprite terminal (privzeta pot je koren projekta) in nato zaženite spodnji ukaz za fino prilagajanje LLM na izbranem naboru podatkov.

```bash
python finetuning/invoke_olive.py 
```

Kontrolne točke in končni model bodo shranjeni v `models` folder.

Next run inferencing with the fune-tuned model through chats in a `console`, `web browser` or `prompt flow`.

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

Za uporabo `prompt flow` in VS Code, please refer to this [Quick Start](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html).

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
2. If you are using private dataset on HuggingFace, make sure you have a [HuggingFace account](https://huggingface.co/?WT.mc_id=aiml-137032-kinfeylo) and [generate an access token](https://huggingface.co/docs/hub/security-tokens?WT.mc_id=aiml-137032-kinfeylo)
3. Enable Remote Fine-tuning and Inference feature flag in the AI Toolkit for VS Code
   1. Open the VS Code Settings by selecting *File -> Preferences -> Settings*.
   2. Navigate to *Extensions* and select *AI Toolkit*.
   3. Select the *"Enable Remote Fine-tuning And Inference"* option.
   4. Reload VS Code to take effect.

- [Remote Fine tuning](https://github.com/microsoft/vscode-ai-toolkit/blob/main/archive/remote-finetuning.md)

### Setting Up a Remote Development Project
1. Execute the command palette `AI Toolkit: Osredotoči se na pogled virov`.
2. Navigate to *Model Fine-tuning* to access the model catalog. Assign a name to your project and select its location on your machine. Then, hit the *"Configure Project"* button.
3. Project Configuration
    1. Avoid enabling the *"Fine-tune locally"* option.
    2. The Olive configuration settings will appear with pre-set default values. Please adjust and fill in these configurations as required.
    3. Move on to *Generate Project*. This stage leverages WSL and involves setting up a new Conda environment, preparing for future updates that include Dev Containers.
4. Click on *"Relaunch Window In Workspace"* to open your remote development project.

> **Note:** The project currently works either locally or remotely within the AI Toolkit for VS Code. If you choose *"Fine-tune locally"* during project creation, it will operate exclusively in WSL without remote development capabilities. On the other hand, if you forego enabling *"Fine-tune locally"*, the project will be restricted to the remote Azure Container App environment.

### Provision Azure Resources
To get started, you need to provision the Azure Resource for remote fine-tuning. Do this by running the `AI Toolkit: Zagotovi Azure Container Apps nalogo za fino prilagajanje` from the command palette.

Monitor the progress of the provision through the link displayed in the output channel.

### [Optional] Add Huggingface Token to the Azure Container App Secret
If you're using private HuggingFace dataset, set your HuggingFace token as an environment variable to avoid the need for manual login on the Hugging Face Hub.
You can do this using the `AI Toolkit: Dodaj skrivnost naloge Azure Container Apps za ukaz za fino prilagajanje`. With this command, you can set the secret name as [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) and use your Hugging Face token as the secret value.

### Run Fine-tuning
To start the remote fine-tuning job, execute the `AI Toolkit: Zaženi fino prilagajanje` command.

To view the system and console logs, you can visit the Azure portal using the link in the output panel (more steps at [View and Query Logs on Azure](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)). Or, you can view the console logs directly in the VSCode output panel by running the command `AI Toolkit: Prikaži pretočne dnevnike tekoče naloge za fino prilagajanje`. 
> **Note:** The job might be queued due to insufficient resources. If the log is not displayed, execute the `AI Toolkit: Prikaži pretočne dnevnike tekoče naloge za fino prilagajanje` command, wait for a while and then execute the command again to re-connect to the streaming log.

During this process, QLoRA will be used for fine-tuning, and will create LoRA adapters for the model to use during inference.
The results of the fine-tuning will be stored in the Azure Files.

### Provision Inference Endpoint
After the adapters are trained in the remote environment, use a simple Gradio application to interact with the model.
Similar to the fine-tuning process, you need to set up the Azure Resources for remote inference by executing the `AI Toolkit: Zagotovi Azure Container Apps za inferenco` from the command palette.

By default, the subscription and the resource group for inference should match those used for fine-tuning. The inference will use the same Azure Container App Environment and access the model and model adapter stored in Azure Files, which were generated during the fine-tuning step. 


### Deploy the Inference Endpoint
If you wish to revise the inference code or reload the inference model, please execute the `AI Toolkit: Namesti za inferenco` command. This will synchronize your latest code with Azure Container App and restart the replica.  

Once deployment is successfully completed, you can access the inference API by clicking on the "*Go to Inference Endpoint*" button displayed in the VSCode notification. Or, the web API endpoint can be found under `ACA_APP_ENDPOINT` in `./infra/inference.config.json` in v izhodni plošči. Zdaj ste pripravljeni na vrednotenje modela z uporabo te točke.

### Napredna uporaba
Za več informacij o oddaljenem razvoju z AI Toolkit si oglejte dokumentacijo [Fino prilagajanje modelov na daljavo](https://aka.ms/ai-toolkit/remote-provision) in [Inferenca z fino prilagojenim modelom](https://aka.ms/ai-toolkit/remote-inference).

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitev strojnega prevajanja z umetno inteligenco. Čeprav si prizadevamo za natančnost, vas prosimo, da upoštevate, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo strokovni človeški prevod. Ne prevzemamo odgovornosti za morebitna nesporazumevanja ali napačne interpretacije, ki izhajajo iz uporabe tega prevoda.