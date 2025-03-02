## RAG avec PromptFlow et AISearch

Dans cet exemple, nous allons mettre en œuvre une application de génération augmentée par récupération (RAG) en utilisant Phi3 comme SLM, AI Search comme vectorDB et Prompt Flow comme orchestrateur low-code.

## Fonctionnalités

- Déploiement facile avec Docker.
- Architecture évolutive pour gérer les flux de travail d'IA.
- Approche low-code avec Prompt Flow.

## Prérequis

Avant de commencer, assurez-vous de répondre aux exigences suivantes :

- Docker installé sur votre machine locale.
- Un compte Azure avec les permissions pour créer et gérer des ressources de conteneurs.
- Des instances Azure AI Studio et Azure AI Search.
- Un modèle d'embedding pour créer votre index (peut être un embedding Azure OpenAI ou un modèle open source du catalogue).
- Python 3.8 ou une version ultérieure installé sur votre machine locale.
- Un Azure Container Registry (ou tout autre registre de votre choix).

## Installation

1. Créez un nouveau flux dans votre projet Azure AI Studio en utilisant le fichier flow.yaml.
2. Déployez un modèle Phi3 depuis le catalogue de modèles Azure AI et créez la connexion à votre projet. [Déployer Phi-3 comme modèle en tant que service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Créez l'index vectoriel sur Azure AI Search en utilisant un document de votre choix. [Créer un index vectoriel sur Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Déployez le flux sur un endpoint managé et utilisez-le dans le fichier prompt-flow-frontend.py. [Déployer un flux sur un endpoint en ligne](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Clonez le dépôt :

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Construisez l'image Docker :

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Poussez l'image Docker vers Azure Container Registry :

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Utilisation

1. Exécutez le conteneur Docker :

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Accédez à l'application dans votre navigateur à l'adresse `http://localhost:8501`.

## Contact

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Article complet : [RAG avec Phi-3-Medium comme modèle en tant que service depuis le catalogue de modèles Azure](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée par intelligence artificielle. Bien que nous fassions de notre mieux pour garantir l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.