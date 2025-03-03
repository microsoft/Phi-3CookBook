## RAG PromptFlow-val és AISearch-csel

Ebben a példában egy Retrieval Augmented Generation (RAG) alkalmazást valósítunk meg, amely a Phi3-at használja SLM-ként, az AI Search-t vectorDB-ként és a Prompt Flow-t alacsony kódú orchestrátorként.

## Jellemzők

- Egyszerű telepítés Docker segítségével.
- Skálázható architektúra az AI munkafolyamatok kezeléséhez.
- Alacsony kódú megközelítés a Prompt Flow használatával.

## Előfeltételek

Mielőtt elkezdenéd, győződj meg róla, hogy teljesítetted az alábbi követelményeket:

- Docker telepítve van a helyi gépedre.
- Egy Azure-fiók, amely jogosultságokkal rendelkezik konténer erőforrások létrehozására és kezelésére.
- Azure AI Studio és Azure AI Search példák.
- Egy beágyazási modell az index létrehozásához (lehet Azure OpenAI beágyazás vagy egy OS modell a katalógusból).
- Python 3.8 vagy újabb telepítve van a helyi gépedre.
- Egy Azure Container Registry (vagy bármely általad választott registry).

## Telepítés

1. Hozz létre egy új folyamatot az Azure AI Studio Projektedben a flow.yaml fájl segítségével.
2. Telepíts egy Phi3 modellt az Azure AI modellkatalógusából, és hozd létre a kapcsolatot a projekteddel. [Phi-3 telepítése Model as a Service-ként](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Hozz létre egy vektor indexet az Azure AI Search-ben bármely általad választott dokumentummal. [Vektor index létrehozása az Azure AI Search-ben](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Telepítsd a folyamatot egy menedzselt végpontra, és használd a prompt-flow-frontend.py fájlban. [Folyamat telepítése online végpontra](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Klónozd a repót:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Építsd meg a Docker képet:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Töltsd fel a Docker képet az Azure Container Registry-be:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Használat

1. Indítsd el a Docker konténert:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Nyisd meg az alkalmazást a böngésződben a `http://localhost:8501` címen.

## Kapcsolat

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Teljes cikk: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Felelősségkizárás**:  
Ez a dokumentum gépi AI fordítási szolgáltatások segítségével készült. Bár törekszünk a pontosságra, kérjük, vegye figyelembe, hogy az automatikus fordítások hibákat vagy pontatlanságokat tartalmazhatnak. Az eredeti dokumentum az eredeti nyelvén tekintendő hiteles forrásnak. Kritikus információk esetén javasolt professzionális emberi fordítást igénybe venni. Nem vállalunk felelősséget az ezen fordítás használatából eredő félreértésekért vagy téves értelmezésekért.