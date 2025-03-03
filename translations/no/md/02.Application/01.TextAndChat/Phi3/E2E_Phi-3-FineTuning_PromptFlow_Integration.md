# Finjuster og integrer tilpassede Phi-3-modeller med Prompt Flow

Denne ende-til-ende (E2E) eksempelveiledningen er basert på artikkelen "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" fra Microsoft Tech Community. Den introduserer prosessene for finjustering, utrulling og integrering av tilpassede Phi-3-modeller med Prompt Flow.

## Oversikt

I dette E2E-eksemplet vil du lære hvordan du finjusterer Phi-3-modellen og integrerer den med Prompt Flow. Ved å bruke Azure Machine Learning og Prompt Flow vil du etablere en arbeidsflyt for å utrulle og bruke tilpassede AI-modeller. Dette E2E-eksemplet er delt inn i tre scenarier:

**Scenario 1: Konfigurer Azure-ressurser og forbered deg på finjustering**

**Scenario 2: Finjuster Phi-3-modellen og utrull i Azure Machine Learning Studio**

**Scenario 3: Integrer med Prompt Flow og chat med din tilpassede modell**

Her er en oversikt over dette E2E-eksemplet.

![Phi-3-FineTuning_PromptFlow_Integration Oversikt](../../../../../../translated_images/00-01-architecture.dfeb1f15c7d3c8989fb267a05ac83a25485a7230bde037df9d3d92336afc1993.no.png)

### Innholdsfortegnelse

