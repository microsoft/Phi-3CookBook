# Ajuster Phi3 avec Olive

Dans cet exemple, vous allez utiliser Olive pour :

1. Ajuster un adaptateur LoRA pour classifier des phrases en Triste, Joie, Peur, Surprise.
1. Fusionner les poids de l'adaptateur dans le modèle de base.
1. Optimiser et quantifier le modèle en `int4`.

Nous vous montrerons également comment inférer le modèle ajusté en utilisant l'API Generate d'ONNX Runtime (ORT).

> **⚠️ Pour l'ajustement, vous aurez besoin d'un GPU approprié - par exemple, un A10, V100, A100.**

## 💾 Installer

Créez un nouvel environnement virtuel Python (par exemple, en utilisant `conda`) :

```bash
conda create -n olive-ai python=3.11
conda activate olive-ai
```

Ensuite, installez Olive et les dépendances pour un workflow d'ajustement :

```bash
cd Phi-3CookBook/code/04.Finetuning/olive-ort-example
pip install olive-ai[gpu]
pip install -r requirements.txt
```

## 🧪 Ajuster Phi3 avec Olive
Le [fichier de configuration Olive](../../../../../code/04.Finetuning/olive-ort-example/phrase-classification.json) contient un *workflow* avec les *passes* suivantes :

Phi3 -> LoRA -> MergeAdapterWeights -> ModelBuilder

À un niveau élevé, ce workflow va :

1. Ajuster Phi3 (pendant 150 étapes, que vous pouvez modifier) en utilisant les données [dataset/data-classification.json](../../../../../code/04.Finetuning/olive-ort-example/dataset/dataset-classification.json).
1. Fusionner les poids de l'adaptateur LoRA dans le modèle de base. Cela vous donnera un seul artefact de modèle au format ONNX.
1. Model Builder optimisera le modèle pour le runtime ONNX *et* quantifiera le modèle en `int4`.

Pour exécuter le workflow, lancez :

```bash
olive run --config phrase-classification.json
```

Lorsque Olive aura terminé, votre modèle Phi3 ajusté et optimisé `int4` sera disponible dans : `code/04.Finetuning/olive-ort-example/models/lora-merge-mb/gpu-cuda_model`.

## 🧑‍💻 Intégrer le Phi3 ajusté dans votre application

Pour exécuter l'application :

```bash
python app/app.py --phrase "cricket is a wonderful sport!" --model-path models/lora-merge-mb/gpu-cuda_model
```

Cette réponse devrait être une classification en un seul mot de la phrase (Triste/Joie/Peur/Surprise).

**Avertissement** :
Ce document a été traduit à l'aide de services de traduction automatisés basés sur l'IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.