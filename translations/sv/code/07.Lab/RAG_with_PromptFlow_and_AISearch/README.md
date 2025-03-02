## RAG med PromptFlow och AISearch

I det här exemplet ska vi implementera en Retrieval Augmented Generation (RAG)-applikation som använder Phi3 som SLM, AI Search som vectorDB och Prompt Flow som low-code-orkestrator.

## Funktioner

- Enkel distribution med Docker.
- Skalbar arkitektur för att hantera AI-arbetsflöden.
- Low-code-ansats med Prompt Flow.

## Förutsättningar

Innan du börjar, se till att du uppfyller följande krav:

- Docker installerat på din lokala maskin.
- Ett Azure-konto med behörighet att skapa och hantera containerresurser.
- Azure AI Studio och Azure AI Search-instans.
- En embedding-modell för att skapa ditt index (kan vara antingen en Azure OpenAI-embedding eller en OS-modell från katalogen).
- Python 3.8 eller senare installerat på din lokala maskin.
- Ett Azure Container Registry (eller valfritt annat register).

## Installation

1. Skapa ett nytt flöde i ditt Azure AI Studio-projekt med hjälp av filen flow.yaml.
2. Distribuera en Phi3-modell från din Azure AI-modellkatalog och skapa anslutningen till ditt projekt. [Distribuera Phi-3 som en modell som tjänst](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Skapa ett vektorindex i Azure AI Search med valfritt dokument. [Skapa ett vektorindex i Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Distribuera flödet på en hanterad slutpunkt och använd det i filen prompt-flow-frontend.py. [Distribuera ett flöde på en online-slutpunkt](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Klona arkivet:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Bygg Docker-avbildningen:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Skicka Docker-avbildningen till Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Användning

1. Kör Docker-containern:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Öppna applikationen i din webbläsare på `http://localhost:8501`.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Fullständig artikel: [RAG med Phi-3-Medium som en modell som tjänst från Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, vänligen notera att automatiska översättningar kan innehålla fel eller brister. Det ursprungliga dokumentet på sitt ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.