## RAG con PromptFlow y AISearch

En este ejemplo, implementaremos una aplicación de Generación Aumentada por Recuperación (RAG) utilizando Phi3 como SLM, AI Search como vectorDB y Prompt Flow como orquestador de bajo código.

## Características

- Despliegue sencillo usando Docker.
- Arquitectura escalable para manejar flujos de trabajo de IA.
- Enfoque de bajo código usando Prompt Flow.

## Requisitos Previos

Antes de comenzar, asegúrate de cumplir con los siguientes requisitos:

- Docker instalado en tu máquina local.
- Una cuenta de Azure con permisos para crear y gestionar recursos de contenedores.
- Instancias de Azure AI Studio y Azure AI Search.
- Un modelo de embeddings para crear tu índice (puede ser un embedding de Azure OpenAI o un modelo OS del catálogo).
- Python 3.8 o posterior instalado en tu máquina local.
- Un Azure Container Registry (o cualquier registro de tu elección).

## Instalación

1. Crea un nuevo flujo en tu proyecto de Azure AI Studio usando el archivo flow.yaml.
2. Despliega un modelo Phi3 desde tu catálogo de modelos de Azure AI y crea la conexión con tu proyecto. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Crea el índice vectorial en Azure AI Search usando cualquier documento de tu elección. [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Despliega el flujo en un endpoint gestionado y úsalo en el archivo prompt-flow-frontend.py. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Clona el repositorio:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Construye la imagen de Docker:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Empuja la imagen de Docker a Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Uso

1. Ejecuta el contenedor Docker:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Accede a la aplicación en tu navegador en `http://localhost:8501`.

## Contacto

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Artículo completo: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

Aviso legal: La traducción fue realizada por un modelo de IA y puede no ser perfecta. Por favor, revise el resultado y haga las correcciones necesarias.