# Recette de finetuning Phi-3.5-vision

Ceci est le support officiel du finetuning de Phi-3.5-vision en utilisant les bibliothèques huggingface.
Veuillez `cd` dans le répertoire de code [vision_finetuning](../../../../code/04.Finetuning/vision_finetuning) avant d'exécuter les commandes suivantes.

## Installation

```bash
# create a new conda environment
conda create -n phi3v python=3.10
conda activate phi3v

# install pytorch
conda install pytorch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 pytorch-cuda=12.1 -c pytorch -c nvidia

# other libraries needed to run the example code
pip install -r requirements.txt

# (optional) flash attention -- Ampere+ GPUs (e.g., A100, H100)
pip install ninja
MAX_JOBS=32 pip install flash-attn==2.4.2 --no-build-isolation

# (optional) QLoRA -- Turing+ GPUs (e.g., RTX 8000)
pip install bitsandbytes==0.43.1
```

## Démarrage rapide

Nous fournissons deux scripts de finetuning d'exemple, l'un pour DocVQA et l'autre pour la classification des mèmes haineux.

Matériel minimal testé sur 4x RTX8000 (48GB RAM par GPU)

```bash
# minimal script on a mini-train split of DocVQA
torchrun --nproc_per_node=4 finetune_hf_trainer_docvqa.py
```

Phi-3.5-vision prend désormais officiellement en charge les entrées multi-images. Voici un exemple pour le finetuning de NLVR2

```bash
torchrun --nproc_per_node=8 finetune_hf_trainer_nlvr2.py
```

## Guide d'utilisation

En fonction du matériel, les utilisateurs peuvent choisir différentes stratégies de finetuning. Nous prenons en charge le finetuning complet (avec Deepspeed Zero-2) avec des paramètres de vision éventuellement gelés, et LoRA (y compris 4bit QLoRA).
En général, nous recommandons d'utiliser le finetuning complet avec flash attention et bf16 dès que possible.

### Guide pour convertir votre jeu de données personnalisé au format requis

Nous utilisons un jeu de données de classification vidéo minimal (un sous-ensemble de UCF-101) comme exemple de bout en bout pour démontrer comment convertir votre jeu de données personnalisé au format requis et affiner Phi-3.5-vision dessus.

```bash
# convert data
python convert_ucf101.py --out_dir /path/to/converted_ucf101

# training
torchrun --nproc_per_node=4 finetune_hf_trainer_ucf101.py --data_dir /path/to/converted_ucf101
```

Les données converties ressembleront à ceci :

```bash
> tree --filelimit=10 /path/to/converted_ucf101
/path/to/converted_ucf101
├── images
│   ├── test
│   │   ├── ApplyEyeMakeup [48 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [32 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [56 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [72 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [32 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [72 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [80 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [88 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [48 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [72 entries exceeds filelimit, not opening dir]
│   ├── train
│   │   ├── ApplyEyeMakeup [240 entries exceeds filelimit, not opening dir]
│   │   ├── ApplyLipstick [240 entries exceeds filelimit, not opening dir]
│   │   ├── Archery [240 entries exceeds filelimit, not opening dir]
│   │   ├── BabyCrawling [240 entries exceeds filelimit, not opening dir]
│   │   ├── BalanceBeam [240 entries exceeds filelimit, not opening dir]
│   │   ├── BandMarching [240 entries exceeds filelimit, not opening dir]
│   │   ├── BaseballPitch [240 entries exceeds filelimit, not opening dir]
│   │   ├── Basketball [240 entries exceeds filelimit, not opening dir]
│   │   ├── BasketballDunk [240 entries exceeds filelimit, not opening dir]
│   │   └── BenchPress [240 entries exceeds filelimit, not opening dir]
│   └── val
│       ├── ApplyEyeMakeup [24 entries exceeds filelimit, not opening dir]
│       ├── ApplyLipstick [24 entries exceeds filelimit, not opening dir]
│       ├── Archery [24 entries exceeds filelimit, not opening dir]
│       ├── BabyCrawling [24 entries exceeds filelimit, not opening dir]
│       ├── BalanceBeam [24 entries exceeds filelimit, not opening dir]
│       ├── BandMarching [24 entries exceeds filelimit, not opening dir]
│       ├── BaseballPitch [24 entries exceeds filelimit, not opening dir]
│       ├── Basketball [24 entries exceeds filelimit, not opening dir]
│       ├── BasketballDunk [24 entries exceeds filelimit, not opening dir]
│       └── BenchPress [24 entries exceeds filelimit, not opening dir]
├── ucf101_test.jsonl
├── ucf101_train.jsonl
└── ucf101_val.jsonl

34 directories, 3 files
```

Pour l'annotation `jsonl`, chaque ligne doit être un dictionnaire comme :

