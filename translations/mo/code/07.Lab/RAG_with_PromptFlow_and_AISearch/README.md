## RAG miaraka amin'ny PromptFlow sy AISearch

Amin'ity ohatra ity, dia hampihatra fampiharana Retrieval Augmented Generation (RAG) isika, mampiasa Phi3 ho SLM, AI Search ho vectorDB, ary Prompt Flow ho mpandrindra low-code.

## Toetoetra

- Fametrahana mora amin'ny alàlan'ny Docker.
- Rafitra azo ampitomboina mba handraisana ireo asa mifandraika amin'ny AI.
- Fomba fohy amin'ny fampiasana Prompt Flow.

## Takiana alohan'ny hanombohana

Alohan'ny hanombohanao, ataovy azo antoka fa manana ireto manaraka ireto ianao:

- Docker napetraka amin'ny solosainao.
- Kaonty Azure miaraka amin'ny alalana hamorona sy hitantana loharano anaty container.
- Azure AI Studio sy Azure AI Search efa misy.
- Modely embedding hanaovana ny index anao (azo avy amin'ny Azure OpenAI embedding na avy amin'ny OS modely ao amin'ny catalog).
- Python 3.8 na dikan-teny farany kokoa napetraka amin'ny solosainao.
- Azure Container Registry (na registry hafa araka izay tianao).

## Fametrahana

1. Mamoròna flow vaovao ao amin'ny tetikasa Azure AI Studio anao amin'ny alàlan'ny rakitra flow.yaml.
2. Mametraha Phi3 Model avy amin'ny catalog modely Azure AI anao ary mamoròna fifandraisana amin'ny tetikasanao. [Mametraha Phi-3 ho Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Mamoròna vector index ao amin'ny Azure AI Search mampiasa rakitra tianao. [Mamoròna vector index ao amin'ny Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Alefaso ny flow amin'ny managed endpoint ary ampiasao ao amin'ny rakitra prompt-flow-frontend.py. [Alefaso ny flow amin'ny online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Clone-o ny repository:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Amboary ny Docker image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Alefaso ny Docker image ao amin'ny Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Fampiasana

1. Alefaso ny Docker container:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Jereo ao amin'ny tranonkalanao amin'ny alàlan'ny `http://localhost:8501`.

## Fifandraisana

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Lahatsoratra feno: [RAG miaraka amin'ny Phi-3-Medium ho Model as a Service avy amin'ny Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

It seems like you might be asking for a translation into "mo," but it's unclear what language "mo" refers to. Could you clarify which language you'd like this text translated into? For example, is it Maori, Mongolian, or something else?