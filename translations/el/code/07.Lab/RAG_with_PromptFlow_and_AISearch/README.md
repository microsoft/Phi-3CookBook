## RAG με PromptFlow και AISearch

Σε αυτό το παράδειγμα, θα υλοποιήσουμε μια εφαρμογή Retrieval Augmented Generation (RAG) αξιοποιώντας το Phi3 ως SLM, το AI Search ως vectorDB και το Prompt Flow ως low-code orchestrator.

## Χαρακτηριστικά

- Εύκολη ανάπτυξη με χρήση Docker.
- Επεκτάσιμη αρχιτεκτονική για διαχείριση AI workflows.
- Προσέγγιση χαμηλού κώδικα με χρήση Prompt Flow.

## Προαπαιτούμενα

Πριν ξεκινήσετε, βεβαιωθείτε ότι πληρούνται οι παρακάτω απαιτήσεις:

- Εγκατεστημένο Docker στον υπολογιστή σας.
- Λογαριασμός Azure με δικαιώματα δημιουργίας και διαχείρισης πόρων container.
- Ενεργές υπηρεσίες Azure AI Studio και Azure AI Search.
- Ένα embedding model για τη δημιουργία του index σας (μπορεί να είναι είτε embedding από το Azure OpenAI είτε μοντέλο από τον κατάλογο OS).
- Εγκατεστημένο Python 3.8 ή νεότερη έκδοση στον υπολογιστή σας.
- Ένα Azure Container Registry (ή οποιοδήποτε registry της επιλογής σας).

## Εγκατάσταση

1. Δημιουργήστε ένα νέο flow στο Azure AI Studio Project σας χρησιμοποιώντας το αρχείο flow.yaml.
2. Αναπτύξτε ένα μοντέλο Phi3 από τον κατάλογο μοντέλων του Azure AI και δημιουργήστε τη σύνδεση με το project σας. [Deploy Phi-3 ως Model as a Service](https://learn.microsoft.com/azure/machine-learning/how-to-deploy-models-phi-3?view=azureml-api-2&tabs=phi-3-mini)
3. Δημιουργήστε τον vector index στο Azure AI Search χρησιμοποιώντας οποιοδήποτε έγγραφο της επιλογής σας. [Create a vector index on Azure AI Search](https://learn.microsoft.com/azure/search/search-how-to-create-search-index?tabs=portal)
4. Αναπτύξτε το flow σε ένα managed endpoint και χρησιμοποιήστε το στο αρχείο prompt-flow-frontend.py. [Deploy a flow on an online endpoint](https://learn.microsoft.com/azure/ai-studio/how-to/flow-deploy)
5. Κλωνοποιήστε το αποθετήριο:

    ```sh
    git clone [[https://github.com/yourusername/prompt-flow-frontend.git](https://github.com/microsoft/Phi-3CookBook.git)](https://github.com/microsoft/Phi-3CookBook.git)
    
    cd code/07.Lab/RAG with PromptFlow and AISearch
    ```

6. Δημιουργήστε την εικόνα Docker:

    ```sh
    docker build -t prompt-flow-frontend.py .
    ```

7. Ανεβάστε την εικόνα Docker στο Azure Container Registry:

    ```sh
    az acr login --name yourregistry
    
    docker tag prompt-flow-frontend.py:latest yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    
    docker push yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

## Χρήση

1. Τρέξτε το container Docker:

    ```sh
    docker run -p 8501:8501 yourregistry.azurecr.io/prompt-flow-frontend.py:latest
    ```

2. Ανοίξτε την εφαρμογή στον περιηγητή σας στη διεύθυνση `http://localhost:8501`.

## Επικοινωνία

Valentina Alto - [Linkedin](https://www.linkedin.com/in/valentina-alto-6a0590148/)

Ολόκληρο το άρθρο: [RAG με Phi-3-Medium ως Model as a Service από τον Azure Model Catalog](https://medium.com/@valentinaalto/rag-with-phi-3-medium-as-a-model-as-a-service-from-azure-model-catalog-62e1411948f3)

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες μηχανικής μετάφρασης με βάση την τεχνητή νοημοσύνη. Ενώ καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη σας ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα στην οποία συντάχθηκε θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική μετάφραση από άνθρωπο. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.