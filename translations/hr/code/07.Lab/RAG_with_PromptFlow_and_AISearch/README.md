## RAG s PromptFlow i AISearch

U ovom primjeru implementirat ćemo aplikaciju Retrieval Augmented Generation (RAG) koristeći Phi3 kao SLM, AI Search kao vectorDB i Prompt Flow kao low-code orkestrator.

## Značajke

- Jednostavno postavljanje pomoću Dockera.
- Skalabilna arhitektura za upravljanje AI radnim procesima.
- Pristup s malo koda koristeći Prompt Flow.

## Preduvjeti

Prije nego što započnete, provjerite jeste li ispunili sljedeće zahtjeve:

- Docker instaliran na vašem lokalnom računalu.
- Azure račun s dozvolama za kreiranje i upravljanje resursima u spremnicima.
- Azure AI Studio i Azure AI Search instance.
- Model za stvaranje ugrađivanja kako biste kreirali svoj indeks (može biti Azure OpenAI embedding ili OS model iz kataloga).
- Python 3.8 ili novija verzija instalirana na vašem lokalnom računalu.
- Azure Container Registry (ili bilo koji drugi registar po vašem izboru).

## Instalacija

1. Kreirajte novi flow u svom projektu na Azure AI Studio koristeći datoteku flow.yaml.
2. Implementirajte Phi3 model iz kataloga modela Azure AI i povežite ga sa svojim projektom. [Implementirajte Phi-3 kao Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Kreirajte vektorski indeks na Azure AI Search koristeći bilo koji dokument po vašem izboru. [Kreirajte vektorski indeks na Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Implementirajte flow na upravljanu krajnju točku i koristite ga u datoteci prompt-flow-frontend.py. [Implementirajte flow na online krajnju točku](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Klonirajte repozitorij:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Izgradite Docker sliku:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Pošaljite Docker sliku u Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Korištenje

1. Pokrenite Docker spremnik:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Pristupite aplikaciji u svom pregledniku na `http://localhost:8501`.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Cijeli članak: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Odricanje od odgovornosti**:  
Ovaj dokument je preveden korištenjem usluga strojno vođenog AI prevođenja. Iako nastojimo osigurati točnost, imajte na umu da automatski prijevodi mogu sadržavati pogreške ili netočnosti. Izvorni dokument na izvornom jeziku treba smatrati mjerodavnim izvorom. Za ključne informacije preporučuje se profesionalni prijevod od strane ljudskog prevoditelja. Ne preuzimamo odgovornost za nesporazume ili pogrešna tumačenja koja mogu proizaći iz korištenja ovog prijevoda.