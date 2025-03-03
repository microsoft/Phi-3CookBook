# Genera un DataSet di immagini scaricando il DataSet da Hugging Face e le immagini associate

### Panoramica

Questo script prepara un dataset per il machine learning scaricando le immagini necessarie, filtrando le righe in cui il download delle immagini fallisce e salvando il dataset come file CSV.

### Prerequisiti

Prima di eseguire questo script, assicurati di avere installato le seguenti librerie: `Pandas`, `Datasets`, `requests`, `PIL` e `io`. Inoltre, sarà necessario sostituire `'Insert_Your_Dataset'` nella riga 2 con il nome del tuo dataset su Hugging Face.

Librerie necessarie:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funzionalità

Lo script esegue i seguenti passaggi:

1. Scarica il dataset da Hugging Face utilizzando `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`.  
2. Filtra le righe del dataset in cui il download delle immagini fallisce.  
3. Salva il dataset filtrato come file CSV.  

La funzione `download_image()` scarica un'immagine da un URL e la salva localmente utilizzando la libreria Pillow Image Library (PIL) e il modulo `io`. Restituisce True se l'immagine viene scaricata con successo e False in caso contrario. La funzione solleva anche un'eccezione con il messaggio di errore se la richiesta fallisce.

### Come funziona

La funzione `download_image` accetta due parametri: `image_url`, che è l'URL dell'immagine da scaricare, e `save_path`, che è il percorso in cui verrà salvata l'immagine scaricata.

Ecco come funziona la funzione:

1. Inizia effettuando una richiesta GET all'`image_url` utilizzando il metodo `requests.get`. Questo recupera i dati dell'immagine dall'URL.  
2. La riga `response.raise_for_status()` verifica se la richiesta è stata eseguita con successo. Se il codice di stato della risposta indica un errore (ad esempio, 404 - Non Trovato), verrà sollevata un'eccezione. Questo garantisce che si proceda con il download dell'immagine solo se la richiesta ha avuto successo.  
3. I dati dell'immagine vengono quindi passati al metodo `Image.open` del modulo PIL (Python Imaging Library). Questo metodo crea un oggetto `Image` a partire dai dati dell'immagine.  
4. La riga `image.save(save_path)` salva l'immagine nel percorso specificato (`save_path`). Il percorso deve includere il nome del file desiderato e l'estensione.  
5. Infine, la funzione restituisce `True` per indicare che l'immagine è stata scaricata e salvata con successo. Se si verifica un'eccezione durante il processo, questa viene catturata, viene stampato un messaggio di errore che indica il fallimento, e viene restituito `False`.

Questa funzione è utile per scaricare immagini da URL e salvarle localmente. Gestisce eventuali errori durante il processo di download e fornisce un feedback sull'esito del download.

Vale la pena notare che la libreria `requests` viene utilizzata per effettuare richieste HTTP, la libreria PIL viene utilizzata per lavorare con le immagini, e la classe `BytesIO` viene utilizzata per gestire i dati dell'immagine come un flusso di byte.

### Conclusione

Questo script offre un modo conveniente per preparare un dataset per il machine learning scaricando le immagini necessarie, filtrando le righe in cui il download delle immagini fallisce e salvando il dataset come file CSV.

### Script di esempio

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

### Download del codice di esempio 
[Genera uno script per un nuovo Data Set](../../../../code/04.Finetuning/generate_dataset.py)

### Data Set di esempio
[Esempio di Data Set per il fine-tuning con LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Disclaimer (Dichiarazione di esclusione di responsabilità):**  
Questo documento è stato tradotto utilizzando servizi di traduzione basati su intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di tenere presente che le traduzioni automatiche possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre deve essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali fraintendimenti o interpretazioni errate derivanti dall'uso di questa traduzione.