## RAG na PromptFlow na AISearch

Katika mfano huu, tutatekeleza programu ya Retrieval Augmented Generation (RAG) tukitumia Phi3 kama SLM, AI Search kama vectorDB na Prompt Flow kama mpangilio wa msimbo wa chini.

## Vipengele

- Urahisi wa kupeleka kwa kutumia Docker.
- Miundombinu inayoweza kupanuka kushughulikia mchakato wa AI.
- Njia ya msimbo wa chini kwa kutumia Prompt Flow.

## Mahitaji ya Awali

Kabla ya kuanza, hakikisha umetimiza mahitaji yafuatayo:

- Docker imewekwa kwenye kompyuta yako ya eneo-kazi.
- Akaunti ya Azure yenye ruhusa za kuunda na kusimamia rasilimali za kontena.
- Studio ya Azure AI na matukio ya Azure AI Search.
- Mfano wa embedding ili kuunda index yako (unaweza kutumia Azure OpenAI embedding au mfano wa OS kutoka kwenye katalogi).
- Python 3.8 au toleo la juu zaidi limewekwa kwenye kompyuta yako ya eneo-kazi.
- Azure Container Registry (au rejista yoyote unayochagua).

## Ufungaji

1. Unda mtiririko mpya kwenye Mradi wako wa Azure AI Studio ukitumia faili ya flow.yaml.
2. Peleka Mfano wa Phi3 kutoka kwenye katalogi ya mifano ya Azure AI na uunde muunganisho kwenye mradi wako. [Peleka Phi-3 kama Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Unda vector index kwenye Azure AI Search kwa kutumia hati yoyote unayochagua. [Unda vector index kwenye Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Peleka mtiririko kwenye endpoint inayosimamiwa na uitumie kwenye faili ya prompt-flow-frontend.py. [Peleka mtiririko kwenye endpoint ya mtandaoni](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Clone hifadhi:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Jenga picha ya Docker:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Sukuma picha ya Docker kwenye Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Matumizi

1. Endesha kontena la Docker:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Fikia programu kwenye kivinjari chako kwa `http://localhost:8501`.

## Mawasiliano

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Makala Kamili: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Kanusho**:  
Hati hii imetafsiriwa kwa kutumia huduma za tafsiri za AI zinazotegemea mashine. Ingawa tunajitahidi kwa usahihi, tafadhali fahamu kuwa tafsiri za kiotomatiki zinaweza kuwa na makosa au kutokuwa sahihi. Hati ya asili katika lugha yake ya awali inapaswa kuchukuliwa kuwa chanzo cha mamlaka. Kwa habari muhimu, inashauriwa kutumia huduma za wataalamu wa tafsiri ya kibinadamu. Hatutawajibika kwa maelewano mabaya au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.