# Vylepšení a integrace vlastních Phi-3 modelů s Prompt flow v Azure AI Foundry

Tento komplexní příklad (E2E) je založen na průvodci "[Vylepšení a integrace vlastních Phi-3 modelů s Prompt Flow v Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" z Microsoft Tech Community. Popisuje procesy vylepšování, nasazování a integrace vlastních Phi-3 modelů s Prompt flow v Azure AI Foundry. 
Na rozdíl od E2E příkladu "[Vylepšení a integrace vlastních Phi-3 modelů s Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", který vyžadoval spuštění kódu lokálně, se tento tutoriál zaměřuje výhradně na vylepšení a integraci modelu přímo v Azure AI / ML Studiu.

## Přehled

V tomto E2E příkladu se naučíte, jak vylepšit model Phi-3 a integrovat ho s Prompt flow v Azure AI Foundry. Využitím Azure AI / ML Studia vytvoříte workflow pro nasazení a použití vlastních AI modelů. Tento příklad je rozdělen do tří scénářů:

**Scénář 1: Nastavení Azure zdrojů a příprava na vylepšení**

**Scénář 2: Vylepšení modelu Phi-3 a jeho nasazení v Azure Machine Learning Studiu**

**Scénář 3: Integrace s Prompt flow a komunikace s vaším vlastním modelem v Azure AI Foundry**

Níže je přehled tohoto E2E příkladu.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.cs.png)

### Obsah

