# **Affiner Phi-3 avec le Framework Apple MLX**

Nous pouvons réaliser l'affinage combiné avec Lora via la ligne de commande du framework Apple MLX. (Si vous souhaitez en savoir plus sur le fonctionnement du Framework MLX, veuillez lire [Inference Phi-3 with Apple MLX Framework](../03.Inference/MLX_Inference.md))


## **1. Préparation des données**

Par défaut, le framework MLX nécessite le format jsonl pour train, test et eval, et est combiné avec Lora pour compléter les tâches d'affinage.


### ***Remarque :***

1. Format des données jsonl :


```json

{"text": "<|user|>\nQuand les vierges de fer étaient-elles couramment utilisées ? <|end|>\n<|assistant|> \nLes vierges de fer n'ont jamais été couramment utilisées <|end|>"}
{"text": "<|user|>\nDe quoi les humains ont-ils évolué ? <|end|>\n<|assistant|> \nLes humains et les singes ont évolué à partir d'un ancêtre commun <|end|>"}
{"text": "<|user|>\nLe 91 est-il un nombre premier ? <|end|>\n<|assistant|> \nNon, le 91 n'est pas un nombre premier <|end|>"}
....

```

2. Notre exemple utilise les [données de TruthfulQA](https://github.com/sylinrl/TruthfulQA/blob/main/TruthfulQA.csv), mais la quantité de données est relativement insuffisante, donc les résultats de l'affinage ne sont pas nécessairement les meilleurs. Il est recommandé que les apprenants utilisent de meilleures données basées sur leurs propres scénarios pour compléter.

3. Le format des données est combiné avec le modèle Phi-3

Veuillez télécharger les données depuis ce [lien](../../code/04.Finetuning/mlx/), veuillez inclure tous les fichiers .jsonl dans le dossier ***data***


## **2. Affinage dans votre terminal**

Veuillez exécuter cette commande dans le terminal


```bash

python -m mlx_lm.lora --model microsoft/Phi-3-mini-4k-instruct --train --data ./data --iters 1000 

```


## ***Remarque :***

1. Il s'agit d'un affinage LoRA, le framework MLX n'a pas publié QLoRA

2. Vous pouvez configurer config.yaml pour changer certains arguments, tels que


```yaml


# Le chemin vers le répertoire local du modèle ou le repo Hugging Face.
model: "microsoft/Phi-3-mini-4k-instruct"
# Entraînement ou non (booléen)
train: true

# Répertoire avec les fichiers {train, valid, test}.jsonl
data: "data"

# La graine PRNG
seed: 0

# Nombre de couches à affiner
lora_layers: 32

# Taille des mini-lots.
batch_size: 1

# Nombre d'itérations pour l'entraînement.
iters: 1000

# Nombre de lots de validation, -1 utilise l'ensemble de validation complet.
val_batches: 25

# Taux d'apprentissage Adam.
learning_rate: 1e-6

# Nombre d'étapes d'entraînement entre les rapports de perte.
steps_per_report: 10

# Nombre d'étapes d'entraînement entre les validations.
steps_per_eval: 200

# Chemin de chargement pour reprendre l'entraînement avec les poids de l'adaptateur donnés.
resume_adapter_file: null

# Chemin de sauvegarde/chargement pour les poids de l'adaptateur entraînés.
adapter_path: "adapters"

# Sauvegarder le modèle tous les N itérations.
save_every: 1000

# Évaluer sur l'ensemble de test après l'entraînement
test: false

# Nombre de lots de l'ensemble de test, -1 utilise l'ensemble de test complet.
test_batches: 100

# Longueur maximale de la séquence.
max_seq_length: 2048

# Utiliser le point de contrôle de gradient pour réduire l'utilisation de la mémoire.
grad_checkpoint: true

# Les paramètres LoRA ne peuvent être spécifiés que dans un fichier de configuration
lora_parameters:
  # Les clés de couche auxquelles appliquer LoRA.
  # Elles seront appliquées pour les dernières lora_layers
  keys: ["o_proj","qkv_proj"]
  rank: 64
  alpha: 64
  dropout: 0.1


```

Veuillez exécuter cette commande dans le terminal


```bash

python -m  mlx_lm.lora --config lora_config.yaml

```


## **3. Exécuter l'adaptateur d'affinage pour tester**

Vous pouvez exécuter l'adaptateur d'affinage dans le terminal, comme ceci 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --adapter-path ./adapters --max-token 2048 --prompt "Pourquoi les caméléons changent-ils de couleur ?" --eos-token "<|end|>"    

```

et exécuter le modèle original pour comparer le résultat 


```bash

python -m mlx_lm.generate --model microsoft/Phi-3-mini-4k-instruct --max-token 2048 --prompt "Pourquoi les caméléons changent-ils de couleur ?" --eos-token "<|end|>"    

```

Vous pouvez essayer de comparer les résultats de l'affinage avec le modèle original


## **4. Fusionner les adaptateurs pour générer de nouveaux modèles**


```bash

python -m mlx_lm.fuse --model microsoft/Phi-3-mini-4k-instruct

```

## **5. Exécuter des modèles d'affinage quantifiés en utilisant ollama**

Avant utilisation, veuillez configurer votre environnement llama.cpp


```bash

git clone https://github.com/ggerganov/llama.cpp.git

cd llama.cpp

pip install -r requirements.txt

python convert.py 'Your meger model path'  --outfile phi-3-mini-ft.gguf --outtype f16 

```

***Remarque :*** 

1. Prend en charge maintenant la conversion de quantification de fp32, fp16 et INT 8

2. Le modèle fusionné manque de tokenizer.model, veuillez le télécharger depuis https://huggingface.co/microsoft/Phi-3-mini-4k-instruct

configurer le fichier de modèle Ollma (Si ollama n'est pas installé, veuillez lire [Ollama QuickStart](../02.QuickStart/Ollama_QuickStart.md)


```txt

FROM ./phi-3-mini-ft.gguf
PARAMETER stop "<|end|>"

```

exécuter la commande dans le terminal


```bash

 ollama create phi3ft -f Modelfile 

 ollama run phi3ft "Pourquoi les caméléons changent-ils de couleur ?" 

```

Félicitations ! Vous maîtrisez l'affinage avec le Framework MLX

Avertissement : La traduction a été réalisée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez examiner le résultat et apporter les corrections nécessaires.