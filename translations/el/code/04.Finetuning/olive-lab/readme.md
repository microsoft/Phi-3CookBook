# Εργαστήριο: Βελτιστοποίηση AI μοντέλων για τοπική εκτέλεση

## Εισαγωγή 

> [!IMPORTANT]
> Αυτό το εργαστήριο απαιτεί **GPU Nvidia A10 ή A100** με εγκατεστημένους τους αντίστοιχους drivers και το CUDA toolkit (έκδοση 12+).

> [!NOTE]
> Αυτό είναι ένα εργαστήριο διάρκειας **35 λεπτών**, που θα σας προσφέρει μια πρακτική εισαγωγή στις βασικές έννοιες της βελτιστοποίησης μοντέλων για τοπική εκτέλεση χρησιμοποιώντας το OLIVE.

## Στόχοι Μάθησης

Μέχρι το τέλος αυτού του εργαστηρίου, θα μπορείτε να χρησιμοποιήσετε το OLIVE για:

- Κβαντοποίηση ενός AI μοντέλου χρησιμοποιώντας τη μέθοδο κβαντοποίησης AWQ.
- Προσαρμογή ενός AI μοντέλου για μια συγκεκριμένη εργασία.
- Δημιουργία LoRA adapters (προσαρμοσμένου μοντέλου) για αποδοτική τοπική εκτέλεση με το ONNX Runtime.

### Τι είναι το Olive

Το Olive (*O*NNX *live*) είναι ένα εργαλείο βελτιστοποίησης μοντέλων με συνοδευτικό CLI, που σας επιτρέπει να παραδίδετε μοντέλα για το ONNX runtime +++https://onnxruntime.ai+++ με ποιότητα και απόδοση.

![Olive Flow](../../../../../translated_images/olive-flow.e4682fa65f77777f49e884482fa8dd83eadcb90904fcb41a54093af85c330060.el.png)

Η είσοδος στο Olive είναι συνήθως ένα μοντέλο PyTorch ή Hugging Face, και η έξοδος είναι ένα βελτιστοποιημένο ONNX μοντέλο που εκτελείται σε μια συσκευή (στόχος ανάπτυξης) με το ONNX runtime. Το Olive θα βελτιστοποιήσει το μοντέλο για τον AI επιταχυντή (NPU, GPU, CPU) της συσκευής, όπως παρέχεται από κατασκευαστές υλικού όπως Qualcomm, AMD, Nvidia ή Intel.

Το Olive εκτελεί μια *ροή εργασίας*, που είναι μια διατεταγμένη ακολουθία μεμονωμένων εργασιών βελτιστοποίησης μοντέλου που ονομάζονται *περάσματα* - παραδείγματα περιλαμβάνουν: συμπίεση μοντέλου, καταγραφή γραφήματος, κβαντοποίηση, βελτιστοποίηση γραφήματος. Κάθε πέρασμα έχει ένα σύνολο παραμέτρων που μπορούν να ρυθμιστούν για την επίτευξη των καλύτερων μετρικών, όπως ακρίβεια και καθυστέρηση, που αξιολογούνται από τον αντίστοιχο αξιολογητή. Το Olive χρησιμοποιεί μια στρατηγική αναζήτησης που εφαρμόζει έναν αλγόριθμο αναζήτησης για αυτόματη ρύθμιση κάθε περάσματος μεμονωμένα ή σε συνδυασμό.

#### Οφέλη του Olive

