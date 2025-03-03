# Vyladenie a integrácia vlastných modelov Phi-3 s Prompt Flow v Azure AI Foundry

Tento kompletný (E2E) príklad je založený na návode "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" z Microsoft Tech Community. Predstavuje procesy vyladenia, nasadenia a integrácie vlastných modelov Phi-3 s Prompt Flow v Azure AI Foundry.  
Na rozdiel od príkladu "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", ktorý zahŕňal spúšťanie kódu lokálne, sa tento návod sústreďuje výlučne na vyladenie a integráciu vášho modelu v Azure AI / ML Studio.

## Prehľad

V tomto E2E príklade sa naučíte, ako vyladiť model Phi-3 a integrovať ho s Prompt Flow v Azure AI Foundry. Využitím Azure AI / ML Studio vytvoríte pracovný postup pre nasadenie a používanie vlastných AI modelov. Tento E2E príklad je rozdelený do troch scenárov:

**Scenár 1: Nastavenie Azure zdrojov a príprava na vyladenie**

**Scenár 2: Vyladenie modelu Phi-3 a nasadenie v Azure Machine Learning Studio**

**Scenár 3: Integrácia s Prompt Flow a rozhovor s vaším vlastným modelom v Azure AI Foundry**

Nižšie je prehľad tohto E2E príkladu.

![Phi-3-FineTuning_PromptFlow_Integration Prehľad.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.sk.png)

### Obsah

