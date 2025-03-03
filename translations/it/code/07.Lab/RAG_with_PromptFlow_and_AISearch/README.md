## RAG con PromptFlow e AISearch

In questo esempio, implementeremo un'applicazione di Retrieval Augmented Generation (RAG) utilizzando Phi3 come SLM, AI Search come vectorDB e Prompt Flow come orchestratore low-code.

## Funzionalità

- Implementazione semplificata con Docker.
- Architettura scalabile per la gestione di flussi di lavoro AI.
- Approccio low-code tramite Prompt Flow.

## Prerequisiti

Prima di iniziare, assicurati di aver soddisfatto i seguenti requisiti:

- Docker installato sulla tua macchina locale.
- Un account Azure con permessi per creare e gestire risorse container.
- Un'istanza di Azure AI Studio e Azure AI Search.
- Un modello di embedding per creare il tuo indice (può essere un embedding di Azure OpenAI o un modello open source dal catalogo).
- Python 3.8 o versione successiva installato sulla tua macchina locale.
- Un Azure Container Registry (o un altro registro a tua scelta).

## Installazione

1. Crea un nuovo flow nel tuo progetto Azure AI Studio utilizzando il file flow.yaml.
2. Distribuisci un modello Phi3 dal catalogo modelli di Azure AI e crea la connessione al tuo progetto. [Distribuisci Phi-3 come Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Crea l'indice vettoriale su Azure AI Search utilizzando un documento a tua scelta. [Crea un indice vettoriale su Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Distribuisci il flow su un endpoint gestito e utilizzalo nel file prompt-flow-frontend.py. [Distribuisci un flow su un endpoint online](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Clona il repository:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Crea l'immagine Docker:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Carica l'immagine Docker su Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Utilizzo

1. Avvia il container Docker:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Accedi all'applicazione nel tuo browser all'indirizzo `http://localhost:8501`.

## Contatti

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Articolo completo: [RAG con Phi-3-Medium come Model as a Service dal Catalogo Modelli di Azure](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Disclaimer**:  
Questo documento è stato tradotto utilizzando servizi di traduzione automatizzati basati sull'intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre deve essere considerato la fonte autorevole. Per informazioni critiche, si consiglia una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.