- **Μείωση της απογοήτευσης και του χρόνου** από τη δοκιμή και το σφάλμα με διαφορετικές τεχνικές για βελτιστοποίηση γραφήματος, συμπίεση και κβαντοποίηση. Ορίστε τους περιορισμούς ποιότητας και απόδοσης και αφήστε το Olive να βρει αυτόματα το καλύτερο μοντέλο για εσάς.
- **Περισσότερα από 40 ενσωματωμένα στοιχεία βελτιστοποίησης μοντέλων** που καλύπτουν προηγμένες τεχνικές κβαντοποίησης, συμπίεσης, βελτιστοποίησης γραφήματος και προσαρμογής.
- **Εύχρηστο CLI** για κοινές εργασίες βελτιστοποίησης μοντέλων. Για παράδειγμα, olive quantize, olive auto-opt, olive finetune.
- Ενσωματωμένη συσκευασία και ανάπτυξη μοντέλων.
- Υποστήριξη για δημιουργία μοντέλων για **Multi LoRA serving**.
- Δημιουργία ροών εργασίας χρησιμοποιώντας YAML/JSON για οργάνωση εργασιών βελτιστοποίησης και ανάπτυξης μοντέλων.
- Ενσωμάτωση με **Hugging Face** και **Azure AI**.
- Ενσωματωμένος μηχανισμός **caching** για **εξοικονόμηση κόστους**.

## Οδηγίες Εργαστηρίου
> [!NOTE]
> Βεβαιωθείτε ότι έχετε προετοιμάσει το Azure AI Hub και το Project σας και έχετε ρυθμίσει τον A100 υπολογιστή σας όπως στο Εργαστήριο 1.

### Βήμα 0: Σύνδεση με το Azure AI Compute

Θα συνδεθείτε με το Azure AI compute χρησιμοποιώντας τη δυνατότητα απομακρυσμένης σύνδεσης στο **VS Code.** 

1. Ανοίξτε την εφαρμογή επιφάνειας εργασίας **VS Code**:
1. Ανοίξτε το **command palette** χρησιμοποιώντας **Shift+Ctrl+P**
1. Στο command palette, αναζητήστε **AzureML - remote: Connect to compute instance in New Window**.
1. Ακολουθήστε τις οδηγίες στην οθόνη για να συνδεθείτε με το Compute. Αυτό περιλαμβάνει την επιλογή της συνδρομής Azure, του Resource Group, του Project και του ονόματος του Compute που ρυθμίσατε στο Εργαστήριο 1.
1. Μόλις συνδεθείτε στο Azure ML Compute node, αυτό θα εμφανίζεται στην **κάτω αριστερή γωνία του Visual Code** `><Azure ML: Compute Name`

### Βήμα 1: Κλωνοποίηση αυτού του αποθετηρίου

Στο VS Code, μπορείτε να ανοίξετε ένα νέο τερματικό με **Ctrl+J** και να κλωνοποιήσετε αυτό το αποθετήριο:

Στο τερματικό θα δείτε την προτροπή

```
azureuser@computername:~/cloudfiles/code$ 
```
Κλωνοποιήστε τη λύση 

```bash
cd ~/localfiles
git clone https://github.com/microsoft/phi-3cookbook.git
```

### Βήμα 2: Άνοιγμα Φακέλου στο VS Code

Για να ανοίξετε το VS Code στον σχετικό φάκελο, εκτελέστε την παρακάτω εντολή στο τερματικό, η οποία θα ανοίξει ένα νέο παράθυρο:

```bash
code phi-3cookbook/code/04.Finetuning/Olive-lab
```

Εναλλακτικά, μπορείτε να ανοίξετε τον φάκελο επιλέγοντας **File** > **Open Folder**. 

### Βήμα 3: Εξαρτήσεις

Ανοίξτε ένα παράθυρο τερματικού στο VS Code στο Azure AI Compute Instance σας (συμβουλή: **Ctrl+J**) και εκτελέστε τις παρακάτω εντολές για να εγκαταστήσετε τις εξαρτήσεις:

```bash
conda create -n olive-ai python=3.11 -y
conda activate olive-ai
pip install -r requirements.txt
az extension remove -n azure-cli-ml
az extension add -n ml
```

> [!NOTE]
> Θα χρειαστούν περίπου **5 λεπτά** για να εγκατασταθούν όλες οι εξαρτήσεις.

Σε αυτό το εργαστήριο θα κατεβάσετε και θα ανεβάσετε μοντέλα στον κατάλογο μοντέλων του Azure AI. Για να έχετε πρόσβαση στον κατάλογο μοντέλων, θα χρειαστεί να συνδεθείτε στο Azure χρησιμοποιώντας:

```bash
az login
```

