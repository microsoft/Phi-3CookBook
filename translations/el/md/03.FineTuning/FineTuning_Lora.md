# **Προσαρμογή του Phi-3 με Lora**

Προσαρμογή του γλωσσικού μοντέλου Phi-3 Mini της Microsoft χρησιμοποιώντας [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) σε ένα προσαρμοσμένο σύνολο δεδομένων συνομιλιακών οδηγιών.

Το LoRA θα βοηθήσει στη βελτίωση της κατανόησης συνομιλιών και της δημιουργίας απαντήσεων.

## Οδηγός βήμα προς βήμα για την προσαρμογή του Phi-3 Mini:

**Εισαγωγές και Ρύθμιση**

Εγκατάσταση του loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Ξεκινήστε εισάγοντας τις απαραίτητες βιβλιοθήκες, όπως datasets, transformers, peft, trl και torch. 
Ρυθμίστε το logging για την παρακολούθηση της διαδικασίας εκπαίδευσης.

Μπορείτε να επιλέξετε να προσαρμόσετε ορισμένα επίπεδα αντικαθιστώντας τα με αντίστοιχα που υλοποιούνται στο loralib. Υποστηρίζουμε μόνο nn.Linear, nn.Embedding και nn.Conv2d προς το παρόν. Υποστηρίζουμε επίσης ένα MergedLinear για περιπτώσεις όπου ένα μόνο nn.Linear αντιπροσωπεύει περισσότερα από ένα επίπεδα, όπως σε ορισμένες υλοποιήσεις της προβολής qkv της προσοχής (δείτε τις Πρόσθετες Σημειώσεις για περισσότερα).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

Πριν ξεκινήσει ο βρόχος εκπαίδευσης, σημειώστε μόνο τις παραμέτρους του LoRA ως εκπαιδεύσιμες.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Κατά την αποθήκευση ενός checkpoint, δημιουργήστε ένα state_dict που περιέχει μόνο τις παραμέτρους του LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Κατά τη φόρτωση ενός checkpoint χρησιμοποιώντας το load_state_dict, βεβαιωθείτε ότι έχετε ορίσει strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

Τώρα η εκπαίδευση μπορεί να συνεχιστεί κανονικά.

**Υπερπαράμετροι**

Ορίστε δύο λεξικά: training_config και peft_config. Το training_config περιλαμβάνει υπερπαραμέτρους για την εκπαίδευση, όπως learning rate, μέγεθος παρτίδας και ρυθμίσεις καταγραφής.

Το peft_config καθορίζει παραμέτρους που σχετίζονται με το LoRA, όπως rank, dropout και τύπο εργασίας.

**Φόρτωση Μοντέλου και Tokenizer**

Καθορίστε τη διαδρομή προς το προεκπαιδευμένο μοντέλο Phi-3 (π.χ., "microsoft/Phi-3-mini-4k-instruct"). Διαμορφώστε τις ρυθμίσεις του μοντέλου, συμπεριλαμβανομένης της χρήσης cache, του τύπου δεδομένων (bfloat16 για μικτή ακρίβεια) και της υλοποίησης προσοχής.

**Εκπαίδευση**

Προσαρμόστε το μοντέλο Phi-3 χρησιμοποιώντας το προσαρμοσμένο σύνολο δεδομένων συνομιλιακών οδηγιών. Αξιοποιήστε τις ρυθμίσεις LoRA από το peft_config για αποδοτική προσαρμογή. Παρακολουθήστε την πρόοδο της εκπαίδευσης χρησιμοποιώντας τη συγκεκριμένη στρατηγική καταγραφής.

Αξιολόγηση και Αποθήκευση: Αξιολογήστε το προσαρμοσμένο μοντέλο.
Αποθηκεύστε checkpoints κατά τη διάρκεια της εκπαίδευσης για μελλοντική χρήση.

**Παραδείγματα**
- [Μάθετε περισσότερα με αυτό το notebook](../../../../code/03.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Παράδειγμα Python FineTuning Sample](../../../../code/03.Finetuning/FineTrainingScript.py)
- [Παράδειγμα Fine Tuning στο Hugging Face Hub με LORA](../../../../code/03.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Παράδειγμα Hugging Face Model Card - LORA Fine Tuning Sample](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Παράδειγμα Fine Tuning στο Hugging Face Hub με QLORA](../../../../code/03.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες μηχανικής μετάφρασης με τεχνητή νοημοσύνη. Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη σας ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν σφάλματα ή ανακρίβειες. Το πρωτότυπο έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.