# **Affiner Phi-3 avec Lora**

Affiner le modèle de langage Phi-3 Mini de Microsoft en utilisant [LoRA (Low-Rank Adaptation)](https://github.com/microsoft/LoRA?WT.mc_id=aiml-138114-kinfeylo) sur un ensemble de données personnalisé d'instructions de chat.

LORA aidera à améliorer la compréhension conversationnelle et la génération de réponses.

## Guide étape par étape pour affiner Phi-3 Mini :

**Imports et Configuration**

Installation de loralib

```
pip install loralib
# Alternativement
# pip install git+https://github.com/microsoft/LoRA

```

Commencez par importer les bibliothèques nécessaires telles que datasets, transformers, peft, trl et torch.
Configurez la journalisation pour suivre le processus d'entraînement.

Vous pouvez choisir d'adapter certaines couches en les remplaçant par des équivalents implémentés dans loralib. Nous ne prenons en charge que nn.Linear, nn.Embedding et nn.Conv2d pour le moment. Nous prenons également en charge un MergedLinear pour les cas où un seul nn.Linear représente plus d'une couche, comme dans certaines implémentations de la projection qkv d'attention (voir Notes supplémentaires pour plus de détails).

```
# ===== Avant =====
# layer = nn.Linear(in_features, out_features)
```

```
# ===== Après ======
```

import loralib as lora

```
# Ajouter une paire de matrices d'adaptation de faible rang avec un rang r=16
layer = lora.Linear(in_features, out_features, r=16)
```

Avant de commencer la boucle d'entraînement, marquez uniquement les paramètres LoRA comme étant entraînables.

```
import loralib as lora
model = BigModel()
# Cela définit requires_grad à False pour tous les paramètres sans la chaîne "lora_" dans leurs noms
lora.mark_only_lora_as_trainable(model)
# Boucle d'entraînement
for batch in dataloader:
```

Lors de la sauvegarde d'un checkpoint, générez un state_dict qui ne contient que les paramètres LoRA.

```
# ===== Avant =====
# torch.save(model.state_dict(), checkpoint_path)
```
```
# ===== Après =====
torch.save(lora.lora_state_dict(model), checkpoint_path)
```

Lors du chargement d'un checkpoint en utilisant load_state_dict, assurez-vous de définir strict=False.

```
# Chargez d'abord le checkpoint pré-entraîné
model.load_state_dict(torch.load('ckpt_pretrained.pt'), strict=False)
# Puis chargez le checkpoint LoRA
model.load_state_dict(torch.load('ckpt_lora.pt'), strict=False)
```

L'entraînement peut maintenant se poursuivre comme d'habitude.

**Hyperparamètres**

Définissez deux dictionnaires : training_config et peft_config. training_config inclut les hyperparamètres pour l'entraînement, tels que le taux d'apprentissage, la taille du lot et les paramètres de journalisation.

peft_config spécifie les paramètres liés à LoRA comme le rang, le dropout et le type de tâche.

**Chargement du Modèle et du Tokenizer**

Spécifiez le chemin vers le modèle pré-entraîné Phi-3 (par exemple, "microsoft/Phi-3-mini-4k-instruct"). Configurez les paramètres du modèle, y compris l'utilisation du cache, le type de données (bfloat16 pour la précision mixte) et l'implémentation de l'attention.

**Entraînement**

Affinez le modèle Phi-3 en utilisant l'ensemble de données personnalisé d'instructions de chat. Utilisez les paramètres LoRA de peft_config pour une adaptation efficace. Surveillez les progrès de l'entraînement en utilisant la stratégie de journalisation spécifiée.
Évaluation et Sauvegarde : Évaluez le modèle affiné.
Sauvegardez les checkpoints pendant l'entraînement pour une utilisation ultérieure.

**Exemples**
- [En savoir plus avec ce notebook d'exemple](../../code/04.Finetuning/Phi_3_Inference_Finetuning.ipynb)
- [Exemple de script d'affinage en Python](../../code/04.Finetuning/FineTrainingScript.py)
- [Exemple d'affinage avec LORA sur Hugging Face Hub](../../code/04.Finetuning/Phi-3-finetune-lora-python.ipynb)
- [Exemple de carte de modèle Hugging Face - Exemple d'affinage avec LORA](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct/blob/main/sample_finetune.py)
- [Exemple d'affinage avec QLORA sur Hugging Face Hub](../../code/04.Finetuning/Phi-3-finetune-qlora-python.ipynb)

Avertissement : La traduction a été réalisée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. Veuillez examiner le résultat et apporter les corrections nécessaires.