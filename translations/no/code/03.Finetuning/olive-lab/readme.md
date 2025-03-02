# Lab. Optimaliser AI-modeller for enhetsbasert inferens

## Introduksjon 

> [!IMPORTANT]
> Dette laben krever en **Nvidia A10 eller A100 GPU** med tilhørende drivere og CUDA-verktøysett (versjon 12+) installert.

> [!NOTE]
> Dette er en **35-minutters** lab som gir deg en praktisk introduksjon til kjernekonseptene for optimalisering av modeller for enhetsbasert inferens ved bruk av OLIVE.

## Læringsmål

Ved slutten av denne laben vil du kunne bruke OLIVE til å:

- Kvantisere en AI-modell ved hjelp av AWQ-kvantisering.
- Finjustere en AI-modell for en spesifikk oppgave.
- Generere LoRA-adaptere (finjustert modell) for effektiv enhetsbasert inferens på ONNX Runtime.

### Hva er Olive

Olive (*O*NNX *live*) er et verktøy for modelloptimalisering med tilhørende CLI som gjør det mulig å levere modeller for ONNX runtime +++https://onnxruntime.ai+++ med høy kvalitet og ytelse.

![Olive Flow](../../../../../translated_images/olive-flow.5beac74493fb2216eb8578519cfb1c4a1e752a3536bc755c4545bd0959634684.no.png)

Inndata til Olive er vanligvis en PyTorch- eller Hugging Face-modell, og utdata er en optimalisert ONNX-modell som kjøres på en enhet (utplasseringsmål) med ONNX runtime. Olive optimaliserer modellen for AI-akseleratoren (NPU, GPU, CPU) som tilbys av en maskinvareleverandør som Qualcomm, AMD, Nvidia eller Intel.

Olive kjører en *arbeidsflyt*, som er en ordnet sekvens av individuelle modelloptimaliseringstasker kalt *passes* - eksempler på passes inkluderer: modellkompresjon, grafinnsamling, kvantisering, grafoptimalisering. Hver pass har et sett med parametere som kan justeres for å oppnå de beste målingene, som nøyaktighet og forsinkelse, som vurderes av den respektive evaluator. Olive bruker en søkestrategi med en algoritme for å finjustere hver pass én etter én eller flere passes sammen.

#### Fordeler med Olive

- **Reduser frustrasjon og tid** brukt på prøving og feiling med forskjellige teknikker for grafoptimalisering, kompresjon og kvantisering. Definer dine kvalitets- og ytelseskrav, og la Olive automatisk finne den beste modellen for deg.
- **40+ innebygde komponenter for modelloptimalisering** som dekker de nyeste teknikkene innen kvantisering, kompresjon, grafoptimalisering og finjustering.
- **Brukervennlig CLI** for vanlige modelloptimaliseringstasker. For eksempel: olive quantize, olive auto-opt, olive finetune.
- Innebygd modellpakking og distribusjon.
- Støtte for generering av modeller for **Multi LoRA-tjenester**.
- Lag arbeidsflyter med YAML/JSON for å organisere modelloptimalisering og distribusjonstasker.
- Integrasjon med **Hugging Face** og **Azure AI**.
- Innebygd **cache-mekanisme** for å **spare kostnader**.

## Labinstruksjoner
> [!NOTE]
> Sørg for at du har opprettet din Azure AI Hub og prosjekt, og satt opp din A100 compute som beskrevet i Lab 1.

### Steg 0: Koble til din Azure AI Compute

Du vil koble til Azure AI compute ved å bruke fjernfunksjonen i **VS Code.** 

1. Åpne din **VS Code** desktop-applikasjon:
1. Åpne **kommandopaletten** ved å bruke **Shift+Ctrl+P**
1. Søk i kommandopaletten etter **AzureML - remote: Connect to compute instance in New Window**.
1. Følg instruksjonene på skjermen for å koble til Compute. Dette innebærer å velge din Azure-abonnement, ressursgruppe, prosjekt og Compute-navn som du satte opp i Lab 1.
1. Når du er koblet til din Azure ML Compute-node, vil dette vises nederst til venstre i Visual Code `><Azure ML: Compute Name`

