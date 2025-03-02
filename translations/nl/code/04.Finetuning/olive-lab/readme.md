# Lab. Optimaliseer AI-modellen voor on-device inferentie

## Introductie 

> [!IMPORTANT]
> Deze lab vereist een **Nvidia A10 of A100 GPU** met bijbehorende drivers en CUDA-toolkit (versie 12+) geïnstalleerd.

> [!NOTE]
> Dit is een **lab van 35 minuten** waarin je hands-on kennis maakt met de kernconcepten van het optimaliseren van modellen voor on-device inferentie met behulp van OLIVE.

## Leerdoelen

Aan het einde van deze lab kun je OLIVE gebruiken om:

- Een AI-model te kwantiseren met behulp van de AWQ-kwantisatiemethode.
- Een AI-model fijn af te stemmen voor een specifieke taak.
- LoRA-adapters (fijn afgestemd model) te genereren voor efficiënte on-device inferentie op de ONNX Runtime.

### Wat is Olive

Olive (*O*NNX *live*) is een toolkit voor modeloptimalisatie met een bijbehorende CLI, waarmee je modellen kunt leveren voor de ONNX runtime +++https://onnxruntime.ai+++ met kwaliteit en prestaties.

![Olive Flow](../../../../../translated_images/olive-flow.e4682fa65f77777f49e884482fa8dd83eadcb90904fcb41a54093af85c330060.nl.png)

De invoer voor Olive is meestal een PyTorch- of Hugging Face-model, en de uitvoer is een geoptimaliseerd ONNX-model dat wordt uitgevoerd op een apparaat (implementatiedoel) met de ONNX runtime. Olive optimaliseert het model voor de AI-versneller (NPU, GPU, CPU) van het implementatiedoel, geleverd door een hardwareleverancier zoals Qualcomm, AMD, Nvidia of Intel.

Olive voert een *workflow* uit, een geordende reeks individuele modeloptimalisatietaken die *passes* worden genoemd. Voorbeelden van passes zijn: modelcompressie, grafiekopname, kwantisatie, grafiekoptimalisatie. Elke pass heeft een set parameters die kunnen worden afgestemd om de beste statistieken te behalen, zoals nauwkeurigheid en latentie, die worden geëvalueerd door de respectieve evaluator. Olive maakt gebruik van een zoekstrategie die een zoekalgoritme gebruikt om elke pass afzonderlijk of een set passes samen automatisch af te stemmen.

#### Voordelen van Olive

- **Minder frustratie en tijd** door trial-and-error handmatige experimenten met verschillende technieken voor grafiekoptimalisatie, compressie en kwantisatie. Definieer je kwaliteits- en prestatie-eisen en laat Olive automatisch het beste model voor je vinden.
- **Meer dan 40 ingebouwde modeloptimalisatiecomponenten** die gebruikmaken van geavanceerde technieken in kwantisatie, compressie, grafiekoptimalisatie en fijn afstemmen.
- **Gebruiksvriendelijke CLI** voor veelvoorkomende modeloptimalisatietaken. Bijvoorbeeld olive quantize, olive auto-opt, olive finetune.
- Modelverpakking en -implementatie ingebouwd.
- Ondersteunt het genereren van modellen voor **Multi LoRA serving**.
- Stel workflows samen met YAML/JSON om modeloptimalisatie- en implementatietaken te orkestreren.
- **Hugging Face** en **Azure AI** integratie.
- Ingebouwd **cachesysteem** om **kosten te besparen**.

## Labinstructies
> [!NOTE]
> Zorg ervoor dat je je Azure AI Hub en Project hebt ingericht en je A100 compute hebt ingesteld zoals beschreven in Lab 1.

### Stap 0: Verbinden met je Azure AI Compute

Je maakt verbinding met Azure AI compute via de remote-functie in **VS Code.** 

1. Open je **VS Code** desktopapplicatie:
1. Open de **command palette** met **Shift+Ctrl+P**.
1. Zoek in de command palette naar **AzureML - remote: Connect to compute instance in New Window**.
1. Volg de instructies op het scherm om verbinding te maken met de Compute. Dit omvat het selecteren van je Azure-abonnement, resourcegroep, project en computenaam die je hebt ingesteld in Lab 1.
1. Zodra je verbonden bent met je Azure ML Compute-node, wordt dit weergegeven in de **linkerbenedenhoek van Visual Code** `><Azure ML: Compute Name`.

