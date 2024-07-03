## RAG with PromptFlow and AISearch

In this example, we will implement a Retrieval Augmented Generation (RAG) application leveraging Phi3 as SLM, AI Search as vectorDB and Prompt Flow as low-code orchestrator.

## Features

- Easy deployment using Docker.
- Scalable architecture for handling AI workflows.
- Low code approach using Prompt Flow

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Docker installed on your local machine.
- An Azure account with permissions to create and manage container resources.
- An Azure AI Studio and Azure AI Search instances
- An embedding model to create your index (can be either an Azure OpenAI embedding or an OS model from the catalog)
- Python 3.8 or later installed on your local machine.
- An Azure Container Registry (or any registry of your choice)

## Installation

1. Create a new flow on your Azure AI Studio Project using the flow.yaml file.
2. Deploy a Phi3 Model from your Azure AI model catalog and create the connection to your project. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Create the vector index on Azure AI Search using any document of your choice [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Deploy the flow on a managed enpoint and use it in the prompt-flow-frontend.py file. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Clone the repository:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Build the Docker image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Push the Docker image to Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Usage

1. Run the Docker container:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Access the application in your browser at `http://localhost:8501`.

## Contact

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Full Article: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)
