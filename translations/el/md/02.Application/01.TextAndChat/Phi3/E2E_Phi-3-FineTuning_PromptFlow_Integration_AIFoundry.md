# Προσαρμογή και Ενσωμάτωση Προσαρμοσμένων Μοντέλων Phi-3 με το Prompt Flow στο Azure AI Foundry

Αυτό το ολοκληρωμένο παράδειγμα (E2E) βασίζεται στον οδηγό "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?WT.mc_id=aiml-137032-kinfeylo)" από την κοινότητα Microsoft Tech. Παρουσιάζει τις διαδικασίες προσαρμογής, ανάπτυξης και ενσωμάτωσης προσαρμοσμένων μοντέλων Phi-3 με το Prompt Flow στο Azure AI Foundry.  
Σε αντίθεση με το δείγμα E2E "[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow](./E2E_Phi-3-FineTuning_PromptFlow_Integration.md)", που απαιτούσε την εκτέλεση κώδικα τοπικά, αυτό το σεμινάριο επικεντρώνεται εξ ολοκλήρου στην προσαρμογή και ενσωμάτωση του μοντέλου σας μέσα στο Azure AI / ML Studio.

## Επισκόπηση

Σε αυτό το παράδειγμα E2E, θα μάθετε πώς να προσαρμόσετε το μοντέλο Phi-3 και να το ενσωματώσετε με το Prompt Flow στο Azure AI Foundry. Με την αξιοποίηση του Azure AI / ML Studio, θα δημιουργήσετε μια ροή εργασίας για την ανάπτυξη και χρήση προσαρμοσμένων μοντέλων AI. Αυτό το παράδειγμα E2E χωρίζεται σε τρία σενάρια:

**Σενάριο 1: Δημιουργία πόρων Azure και Προετοιμασία για προσαρμογή**

**Σενάριο 2: Προσαρμογή του μοντέλου Phi-3 και Ανάπτυξή του στο Azure Machine Learning Studio**

**Σενάριο 3: Ενσωμάτωση με το Prompt Flow και Συνομιλία με το προσαρμοσμένο σας μοντέλο στο Azure AI Foundry**

Ακολουθεί μια επισκόπηση αυτού του παραδείγματος E2E.

![Phi-3-FineTuning_PromptFlow_Integration Overview.](../../../../../../translated_images/00-01-architecture.48557afd46be88c521fb66f886c611bb93ec4cde1b00e138174ae97f75f56262.el.png)

### Πίνακας Περιεχομένων

