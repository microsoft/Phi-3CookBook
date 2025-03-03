## RAG s PromptFlow a AISearch

V tomto príklade implementujeme aplikáciu Retrieval Augmented Generation (RAG) využívajúcu Phi3 ako SLM, AI Search ako vectorDB a Prompt Flow ako nízkokódový orchestrátor.

## Funkcie

- Jednoduché nasadenie pomocou Dockeru.
- Škálovateľná architektúra na spracovanie AI workflowov.
- Nízko-kódový prístup pomocou Prompt Flow.

## Predpoklady

Predtým, ako začnete, uistite sa, že spĺňate nasledujúce požiadavky:

- Docker nainštalovaný na vašom lokálnom počítači.
- Azure účet s oprávneniami na vytváranie a správu kontajnerových zdrojov.
- Inštancie Azure AI Studio a Azure AI Search.
- Embedding model na vytvorenie vášho indexu (môže to byť buď Azure OpenAI embedding alebo OS model z katalógu).
- Python 3.8 alebo novšia verzia nainštalovaná na vašom lokálnom počítači.
- Azure Container Registry (alebo akýkoľvek registry podľa vášho výberu).

## Inštalácia

1. Vytvorte nový flow vo vašom projekte Azure AI Studio pomocou súboru flow.yaml.
2. Nasadte Phi3 Model z vášho katalógu modelov Azure AI a vytvorte spojenie s vaším projektom. [Nasadiť Phi-3 ako Model ako Službu](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Vytvorte vektorový index na Azure AI Search pomocou akéhokoľvek dokumentu podľa vášho výberu. [Vytvoriť vektorový index na Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Nasadte flow na spravovaný endpoint a použite ho v súbore prompt-flow-frontend.py. [Nasadiť flow na online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Naklonujte repozitár:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Vytvorte Docker image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Nahrajte Docker image do Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Použitie

1. Spustite Docker kontajner:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Pristupujte k aplikácii vo vašom prehliadači na adrese `http://localhost:8501`.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Celý článok: [RAG s Phi-3-Medium ako Model ako Služba z Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových AI prekladateľských služieb. Hoci sa snažíme o presnosť, prosím, uvedomte si, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny ľudský preklad. Nezodpovedáme za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.