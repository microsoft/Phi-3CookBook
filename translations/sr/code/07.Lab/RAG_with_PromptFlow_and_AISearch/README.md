## RAG sa PromptFlow i AISearch

U ovom primeru implementiraćemo aplikaciju za generaciju sa obogaćenim pretraživanjem (RAG) koristeći Phi3 kao SLM, AI Search kao vectorDB i Prompt Flow kao nisko-kodni orkestrator.

## Karakteristike

- Jednostavno postavljanje pomoću Dockera.
- Skalabilna arhitektura za upravljanje AI tokovima rada.
- Nisko-kodni pristup korišćenjem Prompt Flow-a.

## Preduslovi

Pre nego što počnete, uverite se da imate sledeće:

- Docker instaliran na vašem lokalnom računaru.
- Azure nalog sa dozvolama za kreiranje i upravljanje resursima kontejnera.
- Azure AI Studio i Azure AI Search instance.
- Model za kreiranje ugrađivanja (može biti ili Azure OpenAI embedding ili OS model iz kataloga).
- Python 3.8 ili noviji instaliran na vašem lokalnom računaru.
- Azure Container Registry (ili bilo koji registar po vašem izboru).

## Instalacija

1. Kreirajte novi tok u svom Azure AI Studio projektu koristeći datoteku flow.yaml.
2. Postavite Phi3 model iz vašeg Azure AI kataloga modela i povežite ga sa svojim projektom. [Postavite Phi-3 kao Model kao Servis](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Kreirajte vektorski indeks na Azure AI Search koristeći bilo koji dokument po vašem izboru [Kreirajte vektorski indeks na Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Postavite tok na upravljani endpoint i koristite ga u fajlu prompt-flow-frontend.py. [Postavite tok na online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Klonirajte repozitorijum:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Kreirajte Docker sliku:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Pošaljite Docker sliku u Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Upotreba

1. Pokrenite Docker kontejner:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Pristupite aplikaciji u vašem pregledaču na `http://localhost:8501`.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Ceo članak: [RAG sa Phi-3-Medium kao Model kao Servis iz Azure kataloga modela](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем услуга машинског превођења заснованих на вештачкој интелигенцији. Иако настојимо да обезбедимо тачност, молимо вас да будете свесни да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на свом изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални превод од стране људи. Не сносимо одговорност за било какве неспоразуме или погрешна тумачења настала услед коришћења овог превода.