1. **[Σενάριο 1: Δημιουργία πόρων Azure και Προετοιμασία για προσαρμογή](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Δημιουργία ενός Azure Machine Learning Workspace](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Αίτηση ποσοστώσεων GPU στη Συνδρομή Azure](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Προσθήκη ανάθεσης ρόλων](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Ρύθμιση έργου](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Προετοιμασία συνόλου δεδομένων για προσαρμογή](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Σενάριο 2: Προσαρμογή του μοντέλου Phi-3 και Ανάπτυξή του στο Azure Machine Learning Studio](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Προσαρμογή του μοντέλου Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Ανάπτυξη του προσαρμοσμένου μοντέλου Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

1. **[Σενάριο 3: Ενσωμάτωση με το Prompt Flow και Συνομιλία με το προσαρμοσμένο σας μοντέλο στο Azure AI Foundry](../../../../../../md/02.Application/01.TextAndChat/Phi3)**
    - [Ενσωμάτωση του προσαρμοσμένου μοντέλου Phi-3 με το Prompt Flow](../../../../../../md/02.Application/01.TextAndChat/Phi3)
    - [Συνομιλία με το προσαρμοσμένο σας μοντέλο Phi-3](../../../../../../md/02.Application/01.TextAndChat/Phi3)

## Σενάριο 1: Δημιουργία πόρων Azure και Προετοιμασία για προσαρμογή

### Δημιουργία ενός Azure Machine Learning Workspace

1. Πληκτρολογήστε *azure machine learning* στη **γραμμή αναζήτησης** στο επάνω μέρος της πύλης και επιλέξτε **Azure Machine Learning** από τις επιλογές που εμφανίζονται.

    ![Type azure machine learning.](../../../../../../translated_images/01-01-type-azml.d34ed3e290197950bb59b5574720c139f88921832c375c07d5c0f3134d7831ca.el.png)

2. Επιλέξτε **+ Create** από το μενού πλοήγησης.

3. Επιλέξτε **New workspace** από το μενού πλοήγησης.

    ![Select new workspace.](../../../../../../translated_images/01-02-select-new-workspace.969d9b84a9a134e223a6efeba5bb9a81729993389665a76b81a22cb65e1ee702.el.png)

4. Εκτελέστε τις παρακάτω ενέργειες:

    - Επιλέξτε τη **Συνδρομή Azure** σας.
    - Επιλέξτε την **Ομάδα πόρων** που θα χρησιμοποιήσετε (δημιουργήστε μια νέα αν χρειάζεται).
    - Εισαγάγετε **Όνομα Workspace**. Πρέπει να είναι μοναδικό.
    - Επιλέξτε την **Περιοχή** που θέλετε να χρησιμοποιήσετε.
    - Επιλέξτε τον **Λογαριασμό αποθήκευσης** που θα χρησιμοποιήσετε (δημιουργήστε έναν νέο αν χρειάζεται).
    - Επιλέξτε το **Key vault** που θα χρησιμοποιήσετε (δημιουργήστε έναν νέο αν χρειάζεται).
    - Επιλέξτε το **Application insights** που θα χρησιμοποιήσετε (δημιουργήστε έναν νέο αν χρειάζεται).
    - Επιλέξτε το **Container registry** που θα χρησιμοποιήσετε (δημιουργήστε έναν νέο αν χρειάζεται).

    ![Fill azure machine learning.](../../../../../../translated_images/01-03-fill-AZML.97c43ed40b5231572001c9e2a5193a4c63de657f07401d1fce962a085e129809.el.png)

5. Επιλέξτε **Review + Create**.

6. Επιλέξτε **Create**.

### Αίτηση ποσοστώσεων GPU στη Συνδρομή Azure

Σε αυτό το σεμινάριο, θα μάθετε πώς να προσαρμόσετε και να αναπτύξετε ένα μοντέλο Phi-3, χρησιμοποιώντας GPUs. Για την προσαρμογή, θα χρησιμοποιήσετε τη GPU *Standard_NC24ads_A100_v4*, η οποία απαιτεί αίτηση ποσοστώσεων. Για την ανάπτυξη, θα χρησιμοποιήσετε τη GPU *Standard_NC6s_v3*, η οποία επίσης απαιτεί αίτηση ποσοστώσεων.

> [!NOTE]
>
> Μόνο οι συνδρομές Pay-As-You-Go (ο τυπικός τύπος συνδρομής) είναι επιλέξιμες για κατανομή GPU. Οι συνδρομές με παροχές δεν υποστηρίζονται προς το παρόν.

1. Επισκεφθείτε το [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Εκτελέστε τις παρακάτω ενέργειες για να ζητήσετε ποσοστώσεις GPU *Standard NCADSA100v4 Family*:

    - Επιλέξτε **Quota** από την αριστερή καρτέλα.
    - Επιλέξτε την **Οικογένεια εικονικών μηχανών** που θα χρησιμοποιήσετε. Για παράδειγμα, επιλέξτε **Standard NCADSA100v4 Family Cluster Dedicated vCPUs**, που περιλαμβάνει τη GPU *Standard_NC24ads_A100_v4*.
    - Επιλέξτε **Request quota** από το μενού πλοήγησης.

        ![Request quota.](../../../../../../translated_images/02-02-request-quota.9bb6ecf76b842dbccd70603b5a6f8533e7a2a0f9f9cc8304bef67fb0bb09e49a.el.png)

    - Στη σελίδα Request quota, εισαγάγετε το **Νέο όριο πυρήνων** που θέλετε να χρησιμοποιήσετε. Για παράδειγμα, 24.
    - Στη σελίδα Request quota, επιλέξτε **Submit** για να ζητήσετε την ποσοστώση GPU.

1. Εκτελέστε τις παρακάτω ενέργειες για να ζητήσετε ποσοστώσεις GPU *Standard NCSv3 Family*:

    - Επιλέξτε **Quota** από την αριστερή καρτέλα.
    - Επιλέξτε την **Οικογένεια εικονικών μηχανών** που θα χρησιμοποιήσετε. Για παράδειγμα, επιλέξτε **Standard NCSv3 Family Cluster Dedicated vCPUs**, που περιλαμβάνει τη GPU *Standard_NC6s_v3*.
    - Επιλέξτε **Request quota** από το μενού πλοήγησης.
    - Στη σελίδα Request quota, εισαγάγετε το **Νέο όριο πυρήνων** που θέλετε να χρησιμοποιήσετε. Για παράδειγμα, 24.
    - Στη σελίδα Request quota, επιλέξτε **Submit** για να ζητήσετε την ποσοστώση GPU.

### Προσθήκη ανάθεσης ρόλων

Για να προσαρμόσετε και να αναπτύξετε τα μοντέλα σας, πρέπει πρώτα να δημιουργήσετε μια Διαχειριζόμενη Ταυτότητα που έχει ανατεθεί από τον χρήστη (UAI) και να της εκχωρήσετε τα κατάλληλα δικαιώματα. Αυτή η ταυτότητα θα χρησιμοποιηθεί για πιστοποίηση κατά την ανάπτυξη.  

#### Δημιουργία Διαχειριζόμενης Ταυτότητας που έχει ανατεθεί από τον χρήστη (UAI)

1. Πληκτρολογήστε *managed identities* στη **γραμμή αναζήτησης** στο επάνω μέρος της πύλης και επιλέξτε **Managed Identities** από τις επιλογές που εμφανίζονται.

    ![Type managed identities.](../../../../../../translated_images/03-01-type-managed-identities.61954962fbc13913ceb35d00dd9d746b91fdd96834383b65214fa0f4d1152441.el.png)

1. Επιλέξτε **+ Create**.

    ![Select create.](../../../../../../translated_images/03-02-select-create.4608dd89e644e68f40b559d30788383bc70dd3d14f082c78f460ba45d208f273.el.png)

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Επιλέξτε τη **Συνδρομή Azure** σας.
    - Επιλέξτε την **Ομάδα πόρων** που θα χρησιμοποιήσετε (δημιουργήστε μια νέα αν χρειάζεται).
    - Επιλέξτε την **Περιοχή** που θέλετε να χρησιμοποιήσετε.
    - Εισαγάγετε το **Όνομα**. Πρέπει να είναι μοναδικό.

    ![Select create.](../../../../../../translated_images/03-03-fill-managed-identities-1.ff32a0010dd0667dd231f214881ab59f809ecf10b901030fc3db4e41a50a834a.el.png)

1. Επιλέξτε **Review + create**.

1. Επιλέξτε **+ Create**.

#### Προσθήκη ρόλου Contributor στη Διαχειριζόμενη Ταυτότητα

1. Μεταβείτε στον πόρο Διαχειριζόμενης Ταυτότητας που δημιουργήσατε.

1. Επιλέξτε **Azure role assignments** από την αριστερή καρτέλα.

1. Επιλέξτε **+Add role assignment** από το μενού πλοήγησης.

1. Στη σελίδα Add role assignment, εκτελέστε τις παρακάτω ενέργειες:
    - Επιλέξτε το **Scope** ως **Resource group**.
    - Επιλέξτε τη **Συνδρομή Azure** σας.
    - Επιλέξτε την **Ομάδα πόρων** που θα χρησιμοποιήσετε.
    - Επιλέξτε το **Ρόλο** ως **Contributor**.

    ![Fill contributor role.](../../../../../../translated_images/03-04-fill-contributor-role.419141712bde1fa89624c3792233a367b23cbc46fb7018d1d11c3cd65a25f748.el.png)

2. Επιλέξτε **Save**.

#### Προσθήκη ρόλου Storage Blob Data Reader στη Διαχειριζόμενη Ταυτότητα

1. Πληκτρολογήστε *storage accounts* στη **γραμμή αναζήτησης** στο επάνω μέρος της πύλης και επιλέξτε **Storage accounts** από τις επιλογές που εμφανίζονται.

    ![Type storage accounts.](../../../../../../translated_images/03-05-type-storage-accounts.026e03a619ba23f474f9d704cd9050335df48aab7253eb17729da506baf2056b.el.png)

1. Επιλέξτε τον λογαριασμό αποθήκευσης που συνδέεται με το Azure Machine Learning workspace που δημιουργήσατε. Για παράδειγμα, *finetunephistorage*.

1. Εκτελέστε τις παρακάτω ενέργειες για να μεταβείτε στη σελίδα Add role assignment:

    - Μεταβείτε στον λογαριασμό αποθήκευσης Azure που δημιουργήσατε.
    - Επιλέξτε **Access Control (IAM)** από την αριστερή καρτέλα.
    - Επιλέξτε **+ Add** από το μενού πλοήγησης.
    - Επιλέξτε **Add role assignment** από το μενού πλοήγησης.

    ![Add role.](../../../../../../translated_images/03-06-add-role.ea9dffa9d4e12c8ce5d7ee4c5ffb6eb7f7a5aac820c60a5782a3fb634b7aa09a.el.png)

1. Στη σελίδα Add role assignment, εκτελέστε τις παρακάτω ενέργειες:

    - Στη σελίδα Role, πληκτρολογήστε *Storage Blob Data Reader* στη **γραμμή αναζήτησης** και επιλέξτε **Storage Blob Data Reader** από τις επιλογές που εμφανίζονται.
    - Στη σελίδα Role, επιλέξτε **Next**.
    - Στη σελίδα Members, επιλέξτε **Assign access to** **Managed identity**.
    - Στη σελίδα Members, επιλέξτε **+ Select members**.
    - Στη σελίδα Select managed identities, επιλέξτε τη **Συνδρομή Azure** σας.
    - Στη σελίδα Select managed identities, επιλέξτε τη **Διαχειριζόμενη ταυτότητα** που δημιουργήσατε. Για παράδειγμα, *finetunephi-managedidentity*.
    - Στη σελίδα Select managed identities, επιλέξτε **Select**.

    ![Select managed identity.](../../../../../../translated_images/03-08-select-managed-identity.2456b3430a31bbaba7c744256dfb99c7fa6e12ba2dd122e34205973d29115d6c.el.png)

1. Επιλέξτε **Review + assign**.

#### Προσθήκη ρόλου AcrPull στη Διαχειριζόμενη Ταυτότητα

1. Πληκτρολογήστε *container registries* στη **γραμμή αναζήτησης** στο επάνω μέρος της πύλης και επιλέξτε **Container registries** από τις επιλογές που εμφανίζονται.

    ![Type container registries.](../../../../../../translated_images/03-09-type-container-registries.cac7db97652dda0e9d7b98d40034f5ac81752db9528b708e014c74a9891c49aa.el.png)

1. Επιλέξτε το container registry που συνδέεται με το Azure Machine Learning workspace. Για παράδειγμα, *finetunephicontainerregistry*.

1. Εκτελέστε τις παρακάτω ενέργειες για να μεταβείτε στη σελίδα Add role assignment:

    - Επιλέξτε **Access Control (IAM)** από την αριστερή καρτέλα.
    - Επιλέξτε **+ Add** από το μενού πλοήγησης.
    - Επιλέξτε **Add role assignment** από το μενού πλοήγησης.

1. Στη σελίδα Add role assignment, εκτελέστε τις παρακάτω ενέργειες:

    - Στη σελίδα Role, πληκτρολογήστε *AcrPull* στη **γραμμή αναζήτησης** και επιλέξτε **AcrPull** από τις επιλογές που εμφανίζονται.
    - Στη σελίδα Role, επιλέξτε **Next**.
    - Στη σελίδα Members, επιλέξτε **Assign access to** **Managed identity**.
    - Στη σελίδα Members, επιλέξτε **+ Select members**.
    - Στη σελίδα Select managed identities, επιλέξτε τη **Συνδρομή Azure** σας.
    - Στη σελίδα Select managed identities, επιλέξτε τη **Διαχειριζόμενη ταυτότητα** που δημιουργήσατε. Για παράδειγμα, *finetunephi-managedidentity*.
    - Στη σελίδα Select managed identities, επιλέξτε **Select**.
    - Επιλέξτε **Review + assign**.

### Ρύθμιση έργου

Για να κατεβάσετε τα σύνολα δεδομένων που απαιτούνται για την προσαρμογή, θα ρυθμίσετε ένα τοπικό περιβάλλον.

Σε αυτή την άσκηση, θα:

- Δημιουργήσετε έναν φάκελο για να εργαστείτε μέσα σε αυτόν.
- Δημιουργήσετε ένα εικονικό περιβάλλον.
- Εγκαταστήσετε τα απαιτούμενα πακέτα.
- Δημιουργήσετε ένα αρχείο *download_dataset.py* για να κατεβάσετε το σύνολο δεδομένων.

#### Δημιουργία φακέλου για εργασία

1. Ανοίξτε ένα τερματικό παράθυρο και πληκτρολογήστε την παρακάτω εντολή για να δημιουργήσετε έναν φάκελο με όνομα *finetune-phi* στην προεπιλεγμένη διαδρομή.

    ```console
    mkdir finetune-phi
    ```

2. Πληκτρολογήστε την παρακάτω εντολή στο τερματικό σας για να μεταβείτε στον φάκε
1. Επισκεφθείτε το [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Επιλέξτε **Compute** από την καρτέλα στην αριστερή πλευρά.

1. Επιλέξτε **Compute clusters** από το μενού πλοήγησης.

1. Επιλέξτε **+ New**.

    ![Επιλέξτε compute.](../../../../../../translated_images/06-01-select-compute.e151458e2884d4877a05acf3553d015cd63c0c6ed056efcfbd425c715692a947.el.png)

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Επιλέξτε την **Περιοχή (Region)** που θέλετε να χρησιμοποιήσετε.
    - Ρυθμίστε το **Virtual machine tier** σε **Dedicated**.
    - Ρυθμίστε τον **Τύπο εικονικής μηχανής (Virtual machine type)** σε **GPU**.
    - Ορίστε το φίλτρο **Μέγεθος εικονικής μηχανής (Virtual machine size)** σε **Select from all options**.
    - Επιλέξτε το **Μέγεθος εικονικής μηχανής (Virtual machine size)** σε **Standard_NC24ads_A100_v4**.

    ![Δημιουργία cluster.](../../../../../../translated_images/06-02-create-cluster.19e5e8403b754eecaa1e2886625335ca16f4161391e0d75ef85f2e5eaa8ffb5a.el.png)

1. Επιλέξτε **Next**.

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Εισάγετε **Compute name**. Πρέπει να είναι μοναδική τιμή.
    - Ορίστε τον **Ελάχιστο αριθμό κόμβων (Minimum number of nodes)** σε **0**.
    - Ορίστε τον **Μέγιστο αριθμό κόμβων (Maximum number of nodes)** σε **1**.
    - Ορίστε το **Idle seconds before scale down** σε **120**.

    ![Δημιουργία cluster.](../../../../../../translated_images/06-03-create-cluster.8796fad73635590754b6095c30fe98112db248596d194cd5b0af077cca371ac1.el.png)

1. Επιλέξτε **Create**.

#### Fine-tune το μοντέλο Phi-3

1. Επισκεφθείτε το [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Επιλέξτε το Azure Machine Learning workspace που δημιουργήσατε.

    ![Επιλέξτε workspace που δημιουργήσατε.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.el.png)

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Επιλέξτε **Model catalog** από την καρτέλα στην αριστερή πλευρά.
    - Πληκτρολογήστε *phi-3-mini-4k* στη **γραμμή αναζήτησης** και επιλέξτε **Phi-3-mini-4k-instruct** από τις επιλογές που εμφανίζονται.

    ![Πληκτρολογήστε phi-3-mini-4k.](../../../../../../translated_images/06-05-type-phi-3-mini-4k.808fa02bdce5b9cda91e19a5fa9ff254697575293245ea49263f860354032e66.el.png)

1. Επιλέξτε **Fine-tune** από το μενού πλοήγησης.

    ![Επιλέξτε fine tune.](../../../../../../translated_images/06-06-select-fine-tune.bcb1fd63ead2da12219c0615d35cef2c9ce18d3c8467ef604d755accba87a063.el.png)

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Ρυθμίστε το **Select task type** σε **Chat completion**.
    - Επιλέξτε **+ Select data** για να ανεβάσετε **Traning data**.
    - Ρυθμίστε τον τύπο μεταφόρτωσης δεδομένων επικύρωσης σε **Provide different validation data**.
    - Επιλέξτε **+ Select data** για να ανεβάσετε **Validation data**.

    ![Συμπληρώστε τη σελίδα fine-tuning.](../../../../../../translated_images/06-07-fill-finetuning.dcf5eb5a2d6d2bfb727e1fc278de717df0b25cf8d11ace970df8ea7d5951591e.el.png)

    > [!TIP]
    >
    > Μπορείτε να επιλέξετε **Advanced settings** για να προσαρμόσετε ρυθμίσεις, όπως το **learning_rate** και το **lr_scheduler_type**, ώστε να βελτιστοποιήσετε τη διαδικασία fine-tuning σύμφωνα με τις ανάγκες σας.

1. Επιλέξτε **Finish**.

1. Σε αυτήν την άσκηση, πραγματοποιήσατε επιτυχώς fine-tuning στο μοντέλο Phi-3 χρησιμοποιώντας το Azure Machine Learning. Σημειώστε ότι η διαδικασία fine-tuning μπορεί να διαρκέσει αρκετό χρόνο. Μετά την εκτέλεση της εργασίας fine-tuning, θα χρειαστεί να περιμένετε να ολοκληρωθεί. Μπορείτε να παρακολουθείτε την κατάσταση της εργασίας fine-tuning μεταβαίνοντας στην καρτέλα Jobs στην αριστερή πλευρά του Azure Machine Learning Workspace. Στη συνέχεια, θα αναπτύξετε το fine-tuned μοντέλο και θα το ενσωματώσετε στο Prompt flow.

    ![Δείτε την εργασία fine-tuning.](../../../../../../translated_images/06-08-output.3fedec9572bca5d86b7db3a6d060345c762aa59ce6aefa2b1998154b9f475b69.el.png)

### Ανάπτυξη του fine-tuned μοντέλου Phi-3

Για να ενσωματώσετε το fine-tuned μοντέλο Phi-3 στο Prompt flow, πρέπει να το αναπτύξετε ώστε να είναι διαθέσιμο για πραγματικό χρόνο προβλέψεις. Αυτή η διαδικασία περιλαμβάνει την εγγραφή του μοντέλου, τη δημιουργία ενός online endpoint και την ανάπτυξη του μοντέλου.

Σε αυτήν την άσκηση, θα:

- Εγγράψετε το fine-tuned μοντέλο στο Azure Machine Learning workspace.
- Δημιουργήσετε ένα online endpoint.
- Αναπτύξετε το εγγεγραμμένο fine-tuned μοντέλο Phi-3.

#### Εγγραφή του fine-tuned μοντέλου

1. Επισκεφθείτε το [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723).

1. Επιλέξτε το Azure Machine Learning workspace που δημιουργήσατε.

    ![Επιλέξτε workspace που δημιουργήσατε.](../../../../../../translated_images/06-04-select-workspace.f5449319befd49bad6028622f194507712fccee9d744f96b78765d2c1ffcb9c3.el.png)

1. Επιλέξτε **Models** από την καρτέλα στην αριστερή πλευρά.
1. Επιλέξτε **+ Register**.
1. Επιλέξτε **From a job output**.

    ![Εγγραφή μοντέλου.](../../../../../../translated_images/07-01-register-model.46cad47d2bb083c74e616691ef836735209ffc42b29fb432a1acbef52e28d41f.el.png)

1. Επιλέξτε την εργασία που δημιουργήσατε.

    ![Επιλέξτε εργασία.](../../../../../../translated_images/07-02-select-job.a5d34472aead80a4b69594f277dd43491c6aaf42d847940c1dc2081d909a23f3.el.png)

1. Επιλέξτε **Next**.

1. Ρυθμίστε το **Model type** σε **MLflow**.

1. Βεβαιωθείτε ότι είναι επιλεγμένο το **Job output**. Θα πρέπει να είναι αυτόματα επιλεγμένο.

    ![Επιλέξτε έξοδο.](../../../../../../translated_images/07-03-select-output.e1a56a25db9065901df821343ff894ca45ce0569c3daf30b5aafdd060f26e059.el.png)

2. Επιλέξτε **Next**.

3. Επιλέξτε **Register**.

    ![Επιλέξτε εγγραφή.](../../../../../../translated_images/07-04-register.71316a5a4d2e1f520f14fee93be7865a785971cdfdd8cd08779866f5f29f7da4.el.png)

4. Μπορείτε να δείτε το εγγεγραμμένο μοντέλο σας μεταβαίνοντας στο μενού **Models** από την αριστερή πλευρά.

    ![Εγγεγραμμένο μοντέλο.](../../../../../../translated_images/07-05-registered-model.969e2ec99a4cbf5cc9bb006b118110803853a15aa3c499eceb7812d976bd6128.el.png)

#### Ανάπτυξη του fine-tuned μοντέλου

1. Μεταβείτε στο Azure Machine Learning workspace που δημιουργήσατε.

1. Επιλέξτε **Endpoints** από την καρτέλα στην αριστερή πλευρά.

1. Επιλέξτε **Real-time endpoints** από το μενού πλοήγησης.

    ![Δημιουργία endpoint.](../../../../../../translated_images/07-06-create-endpoint.0741c2a4369bd3b9c4e17aa7b31ed0337bfb1303f9038244784791250164b2f7.el.png)

1. Επιλέξτε **Create**.

1. Επιλέξτε το εγγεγραμμένο μοντέλο που δημιουργήσατε.

    ![Επιλέξτε εγγεγραμμένο μοντέλο.](../../../../../../translated_images/07-07-select-registered-model.7a270d391fd543a21d9a024d2ea516667c039393dbe954019e19162dd07d2387.el.png)

1. Επιλέξτε **Select**.

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Ρυθμίστε το **Virtual machine** σε *Standard_NC6s_v3*.
    - Ορίστε τον **Αριθμό instances (Instance count)** που θέλετε να χρησιμοποιήσετε. Για παράδειγμα, *1*.
    - Ρυθμίστε το **Endpoint** σε **New** για να δημιουργήσετε ένα endpoint.
    - Εισάγετε **Endpoint name**. Πρέπει να είναι μοναδική τιμή.
    - Εισάγετε **Deployment name**. Πρέπει να είναι μοναδική τιμή.

    ![Συμπληρώστε τις ρυθμίσεις ανάπτυξης.](../../../../../../translated_images/07-08-deployment-setting.5907ac712d60af1f5e6d18e09a39b3fcd5706e9ce2e3dffc7120a2f79e025483.el.png)

1. Επιλέξτε **Deploy**.

> [!WARNING]
> Για να αποφύγετε πρόσθετες χρεώσεις στον λογαριασμό σας, βεβαιωθείτε ότι διαγράψατε το δημιουργημένο endpoint στο Azure Machine Learning workspace.
>

#### Έλεγχος κατάστασης ανάπτυξης στο Azure Machine Learning Workspace

1. Μεταβείτε στο Azure Machine Learning workspace που δημιουργήσατε.

1. Επιλέξτε **Endpoints** από την καρτέλα στην αριστερή πλευρά.

1. Επιλέξτε το endpoint που δημιουργήσατε.

    ![Επιλέξτε endpoints](../../../../../../translated_images/07-09-check-deployment.dc970e535b490992ff68e6127c9d520389b3f0f5a5fc41358c2ad16669bce49a.el.png)

1. Σε αυτήν τη σελίδα, μπορείτε να διαχειριστείτε τα endpoints κατά τη διάρκεια της διαδικασίας ανάπτυξης.

> [!NOTE]
> Όταν ολοκληρωθεί η ανάπτυξη, βεβαιωθείτε ότι το **Live traffic** έχει οριστεί σε **100%**. Αν όχι, επιλέξτε **Update traffic** για να προσαρμόσετε τις ρυθμίσεις. Σημειώστε ότι δεν μπορείτε να δοκιμάσετε το μοντέλο αν το traffic είναι ρυθμισμένο στο 0%.
>
> ![Ορισμός traffic.](../../../../../../translated_images/07-10-set-traffic.a0fccfd2b1e2bd0dba22860daa76d35999cfcf23b53ecc09df92f992c4cab64f.el.png)
>

## Σενάριο 3: Ενσωμάτωση με το Prompt flow και συνομιλία με το προσαρμοσμένο μοντέλο σας στο Azure AI Foundry

### Ενσωμάτωση του προσαρμοσμένου μοντέλου Phi-3 με το Prompt flow

Αφού αναπτύξετε επιτυχώς το fine-tuned μοντέλο σας, μπορείτε τώρα να το ενσωματώσετε με το Prompt Flow για να το χρησιμοποιήσετε σε εφαρμογές πραγματικού χρόνου, επιτρέποντας μια ποικιλία διαδραστικών εργασιών με το προσαρμοσμένο μοντέλο Phi-3 σας.

Σε αυτήν την άσκηση, θα:

- Δημιουργήσετε το Azure AI Foundry Hub.
- Δημιουργήσετε το Azure AI Foundry Project.
- Δημιουργήσετε Prompt flow.
- Προσθέσετε μια προσαρμοσμένη σύνδεση για το fine-tuned μοντέλο Phi-3.
- Ρυθμίσετε το Prompt flow για συνομιλία με το προσαρμοσμένο μοντέλο Phi-3 σας.

> [!NOTE]
> Μπορείτε επίσης να ενσωματώσετε με το Promptflow χρησιμοποιώντας το Azure ML Studio. Η ίδια διαδικασία ενσωμάτωσης μπορεί να εφαρμοστεί και στο Azure ML Studio.

#### Δημιουργία Azure AI Foundry Hub

Πρέπει να δημιουργήσετε ένα Hub πριν δημιουργήσετε το Project. Το Hub λειτουργεί σαν Resource Group, επιτρέποντάς σας να οργανώνετε και να διαχειρίζεστε πολλαπλά Projects στο Azure AI Foundry.

1. Επισκεφθείτε το [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Επιλέξτε **All hubs** από την καρτέλα στην αριστερή πλευρά.

1. Επιλέξτε **+ New hub** από το μενού πλοήγησης.

    ![Δημιουργία hub.](../../../../../../translated_images/08-01-create-hub.c54d78fb49923ff1d8c6a11010a8c8eca9b044d525182a2a1700b3ff4c542674.el.png)

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Εισάγετε **Hub name**. Πρέπει να είναι μοναδική τιμή.
    - Επιλέξτε την Azure **Subscription** σας.
    - Επιλέξτε το **Resource group** που θα χρησιμοποιήσετε (δημιουργήστε νέο αν χρειάζεται).
    - Επιλέξτε την **Τοποθεσία (Location)** που θέλετε να χρησιμοποιήσετε.
    - Επιλέξτε το **Connect Azure AI Services** που θα χρησιμοποιήσετε (δημιουργήστε νέο αν χρειάζεται).
    - Ρυθμίστε το **Connect Azure AI Search** σε **Skip connecting**.

    ![Συμπληρώστε το hub.](../../../../../../translated_images/08-02-fill-hub.ced9ab1db4d2f3324d3d34bd9e846641e80bb9e4ebfc56f47d09ce6885e9caf7.el.png)

1. Επιλέξτε **Next**.

#### Δημιουργία Azure AI Foundry Project

1. Στο Hub που δημιουργήσατε, επιλέξτε **All projects** από την καρτέλα στην αριστερή πλευρά.

1. Επιλέξτε **+ New project** από το μενού πλοήγησης.

    ![Επιλέξτε νέο project.](../../../../../../translated_images/08-04-select-new-project.e3033e8fa767fa86e03dc830014e59222eceacbc322082771d0e11be6e60ed6a.el.png)

1. Εισάγετε **Project name**. Πρέπει να είναι μοναδική τιμή.

    ![Δημιουργία project.](../../../../../../translated_images/08-05-create-project.6172ff97b4c49ad0f364e6d4a7b658dba45f8e27aaa2126a83d0af77056450b0.el.png)

1. Επιλέξτε **Create a project**.

#### Προσθήκη προσαρμοσμένης σύνδεσης για το fine-tuned μοντέλο Phi-3

Για να ενσωματώσετε το προσαρμοσμένο μοντέλο Phi-3 σας με το Prompt flow, πρέπει να αποθηκεύσετε το endpoint και το κλειδί του μοντέλου σε μια προσαρμοσμένη σύνδεση. Αυτή η ρύθμιση εξασφαλίζει την πρόσβαση στο προσαρμοσμένο μοντέλο Phi-3 σας στο Prompt flow.

#### Ρύθμιση api key και endpoint uri του fine-tuned μοντέλου Phi-3

1. Επισκεφθείτε το [Azure ML Studio](https://ml.azure.com/home?WT.mc_id=aiml-137032-kinfeylo).

1. Μεταβείτε στο Azure Machine learning workspace που δημιουργήσατε.

1. Επιλέξτε **Endpoints** από την καρτέλα στην αριστερή πλευρά.

    ![Επιλέξτε endpoints.](../../../../../../translated_images/08-06-select-endpoints.7c12a37c1b477c2829a045a230ae9c18373156fe7adb797dcabd3ab18bd139a7.el.png)

1. Επιλέξτε το endpoint που δημιουργήσατε.

    ![Επιλέξτε endpoints.](../../../../../../translated_images/08-07-select-endpoint-created.d69043d757b715c24c88c9ae7e796247eb8909bae8967839a7dc30de3f403caf.el.png)

1. Επιλέξτε **Consume** από το μενού πλοήγησης.

1. Αντιγράψτε το **REST endpoint** και το **Primary key** σας.
![Αντιγραφή κλειδιού API και URI τελικού σημείου.](../../../../../../translated_images/08-08-copy-endpoint-key.511a027574cee0efc50fdda33b6de1e1e268c5979914ba944b72092f72f95544.el.png)

#### Προσθήκη Προσαρμοσμένης Σύνδεσης

1. Επισκεφθείτε το [Azure AI Foundry](https://ai.azure.com/?WT.mc_id=aiml-137032-kinfeylo).

1. Μεταβείτε στο έργο Azure AI Foundry που δημιουργήσατε.

1. Στο έργο που δημιουργήσατε, επιλέξτε **Ρυθμίσεις** από την αριστερή πλαϊνή καρτέλα.

1. Επιλέξτε **+ Νέα σύνδεση**.

    ![Επιλογή νέας σύνδεσης.](../../../../../../translated_images/08-09-select-new-connection.c55d4faa9f655e163a5d7aec1f21843ea30738d4e8c5ce5f0724048ebc6ca007.el.png)

1. Επιλέξτε **Προσαρμοσμένα κλειδιά** από το μενού πλοήγησης.

    ![Επιλογή προσαρμοσμένων κλειδιών.](../../../../../../translated_images/08-10-select-custom-keys.78c5267f5d037ef1931bc25e4d1a77747b709df7141a9968e25ebd9188ac9fdd.el.png)

1. Εκτελέστε τις παρακάτω ενέργειες:

    - Επιλέξτε **+ Προσθήκη ζευγών κλειδιού-τιμής**.
    - Για το όνομα κλειδιού, εισάγετε **endpoint** και επικολλήστε το endpoint που αντιγράψατε από το Azure ML Studio στο πεδίο τιμής.
    - Επιλέξτε ξανά **+ Προσθήκη ζευγών κλειδιού-τιμής**.
    - Για το όνομα κλειδιού, εισάγετε **key** και επικολλήστε το κλειδί που αντιγράψατε από το Azure ML Studio στο πεδίο τιμής.
    - Αφού προσθέσετε τα κλειδιά, επιλέξτε **is secret** για να αποτρέψετε την έκθεση του κλειδιού.

    ![Προσθήκη σύνδεσης.](../../../../../../translated_images/08-11-add-connection.a2e410ab11c11a4798fe8ac56ba4e9707d1a5079be00f6f91bb187515f756a31.el.png)

1. Επιλέξτε **Προσθήκη σύνδεσης**.

#### Δημιουργία Prompt Flow

Προσθέσατε μια προσαρμοσμένη σύνδεση στο Azure AI Foundry. Τώρα, ας δημιουργήσουμε ένα Prompt flow ακολουθώντας τα παρακάτω βήματα. Στη συνέχεια, θα συνδέσετε αυτό το Prompt flow με την προσαρμοσμένη σύνδεση ώστε να μπορείτε να χρησιμοποιήσετε το fine-tuned μοντέλο μέσα στο Prompt flow.

1. Μεταβείτε στο έργο Azure AI Foundry που δημιουργήσατε.

1. Επιλέξτε **Prompt flow** από την αριστερή πλαϊνή καρτέλα.

1. Επιλέξτε **+ Δημιουργία** από το μενού πλοήγησης.

    ![Επιλογή Promptflow.](../../../../../../translated_images/08-12-select-promptflow.1782ec6988841bb53c35011f31fbebc1bdc09c6f4653fea935176212ba608af1.el.png)

1. Επιλέξτε **Chat flow** από το μενού πλοήγησης.

    ![Επιλογή chat flow.](../../../../../../translated_images/08-13-select-flow-type.f346cc55beed0b2774bd61b2afe86f3640cc772c1715914926333b0e4d6281ee.el.png)

1. Εισάγετε **Όνομα φακέλου** που θέλετε να χρησιμοποιήσετε.

    ![Εισαγωγή ονόματος.](../../../../../../translated_images/08-14-enter-name.e2b324f7734290157520834403e041f46c06cbdfa5633f4c91725f7389b41cf7.el.png)

2. Επιλέξτε **Δημιουργία**.

#### Ρύθμιση Prompt Flow για συνομιλία με το προσαρμοσμένο μοντέλο Phi-3

Χρειάζεται να ενσωματώσετε το fine-tuned μοντέλο Phi-3 σε ένα Prompt flow. Ωστόσο, το υπάρχον Prompt flow που παρέχεται δεν είναι σχεδιασμένο για αυτόν τον σκοπό. Επομένως, πρέπει να ανασχεδιάσετε το Prompt flow για να επιτρέψετε την ενσωμάτωση του προσαρμοσμένου μοντέλου.

1. Στο Prompt flow, εκτελέστε τις παρακάτω ενέργειες για να αναδομήσετε τη ροή:

    - Επιλέξτε **Λειτουργία αρχείου Raw**.
    - Διαγράψτε όλο τον υπάρχοντα κώδικα στο αρχείο *flow.dag.yml*.
    - Προσθέστε τον παρακάτω κώδικα στο αρχείο *flow.dag.yml*.

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

    - Επιλέξτε **Αποθήκευση**.

    ![Επιλογή λειτουργίας raw αρχείου.](../../../../../../translated_images/08-15-select-raw-file-mode.8383d30bf0b893f0f05e340e68fa3631ee2a526b861551865e2e8a5dd6d4b02b.el.png)

1. Προσθέστε τον παρακάτω κώδικα στο αρχείο *integrate_with_promptflow.py* για να χρησιμοποιήσετε το προσαρμοσμένο μοντέλο Phi-3 στο Prompt flow.

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        data = {
            "input_data": {
                "input_string": [
                    {"role": "user", "content": input_data}
                ],
                "parameters": {
                    "temperature": 0.7,
                    "max_new_tokens": 128
                }
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Επικόλληση κώδικα prompt flow.](../../../../../../translated_images/08-16-paste-promptflow-code.1e74d673739ae3fc114a386fd7dff65d6f98d8bf69be16d4b577cbb75844ba38.el.png)

> [!NOTE]
> Για περισσότερες λεπτομέρειες σχετικά με τη χρήση του Prompt flow στο Azure AI Foundry, μπορείτε να ανατρέξετε στον οδηγό [Prompt flow στο Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow).

1. Επιλέξτε **Είσοδος συνομιλίας**, **Έξοδος συνομιλίας** για να ενεργοποιήσετε τη συνομιλία με το μοντέλο σας.

    ![Είσοδος και έξοδος.](../../../../../../translated_images/08-17-select-input-output.71fb7bf702d1fff773d9d929aa482bc1962e8ce36dac04ad9d9b86db8c6bb776.el.png)

1. Τώρα είστε έτοιμοι να συνομιλήσετε με το προσαρμοσμένο μοντέλο Phi-3 σας. Στην επόμενη άσκηση, θα μάθετε πώς να ξεκινήσετε το Prompt flow και να το χρησιμοποιήσετε για συνομιλία με το fine-tuned μοντέλο Phi-3 σας.

> [!NOTE]
>
> Η αναδομημένη ροή θα πρέπει να μοιάζει με την παρακάτω εικόνα:
>
> ![Παράδειγμα ροής.](../../../../../../translated_images/08-18-graph-example.bb35453a6bfee310805715e3ec0678e118273bc32ae8248acfcf8e4c553ed1e5.el.png)
>

### Συνομιλήστε με το προσαρμοσμένο μοντέλο Phi-3 σας

Τώρα που έχετε fine-tuned και ενσωματώσει το προσαρμοσμένο μοντέλο Phi-3 σας με το Prompt flow, είστε έτοιμοι να ξεκινήσετε την αλληλεπίδραση με αυτό. Αυτή η άσκηση θα σας καθοδηγήσει στη διαδικασία ρύθμισης και έναρξης συνομιλίας με το μοντέλο σας χρησιμοποιώντας το Prompt flow. Ακολουθώντας αυτά τα βήματα, θα μπορείτε να αξιοποιήσετε πλήρως τις δυνατότητες του fine-tuned μοντέλου Phi-3 σας για διάφορες εργασίες και συνομιλίες.

- Συνομιλήστε με το προσαρμοσμένο μοντέλο Phi-3 σας χρησιμοποιώντας το Prompt flow.

#### Ξεκινήστε το Prompt Flow

1. Επιλέξτε **Έναρξη συνεδριών υπολογισμού** για να ξεκινήσετε το Prompt flow.

    ![Έναρξη συνεδρίας υπολογισμού.](../../../../../../translated_images/09-01-start-compute-session.bf4fd553850fc0efcb8f8fa1e089839f9ea09333f48689aeb8ecce41e4a1ba42.el.png)

1. Επιλέξτε **Επικύρωση και ανάλυση εισόδου** για να ανανεώσετε τις παραμέτρους.

    ![Επικύρωση εισόδου.](../../../../../../translated_images/09-02-validate-input.24092d447308054d25144e73649a9ac630bd895c376297b03d82354090815a97.el.png)

1. Επιλέξτε την **Τιμή** της **σύνδεσης** στην προσαρμοσμένη σύνδεση που δημιουργήσατε. Για παράδειγμα, *connection*.

    ![Σύνδεση.](../../../../../../translated_images/09-03-select-connection.77f4eef8f74410b4abae1e34ba0f6bc34b3f1390b7158ab4023a08c025ff4993.el.png)

#### Συνομιλήστε με το προσαρμοσμένο μοντέλο σας

1. Επιλέξτε **Συνομιλία**.

    ![Επιλογή συνομιλίας.](../../../../../../translated_images/09-04-select-chat.3cd7462ff5c6e3aa0eb686a29b91420a8fdcd3066fba5507dc257d7b91a3c492.el.png)

1. Να ένα παράδειγμα αποτελεσμάτων: Τώρα μπορείτε να συνομιλήσετε με το προσαρμοσμένο μοντέλο Phi-3 σας. Συνιστάται να κάνετε ερωτήσεις βάσει των δεδομένων που χρησιμοποιήθηκαν για το fine-tuning.

    ![Συνομιλία με prompt flow.](../../../../../../translated_images/09-05-chat-with-promptflow.30574a870c00e676916d9afb28b70d3fb90e1f00e73f70413cd6aeed74d9c151.el.png)

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες μετάφρασης που βασίζονται σε τεχνητή νοημοσύνη. Ενώ καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή λανθασμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.