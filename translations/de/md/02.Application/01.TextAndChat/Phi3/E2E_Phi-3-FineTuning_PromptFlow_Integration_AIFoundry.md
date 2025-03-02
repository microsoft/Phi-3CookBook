# Feinabstimmung und Integration benutzerdefinierter Phi-3-Modelle mit Prompt Flow in Azure AI Foundry

Dieses End-to-End (E2E)-Beispiel basiert auf der Anleitung "[Feinabstimmung und Integration benutzerdefinierter Phi-3-Modelle mit Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" aus der Microsoft Tech Community. Es zeigt die Prozesse der Feinabstimmung, Bereitstellung und Integration benutzerdefinierter Phi-3-Modelle mit Prompt Flow in Azure AI Foundry.
Im Gegensatz zum E2E-Beispiel "[Feinabstimmung und Integration benutzerdefinierter Phi-3-Modelle mit Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", das die lokale Ausführung von Code beinhaltete, konzentriert sich dieses Tutorial vollständig auf die Feinabstimmung und Integration Ihres Modells innerhalb des Azure AI / ML Studios.

## Übersicht

In diesem E2E-Beispiel lernen Sie, wie Sie das Phi-3-Modell feinabstimmen und mit Prompt Flow in Azure AI Foundry integrieren. Durch die Nutzung des Azure AI / ML Studios erstellen Sie einen Workflow zur Bereitstellung und Nutzung benutzerdefinierter KI-Modelle. Dieses E2E-Beispiel ist in drei Szenarien unterteilt:

**Szenario 1: Azure-Ressourcen einrichten und Vorbereitung zur Feinabstimmung**

**Szenario 2: Feinabstimmung des Phi-3-Modells und Bereitstellung im Azure Machine Learning Studio**

**Szenario 3: Integration mit Prompt Flow und Interaktion mit Ihrem benutzerdefinierten Modell in Azure AI Foundry**

Hier ist eine Übersicht über dieses E2E-Beispiel.

![Phi-3-FineTuning_PromptFlow_Integration Übersicht.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.de.png)

### Inhaltsverzeichnis

