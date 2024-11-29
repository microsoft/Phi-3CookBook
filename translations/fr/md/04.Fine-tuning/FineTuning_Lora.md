# **Affinage de Phi-3 avec Lora**

Affinage du modèle de langage Phi-3 Mini de Microsoft en utilisant [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) sur un jeu de données d'instructions de chat personnalisé.

LoRA aidera à améliorer la compréhension conversationnelle et la génération de réponses.

## Guide étape par étape pour affiner Phi-3 Mini :

**Imports et Configuration**

Installation de loralib

```
pip install loralib
# Alternatively
# pip install git+https://github.com/microsoft/LoRA

```

Commencez par importer les bibliothèques nécessaires telles que datasets, transformers, peft, trl, et torch.
Configurez la journalisation pour suivre le processus de formation.

Vous pouvez choisir d'adapter certaines couches en les remplaçant par des équivalents implémentés dans loralib. Nous ne supportons pour l'instant que nn.Linear, nn.Embedding, et nn.Conv2d. Nous supportons également un MergedLinear pour les cas où un seul nn.Linear représente plus d'une couche, comme dans certaines implémentations de la projection attention qkv (voir Notes supplémentaires pour plus d'informations).

```
# ===== Before =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== After ======
```

import loralib as lora

```
# Add a pair of low-rank adaptation matrices with rank r=16
layer = lora.Linear(in_features, out_features, r=16)
```

Avant que la boucle d'entraînement ne commence, marquez uniquement les paramètres LoRA comme entraînables.

```
import loralib as lora
model = BigModel()
# This sets requires_grad to False for all parameters without the string "lora_" in their names
lora.mark_only_lora_as_trainable(model)
# Training loop
for batch in dataloader:
```

Lors de l'enregistrement d'un checkpoint, générez un state_dict qui ne contient que les paramètres LoRA.

```
# ===== Before =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== After =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Lors du chargement d'un checkpoint en utilisant load_state_dict, assurez-vous de définir strict=False.

```
# Load the pretrained checkpoint first
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Then load the LoRA checkpoint
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

L'entraînement peut maintenant se dérouler normalement.

**Hyperparamètres**

Définissez deux dictionnaires : training_config et peft_config. training_config inclut les hyperparamètres pour l'entraînement, tels que le taux d'apprentissage, la taille du lot, et les paramètres de journalisation.

peft_config spécifie les paramètres liés à LoRA comme le rang, le dropout, et le type de tâche.

**Chargement du Modèle et du Tokenizer**

Spécifiez le chemin vers le modèle pré-entraîné Phi-3 (par exemple, "microsoft/Phi-3-mini-4k-instruct"). Configurez les paramètres du modèle, y compris l'utilisation du cache, le type de données (bfloat16 pour la précision mixte), et l'implémentation de l'attention.

**Entraînement**

Affinez le modèle Phi-3 en utilisant le jeu de données d'instructions de chat personnalisé. Utilisez les paramètres LoRA de peft_config pour une adaptation efficace. Surveillez la progression de l'entraînement en utilisant la stratégie de journalisation spécifiée.
Évaluation et Sauvegarde : Évaluez le modèle affiné.
Enregistrez les checkpoints pendant l'entraînement pour une utilisation ultérieure.

**Exemples**
- [En savoir plus avec cet exemple de notebook](../../../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Exemple de script d'affinage en Python](../../../../code/04.Finetuning/FineTrainingScript.py)
- [Exemple d'affinage avec LORA sur Hugging Face Hub](../../../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Exemple de carte modèle Hugging Face - Affinage LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Exemple d'affinage avec QLORA sur Hugging Face Hub](../../../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

**Avertissement** :
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées résultant de l'utilisation de cette traduction.