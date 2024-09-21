
Il importe le module os, qui fournit une manière portable d'utiliser des fonctionnalités dépendantes du système d'exploitation. Il utilise la fonction os.system pour exécuter le script download-dataset.py dans le shell avec des arguments spécifiques en ligne de commande. Les arguments spécifient le jeu de données à télécharger (HuggingFaceH4/ultrachat_200k), le répertoire dans lequel le télécharger (ultrachat_200k_dataset), et le pourcentage du jeu de données à diviser (5). La fonction os.system renvoie le statut de sortie de la commande qu'elle a exécutée ; ce statut est stocké dans la variable exit_status. Il vérifie si exit_status n'est pas égal à 0. Dans les systèmes d'exploitation de type Unix, un statut de sortie de 0 indique généralement qu'une commande a réussi, tandis que tout autre nombre indique une erreur. Si exit_status n'est pas égal à 0, il lève une Exception avec un message indiquant qu'il y a eu une erreur lors du téléchargement du jeu de données. En résumé, ce script exécute une commande pour télécharger un jeu de données en utilisant un script d'aide, et il lève une exception si la commande échoue. ```
# Importer le module os, qui fournit une manière d'utiliser des fonctionnalités dépendantes du système d'exploitation
import os

# Utiliser la fonction os.system pour exécuter le script download-dataset.py dans le shell avec des arguments spécifiques en ligne de commande
# Les arguments spécifient le jeu de données à télécharger (HuggingFaceH4/ultrachat_200k), le répertoire dans lequel le télécharger (ultrachat_200k_dataset), et le pourcentage du jeu de données à diviser (5)
# La fonction os.system renvoie le statut de sortie de la commande qu'elle a exécutée ; ce statut est stocké dans la variable exit_status
exit_status = os.system(
    "python ./download-dataset.py --dataset HuggingFaceH4/ultrachat_200k --download_dir ultrachat_200k_dataset --dataset_split_pc 5"
)

# Vérifier si exit_status n'est pas égal à 0
# Dans les systèmes d'exploitation de type Unix, un statut de sortie de 0 indique généralement qu'une commande a réussi, tandis que tout autre nombre indique une erreur
# Si exit_status n'est pas égal à 0, lever une Exception avec un message indiquant qu'il y a eu une erreur lors du téléchargement du jeu de données
if exit_status != 0:
    raise Exception("Erreur lors du téléchargement du jeu de données")
```
### Charger les données dans un DataFrame
Ce script Python charge un fichier JSON Lines dans un DataFrame pandas et affiche les 5 premières lignes. Voici un aperçu de ce qu'il fait :

Il importe la bibliothèque pandas, qui est une bibliothèque puissante pour la manipulation et l'analyse de données.

Il définit la largeur maximale des colonnes pour les options d'affichage de pandas à 0. Cela signifie que le texte complet de chaque colonne sera affiché sans troncature lorsque le DataFrame sera imprimé.

Il utilise la fonction pd.read_json pour charger le fichier train_sft.jsonl du répertoire ultrachat_200k_dataset dans un DataFrame. L'argument lines=True indique que le fichier est au format JSON Lines, où chaque ligne est un objet JSON distinct.

Il utilise la méthode head pour afficher les 5 premières lignes du DataFrame. Si le DataFrame a moins de 5 lignes, il les affichera toutes.

En résumé, ce script charge un fichier JSON Lines dans un DataFrame et affiche les 5 premières lignes avec le texte complet des colonnes.

```
# Importer la bibliothèque pandas, qui est une bibliothèque puissante pour la manipulation et l'analyse de données
import pandas as pd

# Définir la largeur maximale des colonnes pour les options d'affichage de pandas à 0
# Cela signifie que le texte complet de chaque colonne sera affiché sans troncature lorsque le DataFrame sera imprimé
pd.set_option("display.max_colwidth", 0)

# Utiliser la fonction pd.read_json pour charger le fichier train_sft.jsonl du répertoire ultrachat_200k_dataset dans un DataFrame
# L'argument lines=True indique que le fichier est au format JSON Lines, où chaque ligne est un objet JSON distinct
df = pd.read_json("./ultrachat_200k_dataset/train_sft.jsonl", lines=True)