1. **[Scénář 1: Nastavení Azure zdrojů a příprava na vylepšení](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Vytvoření Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Žádost o GPU kvóty v Azure Subscription](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Přidání role](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Nastavení projektu](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Příprava datasetu na vylepšení](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scénář 2: Vylepšení modelu Phi-3 a jeho nasazení v Azure Machine Learning Studiu](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Vylepšení modelu Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Nasazení vylepšeného modelu Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scénář 3: Integrace s Prompt flow a komunikace s vaším vlastním modelem v Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integrace vlastního modelu Phi-3 s Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Komunikace s vaším vlastním modelem Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scénář 1: Nastavení Azure zdrojů a příprava na vylepšení

### Vytvoření Azure Machine Learning Workspace

1. Do **vyhledávacího pole** v horní části portálové stránky zadejte *azure machine learning* a z nabízených možností vyberte **Azure Machine Learning**.

    ![Zadejte azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.cs.png)

2. Z nabídky navigace vyberte **+ Vytvořit**.

3. V nabídce navigace vyberte **Nový workspace**.

    ![Vyberte nový workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.cs.png)

4. Proveďte následující kroky:

    - Vyberte svůj Azure **Subscription**.
    - Vyberte **Resource group** (vytvořte novou, pokud je to potřeba).
    - Zadejte **Workspace Name**. Musí být unikátní.
    - Vyberte **Region**, který chcete použít.
    - Vyberte **Storage account** (vytvořte nový, pokud je to potřeba).
    - Vyberte **Key vault** (vytvořte nový, pokud je to potřeba).
    - Vyberte **Application insights** (vytvořte nový, pokud je to potřeba).
    - Vyberte **Container registry** (vytvořte nový, pokud je to potřeba).

    ![Vyplňte Azure Machine Learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.cs.png)

5. Vyberte **Review + Create**.

6. Vyberte **Create**.

### Žádost o GPU kvóty v Azure Subscription

V tomto tutoriálu se naučíte, jak vylepšit a nasadit Phi-3 model s využitím GPU. Pro vylepšení použijete GPU *Standard_NC24ads_A100_v4*, které vyžaduje žádost o kvótu. Pro nasazení použijete GPU *Standard_NC6s_v3*, které také vyžaduje žádost o kvótu.

> [!NOTE]
>
> Pouze Pay-As-You-Go subscription (standardní typ předplatného) jsou způsobilé pro alokaci GPU; předplatné založené na výhodách aktuálně nejsou podporovány.

1. Navštivte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Proveďte následující kroky pro žádost o kvótu *Standard NCADSA100v4 Family*:

    - Vyberte **Quota** z levého panelu.
    - Vyberte **Virtual machine family**. Například vyberte **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, což zahrnuje GPU *Standard_NC24ads_A100_v4*.
    - Vyberte **Request quota** z nabídky navigace.

        ![Žádost o kvótu.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.cs.png)

    - Na stránce Request quota zadejte **New cores limit**, který chcete použít. Například 24.
    - Na stránce Request quota vyberte **Submit** pro odeslání žádosti o GPU kvótu.

1. Proveďte následující kroky pro žádost o kvótu *Standard NCSv3 Family*:

    - Vyberte **Quota** z levého panelu.
    - Vyberte **Virtual machine family**. Například vyberte **Standard NCSv3 Family Cluster Dedicated vCPUs**, což zahrnuje GPU *Standard_NC6s_v3*.
    - Vyberte **Request quota** z nabídky navigace.
    - Na stránce Request quota zadejte **New cores limit**, který chcete použít. Například 24.
    - Na stránce Request quota vyberte **Submit** pro odeslání žádosti o GPU kvótu.

### Přidání role

Pro vylepšení a nasazení vašich modelů musíte nejprve vytvořit User Assigned Managed Identity (UAI) a přiřadit jí odpovídající oprávnění. Tato UAI bude použita pro autentizaci během nasazování.

#### Vytvoření User Assigned Managed Identity (UAI)

1. Do **vyhledávacího pole** v horní části portálové stránky zadejte *managed identities* a z nabízených možností vyberte **Managed Identities**.

    ![Zadejte managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.cs.png)

1. Vyberte **+ Vytvořit**.

    ![Vyberte vytvořit.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.cs.png)

1. Proveďte následující kroky:

    - Vyberte svůj Azure **Subscription**.
    - Vyberte **Resource group** (vytvořte novou, pokud je to potřeba).
    - Vyberte **Region**, který chcete použít.
    - Zadejte **Name**. Musí být unikátní.

    ![Vyplňte Managed Identities.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.cs.png)

1. Vyberte **Review + create**.

1. Vyberte **+ Create**.

#### Přidání role Contributor k Managed Identity

1. Přejděte k Managed Identity zdroji, který jste vytvořili.

1. Vyberte **Azure role assignments** z levého panelu.

1. Vyberte **+Add role assignment** z nabídky navigace.

1. Na stránce Add role assignment proveďte následující kroky:
    - Nastavte **Scope** na **Resource group**.
    - Vyberte svůj Azure **Subscription**.
    - Vyberte **Resource group**, kterou chcete použít.
    - Nastavte **Role** na **Contributor**.

    ![Vyplňte roli Contributor.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.cs.png)

2. Vyberte **Save**.

#### Přidání role Storage Blob Data Reader k Managed Identity

1. Do **vyhledávacího pole** v horní části portálové stránky zadejte *storage accounts* a z nabízených možností vyberte **Storage accounts**.

    ![Zadejte storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.cs.png)

1. Vyberte úložiště, které je spojeno s Azure Machine Learning workspace, které jste vytvořili. Například *finetunephistorage*.

1. Proveďte následující kroky pro navigaci na stránku Add role assignment:

    - Přejděte do Azure Storage účtu, který jste vytvořili.
    - Vyberte **Access Control (IAM)** z levého panelu.
    - Vyberte **+ Add** z nabídky navigace.
    - Vyberte **Add role assignment** z nabídky navigace.

    ![Přidání role.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.cs.png)

1. Na stránce Add role assignment proveďte následující kroky:

    - Na stránce Role zadejte *Storage Blob Data Reader* do **vyhledávacího pole** a vyberte **Storage Blob Data Reader** z nabízených možností.
    - Na stránce Role vyberte **Next**.
    - Na stránce Members nastavte **Assign access to** na **Managed identity**.
    - Na stránce Members vyberte **+ Select members**.
    - Na stránce Select managed identities vyberte svůj Azure **Subscription**.
    - Na stránce Select managed identities vyberte **Managed identity**, kterou jste vytvořili. Například *finetunephi-managedidentity*.
    - Na stránce Select managed identities vyberte **Select**.

    ![Vyberte Managed Identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.cs.png)

1. Vyberte **Review + assign**.

#### Přidání role AcrPull k Managed Identity

1. Do **vyhledávacího pole** v horní části portálové stránky zadejte *container registries* a z nabízených možností vyberte **Container registries**.

    ![Zadejte container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.cs.png)

1. Vyberte registr kontejnerů, který je spojen s Azure Machine Learning workspace. Například *finetunephicontainerregistry*.

1. Proveďte následující kroky pro navigaci na stránku Add role assignment:

    - Vyberte **Access Control (IAM)** z levého panelu.
    - Vyberte **+ Add** z nabídky navigace.
    - Vyberte **Add role assignment** z nabídky navigace.

1. Na stránce Add role assignment proveďte následující kroky:

    - Na stránce Role zadejte *AcrPull* do **vyhledávacího pole** a vyberte **AcrPull** z nabízených možností.
    - Na stránce Role vyberte **Next**.
    - Na stránce Members nastavte **Assign access to** na **Managed identity**.
    - Na stránce Members vyberte **+ Select members**.
    - Na stránce Select managed identities vyberte svůj Azure **Subscription**.
    - Na stránce Select managed identities vyberte **Managed identity**, kterou jste vytvořili. Například *finetunephi-managedidentity*.
    - Na stránce Select managed identities vyberte **Select**.
    - Vyberte **Review + assign**.

### Nastavení projektu

Pro stažení datasetů potřebných k vylepšení nastavíte lokální prostředí.

V tomto cvičení:

- Vytvoříte složku pro práci.
- Vytvoříte virtuální prostředí.
- Nainstalujete potřebné balíčky.
- Vytvoříte soubor *download_dataset.py* pro stažení datasetu.

#### Vytvoření složky pro práci

1. Otevřete terminálové okno a zadejte následující příkaz pro vytvoření složky s názvem *finetune-phi* ve výchozí cestě.

    ```console
    mkdir finetune-phi
    ```

2. Zadejte následující příkaz v terminálu pro přechod do složky *finetune-phi*, kterou jste vytvořili.

    ```console
    cd finetune-phi
    ```

#### Vytvoření virtuálního prostředí

1. Zadejte následující příkaz v terminálu pro vytvoření virtuálního prostředí s názvem *.venv*.

    ```console
    python -m venv .venv
    ```

2. Zadejte následující příkaz v terminálu pro aktivaci virtuálního prostředí.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Pokud vše funguje správně, měli byste vidět *(.venv)* před příkazovým řádkem.

#### Instalace potřebných balíčků

1. Zadejte následující příkazy v terminálu pro instalaci potřebných balíčků.

    ```console
    pip install datasets==2.19.1
    ```

#### Vytvoření `download_dataset.py`

> [!NOTE]
> Kompletní struktura složek:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Otevřete **Visual Studio Code**.

1. Vyberte **Soubor** z horního menu.

1. Vyberte **Otevřít složku**.

1. Vyberte složku *finetune-phi*, kterou jste vytvořili, umístěnou v *C:\Users\yourUserName\finetune-phi*.

    ![Vyberte složku, kterou jste vytvořili.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.cs.png)

1. V levém panelu Visual Studio Code klikněte pravým tlačítkem a vyberte **Nový soubor** pro vytvoření nového souboru s názvem *download_dataset.py*.

    ![Vytvořte nový soubor.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.cs.png)

### Příprava datasetu na vylepšení

V tomto cvičení spustíte soubor *download_dataset.py* pro stažení datasetu *ultrachat_200k* do svého lokálního prostředí. Tento dataset následně použijete k vylepšení modelu Phi-3 v Azure Machine Learning.

V tomto cvičení:

- Přidáte kód do souboru *download_dataset.py* pro stažení datasetu.
- Spustíte soubor *download_dataset.py* pro stažení datasetu do svého lokálního prostředí.

#### Stažení datasetu pomocí *download_dataset.py*

1. Otevřete soubor *download_dataset.py* ve Visual Studio Code.

1. Přidejte následující kód do souboru *download_dataset.py*.

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

1. Zadejte následující příkaz v terminálu pro spuštění skriptu a stažení datasetu do svého lokálního prostředí.

    ```console
    python download_dataset.py
    ```

1. Ověřte, že dataset byl úspěšně uložen do vašeho lokálního adresáře *finetune-phi/data*.

> [!NOTE]
>
> #### Poznámka k velikosti datasetu a době vylepšení
>
> V tomto tutoriálu použijete pouze 1 % datasetu (`split='train[:1%]'`). To výrazně snižuje množství dat, což urychluje proces nahrávání i vylepšování. Můžete upravit procento pro nalezení správné rovnováhy mezi dobou tr
1. Navštivte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vyberte **Compute** z levého panelu.

1. Vyberte **Compute clusters** z navigační nabídky.

1. Vyberte **+ New**.

    ![Vyberte compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.cs.png)

1. Proveďte následující kroky:

    - Vyberte **Region**, který chcete použít.
    - Nastavte **Virtual machine tier** na **Dedicated**.
    - Nastavte **Virtual machine type** na **GPU**.
    - Nastavte filtr **Virtual machine size** na **Select from all options**.
    - Nastavte **Virtual machine size** na **Standard_NC24ads_A100_v4**.

    ![Vytvořte cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.cs.png)

1. Vyberte **Next**.

1. Proveďte následující kroky:

    - Zadejte **Compute name**. Musí to být unikátní hodnota.
    - Nastavte **Minimum number of nodes** na **0**.
    - Nastavte **Maximum number of nodes** na **1**.
    - Nastavte **Idle seconds before scale down** na **120**.

    ![Vytvořte cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.cs.png)

1. Vyberte **Create**.

#### Jemné doladění modelu Phi-3

1. Navštivte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vyberte Azure Machine Learning workspace, který jste vytvořili.

    ![Vyberte workspace, který jste vytvořili.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.cs.png)

1. Proveďte následující kroky:

    - Vyberte **Model catalog** z levého panelu.
    - Zadejte *phi-3-mini-4k* do **vyhledávacího pole** a vyberte **Phi-3-mini-4k-instruct** z nabízených možností.

    ![Zadejte phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.cs.png)

1. Vyberte **Fine-tune** z navigační nabídky.

    ![Vyberte fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.cs.png)

1. Proveďte následující kroky:

    - Nastavte **Select task type** na **Chat completion**.
    - Vyberte **+ Select data** pro nahrání **Training data**.
    - Nastavte typ nahrání validačních dat na **Provide different validation data**.
    - Vyberte **+ Select data** pro nahrání **Validation data**.

    ![Vyplňte stránku jemného doladění.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.cs.png)

    > [!TIP]
    >
    > Můžete vybrat **Advanced settings** pro přizpůsobení konfigurací, jako jsou **learning_rate** a **lr_scheduler_type**, aby byl proces jemného doladění optimalizován podle vašich konkrétních potřeb.

1. Vyberte **Finish**.

1. V tomto cvičení jste úspěšně provedli jemné doladění modelu Phi-3 pomocí Azure Machine Learning. Vezměte na vědomí, že proces jemného doladění může trvat značnou dobu. Po spuštění úlohy jemného doladění musíte počkat na její dokončení. Stav úlohy jemného doladění můžete sledovat v záložce Jobs na levé straně vašeho Azure Machine Learning Workspace. V další sérii nasadíte jemně doladěný model a integrujete ho s Prompt Flow.

    ![Zobrazte úlohu jemného doladění.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.cs.png)

### Nasazení jemně doladěného modelu Phi-3

Pro integraci jemně doladěného modelu Phi-3 s Prompt Flow je nutné model nasadit, aby byl dostupný pro real-time inference. Tento proces zahrnuje registraci modelu, vytvoření online endpointu a nasazení modelu.

V tomto cvičení:

- Zaregistrujete jemně doladěný model v Azure Machine Learning workspace.
- Vytvoříte online endpoint.
- Nasadíte registrovaný jemně doladěný model Phi-3.

#### Registrace jemně doladěného modelu

1. Navštivte [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Vyberte Azure Machine Learning workspace, který jste vytvořili.

    ![Vyberte workspace, který jste vytvořili.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.cs.png)

1. Vyberte **Models** z levého panelu.
1. Vyberte **+ Register**.
1. Vyberte **From a job output**.

    ![Zaregistrujte model.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.cs.png)

1. Vyberte úlohu, kterou jste vytvořili.

    ![Vyberte úlohu.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.cs.png)

1. Vyberte **Next**.

1. Nastavte **Model type** na **MLflow**.

1. Ujistěte se, že je vybrána možnost **Job output**; měla by být automaticky vybrána.

    ![Vyberte výstup.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.cs.png)

2. Vyberte **Next**.

3. Vyberte **Register**.

    ![Vyberte registraci.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.cs.png)

4. Svůj registrovaný model můžete zobrazit v nabídce **Models** z levého panelu.

    ![Registrovaný model.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.cs.png)

#### Nasazení jemně doladěného modelu

1. Přejděte do Azure Machine Learning workspace, který jste vytvořili.

1. Vyberte **Endpoints** z levého panelu.

1. Vyberte **Real-time endpoints** z navigační nabídky.

    ![Vytvořte endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.cs.png)

1. Vyberte **Create**.

1. Vyberte registrovaný model, který jste vytvořili.

    ![Vyberte registrovaný model.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.cs.png)

1. Vyberte **Select**.

1. Proveďte následující kroky:

    - Nastavte **Virtual machine** na *Standard_NC6s_v3*.
    - Nastavte **Instance count** podle potřeby, například *1*.
    - Nastavte **Endpoint** na **New** pro vytvoření endpointu.
    - Zadejte **Endpoint name**. Musí to být unikátní hodnota.
    - Zadejte **Deployment name**. Musí to být unikátní hodnota.

    ![Vyplňte nastavení nasazení.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.cs.png)

1. Vyberte **Deploy**.

> [!WARNING]
> Aby nedošlo k dodatečným poplatkům na vašem účtu, nezapomeňte odstranit vytvořený endpoint v Azure Machine Learning workspace.
>

#### Zkontrolujte stav nasazení v Azure Machine Learning Workspace

1. Přejděte do Azure Machine Learning workspace, který jste vytvořili.

1. Vyberte **Endpoints** z levého panelu.

1. Vyberte endpoint, který jste vytvořili.

    ![Vyberte endpointy](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.cs.png)

1. Na této stránce můžete spravovat endpointy během procesu nasazení.

> [!NOTE]
> Po dokončení nasazení se ujistěte, že **Live traffic** je nastaveno na **100%**. Pokud není, vyberte **Update traffic** pro úpravu nastavení provozu. Všimněte si, že model nelze testovat, pokud je provoz nastaven na 0%.
>
> ![Nastavte provoz.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.cs.png)
>
![Zkopírujte klíč API a URI koncového bodu.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.cs.png)

#### Přidání vlastního připojení

1. Navštivte [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Přejděte na projekt Azure AI Foundry, který jste vytvořili.

1. V projektu, který jste vytvořili, vyberte **Nastavení** z levého panelu.

1. Zvolte **+ Nové připojení**.

    ![Vyberte nové připojení.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.cs.png)

1. Vyberte **Vlastní klíče** z navigačního menu.

    ![Vyberte vlastní klíče.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.cs.png)

1. Proveďte následující kroky:

    - Vyberte **+ Přidat dvojici klíč-hodnota**.
    - Do pole pro název klíče zadejte **endpoint** a vložte URI koncového bodu, které jste zkopírovali z Azure ML Studio, do pole pro hodnotu.
    - Opět vyberte **+ Přidat dvojici klíč-hodnota**.
    - Do pole pro název klíče zadejte **key** a vložte klíč, který jste zkopírovali z Azure ML Studio, do pole pro hodnotu.
    - Po přidání klíčů zvolte **je tajné**, aby byl klíč skrytý.

    ![Přidání připojení.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.cs.png)

1. Zvolte **Přidat připojení**.

#### Vytvoření Prompt flow

Přidali jste vlastní připojení v Azure AI Foundry. Nyní vytvoříme Prompt flow pomocí následujících kroků. Poté připojíte tento Prompt flow k vlastnímu připojení, abyste mohli v Prompt flow využít model upravený na míru.

1. Přejděte na projekt Azure AI Foundry, který jste vytvořili.

1. Vyberte **Prompt flow** z levého panelu.

1. Zvolte **+ Vytvořit** z navigačního menu.

    ![Vyberte Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.cs.png)

1. Vyberte **Chat flow** z navigačního menu.

    ![Vyberte typ toku.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.cs.png)

1. Zadejte **Název složky**, kterou chcete použít.

    ![Zadejte název.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.cs.png)

2. Vyberte **Vytvořit**.

#### Nastavení Prompt flow pro komunikaci s vlastním modelem Phi-3

Je potřeba integrovat upravený model Phi-3 do Prompt flow. Stávající Prompt flow však není navržen pro tento účel. Proto je nutné Prompt flow přepracovat, aby bylo možné integrovat vlastní model.

1. V Prompt flow proveďte následující kroky pro přestavbu stávajícího toku:

    - Vyberte **Režim syrového souboru**.
    - Odstraňte veškerý stávající kód v souboru *flow.dag.yml*.
    - Přidejte následující kód do souboru *flow.dag.yml*.

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

    - Vyberte **Uložit**.

    ![Vyberte režim syrového souboru.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.cs.png)

1. Přidejte následující kód do souboru *integrate_with_promptflow.py*, abyste mohli použít vlastní model Phi-3 v Prompt flow.

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

    ![Vložte kód Prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.cs.png)

> [!NOTE]
> Pro podrobnější informace o používání Prompt flow v Azure AI Foundry můžete navštívit [Prompt flow v Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Vyberte **Chat input**, **Chat output**, abyste povolili komunikaci s modelem.

    ![Vstup a výstup.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.cs.png)

1. Nyní jste připraveni komunikovat s vlastním modelem Phi-3. V další cvičení se naučíte, jak spustit Prompt flow a použít jej ke komunikaci s upraveným modelem Phi-3.

> [!NOTE]
>
> Přestavěný tok by měl vypadat jako na obrázku níže:
>
> ![Příklad toku.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.cs.png)
>

### Komunikace s vlastním modelem Phi-3

Nyní, když jste upravili a integrovali vlastní model Phi-3 s Prompt flow, jste připraveni začít s ním komunikovat. Toto cvičení vás provede procesem nastavení a spuštění konverzace s vaším modelem pomocí Prompt flow. Díky těmto krokům budete moci plně využít schopnosti svého upraveného modelu Phi-3 pro různé úkoly a konverzace.

- Komunikujte s vlastním modelem Phi-3 pomocí Prompt flow.

#### Spuštění Prompt flow

1. Vyberte **Spustit výpočetní relace**, abyste spustili Prompt flow.

    ![Spustit výpočetní relaci.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.cs.png)

1. Vyberte **Ověřit a analyzovat vstup**, abyste obnovili parametry.

    ![Ověřit vstup.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.cs.png)

1. Vyberte **Hodnotu** připojení k vlastnímu připojení, které jste vytvořili. Například *connection*.

    ![Připojení.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.cs.png)

#### Komunikace s vlastním modelem

1. Vyberte **Chat**.

    ![Vyberte chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.cs.png)

1. Zde je příklad výsledků: Nyní můžete komunikovat s vlastním modelem Phi-3. Doporučuje se pokládat otázky na základě dat použitých pro jemné doladění.

    ![Chat s Prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.cs.png)

**Prohlášení**:  
Tento dokument byl přeložen pomocí strojových AI překladatelských služeb. Ačkoli se snažíme o přesnost, mějte prosím na paměti, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Nezodpovídáme za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.