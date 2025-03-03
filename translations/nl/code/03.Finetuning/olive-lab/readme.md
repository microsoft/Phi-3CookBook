# Lab. Optimaliseer AI-modellen voor on-device inference

## Introductie

> [!IMPORTANT]
> Deze lab vereist een **Nvidia A10 of A100 GPU** met bijbehorende drivers en geïnstalleerde CUDA-toolkit (versie 12+).

> [!NOTE]
> Dit is een **35-minuten** durende lab waarin je een praktische introductie krijgt tot de kernconcepten van het optimaliseren van modellen voor on-device inference met behulp van OLIVE.

## Leerdoelen

Aan het einde van deze lab kun je met OLIVE:

- Een AI-model kwantificeren met de AWQ-kwantisatiemethode.
- Een AI-model fine-tunen voor een specifieke taak.
- LoRA-adapters (gefinetuned model) genereren voor efficiënte on-device inference op de ONNX Runtime.

### Wat is Olive

Olive (*O*NNX *live*) is een modeloptimalisatietoolkit met een bijbehorende CLI waarmee je modellen kunt implementeren voor de ONNX runtime +++https://onnxruntime.ai+++ met kwaliteit en prestaties.

![Olive Flow](../../../../../translated_images/olive-flow.5beac74493fb2216eb8578519cfb1c4a1e752a3536bc755c4545bd0959634684.nl.png)

De input voor Olive is doorgaans een PyTorch- of Hugging Face-model, en de output is een geoptimaliseerd ONNX-model dat wordt uitgevoerd op een apparaat (implementatiedoel) dat de ONNX runtime gebruikt. Olive optimaliseert het model voor de AI-versneller (NPU, GPU, CPU) van het implementatiedoel, geleverd door een hardwareleverancier zoals Qualcomm, AMD, Nvidia of Intel.

Olive voert een *workflow* uit, wat een geordende reeks van individuele modeloptimalisatietaken genaamd *passes* is - voorbeelden van passes zijn: modelcompressie, grafiekopname, kwantisatie, grafiekoptimalisatie. Elke pass heeft een reeks parameters die kunnen worden aangepast om de beste metriek te bereiken, bijvoorbeeld nauwkeurigheid en latentie, die worden geëvalueerd door de respectieve evaluator. Olive gebruikt een zoekstrategie met een zoekalgoritme om elke pass afzonderlijk of een set passes samen automatisch te optimaliseren.

#### Voordelen van Olive

- **Minder frustratie en tijd** door trial-and-error handmatige experimenten met verschillende technieken voor grafiekoptimalisatie, compressie en kwantisatie te verminderen. Definieer je kwaliteits- en prestatie-eisen en laat Olive automatisch het beste model voor je vinden.
- **Meer dan 40 ingebouwde modeloptimalisatiecomponenten** die gebruik maken van de nieuwste technieken op het gebied van kwantisatie, compressie, grafiekoptimalisatie en finetuning.
- **Eenvoudig te gebruiken CLI** voor veelvoorkomende modeloptimalisatietaken. Bijvoorbeeld olive quantize, olive auto-opt, olive finetune.
- Modelverpakking en implementatie ingebouwd.
- Ondersteuning voor het genereren van modellen voor **Multi LoRA serving**.
- Workflows bouwen met YAML/JSON om modeloptimalisatie- en implementatietaken te orkestreren.
- **Hugging Face** en **Azure AI** integratie.
- Ingebouwd **cachingsysteem** om **kosten te besparen**.

## Labinstructies
> [!NOTE]
> Zorg ervoor dat je je Azure AI Hub en Project hebt ingericht en je A100 compute hebt ingesteld zoals beschreven in Lab 1.

### Stap 0: Verbind met je Azure AI Compute

Je maakt verbinding met de Azure AI compute met behulp van de remote-functie in **VS Code.** 

1. Open je **VS Code** desktopapplicatie:
1. Open de **command palette** met **Shift+Ctrl+P**.
1. Zoek in de command palette naar **AzureML - remote: Connect to compute instance in New Window**.
1. Volg de instructies op het scherm om verbinding te maken met de Compute. Dit omvat het selecteren van je Azure Subscription, Resource Group, Project en Compute-naam die je hebt ingesteld in Lab 1.
1. Zodra je verbonden bent met je Azure ML Compute-node, wordt dit weergegeven in de **linkerbenedenhoek van Visual Code** `><Azure ML: Compute Name`.