# Utiliser la méthode head pour afficher les 5 premières lignes du DataFrame
# Si le DataFrame a moins de 5 lignes, il les affichera toutes
df.head()
```
## 5. Soumettre le travail de fine tuning en utilisant le modèle et les données comme entrées
Créez le travail qui utilise le composant de pipeline chat-completion. En savoir plus sur tous les paramètres pris en charge pour le fine tuning.

### Définir les paramètres de fine tuning

Les paramètres de fine tuning peuvent être regroupés en 2 catégories - paramètres de formation, paramètres d'optimisation

Les paramètres de formation définissent les aspects de la formation tels que :

- L'optimiseur, le planificateur à utiliser
- La métrique à optimiser pour le fine tuning
- Le nombre d'étapes de formation et la taille du lot, etc.
- Les paramètres d'optimisation aident à optimiser la mémoire GPU et à utiliser efficacement les ressources de calcul.

Voici quelques-uns des paramètres appartenant à cette catégorie. Les paramètres d'optimisation diffèrent pour chaque modèle et sont emballés avec le modèle pour gérer ces variations.

- Activer le deepspeed et LoRA
- Activer l'entraînement en précision mixte
- Activer l'entraînement multi-nœuds

**Note:** Le fine tuning supervisé peut entraîner une perte d'alignement ou un oubli catastrophique. Nous recommandons de vérifier ce problème et de procéder à une étape d'alignement après le fine tuning.

### Paramètres de Fine Tuning

Ce script Python configure les paramètres pour le fine tuning d'un modèle d'apprentissage automatique. Voici un aperçu de ce qu'il fait :

Il configure les paramètres de formation par défaut tels que le nombre d'époques de formation, les tailles de lot pour la formation et l'évaluation, le taux d'apprentissage, et le type de planificateur de taux d'apprentissage.

Il configure les paramètres d'optimisation par défaut tels que l'application de la propagation de pertinence par couche (LoRa) et DeepSpeed, et le stade DeepSpeed.

Il combine les paramètres de formation et d'optimisation en un seul dictionnaire appelé finetune_parameters.

Il vérifie si le foundation_model a des paramètres par défaut spécifiques au modèle. Si c'est le cas, il imprime un message d'avertissement et met à jour le dictionnaire finetune_parameters avec ces paramètres par défaut spécifiques au modèle. La fonction ast.literal_eval est utilisée pour convertir les paramètres par défaut spécifiques au modèle d'une chaîne de caractères en un dictionnaire Python.

Il imprime l'ensemble final de paramètres de fine tuning qui seront utilisés pour l'exécution.

En résumé, ce script configure et affiche les paramètres pour le fine tuning d'un modèle d'apprentissage automatique, avec la possibilité de remplacer les paramètres par défaut par des paramètres spécifiques au modèle.

```
# Configurer les paramètres de formation par défaut tels que le nombre d'époques de formation, les tailles de lot pour la formation et l'évaluation, le taux d'apprentissage, et le type de planificateur de taux d'apprentissage
training_parameters = dict(
    num_train_epochs=3,
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    learning_rate=5e-6,
    lr_scheduler_type="cosine",
)

# Configurer les paramètres d'optimisation par défaut tels que l'application de la propagation de pertinence par couche (LoRa) et DeepSpeed, et le stade DeepSpeed
optimization_parameters = dict(
    apply_lora="true",
    apply_deepspeed="true",
    deepspeed_stage=2,
)

# Combiner les paramètres de formation et d'optimisation en un seul dictionnaire appelé finetune_parameters
finetune_parameters = {**training_parameters, **optimization_parameters}

# Vérifier si le foundation_model a des paramètres par défaut spécifiques au modèle
# Si c'est le cas, imprimer un message d'avertissement et mettre à jour le dictionnaire finetune_parameters avec ces paramètres par défaut spécifiques au modèle
# La fonction ast.literal_eval est utilisée pour convertir les paramètres par défaut spécifiques au modèle d'une chaîne de caractères en un dictionnaire Python
if "model_specific_defaults" in foundation_model.tags:
    print("Attention ! Des paramètres par défaut spécifiques au modèle existent. Les paramètres par défaut peuvent être remplacés.")
    finetune_parameters.update(
        ast.literal_eval(  # convertir la chaîne de caractères en dictionnaire Python
            foundation_model.tags["model_specific_defaults"]
        )
    )