1. **[Scenario 1: Konfigurer Azure-ressurser og forbered deg på finjustering](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Opprett et Azure Machine Learning-arbeidsområde](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Be om GPU-kvoter i Azure-abonnement](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Legg til rolletilordning](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Sett opp prosjekt](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Forbered datasett for finjustering](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 2: Finjuster Phi-3-modellen og utrull i Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Konfigurer Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Finjuster Phi-3-modellen](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Utrull den finjusterte modellen](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 3: Integrer med Prompt Flow og chat med din tilpassede modell](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrer den tilpassede Phi-3-modellen med Prompt Flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Chat med din tilpassede modell](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenario 1: Konfigurer Azure-ressurser og forbered deg på finjustering

### Opprett et Azure Machine Learning-arbeidsområde

1. Skriv *azure machine learning* i **søkelinjen** øverst på portalen og velg **Azure Machine Learning** fra alternativene som vises.

    ![Skriv azure machine learning](../../../../../../translated_images/01-01-type-azml.321cff72d18a51c06dee2db7463868f3ca6619559a5d68b7795d70f4a8b3a683.no.png)

1. Velg **+ Opprett** fra navigasjonsmenyen.

1. Velg **Nytt arbeidsområde** fra navigasjonsmenyen.

    ![Velg nytt arbeidsområde](../../../../../../translated_images/01-02-select-new-workspace.9bd9208488fcf38226fc8d3cefffecb2cb14f414f6d8d982492c1bde8634e24a.no.png)

1. Utfør følgende oppgaver:

    - Velg ditt Azure-**abonnement**.
    - Velg **ressursgruppen** som skal brukes (opprett en ny om nødvendig).
    - Skriv inn **arbeidsområdenavn**. Det må være unikt.
    - Velg **regionen** du ønsker å bruke.
    - Velg **lagringskontoen** som skal brukes (opprett en ny om nødvendig).
    - Velg **nøkkelhvelvet** som skal brukes (opprett en ny om nødvendig).
    - Velg **Application Insights** som skal brukes (opprett en ny om nødvendig).
    - Velg **Container Registry** som skal brukes (opprett en ny om nødvendig).

    ![Fyll ut AZML.](../../../../../../translated_images/01-03-fill-AZML.b2ebbef59952cd17d16b1f82adc252bf7616f8638d451e3c6595ffefe44f2cfa.no.png)

1. Velg **Gjennomgå + Opprett**.

1. Velg **Opprett**.

### Be om GPU-kvoter i Azure-abonnement

I dette E2E-eksemplet vil du bruke *Standard_NC24ads_A100_v4 GPU* til finjustering, som krever en kvoteforespørsel, og *Standard_E4s_v3* CPU til utrulling, som ikke krever en kvoteforespørsel.

> [!NOTE]
>
> Bare Pay-As-You-Go-abonnementer (standardabonnementstype) er kvalifisert for GPU-allokering; fordelsabonnementer støttes foreløpig ikke.
>
> For de som bruker fordelsabonnementer (som Visual Studio Enterprise-abonnement) eller de som ønsker å raskt teste finjusterings- og utrullingsprosessen, gir denne veiledningen også instruksjoner for finjustering med et minimalt datasett ved bruk av en CPU. Det er imidlertid viktig å merke seg at resultatene fra finjustering er betydelig bedre når du bruker en GPU med større datasett.

1. Besøk [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Utfør følgende oppgaver for å be om *Standard NCADSA100v4 Family*-kvote:

    - Velg **Kvote** fra venstremenyen.
    - Velg **Virtuell maskinfamilie** som skal brukes. For eksempel, velg **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, som inkluderer *Standard_NC24ads_A100_v4* GPU.
    - Velg **Be om kvote** fra navigasjonsmenyen.

        ![Be om kvote.](../../../../../../translated_images/01-04-request-quota.ddf063c7cda9799b8ef6fbde6c3c796201578fe9078feb1c624ed75c7705ad18.no.png)

    - På kvoteforespørselssiden, skriv inn **ny grense for kjerner** du ønsker å bruke. For eksempel, 24.
    - På kvoteforespørselssiden, velg **Send inn** for å be om GPU-kvoten.

> [!NOTE]
> Du kan velge riktig GPU eller CPU for dine behov ved å referere til dokumentet [Størrelser for virtuelle maskiner i Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist).

### Legg til rolletilordning

For å finjustere og utrulle modellene dine, må du først opprette en Brukerdefinert Administrert Identitet (UAI) og tilordne den riktige tillatelser. Denne UAI-en vil bli brukt til autentisering under utrulling.

#### Opprett Brukerdefinert Administrert Identitet (UAI)

1. Skriv *managed identities* i **søkelinjen** øverst på portalen og velg **Administrerte identiteter** fra alternativene som vises.

    ![Skriv administrerte identiteter.](../../../../../../translated_images/01-05-type-managed-identities.8bf5dc5a4fa3e852f897ec1a983e506c2bc7b7113d159598bf0adeb66d20a5c4.no.png)

1. Velg **+ Opprett**.

    ![Velg opprett.](../../../../../../translated_images/01-06-select-create.025632b7b54fe323f7d38edabbae05dd23f4665d0731f7143719c27c32e7e84f.no.png)

1. Utfør følgende oppgaver:

    - Velg ditt Azure-**abonnement**.
    - Velg **ressursgruppen** som skal brukes (opprett en ny om nødvendig).
    - Velg **regionen** du ønsker å bruke.
    - Skriv inn **navnet**. Det må være unikt.

1. Velg **Gjennomgå + opprett**.

1. Velg **+ Opprett**.

#### Legg til Contributor-rolletilordning til administrert identitet

1. Gå til ressursen for den administrerte identiteten du opprettet.

1. Velg **Azure-rolletilordninger** fra venstremenyen.

1. Velg **+ Legg til rolletilordning** fra navigasjonsmenyen.

1. På siden for å legge til rolletilordning, utfør følgende oppgaver:
    - Velg **Omfang** til **Ressursgruppe**.
    - Velg ditt Azure-**abonnement**.
    - Velg **ressursgruppen** som skal brukes.
    - Velg **Rolle** til **Contributor**.

    ![Fyll ut Contributor-rolle.](../../../../../../translated_images/01-07-fill-contributor-role.8936866326c7cdc3b876f14657e03422cca9dbff8b193dd541a693ce34407b26.no.png)

1. Velg **Lagre**.

#### Legg til Storage Blob Data Reader-rolletilordning til administrert identitet

1. Skriv *storage accounts* i **søkelinjen** øverst på portalen og velg **Lagringskontoer** fra alternativene som vises.

    ![Skriv lagringskontoer.](../../../../../../translated_images/01-08-type-storage-accounts.83554a27ff3edb5099ee3fbf7f467b843dabcc0e0e5fbb829a341eab3469ffa5.no.png)

1. Velg lagringskontoen som er tilknyttet Azure Machine Learning-arbeidsområdet du opprettet. For eksempel, *finetunephistorage*.

1. Utfør følgende oppgaver for å navigere til siden for å legge til rolletilordning:

    - Gå til Azure Storage-kontoen du opprettet.
    - Velg **Tilgangskontroll (IAM)** fra venstremenyen.
    - Velg **+ Legg til** fra navigasjonsmenyen.
    - Velg **Legg til rolletilordning** fra navigasjonsmenyen.

    ![Legg til rolle.](../../../../../../translated_images/01-09-add-role.4fef55886792c7e860da4c5a808044e6f7067fb5694f3ed4819a5758c6cc574e.no.png)

1. På siden for å legge til rolletilordning, utfør følgende oppgaver:

    - På rollen-siden, skriv *Storage Blob Data Reader* i **søkelinjen** og velg **Storage Blob Data Reader** fra alternativene som vises.
    - På rollen-siden, velg **Neste**.
    - På medlemssiden, velg **Tilordne tilgang til** **Administrert identitet**.
    - På medlemssiden, velg **+ Velg medlemmer**.
    - På siden for å velge administrerte identiteter, velg ditt Azure-**abonnement**.
    - På siden for å velge administrerte identiteter, velg **Administrert identitet** til **Administrert identitet**.
    - På siden for å velge administrerte identiteter, velg den administrerte identiteten du opprettet. For eksempel, *finetunephi-managedidentity*.
    - På siden for å velge administrerte identiteter, velg **Velg**.

    ![Velg administrert identitet.](../../../../../../translated_images/01-10-select-managed-identity.fffa802e4e6ce2de4fe50e64d37d3f2ef268c2ee16f30ec6f92bd1829b5f19c1.no.png)

1. Velg **Gjennomgå + tilordne**.

#### Legg til AcrPull-rolletilordning til administrert identitet

1. Skriv *container registries* i **søkelinjen** øverst på portalen og velg **Container registries** fra alternativene som vises.

    ![Skriv container registries.](../../../../../../translated_images/01-11-type-container-registries.62e58403d73d16a0cc715571c8a7b4105a0e97b1422aa5f26106aff1c0e8a47d.no.png)

1. Velg containerregisteret som er tilknyttet Azure Machine Learning-arbeidsområdet. For eksempel, *finetunephicontainerregistries*.

1. Utfør følgende oppgaver for å navigere til siden for å legge til rolletilordning:

    - Velg **Tilgangskontroll (IAM)** fra venstremenyen.
    - Velg **+ Legg til** fra navigasjonsmenyen.
    - Velg **Legg til rolletilordning** fra navigasjonsmenyen.

1. På siden for å legge til rolletilordning, utfør følgende oppgaver:

    - På rollen-siden, skriv *AcrPull* i **søkelinjen** og velg **AcrPull** fra alternativene som vises.
    - På rollen-siden, velg **Neste**.
    - På medlemssiden, velg **Tilordne tilgang til** **Administrert identitet**.
    - På medlemssiden, velg **+ Velg medlemmer**.
    - På siden for å velge administrerte identiteter, velg ditt Azure-**abonnement**.
    - På siden for å velge administrerte identiteter, velg **Administrert identitet** til **Administrert identitet**.
    - På siden for å velge administrerte identiteter, velg den administrerte identiteten du opprettet. For eksempel, *finetunephi-managedidentity*.
    - På siden for å velge administrerte identiteter, velg **Velg**.
    - Velg **Gjennomgå + tilordne**.

### Sett opp prosjekt

Nå skal du opprette en mappe for prosjektet og sette opp et virtuelt miljø for å utvikle et program som samhandler med brukere og bruker lagret chatthistorikk fra Azure Cosmos DB for å forbedre svarene.

#### Opprett en mappe for prosjektet

1. Åpne et terminalvindu og skriv følgende kommando for å opprette en mappe kalt *finetune-phi* i standardbanen.

    ```console
    mkdir finetune-phi
    ```

1. Skriv følgende kommando i terminalen for å navigere til *finetune-phi*-mappen du opprettet.

    ```console
    cd finetune-phi
    ```

#### Opprett et virtuelt miljø

1. Skriv følgende kommando i terminalen for å opprette et virtuelt miljø kalt *.venv*.

    ```console
    python -m venv .venv
    ```

1. Skriv følgende kommando i terminalen for å aktivere det virtuelle miljøet.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> Hvis det fungerer, skal du se *(.venv)* før kommandoprompten.

#### Installer nødvendige pakker

1. Skriv følgende kommandoer i terminalen for å installere de nødvendige pakkene.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Opprett prosjektfiler

I denne øvelsen skal du opprette de essensielle filene for prosjektet. Disse filene inkluderer skript for nedlasting av datasett, oppsett av Azure Machine Learning-miljøet, finjustering av Phi-3-modellen og utrulling av den finjusterte modellen. Du skal også opprette en *conda.yml*-fil for å sette opp finjusteringsmiljøet.

I denne øvelsen skal du:

- Opprette en *download_dataset.py*-fil for å laste ned datasettet.
- Opprette en *setup_ml.py*-fil for å sette opp Azure Machine Learning-miljøet.
- Opprette en *fine_tune.py*-fil i *finetuning_dir*-mappen for å finjustere Phi-3-modellen ved hjelp av datasettet.
- Opprette en *conda.yml*-fil for å sette opp finjusteringsmiljøet.
- Opprette en *deploy_model.py*-fil for å utrulle den finjusterte modellen.
- Opprette en *integrate_with_promptflow.py*-fil for å integrere den finjusterte modellen og kjøre modellen ved hjelp av Prompt Flow.
- Opprette en *flow.dag.yml*-fil for å sette opp arbeidsflytstrukturen for Prompt Flow.
- Opprette en *config.py*-fil for å legge inn Azure-informasjon.

> [!NOTE]
>
> Komplett mappestruktur:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        ├── finetuning_dir
> .        │      └── fine_tune.py
> .        ├── conda.yml
> .        ├── config.py
> .        ├── deploy_model.py
> .        ├── download_dataset.py
> .        ├── flow.dag.yml
> .        ├── integrate_with_promptflow.py
> .        └── setup_ml.py
> ```

1. Åpne **Visual Studio Code**.

1. Velg **Fil** fra menylinjen.

1. Velg **Åpne mappe**.

1. Velg *finetune-phi*-mappen du opprettet, som ligger på *C:\Users\yourUserName\finetune-phi*.

    ![Åpne prosjektmappe.](../../../../../../translated_images/01-12-open-project-folder.1f7f0f79e5d4d62e546e906e1ce5a480cd98d06062ce292b7b99c6cfcd434fdf.no.png)

1. I venstre panel i Visual Studio Code, høyreklikk og velg **Ny fil** for å opprette en ny fil kalt *download_dataset.py*.

1. I venstre panel i Visual Studio Code, høyreklikk og velg **Ny fil** for å opprette en ny fil kalt *setup_ml.py*.

1. I venstre panel i Visual Studio Code, høyreklikk og velg **Ny fil** for å opprette en ny fil kalt *deploy_model.py*.

    ![Opprett ny fil.](../../../../../../translated_images/01-13-create-new-file.40698c2e0415929e7b6dc2b30925677e413f965bac4134d3aefa0b44d443deaf.no.png)

1. I venstre panel i Visual Studio Code, høyreklikk og velg **Ny mappe** for å opprette en ny mappe kalt *finetuning_dir*.

1. I *finetuning_dir*-mappen, opprett en ny fil kalt *fine_tune.py*.

#### Opprett og konfigurer *conda.yml*-fil

1. I venstre panel i Visual Studio Code, høyreklikk og velg **Ny fil** for å opprette en ny fil kalt *conda.yml*.

1. Legg til følgende kode i *conda.yml*-filen for å sette opp finjusteringsmiljøet for Phi-3-modellen.

    ```yml
    name: phi-3-training-env
    channels:
      - defaults
      - conda-forge
    dependencies:
      - python=3.10
      - pip
      - numpy<2.0
      - pip:
          - torch==2.4.0
          - torchvision==0.19.0
          - trl==0.8.6
          - transformers==4.41
          - datasets==2.21.0
          - azureml-core==1.57.0
          - azure-storage-blob==12.19.0
          - azure-ai-ml==1.16
          - azure-identity==1.17.1
          - accelerate==0.33.0
          - mlflow==2.15.1
          - azureml-mlflow==1.57.0
    ```

#### Opprett og konfigurer *config.py*-fil

1. I venstre panel i Visual Studio Code, høyreklikk og velg **Ny fil** for å opprette en ny fil kalt *config.py*.

1. Legg til følgende kode i *config.py*-filen for å inkludere
![Finn abonnement-ID.](../../../../../../translated_images/01-14-find-subscriptionid.4daef33360f6d3808a9f1acea2b6b6121c498c75c36cb6ecc6c6b211f0d3b725.no.png)

1. Utfør følgende oppgaver for å legge til Azure Workspace Name:

    - Gå til Azure Machine Learning-ressursen du opprettet.
    - Kopier og lim inn kontonavnet ditt i *config.py*-filen.

    ![Finn Azure Machine Learning-navn.](../../../../../../translated_images/01-15-find-AZML-name.c8efdc5a8f2e594260004695c145fafb4fd903e96715f495a43733560cd706b5.no.png)

1. Utfør følgende oppgaver for å legge til Azure Resource Group Name:

    - Gå til Azure Machine Learning-ressursen du opprettet.
    - Kopier og lim inn Azure Resource Group Name i *config.py*-filen.

    ![Finn ressursgruppenavn.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.0647be51d3f1b8183995949df5866455e5532ef1c3d1f93b33dc9a91d615e882.no.png)

2. Utfør følgende oppgaver for å legge til Azure Managed Identity-navn:

    - Gå til Managed Identities-ressursen du opprettet.
    - Kopier og lim inn Azure Managed Identity-navnet i *config.py*-filen.

    ![Finn UAI.](../../../../../../translated_images/01-17-find-uai.b0fe7164cacc93b03c3c534daee68da244de6de4e6dcbc2a4e9df43403eb0f1b.no.png)

### Forbered datasett for finjustering

I denne øvelsen skal du kjøre *download_dataset.py*-filen for å laste ned *ULTRACHAT_200k*-datasettene til ditt lokale miljø. Deretter bruker du disse datasettene for å finjustere Phi-3-modellen i Azure Machine Learning.

#### Last ned datasettet ved hjelp av *download_dataset.py*

1. Åpne *download_dataset.py*-filen i Visual Studio Code.

1. Legg til følgende kode i *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset
    from config import (
        TRAIN_DATA_PATH,
        TEST_DATA_PATH)

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Load the dataset with the specified name, configuration, and split ratio
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Split the dataset into train and test sets (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Open the file in write mode
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterate over each record in the dataset
            for record in dataset:
                # Dump the record as a JSON object and write it to the file
                json.dump(record, f)
                # Write a newline character to separate records
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Load and split the ULTRACHAT_200k dataset with a specific configuration and split ratio
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extract the train and test datasets from the split
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Save the train dataset to a JSONL file
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **Veiledning for finjustering med et minimalt datasett ved bruk av CPU**
>
> Hvis du ønsker å bruke en CPU for finjustering, er denne tilnærmingen ideell for de med fordelsabonnementer (som Visual Studio Enterprise Subscription) eller for raskt å teste finjusterings- og distribusjonsprosessen.
>
> Erstatt `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` with `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Skriv inn følgende kommando i terminalen for å kjøre skriptet og laste ned datasettet til ditt lokale miljø.

    ```console
    python download_data.py
    ```

1. Verifiser at datasettene ble lagret i den lokale *finetune-phi/data*-mappen.

> [!NOTE]
>
> **Datasettstørrelse og finjusteringstid**
>
> I dette E2E-eksemplet bruker du kun 1 % av datasettet (`train_sft[:1%]`). Dette reduserer datamengden betydelig, noe som gjør opplastings- og finjusteringsprosessen raskere. Du kan justere prosentandelen for å finne den rette balansen mellom treningstid og modellens ytelse. Å bruke en mindre del av datasettet reduserer tiden som kreves for finjustering, noe som gjør prosessen mer håndterbar for et E2E-eksempel.

## Scenario 2: Finjuster Phi-3-modellen og distribuer i Azure Machine Learning Studio

### Konfigurer Azure CLI

Du må konfigurere Azure CLI for å autentisere miljøet ditt. Azure CLI lar deg administrere Azure-ressurser direkte fra kommandolinjen og gir de nødvendige legitimasjonene for at Azure Machine Learning skal få tilgang til disse ressursene. For å komme i gang, installer [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli).

1. Åpne et terminalvindu og skriv inn følgende kommando for å logge på Azure-kontoen din.

    ```console
    az login
    ```

1. Velg Azure-kontoen du vil bruke.

1. Velg Azure-abonnementet du vil bruke.

    ![Finn ressursgruppenavn.](../../../../../../translated_images/02-01-login-using-azure-cli.b6e8fb6255e8d09673cb48eca2b12aebbb84dfb8817af8a6b1dfd4bb2759d68f.no.png)

> [!TIP]
>
> Hvis du har problemer med å logge inn på Azure, kan du prøve å bruke en enhetskode. Åpne et terminalvindu og skriv inn følgende kommando for å logge inn på Azure-kontoen din:
>
> ```console
> az login --use-device-code
> ```
>

### Finjuster Phi-3-modellen

I denne øvelsen skal du finjustere Phi-3-modellen ved hjelp av det oppgitte datasettet. Først definerer du finjusteringsprosessen i *fine_tune.py*-filen. Deretter konfigurerer du Azure Machine Learning-miljøet og starter finjusteringsprosessen ved å kjøre *setup_ml.py*-filen. Dette skriptet sikrer at finjusteringen skjer innenfor Azure Machine Learning-miljøet.

Ved å kjøre *setup_ml.py* vil du starte finjusteringsprosessen i Azure Machine Learning-miljøet.

#### Legg til kode i *fine_tune.py*-filen

1. Naviger til *finetuning_dir*-mappen og åpne *fine_tune.py*-filen i Visual Studio Code.

1. Legg til følgende kode i *fine_tune.py*.

    ```python
    import argparse
    import sys
    import logging
    import os
    from datasets import load_dataset
    import torch
    import mlflow
    from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
    from trl import SFTTrainer

    # To avoid the INVALID_PARAMETER_VALUE error in MLflow, disable MLflow integration
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
        level=logging.WARNING
    )
    logger = logging.getLogger(__name__)

    def initialize_model_and_tokenizer(model_name, model_kwargs):
        """
        Initialize the model and tokenizer with the given pretrained model name and arguments.
        """
        model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.model_max_length = 2048
        tokenizer.pad_token = tokenizer.unk_token
        tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids(tokenizer.pad_token)
        tokenizer.padding_side = 'right'
        return model, tokenizer

    def apply_chat_template(example, tokenizer):
        """
        Apply a chat template to tokenize messages in the example.
        """
        messages = example["messages"]
        if messages[0]["role"] != "system":
            messages.insert(0, {"role": "system", "content": ""})
        example["text"] = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=False
        )
        return example

    def load_and_preprocess_data(train_filepath, test_filepath, tokenizer):
        """
        Load and preprocess the dataset.
        """
        train_dataset = load_dataset('json', data_files=train_filepath, split='train')
        test_dataset = load_dataset('json', data_files=test_filepath, split='train')
        column_names = list(train_dataset.features)

        train_dataset = train_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to train dataset",
        )

        test_dataset = test_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to test dataset",
        )

        return train_dataset, test_dataset

    def train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, output_dir):
        """
        Train and evaluate the model.
        """
        training_args = TrainingArguments(
            bf16=True,
            do_eval=True,
            output_dir=output_dir,
            eval_strategy="epoch",
            learning_rate=5.0e-06,
            logging_steps=20,
            lr_scheduler_type="cosine",
            num_train_epochs=3,
            overwrite_output_dir=True,
            per_device_eval_batch_size=4,
            per_device_train_batch_size=4,
            remove_unused_columns=True,
            save_steps=500,
            seed=0,
            gradient_checkpointing=True,
            gradient_accumulation_steps=1,
            warmup_ratio=0.2,
        )

        trainer = SFTTrainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=test_dataset,
            max_seq_length=2048,
            dataset_text_field="text",
            tokenizer=tokenizer,
            packing=True
        )

        train_result = trainer.train()
        trainer.log_metrics("train", train_result.metrics)

        mlflow.transformers.log_model(
            transformers_model={"model": trainer.model, "tokenizer": tokenizer},
            artifact_path=output_dir,
        )

        tokenizer.padding_side = 'left'
        eval_metrics = trainer.evaluate()
        eval_metrics["eval_samples"] = len(test_dataset)
        trainer.log_metrics("eval", eval_metrics)

    def main(train_file, eval_file, model_output_dir):
        """
        Main function to fine-tune the model.
        """
        model_kwargs = {
            "use_cache": False,
            "trust_remote_code": True,
            "torch_dtype": torch.bfloat16,
            "device_map": None,
            "attn_implementation": "eager"
        }

        # pretrained_model_name = "microsoft/Phi-3-mini-4k-instruct"
        pretrained_model_name = "microsoft/Phi-3.5-mini-instruct"

        with mlflow.start_run():
            model, tokenizer = initialize_model_and_tokenizer(pretrained_model_name, model_kwargs)
            train_dataset, test_dataset = load_and_preprocess_data(train_file, eval_file, tokenizer)
            train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, model_output_dir)

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--train-file", type=str, required=True, help="Path to the training data")
        parser.add_argument("--eval-file", type=str, required=True, help="Path to the evaluation data")
        parser.add_argument("--model_output_dir", type=str, required=True, help="Directory to save the fine-tuned model")
        args = parser.parse_args()
        main(args.train_file, args.eval_file, args.model_output_dir)

    ```

1. Lagre og lukk *fine_tune.py*-filen.

> [!TIP]
> **Du kan finjustere Phi-3.5-modellen**
>
> I *fine_tune.py*-filen kan du endre feltet `pretrained_model_name` from `"microsoft/Phi-3-mini-4k-instruct"` to any model you want to fine-tune. For example, if you change it to `"microsoft/Phi-3.5-mini-instruct"`, you'll be using the Phi-3.5-mini-instruct model for fine-tuning. To find and use the model name you prefer, visit [Hugging Face](https://huggingface.co/), search for the model you're interested in, and then copy and paste its name into the `pretrained_model_name` i skriptet ditt.
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Finjuster Phi-3.5.":::
>

#### Legg til kode i *setup_ml.py*-filen

1. Åpne *setup_ml.py*-filen i Visual Studio Code.

1. Legg til følgende kode i *setup_ml.py*.

    ```python
    import logging
    from azure.ai.ml import MLClient, command, Input
    from azure.ai.ml.entities import Environment, AmlCompute
    from azure.identity import AzureCliCredential
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        TRAIN_DATA_PATH,
        TEST_DATA_PATH
    )

    # Constants

    # Uncomment the following lines to use a CPU instance for training
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    FINETUNING_DIR = "./finetuning_dir" # Path to the fine-tuning script
    TRAINING_ENV_NAME = "phi-3-training-environment" # Name of the training environment
    MODEL_OUTPUT_DIR = "./model_output" # Path to the model output directory in azure ml

    # Logging setup to track the process
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.WARNING
    )

    def get_ml_client():
        """
        Initialize the ML Client using Azure CLI credentials.
        """
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def create_or_get_environment(ml_client):
        """
        Create or update the training environment in Azure ML.
        """
        env = Environment(
            image=DOCKER_IMAGE_NAME,  # Docker image for the environment
            conda_file=CONDA_FILE,  # Conda environment file
            name=TRAINING_ENV_NAME,  # Name of the environment
        )
        return ml_client.environments.create_or_update(env)

    def create_or_get_compute_cluster(ml_client, compute_name, COMPUTE_INSTANCE_TYPE, location):
        """
        Create or update the compute cluster in Azure ML.
        """
        try:
            compute_cluster = ml_client.compute.get(compute_name)
            logger.info(f"Compute cluster '{compute_name}' already exists. Reusing it for the current run.")
        except Exception:
            logger.info(f"Compute cluster '{compute_name}' does not exist. Creating a new one with size {COMPUTE_INSTANCE_TYPE}.")
            compute_cluster = AmlCompute(
                name=compute_name,
                size=COMPUTE_INSTANCE_TYPE,
                location=location,
                tier="Dedicated",  # Tier of the compute cluster
                min_instances=0,  # Minimum number of instances
                max_instances=1  # Maximum number of instances
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Wait for the cluster to be created
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # Path to fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Training environment
            compute=compute_name,  # Compute cluster to use
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Path to the training data file
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Path to the evaluation data file
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # Initialize ML Client
        ml_client = get_ml_client()

        # Create Environment
        env = create_or_get_environment(ml_client)
        
        # Create or get existing compute cluster
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Create and Submit Fine-Tuning Job
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Submit the job
        ml_client.jobs.stream(returned_job.name)  # Stream the job logs
        
        # Capture the job name
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. Erstatt `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `LOCATION` med dine spesifikke detaljer.

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **Veiledning for finjustering med et minimalt datasett ved bruk av CPU**
>
> Hvis du ønsker å bruke en CPU for finjustering, er denne tilnærmingen ideell for de med fordelsabonnementer (som Visual Studio Enterprise Subscription) eller for raskt å teste finjusterings- og distribusjonsprosessen.
>
> 1. Åpne *setup_ml*-filen.
> 1. Erstatt `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `DOCKER_IMAGE_NAME` with the following. If you do not have access to *Standard_E16s_v3*, you can use an equivalent CPU instance or request a new quota.
> 1. Replace `LOCATION` med dine spesifikke detaljer.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. Skriv inn følgende kommando for å kjøre *setup_ml.py*-skriptet og starte finjusteringsprosessen i Azure Machine Learning.

    ```python
    python setup_ml.py
    ```

1. I denne øvelsen har du finjustert Phi-3-modellen ved hjelp av Azure Machine Learning. Ved å kjøre *setup_ml.py*-skriptet har du konfigurert Azure Machine Learning-miljøet og startet finjusteringsprosessen definert i *fine_tune.py*-filen. Vær oppmerksom på at finjusteringsprosessen kan ta en betydelig mengde tid. Etter å ha kjørt `python setup_ml.py` command, you need to wait for the process to complete. You can monitor the status of the fine-tuning job by following the link provided in the terminal to the Azure Machine Learning portal.

    ![See finetuning job.](../../../../../../translated_images/02-02-see-finetuning-job.a28c8552f7b7bc088ccd67dd0c522f7fc1944048d3554bb1b24f95a1169ad538.no.png)

### Deploy the fine-tuned model

To integrate the fine-tuned Phi-3 model with Prompt Flow, you need to deploy the model to make it accessible for real-time inference. This process involves registering the model, creating an online endpoint, and deploying the model.

#### Set the model name, endpoint name, and deployment name for deployment

1. Open *config.py* file.

1. Replace `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` with the desired name for your model.

1. Replace `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` with the desired name for your endpoint.

1. Replace `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` med ønsket navn for distribusjonen din.

#### Legg til kode i *deploy_model.py*-filen

Å kjøre *deploy_model.py*-filen automatiserer hele distribusjonsprosessen. Den registrerer modellen, oppretter et endepunkt og utfører distribusjonen basert på innstillingene som er spesifisert i config.py-filen, som inkluderer modellnavn, endepunktnavn og distribusjonsnavn.

1. Åpne *deploy_model.py*-filen i Visual Studio Code.

1. Legg til følgende kode i *deploy_model.py*.

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # Configuration imports
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        AZURE_MANAGED_IDENTITY_RESOURCE_ID,
        AZURE_MANAGED_IDENTITY_CLIENT_ID,
        AZURE_MODEL_NAME,
        AZURE_ENDPOINT_NAME,
        AZURE_DEPLOYMENT_NAME
    )

    # Constants
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def get_ml_client():
        """Initialize and return the ML Client."""
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def register_model(ml_client, model_name, job_name):
        """Register a new model."""
        model_path = f"azureml://jobs/{job_name}/outputs/artifacts/paths/model_output"
        logger.info(f"Registering model {model_name} from job {job_name} at path {model_path}.")
        run_model = Model(
            path=model_path,
            name=model_name,
            description="Model created from run.",
            type=AssetTypes.MLFLOW_MODEL,
        )
        model = ml_client.models.create_or_update(run_model)
        logger.info(f"Registered model ID: {model.id}")
        return model

    def delete_existing_endpoint(ml_client, endpoint_name):
        """Delete existing endpoint if it exists."""
        try:
            endpoint_result = ml_client.online_endpoints.get(name=endpoint_name)
            logger.info(f"Deleting existing endpoint {endpoint_name}.")
            ml_client.online_endpoints.begin_delete(name=endpoint_name).result()
            logger.info(f"Deleted existing endpoint {endpoint_name}.")
        except Exception as e:
            logger.info(f"No existing endpoint {endpoint_name} found to delete: {e}")

    def create_or_update_endpoint(ml_client, endpoint_name, description=""):
        """Create or update an endpoint."""
        delete_existing_endpoint(ml_client, endpoint_name)
        logger.info(f"Creating new endpoint {endpoint_name}.")
        endpoint = ManagedOnlineEndpoint(
            name=endpoint_name,
            description=description,
            identity=IdentityConfiguration(
                type="user_assigned",
                user_assigned_identities=[ManagedIdentityConfiguration(resource_id=AZURE_MANAGED_IDENTITY_RESOURCE_ID)]
            )
        )
        endpoint_result = ml_client.online_endpoints.begin_create_or_update(endpoint).result()
        logger.info(f"Created new endpoint {endpoint_name}.")
        return endpoint_result

    def create_or_update_deployment(ml_client, endpoint_name, deployment_name, model):
        """Create or update a deployment."""

        logger.info(f"Creating deployment {deployment_name} for endpoint {endpoint_name}.")
        deployment = ManagedOnlineDeployment(
            name=deployment_name,
            endpoint_name=endpoint_name,
            model=model.id,
            instance_type=COMPUTE_INSTANCE_TYPE,
            instance_count=1,
            environment_variables=deployment_env_vars,
            request_settings=OnlineRequestSettings(
                max_concurrent_requests_per_instance=3,
                request_timeout_ms=180000,
                max_queue_wait_ms=120000
            ),
            liveness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
            readiness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
        )
        deployment_result = ml_client.online_deployments.begin_create_or_update(deployment).result()
        logger.info(f"Created deployment {deployment.name} for endpoint {endpoint_name}.")
        return deployment_result

    def set_traffic_to_deployment(ml_client, endpoint_name, deployment_name):
        """Set traffic to the specified deployment."""
        try:
            # Fetch the current endpoint details
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Log the current traffic allocation for debugging
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Set the traffic allocation for the deployment
            endpoint.traffic = {deployment_name: 100}
            
            # Update the endpoint with the new traffic allocation
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Log the updated traffic allocation for debugging
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Log any errors that occur during the process
            logger.error(f"Failed to set traffic to deployment: {e}")
            raise


    def main():
        ml_client = get_ml_client()

        registered_model = register_model(ml_client, AZURE_MODEL_NAME, JOB_NAME)
        logger.info(f"Registered model ID: {registered_model.id}")

        endpoint = create_or_update_endpoint(ml_client, AZURE_ENDPOINT_NAME, "Endpoint for finetuned Phi-3 model")
        logger.info(f"Endpoint {AZURE_ENDPOINT_NAME} is ready.")

        try:
            deployment = create_or_update_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME, registered_model)
            logger.info(f"Deployment {AZURE_DEPLOYMENT_NAME} is created for endpoint {AZURE_ENDPOINT_NAME}.")

            set_traffic_to_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME)
            logger.info(f"Traffic is set to deployment {AZURE_DEPLOYMENT_NAME} at endpoint {AZURE_ENDPOINT_NAME}.")
        except Exception as e:
            logger.error(f"Failed to create or update deployment: {e}")

    if __name__ == "__main__":
        main()

    ```

1. Utfør følgende oppgaver for å få `JOB_NAME`:

    - Navigate to Azure Machine Learning resource that you created.
    - Select **Studio web URL** to open the Azure Machine Learning workspace.
    - Select **Jobs** from the left side tab.
    - Select the experiment for fine-tuning. For example, *finetunephi*.
    - Select the job that you created.
    - Copy and paste your job Name into the `JOB_NAME = "your-job-name"` in *deploy_model.py* file.

1. Replace `COMPUTE_INSTANCE_TYPE` med dine spesifikke detaljer.

1. Skriv inn følgende kommando for å kjøre *deploy_model.py*-skriptet og starte distribusjonsprosessen i Azure Machine Learning.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> For å unngå ekstra kostnader på kontoen din, må du sørge for å slette det opprettede endepunktet i Azure Machine Learning-arbeidsområdet.
>

#### Sjekk distribusjonsstatus i Azure Machine Learning Workspace

1. Besøk [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Naviger til Azure Machine Learning-arbeidsområdet du opprettet.

1. Velg **Studio web URL** for å åpne Azure Machine Learning-arbeidsområdet.

1. Velg **Endpoints** fra venstre sidemeny.

    ![Velg endepunkter.](../../../../../../translated_images/02-03-select-endpoints.a32f4eb2854cd54ee997f9bec0e842c3084bbc24bd693457b5c6b132fe966bf4.no.png)

2. Velg endepunktet du opprettet.

    ![Velg endepunktet du opprettet.](../../../../../../translated_images/02-04-select-endpoint-created.048b4f0f6479c1885b62711a151227a24408679be65dd1039cd2f64448ec5842.no.png)

3. På denne siden kan du administrere endepunktene som ble opprettet under distribusjonsprosessen.

## Scenario 3: Integrer med Prompt flow og chat med din tilpassede modell

### Integrer den tilpassede Phi-3-modellen med Prompt flow

Etter å ha distribuert den finjusterte modellen din, kan du nå integrere den med Prompt flow for å bruke modellen din i sanntidsapplikasjoner, noe som muliggjør en rekke interaktive oppgaver med din tilpassede Phi-3-modell.

#### Sett API-nøkkel og endepunkt-URI for den finjusterte Phi-3-modellen

1. Naviger til Azure Machine Learning-arbeidsområdet du opprettet.
1. Velg **Endpoints** fra venstre sidemeny.
1. Velg endepunktet du opprettet.
1. Velg **Consume** fra navigasjonsmenyen.
1. Kopier og lim inn **REST endpoint** i *config.py*-filen, og erstatt `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` with your **REST endpoint**.
1. Copy and paste your **Primary key** into the *config.py* file, replacing `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` med **Primary key**.

    ![Kopier API-nøkkel og endepunkt-URI.](../../../../../../translated_images/02-05-copy-apikey-endpoint.602de7450770e9984149dc7da7472bacafbf0e8447e2adb53896ad93b1dc7684.no.png)

#### Legg til kode i *flow.dag.yml*-filen

1. Åpne *flow.dag.yml*-filen i Visual Studio Code.

1. Legg til følgende kode i *flow.dag.yml*.

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

#### Legg til kode i *integrate_with_promptflow.py*-filen

1. Åpne *integrate_with_promptflow.py*-filen i Visual Studio Code.

1. Legg til følgende kode i *integrate_with_promptflow.py*.

    ```python
    import logging
    import requests
    from promptflow.core import tool
    import asyncio
    import platform
    from config import (
        AZURE_ML_ENDPOINT,
        AZURE_ML_API_KEY
    )

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_azml_endpoint(input_data: list, endpoint_url: str, api_key: str) -> str:
        """
        Send a request to the Azure ML endpoint with the given input data.
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": [input_data],
            "params": {
                "temperature": 0.7,
                "max_new_tokens": 128,
                "do_sample": True,
                "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            result = response.json()[0]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    def setup_asyncio_policy():
        """
        Setup asyncio event loop policy for Windows.
        """
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            logger.info("Set Windows asyncio event loop policy.")

    @tool
    def my_python_tool(input_data: str) -> str:
        """
        Tool function to process input data and query the Azure ML endpoint.
        """
        setup_asyncio_policy()
        return query_azml_endpoint(input_data, AZURE_ML_ENDPOINT, AZURE_ML_API_KEY)

    ```

### Chat med din tilpassede modell

1. Skriv inn følgende kommando for å kjøre *deploy_model.py*-skriptet og starte distribusjonsprosessen i Azure Machine Learning.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Her er et eksempel på resultatene: Nå kan du chatte med din tilpassede Phi-3-modell. Det anbefales å stille spørsmål basert på dataene som ble brukt til finjusteringen.

    ![Prompt flow eksempel.](../../../../../../translated_images/02-06-promptflow-example.023c07a4be8f02199e04eaf49f40ba24415da1be2274cbda9a7aa39776acd0bb.no.png)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved bruk av maskinbaserte AI-oversettelsestjenester. Selv om vi tilstreber nøyaktighet, vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.