## RAG med PromptFlow og AISearch

I dette eksempel vil vi implementere en Retrieval Augmented Generation (RAG)-applikation, der udnytter Phi3 som SLM, AI Search som vectorDB og Prompt Flow som low-code orkestrator.

## Funktioner

- Nem implementering med Docker.
- Skalerbar arkitektur til håndtering af AI-workflows.
- Low-code tilgang med Prompt Flow.

## Forudsætninger

Før du går i gang, skal du sikre dig, at du har opfyldt følgende krav:

- Docker installeret på din lokale maskine.
- En Azure-konto med rettigheder til at oprette og administrere containerressourcer.
- En Azure AI Studio- og Azure AI Search-instans.
- En embeddingsmodel til at oprette dit indeks (kan enten være en Azure OpenAI-embedding eller en OS-model fra kataloget).
- Python 3.8 eller nyere installeret på din lokale maskine.
- Et Azure Container Registry (eller et hvilket som helst andet registry, du foretrækker).

## Installation

1. Opret et nyt flow i dit Azure AI Studio-projekt ved hjælp af flow.yaml-filen.
2. Udrul en Phi3-model fra dit Azure AI-modelkatalog, og opret forbindelsen til dit projekt. [Deploy Phi-3 som Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Opret vector-indekset på Azure AI Search ved hjælp af et hvilket som helst dokument, du ønsker. [Opret et vector-indeks på Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Udrul flowet på en managed endpoint, og brug det i prompt-flow-frontend.py-filen. [Deploy et flow på en online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Klon repository'et:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Byg Docker-billedet:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Push Docker-billedet til Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Brug

1. Kør Docker-containeren:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Tilgå applikationen i din browser på `http://localhost:8501`.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Fuld artikel: [RAG med Phi-3-Medium som Model as a Service fra Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel human oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der måtte opstå ved brug af denne oversættelse.