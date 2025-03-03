## RAG ਨਾਲ PromptFlow ਅਤੇ AISearch

ਇਸ ਉਦਾਹਰਨ ਵਿੱਚ, ਅਸੀਂ Retrieval Augmented Generation (RAG) ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਲਾਗੂ ਕਰਾਂਗੇ, ਜੋ Phi3 ਨੂੰ SLM ਵਜੋਂ, AI Search ਨੂੰ vectorDB ਵਜੋਂ ਅਤੇ Prompt Flow ਨੂੰ low-code orchestrator ਵਜੋਂ ਵਰਤਦਾ ਹੈ।

## ਖਾਸੀਅਤਾਂ

- Docker ਦੀ ਵਰਤੋਂ ਨਾਲ ਆਸਾਨ ਤਰੀਕੇ ਨਾਲ ਡਿਪਲੌਇਮੈਂਟ।
- AI ਵਰਕਫਲੋਜ਼ ਨੂੰ ਸੰਭਾਲਣ ਲਈ ਸਕੇਲਬਲ ਆਰਕੀਟੈਕਚਰ।
- Prompt Flow ਦੀ ਵਰਤੋਂ ਨਾਲ ਘੱਟ ਕੋਡ ਵਾਲਾ ਤਰੀਕਾ।

## ਜ਼ਰੂਰੀ ਤਿਆਰੀ

ਸ਼ੁਰੂ ਕਰਨ ਤੋਂ ਪਹਿਲਾਂ, ਇਹ ਯਕੀਨੀ ਬਣਾਓ ਕਿ ਤੁਸੀਂ ਹੇਠ ਲਿਖੀਆਂ ਲੋੜਾਂ ਨੂੰ ਪੂਰਾ ਕੀਤਾ ਹੈ:

- ਤੁਹਾਡੀ ਲੋਕਲ ਮਸ਼ੀਨ 'ਤੇ Docker ਇੰਸਟਾਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।
- ਇੱਕ Azure ਖਾਤਾ ਜਿਸ ਵਿੱਚ ਕੰਟੇਨਰ ਸਰੋਤ ਬਣਾਉਣ ਅਤੇ ਪ੍ਰਬੰਧਨ ਕਰਨ ਦੀ ਇਜਾਜ਼ਤ ਹੋਵੇ।
- Azure AI Studio ਅਤੇ Azure AI Search ਇੰਸਟੈਂਸ।
- ਆਪਣਾ ਇੰਡੈਕਸ ਬਣਾਉਣ ਲਈ ਇੱਕ embedding ਮਾਡਲ (ਜੋ Azure OpenAI embedding ਜਾਂ catalog ਵਿੱਚੋਂ ਕੋਈ OS ਮਾਡਲ ਹੋ ਸਕਦਾ ਹੈ)।
- ਤੁਹਾਡੀ ਲੋਕਲ ਮਸ਼ੀਨ 'ਤੇ Python 3.8 ਜਾਂ ਇਸ ਤੋਂ ਉੱਪਰ ਵਰਜਨ ਇੰਸਟਾਲ ਹੋਣਾ ਚਾਹੀਦਾ ਹੈ।
- ਇੱਕ Azure Container Registry (ਜਾਂ ਤੁਹਾਡੀ ਪਸੰਦ ਦਾ ਕੋਈ ਵੀ ਰਜਿਸਟਰੀ)।

## ਇੰਸਟਾਲੇਸ਼ਨ

