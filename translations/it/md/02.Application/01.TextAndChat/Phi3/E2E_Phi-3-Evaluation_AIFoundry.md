# Valutare il modello Phi-3 / Phi-3.5 ottimizzato in Azure AI Foundry con focus sui principi di AI responsabile di Microsoft

Questo esempio end-to-end (E2E) si basa sulla guida "[Evaluate Fine-tuned Phi-3 / 3.5 Models in Azure AI Foundry Focusing on Microsoft's Responsible AI](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)" dalla Microsoft Tech Community.

## Panoramica

### Come si può valutare la sicurezza e le prestazioni di un modello Phi-3 / Phi-3.5 ottimizzato in Azure AI Foundry?

Ottimizzare un modello può talvolta portare a risposte non intenzionali o indesiderate. Per garantire che il modello rimanga sicuro ed efficace, è importante valutarne il potenziale di generare contenuti dannosi e la capacità di produrre risposte accurate, pertinenti e coerenti. In questo tutorial, imparerai come valutare la sicurezza e le prestazioni di un modello Phi-3 / Phi-3.5 ottimizzato integrato con Prompt flow in Azure AI Foundry.

Ecco il processo di valutazione di Azure AI Foundry.

![Architettura del tutorial.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.it.png)

*Fonte immagine: [Valutazione delle applicazioni di intelligenza artificiale generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Per ulteriori informazioni dettagliate e per esplorare risorse aggiuntive su Phi-3 / Phi-3.5, visita il [Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723).

### Prerequisiti

- [Python](https://www.python.org/downloads)
- [Abbonamento Azure](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Modello Phi-3 / Phi-3.5 ottimizzato

### Indice

1. [**Scenario 1: Introduzione alla valutazione con Prompt flow di Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Introduzione alla valutazione della sicurezza](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Introduzione alla valutazione delle prestazioni](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [**Scenario 2: Valutare il modello Phi-3 / Phi-3.5 in Azure AI Foundry**](../../../../../../md/02.Application/01.TextAndChat/Phi3)

    - [Prima di iniziare](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Distribuire Azure OpenAI per valutare il modello Phi-3 / Phi-3.5](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Valutare il modello Phi-3 / Phi-3.5 ottimizzato utilizzando Prompt flow di Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. [Congratulazioni!](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## **Scenario 1: Introduzione alla valutazione con Prompt flow di Azure AI Foundry**

### Introduzione alla valutazione della sicurezza

Per garantire che il tuo modello di intelligenza artificiale sia etico e sicuro, è fondamentale valutarlo rispetto ai principi di AI responsabile di Microsoft. In Azure AI Foundry, le valutazioni di sicurezza consentono di verificare la vulnerabilità del modello agli attacchi di tipo jailbreak e il suo potenziale di generare contenuti dannosi, in linea con questi principi.

![Valutazione della sicurezza.](../../../../../../translated_images/safety-evaluation.91fdef98588aadf56e8043d04cd78d24aac1472d6c121a6289f60d50d1f33d42.it.png)

*Fonte immagine: [Valutazione delle applicazioni di intelligenza artificiale generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Principi di AI responsabile di Microsoft

Prima di iniziare con i passaggi tecnici, è essenziale comprendere i principi di AI responsabile di Microsoft, un quadro etico progettato per guidare lo sviluppo, la distribuzione e l'operatività responsabile dei sistemi di intelligenza artificiale. Questi principi garantiscono che le tecnologie di AI siano progettate in modo equo, trasparente e inclusivo. Essi costituiscono la base per valutare la sicurezza dei modelli di AI.

I principi di AI responsabile di Microsoft includono:

- **Equità e inclusività**: I sistemi di AI devono trattare tutti in modo equo ed evitare di influenzare gruppi di persone in situazioni simili in modi diversi. Ad esempio, quando i sistemi di AI forniscono indicazioni su trattamenti medici, domande di prestito o opportunità lavorative, dovrebbero fare le stesse raccomandazioni a chiunque abbia sintomi, circostanze finanziarie o qualifiche professionali simili.

- **Affidabilità e sicurezza**: Per costruire fiducia, è fondamentale che i sistemi di AI operino in modo affidabile, sicuro e coerente. Questi sistemi devono essere in grado di funzionare come originariamente progettati, rispondere in modo sicuro a condizioni inaspettate e resistere a manipolazioni dannose.

- **Trasparenza**: Quando i sistemi di AI aiutano a prendere decisioni che hanno un grande impatto sulla vita delle persone, è fondamentale che le persone comprendano come sono state prese tali decisioni. Ad esempio, una banca potrebbe usare un sistema di AI per decidere se una persona è idonea a un credito.

- **Privacy e sicurezza**: Con l'aumento della diffusione dell'AI, proteggere la privacy e garantire la sicurezza delle informazioni personali e aziendali diventano aspetti sempre più importanti e complessi. 

- **Responsabilità**: Le persone che progettano e distribuiscono sistemi di AI devono essere responsabili del loro funzionamento. Le organizzazioni dovrebbero seguire standard di settore per sviluppare norme di responsabilità.

![Hub responsabile.](../../../../../../translated_images/responsibleai2.93a32c6cd88ec3e57ec73a8c81717cd74ba27d2cd6d500097c82d79ac49726d7.it.png)

*Fonte immagine: [Cos'è l'AI responsabile?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Per saperne di più sui principi di AI responsabile di Microsoft, visita [Cos'è l'AI responsabile?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723).

#### Metriche di sicurezza

In questo tutorial, valuterai la sicurezza del modello Phi-3 ottimizzato utilizzando le metriche di sicurezza di Azure AI Foundry. Queste metriche ti aiutano a valutare il potenziale del modello di generare contenuti dannosi e la sua vulnerabilità agli attacchi di tipo jailbreak. Le metriche di sicurezza includono:

- **Contenuti relativi all'autolesionismo**: Valuta se il modello tende a produrre contenuti relativi all'autolesionismo.
- **Contenuti odiosi e ingiusti**: Valuta se il modello tende a produrre contenuti odiosi o ingiusti.
- **Contenuti violenti**: Valuta se il modello tende a produrre contenuti violenti.
- **Contenuti sessuali**: Valuta se il modello tende a produrre contenuti sessuali inappropriati.

Valutare questi aspetti garantisce che il modello di AI non produca contenuti dannosi o offensivi, allineandosi ai valori sociali e agli standard normativi.

![Valutare sulla base della sicurezza.](../../../../../../translated_images/evaluate-based-on-safety.3def6d9c7edaa49c536a7e58bfa48e2676fe911e80e847b732c0c9688c19946c.it.png)

### Introduzione alla valutazione delle prestazioni

Per garantire che il tuo modello di AI funzioni come previsto, è importante valutarne le prestazioni rispetto alle metriche di performance. In Azure AI Foundry, le valutazioni delle prestazioni consentono di verificare l'efficacia del modello nel generare risposte accurate, pertinenti e coerenti.

![Valutazione delle prestazioni.](../../../../../../translated_images/performance-evaluation.692eccfdea40b8a399040a6304cfee03667b5a9a0636a7152565d806427ff6be.it.png)

*Fonte immagine: [Valutazione delle applicazioni di intelligenza artificiale generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Metriche di prestazione

In questo tutorial, valuterai le prestazioni del modello Phi-3 / Phi-3.5 ottimizzato utilizzando le metriche di prestazione di Azure AI Foundry. Queste metriche ti aiutano a valutare l'efficacia del modello nel generare risposte accurate, pertinenti e coerenti. Le metriche di prestazione includono:

- **Groundedness**: Valuta quanto bene le risposte generate si allineano alle informazioni della fonte di input.
- **Pertinenza**: Valuta la rilevanza delle risposte generate rispetto alle domande poste.
- **Coerenza**: Valuta quanto fluido e naturale appare il testo generato, somigliando al linguaggio umano.
- **Fluenza**: Valuta la competenza linguistica del testo generato.
- **Similarità GPT**: Confronta la risposta generata con la verità di riferimento per verificarne la somiglianza.
- **F1 Score**: Calcola il rapporto tra le parole condivise tra la risposta generata e i dati sorgente.

Queste metriche ti aiutano a valutare l'efficacia del modello nel generare risposte accurate, pertinenti e coerenti.

![Valutare sulla base delle prestazioni.](../../../../../../translated_images/evaluate-based-on-performance.16c477bfd4e547f34dd803492ce032fbdb3376a5dbd236042233e21e5b7f7f6a.it.png)

## **Scenario 2: Valutare il modello Phi-3 / Phi-3.5 in Azure AI Foundry**

### Prima di iniziare

Questo tutorial è un seguito ai post precedenti del blog, "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" e "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)." In questi post, abbiamo illustrato il processo di ottimizzazione di un modello Phi-3 / Phi-3.5 in Azure AI Foundry e la sua integrazione con Prompt flow.

In questo tutorial, distribuirai un modello Azure OpenAI come valutatore in Azure AI Foundry e lo utilizzerai per valutare il tuo modello Phi-3 / Phi-3.5 ottimizzato.

Prima di iniziare questo tutorial, assicurati di avere i seguenti prerequisiti, come descritto nei tutorial precedenti:

1. Un dataset preparato per valutare il modello Phi-3 / Phi-3.5 ottimizzato.
1. Un modello Phi-3 / Phi-3.5 che è stato ottimizzato e distribuito su Azure Machine Learning.
1. Un Prompt flow integrato con il tuo modello Phi-3 / Phi-3.5 ottimizzato in Azure AI Foundry.

> [!NOTE]
> Utilizzerai il file *test_data.jsonl*, situato nella cartella dati del dataset **ULTRACHAT_200k** scaricato nei post del blog precedenti, come dataset per valutare il modello Phi-3 / Phi-3.5 ottimizzato.

#### Integrare il modello personalizzato Phi-3 / Phi-3.5 con Prompt flow in Azure AI Foundry (approccio basato sul codice)

> [!NOTE]
> Se hai seguito l'approccio low-code descritto in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)", puoi saltare questo esercizio e passare a quello successivo.
> Tuttavia, se hai seguito l'approccio basato sul codice descritto in "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)" per ottimizzare e distribuire il tuo modello Phi-3 / Phi-3.5, il processo di connessione del modello a Prompt flow è leggermente diverso. Imparerai questo processo in questo esercizio.

Per procedere, devi integrare il tuo modello Phi-3 / Phi-3.5 ottimizzato in Prompt flow in Azure AI Foundry.

#### Creare un Hub in Azure AI Foundry

Devi creare un Hub prima di creare il Progetto. Un Hub funziona come un Gruppo di risorse, permettendoti di organizzare e gestire più Progetti all'interno di Azure AI Foundry.

1. Accedi a [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Seleziona **Tutti gli hub** dalla barra laterale sinistra.

1. Seleziona **+ Nuovo hub** dal menu di navigazione.

    ![Creare un hub.](../../../../../../translated_images/create-hub.1e304b20eb7e729735ac1c083fbaf6c02be763279b86af2540e8a001f2bf470b.it.png)

1. Esegui le seguenti operazioni:

    - Inserisci un **Nome hub** univoco.
    - Seleziona il tuo **Abbonamento Azure**.
    - Seleziona il **Gruppo di risorse** da utilizzare (creane uno nuovo se necessario).
    - Seleziona la **Località** che desideri utilizzare.
    - Seleziona **Connetti servizi di AI di Azure** da utilizzare (creane uno nuovo se necessario).
    - Seleziona **Connetti Azure AI Search** per **Saltare la connessione**.
![Compila hub.](../../../../../../translated_images/fill-hub.bb8b648703e968da13d123e40a6fc76f2193f6c6b432d24036d2aa9e823ee813.it.png)

1. Seleziona **Avanti**.

#### Crea un progetto Azure AI Foundry

1. Nel Hub che hai creato, seleziona **Tutti i progetti** dalla scheda laterale sinistra.

1. Seleziona **+ Nuovo progetto** dal menu di navigazione.

    ![Seleziona nuovo progetto.](../../../../../../translated_images/select-new-project.1b9270456fbb8d598938036c6bd26247ea39c8b9ad76be16c81df57d54ce78ed.it.png)

1. Inserisci **Nome progetto**. Deve essere un valore univoco.

    ![Crea progetto.](../../../../../../translated_images/create-project.8378d7842c49702498ba20f0553cbe91ff516275c8514ec865799669f9becbff.it.png)

1. Seleziona **Crea un progetto**.

#### Aggiungi una connessione personalizzata per il modello Phi-3 / Phi-3.5 ottimizzato

Per integrare il tuo modello Phi-3 / Phi-3.5 personalizzato con Prompt flow, devi salvare l'endpoint e la chiave del modello in una connessione personalizzata. Questa configurazione garantisce l'accesso al tuo modello personalizzato Phi-3 / Phi-3.5 in Prompt flow.

#### Imposta chiave API e URI dell'endpoint del modello Phi-3 / Phi-3.5 ottimizzato

1. Visita [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Accedi allo spazio di lavoro di Azure Machine Learning che hai creato.

1. Seleziona **Endpoint** dalla scheda laterale sinistra.

    ![Seleziona endpoint.](../../../../../../translated_images/select-endpoints.fc2852aa73fdb1531682b599c0b1f5b39a842f0a60fec7c8e941b3070ec6c463.it.png)

1. Seleziona l'endpoint che hai creato.

    ![Seleziona endpoint creato.](../../../../../../translated_images/select-endpoint-created.e1cd34ec8ae5a3eca599be7c894b0738e243317960138984b32d8a3fe20f4380.it.png)

1. Seleziona **Consuma** dal menu di navigazione.

1. Copia il tuo **Endpoint REST** e la **Chiave primaria**.

    ![Copia chiave API e URI dell'endpoint.](../../../../../../translated_images/copy-endpoint-key.f74d8aab513b5f540d2a219198fc5b7a3e64213497491bedb17f4bd039f16054.it.png)

#### Aggiungi la Connessione Personalizzata

1. Visita [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Accedi al progetto Azure AI Foundry che hai creato.

1. Nel progetto che hai creato, seleziona **Impostazioni** dalla scheda laterale sinistra.

1. Seleziona **+ Nuova connessione**.

    ![Seleziona nuova connessione.](../../../../../../translated_images/select-new-connection.7ac97b4db6dc44c3d4f01a38b22fff11c3e88f75bcbf4d26999048a61a8729b2.it.png)

1. Seleziona **Chiavi personalizzate** dal menu di navigazione.

    ![Seleziona chiavi personalizzate.](../../../../../../translated_images/select-custom-keys.b2e452da9ea19401c4b7c63fe2ec95a3a38fd13ae3e9fca37d431f0b7780d4da.it.png)

1. Esegui le seguenti operazioni:

    - Seleziona **+ Aggiungi coppie chiave-valore**.
    - Per il nome della chiave, inserisci **endpoint** e incolla l'endpoint che hai copiato da Azure ML Studio nel campo del valore.
    - Seleziona **+ Aggiungi coppie chiave-valore** di nuovo.
    - Per il nome della chiave, inserisci **key** e incolla la chiave che hai copiato da Azure ML Studio nel campo del valore.
    - Dopo aver aggiunto le chiavi, seleziona **è segreto** per evitare che la chiave venga esposta.

    ![Aggiungi connessione.](../../../../../../translated_images/add-connection.645b0c3ecf4a21f97a16ffafc9f25fedbb75a823cec5fc9dd778c3ab6130b4f0.it.png)

1. Seleziona **Aggiungi connessione**.

#### Crea Prompt flow

Hai aggiunto una connessione personalizzata in Azure AI Foundry. Ora, crea un Prompt flow seguendo questi passaggi. Successivamente, collegherai questo Prompt flow alla connessione personalizzata per utilizzare il modello ottimizzato all'interno del Prompt flow.

1. Accedi al progetto Azure AI Foundry che hai creato.

1. Seleziona **Prompt flow** dalla scheda laterale sinistra.

1. Seleziona **+ Crea** dal menu di navigazione.

    ![Seleziona Promptflow.](../../../../../../translated_images/select-promptflow.4d42246677cc7ba65feb3e2be4479620a2b1e6637a66847dc1047ca89cd02780.it.png)

1. Seleziona **Chat flow** dal menu di navigazione.

    ![Seleziona chat flow.](../../../../../../translated_images/select-flow-type.e818b610f36e93c5c9741911d7b95232164f01486cbb39a29d748c322bd62038.it.png)

1. Inserisci **Nome cartella** da utilizzare.

    ![Inserisci nome cartella.](../../../../../../translated_images/enter-name.628d4a5d69122cfae9d66e9bccf0f2f38c595e90e456a3837c713aadeff6aa52.it.png)

1. Seleziona **Crea**.

#### Configura Prompt flow per chattare con il tuo modello Phi-3 / Phi-3.5 personalizzato

Devi integrare il modello Phi-3 / Phi-3.5 ottimizzato in un Prompt flow. Tuttavia, il Prompt flow esistente non è progettato per questo scopo. Pertanto, devi riprogettare il Prompt flow per consentire l'integrazione del modello personalizzato.

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

    ![Seleziona modalità file grezzo.](../../../../../../translated_images/select-raw-file-mode.e665df3117bf5411acf4d93bc8ecc405a984120c0ca7b944fe700601fdbac66f.it.png)

1. Aggiungi il seguente codice a *integrate_with_promptflow.py* per utilizzare il modello Phi-3 / Phi-3.5 personalizzato in Prompt flow.

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
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

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
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Incolla codice Prompt flow.](../../../../../../translated_images/paste-promptflow-code.8547c46c57a5354667f91578d7bca9cc2d0f5e1c4dadd59efa1ca18d6376e7a8.it.png)

> [!NOTE]
> Per informazioni più dettagliate sull'uso di Prompt flow in Azure AI Foundry, puoi fare riferimento a [Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Seleziona **Input chat**, **Output chat** per abilitare la chat con il tuo modello.

    ![Seleziona Input Output.](../../../../../../translated_images/select-input-output.4d094b2da9e817e0ef7b9fd5339d929b50364b430ecc476a39c885ae9e4dcb35.it.png)

1. Ora sei pronto per chattare con il tuo modello Phi-3 / Phi-3.5 personalizzato. Nel prossimo esercizio, imparerai come avviare Prompt flow e usarlo per chattare con il tuo modello ottimizzato Phi-3 / Phi-3.5.

> [!NOTE]
>
> Il flusso ricostruito dovrebbe apparire come nell'immagine seguente:
>
> ![Esempio di flusso](../../../../../../translated_images/graph-example.55ee258e205e3b686250c5fc480ffe8956eb9f4887f7b11e94a6720e0d032733.it.png)
>

#### Avvia Prompt flow

1. Seleziona **Avvia sessioni di calcolo** per avviare Prompt flow.

    ![Avvia sessione di calcolo.](../../../../../../translated_images/start-compute-session.e7eb268344e2040fdee7b46a175d2fbd19477e0ab122ef563113828d03b03946.it.png)

1. Seleziona **Convalida e analizza input** per aggiornare i parametri.

    ![Convalida input.](../../../../../../translated_images/validate-input.dffb16c78fc266e52d55582791d67a54d631c166a61d7ca57a258e00c2e14150.it.png)

1. Seleziona il **Valore** della **connessione** alla connessione personalizzata che hai creato. Ad esempio, *connection*.

    ![Connessione.](../../../../../../translated_images/select-connection.5c7a570da52e12219d21fef02800b152d124722619f56064b172a84721603b52.it.png)

#### Chatta con il tuo modello Phi-3 / Phi-3.5 personalizzato

1. Seleziona **Chat**.

    ![Seleziona chat.](../../../../../../translated_images/select-chat.c255a13f678aa46d9601c54a81aa2e0d58c9e01a8c6ec7d86598438d8e19214d.it.png)

1. Ecco un esempio dei risultati: Ora puoi chattare con il tuo modello Phi-3 / Phi-3.5 personalizzato. È consigliato fare domande basate sui dati utilizzati per l'ottimizzazione.

    ![Chatta con Prompt flow.](../../../../../../translated_images/chat-with-promptflow.6da5e838c71f428b6d8aea9a0c655568354ae82babcdc87cd0f0d4edeee9d930.it.png)

### Distribuisci Azure OpenAI per valutare il modello Phi-3 / Phi-3.5

Per valutare il modello Phi-3 / Phi-3.5 in Azure AI Foundry, devi distribuire un modello Azure OpenAI. Questo modello sarà utilizzato per valutare le prestazioni del modello Phi-3 / Phi-3.5.

#### Distribuisci Azure OpenAI

1. Accedi a [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Accedi al progetto Azure AI Foundry che hai creato.

    ![Seleziona Progetto.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.it.png)

1. Nel progetto che hai creato, seleziona **Distribuzioni** dalla scheda laterale sinistra.

1. Seleziona **+ Distribuisci modello** dal menu di navigazione.

1. Seleziona **Distribuisci modello base**.

    ![Seleziona Distribuzioni.](../../../../../../translated_images/deploy-openai-model.91e6d9f9934e0e0c63116bd81a7628ea5ab37617f3e3b23a998a37c7f5aaba8b.it.png)

1. Seleziona il modello Azure OpenAI che desideri utilizzare. Ad esempio, **gpt-4o**.

    ![Seleziona modello Azure OpenAI.](../../../../../../translated_images/select-openai-model.c0f0e8d4afe80525745b4e67b52ae0d23550da9130bc8d1aea8160be0e261399.it.png)

1. Seleziona **Conferma**.

### Valuta il modello Phi-3 / Phi-3.5 ottimizzato utilizzando la valutazione Prompt flow di Azure AI Foundry

### Avvia una nuova valutazione

1. Visita [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723).

1. Accedi al progetto Azure AI Foundry che hai creato.

    ![Seleziona Progetto.](../../../../../../translated_images/select-project-created.84d119464c1bb0a8f5f9ab58012fa88304b0e3b0d6ddda444617424b2bb0d22e.it.png)

1. Nel progetto che hai creato, seleziona **Valutazione** dalla scheda laterale sinistra.

1. Seleziona **+ Nuova valutazione** dal menu di navigazione.
![Seleziona valutazione.](../../../../../../translated_images/select-evaluation.00ce489c57544e735170ae63682b293c3f5e362ded9d62b602ff0cf8e957287c.it.png)

1. Seleziona la valutazione **Prompt flow**.

    ![Seleziona valutazione Prompt flow.](../../../../../../translated_images/promptflow-evaluation.350729f9e70f59110aa0b425adcdf00b2d5382066144ac1cdf265fa1884808b2.it.png)

1. Esegui le seguenti operazioni:

    - Inserisci il nome della valutazione. Deve essere un valore univoco.
    - Seleziona **Domanda e risposta senza contesto** come tipo di attività. Questo perché il dataset **ULTRACHAT_200k** utilizzato in questo tutorial non contiene contesto.
    - Seleziona il prompt flow che desideri valutare.

    ![Valutazione Prompt flow.](../../../../../../translated_images/evaluation-setting1.772ca4e86a27e9c37d627e36c84c07b363a5d5229724f15596599d6b0f1d4ca1.it.png)

1. Seleziona **Avanti**.

1. Esegui le seguenti operazioni:

    - Seleziona **Aggiungi il tuo dataset** per caricare il dataset. Ad esempio, puoi caricare il file del dataset di test, come *test_data.json1*, che è incluso quando scarichi il dataset **ULTRACHAT_200k**.
    - Seleziona la **Colonna del dataset** appropriata che corrisponde al tuo dataset. Ad esempio, se utilizzi il dataset **ULTRACHAT_200k**, seleziona **${data.prompt}** come colonna del dataset.

    ![Valutazione Prompt flow.](../../../../../../translated_images/evaluation-setting2.074e573f2ab245d37b12a9057b8fef349a552962f1ec3b23fd09734d4d653752.it.png)

1. Seleziona **Avanti**.

1. Esegui le seguenti operazioni per configurare le metriche di performance e qualità:

    - Seleziona le metriche di performance e qualità che desideri utilizzare.
    - Seleziona il modello Azure OpenAI che hai creato per la valutazione. Ad esempio, seleziona **gpt-4o**.

    ![Valutazione Prompt flow.](../../../../../../translated_images/evaluation-setting3-1.7e26ae563c1312db5d1d21f8f44652243627f487df036ba27fe58d181102300d.it.png)

1. Esegui le seguenti operazioni per configurare le metriche di rischio e sicurezza:

    - Seleziona le metriche di rischio e sicurezza che desideri utilizzare.
    - Seleziona la soglia per calcolare il tasso di difetti che desideri utilizzare. Ad esempio, seleziona **Media**.
    - Per **domanda**, seleziona **Origine dati** su **{$data.prompt}**.
    - Per **risposta**, seleziona **Origine dati** su **{$run.outputs.answer}**.
    - Per **ground_truth**, seleziona **Origine dati** su **{$data.message}**.

    ![Valutazione Prompt flow.](../../../../../../translated_images/evaluation-setting3-2.185148a456f1edb7d0db874f765dc6bc34fec7e1b00833be81b0428af6d18233.it.png)

1. Seleziona **Avanti**.

1. Seleziona **Invia** per avviare la valutazione.

1. La valutazione richiederà del tempo per essere completata. Puoi monitorare i progressi nella scheda **Valutazione**.

### Rivedi i Risultati della Valutazione

> [!NOTE]
> I risultati presentati di seguito sono forniti a scopo illustrativo per mostrare il processo di valutazione. In questo tutorial, è stato utilizzato un modello ottimizzato su un dataset relativamente piccolo, il che potrebbe portare a risultati non ottimali. I risultati effettivi possono variare significativamente a seconda della dimensione, qualità e diversità del dataset utilizzato, così come della configurazione specifica del modello.

Una volta completata la valutazione, puoi esaminare i risultati sia per le metriche di performance che per quelle di sicurezza.

1. Metriche di performance e qualità:

    - Valuta l’efficacia del modello nel generare risposte coerenti, fluide e pertinenti.

    ![Risultato della valutazione.](../../../../../../translated_images/evaluation-result-gpu.8e9decea0f5dd1250948982514bcde94bb2debba2b686be5e633f1aad093921f.it.png)

1. Metriche di rischio e sicurezza:

    - Assicurati che le risposte del modello siano sicure e in linea con i Principi di AI Responsabile, evitando contenuti dannosi o offensivi.

    ![Risultato della valutazione.](../../../../../../translated_images/evaluation-result-gpu-2.180e37b9669f3d31aade247bd38b87b15a2ef93b69a1633c4e4072946aadaa26.it.png)

1. Puoi scorrere verso il basso per visualizzare i **Risultati dettagliati delle metriche**.

    ![Risultato della valutazione.](../../../../../../translated_images/detailed-metrics-result.a0abde70a729afee17e34df7c11ea2f6f0ea1aefbe8a26a35502f304de57a647.it.png)

1. Valutando il tuo modello personalizzato Phi-3 / Phi-3.5 rispetto sia alle metriche di performance che a quelle di sicurezza, puoi confermare che il modello non solo è efficace, ma aderisce anche alle pratiche di AI responsabile, rendendolo pronto per l’implementazione nel mondo reale.

## Congratulazioni!

### Hai completato questo tutorial

Hai valutato con successo il modello Phi-3 ottimizzato integrato con Prompt flow in Azure AI Foundry. Questo è un passaggio importante per garantire che i tuoi modelli di intelligenza artificiale non solo offrano buone prestazioni, ma rispettino anche i principi di AI Responsabile di Microsoft, aiutandoti a creare applicazioni di intelligenza artificiale affidabili e degne di fiducia.

![Architettura.](../../../../../../translated_images/architecture.99df2035c1c1a82e7f7d3aa3368e5940e46d27d35abd498166e55094298fce81.it.png)

## Pulizia delle Risorse di Azure

Pulisci le tue risorse di Azure per evitare costi aggiuntivi sul tuo account. Vai al portale di Azure e elimina le seguenti risorse:

- La risorsa di Azure Machine Learning.
- L'endpoint del modello di Azure Machine Learning.
- La risorsa del progetto Azure AI Foundry.
- La risorsa Prompt flow di Azure AI Foundry.

### Passaggi Successivi

#### Documentazione

- [Valutare i sistemi AI utilizzando il dashboard AI Responsabile](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Metriche di valutazione e monitoraggio per AI generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Documentazione di Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Documentazione di Prompt flow](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### Contenuti Formativi

- [Introduzione all'approccio AI Responsabile di Microsoft](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduzione ad Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### Riferimenti

- [Che cos'è l'AI Responsabile?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Annuncio di nuovi strumenti in Azure AI per aiutarti a creare applicazioni di AI generativa più sicure e affidabili](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Valutazione delle applicazioni di AI generativa](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando servizi di traduzione automatica basati su intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale umana. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.