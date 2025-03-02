## RAG с PromptFlow и AISearch

В този пример ще реализираме приложение за генериране с подобрен достъп (Retrieval Augmented Generation - RAG), използвайки Phi3 като SLM, AI Search като vectorDB и Prompt Flow като нискокодов оркестратор.

## Характеристики

- Лесно внедряване с помощта на Docker.
- Скалируема архитектура за управление на AI работни потоци.
- Нискокодов подход чрез Prompt Flow.

## Предварителни изисквания

Преди да започнете, уверете се, че сте изпълнили следните изисквания:

- Инсталиран Docker на вашия локален компютър.
- Azure акаунт с права за създаване и управление на контейнерни ресурси.
- Инстанции на Azure AI Studio и Azure AI Search.
- Модел за вграждане, за да създадете вашия индекс (може да бъде Azure OpenAI embedding или OS модел от каталога).
- Инсталиран Python 3.8 или по-нова версия на вашия локален компютър.
- Azure Container Registry (или друг регистър по ваш избор).

## Инсталация

1. Създайте нов flow във вашия проект в Azure AI Studio, използвайки файла flow.yaml.
2. Внедрете модел Phi3 от каталога на модели в Azure AI и създайте връзка с вашия проект. [Внедряване на Phi-3 като Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Създайте векторен индекс в Azure AI Search, използвайки документ по ваш избор. [Създаване на векторен индекс в Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Внедрете flow на управлявана крайна точка и го използвайте във файла prompt-flow-frontend.py. [Внедряване на flow на онлайн крайна точка](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Клонирайте хранилището:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Създайте Docker изображението:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Изпратете Docker изображението в Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Използване

1. Стартирайте Docker контейнера:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Достъпете приложението в браузъра си на адрес `http://localhost:8501`.

## Контакт

Валентина Алто - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Пълна статия: [RAG с Phi-3-Medium като Model as a Service от каталога на модели на Azure](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Отказ от отговорност**:  
Този документ е преведен с помощта на автоматизирани AI услуги за превод. Въпреки че се стремим към точност, моля, имайте предвид, че автоматичните преводи може да съдържат грешки или неточности. Оригиналният документ на неговия оригинален език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален превод от човек. Не носим отговорност за каквито и да било недоразумения или погрешни интерпретации, произтичащи от използването на този превод.