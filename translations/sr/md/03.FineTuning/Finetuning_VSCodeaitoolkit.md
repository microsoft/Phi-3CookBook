## Dobrodošli u AI Toolkit za VS Code

[AI Toolkit za VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) objedinjuje različite modele iz Azure AI Studio kataloga i drugih kataloga poput Hugging Face. Ovaj alat olakšava uobičajene zadatke razvoja AI aplikacija koristeći generativne AI alate i modele kroz:
- Početak rada sa otkrivanjem modela i igralištem.
- Fino podešavanje modela i izvođenje zaključaka koristeći lokalne resurse.
- Daljinsko fino podešavanje i izvođenje zaključaka koristeći Azure resurse.

[Instalirajte AI Toolkit za VSCode](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/Aitoolkit.fc953930f4b4027110910d62005d87c6ac76941120d31139a2d9b0de2d4b64b8.sr.png)

**[Privatni pregled]** Jednostavna konfiguracija za Azure Container Apps za pokretanje finog podešavanja modela i izvođenje zaključaka u oblaku.

Sada započnimo razvoj vaše AI aplikacije:

- [Dobrodošli u AI Toolkit za VS Code](../../../../md/03.FineTuning)
- [Lokalni razvoj](../../../../md/03.FineTuning)
  - [Pripreme](../../../../md/03.FineTuning)
  - [Aktiviranje Conda](../../../../md/03.FineTuning)
  - [Samo fino podešavanje osnovnog modela](../../../../md/03.FineTuning)
  - [Fino podešavanje i izvođenje zaključaka modela](../../../../md/03.FineTuning)
  - [Fino podešavanje modela](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [Primeri i resursi za fino podešavanje](../../../../md/03.FineTuning)
- [**\[Privatni pregled\]** Daljinski razvoj](../../../../md/03.FineTuning)
  - [Preduslovi](../../../../md/03.FineTuning)
  - [Postavljanje projekta za daljinski razvoj](../../../../md/03.FineTuning)
  - [Konfigurisanje Azure resursa](../../../../md/03.FineTuning)
  - [\[Opcionalno\] Dodavanje Huggingface tokena u tajnu Azure Container App-a](../../../../md/03.FineTuning)
  - [Pokretanje finog podešavanja](../../../../md/03.FineTuning)
  - [Konfigurisanje krajnje tačke za izvođenje zaključaka](../../../../md/03.FineTuning)
  - [Postavljanje krajnje tačke za izvođenje zaključaka](../../../../md/03.FineTuning)
  - [Napredna upotreba](../../../../md/03.FineTuning)

## Lokalni razvoj
### Pripreme

1. Uverite se da je NVIDIA drajver instaliran na hostu.  
2. Pokrenite `huggingface-cli login` ako koristite HF za korišćenje skupa podataka.  
3. `Olive` objašnjenja ključnih podešavanja za bilo šta što modifikuje upotrebu memorije.  

### Aktiviranje Conda
Pošto koristimo WSL okruženje koje je deljeno, potrebno je ručno aktivirati conda okruženje. Nakon ovog koraka možete pokrenuti fino podešavanje ili izvođenje zaključaka.

```bash
conda activate [conda-env-name] 
```

### Samo fino podešavanje osnovnog modela
Da biste samo isprobali osnovni model bez finog podešavanja, možete pokrenuti ovu komandu nakon aktiviranja conda okruženja.

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### Fino podešavanje i izvođenje zaključaka modela

Kada se radni prostor otvori u razvojnom kontejneru, otvorite terminal (podrazumevani put je koren projekta), a zatim pokrenite sledeću komandu za fino podešavanje LLM na odabranom skupu podataka.

```bash
python finetuning/invoke_olive.py 
```

Kontrolne tačke i konačni model će biti sačuvani u `models` folder.

Next run inferencing with the fune-tuned model through chats in a `console`, `web browser` or `prompt flow`.

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

Za korišćenje `prompt flow` in VS Code, please refer to this [Quick Start](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html).

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
1. Execute the command palette `AI Toolkit: Fokus na prikaz resursa`.
2. Navigate to *Model Fine-tuning* to access the model catalog. Assign a name to your project and select its location on your machine. Then, hit the *"Configure Project"* button.
3. Project Configuration
    1. Avoid enabling the *"Fine-tune locally"* option.
    2. The Olive configuration settings will appear with pre-set default values. Please adjust and fill in these configurations as required.
    3. Move on to *Generate Project*. This stage leverages WSL and involves setting up a new Conda environment, preparing for future updates that include Dev Containers.
4. Click on *"Relaunch Window In Workspace"* to open your remote development project.

> **Note:** The project currently works either locally or remotely within the AI Toolkit for VS Code. If you choose *"Fine-tune locally"* during project creation, it will operate exclusively in WSL without remote development capabilities. On the other hand, if you forego enabling *"Fine-tune locally"*, the project will be restricted to the remote Azure Container App environment.

### Provision Azure Resources
To get started, you need to provision the Azure Resource for remote fine-tuning. Do this by running the `AI Toolkit: Konfigurisanje Azure Container Apps posla za fino podešavanje` from the command palette.

Monitor the progress of the provision through the link displayed in the output channel.

### [Optional] Add Huggingface Token to the Azure Container App Secret
If you're using private HuggingFace dataset, set your HuggingFace token as an environment variable to avoid the need for manual login on the Hugging Face Hub.
You can do this using the `AI Toolkit: Dodavanje tajne za fino podešavanje Azure Container Apps posla`. With this command, you can set the secret name as [`HF_TOKEN`](https://huggingface.co/docs/huggingface_hub/package_reference/environment_variables#hftoken) and use your Hugging Face token as the secret value.

### Run Fine-tuning
To start the remote fine-tuning job, execute the `AI Toolkit: Pokreni fino podešavanje` command.

To view the system and console logs, you can visit the Azure portal using the link in the output panel (more steps at [View and Query Logs on Azure](https://aka.ms/ai-toolkit/remote-provision#view-and-query-logs-on-azure)). Or, you can view the console logs directly in the VSCode output panel by running the command `AI Toolkit: Prikaz strimovanja logova tekućeg posla za fino podešavanje`. 
> **Note:** The job might be queued due to insufficient resources. If the log is not displayed, execute the `AI Toolkit: Prikaz strimovanja logova tekućeg posla za fino podešavanje` command, wait for a while and then execute the command again to re-connect to the streaming log.

During this process, QLoRA will be used for fine-tuning, and will create LoRA adapters for the model to use during inference.
The results of the fine-tuning will be stored in the Azure Files.

### Provision Inference Endpoint
After the adapters are trained in the remote environment, use a simple Gradio application to interact with the model.
Similar to the fine-tuning process, you need to set up the Azure Resources for remote inference by executing the `AI Toolkit: Konfigurisanje Azure Container Apps za izvođenje zaključaka` from the command palette.

By default, the subscription and the resource group for inference should match those used for fine-tuning. The inference will use the same Azure Container App Environment and access the model and model adapter stored in Azure Files, which were generated during the fine-tuning step. 


### Deploy the Inference Endpoint
If you wish to revise the inference code or reload the inference model, please execute the `AI Toolkit: Postavljanje za izvođenje zaključaka` command. This will synchronize your latest code with Azure Container App and restart the replica.  

Once deployment is successfully completed, you can access the inference API by clicking on the "*Go to Inference Endpoint*" button displayed in the VSCode notification. Or, the web API endpoint can be found under `ACA_APP_ENDPOINT` in `./infra/inference.config.json` i u izlaznom panelu. Sada ste spremni da ocenite model koristeći ovu krajnju tačku.

### Napredna upotreba
Za više informacija o daljinskom razvoju sa AI Toolkit-om, pogledajte dokumentaciju [Fino podešavanje modela na daljinu](https://aka.ms/ai-toolkit/remote-provision) i [Izvođenje zaključaka sa fino podešenim modelom](https://aka.ms/ai-toolkit/remote-inference).

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем машинских услуга за превођење заснованих на вештачкој интелигенцији. Иако тежимо тачности, имајте у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било каква неспоразумевања или погрешна тумачења настала коришћењем овог превода.