1. **[Scenár 1: Nastavenie Azure zdrojov a príprava na vyladenie](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Vytvorenie Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Požiadanie o GPU kvóty v Azure Subscription](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Pridanie priradenia rolí](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Nastavenie projektu](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Príprava datasetu na vyladenie](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenár 2: Vyladenie modelu Phi-3 a nasadenie v Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Vyladenie modelu Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Nasadenie vyladeného modelu Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenár 3: Integrácia s Prompt Flow a rozhovor s vaším vlastným modelom v Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrácia vlastného modelu Phi-3 s Prompt Flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Rozhovor s vaším vlastným modelom Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenár 1: Nastavenie Azure zdrojov a príprava na vyladenie

### Vytvorenie Azure Machine Learning Workspace

1. Napíšte *azure machine learning* do **vyhľadávacieho panela** v hornej časti portálu a vyberte **Azure Machine Learning** z ponúkaných možností.

    ![Napíšte azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.sk.png)

2. Vyberte **+ Create** z navigačného menu.

3. Vyberte **New workspace** z navigačného menu.

    ![Vyberte new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.sk.png)

4. Vykonajte nasledujúce úlohy:

    - Vyberte vašu Azure **Subscription**.
    - Vyberte **Resource group**, ktorú chcete použiť (v prípade potreby vytvorte novú).
    - Zadajte **Workspace Name**. Musí byť unikátne.
    - Vyberte **Region**, ktorú chcete použiť.
    - Vyberte **Storage account**, ktorý chcete použiť (v prípade potreby vytvorte nový).
    - Vyberte **Key vault**, ktorý chcete použiť (v prípade potreby vytvorte nový).
    - Vyberte **Application insights**, ktoré chcete použiť (v prípade potreby vytvorte nové).
    - Vyberte **Container registry**, ktorý chcete použiť (v prípade potreby vytvorte nový).

    ![Vyplňte azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.sk.png)

5. Vyberte **Review + Create**.

6. Vyberte **Create**.

### Požiadanie o GPU kvóty v Azure Subscription

V tomto návode sa naučíte, ako vyladiť a nasadiť model Phi-3 pomocou GPU. Na vyladenie použijete GPU *Standard_NC24ads_A100_v4*, ktoré vyžaduje žiadosť o kvótu. Na nasadenie použijete GPU *Standard_NC6s_v3*, ktoré tiež vyžaduje žiadosť o kvótu.

> [!NOTE]
>
> Iba predplatné typu Pay-As-You-Go (štandardný typ predplatného) sú oprávnené na pridelenie GPU; predplatné s výhodami momentálne nie sú podporované.
>

1. Navštívte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vykonajte nasledujúce kroky na požiadanie o kvótu *Standard NCADSA100v4 Family*:

    - Vyberte **Quota** z ľavého navigačného panela.
    - Vyberte **Virtual machine family**, ktorú chcete použiť. Napríklad vyberte **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, ktorý zahŕňa GPU *Standard_NC24ads_A100_v4*.
    - Vyberte **Request quota** z navigačného menu.

        ![Požiadajte o kvótu.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.sk.png)

    - Na stránke Request quota zadajte **New cores limit**, ktorý chcete použiť. Napríklad 24.
    - Na stránke Request quota vyberte **Submit** na odoslanie žiadosti o GPU kvótu.

1. Vykonajte nasledujúce kroky na požiadanie o kvótu *Standard NCSv3 Family*:

    - Vyberte **Quota** z ľavého navigačného panela.
    - Vyberte **Virtual machine family**, ktorú chcete použiť. Napríklad vyberte **Standard NCSv3 Family Cluster Dedicated vCPUs**, ktorý zahŕňa GPU *Standard_NC6s_v3*.
    - Vyberte **Request quota** z navigačného menu.
    - Na stránke Request quota zadajte **New cores limit**, ktorý chcete použiť. Napríklad 24.
    - Na stránke Request quota vyberte **Submit** na odoslanie žiadosti o GPU kvótu.

### Pridanie priradenia rolí

Na vyladenie a nasadenie modelov musíte najskôr vytvoriť User Assigned Managed Identity (UAI) a priradiť mu potrebné povolenia. Tento UAI bude použitý na autentifikáciu počas nasadenia.

#### Vytvorenie User Assigned Managed Identity (UAI)

1. Napíšte *managed identities* do **vyhľadávacieho panela** v hornej časti portálu a vyberte **Managed Identities** z ponúkaných možností.

    ![Napíšte managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.sk.png)

1. Vyberte **+ Create**.

    ![Vyberte create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.sk.png)

1. Vykonajte nasledujúce úlohy:

    - Vyberte vašu Azure **Subscription**.
    - Vyberte **Resource group**, ktorú chcete použiť (v prípade potreby vytvorte novú).
    - Vyberte **Region**, ktorú chcete použiť.
    - Zadajte **Name**. Musí byť unikátne.

    ![Vyberte create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.sk.png)

1. Vyberte **Review + create**.

1. Vyberte **+ Create**.

#### Pridanie role Contributor k Managed Identity

1. Prejdite na Managed Identity zdroj, ktorý ste vytvorili.

1. Vyberte **Azure role assignments** z ľavého navigačného panela.

1. Vyberte **+Add role assignment** z navigačného menu.

1. Na stránke Add role assignment vykonajte nasledujúce úlohy:
    - Vyberte **Scope** na **Resource group**.
    - Vyberte vašu Azure **Subscription**.
    - Vyberte **Resource group**, ktorú chcete použiť.
    - Vyberte **Role** na **Contributor**.

    ![Vyplňte rolu Contributor.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.sk.png)

2. Vyberte **Save**.

#### Pridanie role Storage Blob Data Reader k Managed Identity

1. Napíšte *storage accounts* do **vyhľadávacieho panela** v hornej časti portálu a vyberte **Storage accounts** z ponúkaných možností.

    ![Napíšte storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.sk.png)

1. Vyberte storage account priradený k Azure Machine Learning workspace, ktorý ste vytvorili. Napríklad *finetunephistorage*.

1. Vykonajte nasledujúce kroky na navigáciu na stránku Add role assignment:

    - Prejdite na Azure Storage account, ktorý ste vytvorili.
    - Vyberte **Access Control (IAM)** z ľavého navigačného panela.
    - Vyberte **+ Add** z navigačného menu.
    - Vyberte **Add role assignment** z navigačného menu.

    ![Pridajte rolu.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.sk.png)

1. Na stránke Add role assignment vykonajte nasledujúce úlohy:

    - Na stránke Role napíšte *Storage Blob Data Reader* do **vyhľadávacieho panela** a vyberte **Storage Blob Data Reader** z ponúkaných možností.
    - Na stránke Role vyberte **Next**.
    - Na stránke Members vyberte **Assign access to** **Managed identity**.
    - Na stránke Members vyberte **+ Select members**.
    - Na stránke Select managed identities vyberte vašu Azure **Subscription**.
    - Na stránke Select managed identities vyberte **Managed identity** na **Manage Identity**.
    - Na stránke Select managed identities vyberte Managed Identity, ktorý ste vytvorili. Napríklad *finetunephi-managedidentity*.
    - Na stránke Select managed identities vyberte **Select**.

    ![Vyberte managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.sk.png)

1. Vyberte **Review + assign**.

#### Pridanie role AcrPull k Managed Identity

1. Napíšte *container registries* do **vyhľadávacieho panela** v hornej časti portálu a vyberte **Container registries** z ponúkaných možností.

    ![Napíšte container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.sk.png)

1. Vyberte container registry priradený k Azure Machine Learning workspace. Napríklad *finetunephicontainerregistry*.

1. Vykonajte nasledujúce kroky na navigáciu na stránku Add role assignment:

    - Vyberte **Access Control (IAM)** z ľavého navigačného panela.
    - Vyberte **+ Add** z navigačného menu.
    - Vyberte **Add role assignment** z navigačného menu.

1. Na stránke Add role assignment vykonajte nasledujúce úlohy:

    - Na stránke Role napíšte *AcrPull* do **vyhľadávacieho panela** a vyberte **AcrPull** z ponúkaných možností.
    - Na stránke Role vyberte **Next**.
    - Na stránke Members vyberte **Assign access to** **Managed identity**.
    - Na stránke Members vyberte **+ Select members**.
    - Na stránke Select managed identities vyberte vašu Azure **Subscription**.
    - Na stránke Select managed identities vyberte **Managed identity** na **Manage Identity**.
    - Na stránke Select managed identities vyberte Managed Identity, ktorý ste vytvorili. Napríklad *finetunephi-managedidentity*.
    - Na stránke Select managed identities vyberte **Select**.
    - Vyberte **Review + assign**.

### Nastavenie projektu

Na stiahnutie datasetov potrebných na vyladenie nastavíte lokálne prostredie.

V tomto cvičení:

- Vytvoríte priečinok na prácu.
- Vytvoríte virtuálne prostredie.
- Nainštalujete potrebné balíčky.
- Vytvoríte súbor *download_dataset.py* na stiahnutie datasetu.

#### Vytvorenie priečinka na prácu

1. Otvorte terminál a napíšte nasledujúci príkaz na vytvorenie priečinka s názvom *finetune-phi* v predvolenej ceste.

    ```console
    mkdir finetune-phi
    ```

2. Napíšte nasledujúci príkaz v termináli na navigáciu do vytvoreného priečinka *finetune-phi*.

    ```console
    cd finetune-phi
    ```

#### Vytvorenie virtuálneho prostredia

1. Napíšte nasledujúci príkaz v termináli na vytvorenie virtuálneho prostredia s názvom *.venv*.

    ```console
    python -m venv .venv
    ```

2. Napíšte nasledujúci príkaz v termináli na aktiváciu virtuálneho prostredia.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Ak sa to podarilo, pred výzvou príkazového riadku by ste mali vidieť *(.venv)*.

#### Inštalácia potrebných balíčkov

1. Napíšte nasledujúce príkazy v termináli na inštaláciu potrebných balíčkov.

    ```console
    pip install datasets==2.19.1
    ```

#### Vytvorenie `download_dataset.py`

> [!NOTE]
> Kompletná štruktúra priečinkov:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Otvorte **Visual Studio Code**.

1. Vyberte **File** z menu.

1. Vyberte **Open Folder**.

1. Vyberte priečinok *finetune-phi*, ktorý ste vytvorili, nachádzajúci sa na *C:\Users\yourUserName\finetune-phi*.

    ![Vyberte priečinok, ktorý ste vytvorili.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.sk.png)

1. V ľavom paneli Visual Studio Code kliknite pravým tlačidlom a vyberte **New File** na vytvorenie nového súboru s názvom *download_dataset.py*.

    ![Vytvorte nový súbor.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.sk.png)

### Príprava datasetu na vyladenie

V tomto cvičení spustíte súbor *download_dataset.py* na stiahnutie datasetu *ultrachat_200k* do vášho lokálneho prostredia. Tento dataset následne použijete na vyladenie modelu Phi-3 v Azure Machine Learning.

V tomto cvičení:

- Pridáte kód do súboru *download_dataset.py* na stiahnutie datasetov.
- Spustíte súbor *download_dataset.py* na stiahnutie datasetov do vášho lokálneho prostredia.

#### Stiahnutie datasetu pomocou *download_dataset.py*

1. Otvorte súbor *download_dataset.py* vo Visual Studio Code.

1. Pridajte nasledujúci kód do súboru *download_dataset.py*.

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

1. Napíšte nasledujúci príkaz v termináli na spustenie skriptu a stiahnutie datasetu do vášho lokálneho prostredia.

    ```console
    python download_dataset.py
    ```

1.
1. Navštívte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vyberte **Compute** z ľavého panela.

1. Vyberte **Compute clusters** z navigačného menu.

1. Kliknite na **+ New**.

    ![Vyberte compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.sk.png)

1. Vykonajte nasledujúce kroky:

    - Vyberte **Region**, ktorý chcete použiť.
    - Nastavte **Virtual machine tier** na **Dedicated**.
    - Nastavte **Virtual machine type** na **GPU**.
    - Nastavte filter **Virtual machine size** na **Select from all options**.
    - Vyberte **Virtual machine size** na **Standard_NC24ads_A100_v4**.

    ![Vytvorte cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.sk.png)

1. Kliknite na **Next**.

1. Vykonajte nasledujúce kroky:

    - Zadajte **Compute name**. Musí byť jedinečné.
    - Nastavte **Minimum number of nodes** na **0**.
    - Nastavte **Maximum number of nodes** na **1**.
    - Nastavte **Idle seconds before scale down** na **120**.

    ![Vytvorte cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.sk.png)

1. Kliknite na **Create**.

#### Jemné doladenie modelu Phi-3

1. Navštívte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vyberte pracovný priestor Azure Machine Learning, ktorý ste vytvorili.

    ![Vyberte pracovný priestor, ktorý ste vytvorili.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.sk.png)

1. Vykonajte nasledujúce kroky:

    - Vyberte **Model catalog** z ľavého panela.
    - Do **search bar** zadajte *phi-3-mini-4k* a z dostupných možností vyberte **Phi-3-mini-4k-instruct**.

    ![Zadajte phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.sk.png)

1. Vyberte **Fine-tune** z navigačného menu.

    ![Vyberte fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.sk.png)

1. Vykonajte nasledujúce kroky:

    - Nastavte **Select task type** na **Chat completion**.
    - Kliknite na **+ Select data** na nahratie **Traning data**.
    - Nastavte typ nahrávania validačných dát na **Provide different validation data**.
    - Kliknite na **+ Select data** na nahratie **Validation data**.

    ![Vyplňte stránku jemného doladenia.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.sk.png)

    > [!TIP]
    >
    > Môžete vybrať **Advanced settings** na prispôsobenie konfigurácií, ako sú **learning_rate** a **lr_scheduler_type**, aby ste optimalizovali proces jemného doladenia podľa vašich špecifických potrieb.

1. Kliknite na **Finish**.

1. V tomto cvičení ste úspešne jemne doladili model Phi-3 pomocou Azure Machine Learning. Upozorňujeme, že proces jemného doladenia môže trvať dlhší čas. Po spustení jemného doladenia musíte počkať na jeho dokončenie. Stav jemného doladenia môžete sledovať v karte Jobs na ľavej strane vášho pracovného priestoru Azure Machine Learning. V ďalšej sérii nasadíte jemne doladený model a integrujete ho s Prompt flow.

    ![Pozrite si úlohu jemného doladenia.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.sk.png)

### Nasadenie jemne doladeného modelu Phi-3

Na integráciu jemne doladeného modelu Phi-3 s Prompt flow musíte model nasadiť, aby bol dostupný na inferenciu v reálnom čase. Tento proces zahŕňa registráciu modelu, vytvorenie online koncového bodu a nasadenie modelu.

V tomto cvičení:

- Zaregistrujete jemne doladený model v pracovnom priestore Azure Machine Learning.
- Vytvoríte online koncový bod.
- Nasadíte zaregistrovaný jemne doladený model Phi-3.

#### Registrácia jemne doladeného modelu

1. Navštívte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vyberte pracovný priestor Azure Machine Learning, ktorý ste vytvorili.

    ![Vyberte pracovný priestor, ktorý ste vytvorili.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.sk.png)

1. Vyberte **Models** z ľavého panela.
1. Kliknite na **+ Register**.
1. Vyberte **From a job output**.

    ![Zaregistrujte model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.sk.png)

1. Vyberte úlohu, ktorú ste vytvorili.

    ![Vyberte úlohu.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.sk.png)

1. Kliknite na **Next**.

1. Nastavte **Model type** na **MLflow**.

1. Uistite sa, že **Job output** je vybrané; malo by byť automaticky vybrané.

    ![Vyberte výstup.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.sk.png)

2. Kliknite na **Next**.

3. Kliknite na **Register**.

    ![Vyberte register.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.sk.png)

4. Svoj zaregistrovaný model môžete zobraziť tak, že prejdete do menu **Models** z ľavého panela.

    ![Zaregistrovaný model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.sk.png)

#### Nasadenie jemne doladeného modelu

1. Prejdite do pracovného priestoru Azure Machine Learning, ktorý ste vytvorili.

1. Vyberte **Endpoints** z ľavého panela.

1. Vyberte **Real-time endpoints** z navigačného menu.

    ![Vytvorte endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.sk.png)

1. Kliknite na **Create**.

1. Vyberte zaregistrovaný model, ktorý ste vytvorili.

    ![Vyberte zaregistrovaný model.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.sk.png)

1. Kliknite na **Select**.

1. Vykonajte nasledujúce kroky:

    - Nastavte **Virtual machine** na *Standard_NC6s_v3*.
    - Nastavte **Instance count**, napríklad na *1*.
    - Nastavte **Endpoint** na **New**, aby ste vytvorili endpoint.
    - Zadajte **Endpoint name**. Musí byť jedinečné.
    - Zadajte **Deployment name**. Musí byť jedinečné.

    ![Vyplňte nastavenia nasadenia.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.sk.png)

1. Kliknite na **Deploy**.

> [!WARNING]
> Aby ste sa vyhli dodatočným poplatkom na vašom účte, nezabudnite vymazať vytvorený endpoint v pracovnom priestore Azure Machine Learning.
>

#### Skontrolujte stav nasadenia v pracovnom priestore Azure Machine Learning

1. Prejdite do pracovného priestoru Azure Machine Learning, ktorý ste vytvorili.

1. Vyberte **Endpoints** z ľavého panela.

1. Vyberte endpoint, ktorý ste vytvorili.

    ![Vyberte endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.sk.png)

1. Na tejto stránke môžete spravovať endpoints počas procesu nasadenia.

> [!NOTE]
> Po dokončení nasadenia sa uistite, že **Live traffic** je nastavený na **100%**. Ak nie je, vyberte **Update traffic**, aby ste upravili nastavenia prenosu. Upozorňujeme, že model nemôžete testovať, ak je prenos nastavený na 0%.
>
> ![Nastavte traffic.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.sk.png)
>

## Scenár 3: Integrácia s Prompt flow a komunikácia s vaším vlastným modelom v Azure AI Foundry

### Integrácia vlastného modelu Phi-3 s Prompt flow

Po úspešnom nasadení vášho jemne doladeného modelu ho môžete integrovať s Prompt Flow, aby ste mohli svoj model používať v reálnych aplikáciách a umožniť rôzne interaktívne úlohy s vaším vlastným modelom Phi-3.

V tomto cvičení:

- Vytvoríte Azure AI Foundry Hub.
- Vytvoríte Azure AI Foundry Project.
- Vytvoríte Prompt flow.
- Pridáte vlastné pripojenie pre jemne doladený model Phi-3.
- Nastavíte Prompt flow na komunikáciu s vaším vlastným modelom Phi-3.

> [!NOTE]
> Integrácia s Promptflow je možná aj pomocou Azure ML Studio. Rovnaký proces integrácie sa dá aplikovať aj v Azure ML Studio.

#### Vytvorenie Azure AI Foundry Hub

Pred vytvorením projektu musíte vytvoriť Hub. Hub funguje ako Resource Group, ktorá vám umožňuje organizovať a spravovať viacero projektov v Azure AI Foundry.

1. Navštívte [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Vyberte **All hubs** z ľavého panela.

1. Kliknite na **+ New hub** z navigačného menu.

    ![Vytvorte hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.sk.png)

1. Vykonajte nasledujúce kroky:

    - Zadajte **Hub name**. Musí byť jedinečné.
    - Vyberte vašu Azure **Subscription**.
    - Vyberte **Resource group**, ktorú chcete použiť (v prípade potreby vytvorte novú).
    - Vyberte **Location**, ktorú chcete použiť.
    - Vyberte **Connect Azure AI Services**, ktoré chcete použiť (v prípade potreby vytvorte nové).
    - Nastavte **Connect Azure AI Search** na **Skip connecting**.

    ![Vyplňte hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.sk.png)

1. Kliknite na **Next**.

#### Vytvorenie Azure AI Foundry Project

1. V Hube, ktorý ste vytvorili, vyberte **All projects** z ľavého panela.

1. Kliknite na **+ New project** z navigačného menu.

    ![Vyberte nový projekt.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.sk.png)

1. Zadajte **Project name**. Musí byť jedinečné.

    ![Vytvorte projekt.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.sk.png)

1. Kliknite na **Create a project**.

#### Pridanie vlastného pripojenia pre jemne doladený model Phi-3

Aby ste integrovali váš vlastný model Phi-3 s Prompt flow, musíte uložiť endpoint a kľúč modelu v rámci vlastného pripojenia. Toto nastavenie zabezpečí prístup k vášmu vlastnému modelu Phi-3 v Prompt flow.

#### Nastavenie api kľúča a endpoint uri jemne doladeného modelu Phi-3

1. Navštívte [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Prejdite do pracovného priestoru Azure Machine Learning, ktorý ste vytvorili.

1. Vyberte **Endpoints** z ľavého panela.

    ![Vyberte endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.sk.png)

1. Vyberte endpoint, ktorý ste vytvorili.

    ![Vyberte endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.sk.png)

1. Kliknite na **Consume** z navigačného menu.

1. Skopírujte svoj **REST endpoint** a **Primary key**.
![Skopírujte kľúč API a URI koncového bodu.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.sk.png)

#### Pridanie vlastného pripojenia

1. Navštívte [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Prejdite na projekt Azure AI Foundry, ktorý ste vytvorili.

1. V projekte, ktorý ste vytvorili, vyberte **Settings** z ľavého panelu.

1. Zvoľte **+ New connection**.

    ![Vyberte nové pripojenie.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.sk.png)

1. Zvoľte **Custom keys** z navigačného menu.

    ![Vyberte vlastné kľúče.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.sk.png)

1. Vykonajte nasledujúce kroky:

    - Vyberte **+ Add key value pairs**.
    - Pre názov kľúča zadajte **endpoint** a vložte URI koncového bodu, ktorý ste skopírovali z Azure ML Studio, do poľa hodnoty.
    - Opäť vyberte **+ Add key value pairs**.
    - Pre názov kľúča zadajte **key** a vložte kľúč, ktorý ste skopírovali z Azure ML Studio, do poľa hodnoty.
    - Po pridaní kľúčov vyberte **is secret**, aby ste zabránili zobrazeniu kľúča.

    ![Pridanie pripojenia.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.sk.png)

1. Vyberte **Add connection**.

#### Vytvorenie Prompt flow

Pridali ste vlastné pripojenie v Azure AI Foundry. Teraz vytvorme Prompt flow pomocou nasledujúcich krokov. Potom prepojíte tento Prompt flow s vlastným pripojením, aby ste mohli používať jemne doladený model v rámci Prompt flow.

1. Prejdite na projekt Azure AI Foundry, ktorý ste vytvorili.

1. Zvoľte **Prompt flow** z ľavého panelu.

1. Zvoľte **+ Create** z navigačného menu.

    ![Vyberte Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.sk.png)

1. Zvoľte **Chat flow** z navigačného menu.

    ![Vyberte chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.sk.png)

1. Zadajte **Folder name**, ktorý chcete použiť.

    ![Zadajte názov.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.sk.png)

2. Vyberte **Create**.

#### Nastavenie Prompt flow na chatovanie s vaším vlastným modelom Phi-3

Je potrebné integrovať jemne doladený model Phi-3 do Prompt flow. Existujúci Prompt flow však nie je navrhnutý na tento účel. Preto musíte Prompt flow upraviť, aby ste umožnili integráciu vlastného modelu.

1. V Prompt flow vykonajte nasledujúce kroky na prestavbu existujúceho flow:

    - Vyberte **Raw file mode**.
    - Odstráňte všetok existujúci kód v súbore *flow.dag.yml*.
    - Pridajte nasledujúci kód do súboru *flow.dag.yml*.

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

    - Vyberte **Save**.

    ![Vyberte režim raw file.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.sk.png)

1. Pridajte nasledujúci kód do súboru *integrate_with_promptflow.py* na použitie vlastného modelu Phi-3 v Prompt flow.

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

    ![Vložte kód Prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.sk.png)

> [!NOTE]
> Pre podrobnejšie informácie o používaní Prompt flow v Azure AI Foundry si môžete pozrieť [Prompt flow v Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Vyberte **Chat input**, **Chat output**, aby ste umožnili chatovanie s vaším modelom.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.sk.png)

1. Teraz ste pripravení chatovať s vaším vlastným modelom Phi-3. V ďalšom cvičení sa naučíte, ako spustiť Prompt flow a použiť ho na chatovanie s vaším jemne doladeným modelom Phi-3.

> [!NOTE]
>
> Upravený flow by mal vyzerať ako na obrázku nižšie:
>
> ![Príklad flow.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.sk.png)
>

### Chatovanie s vaším vlastným modelom Phi-3

Teraz, keď ste jemne doladili a integrovali váš vlastný model Phi-3 s Prompt flow, ste pripravení začať s ním komunikovať. Toto cvičenie vás prevedie procesom nastavenia a spustenia chatu s vaším modelom pomocou Prompt flow. Postupovaním podľa týchto krokov budete môcť plne využiť schopnosti vášho jemne doladeného modelu Phi-3 pre rôzne úlohy a rozhovory.

- Chatovanie s vaším vlastným modelom Phi-3 pomocou Prompt flow.

#### Spustenie Prompt flow

1. Vyberte **Start compute sessions**, aby ste spustili Prompt flow.

    ![Spustenie výpočtovej relácie.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.sk.png)

1. Vyberte **Validate and parse input**, aby ste obnovili parametre.

    ![Validácia vstupu.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.sk.png)

1. Vyberte **Value** pre **connection** k vlastnému pripojeniu, ktoré ste vytvorili. Napríklad *connection*.

    ![Pripojenie.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.sk.png)

#### Chatovanie s vaším vlastným modelom

1. Vyberte **Chat**.

    ![Vyberte chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.sk.png)

1. Tu je príklad výsledkov: Teraz môžete chatovať s vaším vlastným modelom Phi-3. Odporúča sa klásť otázky na základe údajov použitých pri jemnom doladení.

    ![Chatovanie s Prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.sk.png)

**Upozornenie**:  
Tento dokument bol preložený pomocou služieb strojového prekladu AI. Aj keď sa snažíme o presnosť, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za záväzný zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.