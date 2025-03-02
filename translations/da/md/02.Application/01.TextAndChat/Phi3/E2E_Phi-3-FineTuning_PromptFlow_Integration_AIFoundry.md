# Finjuster og integrer tilpassede Phi-3-modeller med Prompt Flow i Azure AI Foundry

Dette end-to-end (E2E) eksempel er baseret på guiden "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" fra Microsoft Tech Community. Det introducerer processerne for finjustering, udrulning og integration af tilpassede Phi-3-modeller med Prompt Flow i Azure AI Foundry.  
I modsætning til E2E-eksemplet, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", som involverede lokal kørsel af kode, fokuserer denne vejledning udelukkende på finjustering og integration af din model inden for Azure AI / ML Studio.

## Oversigt

I dette E2E-eksempel lærer du, hvordan du finjusterer Phi-3-modellen og integrerer den med Prompt Flow i Azure AI Foundry. Ved at udnytte Azure AI / ML Studio vil du etablere en arbejdsgang til udrulning og brug af tilpassede AI-modeller. Dette E2E-eksempel er opdelt i tre scenarier:

**Scenario 1: Opsæt Azure-ressourcer og forbered dig på finjustering**

**Scenario 2: Finjuster Phi-3-modellen og udrul den i Azure Machine Learning Studio**

**Scenario 3: Integrer med Prompt Flow og chat med din tilpassede model i Azure AI Foundry**

Her er en oversigt over dette E2E-eksempel.

![Phi-3-FineTuning_PromptFlow_Integration Oversigt.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.da.png)

### Indholdsfortegnelse

