## RAG z uporabo PromptFlow in AISearch

V tem primeru bomo implementirali aplikacijo za generiranje z razširjenim pridobivanjem (Retrieval Augmented Generation - RAG), ki uporablja Phi3 kot SLM, AI Search kot vectorDB in Prompt Flow kot nizkokodni orkestrator.

## Funkcionalnosti

- Enostavna uvedba z uporabo Dockerja.
- Prilagodljiva arhitektura za upravljanje AI delovnih tokov.
- Nizkokodni pristop z uporabo Prompt Flow.

## Predpogoji

Preden začnete, poskrbite, da izpolnjujete naslednje zahteve:

- Na svojem lokalnem računalniku imate nameščen Docker.
- Imate Azure račun z dovoljenji za ustvarjanje in upravljanje virov vsebnikov.
- Imate Azure AI Studio in Azure AI Search instance.
- Imate model za vgrajevanje za ustvarjanje svojega indeksa (lahko je Azure OpenAI vgrajevanje ali OS model iz kataloga).
- Na svojem lokalnem računalniku imate nameščen Python 3.8 ali novejši.
- Imate Azure Container Registry (ali kateri koli drug register po vaši izbiri).

## Namestitev

1. Ustvarite nov tok v svojem projektu Azure AI Studio z uporabo datoteke flow.yaml.
2. Uvedite Phi3 model iz kataloga modelov Azure AI in ustvarite povezavo s svojim projektom. [Uvedba Phi-3 kot Model kot storitev](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Ustvarite vektorski indeks na Azure AI Search z uporabo katerega koli dokumenta po vaši izbiri. [Ustvarjanje vektorskega indeksa na Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Uvedite tok na upravljanem končnem mestu in ga uporabite v datoteki prompt-flow-frontend.py. [Uvedba toka na spletnem končnem mestu](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Klonirajte repozitorij:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Ustvarite Docker sliko:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Potisnite Docker sliko v Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Uporaba

1. Zaženite Docker vsebnik:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Dostopajte do aplikacije v svojem brskalniku na `http://localhost:8501`.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Celoten članek: [RAG z uporabo Phi-3-Medium kot Model kot storitev iz Azure Model Kataloga](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitev strojnega prevajanja z umetno inteligenco. Čeprav si prizadevamo za natančnost, vas prosimo, da se zavedate, da lahko avtomatski prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem izvirnem jeziku naj velja za avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.