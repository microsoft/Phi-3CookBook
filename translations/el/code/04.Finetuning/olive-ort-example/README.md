# Προσαρμογή του Phi3 με το Olive

Σε αυτό το παράδειγμα θα χρησιμοποιήσετε το Olive για να:

1. Προσαρμόσετε έναν LoRA adapter ώστε να ταξινομεί φράσεις σε Sad, Joy, Fear, Surprise.
1. Συγχωνεύσετε τα βάρη του adapter με το βασικό μοντέλο.
1. Βελτιστοποιήσετε και ποσοτικοποιήσετε το μοντέλο σε `int4`.

Θα σας δείξουμε επίσης πώς να κάνετε inference στο προσαρμοσμένο μοντέλο χρησιμοποιώντας το ONNX Runtime (ORT) Generate API.

> **⚠️ Για την προσαρμογή, θα χρειαστείτε μια κατάλληλη GPU - για παράδειγμα, A10, V100, A100.**

## 💾 Εγκατάσταση

Δημιουργήστε ένα νέο Python virtual environment (για παράδειγμα, χρησιμοποιώντας `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Στη συνέχεια, εγκαταστήστε το Olive και τις εξαρτήσεις για τη ροή εργασιών προσαρμογής:

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Προσαρμογή του Phi3 με το Olive
Το [Olive configuration file](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) περιέχει μια *ροή εργασιών* με τα εξής *βήματα*:

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

Σε υψηλό επίπεδο, αυτή η ροή εργασιών θα:

1. Προσαρμόσει το Phi3 (για 150 βήματα, τα οποία μπορείτε να τροποποιήσετε) χρησιμοποιώντας τα δεδομένα από το [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Συγχωνεύσει τα βάρη του LoRA adapter με το βασικό μοντέλο. Αυτό θα σας δώσει ένα μόνο μοντέλο σε ONNX format.
1. Το Model Builder θα βελτιστοποιήσει το μοντέλο για το ONNX runtime *και* θα το ποσοτικοποιήσει σε `int4`.

Για να εκτελέσετε τη ροή εργασιών, τρέξτε:

```bash
olive run --config phrase-classification.json
```

Όταν το Olive ολοκληρώσει, το βελτιστοποιημένο `int4` προσαρμοσμένο μοντέλο Phi3 θα είναι διαθέσιμο στο: `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Ενσωμάτωση του προσαρμοσμένου Phi3 στην εφαρμογή σας 

Για να εκτελέσετε την εφαρμογή:

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Η απόκριση θα πρέπει να είναι μια μονολεκτική ταξινόμηση της φράσης (Sad/Joy/Fear/Surprise).

**Αποποίηση ευθυνών**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες μετάφρασης που βασίζονται σε τεχνητή νοημοσύνη. Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.