### Stap 1: Clone deze repo

In VS Code kun je een nieuwe terminal openen met **Ctrl+J** en deze repo clonen:

In de terminal zou je de prompt moeten zien

```
azureuser@computername:~/cloudfiles/code$ 
```
Clone de oplossing 

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Stap 2: Open map in VS Code

Om VS Code in de relevante map te openen, voer je het volgende commando uit in de terminal. Dit opent een nieuw venster:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Je kunt de map ook openen door **Bestand** > **Map openen** te selecteren. 

### Stap 3: Afhankelijkheden

Open een terminalvenster in VS Code in je Azure AI Compute Instance (tip: **Ctrl+J**) en voer de volgende commando's uit om de afhankelijkheden te installeren:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> Het duurt ongeveer **5 minuten** om alle afhankelijkheden te installeren.

In deze lab download en upload je modellen naar de Azure AI Model-catalogus. Om toegang te krijgen tot de modelcatalogus moet je inloggen op Azure met:

```bash
az login
```

> [!NOTE]
> Tijdens het inloggen wordt je gevraagd je abonnement te selecteren. Zorg ervoor dat je het abonnement selecteert dat voor deze lab is verstrekt.

### Stap 4: Voer Olive-commando's uit

Open een terminalvenster in VS Code in je Azure AI Compute Instance (tip: **Ctrl+J**) en zorg ervoor dat de `olive-ai` conda-omgeving is geactiveerd:

```bash
conda activate olive-ai
```

Voer vervolgens de volgende Olive-commando's uit in de opdrachtregel.

1. **Inspecteer de data:** In dit voorbeeld ga je het Phi-3.5-Mini model fine-tunen zodat het gespecialiseerd is in het beantwoorden van reisgerelateerde vragen. De onderstaande code toont de eerste paar records van de dataset, die in JSON-lines formaat zijn:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Kwantificeer het model:** Voordat je het model traint, kwantificeer je het eerst met het volgende commando dat een techniek gebruikt genaamd Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ kwantificeert de gewichten van een model door rekening te houden met de activaties die tijdens inference worden geproduceerd. Dit betekent dat het kwantisatieproces rekening houdt met de werkelijke dataverdeling in de activaties, wat leidt tot een betere behoud van modelnauwkeurigheid in vergelijking met traditionele methoden voor gewichts-kwantisatie.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    Het duurt ongeveer **8 minuten** om de AWQ-kwantisatie te voltooien, wat de modelgrootte **vermindert van ~7,5GB naar ~2,5GB**.
   
   In deze lab laten we zien hoe je modellen van Hugging Face kunt invoeren (bijvoorbeeld: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` commando fine-tunet het gekwantificeerde model. Het model *voor* het fine-tunen kwantificeren in plaats van erna geeft betere nauwkeurigheid omdat het fine-tuneproces een deel van het verlies door de kwantisatie herstelt.
    
    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```
    
    Het duurt ongeveer **6 minuten** om het fine-tunen te voltooien (met 100 stappen).

1. **Optimaliseer:** Met het model getraind, optimaliseer je nu het model met Olive's `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` argumenten - maar voor de doeleinden van deze lab gebruiken we CPU.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```
    
    Het duurt ongeveer **5 minuten** om de optimalisatie te voltooien.

### Stap 5: Snelle test van modelinference

Om het model te testen, maak je een Python-bestand in je map genaamd **app.py** en kopieer-en-plak je de volgende code:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

Voer de code uit met:

```bash
python app.py
```

### Stap 6: Upload model naar Azure AI

Het uploaden van het model naar een Azure AI-modelrepository maakt het model deelbaar met andere leden van je ontwikkelingsteam en zorgt ook voor versiebeheer van het model. Om het model te uploaden, voer je het volgende commando uit:

> [!NOTE]
> Werk de `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup" en Azure AI Project naam bij, en voer het volgende commando uit 

```
az ml workspace show
```

Of door naar +++ai.azure.com+++ te gaan en **management center** **project** **overview** te selecteren.

Werk de `{}` placeholders bij met de naam van je resourcegroep en Azure AI Projectnaam.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
Je kunt vervolgens je geüploade model bekijken en implementeren via https://ml.azure.com/model/list

**Disclaimer**:  
Dit document is vertaald met behulp van machine-gebaseerde AI-vertalingsdiensten. Hoewel we ons best doen voor nauwkeurigheid, moet u zich ervan bewust zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.