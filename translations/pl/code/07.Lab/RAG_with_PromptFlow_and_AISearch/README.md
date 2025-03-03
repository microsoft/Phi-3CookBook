## RAG z PromptFlow i AISearch

W tym przykładzie zaimplementujemy aplikację Retrieval Augmented Generation (RAG), wykorzystując Phi3 jako SLM, AI Search jako vectorDB oraz Prompt Flow jako niskokodowy orkiestrator.

## Funkcje

- Łatwa instalacja przy użyciu Dockera.
- Skalowalna architektura do obsługi przepływów pracy związanych ze sztuczną inteligencją.
- Podejście niskokodowe z wykorzystaniem Prompt Flow.

## Wymagania wstępne

Przed rozpoczęciem upewnij się, że spełniasz następujące wymagania:

- Zainstalowany Docker na twoim komputerze lokalnym.
- Konto Azure z uprawnieniami do tworzenia i zarządzania zasobami kontenerowymi.
- Instancje Azure AI Studio i Azure AI Search.
- Model osadzający do stworzenia indeksu (może to być Azure OpenAI embedding lub model OS z katalogu).
- Python w wersji 3.8 lub nowszej zainstalowany na twoim komputerze lokalnym.
- Azure Container Registry (lub dowolny inny rejestr według wyboru).

## Instalacja

1. Utwórz nowy przepływ w swoim projekcie Azure AI Studio, używając pliku flow.yaml.
2. Wdróż model Phi3 z katalogu modeli Azure AI i połącz go ze swoim projektem. [Wdróż Phi-3 jako Model jako Usługa](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Utwórz indeks wektorowy w Azure AI Search, używając dowolnego dokumentu. [Utwórz indeks wektorowy w Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Wdróż przepływ na zarządzanym punkcie końcowym i użyj go w pliku prompt-flow-frontend.py. [Wdróż przepływ na punkcie końcowym online](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Sklonuj repozytorium:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Zbuduj obraz Dockera:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Wypchnij obraz Dockera do Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Użycie

1. Uruchom kontener Dockera:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Otwórz aplikację w przeglądarce pod adresem `http://localhost:8501`.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Pełny artykuł: [RAG z Phi-3-Medium jako Model jako Usługa z katalogu modeli Azure](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony za pomocą usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż dokładamy starań, aby tłumaczenie było precyzyjne, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiążące źródło. W przypadku kluczowych informacji zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.