# Imprimer l'ensemble final de paramètres de fine tuning qui seront utilisés pour l'exécution
print(
    f"Les paramètres de fine tuning suivants vont être définis pour l'exécution : {finetune_parameters}"
)
```

### Pipeline de Formation
Ce script Python définit une fonction pour générer un nom d'affichage pour un pipeline de formation en apprentissage automatique, puis appelle cette fonction pour générer et imprimer le nom d'affichage. Voici un aperçu de ce qu'il fait :

La fonction get_pipeline_display_name est définie. Cette fonction génère un nom d'affichage basé sur divers paramètres liés au pipeline de formation.

À l'intérieur de la fonction, il calcule la taille totale du lot en multipliant la taille du lot par appareil, le nombre d'étapes d'accumulation de gradient, le nombre de GPU par nœud et le nombre de nœuds utilisés pour le fine tuning.

Il récupère divers autres paramètres tels que le type de planificateur de taux d'apprentissage, si DeepSpeed est appliqué, le stade DeepSpeed, si la propagation de pertinence par couche (LoRa) est appliquée, la limite sur le nombre de points de contrôle du modèle à conserver, et la longueur maximale de la séquence.

Il construit une chaîne de caractères qui inclut tous ces paramètres, séparés par des tirets. Si DeepSpeed ou LoRa est appliqué, la chaîne inclut "ds" suivi du stade DeepSpeed, ou "lora", respectivement. Sinon, elle inclut "nods" ou "nolora", respectivement.

La fonction renvoie cette chaîne de caractères, qui sert de nom d'affichage pour le pipeline de formation.

Après la définition de la fonction, elle est appelée pour générer le nom d'affichage, qui est ensuite imprimé.

En résumé, ce script génère un nom d'affichage pour un pipeline de formation en apprentissage automatique basé sur divers paramètres, puis imprime ce nom d'affichage.

```
# Définir une fonction pour générer un nom d'affichage pour le pipeline de formation
def get_pipeline_display_name():
    # Calculer la taille totale du lot en multipliant la taille du lot par appareil, le nombre d'étapes d'accumulation de gradient, le nombre de GPU par nœud et le nombre de nœuds utilisés pour le fine tuning
    batch_size = (
        int(finetune_parameters.get("per_device_train_batch_size", 1))
        * int(finetune_parameters.get("gradient_accumulation_steps", 1))
        * int(gpus_per_node)
        * int(finetune_parameters.get("num_nodes_finetune", 1))
    )
    # Récupérer le type de planificateur de taux d'apprentissage
    scheduler = finetune_parameters.get("lr_scheduler_type", "linear")
    # Récupérer si DeepSpeed est appliqué
    deepspeed = finetune_parameters.get("apply_deepspeed", "false")
    # Récupérer le stade DeepSpeed
    ds_stage = finetune_parameters.get("deepspeed_stage", "2")
    # Si DeepSpeed est appliqué, inclure "ds" suivi du stade DeepSpeed dans le nom d'affichage ; sinon, inclure "nods"
    if deepspeed == "true":
        ds_string = f"ds{ds_stage}"
    else:
        ds_string = "nods"
    # Récupérer si la propagation de pertinence par couche (LoRa) est appliquée
    lora = finetune_parameters.get("apply_lora", "false")
    # Si LoRa est appliqué, inclure "lora" dans le nom d'affichage ; sinon, inclure "nolora"
    if lora == "true":
        lora_string = "lora"
    else:
        lora_string = "nolora"
    # Récupérer la limite sur le nombre de points de contrôle du modèle à conserver
    save_limit = finetune_parameters.get("save_total_limit", -1)
    # Récupérer la longueur maximale de la séquence
    seq_len = finetune_parameters.get("max_seq_length", -1)
    # Construire le nom d'affichage en concaténant tous ces paramètres, séparés par des tirets
    return (
        model_name
        + "-"
        + "ultrachat"
        + "-"
        + f"bs{batch_size}"
        + "-"
        + f"{scheduler}"
        + "-"
        + ds_string
        + "-"
        + lora_string
        + f"-save_limit{save_limit}"
        + f"-seqlen{seq_len}"
    )

