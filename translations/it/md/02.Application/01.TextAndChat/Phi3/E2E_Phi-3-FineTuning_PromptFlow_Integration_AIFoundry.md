# Perfeziona e integra modelli personalizzati Phi-3 con Prompt Flow in Azure AI Foundry

Questo esempio end-to-end (E2E) si basa sulla guida "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" della Microsoft Tech Community. Introduce i processi di perfezionamento, distribuzione e integrazione di modelli personalizzati Phi-3 con Prompt Flow in Azure AI Foundry.  
A differenza dell'esempio E2E, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", che prevedeva l'esecuzione del codice in locale, questo tutorial si concentra interamente sul perfezionamento e l'integrazione del modello all'interno di Azure AI / ML Studio.

## Panoramica

In questo esempio E2E, imparerai a perfezionare il modello Phi-3 e integrarlo con Prompt Flow in Azure AI Foundry. Sfruttando Azure AI / ML Studio, stabilirai un flusso di lavoro per distribuire e utilizzare modelli AI personalizzati. Questo esempio E2E è suddiviso in tre scenari:

**Scenario 1: Configurare le risorse di Azure e prepararsi per il perfezionamento**

**Scenario 2: Perfezionare il modello Phi-3 e distribuirlo in Azure Machine Learning Studio**

**Scenario 3: Integrare con Prompt Flow e interagire con il tuo modello personalizzato in Azure AI Foundry**

Ecco una panoramica di questo esempio E2E.

![Panoramica FineTuning_PromptFlow_Integration.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.it.png)

### Indice

