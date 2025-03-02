## RAG med PromptFlow og AISearch

I dette eksemplet skal vi implementere en Retrieval Augmented Generation (RAG)-applikasjon ved å bruke Phi3 som SLM, AI Search som vectorDB og Prompt Flow som en lavkode orkestrator.

## Funksjoner

- Enkel distribusjon ved bruk av Docker.
- Skalerbar arkitektur for å håndtere AI-arbeidsflyter.
- Lavkode tilnærming ved bruk av Prompt Flow.

## Forutsetninger

Før du begynner, sørg for at du har oppfylt følgende krav:

- Docker installert på din lokale maskin.
- En Azure-konto med tillatelser til å opprette og administrere containerressurser.
- Azure AI Studio og Azure AI Search-instans.
- En embedding-modell for å lage indeksen din (kan være enten en Azure OpenAI embedding eller en OS-modell fra katalogen).
- Python 3.8 eller nyere installert på din lokale maskin.
- Et Azure Container Registry (eller et annet registry etter eget valg).

## Installasjon

1. Opprett en ny flow i ditt Azure AI Studio-prosjekt ved å bruke flow.yaml-filen.
2. Distribuer en Phi3-modell fra din Azure AI-modellkatalog og opprett tilkoblingen til prosjektet ditt. [Distribuer Phi-3 som en Modell som en Tjeneste](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Opprett vektorindeksen i Azure AI Search ved hjelp av et valgfritt dokument. [Opprett en vektorindeks i Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Distribuer flowen på et administrert endepunkt og bruk den i prompt-flow-frontend.py-filen. [Distribuer en flow på et online endepunkt](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Klon repositoryet:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Bygg Docker-imaget:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Skyv Docker-imaget til Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Bruk

1. Kjør Docker-containeren:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Åpne applikasjonen i nettleseren din på `http://localhost:8501`.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Full artikkel: [RAG med Phi-3-Medium som en Modell som en Tjeneste fra Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.