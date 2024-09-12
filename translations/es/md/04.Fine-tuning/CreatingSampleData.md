# Generar Conjunto de Datos de Imágenes descargando DataSet de Hugging Face y las imágenes asociadas

### Resumen

Este script prepara un conjunto de datos para aprendizaje automático descargando las imágenes requeridas, filtrando las filas donde la descarga de imágenes falla y guardando el conjunto de datos como un archivo CSV.

### Prerrequisitos

Antes de ejecutar este script, asegúrate de tener las siguientes bibliotecas instaladas: `Pandas`, `Datasets`, `requests`, `PIL` y `io`. También necesitarás reemplazar `'Insert_Your_Dataset'` en la línea 2 con el nombre de tu conjunto de datos de Hugging Face.

Bibliotecas necesarias:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funcionalidad

El script realiza los siguientes pasos:

1. Descarga el conjunto de datos de Hugging Face usando la función `load_dataset()`.
2. Convierte el conjunto de datos de Hugging Face a un DataFrame de Pandas para una manipulación más fácil usando el método `to_pandas()`.
3. Crea directorios para guardar el conjunto de datos y las imágenes.
4. Filtra las filas donde la descarga de imágenes falla iterando a través de cada fila en el DataFrame, descargando la imagen usando la función personalizada `download_image()` y añadiendo la fila filtrada a un nuevo DataFrame llamado `filtered_rows`.
5. Crea un nuevo DataFrame con las filas filtradas y lo guarda en el disco como un archivo CSV.
6. Imprime un mensaje indicando dónde se han guardado el conjunto de datos y las imágenes.

### Función Personalizada

La función `download_image()` descarga una imagen desde una URL y la guarda localmente usando la biblioteca Pillow Image (PIL) y el módulo `io`. Devuelve True si la imagen se descarga correctamente y False en caso contrario. La función también lanza una excepción con el mensaje de error cuando la solicitud falla.

### Cómo Funciona

La función download_image toma dos parámetros: image_url, que es la URL de la imagen a descargar, y save_path, que es la ruta donde se guardará la imagen descargada.

Así es como funciona la función:

Comienza haciendo una solicitud GET a la image_url usando el método requests.get. Esto recupera los datos de la imagen desde la URL.

La línea response.raise_for_status() verifica si la solicitud fue exitosa. Si el código de estado de la respuesta indica un error (por ejemplo, 404 - No Encontrado), lanzará una excepción. Esto asegura que solo procedemos con la descarga de la imagen si la solicitud fue exitosa.

Los datos de la imagen se pasan luego al método Image.open del módulo PIL (Python Imaging Library). Este método crea un objeto Image a partir de los datos de la imagen.

La línea image.save(save_path) guarda la imagen en el save_path especificado. El save_path debe incluir el nombre de archivo y la extensión deseados.

Finalmente, la función devuelve True para indicar que la imagen se descargó y guardó correctamente. Si ocurre alguna excepción durante el proceso, captura la excepción, imprime un mensaje de error indicando la falla y devuelve False.

Esta función es útil para descargar imágenes desde URLs y guardarlas localmente. Maneja posibles errores durante el proceso de descarga y proporciona retroalimentación sobre si la descarga fue exitosa o no.

Es importante notar que la biblioteca requests se usa para hacer solicitudes HTTP, la biblioteca PIL se usa para trabajar con imágenes, y la clase BytesIO se usa para manejar los datos de la imagen como un flujo de bytes.

### Conclusión

Este script proporciona una manera conveniente de preparar un conjunto de datos para aprendizaje automático descargando las imágenes requeridas, filtrando las filas donde la descarga de imágenes falla y guardando el conjunto de datos como un archivo CSV.

### Script de Ejemplo

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

### Descargar Código de Ejemplo
[Generate a new Data Set script](../../code/04.Finetuning/generate_dataset.py)

### Conjunto de Datos de Ejemplo
[Sample Data Set example from finetuning with LORA example](../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

