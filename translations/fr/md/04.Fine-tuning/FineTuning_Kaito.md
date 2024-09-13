## Fine-Tuning avec Kaito

[Kaito](https://github.com/Azure/kaito) est un opérateur qui automatise le déploiement de modèles d'inférence AI/ML dans un cluster Kubernetes.

Kaito se distingue des méthodologies de déploiement de modèles les plus courantes basées sur des infrastructures de machines virtuelles par les points suivants :

- Gérer les fichiers de modèles à l'aide d'images de conteneurs. Un serveur HTTP est fourni pour effectuer des appels d'inférence en utilisant la bibliothèque de modèles.
- Éviter de régler les paramètres de déploiement pour s'adapter au matériel GPU en fournissant des configurations prédéfinies.
- Auto-provisionner des nœuds GPU en fonction des exigences du modèle.
- Héberger de grandes images de modèles dans le registre public Microsoft Container Registry (MCR) si la licence le permet.

Avec Kaito, le processus d'intégration de grands modèles d'inférence AI dans Kubernetes est grandement simplifié.

## Architecture

Kaito suit le modèle classique de définition de ressource personnalisée (CRD) / contrôleur de Kubernetes. L'utilisateur gère une ressource personnalisée `workspace` qui décrit les exigences GPU et les spécifications d'inférence. Les contrôleurs Kaito automatiseront le déploiement en conciliant la ressource personnalisée `workspace`.
<div align="left">
  <img src="https://github.com/Azure/kaito/blob/main/docs/img/arch.png" width=80% title="Architecture de Kaito" alt="Architecture de Kaito">
</div>

La figure ci-dessus présente un aperçu de l'architecture de Kaito. Ses principaux composants sont :

- **Contrôleur de workspace** : Il concilie la ressource personnalisée `workspace`, crée des ressources personnalisées `machine` (expliquées ci-dessous) pour déclencher l'auto-provisionnement des nœuds, et crée la charge de travail d'inférence (`deployment` ou `statefulset`) en fonction des configurations prédéfinies du modèle.
- **Contrôleur de provisionnement de nœuds** : Le nom du contrôleur est *gpu-provisioner* dans [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Il utilise le CRD `machine` provenant de [Karpenter](https://sigs.k8s.io/karpenter) pour interagir avec le contrôleur de workspace. Il s'intègre avec les API d'Azure Kubernetes Service (AKS) pour ajouter de nouveaux nœuds GPU au cluster AKS.
> Note : Le [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) est un composant open source. Il peut être remplacé par d'autres contrôleurs s'ils supportent les API de [Karpenter-core](https://sigs.k8s.io/karpenter).

## Installation

Veuillez consulter les instructions d'installation [ici](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Démarrage rapide

Après avoir installé Kaito, vous pouvez essayer les commandes suivantes pour démarrer un service de fine-tuning.

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-tuning-phi-3
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: tuning-phi-3
tuning:
  preset:
    name: phi-3-mini-128k-instruct
  method: qlora
  input:
    urls:
      - "https://huggingface.co/datasets/philschmid/dolly-15k-oai-style/resolve/main/data/train-00000-of-00001-54e3756291ca09c6.parquet?download=true"
  output:
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
```

```sh
$ cat examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-tuning-phi-3
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: tuning-phi-3
tuning:
  preset:
    name: phi-3-mini-128k-instruct
  method: qlora
  input:
    urls:
      - "https://huggingface.co/datasets/philschmid/dolly-15k-oai-style/resolve/main/data/train-00000-of-00001-54e3756291ca09c6.parquet?download=true"
  output:
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml
```

L'état du workspace peut être suivi en exécutant la commande suivante. Lorsque la colonne WORKSPACEREADY devient `True`, le modèle a été déployé avec succès.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Ensuite, vous pouvez trouver l'IP du cluster du service d'inférence et utiliser un pod temporaire `curl` pour tester le point de terminaison du service dans le cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

Avertissement : La traduction a été effectuée à partir de l'original par un modèle d'IA et peut ne pas être parfaite. 
Veuillez examiner le résultat et apporter les corrections nécessaires.