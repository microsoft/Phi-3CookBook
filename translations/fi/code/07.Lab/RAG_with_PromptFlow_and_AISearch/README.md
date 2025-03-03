## RAG PromptFlowin ja AISearchin kanssa

Tässä esimerkissä toteutamme Retrieval Augmented Generation (RAG) -sovelluksen hyödyntämällä Phi3:a SLM:nä, AI Searchia vektorikantana ja Prompt Flow'ta vähäkoodisena orkestroijana.

## Ominaisuudet

- Helppo käyttöönotto Dockerin avulla.
- Skaalautuva arkkitehtuuri AI-työnkulkujen hallintaan.
- Vähäkoodinen lähestymistapa Prompt Flow'n avulla.

## Esivaatimukset

Ennen kuin aloitat, varmista, että seuraavat vaatimukset täyttyvät:

- Docker on asennettu paikalliselle koneellesi.
- Azure-tili, jolla on oikeudet luoda ja hallita konttien resursseja.
- Azure AI Studio ja Azure AI Search -instanssit.
- Upotemalli indeksin luomiseen (voi olla joko Azure OpenAI:n upote tai OS-malli katalogista).
- Python 3.8 tai uudempi asennettuna paikalliselle koneellesi.
- Azure Container Registry (tai muu valitsemasi rekisteri).

## Asennus

1. Luo uusi työnkulku Azure AI Studio -projektissasi käyttämällä flow.yaml-tiedostoa.
2. Ota käyttöön Phi3-malli Azure AI -mallikatalogista ja muodosta yhteys projektiisi. [Ota Phi-3 käyttöön palvelumallina](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Luo vektori-indeksi Azure AI Searchissa valitsemallasi dokumentilla. [Luo vektori-indeksi Azure AI Searchissa](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Ota työnkulku käyttöön hallitulla päätepisteellä ja käytä sitä prompt-flow-frontend.py-tiedostossa. [Ota työnkulku käyttöön verkossa](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Kloonaa arkisto:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Rakenna Docker-kuva:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Työnnä Docker-kuva Azure Container Registryyn:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Käyttö

1. Käynnistä Docker-kontti:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Avaa sovellus selaimessa osoitteessa `http://localhost:8501`.

## Yhteystiedot

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Koko artikkeli: [RAG Phi-3-Mediumilla palvelumallina Azure Model Catalogista](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty konepohjaisilla tekoälykäännöspalveluilla. Vaikka pyrimme tarkkuuteen, huomioithan, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäisellä kielellä tulee pitää ensisijaisena lähteenä. Tärkeää tietoa varten suositellaan ammattimaista ihmisen tekemää käännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinkäsityksistä tai virhetulkinnoista.