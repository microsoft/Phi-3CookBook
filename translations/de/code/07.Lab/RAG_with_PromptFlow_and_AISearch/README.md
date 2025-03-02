## RAG mit PromptFlow und AISearch

In diesem Beispiel implementieren wir eine Retrieval Augmented Generation (RAG)-Anwendung, die Phi3 als SLM, AI Search als VectorDB und Prompt Flow als Low-Code-Orchestrator nutzt.

## Funktionen

- Einfache Bereitstellung mit Docker.
- Skalierbare Architektur für die Verarbeitung von KI-Workflows.
- Low-Code-Ansatz mit Prompt Flow.

## Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass Sie die folgenden Anforderungen erfüllt haben:

- Docker auf Ihrem lokalen Rechner installiert.
- Ein Azure-Konto mit Berechtigungen zum Erstellen und Verwalten von Container-Ressourcen.
- Eine Azure AI Studio- und Azure AI Search-Instanz.
- Ein Embedding-Modell, um Ihren Index zu erstellen (entweder ein Azure OpenAI Embedding oder ein OS-Modell aus dem Katalog).
- Python 3.8 oder höher auf Ihrem lokalen Rechner installiert.
- Ein Azure Container Registry (oder ein beliebiges Registry Ihrer Wahl).

## Installation

1. Erstellen Sie einen neuen Flow in Ihrem Azure AI Studio-Projekt mithilfe der Datei flow.yaml.
2. Stellen Sie ein Phi3-Modell aus Ihrem Azure AI-Modellkatalog bereit und erstellen Sie die Verbindung zu Ihrem Projekt. [Phi-3 als Modell als Service bereitstellen](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Erstellen Sie den Vektorindex in Azure AI Search mit einem beliebigen Dokument Ihrer Wahl. [Einen Vektorindex in Azure AI Search erstellen](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Stellen Sie den Flow auf einem verwalteten Endpunkt bereit und verwenden Sie ihn in der Datei prompt-flow-frontend.py. [Einen Flow auf einem Online-Endpunkt bereitstellen](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Klonen Sie das Repository:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Erstellen Sie das Docker-Image:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Pushen Sie das Docker-Image in das Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Nutzung

1. Starten Sie den Docker-Container:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Greifen Sie über Ihren Browser auf die Anwendung zu unter `http://localhost:8501`.

## Kontakt

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Vollständiger Artikel: [RAG mit Phi-3-Medium als Modell als Service aus dem Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-basierten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, beachten Sie bitte, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die aus der Nutzung dieser Übersetzung entstehen.