1. **[Scenario 1: Configurare le risorse di Azure e prepararsi per il perfezionamento](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
   - [Creare uno spazio di lavoro di Azure Machine Learning](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
   - [Richiedere quote GPU nella sottoscrizione Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
   - [Aggiungere assegnazione di ruoli](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
   - [Impostare il progetto](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
   - [Preparare il dataset per il perfezionamento](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 2: Perfezionare il modello Phi-3 e distribuirlo in Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
   - [Perfezionare il modello Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
   - [Distribuire il modello Phi-3 perfezionato](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Scenario 3: Integrare con Prompt Flow e interagire con il tuo modello personalizzato in Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**  
   - [Integrare il modello personalizzato Phi-3 con Prompt Flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)  
   - [Interagire con il tuo modello personalizzato Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Scenario 1: Configurare le risorse di Azure e prepararsi per il perfezionamento

### Creare uno spazio di lavoro di Azure Machine Learning

1. Digita *azure machine learning* nella **barra di ricerca** in alto nella pagina del portale e seleziona **Azure Machine Learning** tra le opzioni che appaiono.

    ![Digita azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.it.png)

2. Seleziona **+ Crea** dal menu di navigazione.

3. Seleziona **Nuovo spazio di lavoro** dal menu di navigazione.

    ![Seleziona nuovo spazio di lavoro.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.it.png)

4. Esegui le seguenti operazioni:

    - Seleziona la tua **Sottoscrizione Azure**.  
    - Seleziona il **Gruppo di risorse** da utilizzare (creane uno nuovo, se necessario).  
    - Inserisci un **Nome dello spazio di lavoro** univoco.  
    - Seleziona la **Regione** da utilizzare.  
    - Seleziona l'**Account di archiviazione** da utilizzare (creane uno nuovo, se necessario).  
    - Seleziona il **Key vault** da utilizzare (creane uno nuovo, se necessario).  
    - Seleziona **Application Insights** da utilizzare (creane uno nuovo, se necessario).  
    - Seleziona il **Registro container** da utilizzare (creane uno nuovo, se necessario).  

    ![Compila i dettagli di Azure Machine Learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.it.png)

5. Seleziona **Rivedi + Crea**.

6. Seleziona **Crea**.

### Richiedere quote GPU nella sottoscrizione Azure

In questo tutorial, imparerai a perfezionare e distribuire un modello Phi-3 utilizzando GPU. Per il perfezionamento, utilizzerai la GPU *Standard_NC24ads_A100_v4*, che richiede una richiesta di quota. Per la distribuzione, utilizzerai la GPU *Standard_NC6s_v3*, che richiede anch'essa una richiesta di quota.

> [!NOTE]  
> Solo le sottoscrizioni Pay-As-You-Go (il tipo di sottoscrizione standard) sono idonee per l'allocazione GPU; le sottoscrizioni a beneficio non sono attualmente supportate.  

1. Visita [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Esegui le seguenti operazioni per richiedere la quota *Standard NCADSA100v4 Family*:

    - Seleziona **Quota** dalla barra laterale sinistra.  
    - Seleziona la **Famiglia di macchine virtuali** da utilizzare. Ad esempio, seleziona **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, che include la GPU *Standard_NC24ads_A100_v4*.  
    - Seleziona **Richiedi quota** dal menu di navigazione.  

        ![Richiedi quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.it.png)

    - Nella pagina Richiedi quota, inserisci il **Nuovo limite di core** desiderato. Ad esempio, 24.  
    - Nella pagina Richiedi quota, seleziona **Invia** per richiedere la quota GPU.

1. Esegui le seguenti operazioni per richiedere la quota *Standard NCSv3 Family*:

    - Seleziona **Quota** dalla barra laterale sinistra.  
    - Seleziona la **Famiglia di macchine virtuali** da utilizzare. Ad esempio, seleziona **Standard NCSv3 Family Cluster Dedicated vCPUs**, che include la GPU *Standard_NC6s_v3*.  
    - Seleziona **Richiedi quota** dal menu di navigazione.  
    - Nella pagina Richiedi quota, inserisci il **Nuovo limite di core** desiderato. Ad esempio, 24.  
    - Nella pagina Richiedi quota, seleziona **Invia** per richiedere la quota GPU.

### Aggiungere assegnazione di ruoli

Per perfezionare e distribuire i tuoi modelli, devi prima creare un'Identità Gestita Assegnata dall'Utente (UAI) e assegnarle i permessi appropriati. Questa UAI verrà utilizzata per l'autenticazione durante la distribuzione.

#### Creare un'Identità Gestita Assegnata dall'Utente (UAI)

1. Digita *managed identities* nella **barra di ricerca** in alto nella pagina del portale e seleziona **Managed Identities** tra le opzioni che appaiono.

    ![Digita managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.it.png)

1. Seleziona **+ Crea**.

    ![Seleziona crea.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.it.png)

1. Esegui le seguenti operazioni:

    - Seleziona la tua **Sottoscrizione Azure**.  
    - Seleziona il **Gruppo di risorse** da utilizzare (creane uno nuovo, se necessario).  
    - Seleziona la **Regione** da utilizzare.  
    - Inserisci un **Nome** univoco.  

    ![Compila i dettagli per l'identità gestita.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.it.png)

1. Seleziona **Rivedi + Crea**.

1. Seleziona **Crea**.

#### Aggiungere il ruolo di Contributor all'Identità Gestita

1. Vai alla risorsa di Identità Gestita che hai creato.

1. Seleziona **Assegnazioni di ruoli di Azure** dalla barra laterale sinistra.

1. Seleziona **+Aggiungi assegnazione di ruolo** dal menu di navigazione.

1. Nella pagina Aggiungi assegnazione di ruolo, esegui le seguenti operazioni:  
    - Seleziona l'**Ambito** come **Gruppo di risorse**.  
    - Seleziona la tua **Sottoscrizione Azure**.  
    - Seleziona il **Gruppo di risorse** da utilizzare.  
    - Seleziona il **Ruolo** come **Contributor**.  

    ![Compila i dettagli del ruolo di Contributor.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.it.png)

2. Seleziona **Salva**.

#### Aggiungere il ruolo di Storage Blob Data Reader all'Identità Gestita

1. Digita *storage accounts* nella **barra di ricerca** in alto nella pagina del portale e seleziona **Storage accounts** tra le opzioni che appaiono.

    ![Digita storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.it.png)

1. Seleziona l'account di archiviazione associato allo spazio di lavoro di Azure Machine Learning che hai creato. Ad esempio, *finetunephistorage*.  

1. Esegui le seguenti operazioni per navigare alla pagina Aggiungi assegnazione di ruolo:  
    - Vai all'account di archiviazione di Azure che hai creato.  
    - Seleziona **Controllo accessi (IAM)** dalla barra laterale sinistra.  
    - Seleziona **+ Aggiungi** dal menu di navigazione.  
    - Seleziona **Aggiungi assegnazione di ruolo** dal menu di navigazione.  

    ![Aggiungi ruolo.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.it.png)

1. Nella pagina Aggiungi assegnazione di ruolo, esegui le seguenti operazioni:  
    - Nella pagina Ruolo, digita *Storage Blob Data Reader* nella **barra di ricerca** e seleziona **Storage Blob Data Reader** tra le opzioni che appaiono.  
    - Nella pagina Ruolo, seleziona **Avanti**.  
    - Nella pagina Membri, seleziona **Assegna accesso a** **Identità gestita**.  
    - Nella pagina Membri, seleziona **+ Seleziona membri**.  
    - Nella pagina Seleziona identità gestite, seleziona la tua **Sottoscrizione Azure**.  
    - Nella pagina Seleziona identità gestite, seleziona l'**Identità gestita** che hai creato. Ad esempio, *finetunephi-managedidentity*.  
    - Nella pagina Seleziona identità gestite, seleziona **Seleziona**.  

    ![Seleziona identità gestita.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.it.png)

1. Seleziona **Rivedi + assegna**.

#### Aggiungere il ruolo di AcrPull all'Identità Gestita

1. Digita *container registries* nella **barra di ricerca** in alto nella pagina del portale e seleziona **Container registries** tra le opzioni che appaiono.

    ![Digita container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.it.png)

1. Seleziona il registro container associato allo spazio di lavoro di Azure Machine Learning. Ad esempio, *finetunephicontainerregistry*.  

1. Esegui le seguenti operazioni per navigare alla pagina Aggiungi assegnazione di ruolo:  
    - Seleziona **Controllo accessi (IAM)** dalla barra laterale sinistra.  
    - Seleziona **+ Aggiungi** dal menu di navigazione.  
    - Seleziona **Aggiungi assegnazione di ruolo** dal menu di navigazione.  

1. Nella pagina Aggiungi assegnazione di ruolo, esegui le seguenti operazioni:  
    - Nella pagina Ruolo, digita *AcrPull* nella **barra di ricerca** e seleziona **AcrPull** tra le opzioni che appaiono.  
    - Nella pagina Ruolo, seleziona **Avanti**.  
    - Nella pagina Membri, seleziona **Assegna accesso a** **Identità gestita**.  
    - Nella pagina Membri, seleziona **+ Seleziona membri**.  
    - Nella pagina Seleziona identità gestite, seleziona la tua **Sottoscrizione Azure**.  
    - Nella pagina Seleziona identità gestite, seleziona l'**Identità gestita** che hai creato. Ad esempio, *finetunephi-managedidentity*.  
    - Nella pagina Seleziona identità gestite, seleziona **Seleziona**.  
    - Seleziona **Rivedi + assegna**.

### Impostare il progetto

Per scaricare i dataset necessari per il perfezionamento, configurerai un ambiente locale.

In questo esercizio, eseguirai:  

- Creazione di una cartella di lavoro.  
- Creazione di un ambiente virtuale.  
- Installazione dei pacchetti necessari.  
- Creazione di un file *download_dataset.py* per scaricare il dataset.

#### Creare una cartella di lavoro

1. Apri una finestra del terminale e digita il seguente comando per creare una cartella chiamata *finetune-phi* nel percorso predefinito.

    ```console
    mkdir finetune-phi
    ```

2. Digita il seguente comando nel terminale per accedere alla cartella *finetune-phi* che hai creato.

    ```console
    cd finetune-phi
    ```

#### Creare un ambiente virtuale

1. Digita il seguente comando nel terminale per creare un ambiente virtuale chiamato *.venv*.

    ```console
    python -m venv .venv
    ```

2. Digita il seguente comando nel terminale per attivare l'ambiente virtuale.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]  
> Se ha funzionato, dovresti vedere *(.venv)* prima del prompt dei comandi.

#### Installare i pacchetti necessari

1. Digita i seguenti comandi nel terminale per installare i pacchetti richiesti.

    ```console
    pip install datasets==2.19.1
    ```

#### Creare `download_dataset.py`

> [!NOTE]  
> Struttura completa della cartella:  
> ```text
> └── YourUserName
> .    └── finetune-phi
> .        └── download_dataset.py
> ```

1. Apri **Visual Studio Code**.

1. Seleziona **File** dalla barra del menu.

1. Seleziona **Apri cartella**.

1. Seleziona la cartella *finetune-phi* che hai creato, situata in *C:\Users\yourUserName\finetune-phi*.

    ![Seleziona la cartella che hai creato.](../../../../../../translated_images/04-01-open-project-folder.01a82ecd87581d5a0572bc4f12dd8004a204ec366c907a2ad4d42dfd61ea5e21.it.png)

1. Nel riquadro sinistro di Visual Studio Code, fai clic con il tasto destro e seleziona **Nuovo File** per creare un nuovo file chiamato *download_dataset.py*.

    ![Crea un nuovo file.](../../../../../../translated_images/04-02-create-new-file.16e088bf7213c299e258482be49fb1c735ba3eca1503b38a6b45b9289c651732.it.png)

### Preparare il dataset per il perfezionamento

In questo esercizio, eseguirai il file *download_dataset.py* per scaricare i dataset *ultrachat_200k* nel tuo ambiente locale. Successivamente utilizzerai questi dataset per perfezionare il modello Phi-3 in Azure Machine Learning.

In questo esercizio, eseguirai:

- Aggiunta di codice al file *download_dataset.py* per scaricare i dataset.  
- Esecuzione del file *download_dataset.py* per scaricare i dataset nel tuo ambiente locale.

#### Scaricare il dataset usando *download_dataset.py*

1. Apri il file *download_dataset.py* in Visual Studio Code.

1. Aggiungi il seguente codice al file *download_dataset.py*.

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

1. Digita il seguente comando nel terminale per eseguire lo script e scaricare il dataset nel tuo ambiente locale.

    ```console
    python download_dataset.py
    ```

1. Verifica che i dataset siano
1. Visita [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Seleziona **Calcolo** dalla barra laterale sinistra.

1. Seleziona **Cluster di calcolo** dal menu di navigazione.

1. Seleziona **+ Nuovo**.

    ![Seleziona calcolo.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.it.png)

1. Esegui le seguenti operazioni:

    - Seleziona la **Regione** che desideri utilizzare.
    - Imposta il **Livello della macchina virtuale** su **Dedicato**.
    - Imposta il **Tipo di macchina virtuale** su **GPU**.
    - Filtra la **Dimensione della macchina virtuale** su **Seleziona da tutte le opzioni**.
    - Seleziona la **Dimensione della macchina virtuale** su **Standard_NC24ads_A100_v4**.

    ![Crea cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.it.png)

1. Seleziona **Avanti**.

1. Esegui le seguenti operazioni:

    - Inserisci il **Nome del calcolo**. Deve essere un valore univoco.
    - Imposta il **Numero minimo di nodi** su **0**.
    - Imposta il **Numero massimo di nodi** su **1**.
    - Imposta i **Secondi di inattività prima della riduzione scalare** su **120**.

    ![Crea cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.it.png)

1. Seleziona **Crea**.

#### Ottimizza il modello Phi-3

1. Visita [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Seleziona lo spazio di lavoro di Azure Machine Learning che hai creato.

    ![Seleziona lo spazio di lavoro creato.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.it.png)

1. Esegui le seguenti operazioni:

    - Seleziona **Catalogo modelli** dalla barra laterale sinistra.
    - Digita *phi-3-mini-4k* nella **barra di ricerca** e seleziona **Phi-3-mini-4k-instruct** dalle opzioni disponibili.

    ![Digita phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.it.png)

1. Seleziona **Ottimizza** dal menu di navigazione.

    ![Seleziona ottimizza.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.it.png)

1. Esegui le seguenti operazioni:

    - Imposta **Seleziona tipo di attività** su **Chat completion**.
    - Seleziona **+ Seleziona dati** per caricare i **Dati di addestramento**.
    - Imposta il tipo di caricamento dei dati di convalida su **Fornire dati di convalida differenti**.
    - Seleziona **+ Seleziona dati** per caricare i **Dati di convalida**.

    ![Compila la pagina di ottimizzazione.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.it.png)

    > [!TIP]
    >
    > Puoi selezionare **Impostazioni avanzate** per personalizzare configurazioni come **learning_rate** e **lr_scheduler_type** per ottimizzare il processo di ottimizzazione in base alle tue esigenze specifiche.

1. Seleziona **Fine**.

1. In questo esercizio, hai ottimizzato con successo il modello Phi-3 utilizzando Azure Machine Learning. Nota che il processo di ottimizzazione può richiedere molto tempo. Dopo aver avviato il job di ottimizzazione, devi attendere il suo completamento. Puoi monitorare lo stato del job di ottimizzazione accedendo alla scheda Job nella barra laterale sinistra dello spazio di lavoro di Azure Machine Learning. Nella prossima serie di esercizi, distribuirai il modello ottimizzato e lo integrerai con Prompt flow.

    ![Vedi job di ottimizzazione.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.it.png)

### Distribuisci il modello Phi-3 ottimizzato

Per integrare il modello Phi-3 ottimizzato con Prompt flow, è necessario distribuire il modello per renderlo accessibile per inferenze in tempo reale. Questo processo comprende la registrazione del modello, la creazione di un endpoint online e la distribuzione del modello.

In questo esercizio, farai quanto segue:

- Registra il modello ottimizzato nello spazio di lavoro di Azure Machine Learning.
- Crea un endpoint online.
- Distribuisci il modello Phi-3 ottimizzato registrato.

#### Registra il modello ottimizzato

1. Visita [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Seleziona lo spazio di lavoro di Azure Machine Learning che hai creato.

    ![Seleziona lo spazio di lavoro creato.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.it.png)

1. Seleziona **Modelli** dalla barra laterale sinistra.
1. Seleziona **+ Registra**.
1. Seleziona **Da un output di job**.

    ![Registra modello.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.it.png)

1. Seleziona il job che hai creato.

    ![Seleziona job.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.it.png)

1. Seleziona **Avanti**.

1. Imposta **Tipo di modello** su **MLflow**.

1. Assicurati che **Output del job** sia selezionato automaticamente.

    ![Seleziona output.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.it.png)

2. Seleziona **Avanti**.

3. Seleziona **Registra**.

    ![Seleziona registra.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.it.png)

4. Puoi visualizzare il tuo modello registrato accedendo al menu **Modelli** dalla barra laterale sinistra.

    ![Modello registrato.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.it.png)

#### Distribuisci il modello ottimizzato

1. Accedi allo spazio di lavoro di Azure Machine Learning che hai creato.

1. Seleziona **Endpoint** dalla barra laterale sinistra.

1. Seleziona **Endpoint in tempo reale** dal menu di navigazione.

    ![Crea endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.it.png)

1. Seleziona **Crea**.

1. Seleziona il modello registrato che hai creato.

    ![Seleziona modello registrato.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.it.png)

1. Seleziona **Seleziona**.

1. Esegui le seguenti operazioni:

    - Imposta **Macchina virtuale** su *Standard_NC6s_v3*.
    - Imposta il **Numero di istanze** da utilizzare, ad esempio *1*.
    - Imposta l'**Endpoint** su **Nuovo** per creare un endpoint.
    - Inserisci il **Nome dell'endpoint**. Deve essere un valore univoco.
    - Inserisci il **Nome della distribuzione**. Deve essere un valore univoco.

    ![Compila impostazioni di distribuzione.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.it.png)

1. Seleziona **Distribuisci**.

> [!WARNING]
> Per evitare costi aggiuntivi sul tuo account, assicurati di eliminare l'endpoint creato nello spazio di lavoro di Azure Machine Learning.
>

#### Verifica lo stato della distribuzione nello spazio di lavoro di Azure Machine Learning

1. Accedi allo spazio di lavoro di Azure Machine Learning che hai creato.

1. Seleziona **Endpoint** dalla barra laterale sinistra.

1. Seleziona l'endpoint che hai creato.

    ![Seleziona endpoint](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.it.png)

1. In questa pagina, puoi gestire gli endpoint durante il processo di distribuzione.

> [!NOTE]
> Una volta completata la distribuzione, assicurati che **Traffico live** sia impostato su **100%**. Se non lo è, seleziona **Aggiorna traffico** per regolare le impostazioni di traffico. Nota che non puoi testare il modello se il traffico è impostato su 0%.
>
> ![Imposta traffico.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.it.png)
>

## Scenario 3: Integra con Prompt flow e chatta con il tuo modello personalizzato in Azure AI Foundry

### Integra il modello Phi-3 personalizzato con Prompt flow

Dopo aver distribuito con successo il tuo modello ottimizzato, puoi ora integrarlo con Prompt Flow per utilizzarlo in applicazioni in tempo reale, abilitando una varietà di attività interattive con il tuo modello Phi-3 personalizzato.

In questo esercizio, farai quanto segue:

- Crea un Hub di Azure AI Foundry.
- Crea un Progetto di Azure AI Foundry.
- Crea un Prompt flow.
- Aggiungi una connessione personalizzata per il modello Phi-3 ottimizzato.
- Configura Prompt flow per chattare con il tuo modello Phi-3 personalizzato.

> [!NOTE]
> Puoi anche integrare Promptflow utilizzando Azure ML Studio. Lo stesso processo di integrazione può essere applicato in Azure ML Studio.

#### Crea un Hub di Azure AI Foundry

Devi creare un Hub prima di creare il Progetto. Un Hub funziona come un Gruppo di Risorse, consentendoti di organizzare e gestire più Progetti all'interno di Azure AI Foundry.

1. Visita [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Seleziona **Tutti gli hub** dalla barra laterale sinistra.

1. Seleziona **+ Nuovo hub** dal menu di navigazione.

    ![Crea hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.it.png)

1. Esegui le seguenti operazioni:

    - Inserisci il **Nome dell'hub**. Deve essere un valore univoco.
    - Seleziona la tua **Sottoscrizione Azure**.
    - Seleziona il **Gruppo di risorse** da utilizzare (creane uno nuovo se necessario).
    - Seleziona la **Posizione** che desideri utilizzare.
    - Seleziona il **Connetti Servizi Azure AI** da utilizzare (creane uno nuovo se necessario).
    - Imposta **Connetti Azure AI Search** su **Salta connessione**.

    ![Compila hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.it.png)

1. Seleziona **Avanti**.

#### Crea un Progetto di Azure AI Foundry

1. Nell'hub che hai creato, seleziona **Tutti i progetti** dalla barra laterale sinistra.

1. Seleziona **+ Nuovo progetto** dal menu di navigazione.

    ![Seleziona nuovo progetto.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.it.png)

1. Inserisci il **Nome del progetto**. Deve essere un valore univoco.

    ![Crea progetto.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.it.png)

1. Seleziona **Crea un progetto**.

#### Aggiungi una connessione personalizzata per il modello Phi-3 ottimizzato

Per integrare il tuo modello Phi-3 personalizzato con Prompt flow, devi salvare l'endpoint del modello e la chiave in una connessione personalizzata. Questa configurazione garantisce l'accesso al tuo modello Phi-3 personalizzato in Prompt flow.

#### Imposta la chiave API e l'URI dell'endpoint del modello Phi-3 ottimizzato

1. Visita [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Accedi allo spazio di lavoro di Azure Machine Learning che hai creato.

1. Seleziona **Endpoint** dalla barra laterale sinistra.

    ![Seleziona endpoint.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.it.png)

1. Seleziona l'endpoint che hai creato.

    ![Seleziona endpoint.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.it.png)

1. Seleziona **Consume** dal menu di navigazione.

1. Copia il tuo **Endpoint REST** e la **Chiave primaria**.
![Copia la chiave API e l'URI dell'endpoint.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.it.png)

#### Aggiungi la Connessione Personalizzata

1. Visita [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Vai al progetto di Azure AI Foundry che hai creato.

1. Nel progetto che hai creato, seleziona **Impostazioni** dalla barra laterale sinistra.

1. Seleziona **+ Nuova connessione**.

    ![Seleziona nuova connessione.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.it.png)

1. Seleziona **Chiavi personalizzate** dal menu di navigazione.

    ![Seleziona chiavi personalizzate.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.it.png)

1. Esegui le seguenti operazioni:

    - Seleziona **+ Aggiungi coppie chiave-valore**.
    - Per il nome della chiave, inserisci **endpoint** e incolla l'endpoint copiato da Azure ML Studio nel campo valore.
    - Seleziona nuovamente **+ Aggiungi coppie chiave-valore**.
    - Per il nome della chiave, inserisci **key** e incolla la chiave copiata da Azure ML Studio nel campo valore.
    - Dopo aver aggiunto le chiavi, seleziona **è segreto** per evitare che la chiave venga esposta.

    ![Aggiungi connessione.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.it.png)

1. Seleziona **Aggiungi connessione**.

#### Crea Prompt flow

Hai aggiunto una connessione personalizzata in Azure AI Foundry. Ora, creiamo un Prompt flow seguendo i passaggi seguenti. Successivamente, collegherai questo Prompt flow alla connessione personalizzata per poter utilizzare il modello ottimizzato all'interno del Prompt flow.

1. Vai al progetto di Azure AI Foundry che hai creato.

1. Seleziona **Prompt flow** dalla barra laterale sinistra.

1. Seleziona **+ Crea** dal menu di navigazione.

    ![Seleziona Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.it.png)

1. Seleziona **Chat flow** dal menu di navigazione.

    ![Seleziona chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.it.png)

1. Inserisci **Nome cartella** da utilizzare.

    ![Inserisci nome.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.it.png)

2. Seleziona **Crea**.

#### Configura il Prompt flow per chattare con il tuo modello personalizzato Phi-3

Devi integrare il modello Phi-3 ottimizzato in un Prompt flow. Tuttavia, il Prompt flow esistente fornito non è progettato per questo scopo. Pertanto, devi ridisegnare il Prompt flow per consentire l'integrazione del modello personalizzato.

1. Nel Prompt flow, esegui le seguenti operazioni per ricostruire il flusso esistente:

    - Seleziona **Modalità file grezzo**.
    - Elimina tutto il codice esistente nel file *flow.dag.yml*.
    - Aggiungi il seguente codice al file *flow.dag.yml*.

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

    - Seleziona **Salva**.

    ![Seleziona modalità file grezzo.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.it.png)

1. Aggiungi il seguente codice al file *integrate_with_promptflow.py* per utilizzare il modello personalizzato Phi-3 nel Prompt flow.

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

    ![Incolla codice prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.it.png)

> [!NOTE]
> Per informazioni più dettagliate sull'uso di Prompt flow in Azure AI Foundry, puoi fare riferimento a [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Seleziona **Input chat**, **Output chat** per abilitare la chat con il tuo modello.

    ![Input Output.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.it.png)

1. Ora sei pronto per chattare con il tuo modello personalizzato Phi-3. Nel prossimo esercizio, imparerai come avviare il Prompt flow e usarlo per chattare con il tuo modello ottimizzato Phi-3.

> [!NOTE]
>
> Il flusso ricostruito dovrebbe apparire come nell'immagine seguente:
>
> ![Esempio di flusso.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.it.png)
>

### Chatta con il tuo modello personalizzato Phi-3

Ora che hai ottimizzato e integrato il tuo modello personalizzato Phi-3 con Prompt flow, sei pronto per iniziare a interagire con esso. Questo esercizio ti guiderà attraverso il processo di configurazione e avvio di una chat con il tuo modello utilizzando Prompt flow. Seguendo questi passaggi, potrai sfruttare appieno le capacità del tuo modello ottimizzato Phi-3 per vari compiti e conversazioni.

- Chatta con il tuo modello personalizzato Phi-3 utilizzando Prompt flow.

#### Avvia Prompt flow

1. Seleziona **Avvia sessioni di calcolo** per avviare Prompt flow.

    ![Avvia sessione di calcolo.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.it.png)

1. Seleziona **Convalida e analizza input** per rinnovare i parametri.

    ![Convalida input.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.it.png)

1. Seleziona il **Valore** della **connessione** alla connessione personalizzata che hai creato. Ad esempio, *connection*.

    ![Connessione.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.it.png)

#### Chatta con il tuo modello personalizzato

1. Seleziona **Chat**.

    ![Seleziona chat.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.it.png)

1. Ecco un esempio dei risultati: Ora puoi chattare con il tuo modello personalizzato Phi-3. Si consiglia di fare domande basate sui dati utilizzati per l'ottimizzazione.

    ![Chat con prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.it.png)

**Disclaimer (Avvertenza):**  
Questo documento è stato tradotto utilizzando servizi di traduzione automatica basati sull'intelligenza artificiale. Pur cercando di garantire la massima accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.