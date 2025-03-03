# **Ποσοτικοποίηση της Οικογένειας Phi χρησιμοποιώντας τις Επεκτάσεις Γενετικής Τεχνητής Νοημοσύνης για το onnxruntime**

## **Τι είναι οι Επεκτάσεις Γενετικής Τεχνητής Νοημοσύνης για το onnxruntime**

Αυτές οι επεκτάσεις σας βοηθούν να εκτελέσετε γενετική τεχνητή νοημοσύνη με το ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Παρέχουν τον βρόχο γενετικής τεχνητής νοημοσύνης για μοντέλα ONNX, περιλαμβάνοντας την εκτέλεση με το ONNX Runtime, την επεξεργασία των logits, την αναζήτηση και δειγματοληψία, καθώς και τη διαχείριση της προσωρινής μνήμης KV. Οι προγραμματιστές μπορούν να καλέσουν τη μέθοδο υψηλού επιπέδου generate() ή να εκτελέσουν κάθε επανάληψη του μοντέλου σε έναν βρόχο, δημιουργώντας ένα σύμβολο κάθε φορά και προαιρετικά να ενημερώσουν τις παραμέτρους δημιουργίας μέσα στον βρόχο. Υποστηρίζει αναζήτηση greedy/beam και δειγματοληψία TopP, TopK για τη δημιουργία ακολουθιών συμβόλων, καθώς και ενσωματωμένη επεξεργασία logits όπως ποινές επανάληψης. Μπορείτε επίσης εύκολα να προσθέσετε προσαρμοσμένη βαθμολόγηση.

Σε επίπεδο εφαρμογής, μπορείτε να χρησιμοποιήσετε τις Επεκτάσεις Γενετικής Τεχνητής Νοημοσύνης για το onnxruntime για να δημιουργήσετε εφαρμογές χρησιμοποιώντας C++/C#/Python. Σε επίπεδο μοντέλου, μπορείτε να το χρησιμοποιήσετε για να συγχωνεύσετε μοντέλα που έχουν βελτιστοποιηθεί και να εκτελέσετε σχετικές εργασίες ποσοτικής ανάπτυξης.

## **Ποσοτικοποίηση του Phi-3.5 με τις Επεκτάσεις Γενετικής Τεχνητής Νοημοσύνης για το onnxruntime**

### **Υποστηριζόμενα Μοντέλα**

Οι Επεκτάσεις Γενετικής Τεχνητής Νοημοσύνης για το onnxruntime υποστηρίζουν τη μετατροπή ποσοτικοποίησης των Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.

### **Δημιουργός Μοντέλων στις Επεκτάσεις Γενετικής Τεχνητής Νοημοσύνης για το onnxruntime**

Ο Δημιουργός Μοντέλων επιταχύνει σημαντικά τη δημιουργία βελτιστοποιημένων και ποσοτικοποιημένων μοντέλων ONNX που εκτελούνται με το API generate() του ONNX Runtime.

Μέσω του Δημιουργού Μοντέλων, μπορείτε να ποσοτικοποιήσετε το μοντέλο σε INT4, INT8, FP16, FP32 και να συνδυάσετε διαφορετικές μεθόδους επιτάχυνσης υλικού, όπως CPU, CUDA, DirectML, Mobile, κ.λπ.

Για να χρησιμοποιήσετε τον Δημιουργό Μοντέλων, πρέπει να εγκαταστήσετε

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Μετά την εγκατάσταση, μπορείτε να εκτελέσετε το script του Δημιουργού Μοντέλων από το τερματικό για να πραγματοποιήσετε μετατροπή μορφής και ποσοτικοποίησης μοντέλου.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Κατανόηση των σχετικών παραμέτρων:

1. **model_name** Αυτό είναι το μοντέλο στο Hugging Face, όπως το microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, κ.λπ. Μπορεί επίσης να είναι το μονοπάτι όπου αποθηκεύετε το μοντέλο.

2. **path_to_output_folder** Διαδρομή αποθήκευσης της ποσοτικοποιημένης μετατροπής.

3. **execution_provider** Υποστήριξη διαφορετικής επιτάχυνσης υλικού, όπως cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Κατεβάζουμε το μοντέλο από το Hugging Face και το αποθηκεύουμε προσωρινά τοπικά.

***Σημείωση:***

## **Πώς να χρησιμοποιήσετε τον Δημιουργό Μοντέλων για την ποσοτικοποίηση του Phi-3.5**

Ο Δημιουργός Μοντέλων υποστηρίζει πλέον την ποσοτικοποίηση μοντέλων ONNX για το Phi-3.5 Instruct και το Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**Μετατροπή σε INT4 με επιτάχυνση CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Μετατροπή σε INT4 με επιτάχυνση CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Ρύθμιση περιβάλλοντος στο τερματικό

```bash

mkdir models

cd models 

```

2. Κατεβάστε το microsoft/Phi-3.5-vision-instruct στον φάκελο models  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Παρακαλώ κατεβάστε αυτά τα αρχεία στον φάκελο Phi-3.5-vision-instruct σας:

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Κατεβάστε αυτό το αρχείο στον φάκελο models  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Μεταβείτε στο τερματικό

    Μετατροπή υποστήριξης ONNX με FP32

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Σημείωση:**

1. Ο Δημιουργός Μοντέλων υποστηρίζει προς το παρόν τη μετατροπή των Phi-3.5-Instruct και Phi-3.5-Vision, αλλά όχι του Phi-3.5-MoE.

2. Για να χρησιμοποιήσετε το ποσοτικοποιημένο μοντέλο ONNX, μπορείτε να το χρησιμοποιήσετε μέσω του SDK των Επεκτάσεων Γενετικής Τεχνητής Νοημοσύνης για το onnxruntime.

3. Πρέπει να λάβουμε υπόψη πιο υπεύθυνη τεχνητή νοημοσύνη, επομένως, μετά τη μετατροπή ποσοτικοποίησης του μοντέλου, συνιστάται να διεξαχθούν πιο αποτελεσματικές δοκιμές αποτελεσμάτων.

4. Με την ποσοτικοποίηση του μοντέλου CPU INT4, μπορούμε να το αναπτύξουμε σε συσκευές Edge, που έχουν καλύτερα σενάρια εφαρμογής. Έτσι, ολοκληρώσαμε το Phi-3.5-Instruct γύρω από το INT4.

## **Πόροι**

1. Μάθετε περισσότερα για τις Επεκτάσεις Γενετικής Τεχνητής Νοημοσύνης για το onnxruntime  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Αποθετήριο GitHub για τις Επεκτάσεις Γενετικής Τεχνητής Νοημοσύνης για το onnxruntime  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες αυτόματης μετάφρασης με τεχνητή νοημοσύνη. Ενώ καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να γνωρίζετε ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το πρωτότυπο έγγραφο στη γλώσσα του θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική μετάφραση από άνθρωπο. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.