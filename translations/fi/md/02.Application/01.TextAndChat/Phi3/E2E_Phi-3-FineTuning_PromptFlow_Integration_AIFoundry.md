# Hienosäätö ja mukautettujen Phi-3-mallien integrointi Prompt Flow'n avulla Azure AI Foundryssa

Tämä end-to-end (E2E) -esimerkki perustuu Microsoft Tech Community -oppaaseen "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)". Se esittelee prosessit mukautettujen Phi-3-mallien hienosäätöön, käyttöönottoon ja integrointiin Prompt Flow'n avulla Azure AI Foundryssa. Toisin kuin E2E-esimerkissä "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", jossa koodi suoritettiin paikallisesti, tämä opetus keskittyy pelkästään mallin hienosäätöön ja integrointiin Azure AI / ML Studiossa.

## Yleiskatsaus

Tässä E2E-esimerkissä opit hienosäätämään Phi-3-mallin ja integroimaan sen Prompt Flow'n kanssa Azure AI Foundryssa. Hyödyntämällä Azure AI / ML Studiota luot työnkulun mukautettujen AI-mallien käyttöönottoa ja hyödyntämistä varten. Tämä E2E-esimerkki on jaettu kolmeen skenaarioon:

**Skenaario 1: Azure-resurssien määrittäminen ja hienosäätöön valmistautuminen**

**Skenaario 2: Phi-3-mallin hienosäätö ja käyttöönotto Azure Machine Learning Studiossa**

**Skenaario 3: Integrointi Prompt Flow'n kanssa ja keskustelu mukautetun mallin kanssa Azure AI Foundryssa**

Alla on yleiskuvaus tästä E2E-esimerkistä.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.fi.png)

### Sisällysluettelo

