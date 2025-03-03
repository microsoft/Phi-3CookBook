# Erstellen eines Bilddatensatzes durch Herunterladen eines Datensatzes von Hugging Face und zugehörigen Bildern

### Übersicht

Dieses Skript bereitet einen Datensatz für maschinelles Lernen vor, indem es die benötigten Bilder herunterlädt, Zeilen filtert, bei denen das Herunterladen der Bilder fehlschlägt, und den Datensatz als CSV-Datei speichert.

### Voraussetzungen

Bevor Sie dieses Skript ausführen, stellen Sie sicher, dass die folgenden Bibliotheken installiert sind: `Pandas`, `Datasets`, `requests`, `PIL` und `io`. Außerdem müssen Sie `'Insert_Your_Dataset'` in Zeile 2 durch den Namen Ihres Datensatzes von Hugging Face ersetzen.

Benötigte Bibliotheken:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funktionalität

Das Skript führt die folgenden Schritte aus:

1. Es lädt den Datensatz von Hugging Face herunter, indem es die Funktionen `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()` verwendet. Die Funktion `download_image()` lädt ein Bild von einer URL herunter und speichert es lokal mithilfe der Pillow Image Library (PIL) und des Moduls `io`. Sie gibt True zurück, wenn das Bild erfolgreich heruntergeladen wurde, und False, wenn nicht. Die Funktion löst außerdem eine Ausnahme mit der Fehlermeldung aus, wenn die Anfrage fehlschlägt.

### Wie funktioniert das?

Die Funktion `download_image` nimmt zwei Parameter entgegen: `image_url`, die URL des herunterzuladenden Bildes, und `save_path`, den Pfad, an dem das heruntergeladene Bild gespeichert werden soll.

So funktioniert die Funktion:

1. Sie startet mit einer GET-Anfrage an die `image_url` mithilfe der Methode `requests.get`. Dadurch werden die Bilddaten von der URL abgerufen.

2. Die Zeile `response.raise_for_status()` prüft, ob die Anfrage erfolgreich war. Wenn der Statuscode der Antwort auf einen Fehler hinweist (z. B. 404 - Nicht gefunden), wird eine Ausnahme ausgelöst. Dies stellt sicher, dass der Download nur fortgesetzt wird, wenn die Anfrage erfolgreich war.

3. Die Bilddaten werden dann an die Methode `Image.open` aus dem Modul PIL (Python Imaging Library) übergeben. Diese Methode erstellt ein `Image`-Objekt aus den Bilddaten.

4. Die Zeile `image.save(save_path)` speichert das Bild im angegebenen `save_path`. Der `save_path` sollte den gewünschten Dateinamen und die Erweiterung enthalten.

5. Schließlich gibt die Funktion `True` zurück, um anzuzeigen, dass das Bild erfolgreich heruntergeladen und gespeichert wurde. Wenn während des Prozesses eine Ausnahme auftritt, fängt die Funktion die Ausnahme ab, gibt eine Fehlermeldung aus und gibt `False` zurück.

Diese Funktion ist nützlich, um Bilder von URLs herunterzuladen und lokal zu speichern. Sie behandelt potenzielle Fehler während des Downloadprozesses und gibt Feedback, ob der Download erfolgreich war oder nicht.

Es ist erwähnenswert, dass die Bibliothek `requests` für HTTP-Anfragen verwendet wird, die Bibliothek PIL für die Arbeit mit Bildern und die Klasse `BytesIO`, um die Bilddaten als Byte-Stream zu verarbeiten.

### Fazit

Dieses Skript bietet eine praktische Möglichkeit, einen Datensatz für maschinelles Lernen vorzubereiten, indem die benötigten Bilder heruntergeladen, Zeilen gefiltert werden, bei denen das Herunterladen der Bilder fehlschlägt, und der Datensatz als CSV-Datei gespeichert wird.

### Beispielskript

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

### Beispiel-Code herunterladen 
[Neues Datensatz-Skript generieren](../../../../code/04.Finetuning/generate_dataset.py)

### Beispiel-Datensatz
[Beispiel-Datensatz aus dem Finetuning mit LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Haftungsausschluss**:  
Dieses Dokument wurde mit KI-basierten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.