## Συμπεράσματα με το Kaito 

Το [Kaito](https://github.com/Azure/kaito) είναι ένας operator που αυτοματοποιεί την ανάπτυξη μοντέλων AI/ML inference σε ένα Kubernetes cluster.

Το Kaito ξεχωρίζει από τις περισσότερες παραδοσιακές μεθοδολογίες ανάπτυξης μοντέλων, οι οποίες βασίζονται σε υποδομές εικονικών μηχανών, με τα εξής βασικά χαρακτηριστικά:

- Διαχειρίζεται αρχεία μοντέλων χρησιμοποιώντας container images. Παρέχει έναν http server για την εκτέλεση inference calls χρησιμοποιώντας τη βιβλιοθήκη του μοντέλου.
- Αποφεύγει την προσαρμογή παραμέτρων ανάπτυξης για GPU hardware, παρέχοντας προεπιλεγμένες ρυθμίσεις.
- Αυτόματη προμήθεια GPU nodes με βάση τις απαιτήσεις του μοντέλου.
- Φιλοξενεί μεγάλα μοντέλα εικόνων στο δημόσιο Microsoft Container Registry (MCR), εφόσον το επιτρέπει η άδεια χρήσης.

Χρησιμοποιώντας το Kaito, η διαδικασία ενσωμάτωσης μεγάλων AI inference μοντέλων στο Kubernetes απλοποιείται σημαντικά.

## Αρχιτεκτονική

Το Kaito ακολουθεί το κλασικό μοτίβο σχεδίασης Kubernetes Custom Resource Definition(CRD)/controller. Ο χρήστης διαχειρίζεται ένα προσαρμοσμένο resource `workspace` που περιγράφει τις απαιτήσεις GPU και την προδιαγραφή inference. Οι controllers του Kaito αυτοματοποιούν την ανάπτυξη συγχρονίζοντας το προσαρμοσμένο resource `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Αρχιτεκτονική Kaito" alt="Αρχιτεκτονική Kaito">
</div>

Η παραπάνω εικόνα παρουσιάζει την επισκόπηση της αρχιτεκτονικής του Kaito. Τα βασικά του στοιχεία περιλαμβάνουν:

- **Workspace controller**: Συγχρονίζει το προσαρμοσμένο resource `workspace`, δημιουργεί προσαρμοσμένα resources `machine` (εξηγούνται παρακάτω) για να ενεργοποιήσει την αυτόματη προμήθεια κόμβων, και δημιουργεί το inference workload (`deployment` ή `statefulset`) με βάση τις προεπιλεγμένες ρυθμίσεις του μοντέλου.
- **Node provisioner controller**: Ονομάζεται *gpu-provisioner* στο [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Χρησιμοποιεί το CRD `machine` που προέρχεται από το [Karpenter](https://sigs.k8s.io/karpenter) για να αλληλεπιδράσει με τον workspace controller. Ενσωματώνεται με τα Azure Kubernetes Service(AKS) APIs για να προσθέσει νέους GPU κόμβους στο AKS cluster.
> Σημείωση: Το [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) είναι ένα ανοιχτού κώδικα στοιχείο. Μπορεί να αντικατασταθεί από άλλους controllers, εάν υποστηρίζουν τα APIs του [Karpenter-core](https://sigs.k8s.io/karpenter).

## Εγκατάσταση

Παρακαλούμε δείτε τις οδηγίες εγκατάστασης [εδώ](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Γρήγορη εκκίνηση Inference Phi-3
[Δείγμα Κώδικα Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Η κατάσταση του workspace μπορεί να παρακολουθηθεί εκτελώντας την παρακάτω εντολή. Όταν η στήλη WORKSPACEREADY γίνει `True`, το μοντέλο έχει αναπτυχθεί επιτυχώς.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Στη συνέχεια, μπορείτε να βρείτε το cluster ip της inference υπηρεσίας και να χρησιμοποιήσετε ένα προσωρινό pod `curl` για να δοκιμάσετε το endpoint της υπηρεσίας μέσα στο cluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Γρήγορη εκκίνηση Inference Phi-3 με adapters

Αφού εγκατασταθεί το Kaito, μπορείτε να εκτελέσετε τις παρακάτω εντολές για να ξεκινήσετε μια inference υπηρεσία.

[Δείγμα Κώδικα Inference Phi-3 με Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Η κατάσταση του workspace μπορεί να παρακολουθηθεί εκτελώντας την παρακάτω εντολή. Όταν η στήλη WORKSPACEREADY γίνει `True`, το μοντέλο έχει αναπτυχθεί επιτυχώς.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Στη συνέχεια, μπορείτε να βρείτε το cluster ip της inference υπηρεσίας και να χρησιμοποιήσετε ένα προσωρινό pod `curl` για να δοκιμάσετε το endpoint της υπηρεσίας μέσα στο cluster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Αποποίηση Ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες αυτόματης μετάφρασης με τεχνητή νοημοσύνη. Ενώ καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη ότι οι αυτόματες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το αρχικό έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική ανθρώπινη μετάφραση. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.