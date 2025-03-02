## RAG cu PromptFlow și AISearch

În acest exemplu, vom implementa o aplicație de Generare Augmentată prin Recuperare (RAG) folosind Phi3 ca SLM, AI Search ca vectorDB și Prompt Flow ca orchestrator low-code.

## Funcționalități

- Implementare ușoară utilizând Docker.
- Arhitectură scalabilă pentru gestionarea fluxurilor de lucru AI.
- Abordare low-code folosind Prompt Flow.

## Cerințe preliminare

Înainte de a începe, asigurați-vă că ați îndeplinit următoarele cerințe:

- Docker instalat pe mașina dvs. locală.
- Un cont Azure cu permisiuni pentru a crea și gestiona resurse de containere.
- Instanțe Azure AI Studio și Azure AI Search.
- Un model de embedding pentru a crea indexul (poate fi un embedding Azure OpenAI sau un model OS din catalog).
- Python 3.8 sau o versiune mai recentă instalată pe mașina dvs. locală.
- Un Azure Container Registry (sau orice registry la alegerea dvs.).

## Instalare

1. Creați un nou flow în Proiectul dvs. Azure AI Studio folosind fișierul flow.yaml.
2. Implementați un Model Phi3 din catalogul de modele Azure AI și creați conexiunea la proiectul dvs. [Implementați Phi-3 ca Model ca Serviciu](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Creați indexul vectorial în Azure AI Search folosind orice document la alegerea dvs. [Creați un index vectorial în Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Implementați flow-ul pe un endpoint gestionat și utilizați-l în fișierul prompt-flow-frontend.py. [Implementați un flow pe un endpoint online](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Clonați repository-ul:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Construiți imaginea Docker:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Împingeți imaginea Docker în Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Utilizare

1. Rulați containerul Docker:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Accesați aplicația în browser la `http://localhost:8501`.

## Contact

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Articol complet: [RAG cu Phi-3-Medium ca Model ca Serviciu din Catalogul de Modele Azure](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Declinarea responsabilității**:  
Acest document a fost tradus folosind servicii de traducere bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa maternă, ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea umană realizată de un profesionist. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite rezultate din utilizarea acestei traduceri.