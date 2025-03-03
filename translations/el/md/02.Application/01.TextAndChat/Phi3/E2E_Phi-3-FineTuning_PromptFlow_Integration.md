# Βελτιστοποίηση και Ενσωμάτωση Προσαρμοσμένων Μοντέλων Phi-3 με το Prompt flow

Αυτό το δείγμα από άκρο σε άκρο (E2E) βασίζεται στον οδηγό "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?WT.mc_id=aiml-137032-kinfeylo)" από την Microsoft Tech Community. Εισάγει τις διαδικασίες βελτιστοποίησης, ανάπτυξης και ενσωμάτωσης προσαρμοσμένων μοντέλων Phi-3 με το Prompt flow.

## Επισκόπηση

Σε αυτό το δείγμα E2E, θα μάθετε πώς να βελτιστοποιήσετε το μοντέλο Phi-3 και να το ενσωματώσετε με το Prompt flow. Χρησιμοποιώντας το Azure Machine Learning και το Prompt flow, θα δημιουργήσετε μια ροή εργασίας για την ανάπτυξη και χρήση προσαρμοσμένων μοντέλων AI. Το δείγμα E2E χωρίζεται σε τρία σενάρια:

**Σενάριο 1: Ρύθμιση πόρων Azure και Προετοιμασία για βελτιστοποίηση**

**Σενάριο 2: Βελτιστοποίηση του μοντέλου Phi-3 και Ανάπτυξη στο Azure Machine Learning Studio**

**Σενάριο 3: Ενσωμάτωση με το Prompt flow και Συνομιλία με το προσαρμοσμένο σας μοντέλο**

Ακολουθεί μια επισκόπηση του δείγματος E2E.

![Phi-3-FineTuning_PromptFlow_Integration Overview](../../../../../../translated_images/00-01-architecture.dfeb1f15c7d3c8989fb267a05ac83a25485a7230bde037df9d3d92336afc1993.el.png)

### Περιεχόμενα