1. **[Scenario 1: Opsæt Azure-ressourcer og forbered dig på finjustering](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Opret et Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Anmod om GPU-kvoter i Azure-abonnement](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Tilføj rollefordeling](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Opsæt projekt](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Forbered datasæt til finjustering](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 2: Finjuster Phi-3-modellen og udrul den i Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Finjuster Phi-3-modellen](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Udrul den finjusterede Phi-3-model](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 3: Integrer med Prompt Flow og chat med din tilpassede model i Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrer den tilpassede Phi-3-model med Prompt Flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Chat med din tilpassede Phi-3-model](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenario 1: Opsæt Azure-ressourcer og forbered dig på finjustering

### Opret et Azure Machine Learning Workspace

1. Skriv *azure machine learning* i **søgefeltet** øverst på portalens side, og vælg **Azure Machine Learning** fra de viste muligheder.

    ![Skriv azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.da.png)

2. Vælg **+ Opret** fra navigationsmenuen.

3. Vælg **Nyt arbejdsområde** fra navigationsmenuen.

    ![Vælg nyt arbejdsområde.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.da.png)

4. Udfør følgende opgaver:

    - Vælg dit Azure **Abonnement**.
    - Vælg den **Ressourcegruppe**, du vil bruge (opret en ny, hvis nødvendigt).
    - Indtast **Navn på arbejdsområde**. Det skal være en unik værdi.
    - Vælg den **Region**, du vil bruge.
    - Vælg den **Lagringskonto**, du vil bruge (opret en ny, hvis nødvendigt).
    - Vælg den **Nøglehvælving**, du vil bruge (opret en ny, hvis nødvendigt).
    - Vælg den **Applikationsindsigt**, du vil bruge (opret en ny, hvis nødvendigt).
    - Vælg det **Containerregister**, du vil bruge (opret en ny, hvis nødvendigt).

    ![Udfyld azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.da.png)

5. Vælg **Gennemse + Opret**.

6. Vælg **Opret**.

### Anmod om GPU-kvoter i Azure-abonnement

I denne vejledning lærer du, hvordan du finjusterer og udruller en Phi-3-model ved hjælp af GPU'er. Til finjustering vil du bruge GPU'en *Standard_NC24ads_A100_v4*, som kræver en kvoteanmodning. Til udrulning vil du bruge GPU'en *Standard_NC6s_v3*, som også kræver en kvoteanmodning.

> [!NOTE]
>
> Kun Pay-As-You-Go-abonnementer (standardtypen af abonnement) er berettiget til GPU-allokering; fordel-abonnementer understøttes i øjeblikket ikke.
>

1. Besøg [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Udfør følgende opgaver for at anmode om kvote for *Standard NCADSA100v4 Family*:

    - Vælg **Kvote** fra venstre sidetab.
    - Vælg den **Virtuelle maskinfamilie**, du vil bruge. For eksempel **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, som inkluderer GPU'en *Standard_NC24ads_A100_v4*.
    - Vælg **Anmod om kvote** fra navigationsmenuen.

        ![Anmod om kvote.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.da.png)

    - Inde på Anmod om kvote-siden skal du indtaste den **Nye kernegrænse**, du ønsker at bruge. For eksempel 24.
    - Inde på Anmod om kvote-siden skal du vælge **Indsend** for at anmode om GPU-kvoten.

1. Udfør følgende opgaver for at anmode om kvote for *Standard NCSv3 Family*:

    - Vælg **Kvote** fra venstre sidetab.
    - Vælg den **Virtuelle maskinfamilie**, du vil bruge. For eksempel **Standard NCSv3 Family Cluster Dedicated vCPUs**, som inkluderer GPU'en *Standard_NC6s_v3*.
    - Vælg **Anmod om kvote** fra navigationsmenuen.
    - Inde på Anmod om kvote-siden skal du indtaste den **Nye kernegrænse**, du ønsker at bruge. For eksempel 24.
    - Inde på Anmod om kvote-siden skal du vælge **Indsend** for at anmode om GPU-kvoten.

### Tilføj rollefordeling

For at finjustere og udrulle dine modeller skal du først oprette en User Assigned Managed Identity (UAI) og tildele den de relevante tilladelser. Denne UAI vil blive brugt til godkendelse under udrulning.

#### Opret User Assigned Managed Identity (UAI)

1. Skriv *managed identities* i **søgefeltet** øverst på portalens side, og vælg **Managed Identities** fra de viste muligheder.

    ![Skriv managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.da.png)

1. Vælg **+ Opret**.

    ![Vælg opret.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.da.png)

1. Udfør følgende opgaver:

    - Vælg dit Azure **Abonnement**.
    - Vælg den **Ressourcegruppe**, du vil bruge (opret en ny, hvis nødvendigt).
    - Vælg den **Region**, du vil bruge.
    - Indtast **Navn**. Det skal være en unik værdi.

    ![Udfyld managed identities.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.da.png)

1. Vælg **Gennemse + opret**.

1. Vælg **+ Opret**.

#### Tilføj Contributor-rolle til Managed Identity

1. Naviger til den Managed Identity-ressource, du har oprettet.

1. Vælg **Azure rollefordelinger** fra venstre sidetab.

1. Vælg **+ Tilføj rollefordeling** fra navigationsmenuen.

1. Inde på Tilføj rollefordeling-siden skal du udføre følgende opgaver:
    - Vælg **Omfang** til **Ressourcegruppe**.
    - Vælg dit Azure **Abonnement**.
    - Vælg den **Ressourcegruppe**, du vil bruge.
    - Vælg **Rolle** til **Bidragyder**.

    ![Udfyld bidragyderrolle.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.da.png)

2. Vælg **Gem**.

#### Tilføj Storage Blob Data Reader-rolle til Managed Identity

1. Skriv *storage accounts* i **søgefeltet** øverst på portalens side, og vælg **Storage accounts** fra de viste muligheder.

    ![Skriv storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.da.png)

1. Vælg den lagringskonto, der er knyttet til det Azure Machine Learning-arbejdsområde, du har oprettet. For eksempel *finetunephistorage*.

1. Udfør følgende opgaver for at navigere til Tilføj rollefordeling-siden:

    - Naviger til den Azure Storage-konto, du har oprettet.
    - Vælg **Adgangskontrol (IAM)** fra venstre sidetab.
    - Vælg **+ Tilføj** fra navigationsmenuen.
    - Vælg **Tilføj rollefordeling** fra navigationsmenuen.

    ![Tilføj rolle.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.da.png)

1. Inde på Tilføj rollefordeling-siden skal du udføre følgende opgaver:

    - Inde på Rolle-siden skal du skrive *Storage Blob Data Reader* i **søgefeltet** og vælge **Storage Blob Data Reader** fra de viste muligheder.
    - Inde på Rolle-siden skal du vælge **Næste**.
    - Inde på Medlemmer-siden skal du vælge **Tildel adgang til** **Managed identity**.
    - Inde på Medlemmer-siden skal du vælge **+ Vælg medlemmer**.
    - Inde på Vælg managed identities-siden skal du vælge dit Azure **Abonnement**.
    - Inde på Vælg managed identities-siden skal du vælge **Managed identity** til **Manage Identity**.
    - Inde på Vælg managed identities-siden skal du vælge den Managed Identity, du har oprettet. For eksempel *finetunephi-managedidentity*.
    - Inde på Vælg managed identities-siden skal du vælge **Vælg**.

    ![Vælg managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.da.png)

1. Vælg **Gennemse + tildel**.

#### Tilføj AcrPull-rolle til Managed Identity

1. Skriv *container registries* i **søgefeltet** øverst på portalens side, og vælg **Container registries** fra de viste muligheder.

    ![Skriv container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.da.png)

1. Vælg det containerregister, der er knyttet til Azure Machine Learning-arbejdsområdet. For eksempel *finetunephicontainerregistry*.

1. Udfør følgende opgaver for at navigere til Tilføj rollefordeling-siden:

    - Vælg **Adgangskontrol (IAM)** fra venstre sidetab.
    - Vælg **+ Tilføj** fra navigationsmenuen.
    - Vælg **Tilføj rollefordeling** fra navigationsmenuen.

1. Inde på Tilføj rollefordeling-siden skal du udføre følgende opgaver:

    - Inde på Rolle-siden skal du skrive *AcrPull* i **søgefeltet** og vælge **AcrPull** fra de viste muligheder.
    - Inde på Rolle-siden skal du vælge **Næste**.
    - Inde på Medlemmer-siden skal du vælge **Tildel adgang til** **Managed identity**.
    - Inde på Medlemmer-siden skal du vælge **+ Vælg medlemmer**.
    - Inde på Vælg managed identities-siden skal du vælge dit Azure **Abonnement**.
    - Inde på Vælg managed identities-siden skal du vælge **Managed identity** til **Manage Identity**.
    - Inde på Vælg managed identities-siden skal du vælge den Managed Identity, du har oprettet. For eksempel *finetunephi-managedidentity*.
    - Inde på Vælg managed identities-siden skal du vælge **Vælg**.
    - Vælg **Gennemse + tildel**.

### Opsæt projekt

For at downloade de datasæt, der er nødvendige for finjustering, skal du opsætte et lokalt miljø.

I denne øvelse vil du:

- Oprette en mappe til at arbejde i.
- Oprette et virtuelt miljø.
- Installere de nødvendige pakker.
- Oprette en *download_dataset.py*-fil til at downloade datasættet.

#### Opret en mappe til at arbejde i

1. Åbn et terminalvindue, og skriv følgende kommando for at oprette en mappe med navnet *finetune-phi* i standardstien.

    ```console
    mkdir finetune-phi
    ```

2. Skriv følgende kommando i terminalen for at navigere til *finetune-phi*-mappen, du oprettede.

    ```console
    cd finetune-phi
    ```

#### Opret et virtuelt miljø

1. Skriv følgende kommando i terminalen for at oprette et virtuelt miljø med navnet *.venv*.

    ```console
    python -m venv .venv
    ```

2. Skriv følgende kommando i terminalen for at aktivere det virtuelle miljø.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Hvis det virker, bør du se *(.venv)* foran kommandoprompten.

#### Installer de nødvendige pakker

1. Skriv følgende kommandoer i terminalen for at installere de nødvendige pakker.

    ```console
    pip install datasets==2.19.1
    ```

#### Opret `download_dataset.py`

> [!NOTE]
> Komplet mappestruktur:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Åbn **Visual Studio Code**.

1. Vælg **Fil** i menulinjen.

1. Vælg **Åbn mappe**.

1. Vælg *finetune-phi*-mappen, du oprettede, som er placeret på *C:\Users\ditBrugernavn\finetune-phi*.

    ![Vælg den mappe, du oprettede.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.da.png)

1. I venstre side af Visual Studio Code, højreklik og vælg **Ny fil** for at oprette en ny fil med navnet *download_dataset.py*.

    ![Opret en ny fil.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.da.png)

### Forbered datasæt til finjustering

I denne øvelse vil du køre *download_dataset.py*-filen for at downloade *ultrachat_200k*-datasættene til dit lokale miljø. Derefter vil du bruge disse datasæt til at finjustere Phi-3-modellen i Azure Machine Learning.

I denne øvelse vil du:

- Tilføje kode til *download_dataset.py*-filen for at downloade datasættene.
- Køre *download_dataset.py*-filen for at downloade datasættene til dit lokale miljø.

#### Download dit datasæt ved hjælp af *download_dataset.py*

1. Åbn *download_dataset.py*-filen i Visual Studio Code.

1. Tilføj følgende kode til *download_dataset.py*-filen.

    ```python
    import json
    import os
    from datasets import load_dataset

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
        save_dataset_to_jsonl(train_dataset, "data/train_data.jsonl")
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, "data/test_data.jsonl")

    if __name__ == "__main__":
        main()

    ```

1. Skriv følgende kommando i terminalen for at køre scriptet og downloade datasættet til dit lokale miljø.

    ```console
    python download_dataset.py
    ```

1. Bekræft, at datasættene blev gemt korrekt i din lokale *finetune-phi/data*-mappe.

> [!NOTE]
>
> #### Bemærkning om datasætsstørrelse og finjusteringstid
>
> I denne vejledning bruger du kun 1% af datasættet (`split='train[:1%]'`). Dette reducerer betydeligt mængden af data, hvilket gør upload- og finjusteringsprocesserne hurt
1. Besøg [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vælg **Compute** fra menuen til venstre.

1. Vælg **Compute clusters** fra navigationsmenuen.

1. Vælg **+ New**.

    ![Vælg compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.da.png)

1. Udfør følgende opgaver:

    - Vælg den **Region**, du vil bruge.
    - Sæt **Virtual machine tier** til **Dedicated**.
    - Sæt **Virtual machine type** til **GPU**.
    - Filtrer **Virtual machine size** til **Select from all options**.
    - Vælg **Virtual machine size** til **Standard_NC24ads_A100_v4**.

    ![Opret cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.da.png)

1. Vælg **Next**.

1. Udfør følgende opgaver:

    - Indtast **Compute name**. Det skal være en unik værdi.
    - Sæt **Minimum number of nodes** til **0**.
    - Sæt **Maximum number of nodes** til **1**.
    - Sæt **Idle seconds before scale down** til **120**.

    ![Opret cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.da.png)

1. Vælg **Create**.

#### Finjuster Phi-3-modellen

1. Besøg [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vælg den Azure Machine Learning-arbejdsplads, du har oprettet.

    ![Vælg arbejdsplads, du har oprettet.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.da.png)

1. Udfør følgende opgaver:

    - Vælg **Model catalog** fra menuen til venstre.
    - Skriv *phi-3-mini-4k* i **søgefeltet**, og vælg **Phi-3-mini-4k-instruct** fra de viste muligheder.

    ![Skriv phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.da.png)

1. Vælg **Fine-tune** fra navigationsmenuen.

    ![Vælg fine-tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.da.png)

1. Udfør følgende opgaver:

    - Sæt **Select task type** til **Chat completion**.
    - Vælg **+ Select data** for at uploade **Træningsdata**.
    - Sæt uploadtypen for valideringsdata til **Provide different validation data**.
    - Vælg **+ Select data** for at uploade **Valideringsdata**.

    ![Udfyld finjusteringsside.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.da.png)

    > [!TIP]
    >
    > Du kan vælge **Advanced settings** for at tilpasse konfigurationer som **learning_rate** og **lr_scheduler_type** for at optimere finjusteringsprocessen efter dine specifikke behov.

1. Vælg **Finish**.

1. I denne øvelse har du med succes finjusteret Phi-3-modellen ved hjælp af Azure Machine Learning. Bemærk, at finjusteringsprocessen kan tage en del tid. Efter at have kørt finjusteringsjobbet, skal du vente, indtil det er færdigt. Du kan overvåge status for finjusteringsjobbet ved at navigere til fanen Jobs i venstre side af din Azure Machine Learning-arbejdsplads. I den næste serie vil du implementere den finjusterede model og integrere den med Prompt flow.

    ![Se finjusteringsjob.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.da.png)

### Implementer den finjusterede Phi-3-model

For at integrere den finjusterede Phi-3-model med Prompt flow skal du implementere modellen, så den kan tilgås til realtidsforudsigelser. Denne proces indebærer registrering af modellen, oprettelse af en online endpoint og implementering af modellen.

I denne øvelse vil du:

- Registrere den finjusterede model i Azure Machine Learning-arbejdspladsen.
- Oprette en online endpoint.
- Implementere den registrerede finjusterede Phi-3-model.

#### Registrer den finjusterede model

1. Besøg [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vælg den Azure Machine Learning-arbejdsplads, du har oprettet.

    ![Vælg arbejdsplads, du har oprettet.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.da.png)

1. Vælg **Models** fra menuen til venstre.  
1. Vælg **+ Register**.  
1. Vælg **From a job output**.

    ![Registrer model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.da.png)

1. Vælg det job, du har oprettet.

    ![Vælg job.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.da.png)

1. Vælg **Next**.

1. Sæt **Model type** til **MLflow**.

1. Sørg for, at **Job output** er valgt; det bør automatisk være valgt.

    ![Vælg output.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.da.png)

2. Vælg **Next**.

3. Vælg **Register**.

    ![Vælg register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.da.png)

4. Du kan se din registrerede model ved at navigere til menuen **Models** fra venstre side.

    ![Registreret model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.da.png)

#### Implementer den finjusterede model

1. Gå til den Azure Machine Learning-arbejdsplads, du har oprettet.

1. Vælg **Endpoints** fra menuen til venstre.

1. Vælg **Real-time endpoints** fra navigationsmenuen.

    ![Opret endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.da.png)

1. Vælg **Create**.

1. Vælg den registrerede model, du har oprettet.

    ![Vælg registreret model.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.da.png)

1. Vælg **Select**.

1. Udfør følgende opgaver:

    - Sæt **Virtual machine** til *Standard_NC6s_v3*.
    - Vælg det **Instance count**, du ønsker at bruge. For eksempel *1*.
    - Sæt **Endpoint** til **New** for at oprette en ny endpoint.
    - Indtast **Endpoint name**. Det skal være en unik værdi.
    - Indtast **Deployment name**. Det skal være en unik værdi.

    ![Udfyld implementeringsindstillinger.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.da.png)

1. Vælg **Deploy**.

> [!WARNING]
> For at undgå yderligere omkostninger på din konto skal du sørge for at slette den oprettede endpoint i Azure Machine Learning-arbejdspladsen.
>

#### Kontroller implementeringsstatus i Azure Machine Learning Workspace

1. Naviger til den Azure Machine Learning-arbejdsplads, du har oprettet.

1. Vælg **Endpoints** fra menuen til venstre.

1. Vælg den endpoint, du har oprettet.

    ![Vælg endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.da.png)

1. På denne side kan du administrere endpoints under implementeringsprocessen.

> [!NOTE]
> Når implementeringen er færdig, skal du sikre dig, at **Live traffic** er sat til **100%**. Hvis det ikke er tilfældet, skal du vælge **Update traffic** for at justere trafikindstillingerne. Bemærk, at du ikke kan teste modellen, hvis trafikken er sat til 0%.
>
> ![Sæt trafik.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.da.png)
>

## Scenario 3: Integrer med Prompt flow og chat med din tilpassede model i Azure AI Foundry

### Integrer den tilpassede Phi-3-model med Prompt flow

Efter at have implementeret din finjusterede model kan du nu integrere den med Prompt Flow for at bruge din model i realtidsapplikationer, hvilket muliggør en række interaktive opgaver med din tilpassede Phi-3-model.

I denne øvelse vil du:

- Oprette Azure AI Foundry Hub.
- Oprette Azure AI Foundry Project.
- Oprette Prompt flow.
- Tilføje en tilpasset forbindelse til den finjusterede Phi-3-model.
- Opsætte Prompt flow til at chatte med din tilpassede Phi-3-model.

> [!NOTE]
> Du kan også integrere med Prompt flow ved hjælp af Azure ML Studio. Den samme integrationsproces kan anvendes på Azure ML Studio.

#### Opret Azure AI Foundry Hub

Du skal oprette en Hub, før du opretter projektet. En Hub fungerer som en Resource Group og giver dig mulighed for at organisere og administrere flere projekter i Azure AI Foundry.

1. Besøg [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Vælg **All hubs** fra menuen til venstre.

1. Vælg **+ New hub** fra navigationsmenuen.

    ![Opret hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.da.png)

1. Udfør følgende opgaver:

    - Indtast **Hub name**. Det skal være en unik værdi.
    - Vælg din Azure **Subscription**.
    - Vælg den **Resource group**, du vil bruge (opret en ny, hvis nødvendigt).
    - Vælg den **Location**, du vil bruge.
    - Vælg **Connect Azure AI Services**, du vil bruge (opret en ny, hvis nødvendigt).
    - Sæt **Connect Azure AI Search** til **Skip connecting**.

    ![Udfyld hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.da.png)

1. Vælg **Next**.

#### Opret Azure AI Foundry Project

1. I den hub, du har oprettet, skal du vælge **All projects** fra menuen til venstre.

1. Vælg **+ New project** fra navigationsmenuen.

    ![Vælg nyt projekt.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.da.png)

1. Indtast **Project name**. Det skal være en unik værdi.

    ![Opret projekt.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.da.png)

1. Vælg **Create a project**.

#### Tilføj en tilpasset forbindelse til den finjusterede Phi-3-model

For at integrere din tilpassede Phi-3-model med Prompt flow skal du gemme modellens endpoint og nøgle i en tilpasset forbindelse. Denne opsætning sikrer adgang til din tilpassede Phi-3-model i Prompt flow.

#### Sæt API-nøgle og endpoint-URI for den finjusterede Phi-3-model

1. Besøg [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Naviger til den Azure Machine Learning-arbejdsplads, du har oprettet.

1. Vælg **Endpoints** fra menuen til venstre.

    ![Vælg endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.da.png)

1. Vælg den endpoint, du har oprettet.

    ![Vælg endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.da.png)

1. Vælg **Consume** fra navigationsmenuen.

1. Kopiér din **REST endpoint** og **Primary key**.
![Kopiér API-nøgle og endpoint-URI.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.da.png)

#### Tilføj den brugerdefinerede forbindelse

1. Besøg [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Naviger til det Azure AI Foundry-projekt, du har oprettet.

1. I det projekt, du har oprettet, vælg **Indstillinger** i venstre sidepanel.

1. Vælg **+ Ny forbindelse**.

    ![Vælg ny forbindelse.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.da.png)

1. Vælg **Brugerdefinerede nøgler** fra navigationsmenuen.

    ![Vælg brugerdefinerede nøgler.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.da.png)

1. Udfør følgende opgaver:

    - Vælg **+ Tilføj nøgle-værdi-par**.
    - For nøgle-navnet indtast **endpoint**, og indsæt endpointet, du kopierede fra Azure ML Studio, i værdifeltet.
    - Vælg **+ Tilføj nøgle-værdi-par** igen.
    - For nøgle-navnet indtast **key**, og indsæt nøglen, du kopierede fra Azure ML Studio, i værdifeltet.
    - Efter at have tilføjet nøglerne, vælg **is secret** for at forhindre, at nøglen bliver eksponeret.

    ![Tilføj forbindelse.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.da.png)

1. Vælg **Tilføj forbindelse**.

#### Opret Prompt flow

Du har tilføjet en brugerdefineret forbindelse i Azure AI Foundry. Lad os nu oprette et Prompt flow ved hjælp af følgende trin. Derefter vil du forbinde dette Prompt flow til den brugerdefinerede forbindelse, så du kan bruge den fintunede model i Prompt flow.

1. Naviger til det Azure AI Foundry-projekt, du har oprettet.

1. Vælg **Prompt flow** i venstre sidepanel.

1. Vælg **+ Opret** i navigationsmenuen.

    ![Vælg Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.da.png)

1. Vælg **Chat flow** i navigationsmenuen.

    ![Vælg chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.da.png)

1. Indtast **Mappenavn**, der skal bruges.

    ![Indtast navn.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.da.png)

2. Vælg **Opret**.

#### Opsæt Prompt flow til at chatte med din brugerdefinerede Phi-3-model

Du skal integrere den fintunede Phi-3-model i et Prompt flow. Men det eksisterende Prompt flow, der er tilgængeligt, er ikke designet til dette formål. Derfor skal du redesigne Prompt flow for at muliggøre integrationen af den brugerdefinerede model.

1. I Prompt flow skal du udføre følgende opgaver for at genopbygge det eksisterende flow:

    - Vælg **Raw file mode**.
    - Slet al eksisterende kode i *flow.dag.yml*-filen.
    - Tilføj følgende kode til *flow.dag.yml*-filen.

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

    - Vælg **Gem**.

    ![Vælg raw file mode.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.da.png)

1. Tilføj følgende kode til *integrate_with_promptflow.py*-filen for at bruge den brugerdefinerede Phi-3-model i Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": {
                "input_string": [
                    {"role": "user", "content": input_data}
                ],
                "parameters": {
                    "temperature": 0.7,
                    "max_new_tokens": 128
                }
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Indsæt prompt flow kode.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.da.png)

> [!NOTE]
> For mere detaljeret information om brug af Prompt flow i Azure AI Foundry, kan du se [Prompt flow i Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Vælg **Chat input**, **Chat output** for at aktivere chat med din model.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.da.png)

1. Nu er du klar til at chatte med din brugerdefinerede Phi-3-model. I den næste øvelse vil du lære, hvordan du starter Prompt flow og bruger det til at chatte med din fintunede Phi-3-model.

> [!NOTE]
>
> Det genopbyggede flow bør se ud som billedet nedenfor:
>
> ![Flow eksempel.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.da.png)
>

### Chat med din brugerdefinerede Phi-3-model

Nu hvor du har fintunet og integreret din brugerdefinerede Phi-3-model med Prompt flow, er du klar til at begynde at interagere med den. Denne øvelse vil guide dig gennem processen med at opsætte og starte en chat med din model ved hjælp af Prompt flow. Ved at følge disse trin vil du kunne udnytte din fintunede Phi-3-models fulde potentiale til forskellige opgaver og samtaler.

- Chat med din brugerdefinerede Phi-3-model ved hjælp af Prompt flow.

#### Start Prompt flow

1. Vælg **Start compute sessions** for at starte Prompt flow.

    ![Start compute session.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.da.png)

1. Vælg **Valider og parse input** for at forny parametre.

    ![Valider input.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.da.png)

1. Vælg værdien af **connection** til den brugerdefinerede forbindelse, du oprettede. For eksempel *connection*.

    ![Forbindelse.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.da.png)

#### Chat med din brugerdefinerede model

1. Vælg **Chat**.

    ![Vælg chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.da.png)

1. Her er et eksempel på resultaterne: Nu kan du chatte med din brugerdefinerede Phi-3-model. Det anbefales at stille spørgsmål baseret på de data, der blev brugt til fintuning.

    ![Chat med prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.da.png)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på at opnå nøjagtighed, bedes du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.