# Appeler la fonction pour générer le nom d'affichage
pipeline_display_name = get_pipeline_display_name()
# Imprimer le nom d'affichage
print(f"Nom d'affichage utilisé pour l'exécution : {pipeline_display_name}")
```
### Configuration du Pipeline

Ce script Python définit et configure un pipeline d'apprentissage automatique en utilisant le SDK Azure Machine Learning. Voici un aperçu de ce qu'il fait :

1. Il importe les modules nécessaires du SDK Azure AI ML.

2. Il récupère un composant de pipeline nommé "chat_completion_pipeline" depuis le registre.

3. Il définit un travail de pipeline en utilisant le décorateur `@pipeline` et la fonction `create_pipeline`. Le nom du pipeline est défini sur `pipeline_display_name`.

4. À l'intérieur de la fonction `create_pipeline`, il initialise le composant de pipeline récupéré avec divers paramètres, y compris le chemin du modèle, les clusters de calcul pour différentes étapes, les divisions de jeu de données pour l'entraînement et les tests, le nombre de GPU à utiliser pour le fine tuning, et d'autres paramètres de fine tuning.

5. Il mappe la sortie du travail de fine tuning à la sortie du travail de pipeline. Cela est fait pour que le modèle fine tuné puisse être facilement enregistré, ce qui est nécessaire pour déployer le modèle à un point de terminaison en ligne ou par lots.

6. Il crée une instance du pipeline en appelant la fonction `create_pipeline`.

7. Il configure l'option `force_rerun` du pipeline sur `True`, ce qui signifie que les résultats mis en cache des travaux précédents ne seront pas utilisés.

8. Il configure l'option `continue_on_step_failure` du pipeline sur `False`, ce qui signifie que le pipeline s'arrêtera si une étape échoue.

En résumé, ce script définit et configure un pipeline d'apprentissage automatique pour une tâche de complétion de chat en utilisant le SDK Azure Machine Learning.

```
# Importer les modules nécessaires du SDK Azure AI ML
from azure.ai.ml.dsl import pipeline
from azure.ai.ml import Input

# Récupérer le composant de pipeline nommé "chat_completion_pipeline" depuis le registre
pipeline_component_func = registry_ml_client.components.get(
    name="chat_completion_pipeline", label="latest"
)

# Définir le travail de pipeline en utilisant le décorateur @pipeline et la fonction create_pipeline
# Le nom du pipeline est défini sur pipeline_display_name
@pipeline(name=pipeline_display_name)
def create_pipeline():
    # Initialiser le composant de pipeline récupéré avec divers paramètres
    # Ceux-ci incluent le chemin du modèle, les clusters de calcul pour différentes étapes, les divisions de jeu de données pour l'entraînement et les tests, le nombre de GPU à utiliser pour le fine tuning, et d'autres paramètres de fine tuning
    chat_completion_pipeline = pipeline_component_func(
        mlflow_model_path=foundation_model.id,
        compute_model_import=compute_cluster,
        compute_preprocess=compute_cluster,
        compute_finetune=compute_cluster,
        compute_model_evaluation=compute_cluster,
        # Mapper les divisions de jeu de données aux paramètres
        train_file_path=Input(
            type="uri_file", path="./ultrachat_200k_dataset/train_sft.jsonl"
        ),
        test_file_path=Input(
            type="uri_file", path="./ultrachat_200k_dataset/test_sft.jsonl"
        ),
        # Paramètres de formation
        number_of_gpu_to_use_finetuning=gpus_per_node,  # Définir sur le nombre de GPU disponibles dans le calcul
        **finetune_parameters
    )
    return {
        # Mapper la sortie du travail de fine tuning à la sortie du travail de pipeline
        # Cela est fait pour que nous puissions facilement enregistrer le modèle fine tuné
        # L'enregistrement du modèle est nécessaire pour déployer le modèle à un point de terminaison en ligne ou par lots
        "trained_model": chat_completion_pipeline.outputs.mlflow_model_folder
    }

# Créer une instance du pipeline en appelant la fonction create_pipeline
pipeline_object = create_pipeline()

# Ne pas utiliser les résultats mis en cache des travaux précédents
pipeline_object.settings.force_rerun = True

# Configurer continue on step failure sur False
# Cela signifie que le pipeline s'arrêtera si une étape échoue
pipeline_object.settings.continue_on_step_failure = False
```
### Soumettre le Travail

Ce script Python soumet un travail de pipeline d'apprentissage automatique à un espace de travail Azure Machine Learning et attend ensuite que le travail soit terminé. Voici un aperçu de ce qu'il fait :

Il appelle la méthode create_or_update de l'objet jobs dans le workspace_ml_client pour soumettre le travail de pipeline. Le pipeline à exécuter est spécifié par pipeline_object, et l'expérience sous laquelle le travail est exécuté est spécifiée par experiment_name.

Il appelle ensuite la méthode stream de l'objet jobs dans le workspace_ml_client pour attendre que le travail de pipeline soit terminé. Le travail à attendre est spécifié par l'attribut name de l'objet pipeline_job.

En résumé, ce script soumet un travail de pipeline d'apprentissage automatique à un espace de travail Azure Machine Learning, puis attend que le travail soit terminé.

```
# Soumettre le travail de pipeline à l'espace de travail Azure Machine Learning
# Le pipeline à exécuter est spécifié par pipeline_object
# L'expérience sous laquelle le travail est exécuté est spécifiée par experiment_name
pipeline_job = workspace_ml_client.jobs.create_or_update(
    pipeline_object, experiment_name=experiment_name
)