1. **[Szenario 1: Azure-Ressourcen einrichten und Vorbereitung zur Feinabstimmung](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Erstellen eines Azure Machine Learning Workspaces](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Anfordern von GPU-Kontingenten im Azure-Abonnement](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Rollen zuweisen](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Projekt einrichten](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Datensatz für die Feinabstimmung vorbereiten](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Szenario 2: Feinabstimmung des Phi-3-Modells und Bereitstellung im Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Phi-3-Modell feinabstimmen](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Bereitstellen des feinabgestimmten Phi-3-Modells](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Szenario 3: Integration mit Prompt Flow und Interaktion mit Ihrem benutzerdefinierten Modell in Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Integration des benutzerdefinierten Phi-3-Modells mit Prompt Flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Interaktion mit Ihrem benutzerdefinierten Phi-3-Modell](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Szenario 1: Azure-Ressourcen einrichten und Vorbereitung zur Feinabstimmung

### Erstellen eines Azure Machine Learning Workspaces

1. Geben Sie *azure machine learning* in die **Suchleiste** oben auf der Portalseite ein und wählen Sie **Azure Machine Learning** aus den angezeigten Optionen aus.

    ![Geben Sie azure machine learning ein.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.de.png)

2. Wählen Sie **+ Erstellen** aus dem Navigationsmenü.

3. Wählen Sie **Neuen Workspace** aus dem Navigationsmenü.

    ![Neuen Workspace auswählen.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.de.png)

4. Führen Sie die folgenden Schritte aus:

    - Wählen Sie Ihr Azure **Abonnement**.
    - Wählen Sie die zu verwendende **Ressourcengruppe** (erstellen Sie bei Bedarf eine neue).
    - Geben Sie einen **Workspacename** ein. Dieser muss eindeutig sein.
    - Wählen Sie die **Region**, die Sie verwenden möchten.
    - Wählen Sie das zu verwendende **Speicherkonto** (erstellen Sie bei Bedarf ein neues).
    - Wählen Sie den zu verwendenden **Key Vault** (erstellen Sie bei Bedarf einen neuen).
    - Wählen Sie die zu verwendenden **Application Insights** (erstellen Sie bei Bedarf neue).
    - Wählen Sie die zu verwendende **Container Registry** (erstellen Sie bei Bedarf eine neue).

    ![Azure Machine Learning ausfüllen.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.de.png)

5. Wählen Sie **Überprüfen + Erstellen**.

6. Wählen Sie **Erstellen**.

### Anfordern von GPU-Kontingenten im Azure-Abonnement

In diesem Tutorial lernen Sie, wie Sie ein Phi-3-Modell mit GPUs feinabstimmen und bereitstellen. Für die Feinabstimmung verwenden Sie die GPU *Standard_NC24ads_A100_v4*, die ein Kontingentantrag erfordert. Für die Bereitstellung verwenden Sie die GPU *Standard_NC6s_v3*, die ebenfalls ein Kontingentantrag erfordert.

> [!NOTE]
>
> Nur Pay-As-You-Go-Abonnements (der Standardabonnementtyp) sind für die GPU-Zuweisung berechtigt; Vorteil-Abonnements werden derzeit nicht unterstützt.
>

1. Besuchen Sie [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Führen Sie die folgenden Schritte aus, um ein Kontingent für die *Standard NCADSA100v4 Family* zu beantragen:

    - Wählen Sie **Kontingent** aus dem linken Tab.
    - Wählen Sie die zu verwendende **Virtuelle Maschinenfamilie** aus. Zum Beispiel **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, die die GPU *Standard_NC24ads_A100_v4* enthält.
    - Wählen Sie **Kontingent beantragen** aus dem Navigationsmenü.

        ![Kontingent beantragen.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.de.png)

    - Geben Sie auf der Seite "Kontingent beantragen" die gewünschte neue **Kernanzahl** ein. Zum Beispiel 24.
    - Wählen Sie **Senden**, um das GPU-Kontingent zu beantragen.

1. Führen Sie die folgenden Schritte aus, um ein Kontingent für die *Standard NCSv3 Family* zu beantragen:

    - Wählen Sie **Kontingent** aus dem linken Tab.
    - Wählen Sie die zu verwendende **Virtuelle Maschinenfamilie** aus. Zum Beispiel **Standard NCSv3 Family Cluster Dedicated vCPUs**, die die GPU *Standard_NC6s_v3* enthält.
    - Wählen Sie **Kontingent beantragen** aus dem Navigationsmenü.
    - Geben Sie auf der Seite "Kontingent beantragen" die gewünschte neue **Kernanzahl** ein. Zum Beispiel 24.
    - Wählen Sie **Senden**, um das GPU-Kontingent zu beantragen.

### Rollen zuweisen

Um Ihre Modelle feinabzustimmen und bereitzustellen, müssen Sie zunächst eine Benutzerzugewiesene Verwaltete Identität (UAI) erstellen und ihr die entsprechenden Berechtigungen zuweisen. Diese UAI wird während der Bereitstellung für die Authentifizierung verwendet.

#### Benutzerzugewiesene Verwaltete Identität (UAI) erstellen

1. Geben Sie *verwaltete Identitäten* in die **Suchleiste** oben auf der Portalseite ein und wählen Sie **Verwaltete Identitäten** aus den angezeigten Optionen aus.

    ![Verwaltete Identitäten eingeben.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.de.png)

1. Wählen Sie **+ Erstellen**.

    ![Erstellen auswählen.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.de.png)

1. Führen Sie die folgenden Schritte aus:

    - Wählen Sie Ihr Azure **Abonnement**.
    - Wählen Sie die zu verwendende **Ressourcengruppe** (erstellen Sie bei Bedarf eine neue).
    - Wählen Sie die **Region**, die Sie verwenden möchten.
    - Geben Sie den **Namen** ein. Dieser muss eindeutig sein.

    ![Erstellen auswählen.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.de.png)

1. Wählen Sie **Überprüfen + Erstellen**.

1. Wählen Sie **+ Erstellen**.

#### Rolle "Mitwirkender" für verwaltete Identität zuweisen

1. Navigieren Sie zur Ressource der verwalteten Identität, die Sie erstellt haben.

1. Wählen Sie **Azure-Rollen zuweisen** aus dem linken Tab.

1. Wählen Sie **+ Rolle zuweisen** aus dem Navigationsmenü.

1. Führen Sie auf der Seite "Rolle zuweisen" die folgenden Schritte aus:
    - Wählen Sie den **Bereich** **Ressourcengruppe** aus.
    - Wählen Sie Ihr Azure **Abonnement**.
    - Wählen Sie die zu verwendende **Ressourcengruppe**.
    - Wählen Sie die **Rolle** **Mitwirkender**.

    ![Mitwirkender-Rolle ausfüllen.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.de.png)

2. Wählen Sie **Speichern**.

#### Rolle "Storage Blob Data Reader" für verwaltete Identität zuweisen

1. Geben Sie *Speicherkonten* in die **Suchleiste** oben auf der Portalseite ein und wählen Sie **Speicherkonten** aus den angezeigten Optionen aus.

    ![Speicherkonten eingeben.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.de.png)

1. Wählen Sie das Speicherkonto aus, das mit dem Azure Machine Learning Workspace verknüpft ist, den Sie erstellt haben. Zum Beispiel *finetunephistorage*.

1. Führen Sie die folgenden Schritte aus, um zur Seite "Rolle zuweisen" zu gelangen:

    - Navigieren Sie zum Azure-Speicherkonto, das Sie erstellt haben.
    - Wählen Sie **Zugriffssteuerung (IAM)** aus dem linken Tab.
    - Wählen Sie **+ Hinzufügen** aus dem Navigationsmenü.
    - Wählen Sie **Rolle hinzufügen** aus dem Navigationsmenü.

    ![Rolle hinzufügen.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.de.png)

1. Führen Sie auf der Seite "Rolle zuweisen" die folgenden Schritte aus:

    - Geben Sie im Abschnitt "Rolle" *Storage Blob Data Reader* in die **Suchleiste** ein und wählen Sie **Storage Blob Data Reader** aus den angezeigten Optionen aus.
    - Wählen Sie **Weiter**.
    - Wählen Sie im Abschnitt "Mitglieder" **Zugriff zuweisen an** **Verwaltete Identität**.
    - Wählen Sie **+ Mitglieder auswählen**.
    - Wählen Sie im Abschnitt "Verwaltete Identitäten auswählen" Ihr Azure **Abonnement** aus.
    - Wählen Sie die **Verwaltete Identität** aus, die Sie erstellt haben. Zum Beispiel *finetunephi-managedidentity*.
    - Wählen Sie **Auswählen**.

    ![Verwaltete Identität auswählen.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.de.png)

1. Wählen Sie **Überprüfen + Zuweisen**.

#### Rolle "AcrPull" für verwaltete Identität zuweisen

1. Geben Sie *Containerregistrierungen* in die **Suchleiste** oben auf der Portalseite ein und wählen Sie **Containerregistrierungen** aus den angezeigten Optionen aus.

    ![Containerregistrierungen eingeben.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.de.png)

1. Wählen Sie die Containerregistrierung aus, die mit dem Azure Machine Learning Workspace verknüpft ist. Zum Beispiel *finetunephicontainerregistry*.

1. Führen Sie die folgenden Schritte aus, um zur Seite "Rolle zuweisen" zu gelangen:

    - Wählen Sie **Zugriffssteuerung (IAM)** aus dem linken Tab.
    - Wählen Sie **+ Hinzufügen** aus dem Navigationsmenü.
    - Wählen Sie **Rolle hinzufügen** aus dem Navigationsmenü.

1. Führen Sie auf der Seite "Rolle zuweisen" die folgenden Schritte aus:

    - Geben Sie im Abschnitt "Rolle" *AcrPull* in die **Suchleiste** ein und wählen Sie **AcrPull** aus den angezeigten Optionen aus.
    - Wählen Sie **Weiter**.
    - Wählen Sie im Abschnitt "Mitglieder" **Zugriff zuweisen an** **Verwaltete Identität**.
    - Wählen Sie **+ Mitglieder auswählen**.
    - Wählen Sie im Abschnitt "Verwaltete Identitäten auswählen" Ihr Azure **Abonnement** aus.
    - Wählen Sie die **Verwaltete Identität** aus, die Sie erstellt haben. Zum Beispiel *finetunephi-managedidentity*.
    - Wählen Sie **Auswählen**.
    - Wählen Sie **Überprüfen + Zuweisen**.

### Projekt einrichten

Um die für die Feinabstimmung erforderlichen Datensätze herunterzuladen, richten Sie eine lokale Umgebung ein.

In dieser Übung werden Sie:

- Einen Ordner erstellen, um darin zu arbeiten.
- Eine virtuelle Umgebung erstellen.
- Die erforderlichen Pakete installieren.
- Eine Datei *download_dataset.py* erstellen, um den Datensatz herunterzuladen.

#### Ordner erstellen

1. Öffnen Sie ein Terminalfenster und geben Sie den folgenden Befehl ein, um einen Ordner mit dem Namen *finetune-phi* im Standardpfad zu erstellen.

    ```console
    mkdir finetune-phi
    ```

2. Geben Sie den folgenden Befehl in Ihr Terminal ein, um in den erstellten Ordner *finetune-phi* zu wechseln.

    ```console
    cd finetune-phi
    ```

#### Virtuelle Umgebung erstellen

1. Geben Sie den folgenden Befehl in Ihr Terminal ein, um eine virtuelle Umgebung mit dem Namen *.venv* zu erstellen.

    ```console
    python -m venv .venv
    ```

2. Geben Sie den folgenden Befehl in Ihr Terminal ein, um die virtuelle Umgebung zu aktivieren.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
> Wenn es funktioniert hat, sollten Sie *(.venv)* vor der Eingabeaufforderung sehen.

#### Erforderliche Pakete installieren

1. Geben Sie die folgenden Befehle in Ihr Terminal ein, um die erforderlichen Pakete zu installieren.

    ```console
    pip install datasets==2.19.1
    ```

#### `download_dataset.py` erstellen

> [!NOTE]
> Vollständige Ordnerstruktur:
>
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Öffnen Sie **Visual Studio Code**.

1. Wählen Sie **Datei** aus der Menüleiste.

1. Wählen Sie **Ordner öffnen**.

1. Wählen Sie den erstellten Ordner *finetune-phi* aus, der sich unter *C:\Users\IhrBenutzername\finetune-phi* befindet.

    ![Wählen Sie den erstellten Ordner aus.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.de.png)

1. Klicken Sie im linken Bereich von Visual Studio Code mit der rechten Maustaste und wählen Sie **Neue Datei**, um eine neue Datei mit dem Namen *download_dataset.py* zu erstellen.

    ![Neue Datei erstellen.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.de.png)

### Datensatz für die Feinabstimmung vorbereiten

In dieser Übung führen Sie die Datei *download_dataset.py* aus, um die Datensätze *ultrachat_200k* in Ihre lokale Umgebung herunterzuladen. Anschließend verwenden Sie diese Datensätze, um das Phi-3-Modell im Azure Machine Learning feinabzustimmen.

In dieser Übung werden Sie:

- Code zur Datei *download_dataset.py* hinzufügen, um die Datensätze herunterzuladen.
- Die Datei *download_dataset.py* ausführen, um die Datensätze in Ihre lokale Umgebung herunterzuladen.

#### Datensatz mit *download_dataset.py* herunterladen

1. Öffnen Sie die Datei *download_dataset.py* in Visual Studio Code.

1. Fügen Sie den folgenden Code in die Datei *download_dataset.py* ein.

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

1. Geben Sie den folgenden Befehl in Ihr Terminal ein, um das Skript auszuführen und den Datensatz in Ihre lokale Umgebung herunterzuladen.

    ```console
    python download_dataset.py
    ```

1. Überprüfen Sie, ob die Datensätze erfolgreich im lokalen Verzeichnis *finetune-phi/data* gespeichert wurden.

> [!NOTE]
>
> #### Hinweis zur Datensatzgröße und Feinabstimmungszeit
>
> In diesem Tutorial verwenden Sie nur 1 % des Datensatzes (`split='train[:1%]'`). Dies reduziert die Datenmenge erheblich und beschleunigt sowohl den Upload- als auch den Feinabstimmungsprozess. Sie können den Prozentsatz anpassen, um das richtige Gleichgewicht zwischen Trainingszeit und Modell
1. Besuchen Sie [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Wählen Sie **Compute** aus der linken Seitenleiste.

1. Wählen Sie **Compute clusters** aus dem Navigationsmenü.

1. Wählen Sie **+ Neu**.

    ![Compute auswählen.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.de.png)

1. Führen Sie die folgenden Schritte aus:

    - Wählen Sie die gewünschte **Region** aus.
    - Setzen Sie die **Virtual machine tier** auf **Dedicated**.
    - Setzen Sie den **Virtual machine type** auf **GPU**.
    - Filtern Sie die **Virtual machine size** mit **Aus allen Optionen auswählen**.
    - Wählen Sie die **Virtual machine size** auf **Standard_NC24ads_A100_v4**.

    ![Cluster erstellen.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.de.png)

1. Wählen Sie **Weiter**.

1. Führen Sie die folgenden Schritte aus:

    - Geben Sie einen **Compute name** ein. Dieser muss eindeutig sein.
    - Setzen Sie die **Minimale Anzahl von Knoten** auf **0**.
    - Setzen Sie die **Maximale Anzahl von Knoten** auf **1**.
    - Setzen Sie die **Leerlaufzeit vor dem Herunterskalieren (Sekunden)** auf **120**.

    ![Cluster erstellen.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.de.png)

1. Wählen Sie **Erstellen**.

#### Feinabstimmung des Phi-3-Modells

1. Besuchen Sie [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Wählen Sie den Azure Machine Learning-Arbeitsbereich aus, den Sie erstellt haben.

    ![Arbeitsbereich auswählen.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.de.png)

1. Führen Sie die folgenden Schritte aus:

    - Wählen Sie **Model catalog** aus der linken Seitenleiste.
    - Geben Sie *phi-3-mini-4k* in die **Suchleiste** ein und wählen Sie **Phi-3-mini-4k-instruct** aus den angezeigten Optionen.

    ![phi-3-mini-4k eingeben.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.de.png)

1. Wählen Sie **Fine-tune** aus dem Navigationsmenü.

    ![Fine-tune auswählen.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.de.png)

1. Führen Sie die folgenden Schritte aus:

    - Setzen Sie **Aufgabentyp auswählen** auf **Chat completion**.
    - Wählen Sie **+ Daten auswählen**, um **Trainingsdaten** hochzuladen.
    - Setzen Sie den Typ für den Upload von Validierungsdaten auf **Unterschiedliche Validierungsdaten bereitstellen**.
    - Wählen Sie **+ Daten auswählen**, um **Validierungsdaten** hochzuladen.

    ![Seite für Feinabstimmung ausfüllen.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.de.png)

    > [!TIPP]
    >
    > Sie können **Erweiterte Einstellungen** auswählen, um Konfigurationen wie **learning_rate** und **lr_scheduler_type** anzupassen, um den Feinabstimmungsprozess optimal an Ihre spezifischen Anforderungen anzupassen.

1. Wählen Sie **Fertigstellen**.

1. In dieser Übung haben Sie das Phi-3-Modell erfolgreich mit Azure Machine Learning feinabgestimmt. Beachten Sie, dass der Feinabstimmungsprozess eine beträchtliche Zeit in Anspruch nehmen kann. Nach dem Start des Feinabstimmungsjobs müssen Sie warten, bis dieser abgeschlossen ist. Sie können den Status des Feinabstimmungsjobs überwachen, indem Sie im Azure Machine Learning-Arbeitsbereich auf die Registerkarte Jobs auf der linken Seite navigieren. In der nächsten Serie werden Sie das feinabgestimmte Modell bereitstellen und es mit Prompt Flow integrieren.

    ![Feinabstimmungsjob anzeigen.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.de.png)

### Bereitstellung des feinabgestimmten Phi-3-Modells

Um das feinabgestimmte Phi-3-Modell mit Prompt Flow zu integrieren, müssen Sie das Modell bereitstellen, damit es für Echtzeit-Inferenzen zugänglich ist. Dieser Prozess umfasst die Registrierung des Modells, das Erstellen eines Online-Endpunkts und die Bereitstellung des Modells.

In dieser Übung werden Sie:

- Das feinabgestimmte Modell im Azure Machine Learning-Arbeitsbereich registrieren.
- Einen Online-Endpunkt erstellen.
- Das registrierte feinabgestimmte Phi-3-Modell bereitstellen.

#### Registrierung des feinabgestimmten Modells

1. Besuchen Sie [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Wählen Sie den Azure Machine Learning-Arbeitsbereich aus, den Sie erstellt haben.

    ![Arbeitsbereich auswählen.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.de.png)

1. Wählen Sie **Modelle** aus der linken Seitenleiste.
1. Wählen Sie **+ Registrieren**.
1. Wählen Sie **Aus einem Job-Output**.

    ![Modell registrieren.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.de.png)

1. Wählen Sie den erstellten Job aus.

    ![Job auswählen.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.de.png)

1. Wählen Sie **Weiter**.

1. Setzen Sie **Modelltyp** auf **MLflow**.

1. Stellen Sie sicher, dass **Job-Output** ausgewählt ist; dies sollte automatisch geschehen.

    ![Output auswählen.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.de.png)

2. Wählen Sie **Weiter**.

3. Wählen Sie **Registrieren**.

    ![Registrieren auswählen.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.de.png)

4. Sie können Ihr registriertes Modell anzeigen, indem Sie im linken Menü auf **Modelle** navigieren.

    ![Registriertes Modell.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.de.png)

#### Bereitstellung des feinabgestimmten Modells

1. Navigieren Sie zum Azure Machine Learning-Arbeitsbereich, den Sie erstellt haben.

1. Wählen Sie **Endpunkte** aus der linken Seitenleiste.

1. Wählen Sie **Echtzeit-Endpunkte** aus dem Navigationsmenü.

    ![Endpunkt erstellen.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.de.png)

1. Wählen Sie **Erstellen**.

1. Wählen Sie das registrierte Modell aus, das Sie erstellt haben.

    ![Registriertes Modell auswählen.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.de.png)

1. Wählen Sie **Auswählen**.

1. Führen Sie die folgenden Schritte aus:

    - Setzen Sie **Virtuelle Maschine** auf *Standard_NC6s_v3*.
    - Wählen Sie die gewünschte **Anzahl der Instanzen** aus, z. B. *1*.
    - Setzen Sie den **Endpunkt** auf **Neu**, um einen neuen Endpunkt zu erstellen.
    - Geben Sie einen **Endpunktnamen** ein. Dieser muss eindeutig sein.
    - Geben Sie einen **Bereitstellungsnamen** ein. Dieser muss ebenfalls eindeutig sein.

    ![Bereitstellungseinstellungen ausfüllen.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.de.png)

1. Wählen Sie **Bereitstellen**.

> [!WARNUNG]
> Um zusätzliche Kosten für Ihr Konto zu vermeiden, löschen Sie den erstellten Endpunkt im Azure Machine Learning-Arbeitsbereich.
>

#### Überprüfen des Bereitstellungsstatus im Azure Machine Learning-Arbeitsbereich

1. Navigieren Sie zum Azure Machine Learning-Arbeitsbereich, den Sie erstellt haben.

1. Wählen Sie **Endpunkte** aus der linken Seitenleiste.

1. Wählen Sie den erstellten Endpunkt aus.

    ![Endpunkte auswählen.](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.de.png)

1. Auf dieser Seite können Sie die Endpunkte während des Bereitstellungsprozesses verwalten.

> [!HINWEIS]
> Sobald die Bereitstellung abgeschlossen ist, stellen Sie sicher, dass **Live-Traffic** auf **100%** gesetzt ist. Falls nicht, wählen Sie **Traffic aktualisieren**, um die Traffic-Einstellungen anzupassen. Beachten Sie, dass Sie das Modell nicht testen können, wenn der Traffic auf 0% gesetzt ist.
>
> ![Traffic einstellen.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.de.png)
>

## Szenario 3: Integration mit Prompt Flow und Interaktion mit Ihrem benutzerdefinierten Modell in Azure AI Foundry

### Integration des benutzerdefinierten Phi-3-Modells mit Prompt Flow

Nachdem Sie Ihr feinabgestimmtes Modell erfolgreich bereitgestellt haben, können Sie es nun mit Prompt Flow integrieren, um Ihr Modell in Echtzeitanwendungen zu verwenden und eine Vielzahl von interaktiven Aufgaben mit Ihrem benutzerdefinierten Phi-3-Modell zu ermöglichen.

In dieser Übung werden Sie:

- Einen Azure AI Foundry Hub erstellen.
- Ein Azure AI Foundry Projekt erstellen.
- Prompt Flow erstellen.
- Eine benutzerdefinierte Verbindung für das feinabgestimmte Phi-3-Modell hinzufügen.
- Prompt Flow einrichten, um mit Ihrem benutzerdefinierten Phi-3-Modell zu chatten.

> [!HINWEIS]
> Sie können auch mit Prompt Flow über Azure ML Studio integrieren. Der gleiche Integrationsprozess kann auf Azure ML Studio angewendet werden.

#### Azure AI Foundry Hub erstellen

Bevor Sie ein Projekt erstellen, müssen Sie einen Hub erstellen. Ein Hub funktioniert wie eine Ressourcengruppe, mit der Sie mehrere Projekte innerhalb von Azure AI Foundry organisieren und verwalten können.

1. Besuchen Sie [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Wählen Sie **Alle Hubs** aus der linken Seitenleiste.

1. Wählen Sie **+ Neuer Hub** aus dem Navigationsmenü.

    ![Hub erstellen.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.de.png)

1. Führen Sie die folgenden Schritte aus:

    - Geben Sie einen **Hub-Namen** ein. Dieser muss eindeutig sein.
    - Wählen Sie Ihr Azure **Abonnement**.
    - Wählen Sie die **Ressourcengruppe**, die Sie verwenden möchten (erstellen Sie eine neue, falls erforderlich).
    - Wählen Sie den gewünschten **Standort**.
    - Wählen Sie **Azure AI-Dienste verbinden** (erstellen Sie einen neuen, falls erforderlich).
    - Wählen Sie **Azure AI-Suche verbinden** und setzen Sie diese Option auf **Verbindung überspringen**.

    ![Hub ausfüllen.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.de.png)

1. Wählen Sie **Weiter**.

#### Azure AI Foundry Projekt erstellen

1. Wählen Sie in dem erstellten Hub **Alle Projekte** aus der linken Seitenleiste.

1. Wählen Sie **+ Neues Projekt** aus dem Navigationsmenü.

    ![Neues Projekt auswählen.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.de.png)

1. Geben Sie einen **Projektnamen** ein. Dieser muss eindeutig sein.

    ![Projekt erstellen.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.de.png)

1. Wählen Sie **Projekt erstellen**.

#### Benutzerdefinierte Verbindung für das feinabgestimmte Phi-3-Modell hinzufügen

Um Ihr benutzerdefiniertes Phi-3-Modell mit Prompt Flow zu integrieren, müssen Sie den Endpunkt und den Schlüssel des Modells in einer benutzerdefinierten Verbindung speichern. Diese Einrichtung gewährleistet den Zugriff auf Ihr benutzerdefiniertes Phi-3-Modell in Prompt Flow.

#### API-Schlüssel und Endpunkt-URI des feinabgestimmten Phi-3-Modells festlegen

1. Besuchen Sie [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Navigieren Sie zum Azure Machine Learning-Arbeitsbereich, den Sie erstellt haben.

1. Wählen Sie **Endpunkte** aus der linken Seitenleiste.

    ![Endpunkte auswählen.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.de.png)

1. Wählen Sie den erstellten Endpunkt aus.

    ![Endpunkt auswählen.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.de.png)

1. Wählen Sie **Verbrauchen** aus dem Navigationsmenü.

1. Kopieren Sie Ihre **REST-Endpunkt** und **Primärschlüssel**.
![API-Schlüssel und Endpunkt-URI kopieren.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.de.png)

#### Benutzerdefinierte Verbindung hinzufügen

1. Besuchen Sie [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Navigieren Sie zu dem Azure AI Foundry-Projekt, das Sie erstellt haben.

1. Wählen Sie im erstellten Projekt **Einstellungen** aus der linken Seitenleiste.

1. Wählen Sie **+ Neue Verbindung**.

    ![Neue Verbindung auswählen.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.de.png)

1. Wählen Sie **Benutzerdefinierte Schlüssel** aus dem Navigationsmenü.

    ![Benutzerdefinierte Schlüssel auswählen.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.de.png)

1. Führen Sie die folgenden Schritte aus:

    - Wählen Sie **+ Schlüssel-Wert-Paare hinzufügen**.
    - Geben Sie für den Schlüssel **endpoint** ein und fügen Sie den Endpunkt, den Sie aus Azure ML Studio kopiert haben, in das Wertfeld ein.
    - Wählen Sie erneut **+ Schlüssel-Wert-Paare hinzufügen**.
    - Geben Sie für den Schlüssel **key** ein und fügen Sie den Schlüssel, den Sie aus Azure ML Studio kopiert haben, in das Wertfeld ein.
    - Aktivieren Sie nach dem Hinzufügen der Schlüssel die Option **ist geheim**, um zu verhindern, dass der Schlüssel offengelegt wird.

    ![Verbindung hinzufügen.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.de.png)

1. Wählen Sie **Verbindung hinzufügen**.

#### Prompt Flow erstellen

Sie haben eine benutzerdefinierte Verbindung in Azure AI Foundry hinzugefügt. Nun erstellen wir einen Prompt Flow mit den folgenden Schritten. Anschließend verbinden Sie diesen Prompt Flow mit der benutzerdefinierten Verbindung, damit Sie das feinabgestimmte Modell im Prompt Flow nutzen können.

1. Navigieren Sie zu dem Azure AI Foundry-Projekt, das Sie erstellt haben.

1. Wählen Sie **Prompt Flow** aus der linken Seitenleiste.

1. Wählen Sie **+ Erstellen** aus dem Navigationsmenü.

    ![Prompt Flow auswählen.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.de.png)

1. Wählen Sie **Chat Flow** aus dem Navigationsmenü.

    ![Chat Flow auswählen.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.de.png)

1. Geben Sie einen **Ordnernamen** ein, der verwendet werden soll.

    ![Name eingeben.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.de.png)

2. Wählen Sie **Erstellen**.

#### Prompt Flow einrichten, um mit Ihrem benutzerdefinierten Phi-3-Modell zu chatten

Sie müssen das feinabgestimmte Phi-3-Modell in einen Prompt Flow integrieren. Der vorhandene Prompt Flow ist jedoch nicht für diesen Zweck ausgelegt. Daher müssen Sie den Prompt Flow neu gestalten, um die Integration des benutzerdefinierten Modells zu ermöglichen.

1. Führen Sie im Prompt Flow die folgenden Schritte aus, um den vorhandenen Flow neu zu erstellen:

    - Wählen Sie **Rohdateimodus**.
    - Löschen Sie den gesamten vorhandenen Code in der Datei *flow.dag.yml*.
    - Fügen Sie den folgenden Code in die Datei *flow.dag.yml* ein.

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

    - Wählen Sie **Speichern**.

    ![Rohdateimodus auswählen.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.de.png)

1. Fügen Sie den folgenden Code in die Datei *integrate_with_promptflow.py* ein, um das benutzerdefinierte Phi-3-Modell im Prompt Flow zu verwenden.

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

    ![Prompt Flow-Code einfügen.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.de.png)

> [!NOTE]
> Für detailliertere Informationen zur Verwendung von Prompt Flow in Azure AI Foundry können Sie [Prompt Flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) nachlesen.

1. Wählen Sie **Chat-Eingabe**, **Chat-Ausgabe**, um den Chat mit Ihrem Modell zu aktivieren.

    ![Eingabe und Ausgabe.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.de.png)

1. Nun können Sie mit Ihrem benutzerdefinierten Phi-3-Modell chatten. In der nächsten Übung lernen Sie, wie Sie Prompt Flow starten und es verwenden, um mit Ihrem feinabgestimmten Phi-3-Modell zu chatten.

> [!NOTE]
>
> Der neu gestaltete Flow sollte wie im Bild unten aussehen:
>
> ![Beispiel für den Flow.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.de.png)
>

### Chatten Sie mit Ihrem benutzerdefinierten Phi-3-Modell

Nachdem Sie Ihr benutzerdefiniertes Phi-3-Modell feinabgestimmt und in Prompt Flow integriert haben, können Sie nun mit der Interaktion beginnen. Diese Übung führt Sie durch den Prozess der Einrichtung und des Starts eines Chats mit Ihrem Modell mithilfe von Prompt Flow. Indem Sie diese Schritte befolgen, können Sie die Fähigkeiten Ihres feinabgestimmten Phi-3-Modells für verschiedene Aufgaben und Gespräche optimal nutzen.

- Chatten Sie mit Ihrem benutzerdefinierten Phi-3-Modell über Prompt Flow.

#### Prompt Flow starten

1. Wählen Sie **Computersitzungen starten**, um Prompt Flow zu starten.

    ![Computersitzung starten.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.de.png)

1. Wählen Sie **Eingabe validieren und analysieren**, um Parameter zu erneuern.

    ![Eingabe validieren.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.de.png)

1. Wählen Sie den **Wert** der **Verbindung** zu der von Ihnen erstellten benutzerdefinierten Verbindung. Zum Beispiel *connection*.

    ![Verbindung.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.de.png)

#### Mit Ihrem benutzerdefinierten Modell chatten

1. Wählen Sie **Chat**.

    ![Chat auswählen.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.de.png)

1. Hier ist ein Beispiel für die Ergebnisse: Nun können Sie mit Ihrem benutzerdefinierten Phi-3-Modell chatten. Es wird empfohlen, Fragen basierend auf den Daten zu stellen, die für das Fein-Tuning verwendet wurden.

    ![Chat mit Prompt Flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.de.png)

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe von KI-gestützten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.