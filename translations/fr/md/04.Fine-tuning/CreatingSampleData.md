# Générer un Jeu de Données d'Images en téléchargeant le Jeu de Données depuis Hugging Face et les images associées

### Vue d'ensemble

Ce script prépare un jeu de données pour l'apprentissage automatique en téléchargeant les images nécessaires, en filtrant les lignes où le téléchargement des images échoue, et en sauvegardant le jeu de données sous forme de fichier CSV.

### Prérequis

Avant d'exécuter ce script, assurez-vous d'avoir les bibliothèques suivantes installées : `Pandas`, `Datasets`, `requests`, `PIL`, et `io`. Vous devrez également remplacer `'Insert_Your_Dataset'` à la ligne 2 par le nom de votre jeu de données depuis Hugging Face.

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

Le script effectue les étapes suivantes :

1. Télécharge le jeu de données depuis Hugging Face en utilisant la fonction `load_dataset()`.
2. Convertit le jeu de données Hugging Face en un DataFrame Pandas pour une manipulation plus facile en utilisant la méthode `to_pandas()`.
3. Crée des répertoires pour sauvegarder le jeu de données et les images.
4. Filtre les lignes où le téléchargement des images échoue en itérant à travers chaque ligne du DataFrame, télécharge l'image en utilisant la fonction personnalisée `download_image()`, et ajoute la ligne filtrée à un nouveau DataFrame appelé `filtered_rows`.
5. Crée un nouveau DataFrame avec les lignes filtrées et le sauvegarde sur le disque sous forme de fichier CSV.
6. Affiche un message indiquant où le jeu de données et les images ont été sauvegardés.

### Fonction Personnalisée

La fonction `download_image()` télécharge une image à partir d'une URL et la sauvegarde localement en utilisant la bibliothèque Pillow Image (PIL) et le module `io`. Elle renvoie True si l'image est téléchargée avec succès, et False sinon. La fonction lève également une exception avec le message d'erreur lorsque la requête échoue.

### Comment cela fonctionne

La fonction download_image prend deux paramètres : image_url, qui est l'URL de l'image à télécharger, et save_path, qui est le chemin où l'image téléchargée sera sauvegardée.

Voici comment la fonction fonctionne :

Elle commence par faire une requête GET à image_url en utilisant la méthode requests.get. Cela récupère les données de l'image depuis l'URL.

La ligne response.raise_for_status() vérifie si la requête a réussi. Si le code de statut de la réponse indique une erreur (par exemple, 404 - Non Trouvé), elle lèvera une exception. Cela garantit que nous ne procédons au téléchargement de l'image que si la requête a réussi.

Les données de l'image sont ensuite passées à la méthode Image.open du module PIL (Python Imaging Library). Cette méthode crée un objet Image à partir des données de l'image.

La ligne image.save(save_path) sauvegarde l'image au chemin spécifié save_path. Le save_path doit inclure le nom de fichier et l'extension souhaités.

Enfin, la fonction renvoie True pour indiquer que l'image a été téléchargée et sauvegardée avec succès. Si une exception se produit pendant le processus, elle attrape l'exception, affiche un message d'erreur indiquant l'échec, et renvoie False.

Cette fonction est utile pour télécharger des images à partir d'URLs et les sauvegarder localement. Elle gère les erreurs potentielles pendant le processus de téléchargement et fournit un retour d'information sur le succès ou l'échec du téléchargement.

Il est à noter que la bibliothèque requests est utilisée pour faire des requêtes HTTP, la bibliothèque PIL est utilisée pour travailler avec les images, et la classe BytesIO est utilisée pour gérer les données de l'image comme un flux d'octets.

### Conclusion

Ce script fournit un moyen pratique de préparer un jeu de données pour l'apprentissage automatique en téléchargeant les images nécessaires, en filtrant les lignes où le téléchargement des images échoue, et en sauvegardant le jeu de données sous forme de fichier CSV.

### Script Exemple

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

### Télécharger le Code Exemple
[Script pour Générer un Nouveau Jeu de Données](../../../../code/04.Finetuning/generate_dataset.py)

### Exemple de Jeu de Données
[Exemple de Jeu de Données pour le finetuning avec LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

Avertissement : La traduction a été effectuée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez examiner le résultat et apporter les corrections nécessaires.