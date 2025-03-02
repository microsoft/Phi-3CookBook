## RAG s PromptFlow a AISearch

V tomto příkladu si ukážeme, jak implementovat aplikaci Retrieval Augmented Generation (RAG) s využitím Phi3 jako SLM, AI Search jako vectorDB a Prompt Flow jako nízkokódového orchestrátoru.

## Funkce

- Snadné nasazení pomocí Dockeru.
- Škálovatelná architektura pro zpracování AI workflowů.
- Nízkokódový přístup díky Prompt Flow.

## Požadavky

Než začnete, ujistěte se, že splňujete následující požadavky:

- Na vašem lokálním zařízení je nainstalován Docker.
- Máte účet Azure s oprávněním vytvářet a spravovat kontejnerové zdroje.
- Máte instance Azure AI Studio a Azure AI Search.
- Embedding model pro vytvoření indexu (může to být Azure OpenAI embedding nebo OS model z katalogu).
- Python 3.8 nebo novější nainstalovaný na vašem lokálním zařízení.
- Azure Container Registry (nebo jiný registr dle vašeho výběru).

## Instalace

1. Vytvořte nový flow ve vašem projektu Azure AI Studio pomocí souboru flow.yaml.
2. Nasazení modelu Phi3 z katalogu modelů Azure AI a vytvoření připojení k vašemu projektu. [Nasadit Phi-3 jako Model jako službu](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Vytvořte vektorový index na Azure AI Search pomocí libovolného dokumentu dle vašeho výběru. [Vytvoření vektorového indexu na Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Nasazení flow na spravovaný endpoint a jeho použití v souboru prompt-flow-frontend.py. [Nasadit flow na online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Naklonujte repozitář:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Vytvořte Docker image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Nahrajte Docker image do Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Použití

1. Spusťte Docker kontejner:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Přistupte k aplikaci ve vašem prohlížeči na adrese `http://localhost:8501`.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Celý článek: [RAG s Phi-3-Medium jako Model jako služba z katalogu modelů Azure](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Upozornění**:  
Tento dokument byl přeložen pomocí strojových AI překladových služeb. Ačkoli se snažíme o přesnost, vezměte prosím na vědomí, že automatické překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za autoritativní zdroj. Pro důležité informace se doporučuje profesionální lidský překlad. Nenese odpovědnost za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.