1. **[Skenaario 1: Azure-resurssien määrittäminen ja hienosäätöön valmistautuminen](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Azure Machine Learning -työtilan luominen](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [GPU-kvottien pyytäminen Azure-tilauksessa](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Roolin määrityksen lisääminen](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Projektin määrittäminen](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Aineiston valmistelu hienosäätöä varten](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Skenaario 2: Phi-3-mallin hienosäätö ja käyttöönotto Azure Machine Learning Studiossa](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Phi-3-mallin hienosäätö](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Hienosäädetyn Phi-3-mallin käyttöönotto](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Skenaario 3: Integrointi Prompt Flow'n kanssa ja keskustelu mukautetun mallin kanssa Azure AI Foundryssa](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Mukautetun Phi-3-mallin integrointi Prompt Flow'n kanssa](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Keskustelu mukautetun Phi-3-mallin kanssa](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Skenaario 1: Azure-resurssien määrittäminen ja hienosäätöön valmistautuminen

### Azure Machine Learning -työtilan luominen

1. Kirjoita **azure machine learning** portaalin yläreunan **hakupalkkiin** ja valitse **Azure Machine Learning** näkyviin tulevista vaihtoehdoista.

    ![Kirjoita azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.fi.png)

2. Valitse navigointivalikosta **+ Luo**.

3. Valitse navigointivalikosta **Uusi työtila**.

    ![Valitse uusi työtila.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.fi.png)

4. Suorita seuraavat tehtävät:

    - Valitse Azure-tilauksesi **Subscription**.
    - Valitse käytettävä **Resource group** (luo uusi tarvittaessa).
    - Syötä **Workspace Name**. Sen on oltava yksilöllinen arvo.
    - Valitse käytettävä **Region**.
    - Valitse käytettävä **Storage account** (luo uusi tarvittaessa).
    - Valitse käytettävä **Key vault** (luo uusi tarvittaessa).
    - Valitse käytettävä **Application insights** (luo uusi tarvittaessa).
    - Valitse käytettävä **Container registry** (luo uusi tarvittaessa).

    ![Täytä azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.fi.png)

5. Valitse **Review + Create**.

6. Valitse **Create**.

### GPU-kvottien pyytäminen Azure-tilauksessa

Tässä opetusohjelmassa opit hienosäätämään ja ottamaan käyttöön Phi-3-mallin käyttämällä GPU:ta. Hienosäätöä varten käytät *Standard_NC24ads_A100_v4* GPU:ta, joka vaatii kvottipyynnön. Käyttöönottoa varten käytät *Standard_NC6s_v3* GPU:ta, joka myös vaatii kvottipyynnön.

> [!NOTE]
>
> Vain Pay-As-You-Go-tilaukset (standardi tilausmuoto) ovat oikeutettuja GPU-allokaatioon; etuusperusteiset tilaukset eivät tällä hetkellä ole tuettuja.
>

1. Siirry [Azure ML Studioon](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Suorita seuraavat tehtävät pyytääksesi *Standard NCADSA100v4 Family* -kvottaa:

    - Valitse vasemmanpuoleisesta välilehdestä **Quota**.
    - Valitse käytettävä **Virtual machine family**. Esimerkiksi valitse **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, joka sisältää *Standard_NC24ads_A100_v4* GPU:n.
    - Valitse navigointivalikosta **Request quota**.

        ![Pyydä kvottaa.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.fi.png)

    - Syötä Request quota -sivulle **New cores limit**, jota haluat käyttää. Esimerkiksi 24.
    - Valitse Request quota -sivulta **Submit** pyytääksesi GPU-kvottaa.

1. Suorita seuraavat tehtävät pyytääksesi *Standard NCSv3 Family* -kvottaa:

    - Valitse vasemmanpuoleisesta välilehdestä **Quota**.
    - Valitse käytettävä **Virtual machine family**. Esimerkiksi valitse **Standard NCSv3 Family Cluster Dedicated vCPUs**, joka sisältää *Standard_NC6s_v3* GPU:n.
    - Valitse navigointivalikosta **Request quota**.
    - Syötä Request quota -sivulle **New cores limit**, jota haluat käyttää. Esimerkiksi 24.
    - Valitse Request quota -sivulta **Submit** pyytääksesi GPU-kvottaa.

### Roolin määrityksen lisääminen

Jotta voit hienosäätää ja ottaa käyttöön mallejasi, sinun on ensin luotava User Assigned Managed Identity (UAI) ja annettava sille tarvittavat oikeudet. Tätä UAI:ta käytetään todennuksessa käyttöönoton aikana.

#### Luo User Assigned Managed Identity (UAI)

1. Kirjoita **managed identities** portaalin yläreunan **hakupalkkiin** ja valitse **Managed Identities** näkyviin tulevista vaihtoehdoista.

    ![Kirjoita managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.fi.png)

1. Valitse **+ Luo**.

    ![Valitse luo.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.fi.png)

1. Suorita seuraavat tehtävät:

    - Valitse Azure-tilauksesi **Subscription**.
    - Valitse käytettävä **Resource group** (luo uusi tarvittaessa).
    - Valitse käytettävä **Region**.
    - Syötä **Name**. Sen on oltava yksilöllinen arvo.

    ![Täytä managed identities.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.fi.png)

1. Valitse **Review + create**.

1. Valitse **+ Luo**.

#### Lisää Contributor-rooli Managed Identitylle

1. Siirry luomaasi Managed Identity -resurssiin.

1. Valitse vasemmanpuoleisesta välilehdestä **Azure role assignments**.

1. Valitse navigointivalikosta **+Add role assignment**.

1. Suorita Add role assignment -sivulla seuraavat tehtävät:
    - Valitse **Scope** kohdaksi **Resource group**.
    - Valitse Azure-tilauksesi **Subscription**.
    - Valitse käytettävä **Resource group**.
    - Valitse **Role** kohdaksi **Contributor**.

    ![Täytä Contributor-rooli.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.fi.png)

2. Valitse **Save**.

#### Lisää Storage Blob Data Reader -rooli Managed Identitylle

1. Kirjoita **storage accounts** portaalin yläreunan **hakupalkkiin** ja valitse **Storage accounts** näkyviin tulevista vaihtoehdoista.

    ![Kirjoita storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.fi.png)

1. Valitse Azure Machine Learning -työtilaan liitetty tallennustili. Esimerkiksi *finetunephistorage*.

1. Suorita seuraavat tehtävät navigoidaksesi Add role assignment -sivulle:

    - Siirry luomaasi Azure Storage -tiliin.
    - Valitse vasemmanpuoleisesta välilehdestä **Access Control (IAM)**.
    - Valitse navigointivalikosta **+ Add**.
    - Valitse navigointivalikosta **Add role assignment**.

    ![Lisää rooli.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.fi.png)

1. Suorita Add role assignment -sivulla seuraavat tehtävät:

    - Kirjoita Role-sivulla **Storage Blob Data Reader** hakupalkkiin ja valitse näkyviin tulevista vaihtoehdoista **Storage Blob Data Reader**.
    - Valitse Role-sivulla **Next**.
    - Valitse Members-sivulla **Assign access to** -kohdaksi **Managed identity**.
    - Valitse Members-sivulla **+ Select members**.
    - Valitse Select managed identities -sivulla Azure-tilauksesi **Subscription**.
    - Valitse Select managed identities -sivulla **Managed identity** kohdaksi **Manage Identity**.
    - Valitse Select managed identities -sivulla luomasi Managed Identity. Esimerkiksi *finetunephi-managedidentity*.
    - Valitse Select managed identities -sivulla **Select**.

    ![Valitse managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.fi.png)

1. Valitse **Review + assign**.

#### Lisää AcrPull-rooli Managed Identitylle

1. Kirjoita **container registries** portaalin yläreunan **hakupalkkiin** ja valitse **Container registries** näkyviin tulevista vaihtoehdoista.

    ![Kirjoita container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.fi.png)

1. Valitse Azure Machine Learning -työtilaan liitetty konttirekisteri. Esimerkiksi *finetunephicontainerregistry*.

1. Suorita seuraavat tehtävät navigoidaksesi Add role assignment -sivulle:

    - Valitse vasemmanpuoleisesta välilehdestä **Access Control (IAM)**.
    - Valitse navigointivalikosta **+ Add**.
    - Valitse navigointivalikosta **Add role assignment**.

1. Suorita Add role assignment -sivulla seuraavat tehtävät:

    - Kirjoita Role-sivulla **AcrPull** hakupalkkiin ja valitse näkyviin tulevista vaihtoehdoista **AcrPull**.
    - Valitse Role-sivulla **Next**.
    - Valitse Members-sivulla **Assign access to** -kohdaksi **Managed identity**.
    - Valitse Members-sivulla **+ Select members**.
    - Valitse Select managed identities -sivulla Azure-tilauksesi **Subscription**.
    - Valitse Select managed identities -sivulla **Managed identity** kohdaksi **Manage Identity**.
    - Valitse Select managed identities -sivulla luomasi Managed Identity. Esimerkiksi *finetunephi-managedidentity*.
    - Valitse Select managed identities -sivulla **Select**.
    - Valitse **Review + assign**.

### Projektin määrittäminen

Lataa hienosäätöön tarvittavat aineistot määrittämällä paikallinen ympäristö.

Tässä harjoituksessa:

- Luo kansio työskentelyä varten.
- Luo virtuaaliympäristö.
- Asenna tarvittavat paketit.
- Luo *download_dataset.py*-tiedosto aineiston lataamista varten.

#### Luo kansio työskentelyä varten

1. Avaa terminaali-ikkuna ja kirjoita seuraava komento luodaksesi kansion nimeltä *finetune-phi* oletuspolkuun.

    ```console
    mkdir finetune-phi
    ```

2. Kirjoita seuraava komento terminaaliisi siirtyäksesi luomaasi *finetune-phi*-kansioon.

    ```console
    cd finetune-phi
    ```

#### Luo virtuaaliympäristö

1. Kirjoita seuraava komento terminaaliisi luodaksesi virtuaaliympäristön nimeltä *.venv*.

    ```console
    python -m venv .venv
    ```

2. Kirjoita seuraava komento terminaaliisi aktivoidaksesi virtuaaliympäristön.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Jos kaikki toimii, näet *(.venv)* ennen komentokehotetta.

#### Asenna tarvittavat paketit

1. Kirjoita seuraavat komennot terminaaliisi asentaaksesi tarvittavat paketit.

    ```console
    pip install datasets==2.19.1
    ```

#### Luo `download_dataset.py`

> [!NOTE]
> Kansion täydellinen rakenne:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Avaa **Visual Studio Code**.

1. Valitse **File** valikkoriviltä.

1. Valitse **Open Folder**.

1. Valitse luomasi *finetune-phi*-kansio, joka sijaitsee polussa *C:\Users\yourUserName\finetune-phi*.

    ![Valitse luomasi kansio.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.fi.png)

1. Visual Studio Coden vasemmassa paneelissa napsauta hiiren kakkospainikkeella ja valitse **New File** luodaksesi uuden tiedoston nimeltä *download_dataset.py*.

    ![Luo uusi tiedosto.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.fi.png)

### Valmistele aineisto hienosäätöä varten

Tässä harjoituksessa suoritat *download_dataset.py*-tiedoston ladataksesi *ultrachat_200k*-aineistot paikalliseen ympäristöösi. Käytät näitä aineistoja Phi-3-mallin hienosäätöön Azure Machine Learningissa.

Tässä harjoituksessa:

- Lisää koodi *download_dataset.py*-tiedostoon aineistojen lataamista varten.
- Suorita *download_dataset.py*-tiedosto ladataksesi aineistot paikalliseen ympäristöösi.

#### Lataa aineisto käyttämällä *download_dataset.py*-tiedostoa

1. Avaa *download_dataset.py*-tiedosto Visual Studio Codessa.

1. Lisää seuraava koodi *download_dataset.py*-tiedostoon.

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

1. Kirjoita seuraava komento terminaaliisi suorittaaksesi skriptin ja ladataksesi aineiston paikalliseen ympäristöösi.

    ```console
    python download_dataset.py
    ```

1. Varmista, että aineistot tallentuivat onnistuneesti paikalliseen *finetune-phi/data*-hakemistoon.

> [!NOTE]
>
> #### Huomio aineiston koosta ja hienosäädön kestosta
>
> Tässä opetusohjelmassa käytät vain 1 % aineistosta (`split='train[:1%]'`). Tämä pienentää merkittävästi aineiston määrää, mikä nopeuttaa sekä lataus- että hienosäätöprosesseja. Voit säätää prosent
1. Vieraile [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Valitse vasemman puolen välilehdeltä **Compute**.

1. Valitse navigointivalikosta **Compute clusters**.

1. Valitse **+ New**.

    ![Valitse compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.fi.png)

1. Suorita seuraavat tehtävät:

    - Valitse **Region**, jota haluat käyttää.
    - Valitse **Virtual machine tier** kohtaan **Dedicated**.
    - Valitse **Virtual machine type** kohtaan **GPU**.
    - Valitse **Virtual machine size** -suodatin kohtaan **Select from all options**.
    - Valitse **Virtual machine size** kohtaan **Standard_NC24ads_A100_v4**.

    ![Luo klusteri.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.fi.png)

1. Valitse **Next**.

1. Suorita seuraavat tehtävät:

    - Syötä **Compute name**. Sen täytyy olla uniikki arvo.
    - Valitse **Minimum number of nodes** kohtaan **0**.
    - Valitse **Maximum number of nodes** kohtaan **1**.
    - Valitse **Idle seconds before scale down** kohtaan **120**.

    ![Luo klusteri.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.fi.png)

1. Valitse **Create**.

#### Phi-3-mallin hienosäätö

1. Vieraile [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Valitse Azure Machine Learning -työtila, jonka loit.

    ![Valitse luomasi työtila.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.fi.png)

1. Suorita seuraavat tehtävät:

    - Valitse vasemman puolen välilehdeltä **Model catalog**.
    - Kirjoita **phi-3-mini-4k** **hakupalkkiin** ja valitse **Phi-3-mini-4k-instruct** esiin tulevista vaihtoehdoista.

    ![Kirjoita phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.fi.png)

1. Valitse navigointivalikosta **Fine-tune**.

    ![Valitse fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.fi.png)

1. Suorita seuraavat tehtävät:

    - Valitse **Select task type** kohtaan **Chat completion**.
    - Valitse **+ Select data** ladataksesi **Traning data**.
    - Valitse Validation data -lataustyyppi kohtaan **Provide different validation data**.
    - Valitse **+ Select data** ladataksesi **Validation data**.

    ![Täytä hienosäätösivu.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.fi.png)

    > [!TIP]
    >
    > Voit valita **Advanced settings** mukauttaaksesi asetuksia, kuten **learning_rate** ja **lr_scheduler_type**, optimoidaksesi hienosäätöprosessin tarpeidesi mukaan.

1. Valitse **Finish**.

1. Tässä harjoituksessa hienosäädit onnistuneesti Phi-3-mallin Azure Machine Learningin avulla. Huomaa, että hienosäätöprosessi voi kestää huomattavan kauan. Kun hienosäätötyö on käynnissä, sinun täytyy odottaa sen valmistumista. Voit seurata hienosäätötyön tilaa siirtymällä Jobs-välilehdelle Azure Machine Learning -työtilassasi. Seuraavassa osassa mallisi otetaan käyttöön ja integroidaan Prompt flow -työkaluun.

    ![Katso hienosäätötyö.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.fi.png)

### Hienosäädetyn Phi-3-mallin käyttöönotto

Jotta hienosäädetty Phi-3-malli voidaan integroida Prompt flow -työkaluun, sinun täytyy ottaa malli käyttöön reaaliaikaista ennustamista varten. Tämä prosessi sisältää mallin rekisteröinnin, online-päätepisteen luomisen ja mallin käyttöönoton.

Tässä harjoituksessa:

- Rekisteröit hienosäädetyn mallin Azure Machine Learning -työtilassa.
- Luot online-päätepisteen.
- Otat rekisteröidyn hienosäädetyn Phi-3-mallin käyttöön.

#### Rekisteröi hienosäädetty malli

1. Vieraile [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Valitse Azure Machine Learning -työtila, jonka loit.

    ![Valitse luomasi työtila.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.fi.png)

1. Valitse vasemman puolen välilehdeltä **Models**.
1. Valitse **+ Register**.
1. Valitse **From a job output**.

    ![Rekisteröi malli.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.fi.png)

1. Valitse luomasi työ.

    ![Valitse työ.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.fi.png)

1. Valitse **Next**.

1. Valitse **Model type** kohtaan **MLflow**.

1. Varmista, että **Job output** on valittuna; sen pitäisi olla automaattisesti valittuna.

    ![Valitse ulostulo.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.fi.png)

2. Valitse **Next**.

3. Valitse **Register**.

    ![Valitse rekisteröi.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.fi.png)

4. Voit tarkastella rekisteröityä malliasi siirtymällä **Models**-valikkoon vasemman puolen välilehdeltä.

    ![Rekisteröity malli.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.fi.png)

#### Ota hienosäädetty malli käyttöön

1. Siirry Azure Machine Learning -työtilaan, jonka loit.

1. Valitse vasemman puolen välilehdeltä **Endpoints**.

1. Valitse navigointivalikosta **Real-time endpoints**.

    ![Luo päätepiste.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.fi.png)

1. Valitse **Create**.

1. Valitse rekisteröity malli, jonka loit.

    ![Valitse rekisteröity malli.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.fi.png)

1. Valitse **Select**.

1. Suorita seuraavat tehtävät:

    - Valitse **Virtual machine** kohtaan *Standard_NC6s_v3*.
    - Valitse **Instance count**, esimerkiksi *1*.
    - Valitse **Endpoint** kohtaan **New**, jotta luot uuden päätepisteen.
    - Syötä **Endpoint name**. Sen täytyy olla uniikki arvo.
    - Syötä **Deployment name**. Sen täytyy olla uniikki arvo.

    ![Täytä käyttöönottoasetukset.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.fi.png)

1. Valitse **Deploy**.

> [!WARNING]
> Välttääksesi lisäkustannuksia tililläsi, varmista, että poistat luodun päätepisteen Azure Machine Learning -työtilasta.
>

#### Tarkista käyttöönoton tila Azure Machine Learning -työtilassa

1. Siirry Azure Machine Learning -työtilaan, jonka loit.

1. Valitse vasemman puolen välilehdeltä **Endpoints**.

1. Valitse luomasi päätepiste.

    ![Valitse päätepisteet](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.fi.png)

1. Tällä sivulla voit hallita päätepisteitä käyttöönoton aikana.

> [!NOTE]
> Kun käyttöönotto on valmis, varmista, että **Live traffic** on asetettu **100%**. Jos ei, valitse **Update traffic** säätääksesi liikenteen asetuksia. Huomaa, että et voi testata mallia, jos liikenne on asetettu 0%.
>
> ![Aseta liikenne.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.fi.png)
>

## Tilanne 3: Integroi Prompt flow'n kanssa ja keskustele mukautetulla mallillasi Azure AI Foundryssä

### Integroi mukautettu Phi-3-malli Prompt flow'n kanssa

Kun olet onnistuneesti ottanut hienosäädetyn mallin käyttöön, voit nyt integroida sen Prompt flow -työkaluun käyttääksesi malliasi reaaliaikaisissa sovelluksissa. Tämä mahdollistaa erilaisia vuorovaikutteisia tehtäviä mukautetulla Phi-3-mallillasi.

Tässä harjoituksessa:

- Luo Azure AI Foundry Hub.
- Luo Azure AI Foundry Project.
- Luo Prompt flow.
- Lisää mukautettu yhteys hienosäädetylle Phi-3-mallille.
- Määritä Prompt flow keskustelemaan mukautetun Phi-3-mallisi kanssa.

> [!NOTE]
> Voit myös integroida Promptflow'n avulla Azure ML Studioon. Sama integrointiprosessi voidaan soveltaa Azure ML Studioon.

#### Luo Azure AI Foundry Hub

Sinun täytyy luoda Hub ennen kuin voit luoda Projectin. Hub toimii resurssiryhmänä, jonka avulla voit organisoida ja hallita useita projekteja Azure AI Foundryssä.

1. Vieraile [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Valitse vasemman puolen välilehdeltä **All hubs**.

1. Valitse navigointivalikosta **+ New hub**.

    ![Luo hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.fi.png)

1. Suorita seuraavat tehtävät:

    - Syötä **Hub name**. Sen täytyy olla uniikki arvo.
    - Valitse Azure **Subscription**.
    - Valitse **Resource group**, jota haluat käyttää (luo uusi, jos tarpeen).
    - Valitse **Location**, jota haluat käyttää.
    - Valitse **Connect Azure AI Services**, jota haluat käyttää (luo uusi, jos tarpeen).
    - Valitse **Connect Azure AI Search** kohtaan **Skip connecting**.

    ![Täytä hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.fi.png)

1. Valitse **Next**.

#### Luo Azure AI Foundry Project

1. Valitsemassasi Hubissa, valitse vasemman puolen välilehdeltä **All projects**.

1. Valitse navigointivalikosta **+ New project**.

    ![Valitse uusi projekti.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.fi.png)

1. Syötä **Project name**. Sen täytyy olla uniikki arvo.

    ![Luo projekti.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.fi.png)

1. Valitse **Create a project**.

#### Lisää mukautettu yhteys hienosäädetylle Phi-3-mallille

Jotta mukautettu Phi-3-mallisi voidaan integroida Prompt flow -työkaluun, sinun täytyy tallentaa mallin päätepiste ja avain mukautettuun yhteyteen. Tämä asetus varmistaa pääsyn mukautettuun Phi-3-malliisi Prompt flow'ssa.

#### Aseta hienosäädetyn Phi-3-mallin API-avain ja päätepisteen URI

1. Vieraile [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Siirry Azure Machine Learning -työtilaan, jonka loit.

1. Valitse vasemman puolen välilehdeltä **Endpoints**.

    ![Valitse päätepisteet.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.fi.png)

1. Valitse luomasi päätepiste.

    ![Valitse päätepisteet.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.fi.png)

1. Valitse navigointivalikosta **Consume**.

1. Kopioi **REST endpoint** ja **Primary key**.
![Kopioi API-avain ja päätepisteen URI.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.fi.png)

#### Lisää mukautettu yhteys

1. Siirry osoitteeseen [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Avaa luomasi Azure AI Foundry -projekti.

1. Valitse luomastasi projektista vasemman sivupalkin **Asetukset**.

1. Valitse **+ Uusi yhteys**.

    ![Valitse uusi yhteys.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.fi.png)

1. Valitse navigointivalikosta **Mukautetut avaimet**.

    ![Valitse mukautetut avaimet.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.fi.png)

1. Suorita seuraavat tehtävät:

    - Valitse **+ Lisää avain-arvopareja**.
    - Anna avaimen nimeksi **endpoint** ja liitä Azure ML Studiosta kopioitu päätepiste arvokenttään.
    - Valitse **+ Lisää avain-arvopareja** uudelleen.
    - Anna avaimen nimeksi **key** ja liitä Azure ML Studiosta kopioitu avain arvokenttään.
    - Valitse **on salainen**, jotta avain ei ole näkyvissä lisäyksen jälkeen.

    ![Lisää yhteys.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.fi.png)

1. Valitse **Lisää yhteys**.

#### Luo Prompt flow

Olet lisännyt mukautetun yhteyden Azure AI Foundryyn. Nyt luodaan Prompt flow seuraavien vaiheiden avulla. Lopuksi yhdistät tämän Prompt flown mukautettuun yhteyteen, jotta voit käyttää hienosäädettyä mallia Prompt flow'ssa.

1. Avaa luomasi Azure AI Foundry -projekti.

1. Valitse vasemman sivupalkin **Prompt flow**.

1. Valitse navigointivalikosta **+ Luo**.

    ![Valitse Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.fi.png)

1. Valitse navigointivalikosta **Chat flow**.

    ![Valitse chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.fi.png)

1. Anna **Kansio nimi**, jota haluat käyttää.

    ![Anna nimi.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.fi.png)

2. Valitse **Luo**.

#### Määritä Prompt flow keskustelemaan mukautetun Phi-3-mallisi kanssa

Sinun täytyy integroida hienosäädetty Phi-3-malli Prompt flow'hun. Nykyinen Prompt flow ei kuitenkaan ole suunniteltu tätä tarkoitusta varten, joten sinun täytyy muokata Prompt flow'ta, jotta mukautettu malli voidaan integroida.

1. Prompt flow'ssa suorita seuraavat tehtävät muokataksesi olemassa olevaa flow'ta:

    - Valitse **Raakatiedosto-tila**.
    - Poista kaikki olemassa oleva koodi *flow.dag.yml*-tiedostosta.
    - Lisää seuraava koodi *flow.dag.yml*-tiedostoon.

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

    - Valitse **Tallenna**.

    ![Valitse raakatiedosto-tila.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.fi.png)

1. Lisää seuraava koodi *integrate_with_promptflow.py*-tiedostoon, jotta voit käyttää mukautettua Phi-3-mallia Prompt flow'ssa.

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

    ![Liitä Prompt flow -koodi.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.fi.png)

> [!NOTE]
> Lisätietoja Prompt flow'n käytöstä Azure AI Foundryssa löydät täältä: [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Valitse **Chat input**, **Chat output**, jotta voit keskustella mallisi kanssa.

    ![Syöte ja tuloste.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.fi.png)

1. Nyt olet valmis keskustelemaan mukautetun Phi-3-mallisi kanssa. Seuraavassa harjoituksessa opit, kuinka käynnistät Prompt flow'n ja käytät sitä keskustellaksesi hienosäädetyn Phi-3-mallisi kanssa.

> [!NOTE]
>
> Muokattu flow näyttää tältä:
>
> ![Flow-esimerkki.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.fi.png)
>

### Keskustele mukautetun Phi-3-mallisi kanssa

Nyt kun olet hienosäätänyt ja integroinut mukautetun Phi-3-mallisi Prompt flow'hun, voit aloittaa sen käytön. Tämä harjoitus opastaa sinua, kuinka asennat ja aloitat keskustelun mallisi kanssa Prompt flow'n avulla. Näiden vaiheiden avulla voit hyödyntää hienosäädettyä Phi-3-malliasi monenlaisiin tehtäviin ja keskusteluihin.

- Keskustele mukautetun Phi-3-mallisi kanssa Prompt flow'n avulla.

#### Käynnistä Prompt flow

1. Valitse **Käynnistä laskentasessio** käynnistääksesi Prompt flow'n.

    ![Käynnistä laskentasessio.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.fi.png)

1. Valitse **Vahvista ja jäsennä syöte** päivittääksesi parametrit.

    ![Vahvista syöte.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.fi.png)

1. Valitse **Yhteyden** arvo, joka vastaa luomaasi mukautettua yhteyttä. Esimerkiksi *connection*.

    ![Yhteys.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.fi.png)

#### Keskustele mukautetun mallisi kanssa

1. Valitse **Chat**.

    ![Valitse chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.fi.png)

1. Tässä esimerkki tuloksista: Nyt voit keskustella mukautetun Phi-3-mallisi kanssa. On suositeltavaa esittää kysymyksiä mallin hienosäätämiseen käytetyn datan pohjalta.

    ![Keskustele Prompt flow'n kanssa.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.fi.png)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisilla tekoälyyn perustuvilla käännöspalveluilla. Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulisi pitää ensisijaisena lähteenä. Kriittistä tietoa varten suositellaan ammattimaista ihmisen tekemää käännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.