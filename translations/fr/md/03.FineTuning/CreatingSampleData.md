# Générer un jeu de données d'images en téléchargeant un DataSet depuis Hugging Face et les images associées

### Aperçu

Ce script prépare un jeu de données pour l'apprentissage automatique en téléchargeant les images nécessaires, en filtrant les lignes où le téléchargement des images échoue, et en sauvegardant le jeu de données sous forme de fichier CSV.

### Prérequis

Avant d'exécuter ce script, assurez-vous d'avoir les bibliothèques suivantes installées : `Pandas`, `Datasets`, `requests`, `PIL` et `io`. Vous devrez également remplacer `'Insert_Your_Dataset'` à la ligne 2 par le nom de votre jeu de données provenant de Hugging Face.

Bibliothèques requises :

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Fonctionnalités

Le script exécute les étapes suivantes :

1. Télécharge le jeu de données depuis Hugging Face en utilisant les fonctions `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`.  
2. La fonction `download_image()` télécharge une image depuis une URL et la sauvegarde localement en utilisant la bibliothèque Pillow Image Library (PIL) et le module `io`. Elle renvoie True si l'image est téléchargée avec succès, et False dans le cas contraire. La fonction soulève également une exception avec un message d'erreur si la requête échoue.

### Comment cela fonctionne

La fonction `download_image` prend deux paramètres : `image_url`, qui correspond à l'URL de l'image à télécharger, et `save_path`, qui est le chemin où l'image téléchargée sera sauvegardée.

Voici comment la fonction fonctionne :

1. Elle commence par effectuer une requête GET à `image_url` en utilisant la méthode `requests.get`. Cela permet de récupérer les données de l'image à partir de l'URL.

2. La ligne `response.raise_for_status()` vérifie si la requête a réussi. Si le code de statut de la réponse indique une erreur (par exemple, 404 - Non trouvé), une exception sera levée. Cela garantit que nous poursuivons le téléchargement de l'image uniquement si la requête a été réussie.

3. Les données de l'image sont ensuite transmises à la méthode `Image.open` du module PIL (Python Imaging Library). Cette méthode crée un objet Image à partir des données de l'image.

4. La ligne `image.save(save_path)` sauvegarde l'image au chemin spécifié par `save_path`. Ce chemin doit inclure le nom de fichier souhaité et son extension.

5. Enfin, la fonction renvoie `True` pour indiquer que l'image a été téléchargée et sauvegardée avec succès. Si une exception survient pendant le processus, elle est interceptée, un message d'erreur est affiché pour indiquer l'échec, et la fonction renvoie `False`.

Cette fonction est utile pour télécharger des images depuis des URL et les sauvegarder localement. Elle gère les erreurs potentielles pendant le processus de téléchargement et fournit un retour sur le succès ou l'échec du téléchargement.

Il est important de noter que la bibliothèque `requests` est utilisée pour effectuer des requêtes HTTP, la bibliothèque PIL est utilisée pour travailler avec des images, et la classe `BytesIO` est utilisée pour gérer les données de l'image sous forme de flux d'octets.

### Conclusion

Ce script offre un moyen pratique de préparer un jeu de données pour l'apprentissage automatique en téléchargeant les images nécessaires, en filtrant les lignes où les téléchargements échouent, et en sauvegardant le jeu de données sous forme de fichier CSV.

### Exemple de Script

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

### Téléchargement d'un exemple de code 
[Script pour générer un nouveau jeu de données](../../../../code/04.Finetuning/generate_dataset.py)

### Exemple de Jeu de Données
[Exemple de jeu de données issu du finetuning avec LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous déclinons toute responsabilité en cas de malentendus ou de mauvaises interprétations résultant de l'utilisation de cette traduction.