1. ਆਪਣੇ Azure AI Studio ਪ੍ਰੋਜੈਕਟ ਵਿੱਚ flow.yaml ਫਾਇਲ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਇੱਕ ਨਵਾਂ ਫਲੋ ਬਣਾਓ।
2. ਆਪਣੇ Azure AI ਮਾਡਲ catalog ਤੋਂ ਇੱਕ Phi3 ਮਾਡਲ ਡਿਪਲੌਇ ਕਰੋ ਅਤੇ ਇਸ ਨੂੰ ਆਪਣੇ ਪ੍ਰੋਜੈਕਟ ਨਾਲ ਕਨੈਕਟ ਕਰੋ। [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. ਆਪਣੇ ਚੋਣ ਦੇ ਕਿਸੇ ਵੀ ਡੌਕਯੂਮੈਂਟ ਦੀ ਵਰਤੋਂ ਕਰਕੇ Azure AI Search 'ਤੇ ਇੱਕ vector ਇੰਡੈਕਸ ਬਣਾਓ। [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. ਫਲੋ ਨੂੰ ਇੱਕ managed endpoint 'ਤੇ ਡਿਪਲੌਇ ਕਰੋ ਅਤੇ ਇਸ ਨੂੰ prompt-flow-frontend.py ਫਾਇਲ ਵਿੱਚ ਵਰਤੋ। [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. ਰਿਪੋਜ਼ਟਰੀ ਕਲੋਨ ਕਰੋ:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Docker ਇਮੇਜ ਬਣਾਓ:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Docker ਇਮੇਜ ਨੂੰ Azure Container Registry 'ਤੇ ਪੂਸ਼ ਕਰੋ:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## ਵਰਤੋਂ

1. Docker ਕੰਟੇਨਰ ਚਲਾਓ:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. ਆਪਣੇ ਬ੍ਰਾਊਜ਼ਰ ਵਿੱਚ ਐਪਲੀਕੇਸ਼ਨ ਨੂੰ ਇਸ ਪਤੇ 'ਤੇ ਖੋਲ੍ਹੋ: `http://localhost:8501`।

## ਸੰਪਰਕ

ਵਾਲੈਂਟੀਨਾ ਅਲਟੋ - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

ਪੂਰਾ ਲੇਖ: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**ਅਸਵੀਕਾਰਣਾ**:  
ਇਹ ਦਸਤਾਵੇਜ਼ ਮਸ਼ੀਨ-ਆਧਾਰਿਤ AI ਅਨੁਵਾਦ ਸੇਵਾਵਾਂ ਦੀ ਵਰਤੋਂ ਕਰਕੇ ਅਨੁਵਾਦ ਕੀਤਾ ਗਿਆ ਹੈ। ਜਦੋਂ ਕਿ ਅਸੀਂ ਸਹੀ ਹੋਣ ਦਾ ਯਤਨ ਕਰਦੇ ਹਾਂ, ਕਿਰਪਾ ਕਰਕੇ ਧਿਆਨ ਵਿੱਚ ਰੱਖੋ ਕਿ ਆਟੋਮੇਟਿਕ ਅਨੁਵਾਦਾਂ ਵਿੱਚ ਗਲਤੀਆਂ ਜਾਂ ਅਸੁੱਚੀਤਤਾਵਾਂ ਹੋ ਸਕਦੀਆਂ ਹਨ। ਇਸ ਦੀ ਮੂਲ ਭਾਸ਼ਾ ਵਿੱਚ ਮੌਜੂਦ ਮੂਲ ਦਸਤਾਵੇਜ਼ ਨੂੰ ਅਧਿਕਾਰਤ ਸਰੋਤ ਮੰਨਿਆ ਜਾਣਾ ਚਾਹੀਦਾ ਹੈ। ਮਹੱਤਵਪੂਰਨ ਜਾਣਕਾਰੀ ਲਈ, ਪੇਸ਼ੇਵਰ ਮਨੁੱਖੀ ਅਨੁਵਾਦ ਦੀ ਸਿਫਾਰਸ਼ ਕੀਤੀ ਜਾਂਦੀ ਹੈ। ਇਸ ਅਨੁਵਾਦ ਦੇ ਉਪਯੋਗ ਤੋਂ ਪੈਦਾ ਹੋਣ ਵਾਲੀਆਂ ਕਿਸੇ ਵੀ ਗਲਤ ਫਹਿਮੀਆਂ ਜਾਂ ਗਲਤ ਵਿਆਖਿਆਵਾਂ ਲਈ ਅਸੀਂ ਜ਼ਿੰਮੇਵਾਰ ਨਹੀਂ ਹਾਂ।