1. **[Σενάριο 1: Ρύθμιση πόρων Azure και Προετοιμασία για βελτιστοποίηση](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Δημιουργία Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Αίτηση ποσοστώσεων GPU στη συνδρομή Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Προσθήκη ανάθεσης ρόλου](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Ρύθμιση έργου](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Προετοιμασία συνόλου δεδομένων για βελτιστοποίηση](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Σενάριο 2: Βελτιστοποίηση μοντέλου Phi-3 και Ανάπτυξη στο Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Ρύθμιση Azure CLI](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Βελτιστοποίηση του μοντέλου Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Ανάπτυξη του βελτιστοποιημένου μοντέλου](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Σενάριο 3: Ενσωμάτωση με το Prompt flow και Συνομιλία με το προσαρμοσμένο σας μοντέλο](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Ενσωμάτωση του προσαρμοσμένου μοντέλου Phi-3 με το Prompt flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Συνομιλία με το προσαρμοσμένο σας μοντέλο](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Σενάριο 1: Ρύθμιση πόρων Azure και Προετοιμασία για βελτιστοποίηση

### Δημιουργία Azure Machine Learning Workspace

1. Πληκτρολογήστε *azure machine learning* στη **γραμμή αναζήτησης** στην κορυφή της σελίδας του portal και επιλέξτε **Azure Machine Learning** από τις επιλογές που εμφανίζονται.

    ![Type azure machine learning](../../../../../../translated_images/01-01-type-azml.321cff72d18a51c06dee2db7463868f3ca6619559a5d68b7795d70f4a8b3a683.el.png)

1. Επιλέξτε **+ Create** από το μενού πλοήγησης.

1. Επιλέξτε **New workspace** από το μενού πλοήγησης.

    ![Select new workspace](../../../../../../translated_images/01-02-select-new-workspace.9bd9208488fcf38226fc8d3cefffecb2cb14f414f6d8d982492c1bde8634e24a.el.png)

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Επιλέξτε τη συνδρομή Azure σας (**Subscription**).
    - Επιλέξτε την **Ομάδα πόρων** που θέλετε να χρησιμοποιήσετε (δημιουργήστε μία νέα αν χρειάζεται).
    - Εισάγετε **Όνομα Χώρου Εργασίας**. Πρέπει να είναι μοναδικό.
    - Επιλέξτε την **Περιοχή** που θέλετε να χρησιμοποιήσετε.
    - Επιλέξτε τον **Λογαριασμό αποθήκευσης** που θέλετε να χρησιμοποιήσετε (δημιουργήστε έναν νέο αν χρειάζεται).
    - Επιλέξτε το **Key vault** που θέλετε να χρησιμοποιήσετε (δημιουργήστε έναν νέο αν χρειάζεται).
    - Επιλέξτε το **Application insights** που θέλετε να χρησιμοποιήσετε (δημιουργήστε έναν νέο αν χρειάζεται).
    - Επιλέξτε το **Container registry** που θέλετε να χρησιμοποιήσετε (δημιουργήστε έναν νέο αν χρειάζεται).

    ![Fill AZML.](../../../../../../translated_images/01-03-fill-AZML.b2ebbef59952cd17d16b1f82adc252bf7616f8638d451e3c6595ffefe44f2cfa.el.png)

1. Επιλέξτε **Review + Create**.

1. Επιλέξτε **Create**.

### Αίτηση ποσοστώσεων GPU στη συνδρομή Azure

Σε αυτό το δείγμα E2E, θα χρησιμοποιήσετε την GPU *Standard_NC24ads_A100_v4* για βελτιστοποίηση, η οποία απαιτεί αίτηση ποσοστώσεων, και την CPU *Standard_E4s_v3* για ανάπτυξη, η οποία δεν απαιτεί αίτηση ποσοστώσεων.

> [!NOTE]
>
> Μόνο οι συνδρομές Pay-As-You-Go (ο τυπικός τύπος συνδρομής) είναι επιλέξιμες για διάθεση GPU· οι συνδρομές με προνόμια δεν υποστηρίζονται αυτή τη στιγμή.
>
> Για όσους χρησιμοποιούν συνδρομές με προνόμια (όπως Visual Studio Enterprise Subscription) ή θέλουν να δοκιμάσουν γρήγορα τη διαδικασία βελτιστοποίησης και ανάπτυξης, αυτό το σεμινάριο παρέχει επίσης καθοδήγηση για βελτιστοποίηση με ένα ελάχιστο σύνολο δεδομένων χρησιμοποιώντας CPU. Ωστόσο, είναι σημαντικό να σημειωθεί ότι τα αποτελέσματα της βελτιστοποίησης είναι σημαντικά καλύτερα όταν χρησιμοποιείται GPU με μεγαλύτερα σύνολα δεδομένων.

1. Επισκεφθείτε το [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Εκτελέστε τις παρακάτω ενέργειες για να ζητήσετε ποσοστώσεις για την *Οικογένεια Standard NCADSA100v4*:

    - Επιλέξτε **Quota** από την αριστερή καρτέλα.
    - Επιλέξτε την **Οικογένεια εικονικών μηχανών** που θέλετε να χρησιμοποιήσετε. Για παράδειγμα, επιλέξτε **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, που περιλαμβάνει την GPU *Standard_NC24ads_A100_v4*.
    - Επιλέξτε **Request quota** από το μενού πλοήγησης.

        ![Request quota.](../../../../../../translated_images/01-04-request-quota.ddf063c7cda9799b8ef6fbde6c3c796201578fe9078feb1c624ed75c7705ad18.el.png)

    - Στη σελίδα Request quota, εισάγετε το **Νέο όριο πυρήνων** που θέλετε να χρησιμοποιήσετε. Για παράδειγμα, 24.
    - Στη σελίδα Request quota, επιλέξτε **Submit** για να ζητήσετε την ποσοστώση GPU.

> [!NOTE]
> Μπορείτε να επιλέξετε την κατάλληλη GPU ή CPU για τις ανάγκες σας ανατρέχοντας στο έγγραφο [Μεγέθη Εικονικών Μηχανών στο Azure](https://learn.microsoft.com/azure/virtual-machines/sizes/overview?tabs=breakdownseries%2Cgeneralsizelist%2Ccomputesizelist%2Cmemorysizelist%2Cstoragesizelist%2Cgpusizelist%2Cfpgasizelist%2Chpcsizelist).

### Προσθήκη ανάθεσης ρόλου

Για να βελτιστοποιήσετε και να αναπτύξετε τα μοντέλα σας, πρέπει πρώτα να δημιουργήσετε μια User Assigned Managed Identity (UAI) και να της αναθέσετε τα κατάλληλα δικαιώματα. Αυτή η UAI θα χρησιμοποιηθεί για έλεγχο ταυτότητας κατά την ανάπτυξη.

#### Δημιουργία User Assigned Managed Identity (UAI)

1. Πληκτρολογήστε *managed identities* στη **γραμμή αναζήτησης** στην κορυφή της σελίδας του portal και επιλέξτε **Managed Identities** από τις επιλογές που εμφανίζονται.

    ![Type managed identities.](../../../../../../translated_images/01-05-type-managed-identities.8bf5dc5a4fa3e852f897ec1a983e506c2bc7b7113d159598bf0adeb66d20a5c4.el.png)

1. Επιλέξτε **+ Create**.

    ![Select create.](../../../../../../translated_images/01-06-select-create.025632b7b54fe323f7d38edabbae05dd23f4665d0731f7143719c27c32e7e84f.el.png)

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Επιλέξτε τη συνδρομή Azure σας (**Subscription**).
    - Επιλέξτε την **Ομάδα πόρων** που θέλετε να χρησιμοποιήσετε (δημιουργήστε μία νέα αν χρειάζεται).
    - Επιλέξτε την **Περιοχή** που θέλετε να χρησιμοποιήσετε.
    - Εισάγετε το **Όνομα**. Πρέπει να είναι μοναδικό.

1. Επιλέξτε **Review + create**.

1. Επιλέξτε **+ Create**.

#### Προσθήκη ρόλου Contributor στη Managed Identity

1. Μεταβείτε στον πόρο Managed Identity που δημιουργήσατε.

1. Επιλέξτε **Azure role assignments** από την αριστερή καρτέλα.

1. Επιλέξτε **+Add role assignment** από το μενού πλοήγησης.

1. Στη σελίδα Add role assignment, εκτελέστε τις παρακάτω ενέργειες:
    - Επιλέξτε **Scope** ως **Resource group**.
    - Επιλέξτε τη συνδρομή Azure σας (**Subscription**).
    - Επιλέξτε την **Ομάδα πόρων** που θέλετε να χρησιμοποιήσετε.
    - Επιλέξτε τον **Ρόλο** ως **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/01-07-fill-contributor-role.8936866326c7cdc3b876f14657e03422cca9dbff8b193dd541a693ce34407b26.el.png)

1. Επιλέξτε **Save**.

#### Προσθήκη ρόλου Storage Blob Data Reader στη Managed Identity

1. Πληκτρολογήστε *storage accounts* στη **γραμμή αναζήτησης** στην κορυφή της σελίδας του portal και επιλέξτε **Storage accounts** από τις επιλογές που εμφανίζονται.

    ![Type storage accounts.](../../../../../../translated_images/01-08-type-storage-accounts.83554a27ff3edb5099ee3fbf7f467b843dabcc0e0e5fbb829a341eab3469ffa5.el.png)

1. Επιλέξτε τον λογαριασμό αποθήκευσης που σχετίζεται με το Azure Machine Learning workspace που δημιουργήσατε. Για παράδειγμα, *finetunephistorage*.

1. Εκτελέστε τις παρακάτω ενέργειες για να μεταβείτε στη σελίδα Add role assignment:

    - Μεταβείτε στον λογαριασμό αποθήκευσης Azure που δημιουργήσατε.
    - Επιλέξτε **Access Control (IAM)** από την αριστερή καρτέλα.
    - Επιλέξτε **+ Add** από το μενού πλοήγησης.
    - Επιλέξτε **Add role assignment** από το μενού πλοήγησης.

    ![Add role.](../../../../../../translated_images/01-09-add-role.4fef55886792c7e860da4c5a808044e6f7067fb5694f3ed4819a5758c6cc574e.el.png)

1. Στη σελίδα Add role assignment, εκτελέστε τις παρακάτω ενέργειες:

    - Στη σελίδα Role, πληκτρολογήστε *Storage Blob Data Reader* στη **γραμμή αναζήτησης** και επιλέξτε **Storage Blob Data Reader** από τις επιλογές που εμφανίζονται.
    - Στη σελίδα Role, επιλέξτε **Next**.
    - Στη σελίδα Members, επιλέξτε **Assign access to** **Managed identity**.
    - Στη σελίδα Members, επιλέξτε **+ Select members**.
    - Στη σελίδα Select managed identities, επιλέξτε τη συνδρομή Azure σας (**Subscription**).
    - Στη σελίδα Select managed identities, επιλέξτε τη **Managed identity** ως **Manage Identity**.
    - Στη σελίδα Select managed identities, επιλέξτε τη Managed Identity που δημιουργήσατε. Για παράδειγμα, *finetunephi-managedidentity*.
    - Στη σελίδα Select managed identities, επιλέξτε **Select**.

    ![Select managed identity.](../../../../../../translated_images/01-10-select-managed-identity.fffa802e4e6ce2de4fe50e64d37d3f2ef268c2ee16f30ec6f92bd1829b5f19c1.el.png)

1. Επιλέξτε **Review + assign**.

#### Προσθήκη ρόλου AcrPull στη Managed Identity

1. Πληκτρολογήστε *container registries* στη **γραμμή αναζήτησης** στην κορυφή της σελίδας του portal και επιλέξτε **Container registries** από τις επιλογές που εμφανίζονται.

    ![Type container registries.](../../../../../../translated_images/01-11-type-container-registries.62e58403d73d16a0cc715571c8a7b4105a0e97b1422aa5f26106aff1c0e8a47d.el.png)

1. Επιλέξτε το container registry που σχετίζεται με το Azure Machine Learning workspace. Για παράδειγμα, *finetunephicontainerregistries*.

1. Εκτελέστε τις παρακάτω ενέργειες για να μεταβείτε στη σελίδα Add role assignment:

    - Επιλέξτε **Access Control (IAM)** από την αριστερή καρτέλα.
    - Επιλέξτε **+ Add** από το μενού πλοήγησης.
    - Επιλέξτε **Add role assignment** από το μενού πλοήγησης.

1. Στη σελίδα Add role assignment, εκτελέστε τις παρακάτω ενέργειες:

    - Στη σελίδα Role, πληκτρολογήστε *AcrPull* στη **γραμμή αναζήτησης** και επιλέξτε **AcrPull** από τις επιλογές που εμφανίζονται.
    - Στη σελίδα Role, επιλέξτε **Next**.
    - Στη σελίδα Members, επιλέξτε **Assign access to** **Managed identity**.
    - Στη σελίδα Members, επιλέξτε **+ Select members**.
    - Στη σελίδα Select managed identities, επιλέξτε τη συνδρομή Azure σας (**Subscription**).
    - Στη σελίδα Select managed identities, επιλέξτε τη **Managed identity** ως **Manage Identity**.
    - Στη σελίδα Select managed identities, επιλέξτε τη Managed Identity που δημιουργήσατε. Για παράδειγμα, *finetunephi-managedidentity*.
    - Στη σελίδα Select managed identities, επιλέξτε **Select**.
    - Επιλέξτε **Review + assign**.

### Ρύθμιση έργου

Τώρα, θα δημιουργήσετε έναν φάκελο για να εργαστείτε και θα ρυθμίσετε ένα εικονικό περιβάλλον για να αναπτύξετε ένα πρόγραμμα που αλληλεπιδρά με χρήστες και χρησιμοποιεί αποθηκευμένο ιστορικό συνομιλιών από το Azure Cosmos DB για να ενημερώσει τις απαντήσεις του.

#### Δημιουργία φακέλου για εργασία

1. Ανοίξτε ένα παράθυρο τερματικού και πληκτρολογήστε την παρακάτω εντολή για να δημιουργήσετε έναν φάκελο με όνομα *finetune-phi* στη διαδρομή προεπιλογής.

    ```console
    mkdir finetune-phi
    ```

1. Πληκτρολογήστε την παρακάτω εντολή στο τερματικό σας για να μεταβείτε στον φάκελο *finetune-phi* που δημιουργήσατε.

    ```console
    cd finetune-phi
    ```

#### Δημιουργία εικονικού περιβάλλοντος

1. Πληκτρολογήστε την παρακάτω εντολή στο τερματικό σας για να δημιουργήσετε ένα εικονικό περιβάλλον με όνομα *.venv*.

    ```console
    python -m venv .venv
    ```

1. Πληκτρολογήστε την παρακάτω εντολή στο τερματικό σας για να ενεργοποιήσετε το εικονικό περιβάλλον.

    ```console
    .venv\Scripts\activate.bat
    ```

> [!NOTE]
>
> Αν λειτουργεί, θα πρέπει να δείτε το *(.venv)* πριν από την προτροπή εντολών.

#### Εγκατάσταση των απαιτούμενων πακέτων

1. Πληκτρολογήστε τις παρακάτω εντολές στο τερματικό σας για να εγκαταστήσετε τα απαιτούμενα πακέτα.

    ```console
    pip install datasets==2.19.1
    pip install transformers==4.41.1
    pip install azure-ai-ml==1.16.0
    pip install torch==2.3.1
    pip install trl==0.9.4
    pip install promptflow==1.12.0
    ```

#### Δημιουργία αρχείων έργου

Σε αυτή την άσκηση, θα δημιουργήσετε τα απαραίτητα αρχεία για το έργο μας. Αυτά
![Εύρεση αναγνωριστικού συνδρομής.](../../../../../../translated_images/01-14-find-subscriptionid.4daef33360f6d3808a9f1acea2b6b6121c498c75c36cb6ecc6c6b211f0d3b725.el.png)

1. Εκτελέστε τα παρακάτω βήματα για να προσθέσετε το όνομα του Azure Workspace:

    - Μεταβείτε στον πόρο Azure Machine Learning που δημιουργήσατε.
    - Αντιγράψτε και επικολλήστε το όνομα του λογαριασμού σας στο αρχείο *config.py*.

    ![Εύρεση ονόματος Azure Machine Learning.](../../../../../../translated_images/01-15-find-AZML-name.c8efdc5a8f2e594260004695c145fafb4fd903e96715f495a43733560cd706b5.el.png)

1. Εκτελέστε τα παρακάτω βήματα για να προσθέσετε το όνομα του Azure Resource Group:

    - Μεταβείτε στον πόρο Azure Machine Learning που δημιουργήσατε.
    - Αντιγράψτε και επικολλήστε το όνομα του Azure Resource Group στο αρχείο *config.py*.

    ![Εύρεση ονόματος Resource Group.](../../../../../../translated_images/01-16-find-AZML-resourcegroup.0647be51d3f1b8183995949df5866455e5532ef1c3d1f93b33dc9a91d615e882.el.png)

2. Εκτελέστε τα παρακάτω βήματα για να προσθέσετε το όνομα του Azure Managed Identity:

    - Μεταβείτε στον πόρο Managed Identities που δημιουργήσατε.
    - Αντιγράψτε και επικολλήστε το όνομα του Azure Managed Identity στο αρχείο *config.py*.

    ![Εύρεση UAI.](../../../../../../translated_images/01-17-find-uai.b0fe7164cacc93b03c3c534daee68da244de6de4e6dcbc2a4e9df43403eb0f1b.el.png)

### Προετοιμασία συνόλου δεδομένων για fine-tuning

Σε αυτή την άσκηση, θα εκτελέσετε το αρχείο *download_dataset.py* για να κατεβάσετε τα σύνολα δεδομένων *ULTRACHAT_200k* στο τοπικό σας περιβάλλον. Στη συνέχεια, θα χρησιμοποιήσετε αυτά τα δεδομένα για fine-tuning του μοντέλου Phi-3 στο Azure Machine Learning.

#### Κατεβάστε το σύνολο δεδομένων χρησιμοποιώντας το *download_dataset.py*

1. Ανοίξτε το αρχείο *download_dataset.py* στο Visual Studio Code.

1. Προσθέστε τον παρακάτω κώδικα στο *download_dataset.py*.

    ```python
    import json
    import os
    from datasets import load_dataset
    from config import (
        TRAIN_DATA_PATH,
        TEST_DATA_PATH)

    def load_and_split_dataset(dataset_name, config_name, split_ratio):
        """
        Load and split a dataset.
        """
        # Load the dataset with the specified name, configuration, and split ratio
        dataset = load_dataset(dataset_name, config_name, split=split_ratio)
        print(f"Original dataset size: {len(dataset)}")
        
        # Split the dataset into train and test sets (80% train, 20% test)
        split_dataset = dataset.train_test_split(test_size=0.2)
        print(f"Train dataset size: {len(split_dataset['train'])}")
        print(f"Test dataset size: {len(split_dataset['test'])}")
        
        return split_dataset

    def save_dataset_to_jsonl(dataset, filepath):
        """
        Save a dataset to a JSONL file.
        """
        # Create the directory if it does not exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Open the file in write mode
        with open(filepath, 'w', encoding='utf-8') as f:
            # Iterate over each record in the dataset
            for record in dataset:
                # Dump the record as a JSON object and write it to the file
                json.dump(record, f)
                # Write a newline character to separate records
                f.write('\n')
        
        print(f"Dataset saved to {filepath}")

    def main():
        """
        Main function to load, split, and save the dataset.
        """
        # Load and split the ULTRACHAT_200k dataset with a specific configuration and split ratio
        dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')
        
        # Extract the train and test datasets from the split
        train_dataset = dataset['train']
        test_dataset = dataset['test']

        # Save the train dataset to a JSONL file
        save_dataset_to_jsonl(train_dataset, TRAIN_DATA_PATH)
        
        # Save the test dataset to a separate JSONL file
        save_dataset_to_jsonl(test_dataset, TEST_DATA_PATH)

    if __name__ == "__main__":
        main()

    ```

> [!TIP]
>
> **Οδηγίες για fine-tuning με μικρό σύνολο δεδομένων χρησιμοποιώντας CPU**
>
> Εάν θέλετε να χρησιμοποιήσετε CPU για fine-tuning, αυτή η προσέγγιση είναι ιδανική για όσους έχουν συνδρομές παροχών (όπως Visual Studio Enterprise Subscription) ή για γρήγορη δοκιμή της διαδικασίας fine-tuning και ανάπτυξης.
>
> Αντικαταστήστε `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:1%]')` with `dataset = load_and_split_dataset("HuggingFaceH4/ultrachat_200k", 'default', 'train_sft[:10]')`
>

1. Πληκτρολογήστε την παρακάτω εντολή στο τερματικό σας για να εκτελέσετε το script και να κατεβάσετε το σύνολο δεδομένων στο τοπικό σας περιβάλλον.

    ```console
    python download_data.py
    ```

1. Επαληθεύστε ότι τα σύνολα δεδομένων αποθηκεύτηκαν με επιτυχία στον τοπικό φάκελο *finetune-phi/data*.

> [!NOTE]
>
> **Μέγεθος συνόλου δεδομένων και χρόνος fine-tuning**
>
> Σε αυτό το δείγμα E2E, χρησιμοποιείτε μόνο το 1% του συνόλου δεδομένων (`train_sft[:1%]`). Αυτό μειώνει σημαντικά την ποσότητα δεδομένων, επιταχύνοντας τόσο τη μεταφόρτωση όσο και τη διαδικασία fine-tuning. Μπορείτε να προσαρμόσετε το ποσοστό για να βρείτε την κατάλληλη ισορροπία μεταξύ χρόνου εκπαίδευσης και απόδοσης μοντέλου. Η χρήση μικρότερου υποσυνόλου δεδομένων μειώνει τον απαιτούμενο χρόνο για fine-tuning, καθιστώντας τη διαδικασία πιο διαχειρίσιμη για ένα δείγμα E2E.

## Σενάριο 2: Fine-tuning του μοντέλου Phi-3 και ανάπτυξή του στο Azure Machine Learning Studio

### Ρύθμιση Azure CLI

Πρέπει να ρυθμίσετε το Azure CLI για να αυθεντικοποιήσετε το περιβάλλον σας. Το Azure CLI σας επιτρέπει να διαχειρίζεστε πόρους Azure απευθείας από τη γραμμή εντολών και παρέχει τα απαραίτητα διαπιστευτήρια για πρόσβαση στο Azure Machine Learning. Για να ξεκινήσετε, εγκαταστήστε το [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli)

1. Ανοίξτε ένα παράθυρο τερματικού και πληκτρολογήστε την παρακάτω εντολή για να συνδεθείτε στον λογαριασμό σας Azure.

    ```console
    az login
    ```

1. Επιλέξτε τον λογαριασμό Azure που θέλετε να χρησιμοποιήσετε.

1. Επιλέξτε τη συνδρομή Azure που θέλετε να χρησιμοποιήσετε.

    ![Εύρεση ονόματος Resource Group.](../../../../../../translated_images/02-01-login-using-azure-cli.b6e8fb6255e8d09673cb48eca2b12aebbb84dfb8817af8a6b1dfd4bb2759d68f.el.png)

> [!TIP]
>
> Εάν αντιμετωπίζετε προβλήματα σύνδεσης στο Azure, δοκιμάστε να χρησιμοποιήσετε έναν κωδικό συσκευής. Ανοίξτε ένα παράθυρο τερματικού και πληκτρολογήστε την παρακάτω εντολή για να συνδεθείτε στον λογαριασμό σας Azure:
>
> ```console
> az login --use-device-code
> ```
>

### Fine-tuning του μοντέλου Phi-3

Σε αυτή την άσκηση, θα κάνετε fine-tuning του μοντέλου Phi-3 χρησιμοποιώντας το παρεχόμενο σύνολο δεδομένων. Πρώτα, θα ορίσετε τη διαδικασία fine-tuning στο αρχείο *fine_tune.py*. Στη συνέχεια, θα ρυθμίσετε το περιβάλλον Azure Machine Learning και θα ξεκινήσετε τη διαδικασία fine-tuning εκτελώντας το αρχείο *setup_ml.py*. Αυτό το script διασφαλίζει ότι η διαδικασία fine-tuning εκτελείται μέσα στο περιβάλλον Azure Machine Learning.

Με την εκτέλεση του *setup_ml.py*, θα ξεκινήσει η διαδικασία fine-tuning στο περιβάλλον Azure Machine Learning.

#### Προσθέστε κώδικα στο αρχείο *fine_tune.py*

1. Μεταβείτε στον φάκελο *finetuning_dir* και ανοίξτε το αρχείο *fine_tune.py* στο Visual Studio Code.

1. Προσθέστε τον παρακάτω κώδικα στο *fine_tune.py*.

    ```python
    import argparse
    import sys
    import logging
    import os
    from datasets import load_dataset
    import torch
    import mlflow
    from transformers import AutoModelForCausalLM, AutoTokenizer, TrainingArguments
    from trl import SFTTrainer

    # To avoid the INVALID_PARAMETER_VALUE error in MLflow, disable MLflow integration
    os.environ["DISABLE_MLFLOW_INTEGRATION"] = "True"

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
        level=logging.WARNING
    )
    logger = logging.getLogger(__name__)

    def initialize_model_and_tokenizer(model_name, model_kwargs):
        """
        Initialize the model and tokenizer with the given pretrained model name and arguments.
        """
        model = AutoModelForCausalLM.from_pretrained(model_name, **model_kwargs)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        tokenizer.model_max_length = 2048
        tokenizer.pad_token = tokenizer.unk_token
        tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids(tokenizer.pad_token)
        tokenizer.padding_side = 'right'
        return model, tokenizer

    def apply_chat_template(example, tokenizer):
        """
        Apply a chat template to tokenize messages in the example.
        """
        messages = example["messages"]
        if messages[0]["role"] != "system":
            messages.insert(0, {"role": "system", "content": ""})
        example["text"] = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=False
        )
        return example

    def load_and_preprocess_data(train_filepath, test_filepath, tokenizer):
        """
        Load and preprocess the dataset.
        """
        train_dataset = load_dataset('json', data_files=train_filepath, split='train')
        test_dataset = load_dataset('json', data_files=test_filepath, split='train')
        column_names = list(train_dataset.features)

        train_dataset = train_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to train dataset",
        )

        test_dataset = test_dataset.map(
            apply_chat_template,
            fn_kwargs={"tokenizer": tokenizer},
            num_proc=10,
            remove_columns=column_names,
            desc="Applying chat template to test dataset",
        )

        return train_dataset, test_dataset

    def train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, output_dir):
        """
        Train and evaluate the model.
        """
        training_args = TrainingArguments(
            bf16=True,
            do_eval=True,
            output_dir=output_dir,
            eval_strategy="epoch",
            learning_rate=5.0e-06,
            logging_steps=20,
            lr_scheduler_type="cosine",
            num_train_epochs=3,
            overwrite_output_dir=True,
            per_device_eval_batch_size=4,
            per_device_train_batch_size=4,
            remove_unused_columns=True,
            save_steps=500,
            seed=0,
            gradient_checkpointing=True,
            gradient_accumulation_steps=1,
            warmup_ratio=0.2,
        )

        trainer = SFTTrainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=test_dataset,
            max_seq_length=2048,
            dataset_text_field="text",
            tokenizer=tokenizer,
            packing=True
        )

        train_result = trainer.train()
        trainer.log_metrics("train", train_result.metrics)

        mlflow.transformers.log_model(
            transformers_model={"model": trainer.model, "tokenizer": tokenizer},
            artifact_path=output_dir,
        )

        tokenizer.padding_side = 'left'
        eval_metrics = trainer.evaluate()
        eval_metrics["eval_samples"] = len(test_dataset)
        trainer.log_metrics("eval", eval_metrics)

    def main(train_file, eval_file, model_output_dir):
        """
        Main function to fine-tune the model.
        """
        model_kwargs = {
            "use_cache": False,
            "trust_remote_code": True,
            "torch_dtype": torch.bfloat16,
            "device_map": None,
            "attn_implementation": "eager"
        }

        # pretrained_model_name = "microsoft/Phi-3-mini-4k-instruct"
        pretrained_model_name = "microsoft/Phi-3.5-mini-instruct"

        with mlflow.start_run():
            model, tokenizer = initialize_model_and_tokenizer(pretrained_model_name, model_kwargs)
            train_dataset, test_dataset = load_and_preprocess_data(train_file, eval_file, tokenizer)
            train_and_evaluate_model(train_dataset, test_dataset, model, tokenizer, model_output_dir)

    if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument("--train-file", type=str, required=True, help="Path to the training data")
        parser.add_argument("--eval-file", type=str, required=True, help="Path to the evaluation data")
        parser.add_argument("--model_output_dir", type=str, required=True, help="Directory to save the fine-tuned model")
        args = parser.parse_args()
        main(args.train_file, args.eval_file, args.model_output_dir)

    ```

1. Αποθηκεύστε και κλείστε το αρχείο *fine_tune.py*.

> [!TIP]
> **Μπορείτε να κάνετε fine-tuning του μοντέλου Phi-3.5**
>
> Στο αρχείο *fine_tune.py*, μπορείτε να αλλάξετε το πεδίο `pretrained_model_name` from `"microsoft/Phi-3-mini-4k-instruct"` to any model you want to fine-tune. For example, if you change it to `"microsoft/Phi-3.5-mini-instruct"`, you'll be using the Phi-3.5-mini-instruct model for fine-tuning. To find and use the model name you prefer, visit [Hugging Face](https://huggingface.co/), search for the model you're interested in, and then copy and paste its name into the `pretrained_model_name` στο script σας.
>
> :::image type="content" source="../../imgs/03/FineTuning-PromptFlow/finetunephi3.5.png" alt-text="Fine tune Phi-3.5.":::
>

#### Προσθέστε κώδικα στο αρχείο *setup_ml.py*

1. Ανοίξτε το αρχείο *setup_ml.py* στο Visual Studio Code.

1. Προσθέστε τον παρακάτω κώδικα στο *setup_ml.py*.

    ```python
    import logging
    from azure.ai.ml import MLClient, command, Input
    from azure.ai.ml.entities import Environment, AmlCompute
    from azure.identity import AzureCliCredential
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        TRAIN_DATA_PATH,
        TEST_DATA_PATH
    )

    # Constants

    # Uncomment the following lines to use a CPU instance for training
    # COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
    # COMPUTE_NAME = "cpu-e16s-v3"
    # DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"

    # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/curated/acft-hf-nlp-gpu:59"

    CONDA_FILE = "conda.yml"
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    FINETUNING_DIR = "./finetuning_dir" # Path to the fine-tuning script
    TRAINING_ENV_NAME = "phi-3-training-environment" # Name of the training environment
    MODEL_OUTPUT_DIR = "./model_output" # Path to the model output directory in azure ml

    # Logging setup to track the process
    logger = logging.getLogger(__name__)
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.WARNING
    )

    def get_ml_client():
        """
        Initialize the ML Client using Azure CLI credentials.
        """
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def create_or_get_environment(ml_client):
        """
        Create or update the training environment in Azure ML.
        """
        env = Environment(
            image=DOCKER_IMAGE_NAME,  # Docker image for the environment
            conda_file=CONDA_FILE,  # Conda environment file
            name=TRAINING_ENV_NAME,  # Name of the environment
        )
        return ml_client.environments.create_or_update(env)

    def create_or_get_compute_cluster(ml_client, compute_name, COMPUTE_INSTANCE_TYPE, location):
        """
        Create or update the compute cluster in Azure ML.
        """
        try:
            compute_cluster = ml_client.compute.get(compute_name)
            logger.info(f"Compute cluster '{compute_name}' already exists. Reusing it for the current run.")
        except Exception:
            logger.info(f"Compute cluster '{compute_name}' does not exist. Creating a new one with size {COMPUTE_INSTANCE_TYPE}.")
            compute_cluster = AmlCompute(
                name=compute_name,
                size=COMPUTE_INSTANCE_TYPE,
                location=location,
                tier="Dedicated",  # Tier of the compute cluster
                min_instances=0,  # Minimum number of instances
                max_instances=1  # Maximum number of instances
            )
            ml_client.compute.begin_create_or_update(compute_cluster).wait()  # Wait for the cluster to be created
        return compute_cluster

    def create_fine_tuning_job(env, compute_name):
        """
        Set up the fine-tuning job in Azure ML.
        """
        return command(
            code=FINETUNING_DIR,  # Path to fine_tune.py
            command=(
                "python fine_tune.py "
                "--train-file ${{inputs.train_file}} "
                "--eval-file ${{inputs.eval_file}} "
                "--model_output_dir ${{inputs.model_output}}"
            ),
            environment=env,  # Training environment
            compute=compute_name,  # Compute cluster to use
            inputs={
                "train_file": Input(type="uri_file", path=TRAIN_DATA_PATH),  # Path to the training data file
                "eval_file": Input(type="uri_file", path=TEST_DATA_PATH),  # Path to the evaluation data file
                "model_output": MODEL_OUTPUT_DIR
            }
        )

    def main():
        """
        Main function to set up and run the fine-tuning job in Azure ML.
        """
        # Initialize ML Client
        ml_client = get_ml_client()

        # Create Environment
        env = create_or_get_environment(ml_client)
        
        # Create or get existing compute cluster
        create_or_get_compute_cluster(ml_client, COMPUTE_NAME, COMPUTE_INSTANCE_TYPE, LOCATION)

        # Create and Submit Fine-Tuning Job
        job = create_fine_tuning_job(env, COMPUTE_NAME)
        returned_job = ml_client.jobs.create_or_update(job)  # Submit the job
        ml_client.jobs.stream(returned_job.name)  # Stream the job logs
        
        # Capture the job name
        job_name = returned_job.name
        print(f"Job name: {job_name}")

    if __name__ == "__main__":
        main()

    ```

1. Αντικαταστήστε `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `LOCATION` με τις δικές σας λεπτομέρειες.

    ```python
   # Uncomment the following lines to use a GPU instance for training
    COMPUTE_INSTANCE_TYPE = "Standard_NC24ads_A100_v4"
    COMPUTE_NAME = "gpu-nc24s-a100-v4"
    ...
    LOCATION = "eastus2" # Replace with the location of your compute cluster
    ```

> [!TIP]
>
> **Οδηγίες για fine-tuning με μικρό σύνολο δεδομένων χρησιμοποιώντας CPU**
>
> Εάν θέλετε να χρησιμοποιήσετε CPU για fine-tuning, αυτή η προσέγγιση είναι ιδανική για όσους έχουν συνδρομές παροχών (όπως Visual Studio Enterprise Subscription) ή για γρήγορη δοκιμή της διαδικασίας fine-tuning και ανάπτυξης.
>
> 1. Ανοίξτε το αρχείο *setup_ml*.
> 1. Αντικαταστήστε `COMPUTE_INSTANCE_TYPE`, `COMPUTE_NAME`, and `DOCKER_IMAGE_NAME` with the following. If you do not have access to *Standard_E16s_v3*, you can use an equivalent CPU instance or request a new quota.
> 1. Replace `LOCATION` με τις δικές σας λεπτομέρειες.
>
>    ```python
>    # Uncomment the following lines to use a CPU instance for training
>    COMPUTE_INSTANCE_TYPE = "Standard_E16s_v3" # cpu
>    COMPUTE_NAME = "cpu-e16s-v3"
>    DOCKER_IMAGE_NAME = "mcr.microsoft.com/azureml/openmpi4.1.0-ubuntu20.04:latest"
>    LOCATION = "eastus2" # Replace with the location of your compute cluster
>    ```
>

1. Πληκτρολογήστε την παρακάτω εντολή για να εκτελέσετε το script *setup_ml.py* και να ξεκινήσετε τη διαδικασία fine-tuning στο Azure Machine Learning.

    ```python
    python setup_ml.py
    ```

1. Σε αυτή την άσκηση, κάνατε με επιτυχία fine-tuning του μοντέλου Phi-3 χρησιμοποιώντας το Azure Machine Learning. Με την εκτέλεση του script *setup_ml.py*, ρυθμίσατε το περιβάλλον Azure Machine Learning και ξεκινήσατε τη διαδικασία fine-tuning που ορίστηκε στο αρχείο *fine_tune.py*. Λάβετε υπόψη ότι η διαδικασία fine-tuning μπορεί να διαρκέσει αρκετό χρόνο. Μετά την εκτέλεση του `python setup_ml.py` command, you need to wait for the process to complete. You can monitor the status of the fine-tuning job by following the link provided in the terminal to the Azure Machine Learning portal.

    ![See finetuning job.](../../../../../../translated_images/02-02-see-finetuning-job.a28c8552f7b7bc088ccd67dd0c522f7fc1944048d3554bb1b24f95a1169ad538.el.png)

### Deploy the fine-tuned model

To integrate the fine-tuned Phi-3 model with Prompt Flow, you need to deploy the model to make it accessible for real-time inference. This process involves registering the model, creating an online endpoint, and deploying the model.

#### Set the model name, endpoint name, and deployment name for deployment

1. Open *config.py* file.

1. Replace `AZURE_MODEL_NAME = "your_fine_tuned_model_name"` with the desired name for your model.

1. Replace `AZURE_ENDPOINT_NAME = "your_fine_tuned_model_endpoint_name"` with the desired name for your endpoint.

1. Replace `AZURE_DEPLOYMENT_NAME = "your_fine_tuned_model_deployment_name"` με το επιθυμητό όνομα για την ανάπτυξή σας.

#### Προσθέστε κώδικα στο αρχείο *deploy_model.py*

Η εκτέλεση του αρχείου *deploy_model.py* αυτοματοποιεί ολόκληρη τη διαδικασία ανάπτυξης. Εγγράφει το μοντέλο, δημιουργεί ένα endpoint και εκτελεί την ανάπτυξη σύμφωνα με τις ρυθμίσεις που καθορίζονται στο αρχείο config.py, το οποίο περιλαμβάνει το όνομα του μοντέλου, το όνομα του endpoint και το όνομα της ανάπτυξης.

1. Ανοίξτε το αρχείο *deploy_model.py* στο Visual Studio Code.

1. Προσθέστε τον παρακάτω κώδικα στο *deploy_model.py*.

    ```python
    import logging
    from azure.identity import AzureCliCredential
    from azure.ai.ml import MLClient
    from azure.ai.ml.entities import Model, ProbeSettings, ManagedOnlineEndpoint, ManagedOnlineDeployment, IdentityConfiguration, ManagedIdentityConfiguration, OnlineRequestSettings
    from azure.ai.ml.constants import AssetTypes

    # Configuration imports
    from config import (
        AZURE_SUBSCRIPTION_ID,
        AZURE_RESOURCE_GROUP_NAME,
        AZURE_ML_WORKSPACE_NAME,
        AZURE_MANAGED_IDENTITY_RESOURCE_ID,
        AZURE_MANAGED_IDENTITY_CLIENT_ID,
        AZURE_MODEL_NAME,
        AZURE_ENDPOINT_NAME,
        AZURE_DEPLOYMENT_NAME
    )

    # Constants
    JOB_NAME = "your-job-name"
    COMPUTE_INSTANCE_TYPE = "Standard_E4s_v3"

    deployment_env_vars = {
        "SUBSCRIPTION_ID": AZURE_SUBSCRIPTION_ID,
        "RESOURCE_GROUP_NAME": AZURE_RESOURCE_GROUP_NAME,
        "UAI_CLIENT_ID": AZURE_MANAGED_IDENTITY_CLIENT_ID,
    }

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def get_ml_client():
        """Initialize and return the ML Client."""
        credential = AzureCliCredential()
        return MLClient(credential, AZURE_SUBSCRIPTION_ID, AZURE_RESOURCE_GROUP_NAME, AZURE_ML_WORKSPACE_NAME)

    def register_model(ml_client, model_name, job_name):
        """Register a new model."""
        model_path = f"azureml://jobs/{job_name}/outputs/artifacts/paths/model_output"
        logger.info(f"Registering model {model_name} from job {job_name} at path {model_path}.")
        run_model = Model(
            path=model_path,
            name=model_name,
            description="Model created from run.",
            type=AssetTypes.MLFLOW_MODEL,
        )
        model = ml_client.models.create_or_update(run_model)
        logger.info(f"Registered model ID: {model.id}")
        return model

    def delete_existing_endpoint(ml_client, endpoint_name):
        """Delete existing endpoint if it exists."""
        try:
            endpoint_result = ml_client.online_endpoints.get(name=endpoint_name)
            logger.info(f"Deleting existing endpoint {endpoint_name}.")
            ml_client.online_endpoints.begin_delete(name=endpoint_name).result()
            logger.info(f"Deleted existing endpoint {endpoint_name}.")
        except Exception as e:
            logger.info(f"No existing endpoint {endpoint_name} found to delete: {e}")

    def create_or_update_endpoint(ml_client, endpoint_name, description=""):
        """Create or update an endpoint."""
        delete_existing_endpoint(ml_client, endpoint_name)
        logger.info(f"Creating new endpoint {endpoint_name}.")
        endpoint = ManagedOnlineEndpoint(
            name=endpoint_name,
            description=description,
            identity=IdentityConfiguration(
                type="user_assigned",
                user_assigned_identities=[ManagedIdentityConfiguration(resource_id=AZURE_MANAGED_IDENTITY_RESOURCE_ID)]
            )
        )
        endpoint_result = ml_client.online_endpoints.begin_create_or_update(endpoint).result()
        logger.info(f"Created new endpoint {endpoint_name}.")
        return endpoint_result

    def create_or_update_deployment(ml_client, endpoint_name, deployment_name, model):
        """Create or update a deployment."""

        logger.info(f"Creating deployment {deployment_name} for endpoint {endpoint_name}.")
        deployment = ManagedOnlineDeployment(
            name=deployment_name,
            endpoint_name=endpoint_name,
            model=model.id,
            instance_type=COMPUTE_INSTANCE_TYPE,
            instance_count=1,
            environment_variables=deployment_env_vars,
            request_settings=OnlineRequestSettings(
                max_concurrent_requests_per_instance=3,
                request_timeout_ms=180000,
                max_queue_wait_ms=120000
            ),
            liveness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
            readiness_probe=ProbeSettings(
                failure_threshold=30,
                success_threshold=1,
                period=100,
                initial_delay=500,
            ),
        )
        deployment_result = ml_client.online_deployments.begin_create_or_update(deployment).result()
        logger.info(f"Created deployment {deployment.name} for endpoint {endpoint_name}.")
        return deployment_result

    def set_traffic_to_deployment(ml_client, endpoint_name, deployment_name):
        """Set traffic to the specified deployment."""
        try:
            # Fetch the current endpoint details
            endpoint = ml_client.online_endpoints.get(name=endpoint_name)
            
            # Log the current traffic allocation for debugging
            logger.info(f"Current traffic allocation: {endpoint.traffic}")
            
            # Set the traffic allocation for the deployment
            endpoint.traffic = {deployment_name: 100}
            
            # Update the endpoint with the new traffic allocation
            endpoint_poller = ml_client.online_endpoints.begin_create_or_update(endpoint)
            updated_endpoint = endpoint_poller.result()
            
            # Log the updated traffic allocation for debugging
            logger.info(f"Updated traffic allocation: {updated_endpoint.traffic}")
            logger.info(f"Set traffic to deployment {deployment_name} at endpoint {endpoint_name}.")
            return updated_endpoint
        except Exception as e:
            # Log any errors that occur during the process
            logger.error(f"Failed to set traffic to deployment: {e}")
            raise


    def main():
        ml_client = get_ml_client()

        registered_model = register_model(ml_client, AZURE_MODEL_NAME, JOB_NAME)
        logger.info(f"Registered model ID: {registered_model.id}")

        endpoint = create_or_update_endpoint(ml_client, AZURE_ENDPOINT_NAME, "Endpoint for finetuned Phi-3 model")
        logger.info(f"Endpoint {AZURE_ENDPOINT_NAME} is ready.")

        try:
            deployment = create_or_update_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME, registered_model)
            logger.info(f"Deployment {AZURE_DEPLOYMENT_NAME} is created for endpoint {AZURE_ENDPOINT_NAME}.")

            set_traffic_to_deployment(ml_client, AZURE_ENDPOINT_NAME, AZURE_DEPLOYMENT_NAME)
            logger.info(f"Traffic is set to deployment {AZURE_DEPLOYMENT_NAME} at endpoint {AZURE_ENDPOINT_NAME}.")
        except Exception as e:
            logger.error(f"Failed to create or update deployment: {e}")

    if __name__ == "__main__":
        main()

    ```

1. Εκτελέστε τα παρακάτω βήματα για να λάβετε το `JOB_NAME`:

    - Navigate to Azure Machine Learning resource that you created.
    - Select **Studio web URL** to open the Azure Machine Learning workspace.
    - Select **Jobs** from the left side tab.
    - Select the experiment for fine-tuning. For example, *finetunephi*.
    - Select the job that you created.
    - Copy and paste your job Name into the `JOB_NAME = "your-job-name"` in *deploy_model.py* file.

1. Replace `COMPUTE_INSTANCE_TYPE` με τις δικές σας λεπτομέρειες.

1. Πληκτρολογήστε την παρακάτω εντολή για να εκτελέσετε το script *deploy_model.py* και να ξεκινήσετε τη διαδικασία ανάπτυξης στο Azure Machine Learning.

    ```python
    python deploy_model.py
    ```

> [!WARNING]
> Για να αποφύγετε πρόσθετες χρεώσεις στον λογαριασμό σας, βεβαιωθείτε ότι διαγράφετε το endpoint που δημιουργήθηκε στο workspace του Azure Machine Learning.
>

#### Ελέγξτε την κατάσταση ανάπτυξης στο Workspace του Azure Machine Learning

1. Επισκεφθείτε το [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Μεταβείτε στο workspace του Azure Machine Learning που δημιουργήσατε.

1. Επιλέξτε **Studio web URL** για να ανοίξετε το workspace του Azure Machine Learning.

1. Επιλέξτε **Endpoints** από την αριστερή καρτέλα.

    ![Επιλέξτε endpoints.](../../../../../../translated_images/02-03-select-endpoints.a32f4eb2854cd54ee997f9bec0e842c3084bbc24bd693457b5c6b132fe966bf4.el.png)

2. Επιλέξτε το endpoint που δημιουργήσατε.

    ![Επιλέξτε το endpoint που δημιουργήσατε.](../../../../../../translated_images/02-04-select-endpoint-created.048b4f0f6479c1885b62711a151227a24408679be65dd1039cd2f64448ec5842.el.png)

3. Σε αυτή τη σελίδα, μπορείτε να διαχειριστείτε τα endpoints που δημιουργήθηκαν κατά τη διαδικασία ανάπτυξης.

## Σενάριο 3: Ενσωμάτωση με Prompt flow και συνομιλία με το προσαρμοσμένο σας μοντέλο

### Ενσωμάτωση του προσαρμοσμένου μοντέλου Phi-3 με το Prompt flow

Αφού ολοκληρώσετε την ανάπτυξη του fine-tuned μοντέλου σας, μπορείτε τώρα να το ενσωματώσετε με το Prompt flow για να το χρησιμοποιήσετε σε εφαρμογές πραγματικού χρόνου, επιτρέποντας μια ποικιλία διαδραστικών εργασιών με το προσαρμοσμένο σας μοντέλο Phi-3.

#### Ορίστε το api key και το endpoint uri του fine-tuned μοντέλου Phi-3

1. Μεταβείτε στο workspace του Azure Machine Learning που δημιουργήσατε.
1. Επιλέξτε **Endpoints** από την αριστερή καρτέλα.
1. Επιλέξτε το endpoint που δημιουργήσατε.
1. Επιλέξτε **Consume** από το μενού πλοήγησης.
1. Αντιγράψτε και επικολλήστε το **REST endpoint** στο αρχείο *config.py*, αντικαθιστώντας `AZURE_ML_ENDPOINT = "your_fine_tuned_model_endpoint_uri"` with your **REST endpoint**.
1. Copy and paste your **Primary key** into the *config.py* file, replacing `AZURE_ML_API_KEY = "your_fine_tuned_model_api_key"` με το **Primary key** σας.

    ![Αντιγραφή api key και endpoint uri.](../../../../../../translated_images/02-05-copy-apikey-endpoint.602de7450770e9984149dc7da7472bacafbf0e8447e2adb53896ad93b1dc7684.el.png)

#### Προσθέστε κώδικα στο αρχείο *flow.dag.yml*

1. Ανοίξτε το αρχείο *flow.dag.yml* στο Visual Studio Code.

1. Προσθέστε τον παρακάτω κώδικα στο *flow.dag.yml*.

    ```yml
    inputs:
      input_data:
        type: string
        default: "Who founded Microsoft?"

    outputs:
      answer:
        type: string
        reference: ${integrate_with_promptflow.output}

    nodes:
    - name: integrate_with_promptflow
      type: python
      source:
        type: code
        path: integrate_with_promptflow.py
      inputs:
        input_data: ${inputs.input_data}
    ```

#### Προσθέστε κώδικα στο αρχείο *integrate_with_promptflow.py*

1. Ανοίξτε το αρχείο *integrate_with_promptflow.py* στο Visual Studio Code.

1. Προσθέστε τον παρακάτω κώδικα στο *integrate_with_promptflow.py*.

    ```python
    import logging
    import requests
    from promptflow.core import tool
    import asyncio
    import platform
    from config import (
        AZURE_ML_ENDPOINT,
        AZURE_ML_API_KEY
    )

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_azml_endpoint(input_data: list, endpoint_url: str, api_key: str) -> str:
        """
        Send a request to the Azure ML endpoint with the given input data.
        """
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": [input_data],
            "params": {
                "temperature": 0.7,
                "max_new_tokens": 128,
                "do_sample": True,
                "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            result = response.json()[0]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    def setup_asyncio_policy():
        """
        Setup asyncio event loop policy for Windows.
        """
        if platform.system() == 'Windows':
            asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
            logger.info("Set Windows asyncio event loop policy.")

    @tool
    def my_python_tool(input_data: str) -> str:
        """
        Tool function to process input data and query the Azure ML endpoint.
        """
        setup_asyncio_policy()
        return query_azml_endpoint(input_data, AZURE_ML_ENDPOINT, AZURE_ML_API_KEY)

    ```

### Συνομιλία με το προσαρμοσμένο σας μοντέλο

1. Πληκτρολογήστε την παρακάτω εντολή για να εκτελέσετε το script *deploy_model.py* και να ξεκινήσετε τη διαδικασία ανάπτυξης στο Azure Machine Learning.

    ```python
    pf flow serve --source ./ --port 8080 --host localhost
    ```

1. Παράδειγμα αποτελεσμάτων: Τώρα μπορείτε να συνομιλήσετε με το προσαρμοσμένο σας μοντέλο Phi-3. Συνιστάται να κάνετε ερωτήσεις που βασίζονται στα δεδομένα που χρησιμοποιήθηκαν για το fine-tuning.

    ![Παράδειγμα Prompt flow.](../../../../../../translated_images/02-06-promptflow-example.023c07a4be8f02199e04eaf49f40ba24415da1be2274cbda9a7aa39776acd0bb.el.png)

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες αυτόματης μετάφρασης με βάση την τεχνητή νοημοσύνη. Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.