# Attendre que le travail de pipeline soit terminé
# Le travail à attendre est spécifié par l'attribut name de l'objet pipeline_job
workspace_ml_client.jobs.stream(pipeline_job.name)
```

## 6. Enregistrer le modèle fine tuné avec l'espace de travail
Nous allons
```
# Importer les modules nécessaires du SDK Azure AI ML
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes

# Vérifiez si la sortie `trained_model` est disponible à partir du job de pipeline
print("outputs du job de pipeline : ", workspace_ml_client.jobs.get(pipeline_job.name).outputs)

# Construire un chemin vers le modèle entraîné en formatant une chaîne avec le nom du job de pipeline et le nom de la sortie ("trained_model")
model_path_from_job = "azureml://jobs/{0}/outputs/{1}".format(
    pipeline_job.name, "trained_model"
)

# Définir un nom pour le modèle affiné en ajoutant "-ultrachat-200k" au nom du modèle original et en remplaçant les barres obliques par des tirets
finetuned_model_name = model_name + "-ultrachat-200k"
finetuned_model_name = finetuned_model_name.replace("/", "-")

print("chemin pour enregistrer le modèle : ", model_path_from_job)

# Préparer l'enregistrement du modèle en créant un objet Model avec divers paramètres
# Ceux-ci incluent le chemin vers le modèle, le type de modèle (modèle MLflow), le nom et la version du modèle, et une description du modèle
prepare_to_register_model = Model(
    path=model_path_from_job,
    type=AssetTypes.MLFLOW_MODEL,
    name=finetuned_model_name,
    version=timestamp,  # Utiliser le timestamp comme version pour éviter les conflits de version
    description=model_name + " modèle affiné pour ultrachat 200k chat-completion",
)

print("préparer l'enregistrement du modèle : \n", prepare_to_register_model)

# Enregistrer le modèle en appelant la méthode create_or_update de l'objet models dans workspace_ml_client avec l'objet Model comme argument
registered_model = workspace_ml_client.models.create_or_update(
    prepare_to_register_model
)

# Imprimer le modèle enregistré
print("modèle enregistré : \n", registered_model)
```
## 7. Déployer le modèle affiné sur un point de terminaison en ligne
Les points de terminaison en ligne fournissent une API REST durable qui peut être utilisée pour s'intégrer aux applications nécessitant l'utilisation du modèle.

### Gérer le point de terminaison
Ce script Python crée un point de terminaison en ligne géré dans Azure Machine Learning pour un modèle enregistré. Voici une explication de ce qu'il fait :

Il importe les modules nécessaires du SDK Azure AI ML.

Il définit un nom unique pour le point de terminaison en ligne en ajoutant un horodatage à la chaîne "ultrachat-completion-".

Il se prépare à créer le point de terminaison en ligne en créant un objet ManagedOnlineEndpoint avec divers paramètres, y compris le nom du point de terminaison, une description du point de terminaison et le mode d'authentification ("key").

Il crée le point de terminaison en ligne en appelant la méthode begin_create_or_update du workspace_ml_client avec l'objet ManagedOnlineEndpoint comme argument. Il attend ensuite que l'opération de création se termine en appelant la méthode wait.

En résumé, ce script crée un point de terminaison en ligne géré dans Azure Machine Learning pour un modèle enregistré.

```
# Importer les modules nécessaires du SDK Azure AI ML
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint,
    ManagedOnlineDeployment,
    ProbeSettings,
    OnlineRequestSettings,
)

# Définir un nom unique pour le point de terminaison en ligne en ajoutant un horodatage à la chaîne "ultrachat-completion-"
online_endpoint_name = "ultrachat-completion-" + timestamp

# Se préparer à créer le point de terminaison en ligne en créant un objet ManagedOnlineEndpoint avec divers paramètres
# Ceux-ci incluent le nom du point de terminaison, une description du point de terminaison et le mode d'authentification ("key")
endpoint = ManagedOnlineEndpoint(
    name=online_endpoint_name,
    description="Online endpoint for "
    + registered_model.name
    + ", fine tuned model for ultrachat-200k-chat-completion",
    auth_mode="key",
)

