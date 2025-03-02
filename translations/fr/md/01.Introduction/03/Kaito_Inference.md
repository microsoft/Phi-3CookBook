## Inférence avec Kaito

[Kaito](https://github.com/Azure/kaito) est un opérateur qui automatise le déploiement de modèles d'inférence AI/ML dans un cluster Kubernetes.

Kaito présente les différenciations clés suivantes par rapport à la plupart des méthodologies de déploiement de modèles classiques basées sur des infrastructures de machines virtuelles :

- Gérer les fichiers de modèles à l'aide d'images de conteneurs. Un serveur HTTP est fourni pour effectuer des appels d'inférence en utilisant la bibliothèque du modèle.
- Éviter de régler les paramètres de déploiement pour s'adapter au matériel GPU en fournissant des configurations prédéfinies.
- Auto-provisionner les nœuds GPU en fonction des besoins du modèle.
- Héberger de grandes images de modèles dans le Microsoft Container Registry (MCR) public si la licence le permet.

Avec Kaito, le processus d'intégration de grands modèles d'inférence AI dans Kubernetes est grandement simplifié.

## Architecture

Kaito suit le modèle classique de conception basé sur les Custom Resource Definitions (CRD) et les contrôleurs Kubernetes. L'utilisateur gère une ressource personnalisée `workspace` qui décrit les besoins en GPU et la spécification d'inférence. Les contrôleurs Kaito automatisent le déploiement en conciliant la ressource personnalisée `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Architecture de Kaito" alt="Architecture de Kaito">
</div>

La figure ci-dessus présente un aperçu de l'architecture de Kaito. Ses principaux composants comprennent :

- **Workspace controller** : Il concilie la ressource personnalisée `workspace`, crée des ressources personnalisées `machine` (expliquées ci-dessous) pour déclencher l'auto-provisionnement des nœuds et crée la charge de travail d'inférence (`deployment` ou `statefulset`) en fonction des configurations prédéfinies du modèle.
- **Node provisioner controller** : Le contrôleur porte le nom *gpu-provisioner* dans le [helm chart gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Il utilise la CRD `machine` issue de [Karpenter](https://sigs.k8s.io/karpenter) pour interagir avec le contrôleur de workspace. Il s'intègre aux API Azure Kubernetes Service (AKS) pour ajouter de nouveaux nœuds GPU au cluster AKS.  
> Note : Le [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) est un composant open source. Il peut être remplacé par d'autres contrôleurs s'ils prennent en charge les API de [Karpenter-core](https://sigs.k8s.io/karpenter).

## Installation

Veuillez consulter le guide d'installation [ici](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Démarrage rapide Inférence Phi-3
[Exemple de code d'inférence Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      apps: phi-3
inference:
  preset:
    name: phi-3-mini-4k-instruct
    # Note: This configuration also works with the phi-3-mini-128k-instruct preset
```

```sh
$ cat examples/inference/kaito_workspace_phi_3.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: phi-3-adapter
tuning:
  preset:
    name: phi-3-mini-4k-instruct
  method: qlora
  input:
    urls:
      - "https://huggingface.co/datasets/philschmid/dolly-15k-oai-style/resolve/main/data/train-00000-of-00001-54e3756291ca09c6.parquet?download=true"
  output:
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # Tuning Output ACR Path
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3.yaml
```

Le statut du workspace peut être suivi en exécutant la commande suivante. Lorsque la colonne WORKSPACEREADY devient `True`, le modèle a été déployé avec succès.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Ensuite, on peut trouver l'IP du cluster du service d'inférence et utiliser un pod `curl` temporaire pour tester le point de terminaison du service dans le cluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Démarrage rapide Inférence Phi-3 avec adaptateurs

Après avoir installé Kaito, on peut essayer les commandes suivantes pour démarrer un service d'inférence.

[Exemple de code d'inférence Phi-3 avec adaptateurs](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

```
apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini-adapter
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      apps: phi-3-adapter
inference:
  preset:
    name: phi-3-mini-128k-instruct
  adapters:
    - source:
        name: "phi-3-adapter"
        image: "ACR_REPO_HERE.azurecr.io/ADAPTER_HERE:0.0.1"
      strength: "1.0"
```

```sh
$ cat examples/inference/kaito_workspace_phi_3_with_adapters.yaml

apiVersion: kaito.sh/v1alpha1
kind: Workspace
metadata:
  name: workspace-phi-3-mini-adapter
resource:
  instanceType: "Standard_NC6s_v3"
  labelSelector:
    matchLabels:
      app: phi-3-adapter
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
    

$ kubectl apply -f examples/inference/kaito_workspace_phi_3_with_adapters.yaml
```

Le statut du workspace peut être suivi en exécutant la commande suivante. Lorsque la colonne WORKSPACEREADY devient `True`, le modèle a été déployé avec succès.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Ensuite, on peut trouver l'IP du cluster du service d'inférence et utiliser un pod `curl` temporaire pour tester le point de terminaison du service dans le cluster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatisés basés sur l'intelligence artificielle. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatiques peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de recourir à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées découlant de l'utilisation de cette traduction.