> [!NOTE]
> Κατά τη σύνδεση θα σας ζητηθεί να επιλέξετε τη συνδρομή σας. Βεβαιωθείτε ότι έχετε ορίσει τη συνδρομή που παρέχεται για αυτό το εργαστήριο.

### Βήμα 4: Εκτέλεση εντολών Olive 

Ανοίξτε ένα παράθυρο τερματικού στο VS Code στο Azure AI Compute Instance σας (συμβουλή: **Ctrl+J**) και βεβαιωθείτε ότι το `olive-ai` περιβάλλον conda είναι ενεργοποιημένο:

```bash
conda activate olive-ai
```

Στη συνέχεια, εκτελέστε τις παρακάτω εντολές Olive στη γραμμή εντολών.

1. **Επιθεώρηση δεδομένων:** Σε αυτό το παράδειγμα, θα προσαρμόσετε το μοντέλο Phi-3.5-Mini ώστε να εξειδικεύεται στην απάντηση ερωτήσεων που σχετίζονται με ταξίδια. Ο παρακάτω κώδικας εμφανίζει τις πρώτες εγγραφές του συνόλου δεδομένων, που είναι σε μορφή JSON lines:
   
    ```bash
    head data/data_sample_travel.jsonl
    ```
1. **Κβαντοποίηση του μοντέλου:** Πριν από την εκπαίδευση του μοντέλου, πρώτα το κβαντοποιείτε με την παρακάτω εντολή που χρησιμοποιεί μια τεχνική που ονομάζεται Active Aware Quantization (AWQ) +++https://arxiv.org/abs/2306.00978+++. Η AWQ κβαντοποιεί τα βάρη ενός μοντέλου λαμβάνοντας υπόψη τις ενεργοποιήσεις που παράγονται κατά την εκτέλεση. Αυτό σημαίνει ότι η διαδικασία κβαντοποίησης λαμβάνει υπόψη την πραγματική κατανομή δεδομένων στις ενεργοποιήσεις, οδηγώντας σε καλύτερη διατήρηση της ακρίβειας του μοντέλου σε σύγκριση με παραδοσιακές μεθόδους κβαντοποίησης βαρών.
    
    ```bash
    olive quantize \
       --model_name_or_path microsoft/Phi-3.5-mini-instruct \
       --trust_remote_code \
       --algorithm awq \
       --output_path models/phi/awq \
       --log_level 1
    ```
    
    Χρειάζονται περίπου **8 λεπτά** για να ολοκληρωθεί η κβαντοποίηση AWQ, η οποία θα **μειώσει το μέγεθος του μοντέλου από περίπου 7.5GB σε περίπου 2.5GB**.
   
   Σε αυτό το εργαστήριο, σας δείχνουμε πώς να εισάγετε μοντέλα από το Hugging Face (για παράδειγμα: `microsoft/Phi-3.5-mini-instruct`). However, Olive also allows you to input models from the Azure AI catalog by updating the `model_name_or_path` argument to an Azure AI asset ID (for example:  `azureml://registries/azureml/models/Phi-3.5-mini-instruct/versions/4`). 

1. **Train the model:** Next, the `olive finetune` εντολή προσαρμόζει το κβαντοποιημένο μοντέλο. Η κβαντοποίηση του μοντέλου *πριν* από την προσαρμογή αντί για μετά παρέχει καλύτερη ακρίβεια, καθώς η διαδικασία προσαρμογής ανακτά μέρος της απώλειας από την κβαντοποίηση.
    
    ```bash
    olive finetune \
        --method lora \
        --model_name_or_path models/phi/awq \
        --data_files "data/data_sample_travel.jsonl" \
        --data_name "json" \
        --text_template "<|user|>\n{prompt}<|end|>\n<|assistant|>\n{response}<|end|>" \
        --max_steps 100 \
        --output_path ./models/phi/ft \
        --log_level 1
    ```
    
    Χρειάζονται περίπου **6 λεπτά** για να ολοκληρωθεί η προσαρμογή (με 100 βήματα).