# Créer le point de terminaison en ligne en appelant la méthode begin_create_or_update du workspace_ml_client avec l'objet ManagedOnlineEndpoint comme argument
# Ensuite, attendre que l'opération de création se termine en appelant la méthode wait
workspace_ml_client.begin_create_or_update(endpoint).wait()
```
Vous pouvez trouver ici la liste des SKU's supportés pour le déploiement - [Managed online endpoints SKU list](https://learn.microsoft.com/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list)

### Déploiement du modèle ML

Ce script Python déploie un modèle d'apprentissage automatique enregistré sur un point de terminaison en ligne géré dans Azure Machine Learning. Voici une explication de ce qu'il fait :

Il importe le module ast, qui fournit des fonctions pour traiter les arbres de la grammaire syntaxique abstraite de Python.

Il définit le type d'instance pour le déploiement sur "Standard_NC6s_v3".

Il vérifie si le tag inference_compute_allow_list est présent dans le modèle de fondation. Si c'est le cas, il convertit la valeur du tag d'une chaîne à une liste Python et l'assigne à inference_computes_allow_list. Sinon, il définit inference_computes_allow_list sur None.

Il vérifie si le type d'instance spécifié est dans la liste d'autorisation. Si ce n'est pas le cas, il affiche un message demandant à l'utilisateur de sélectionner un type d'instance dans la liste d'autorisation.

Il se prépare à créer le déploiement en créant un objet ManagedOnlineDeployment avec divers paramètres, y compris le nom du déploiement, le nom du point de terminaison, l'ID du modèle, le type et le nombre d'instances, les paramètres de la sonde de vivacité et les paramètres de la requête.

Il crée le déploiement en appelant la méthode begin_create_or_update du workspace_ml_client avec l'objet ManagedOnlineDeployment comme argument. Il attend ensuite que l'opération de création se termine en appelant la méthode wait.

Il définit le trafic du point de terminaison pour diriger 100% du trafic vers le déploiement "demo".

Il met à jour le point de terminaison en appelant la méthode begin_create_or_update du workspace_ml_client avec l'objet endpoint comme argument. Il attend ensuite que l'opération de mise à jour se termine en appelant la méthode result.

En résumé, ce script déploie un modèle d'apprentissage automatique enregistré sur un point de terminaison en ligne géré dans Azure Machine Learning.

```
# Importer le module ast, qui fournit des fonctions pour traiter les arbres de la grammaire syntaxique abstraite de Python
import ast

# Définir le type d'instance pour le déploiement
instance_type = "Standard_NC6s_v3"

# Vérifier si le tag `inference_compute_allow_list` est présent dans le modèle de fondation
if "inference_compute_allow_list" in foundation_model.tags:
    # Si c'est le cas, convertir la valeur du tag d'une chaîne à une liste Python et l'assigner à `inference_computes_allow_list`
    inference_computes_allow_list = ast.literal_eval(
        foundation_model.tags["inference_compute_allow_list"]
    )
    print(f"Please create a compute from the above list - {computes_allow_list}")
else:
    # Sinon, définir `inference_computes_allow_list` sur `None`
    inference_computes_allow_list = None
    print("`inference_compute_allow_list` is not part of model tags")

# Vérifier si le type d'instance spécifié est dans la liste d'autorisation
if (
    inference_computes_allow_list is not None
    and instance_type not in inference_computes_allow_list
):
    print(
        f"`instance_type` is not in the allow listed compute. Please select a value from {inference_computes_allow_list}"
    )

# Se préparer à créer le déploiement en créant un objet `ManagedOnlineDeployment` avec divers paramètres
demo_deployment = ManagedOnlineDeployment(
    name="demo",
    endpoint_name=online_endpoint_name,
    model=registered_model.id,
    instance_type=instance_type,
    instance_count=1,
    liveness_probe=ProbeSettings(initial_delay=600),
    request_settings=OnlineRequestSettings(request_timeout_ms=90000),
)

# Créer le déploiement en appelant la méthode `begin_create_or_update` du `workspace_ml_client` avec l'objet `ManagedOnlineDeployment` comme argument
# Ensuite, attendre que l'opération de création se termine en appelant la méthode `wait`
workspace_ml_client.online_deployments.begin_create_or_update(demo_deployment).wait()

# Définir le trafic du point de terminaison pour diriger 100% du trafic vers le déploiement "demo"
endpoint.traffic = {"demo": 100}

