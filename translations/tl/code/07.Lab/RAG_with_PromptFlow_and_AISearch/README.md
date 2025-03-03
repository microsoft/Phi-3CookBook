## RAG gamit ang PromptFlow at AISearch

Sa halimbawang ito, ipapakita natin kung paano magpatupad ng Retrieval Augmented Generation (RAG) application gamit ang Phi3 bilang SLM, AI Search bilang vectorDB, at Prompt Flow bilang low-code orchestrator.

## Mga Tampok

- Madaling deployment gamit ang Docker.
- Scalable na arkitektura para sa paghawak ng mga AI workflow.
- Low code na diskarte gamit ang Prompt Flow.

## Mga Kinakailangan

Bago ka magsimula, tiyaking natugunan mo ang mga sumusunod na kinakailangan:

- Nakainstall ang Docker sa iyong lokal na makina.
- Isang Azure account na may pahintulot na lumikha at mag-manage ng container resources.
- Mga instance ng Azure AI Studio at Azure AI Search.
- Isang embedding model para gumawa ng iyong index (maaaring Azure OpenAI embedding o isang OS model mula sa catalog).
- Nakainstall ang Python 3.8 o mas bago sa iyong lokal na makina.
- Isang Azure Container Registry (o anumang registry na iyong pipiliin).

## Pag-install

1. Gumawa ng bagong flow sa iyong Azure AI Studio Project gamit ang flow.yaml file.
2. I-deploy ang Phi3 Model mula sa iyong Azure AI model catalog at ikonekta ito sa iyong proyekto. [I-deploy ang Phi-3 bilang Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Gumawa ng vector index sa Azure AI Search gamit ang anumang dokumento na iyong napili. [Gumawa ng vector index sa Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. I-deploy ang flow sa isang managed endpoint at gamitin ito sa prompt-flow-frontend.py file. [I-deploy ang flow sa isang online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. I-clone ang repositoryo:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. I-build ang Docker image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. I-push ang Docker image sa Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Paggamit

1. Patakbuhin ang Docker container:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. I-access ang application sa iyong browser sa `http://localhost:8501`.

## Kontak

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Buong Artikulo: [RAG gamit ang Phi-3-Medium bilang Model as a Service mula sa Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyo ng AI na batay sa makina. Habang pinagsisikapan naming maging tumpak, pakatandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatugma. Ang orihinal na dokumento sa sariling wika nito ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Kami ay hindi mananagot para sa anumang hindi pagkakaintindihan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.