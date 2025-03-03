## Ajustement avec Kaito

[Kaito](https://github.com/Azure/kaito) est un opérateur qui automatise le déploiement de modèles d'inférence AI/ML dans un cluster Kubernetes.

Kaito présente les principales différences suivantes par rapport à la plupart des méthodologies de déploiement de modèles basées sur des infrastructures de machines virtuelles :

- Gérer les fichiers de modèles à l'aide d'images de conteneur. Un serveur HTTP est fourni pour effectuer des appels d'inférence en utilisant la bibliothèque du modèle.
- Éviter de régler les paramètres de déploiement pour s'adapter au matériel GPU en fournissant des configurations prédéfinies.
- Approvisionnement automatique des nœuds GPU en fonction des exigences du modèle.
- Héberger de grandes images de modèles dans le registre public Microsoft Container Registry (MCR) si la licence le permet.

Avec Kaito, le flux de travail pour intégrer de grands modèles d'inférence AI dans Kubernetes est considérablement simplifié.

## Architecture

Kaito suit le modèle classique de conception Kubernetes basé sur la définition de ressource personnalisée (CRD) et un contrôleur. L'utilisateur gère une ressource personnalisée `workspace` qui décrit les besoins en GPU et la spécification d'inférence. Les contrôleurs Kaito automatisent le déploiement en conciliant la ressource personnalisée `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Architecture de Kaito" alt="Architecture de Kaito">
</div>

La figure ci-dessus présente une vue d'ensemble de l'architecture de Kaito. Ses principaux composants incluent :

- **Contrôleur de workspace** : Il concilie la ressource personnalisée `workspace`, crée des ressources personnalisées `machine` (expliquées ci-dessous) pour déclencher l'approvisionnement automatique des nœuds, et crée la charge de travail d'inférence (`deployment` ou `statefulset`) basée sur les configurations prédéfinies du modèle.
- **Contrôleur de provisionnement des nœuds** : Ce contrôleur porte le nom *gpu-provisioner* dans le [chart helm gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Il utilise le CRD `machine` issu de [Karpenter](https://sigs.k8s.io/karpenter) pour interagir avec le contrôleur de workspace. Il s'intègre aux APIs d'Azure Kubernetes Service (AKS) pour ajouter de nouveaux nœuds GPU au cluster AKS.  
> Remarque : Le [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) est un composant open source. Il peut être remplacé par d'autres contrôleurs s'ils prennent en charge les APIs de [Karpenter-core](https://sigs.k8s.io/karpenter).

## Vidéo d'aperçu 
[Regardez la démonstration de Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Installation

Veuillez consulter le guide d'installation [ici](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Démarrage rapide

Après avoir installé Kaito, vous pouvez essayer les commandes suivantes pour démarrer un service d'ajustement.

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

Ensuite, vous pouvez trouver l'adresse IP du service d'inférence dans le cluster et utiliser un pod temporaire `curl` pour tester le point de terminaison du service dans le cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Avertissement** :  
Ce document a été traduit à l'aide de services de traduction automatique basés sur l'IA. Bien que nous nous efforcions d'assurer l'exactitude, veuillez noter que les traductions automatisées peuvent contenir des erreurs ou des inexactitudes. Le document original dans sa langue d'origine doit être considéré comme la source faisant autorité. Pour des informations critiques, il est recommandé de faire appel à une traduction humaine professionnelle. Nous déclinons toute responsabilité en cas de malentendus ou d'interprétations erronées résultant de l'utilisation de cette traduction.