# Mettre à jour le point de terminaison en appelant la méthode `begin_create_or_update` du `workspace_ml_client` avec l'objet `endpoint` comme argument
# Ensuite, attendre que l'opération de mise à jour se termine en appelant la méthode `result`
workspace_ml_client.begin_create_or_update(endpoint).result()
```
## 8. Tester le point de terminaison avec des données d'exemple
Nous allons récupérer des données d'exemple du jeu de données de test et les soumettre au point de terminaison en ligne pour inférence. Nous afficherons ensuite les étiquettes notées à côté des étiquettes de vérité terrain.

### Lecture des résultats
Ce script Python lit un fichier JSON Lines dans un DataFrame pandas, prend un échantillon aléatoire et réinitialise l'index. Voici une explication de ce qu'il fait :

Il lit le fichier ./ultrachat_200k_dataset/test_gen.jsonl dans un DataFrame pandas. La fonction read_json est utilisée avec l'argument lines=True car le fichier est au format JSON Lines, où chaque ligne est un objet JSON distinct.

Il prend un échantillon aléatoire de 1 ligne du DataFrame. La fonction sample est utilisée avec l'argument n=1 pour spécifier le nombre de lignes aléatoires à sélectionner.

Il réinitialise l'index du DataFrame. La fonction reset_index est utilisée avec l'argument drop=True pour supprimer l'index original et le remplacer par un nouvel index de valeurs entières par défaut.

Il affiche les 2 premières lignes du DataFrame en utilisant la fonction head avec l'argument 2. Cependant, comme le DataFrame ne contient qu'une seule ligne après l'échantillonnage, cela n'affichera que cette seule ligne.

En résumé, ce script lit un fichier JSON Lines dans un DataFrame pandas, prend un échantillon aléatoire de 1 ligne, réinitialise l'index et affiche la première ligne.

```
# Importer la bibliothèque pandas
import pandas as pd

# Lire le fichier JSON Lines './ultrachat_200k_dataset/test_gen.jsonl' dans un DataFrame pandas
# L'argument 'lines=True' indique que le fichier est au format JSON Lines, où chaque ligne est un objet JSON distinct
test_df = pd.read_json("./ultrachat_200k_dataset/test_gen.jsonl", lines=True)

# Prendre un échantillon aléatoire de 1 ligne du DataFrame
# L'argument 'n=1' spécifie le nombre de lignes aléatoires à sélectionner
test_df = test_df.sample(n=1)

# Réinitialiser l'index du DataFrame
# L'argument 'drop=True' indique que l'index original doit être supprimé et remplacé par un nouvel index de valeurs entières par défaut
# L'argument 'inplace=True' indique que le DataFrame doit être modifié en place (sans créer un nouvel objet)
test_df.reset_index(drop=True, inplace=True)

# Afficher les 2 premières lignes du DataFrame
# Cependant, comme le DataFrame ne contient qu'une seule ligne après l'échantillonnage, cela n'affichera que cette seule ligne
test_df.head(2)
```
### Créer un objet JSON

Ce script Python crée un objet JSON avec des paramètres spécifiques et le sauvegarde dans un fichier. Voici une explication de ce qu'il fait :

Il importe le module json, qui fournit des fonctions pour travailler avec des données JSON.

Il crée un dictionnaire parameters avec des clés et des valeurs représentant des paramètres pour un modèle d'apprentissage automatique. Les clés sont "temperature", "top_p", "do_sample", et "max_new_tokens", et leurs valeurs correspondantes sont respectivement 0.6, 0.9, True, et 200.

Il crée un autre dictionnaire test_json avec deux clés : "input_data" et "params". La valeur de "input_data" est un autre dictionnaire avec les clés "input_string" et "parameters". La valeur de "input_string" est une liste contenant le premier message du DataFrame test_df. La valeur de "parameters" est le dictionnaire parameters créé précédemment. La valeur de "params" est un dictionnaire vide.

Il ouvre un fichier nommé sample_score.json

```
# Importer le module json, qui fournit des fonctions pour travailler avec des données JSON
import json

# Créer un dictionnaire `parameters` avec des clés et des valeurs représentant des paramètres pour un modèle d'apprentissage automatique
# Les clés sont "temperature", "top_p", "do_sample", et "max_new_tokens", et leurs valeurs correspondantes sont respectivement 0.6, 0.9, True, et 200
parameters = {
    "temperature": 0.6,
    "top_p": 0.9,
    "do_sample": True,
    "max_new_tokens": 200,
}

