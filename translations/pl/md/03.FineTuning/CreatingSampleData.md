# Generowanie zestawu danych obrazów poprzez pobranie zestawu danych z Hugging Face i powiązanych obrazów

### Przegląd

Ten skrypt przygotowuje zestaw danych do uczenia maszynowego poprzez pobranie wymaganych obrazów, odfiltrowanie wierszy, w których pobranie obrazów się nie powiodło, oraz zapisanie zestawu danych w formacie CSV.

### Wymagania wstępne

Przed uruchomieniem tego skryptu upewnij się, że masz zainstalowane następujące biblioteki: `Pandas`, `Datasets`, `requests`, `PIL` i `io`. Musisz także zastąpić `'Insert_Your_Dataset'` w linii 2 nazwą swojego zestawu danych z Hugging Face.

Wymagane biblioteki:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funkcjonalność

Skrypt wykonuje następujące kroki:

1. Pobiera zestaw danych z Hugging Face za pomocą funkcji `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`. Funkcja `download_image()` pobiera obraz z adresu URL i zapisuje go lokalnie za pomocą biblioteki Pillow Image Library (PIL) oraz modułu `io`. Zwraca wartość True, jeśli obraz został pomyślnie pobrany, a False w przeciwnym razie. Funkcja również zgłasza wyjątek z komunikatem o błędzie, gdy żądanie się nie powiedzie.

### Jak to działa

Funkcja `download_image` przyjmuje dwa parametry: `image_url`, czyli adres URL obrazu do pobrania, oraz `save_path`, czyli ścieżkę, w której pobrany obraz zostanie zapisany.

Oto jak działa funkcja:

1. Funkcja rozpoczyna od wykonania żądania GET do `image_url` za pomocą metody `requests.get`. Pobiera to dane obrazu z podanego adresu URL.

2. Linia `response.raise_for_status()` sprawdza, czy żądanie zakończyło się sukcesem. Jeśli kod statusu odpowiedzi wskazuje na błąd (np. 404 - Nie znaleziono), zostanie zgłoszony wyjątek. Dzięki temu kontynuujemy pobieranie obrazu tylko wtedy, gdy żądanie zakończyło się sukcesem.

3. Dane obrazu są następnie przekazywane do metody `Image.open` z modułu PIL (Python Imaging Library). Ta metoda tworzy obiekt obrazu na podstawie danych obrazu.

4. Linia `image.save(save_path)` zapisuje obraz w określonej ścieżce `save_path`. Ścieżka ta powinna zawierać pożądany nazwę pliku i rozszerzenie.

5. Na końcu funkcja zwraca wartość True, aby wskazać, że obraz został pomyślnie pobrany i zapisany. Jeśli w trakcie procesu wystąpi jakikolwiek wyjątek, funkcja przechwytuje wyjątek, wyświetla komunikat o błędzie wskazujący na niepowodzenie i zwraca False.

Ta funkcja jest przydatna do pobierania obrazów z adresów URL i zapisywania ich lokalnie. Obsługuje potencjalne błędy podczas procesu pobierania i dostarcza informacji zwrotnej, czy pobieranie zakończyło się sukcesem.

Warto zauważyć, że biblioteka `requests` jest używana do wykonywania żądań HTTP, biblioteka `PIL` jest używana do pracy z obrazami, a klasa `BytesIO` służy do obsługi danych obrazu jako strumienia bajtów.

### Podsumowanie

Ten skrypt zapewnia wygodny sposób przygotowania zestawu danych do uczenia maszynowego poprzez pobieranie wymaganych obrazów, odfiltrowanie wierszy, w których pobieranie obrazów się nie powiodło, oraz zapisanie zestawu danych w formacie CSV.

### Przykładowy skrypt

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

### Pobieranie przykładowego kodu
[Wygeneruj nowy skrypt zestawu danych](../../../../code/04.Finetuning/generate_dataset.py)

### Przykładowy zestaw danych
[Przykładowy zestaw danych z fine-tuningu przy użyciu LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Zastrzeżenie**:  
Ten dokument został przetłumaczony przy użyciu usług tłumaczenia maszynowego opartego na sztucznej inteligencji. Chociaż staramy się zapewnić dokładność, prosimy mieć na uwadze, że automatyczne tłumaczenia mogą zawierać błędy lub nieścisłości. Oryginalny dokument w jego rodzimym języku powinien być uznawany za wiarygodne źródło. W przypadku kluczowych informacji zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za jakiekolwiek nieporozumienia lub błędne interpretacje wynikające z użycia tego tłumaczenia.