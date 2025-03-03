# Affiner Phi3 avec Olive

Dans cet exemple, vous utiliserez Olive pour :

1. Affiner un adaptateur LoRA pour classifier des phrases en Tristesse, Joie, Peur, Surprise.
1. Fusionner les poids de l'adaptateur avec le modèle de base.
1. Optimiser et quantifier le modèle dans `int4`.

Nous vous montrerons également comment effectuer une inférence avec le modèle affiné en utilisant l'API Generate d'ONNX Runtime (ORT).

> **⚠️ Pour l'affinement, vous aurez besoin d'un GPU adapté - par exemple, un A10, V100, A100.**

## 💾 Installation

Créez un nouvel environnement virtuel Python (par exemple, en utilisant `conda`) :

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Ensuite, installez Olive et les dépendances nécessaires pour un flux de travail d'affinement :

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Affiner Phi3 avec Olive
Le [fichier de configuration Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) contient un *flux de travail* avec les *étapes* suivantes :

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

À un niveau élevé, ce flux de travail effectuera :

1. L'affinement de Phi3 (pour 150 étapes, que vous pouvez modifier) en utilisant les données du fichier [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. La fusion des poids de l'adaptateur LoRA avec le modèle de base. Cela produira un seul artefact de modèle au format ONNX.
1. Le Model Builder optimisera le modèle pour ONNX Runtime *et* quantifiera le modèle dans `int4`.

Pour exécuter le flux de travail, lancez :

```bash
olive run --config phrase-classification.json
```

Une fois Olive terminé, votre modèle Phi3 affiné et optimisé dans `int4` sera disponible ici : `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Intégrer le modèle Phi3 affiné dans votre application 

Pour exécuter l'application :

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Cette réponse devrait être une classification en un mot de la phrase (Tristesse/Joie/Peur/Surprise).

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction professionnelle effectuée par un humain. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées découlant de l'utilisation de cette traduction.