1. **Βελτιστοποίηση:** Με το εκπαιδευμένο μοντέλο, τώρα βελτιστοποιείτε το μοντέλο χρησιμοποιώντας την `auto-opt` command, which will capture the ONNX graph and automatically perform a number of optimizations to improve the model performance for CPU by compressing the model and doing fusions. It should be noted, that you can also optimize for other devices such as NPU or GPU by just updating the `--device` and `--provider` παράμετρο του Olive - αλλά για τους σκοπούς αυτού του εργαστηρίου θα χρησιμοποιήσουμε CPU.

    ```bash
    olive auto-opt \
       --model_name_or_path models/phi/ft/model \
       --adapter_path models/phi/ft/adapter \
       --device cpu \
       --provider CPUExecutionProvider \
       --use_ort_genai \
       --output_path models/phi/onnx-ao \
       --log_level 1
    ```
    
    Χρειάζονται περίπου **5 λεπτά** για να ολοκληρωθεί η βελτιστοποίηση.

### Βήμα 5: Γρήγορη δοκιμή εκτέλεσης μοντέλου

Για να δοκιμάσετε την εκτέλεση του μοντέλου, δημιουργήστε ένα αρχείο Python στον φάκελό σας με το όνομα **app.py** και αντιγράψτε-επικολλήστε τον παρακάτω κώδικα:

```python
import onnxruntime_genai as og
import numpy as np

print("loading model and adapters...", end="", flush=True)
model = og.Model("models/phi/onnx-ao/model")
adapters = og.Adapters(model)
adapters.load("models/phi/onnx-ao/model/adapter_weights.onnx_adapter", "travel")
print("DONE!")

tokenizer = og.Tokenizer(model)
tokenizer_stream = tokenizer.create_stream()

params = og.GeneratorParams(model)
params.set_search_options(max_length=100, past_present_share_buffer=False)
user_input = "what is the best thing to see in chicago"
params.input_ids = tokenizer.encode(f"<|user|>\n{user_input}<|end|>\n<|assistant|>\n")

generator = og.Generator(model, params)

generator.set_active_adapter(adapters, "travel")

print(f"{user_input}")

while not generator.is_done():
    generator.compute_logits()
    generator.generate_next_token()

    new_token = generator.get_next_tokens()[0]
    print(tokenizer_stream.decode(new_token), end='', flush=True)

print("\n")
```

Εκτελέστε τον κώδικα χρησιμοποιώντας:

```bash
python app.py
```

### Βήμα 6: Ανέβασμα μοντέλου στο Azure AI

Το ανέβασμα του μοντέλου σε ένα αποθετήριο μοντέλων Azure AI καθιστά το μοντέλο διαθέσιμο για τα υπόλοιπα μέλη της ομάδας ανάπτυξης σας και επίσης διαχειρίζεται τον έλεγχο εκδόσεων του μοντέλου. Για να ανεβάσετε το μοντέλο, εκτελέστε την παρακάτω εντολή:

> [!NOTE]
> Ενημερώστε τα `{}` placeholders with the name of your resource group and Azure AI Project Name. 

To find your resource group `"resourceGroup"` και το όνομα του Azure AI Project και εκτελέστε την παρακάτω εντολή 

```
az ml workspace show
```

Ή μεταβείτε στο +++ai.azure.com+++ και επιλέξτε **management center** **project** **overview**

Ενημερώστε τα `{}` placeholders με το όνομα του resource group σας και το όνομα του Azure AI Project σας.

```bash
az ml model create \
    --name ft-for-travel \
    --version 1 \
    --path ./models/phi/onnx-ao \
    --resource-group {RESOURCE_GROUP_NAME} \
    --workspace-name {PROJECT_NAME}
```
Στη συνέχεια, μπορείτε να δείτε το ανεβασμένο μοντέλο σας και να το αναπτύξετε στη διεύθυνση https://ml.azure.com/model/list

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες μετάφρασης βασισμένες σε τεχνητή νοημοσύνη. Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για οποιαδήποτε παρερμηνεία ή παρεξήγηση που προκύπτει από τη χρήση αυτής της μετάφρασης.