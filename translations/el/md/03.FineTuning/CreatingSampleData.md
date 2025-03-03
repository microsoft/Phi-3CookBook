# Δημιουργία Συνόλου Δεδομένων Εικόνων με Λήψη Δεδομένων από το Hugging Face και Σχετικών Εικόνων

### Επισκόπηση

Αυτό το script προετοιμάζει ένα σύνολο δεδομένων για μηχανική μάθηση κατεβάζοντας τις απαραίτητες εικόνες, φιλτράροντας γραμμές όπου η λήψη εικόνων αποτυγχάνει, και αποθηκεύοντας το σύνολο δεδομένων σε αρχείο CSV.

### Προαπαιτούμενα

Πριν εκτελέσετε αυτό το script, βεβαιωθείτε ότι έχετε εγκαταστήσει τις ακόλουθες βιβλιοθήκες: `Pandas`, `Datasets`, `requests`, `PIL` και `io`. Θα χρειαστεί επίσης να αντικαταστήσετε το `'Insert_Your_Dataset'` στη γραμμή 2 με το όνομα του συνόλου δεδομένων σας από το Hugging Face.

Απαραίτητες Βιβλιοθήκες:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Λειτουργικότητα

Το script εκτελεί τα παρακάτω βήματα:

1. Κατεβάζει το σύνολο δεδομένων από το Hugging Face χρησιμοποιώντας τη μέθοδο `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`. Η συνάρτηση `download_image()` κατεβάζει μια εικόνα από ένα URL και την αποθηκεύει τοπικά χρησιμοποιώντας τη βιβλιοθήκη Pillow Image Library (PIL) και τη `io`. Επιστρέφει True αν η εικόνα κατέβηκε με επιτυχία, και False διαφορετικά. Η συνάρτηση επίσης εγείρει εξαίρεση με το μήνυμα σφάλματος όταν η αίτηση αποτυγχάνει.

### Πώς λειτουργεί

Η συνάρτηση `download_image` δέχεται δύο παραμέτρους: το `image_url`, που είναι το URL της εικόνας που θα κατέβει, και το `save_path`, που είναι η διαδρομή όπου θα αποθηκευτεί η εικόνα.

Πώς λειτουργεί η συνάρτηση:

- Ξεκινά κάνοντας ένα αίτημα GET στο `image_url` χρησιμοποιώντας τη μέθοδο `requests.get`. Αυτό ανακτά τα δεδομένα της εικόνας από το URL.

- Η γραμμή `response.raise_for_status()` ελέγχει αν το αίτημα ήταν επιτυχές. Αν ο κωδικός κατάστασης της απόκρισης δείχνει σφάλμα (π.χ. 404 - Δεν βρέθηκε), εγείρεται εξαίρεση. Αυτό διασφαλίζει ότι προχωράμε στη λήψη της εικόνας μόνο αν το αίτημα ήταν επιτυχές.

- Τα δεδομένα της εικόνας περνούν στη μέθοδο `Image.open` από το PIL (Python Imaging Library). Αυτή η μέθοδος δημιουργεί ένα αντικείμενο εικόνας από τα δεδομένα.

- Η γραμμή `image.save(save_path)` αποθηκεύει την εικόνα στη συγκεκριμένη διαδρομή `save_path`. Το `save_path` πρέπει να περιλαμβάνει το επιθυμητό όνομα αρχείου και την επέκταση.

- Τέλος, η συνάρτηση επιστρέφει True για να υποδείξει ότι η εικόνα κατέβηκε και αποθηκεύτηκε επιτυχώς. Αν προκύψει οποιαδήποτε εξαίρεση κατά τη διαδικασία, την πιάνει, εκτυπώνει ένα μήνυμα σφάλματος που υποδεικνύει την αποτυχία, και επιστρέφει False.

Αυτή η συνάρτηση είναι χρήσιμη για τη λήψη εικόνων από URLs και την τοπική αποθήκευσή τους. Διαχειρίζεται πιθανά σφάλματα κατά τη διαδικασία λήψης και παρέχει πληροφορίες για το αν η λήψη ήταν επιτυχής ή όχι.

Σημειώνεται ότι η βιβλιοθήκη `requests` χρησιμοποιείται για την εκτέλεση HTTP αιτημάτων, η βιβλιοθήκη PIL για την επεξεργασία εικόνων, και η κλάση `BytesIO` για τη διαχείριση των δεδομένων της εικόνας ως ροή byte.

### Συμπέρασμα

Αυτό το script παρέχει έναν εύχρηστο τρόπο προετοιμασίας ενός συνόλου δεδομένων για μηχανική μάθηση κατεβάζοντας τις απαραίτητες εικόνες, φιλτράροντας γραμμές όπου η λήψη εικόνων αποτυγχάνει, και αποθηκεύοντας το σύνολο δεδομένων σε αρχείο CSV.

### Δείγμα Script

```python
import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO

def download_image(image_url, save_path):
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Check if the request was successful
        image = Image.open(BytesIO(response.content))
        image.save(save_path)
        return True
    except Exception as e:
        print(f"Failed to download {image_url}: {e}")
        return False


# Download the dataset from Hugging Face
dataset = load_dataset('Insert_Your_Dataset')


# Convert the Hugging Face dataset to a Pandas DataFrame
df = dataset['train'].to_pandas()


# Create directories to save the dataset and images
dataset_dir = './data/DataSetName'
images_dir = os.path.join(dataset_dir, 'images')
os.makedirs(images_dir, exist_ok=True)


# Filter out rows where image download fails
filtered_rows = []
for idx, row in df.iterrows():
    image_url = row['imageurl']
    image_name = f"{row['product_code']}.jpg"
    image_path = os.path.join(images_dir, image_name)
    if download_image(image_url, image_path):
        row['local_image_path'] = image_path
        filtered_rows.append(row)


# Create a new DataFrame with the filtered rows
filtered_df = pd.DataFrame(filtered_rows)


# Save the updated dataset to disk
dataset_path = os.path.join(dataset_dir, 'Dataset.csv')
filtered_df.to_csv(dataset_path, index=False)


print(f"Dataset and images saved to {dataset_dir}")
```

### Δείγμα Κώδικα Λήψης
[Script Δημιουργίας Νέου Συνόλου Δεδομένων](../../../../code/04.Finetuning/generate_dataset.py)

### Δείγμα Συνόλου Δεδομένων
[Παράδειγμα Συνόλου Δεδομένων από την Εκπαίδευση με LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες αυτόματης μετάφρασης με τεχνητή νοημοσύνη. Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το αρχικό έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η έγκυρη πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή παρερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.