# Créer un autre dictionnaire `test_json` avec deux clés : "input_data" et "params"
# La valeur de "input_data" est un autre dictionnaire avec les clés "input_string" et "parameters"
# La valeur de "input_string" est une liste contenant le premier message du DataFrame `test_df`
# La valeur de "parameters" est le dictionnaire `parameters` créé précédemment
# La valeur de "params" est un dictionnaire vide
test_json = {
    "input_data": {
        "input_string": [test_df["messages"][0]],
        "parameters": parameters,
    },
    "params": {},
}

# Ouvrir un fichier nommé `sample_score.json` dans le répertoire `./ultrachat_200k_dataset` en mode écriture
with open("./ultrachat_200k_dataset/sample_score.json", "w") as f:
    # Écrire le dictionnaire `test_json` dans le fichier au format JSON en utilisant la fonction `json.dump`
    json.dump(test_json, f)
```
### Invocation du point de terminaison

Ce script Python invoque un point de terminaison en ligne dans Azure Machine Learning pour noter un fichier JSON. Voici une explication de ce qu'il fait :

Il appelle la méthode invoke de la propriété online_endpoints de l'objet workspace_ml_client. Cette méthode est utilisée pour envoyer une requête à un point de terminaison en ligne et obtenir une réponse.

Il spécifie le nom du point de terminaison et du déploiement avec les arguments endpoint_name et deployment_name. Dans ce cas, le nom du point de terminaison est stocké dans la variable online_endpoint_name et le nom du déploiement est "demo".

Il spécifie le chemin vers le fichier JSON à noter avec l'argument request_file. Dans ce cas, le fichier est ./ultrachat_200k_dataset/sample_score.json.

Il stocke la réponse du point de terminaison dans la variable response.

Il imprime la réponse brute.

En résumé, ce script invoque un point de terminaison en ligne dans Azure Machine Learning pour noter un fichier JSON et imprime la réponse.

```
# Invoquer le point de terminaison en ligne dans Azure Machine Learning pour noter le fichier `sample_score.json`
# La méthode `invoke` de la propriété `online_endpoints` de l'objet `workspace_ml_client` est utilisée pour envoyer une requête à un point de terminaison en ligne et obtenir une réponse
# L'argument `endpoint_name` spécifie le nom du point de terminaison, qui est stocké dans la variable `online_endpoint_name`
# L'argument `deployment_name` spécifie le nom du déploiement, qui est "demo"
# L'argument `request_file` spécifie le chemin vers le fichier JSON à noter, qui est `./ultrachat_200k_dataset/sample_score.json`
response = workspace_ml_client.online_endpoints.invoke(
    endpoint_name=online_endpoint_name,
    deployment_name="demo",
    request_file="./ultrachat_200k_dataset/sample_score.json",
)

# Imprimer la réponse brute du point de terminaison
print("raw response: \n", response, "\n")
```
## 9. Supprimer le point de terminaison en ligne
N'oubliez pas de supprimer le point de terminaison en ligne, sinon vous laisserez le compteur de facturation tourner pour le calcul utilisé par le point de terminaison. Cette ligne de code Python supprime un point de terminaison en ligne dans Azure Machine Learning. Voici une explication de ce qu'elle fait :

Elle appelle la méthode begin_delete de la propriété online_endpoints de l'objet workspace_ml_client. Cette méthode est utilisée pour démarrer la suppression d'un point de terminaison en ligne.

Elle spécifie le nom du point de terminaison à supprimer avec l'argument name. Dans ce cas, le nom du point de terminaison est stocké dans la variable online_endpoint_name.

Elle appelle la méthode wait pour attendre que l'opération de suppression soit terminée. Il s'agit d'une opération bloquante, ce qui signifie qu'elle empêchera le script de continuer jusqu'à ce que la suppression soit terminée.

En résumé, cette ligne de code démarre la suppression d'un point de terminaison en ligne dans Azure Machine Learning et attend que l'opération soit terminée.

```
# Supprimer le point de terminaison en ligne dans Azure Machine Learning
# La méthode `begin_delete` de la propriété `online_endpoints` de l'objet `workspace_ml_client` est utilisée pour démarrer la suppression d'un point de terminaison en ligne
# L'argument `name` spécifie le nom du point de terminaison à supprimer, qui est stocké dans la variable `online_endpoint_name`
# La méthode `wait` est appelée pour attendre que l'opération de suppression soit terminée. Il s'agit d'une opération bloquante, ce qui signifie qu'elle empêchera le script de continuer jusqu'à ce que la suppression soit terminée
workspace_ml_client.online_endpoints.begin_delete(name=online_endpoint_name).wait()
```

Avertissement : La traduction a été effectuée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. Veuillez vérifier le résultat et apporter les corrections nécessaires.