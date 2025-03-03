# **Quantification de la famille Phi à l'aide des extensions d'IA générative pour onnxruntime**

## **Qu'est-ce que les extensions d'IA générative pour onnxruntime**

Ces extensions vous permettent d'exécuter des modèles d'IA générative avec ONNX Runtime ([https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)). Elles fournissent une boucle d'IA générative pour les modèles ONNX, incluant l'inférence avec ONNX Runtime, le traitement des logits, la recherche et l'échantillonnage, ainsi que la gestion du cache KV. Les développeurs peuvent appeler une méthode de haut niveau generate(), ou exécuter chaque itération du modèle dans une boucle, générant un token à la fois, tout en ayant la possibilité de mettre à jour les paramètres de génération à l'intérieur de la boucle. Les extensions prennent en charge les recherches gloutonnes (greedy/beam search) ainsi que les échantillonnages TopP et TopK pour générer des séquences de tokens, avec des traitements intégrés des logits comme les pénalités de répétition. Il est également facile d'ajouter des critères de notation personnalisés.

Au niveau applicatif, vous pouvez utiliser les extensions d'IA générative pour onnxruntime pour construire des applications en C++/C#/Python. Au niveau des modèles, elles permettent de fusionner des modèles fine-tunés et de réaliser des déploiements quantitatifs connexes.

## **Quantification de Phi-3.5 avec les extensions d'IA générative pour onnxruntime**

### **Modèles pris en charge**

Les extensions d'IA générative pour onnxruntime prennent en charge la conversion en quantification des modèles Microsoft Phi, Google Gemma, Mistral, Meta LLaMA.

### **Générateur de modèles dans les extensions d'IA générative pour onnxruntime**

Le générateur de modèles accélère considérablement la création de modèles ONNX optimisés et quantifiés qui fonctionnent avec l'API generate() d'ONNX Runtime.

Grâce au générateur de modèles, vous pouvez quantifier un modèle en INT4, INT8, FP16, FP32, et combiner différentes méthodes d'accélération matérielle telles que CPU, CUDA, DirectML, Mobile, etc.

Pour utiliser le générateur de modèles, vous devez installer :

```bash

pip install torch transformers onnx onnxruntime

pip install --pre onnxruntime-genai

```

Après l'installation, vous pouvez exécuter le script du générateur de modèles depuis le terminal pour effectuer la conversion de format et de quantification du modèle.

```bash

python3 -m onnxruntime_genai.models.builder -m model_name -o path_to_output_folder -p precision -e execution_provider -c cache_dir_to_save_hf_files

```

Explication des paramètres pertinents :

1. **model_name** C'est le modèle sur Hugging Face, comme microsoft/Phi-3.5-mini-instruct, microsoft/Phi-3.5-vision-instruct, etc. Cela peut également être le chemin où vous stockez le modèle.

2. **path_to_output_folder** Chemin de sauvegarde pour la conversion quantifiée.

3. **execution_provider** Prise en charge de l'accélération matérielle, comme cpu, cuda, DirectML.

4. **cache_dir_to_save_hf_files** Nous téléchargeons le modèle depuis Hugging Face et le mettons en cache localement.

***Remarque :***

## **Comment utiliser le générateur de modèles pour quantifier Phi-3.5**

Le générateur de modèles prend désormais en charge la quantification des modèles ONNX pour Phi-3.5 Instruct et Phi-3.5-Vision.

### **Phi-3.5-Instruct**

**Conversion en INT4 quantifié accélérée par CPU**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cpu -c ./Phi-3.5-mini-instruct

```

**Conversion en INT4 quantifié accélérée par CUDA**

```bash

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

```python

python3 -m onnxruntime_genai.models.builder -m microsoft/Phi-3.5-mini-instruct  -o ./onnx-cpu -p int4 -e cuda -c ./Phi-3.5-mini-instruct

```

### **Phi-3.5-Vision**

**Phi-3.5-vision-instruct-onnx-cpu-fp32**

1. Configurez l'environnement dans le terminal :

```bash

mkdir models

cd models 

```

2. Téléchargez microsoft/Phi-3.5-vision-instruct dans le dossier models :  
[https://huggingface.co/microsoft/Phi-3.5-vision-instruct](https://huggingface.co/microsoft/Phi-3.5-vision-instruct)

3. Veuillez télécharger ces fichiers dans votre dossier Phi-3.5-vision-instruct :

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/resolve/main/onnx/config.json)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/image_embedding_phi3_v_for_onnx.py)

- [https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/modeling_phi3_v.py)

4. Téléchargez ce fichier dans le dossier models :  
[https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py](https://huggingface.co/lokinfey/Phi-3.5-vision-instruct-onnx-cpu/blob/main/onnx/build.py)

5. Ouvrez le terminal :

    Conversion ONNX avec prise en charge FP32 :

```bash

python build.py -i .\Your Phi-3.5-vision-instruct Path\ -o .\vision-cpu-fp32 -p f32 -e cpu

```

### **Remarque :**

1. Le générateur de modèles prend actuellement en charge la conversion des modèles Phi-3.5-Instruct et Phi-3.5-Vision, mais pas Phi-3.5-MoE.

2. Pour utiliser le modèle quantifié d'ONNX, vous pouvez l'utiliser via le SDK des extensions d'IA générative pour onnxruntime.

3. Nous devons prendre en compte une IA plus responsable, donc après la conversion de quantification du modèle, il est recommandé d'effectuer des tests de résultats plus approfondis.

4. En quantifiant le modèle CPU INT4, nous pouvons le déployer sur des appareils Edge, offrant ainsi de meilleures opportunités d'application. C'est pourquoi nous avons finalisé Phi-3.5-Instruct autour de l'INT4.

## **Ressources**

1. En savoir plus sur les extensions d'IA générative pour onnxruntime :  
[https://onnxruntime.ai/docs/genai/](https://onnxruntime.ai/docs/genai/)

2. Dépôt GitHub des extensions d'IA générative pour onnxruntime :  
[https://github.com/microsoft/onnxruntime-genai](https://github.com/microsoft/onnxruntime-genai)

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisée basés sur l'intelligence artificielle. Bien que nous fassions de notre mieux pour garantir l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous ne sommes pas responsables des malentendus ou des interprétations erronées découlant de l'utilisation de cette traduction.