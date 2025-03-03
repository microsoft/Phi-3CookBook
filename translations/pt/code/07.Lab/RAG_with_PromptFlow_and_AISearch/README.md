## RAG com PromptFlow e AISearch

Neste exemplo, implementaremos uma aplicação de Geração Aumentada por Recuperação (RAG) utilizando o Phi3 como SLM, o AI Search como vectorDB e o Prompt Flow como orquestrador de baixo código.

## Funcionalidades

- Implantação fácil usando Docker.
- Arquitetura escalável para gerenciar fluxos de trabalho de IA.
- Abordagem de baixo código com o Prompt Flow.

## Pré-requisitos

Antes de começar, certifique-se de atender aos seguintes requisitos:

- Docker instalado em sua máquina local.
- Uma conta Azure com permissões para criar e gerenciar recursos de contêiner.
- Instâncias do Azure AI Studio e Azure AI Search.
- Um modelo de embeddings para criar seu índice (pode ser um embedding do Azure OpenAI ou um modelo de código aberto do catálogo).
- Python 3.8 ou superior instalado em sua máquina local.
- Um Azure Container Registry (ou qualquer registro de sua escolha).

## Instalação

1. Crie um novo fluxo no seu projeto do Azure AI Studio usando o arquivo flow.yaml.
2. Implemente um modelo Phi3 a partir do catálogo de modelos do Azure AI e conecte-o ao seu projeto. [Implantar Phi-3 como um Modelo como Serviço](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Crie o índice vetorial no Azure AI Search usando qualquer documento de sua escolha. [Criar um índice vetorial no Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Implemente o fluxo em um endpoint gerenciado e use-o no arquivo prompt-flow-frontend.py. [Implantar um fluxo em um endpoint online](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Clone o repositório:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Construa a imagem Docker:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Envie a imagem Docker para o Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Uso

1. Execute o contêiner Docker:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Acesse a aplicação no seu navegador em `http://localhost:8501`.

## Contato

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Artigo Completo: [RAG com Phi-3-Medium como Modelo como Serviço do Catálogo de Modelos do Azure](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução automática baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte oficial. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.