```json
{"id": "val-0000000300", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g21_c04.0.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.1.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.2.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.3.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.4.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.5.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.6.jpg", "val/BabyCrawling/v_BabyCrawling_g21_c04.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
{"id": "val-0000000301", "source": "ucf101", "conversations": [{"images": ["val/BabyCrawling/v_BabyCrawling_g09_c06.0.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.1.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.2.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.3.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.4.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.5.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.6.jpg", "val/BabyCrawling/v_BabyCrawling_g09_c06.7.jpg"], "user": "Classify the video into one of the following classes: ApplyEyeMakeup, ApplyLipstick, Archery, BabyCrawling, BalanceBeam, BandMarching, BaseballPitch, Basketball, BasketballDunk, BenchPress.", "assistant": "BabyCrawling"}]}
```

Notez que `conversations` est une liste, permettant ainsi la prise en charge de conversations multi-tours si de telles données sont disponibles.

## Demande de quota GPU Azure 

### Prérequis

Un compte Azure avec le rôle de Contributeur (ou un autre rôle incluant l'accès Contributeur).

Si vous n'avez pas de compte Azure, créez un [compte gratuit avant de commencer](https://azure.microsoft.com).

### Demander une augmentation de quota

Vous pouvez soumettre une demande d'augmentation de quota directement depuis Mes quotas. Suivez les étapes ci-dessous pour demander une augmentation de quota. Pour cet exemple, vous pouvez sélectionner n'importe quel quota ajustable dans votre abonnement.

Connectez-vous au [portail Azure](https://portal.azure.com).

Entrez "quotas" dans la boîte de recherche, puis sélectionnez Quotas.
![Quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/quotas-portal.png)

Sur la page d'aperçu, sélectionnez un fournisseur, tel que Compute ou AML.

**Note** Pour tous les fournisseurs autres que Compute, vous verrez une colonne Demander une augmentation au lieu de la colonne Ajustable décrite ci-dessous. Là, vous pouvez demander une augmentation pour un quota spécifique, ou créer une demande de support pour l'augmentation.

Sur la page Mes quotas, sous Nom du quota, sélectionnez le quota que vous souhaitez augmenter. Assurez-vous que la colonne Ajustable indique Oui pour ce quota.

En haut de la page, sélectionnez Nouvelle demande de quota, puis sélectionnez Entrer une nouvelle limite.

![Augmenter le quota](https://learn.microsoft.com/azure/quotas/media/quickstart-increase-quota-portal/enter-new-quota-limit.png)

Dans le volet Nouvelle demande de quota, entrez une valeur numérique pour votre nouvelle limite de quota, puis sélectionnez Soumettre.

Votre demande sera examinée, et vous serez notifié si la demande peut être satisfaite. Cela se produit généralement en quelques minutes.

Si votre demande n'est pas satisfaite, vous verrez un lien pour créer une demande de support. Lorsque vous utilisez ce lien, un ingénieur de support vous aidera avec votre demande d'augmentation.

## Suggestions de SKU de machines GPU Azure Compute

[ND A100 v4-series](https://learn.microsoft.com/azure/virtual-machines/nda100-v4-series)

[ND H100 v5-series](https://learn.microsoft.com/azure/virtual-machines/nd-h100-v5-series)

[Standard_ND40rs_v2](https://learn.microsoft.com/azure/virtual-machines/ndv2-series)

Voici quelques exemples :

### Si vous avez des GPU A100 ou H100

Le finetuning complet donne généralement les meilleures performances. Vous pouvez utiliser la commande suivante pour affiner Phi-3-V sur la classification des mèmes haineux.

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_flash_attention \
  --bf16
```

### Si vous avez des GPU Standard_ND40rs_v2 8x V100-32GB

Il est toujours possible d'affiner complètement Phi-3-V sur la classification des mèmes haineux. Cependant, attendez-vous à un débit beaucoup plus faible par rapport aux GPU A100 ou H100 en raison du manque de support pour flash attention.
La précision pourrait également être affectée en raison du manque de support pour bf16 (la formation en précision mixte fp16 est utilisée à la place).

```bash
torchrun --nproc_per_node=8 --nnodes=<num_nodes> \
  --master_addr=$MASTER_ADDR --master_port=$MASTER_PORT --node_rank=$NODE_RANK \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64
```

### Si vous n'avez pas accès aux GPU de centre de données
Lora pourrait être votre seule option. Vous pouvez utiliser la commande suivante pour affiner Phi-3-V sur la classification des mèmes haineux.

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora
```

Pour les GPU Turing+, QLoRA est pris en charge

```bash
torchrun --nproc_per_node=2 \
  finetune_hf_trainer_hateful_memes.py \
  --output_dir <output_dir> \
  --batch_size 64 \
  --use_lora \
  --use_qlora
```

## Hyperparamètres suggérés et précision attendue
### NLVR2

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_nlvr2.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Méthode de formation | Modèle de vision gelé | type de données | Rang LoRA | Alpha LoRA | Taille de lot | Taux d'apprentissage | Époques | Précision
--- | --- | --- | --- | --- | --- | --- | --- | --- |
finetuning complet |  | bf16 | - | - | 64 | 1e-5 | 3 | 89.40 |
finetuning complet | ✔ | bf16 | - | - | 64 | 2e-5 | 2 | 89.20 |
Résultats LoRA bientôt disponibles |  |  |  |  |  |  |  |  |

### NOTE
Les résultats ci-dessous pour DocVQA et les mèmes haineux sont basés sur la version précédente (Phi-3-vision).
Les nouveaux résultats avec Phi-3.5-vision seront mis à jour bientôt.

### DocVQA (NOTE: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_docvqa.py \
  --full_train \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Méthode de formation | type de données | Rang LoRA | Alpha LoRA | Taille de lot | Taux d'apprentissage | Époques | ANLS
--- | --- | --- | --- | --- | --- | --- | --- |
finetuning complet | bf16 | - | - | 64 | 5e-6 | 2 | 83.65 |
finetuning complet | fp16 | - | - | 64 | 5e-6 | 2 | 82.60 |
modèle d'image gelé| bf16 | - | - | 64 | 1e-4 | 2 | 79.19 |
modèle d'image gelé| fp16 | - | - | 64 | 1e-4 | 2 | 78.74 |
LoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 82.46 |
LoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 82.34 |
QLoRA | bf16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |
QLoRA | fp16 | 32 | 16 | 64 | 2e-4 | 2 | 81.85 |

### Mèmes haineux (NOTE: Phi-3-vision)

```bash
torchrun --nproc_per_node=4 \
  finetune_hf_trainer_hateful_memes.py \
  --bf16 --use_flash_attention \
  --batch_size 64 \
  --output_dir <output_dir> \
  --learning_rate <lr> \
  --num_train_epochs <epochs>

```

Méthode de formation | type de données | Rang LoRA | Alpha LoRA | Taille de lot | Taux d'apprentissage | Époques | Précision
--- | --- | --- | --- | --- | --- | --- | --- |
finetuning complet | bf16 | - | - | 64 | 5e-5 | 2 | 86.4 |
finetuning complet | fp16 | - | - | 64 | 5e-5 | 2 | 85.4 |
modèle d'image gelé| bf16 | - | - | 64 | 1e-4 | 3 | 79.4 |
modèle d'image gelé| fp16 | - | - | 64 | 1e-4 | 3 | 78.6 |
LoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 86.6 |
LoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 85.2 |
QLoRA | bf16 | 128 | 256 | 64 | 2e-4 | 2 | 84.0 |
QLoRA | fp16 | 128 | 256 | 64 | 2e-4 | 2 | 83.8 |

## Benchmarking de la vitesse (NOTE: Phi-3-vision)

Les nouveaux résultats de benchmarking avec Phi-3.5-vision seront mis à jour bientôt.

Le benchmarking de la vitesse est effectué sur le jeu de données DocVQA. La longueur moyenne des séquences de ce jeu de données est de 2443.23 tokens (en utilisant `num_crops=16` pour le modèle d'image).

### 8x A100-80GB (Ampere)

Méthode de formation | \# nœuds | GPU | flash attention | Taille de lot effective | Débit (img/s) | Accélération | Mémoire GPU de pointe (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
finetuning complet | 1 | 8 |  | 64 | 5.041 |  1x | ~42
finetuning complet | 1 | 8 | ✔ | 64 | 8.657 | 1.72x | ~36
finetuning complet | 2 | 16 | ✔ | 64 | 16.903 | 3.35x | ~29
finetuning complet | 4 | 32 | ✔ | 64 | 33.433 | 6.63x | ~26
modèle d'image gelé | 1 | 8 |  | 64 | 17.578 | 3.49x | ~29
modèle d'image gelé | 1 | 8 | ✔ | 64 | 31.736 | 6.30x | ~27
LoRA | 1 | 8 |  | 64 | 5.591 | 1.11x | ~50
LoRA | 1 | 8 | ✔ | 64 | 12.127 | 2.41x | ~16
QLoRA | 1 | 8 |  | 64 | 4.831 | 0.96x | ~32
QLoRA | 1 | 8 | ✔ | 64 | 10.545 | 2.09x | ~10

### 8x V100-32GB (Volta)

Méthode de formation | \# nœuds | GPU | flash attention | Taille de lot effective | Débit (img/s) | Accélération | Mémoire GPU de pointe (GB)
--- | --- | --- | --- | --- | --- | --- | --- |
finetuning complet | 1 | 8 | | 64 | 2.462 |  1x | ~32
finetuning complet | 2 | 16 |  | 64 | 4.182 | 1.70x | ~32
finetuning complet | 4 | 32 |  | 64 | 5.465 | 2.22x | ~32
modèle d'image gelé | 1 | 8 |  | 64 | 8.942 | 3.63x | ~27
LoRA | 1 | 8 |  | 64 | 2.807 | 1.14x | ~30

## Problèmes connus

- Impossible d'exécuter flash attention avec fp16 (bf16 est toujours recommandé lorsque disponible, et tous les GPU prenant en charge flash attention prennent également en charge bf16).
- Ne prend pas encore en charge la sauvegarde des checkpoints intermédiaires et la reprise de la formation.

**Avertissement** :
Ce document a été traduit en utilisant des services de traduction automatique basés sur l'IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, une traduction humaine professionnelle est recommandée. Nous ne sommes pas responsables des malentendus ou des interprétations erronées découlant de l'utilisation de cette traduction.