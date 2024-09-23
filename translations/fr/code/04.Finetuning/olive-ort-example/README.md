# Affiner Phi3 avec Olive

Dans cet exemple, vous utiliserez Olive pour :

1. Affiner un adaptateur LoRA pour classer des phrases en Triste, Joie, Peur, Surprise.
1. Fusionner les poids de l'adaptateur dans le modèle de base.
1. Optimiser et quantifier le modèle en `int4`.

Nous vous montrerons également comment inférer le modèle affiné en utilisant l'API Generate d'ONNX Runtime (ORT).

> **⚠️ Pour l'affinage, vous devrez disposer d'un GPU approprié - par exemple, un A10, V100, A100.**

## 💾 Installation

Créez un nouvel environnement virtuel Python (par exemple, en utilisant `conda`):

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Ensuite, installez Olive et les dépendances pour un flux de travail d'affinage :

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Affiner Phi3 avec Olive
Le [fichier de configuration Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) contient un *workflow* avec les *passes* suivantes :

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

À un niveau élevé, ce workflow va :

1. Affiner Phi3 (pour 150 étapes, que vous pouvez modifier) en utilisant les données de [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Fusionner les poids de l'adaptateur LoRA dans le modèle de base. Cela vous donnera un seul artefact de modèle au format ONNX.
1. Model Builder optimisera le modèle pour le runtime ONNX *et* quantifiera le modèle en `int4`.

Pour exécuter le workflow, lancez :

```bash
olive run --config phrase-classification.json
```

Lorsque Olive aura terminé, votre modèle Phi3 affiné et optimisé en `int4` sera disponible dans : `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Intégrer Phi3 affiné dans votre application 

Pour exécuter l'application :

```bash
python app/app.py --phrase "le cricket est un sport merveilleux !" --model-path models/lora-merge-mb/gpu-cuda_model
```

Cette réponse devrait être une classification en un seul mot de la phrase (Triste/Joie/Peur/Surprise).

Avertissement : La traduction a été réalisée à partir de son original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez examiner le résultat et apporter les corrections nécessaires.