### Steg 1: Klon dette repoet

I VS Code kan du åpne en ny terminal med **Ctrl+J** og klone dette repoet:

I terminalen skal du se prompten

```
azureuser@computername:~/cloudfiles/code$ 
```
Klon løsningen 

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Steg 2: Åpne mappe i VS Code

For å åpne VS Code i riktig mappe, kjør følgende kommando i terminalen, som vil åpne et nytt vindu:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Alternativt kan du åpne mappen ved å velge **File** > **Open Folder**. 

### Steg 3: Avhengigheter

Åpne et terminalvindu i VS Code i din Azure AI Compute-instans (tips: **Ctrl+J**) og kjør følgende kommandoer for å installere avhengighetene:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> Det vil ta omtrent **5 minutter** å installere alle avhengighetene.

I denne laben vil du laste ned og laste opp modeller til Azure AI Model-katalogen. For å få tilgang til modellkatalogen må du logge inn på Azure ved å bruke:

```bash
az login
```

> [!NOTE]
> Ved innlogging vil du bli bedt om å velge abonnement. Sørg for å velge abonnementet som er gitt for denne laben.

### Steg 4: Kjør Olive-kommandoer 

Åpne et terminalvindu i VS Code i din Azure AI Compute-instans (tips: **Ctrl+J**) og sørg for at `olive-ai` conda-miljøet er aktivert:

```bash
conda activate olive-ai
```

Deretter kjører du følgende Olive-kommandoer i kommandolinjen.

1. **Undersøk dataene:** I dette eksempelet skal du finjustere Phi-3.5-Mini-modellen slik at den er spesialisert i å svare på reiserelaterte spørsmål. Koden nedenfor viser de første postene i datasettet, som er i JSON lines-format:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Kvantisér modellen:** Før du trener modellen, kvantiserer du den med følgende kommando som bruker en teknikk kalt Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. AWQ kvantiserer vektene i en modell ved å ta hensyn til aktiveringene produsert under inferens. Dette betyr at kvantiseringsprosessen tar hensyn til den faktiske datadistribusjonen i aktiveringene, noe som fører til bedre bevaring av modellens nøyaktighet sammenlignet med tradisjonelle kvantiseringsmetoder for vekter.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    Det tar **~8 minutter** å fullføre AWQ-kvantiseringen, som vil **redusere modellstørrelsen fra ~7,5 GB til ~2,5 GB**.
   
   I denne laben viser vi hvordan du kan bruke modeller fra Hugging Face (for eksempel: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune`-kommandoen finjusterer den kvantiserte modellen. Kvantisering av modellen *før* finjustering i stedet for etterpå gir bedre nøyaktighet siden finjusteringsprosessen gjenoppretter noe av tapet fra kvantiseringen.
    
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
    
    Det tar **~6 minutter** å fullføre finjusteringen (med 100 steg).

1. **Optimaliser:** Når modellen er trent, optimaliserer du modellen ved å bruke Olives `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider`-argumenter - men for denne laben bruker vi CPU.

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
    
    Det tar **~5 minutter** å fullføre optimaliseringen.

### Steg 5: Rask test av modellens inferens

For å teste inferens av modellen, opprett en Python-fil i mappen din kalt **app.py** og kopier inn følgende kode:

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

Kjør koden ved å bruke:

```bash
python app.py
```

### Steg 6: Last opp modell til Azure AI

Ved å laste opp modellen til et Azure AI-modellregister, kan modellen deles med andre medlemmer av utviklingsteamet ditt og håndtere versjonskontroll av modellen. For å laste opp modellen, kjør følgende kommando:

> [!NOTE]
> Oppdater `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"` og Azure AI-prosjektnavn, og kjør følgende kommando 

```
az ml workspace show
```

Eller ved å gå til +++ai.azure.com+++ og velge **management center**, **project**, **overview**.

Oppdater `{}`-plassholderne med navnet på ressursgruppen og Azure AI-prosjektnavnet ditt.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
Du kan deretter se den opplastede modellen din og distribuere den på https://ml.azure.com/model/list

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi streber etter nøyaktighet, vennligst vær oppmerksom på at automatiske oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.