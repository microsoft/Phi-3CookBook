# Gerar Conjunto de Dados de Imagens baixando o DataSet do Hugging Face e imagens associadas

### Visão Geral

Este script prepara um conjunto de dados para aprendizado de máquina baixando as imagens necessárias, filtrando as linhas onde o download das imagens falha, e salvando o conjunto de dados como um arquivo CSV.

### Pré-requisitos

Antes de executar este script, certifique-se de ter as seguintes bibliotecas instaladas: `Pandas`, `Datasets`, `requests`, `PIL` e `io`. Você também precisará substituir `'Insert_Your_Dataset'` na linha 2 pelo nome do seu conjunto de dados no Hugging Face.

Bibliotecas Necessárias:

```python

import os
import pandas as pd
from datasets import load_dataset
import requests
from PIL import Image
from io import BytesIO
```

### Funcionalidade

O script realiza os seguintes passos:

1. Baixa o conjunto de dados do Hugging Face usando `load_dataset()` function.
2. Converts the Hugging Face dataset to a Pandas DataFrame for easier manipulation using the `to_pandas()` method.
3. Creates directories to save the dataset and images.
4. Filters out rows where image download fails by iterating through each row in the DataFrame, downloading the image using the custom `download_image()` function, and appending the filtered row to a new DataFrame called `filtered_rows`.
5. Creates a new DataFrame with the filtered rows and saves it to disk as a CSV file.
6. Prints a message indicating where the dataset and images have been saved.

### Custom Function

The `download_image()`. A função `download_image()` baixa uma imagem de uma URL e a salva localmente usando a biblioteca Pillow Image Library (PIL) e o módulo `io`. Ela retorna True se a imagem for baixada com sucesso e False caso contrário. A função também levanta uma exceção com a mensagem de erro caso a solicitação falhe.

### Como funciona

A função `download_image` recebe dois parâmetros: `image_url`, que é a URL da imagem a ser baixada, e `save_path`, que é o caminho onde a imagem baixada será salva.

Veja como a função funciona:

1. Ela começa fazendo uma solicitação GET para a `image_url` usando o método `requests.get`. Isso recupera os dados da imagem da URL.

2. A linha `response.raise_for_status()` verifica se a solicitação foi bem-sucedida. Se o código de status da resposta indicar um erro (por exemplo, 404 - Não Encontrado), será levantada uma exceção. Isso garante que o download da imagem só prosseguirá se a solicitação for bem-sucedida.

3. Os dados da imagem são então passados para o método `Image.open` do módulo PIL (Python Imaging Library). Este método cria um objeto `Image` a partir dos dados da imagem.

4. A linha `image.save(save_path)` salva a imagem no `save_path` especificado. O `save_path` deve incluir o nome e a extensão desejados do arquivo.

5. Finalmente, a função retorna `True` para indicar que a imagem foi baixada e salva com sucesso. Se ocorrer qualquer exceção durante o processo, a função captura a exceção, imprime uma mensagem de erro indicando a falha e retorna `False`.

Esta função é útil para baixar imagens de URLs e salvá-las localmente. Ela lida com possíveis erros durante o processo de download e fornece um feedback sobre o sucesso ou falha do download.

Vale destacar que a biblioteca `requests` é usada para fazer solicitações HTTP, a biblioteca PIL é usada para trabalhar com imagens, e a classe `BytesIO` é utilizada para manipular os dados da imagem como um fluxo de bytes.

### Conclusão

Este script fornece uma maneira prática de preparar um conjunto de dados para aprendizado de máquina, baixando as imagens necessárias, filtrando as linhas onde os downloads falham e salvando o conjunto de dados como um arquivo CSV.

### Script de Exemplo

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

### Código para Download 
[Script para gerar um novo conjunto de dados](../../../../code/04.Finetuning/generate_dataset.py)

### Conjunto de Dados de Exemplo
[Exemplo de conjunto de dados usado no fine-tuning com LORA](../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json)

**Aviso Legal**:  
Este documento foi traduzido utilizando serviços de tradução baseados em IA. Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autoritativa. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.