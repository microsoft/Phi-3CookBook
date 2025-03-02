## RAG with PromptFlow and AISearch

In this example, we will build a Retrieval Augmented Generation (RAG) application using Phi3 as the SLM, AI Search as the vector database, and Prompt Flow as a low-code orchestrator.

## Features

- Simple deployment using Docker.
- Scalable architecture to manage AI workflows.
- Low-code approach with Prompt Flow.

## Prerequisites

Before starting, make sure you have the following:

- Docker installed on your local machine.
- An Azure account with permissions to create and manage container resources.
- Instances of Azure AI Studio and Azure AI Search.
- An embedding model to create your index (this can be an Azure OpenAI embedding or an OS model from the catalog).
- Python 3.8 or later installed on your local machine.
- An Azure Container Registry (or any other registry you prefer).

## Installation

1. Create a new flow in your Azure AI Studio project using the flow.yaml file.
2. Deploy a Phi3 Model from your Azure AI model catalog and connect it to your project. [Deploy Phi-3 as a Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Create a vector index in Azure AI Search using any document you prefer. [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Deploy the flow on a managed endpoint and use it in the prompt-flow-frontend.py file. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
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

2. Open the application in your browser at `http://localhost:8501`.

## Contact

Valentina Alto - [LinkedIn](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Full Article: [RAG with Phi-3-Medium as a Model as a Service from Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please note that automated translations may contain errors or inaccuracies. The original document in its native language should be regarded as the authoritative source. For critical information, professional human translation is recommended. We are not responsible for any misunderstandings or misinterpretations resulting from the use of this translation.