### Stap 1: Deze repo klonen

In VS Code kun je een nieuwe terminal openen met **Ctrl+J** en deze repo klonen:

In de terminal zou je de prompt moeten zien

```
azureuser@computername:~/cloudfiles/code$ 
```
Kloon de oplossing 

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Stap 2: Map openen in VS Code

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
> Het installeren van alle afhankelijkheden duurt ongeveer 5 minuten.

In deze lab download en upload je modellen naar de Azure AI Model-catalogus. Om toegang te krijgen tot de modelcatalogus moet je inloggen bij Azure met:

```bash
az login
```

> [!NOTE]
> Tijdens het inloggen wordt gevraagd om je abonnement te selecteren. Zorg ervoor dat je het abonnement kiest dat voor deze lab is voorzien.

### Stap 4: Olive-commando's uitvoeren 

Open een terminalvenster in VS Code in je Azure AI Compute Instance (tip: **Ctrl+J**) en zorg ervoor dat de `olive-ai` conda-omgeving is geactiveerd:

```bash
conda activate olive-ai
```

Voer vervolgens de volgende Olive-commando's uit in de opdrachtregel.

1. **Inspecteer de data:** In dit voorbeeld ga je het Phi-3.5-Mini-model fijn afstemmen zodat het gespecialiseerd is in het beantwoorden van reisinformatievragen. De onderstaande code toont de eerste paar records van de dataset, die in JSON-lines-formaat zijn:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Kwantiseren van het model:** Voordat je het model traint, kwantiseer je het eerst met het volgende commando dat gebruikmaakt van een techniek genaamd Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ kwantiseert de gewichten van een model door rekening te houden met de activaties die tijdens inferentie worden geproduceerd. Dit betekent dat het kwantisatieproces rekening houdt met de daadwerkelijke dataverdeling in de activaties, wat leidt tot een betere nauwkeurigheidsbehoud van het model in vergelijking met traditionele gewichts-kwantisatiemethoden.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    Het duurt **ongeveer 8 minuten** om de AWQ-kwantisatie te voltooien, wat de modelgrootte zal **verminderen van ~7,5GB naar ~2,5GB**.
   
   In deze lab laten we zien hoe je modellen invoert vanuit Hugging Face (bijvoorbeeld: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune`-commando het gekwantisatieerde model fijnstemt. Het model *voorafgaand aan* het fijn afstemmen kwantiseren in plaats van erna geeft een betere nauwkeurigheid omdat het fijn-afstemmingsproces enig verlies van de kwantisatie herstelt.
    
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
    
    Het duurt **ongeveer 6 minuten** om de fijn-afstemming te voltooien (met 100 stappen).

1. **Optimaliseren:** Met het getrainde model optimaliseer je nu het model met Olive's `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider`-argumenten - maar voor deze lab gebruiken we CPU.

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
    
    Het duurt **ongeveer 5 minuten** om de optimalisatie te voltooien.

### Stap 5: Snel testen van model-inferentie

Om de inferentie van het model te testen, maak je een Python-bestand in je map genaamd **app.py** en kopieer-en-plak je de volgende code:

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

### Stap 6: Model uploaden naar Azure AI

Door het model te uploaden naar een Azure AI-modelrepository wordt het model deelbaar met andere leden van je ontwikkelingsteam en wordt ook de versiecontrole van het model afgehandeld. Om het model te uploaden, voer je het volgende commando uit:

> [!NOTE]
> Werk de `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"` en Azure AI-projectnaam bij en voer het volgende commando uit 

```
az ml workspace show
```

Of ga naar +++ai.azure.com+++ en selecteer **management center**, **project**, **overzicht**.

Werk de `{}`-plaatsaanduidingen bij met de naam van je resourcegroep en Azure AI-projectnaam.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
Je kunt je geüploade model bekijken en je model implementeren op https://ml.azure.com/model/list

**Disclaimer (Vrijwaring):**  
Dit document is vertaald met behulp van machine-gebaseerde AI-vertalingsdiensten. Hoewel we ons inspannen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het oorspronkelijke document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.