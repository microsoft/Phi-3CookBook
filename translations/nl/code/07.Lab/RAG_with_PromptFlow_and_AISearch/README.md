## RAG met PromptFlow en AISearch

In dit voorbeeld implementeren we een Retrieval Augmented Generation (RAG)-applicatie met Phi3 als SLM, AI Search als vectorDB en Prompt Flow als low-code orkestrator.

## Functies

- Eenvoudige implementatie met Docker.
- Schaalbare architectuur voor het beheren van AI-workflows.
- Low-code aanpak met Prompt Flow.

## Vereisten

Voordat je begint, zorg ervoor dat je aan de volgende vereisten voldoet:

- Docker geïnstalleerd op je lokale machine.
- Een Azure-account met rechten om containerresources te maken en beheren.
- Een Azure AI Studio- en Azure AI Search-instantie.
- Een embeddingmodel om je index te maken (dit kan een Azure OpenAI embedding zijn of een OS-model uit de catalogus).
- Python 3.8 of later geïnstalleerd op je lokale machine.
- Een Azure Container Registry (of een andere registry naar keuze).

## Installatie

1. Maak een nieuwe flow aan in je Azure AI Studio-project met behulp van het bestand flow.yaml.
2. Implementeer een Phi3-model vanuit je Azure AI-modelcatalogus en maak de verbinding met je project. [Implementeer Phi-3 als een Model als een Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Maak de vectorindex in Azure AI Search met behulp van een document naar keuze. [Maak een vectorindex in Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Implementeer de flow op een beheerd eindpunt en gebruik deze in het bestand prompt-flow-frontend.py. [Implementeer een flow op een online eindpunt](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Clone de repository:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Bouw de Docker-image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Push de Docker-image naar Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Gebruik

1. Start de Docker-container:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Open de applicatie in je browser op `http://localhost:8501`.

## Contact

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Volledig artikel: [RAG met Phi-3-Medium als een Model als een Service vanuit Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Disclaimer**:  
Dit document is vertaald met behulp van AI-gebaseerde vertaaldiensten. Hoewel we ons best doen om nauwkeurigheid te waarborgen, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in zijn oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor kritieke informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.