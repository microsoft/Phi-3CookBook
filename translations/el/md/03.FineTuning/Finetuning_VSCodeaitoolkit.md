## Καλωσορίσατε στο AI Toolkit για το VS Code

[AI Toolkit για το VS Code](https://github.com/microsoft/vscode-ai-toolkit/tree/main) συνδυάζει διάφορα μοντέλα από τον Azure AI Studio Catalog και άλλους καταλόγους, όπως το Hugging Face. Το εργαλείο αυτό απλοποιεί τις συνήθεις εργασίες ανάπτυξης για τη δημιουργία εφαρμογών AI με γενετικά εργαλεία και μοντέλα μέσω:
- Εύκολης εκκίνησης με ανακάλυψη μοντέλων και playground.
- Fine-tuning και inference μοντέλων χρησιμοποιώντας τοπικούς υπολογιστικούς πόρους.
- Απομακρυσμένο fine-tuning και inference χρησιμοποιώντας πόρους του Azure.

[Εγκαταστήστε το AI Toolkit για το VS Code](https://marketplace.visualstudio.com/items?itemName=ms-windows-ai-studio.windows-ai-studio)

![AIToolkit FineTuning](../../../../translated_images/Aitoolkit.fc953930f4b4027110910d62005d87c6ac76941120d31139a2d9b0de2d4b64b8.el.png)

**[Ιδιωτική Προεπισκόπηση]** Δυνατότητα ενός κλικ για δημιουργία Azure Container Apps, ώστε να εκτελείτε fine-tuning και inference μοντέλων στο cloud.

Ας ξεκινήσουμε με την ανάπτυξη της AI εφαρμογής σας:

- [Καλωσορίσατε στο AI Toolkit για το VS Code](../../../../md/03.FineTuning)
- [Τοπική Ανάπτυξη](../../../../md/03.FineTuning)
  - [Προετοιμασίες](../../../../md/03.FineTuning)
  - [Ενεργοποίηση Conda](../../../../md/03.FineTuning)
  - [Μόνο Fine-tuning βασικού μοντέλου](../../../../md/03.FineTuning)
  - [Fine-tuning και Inference μοντέλου](../../../../md/03.FineTuning)
  - [Fine-tuning μοντέλου](../../../../md/03.FineTuning)
  - [Microsoft Olive](../../../../md/03.FineTuning)
  - [Παραδείγματα και Πόροι για Fine-tuning](../../../../md/03.FineTuning)
- [**\[Ιδιωτική Προεπισκόπηση\]** Απομακρυσμένη Ανάπτυξη](../../../../md/03.FineTuning)
  - [Προαπαιτούμενα](../../../../md/03.FineTuning)
  - [Ρύθμιση Έργου Απομακρυσμένης Ανάπτυξης](../../../../md/03.FineTuning)
  - [Δημιουργία Πόρων Azure](../../../../md/03.FineTuning)
  - [\[Προαιρετικά\] Προσθήκη Huggingface Token στο Azure Container App Secret](../../../../md/03.FineTuning)
  - [Εκτέλεση Fine-tuning](../../../../md/03.FineTuning)
  - [Δημιουργία Endpoint για Inference](../../../../md/03.FineTuning)
  - [Ανάπτυξη του Endpoint για Inference](../../../../md/03.FineTuning)
  - [Προχωρημένη χρήση](../../../../md/03.FineTuning)

## Τοπική Ανάπτυξη
### Προετοιμασίες

1. Βεβαιωθείτε ότι ο NVIDIA driver είναι εγκατεστημένος στο host.
2. Εκτελέστε `huggingface-cli login`, αν χρησιμοποιείτε το HF για την αξιοποίηση dataset.
3. `Olive` εξηγήσεις ρυθμίσεων για οτιδήποτε τροποποιεί τη χρήση μνήμης.

### Ενεργοποίηση Conda
Επειδή χρησιμοποιούμε περιβάλλον WSL και είναι κοινόχρηστο, χρειάζεται να ενεργοποιήσετε χειροκίνητα το conda περιβάλλον. Μετά από αυτό το βήμα μπορείτε να εκτελέσετε fine-tuning ή inference.

```bash
conda activate [conda-env-name] 
```

### Μόνο Fine-tuning βασικού μοντέλου
Για να δοκιμάσετε μόνο το βασικό μοντέλο χωρίς fine-tuning, μπορείτε να εκτελέσετε την παρακάτω εντολή αφού ενεργοποιήσετε το conda.

```bash
cd inference

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://0.0.0.0:7860) in a browser after gradio initiates the connections.
python gradio_chat.py --baseonly
```

### Fine-tuning και Inference μοντέλου

Μόλις ανοίξετε το workspace σε ένα dev container, ανοίξτε ένα terminal (η προεπιλεγμένη διαδρομή είναι το root του project) και εκτελέστε την παρακάτω εντολή για να κάνετε fine-tuning σε ένα LLM στο επιλεγμένο dataset.

```bash
python finetuning/invoke_olive.py 
```

Τα checkpoints και το τελικό μοντέλο θα αποθηκευτούν στο `models` folder.

Next run inferencing with the fune-tuned model through chats in a `console`, `web browser` or `prompt flow`.

```bash
cd inference

# Console interface.
python console_chat.py

# Web browser interface allows to adjust a few parameters like max new token length, temperature and so on.
# User has to manually open the link (e.g. http://127.0.0.1:7860) in a browser after gradio initiates the connections.
python gradio_chat.py
```

Για να χρησιμοποιήσετε το `prompt flow` in VS Code, please refer to this [Quick Start](https://microsoft.github.io/promptflow/how-to-guides/quick-start.html).

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

Once deployment is successfully completed, you can access the inference API by clicking on the "*Go to Inference Endpoint*" button displayed in the VSCode notification. Or, the web API endpoint can be found under `ACA_APP_ENDPOINT` in `./infra/inference.config.json` και στο output panel. Τώρα είστε έτοιμοι να αξιολογήσετε το μοντέλο χρησιμοποιώντας αυτό το endpoint.

### Προχωρημένη χρήση
Για περισσότερες πληροφορίες σχετικά με την απομακρυσμένη ανάπτυξη με το AI Toolkit, ανατρέξτε στην τεκμηρίωση [Fine-Tuning μοντέλων απομακρυσμένα](https://aka.ms/ai-toolkit/remote-provision) και [Inference με το fine-tuned μοντέλο](https://aka.ms/ai-toolkit/remote-inference).

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες μετάφρασης που βασίζονται σε τεχνητή νοημοσύνη. Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.