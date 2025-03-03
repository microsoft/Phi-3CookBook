## Fine-Tuning με το Kaito 

[Kaito](https://github.com/Azure/kaito) είναι ένας operator που αυτοματοποιεί την ανάπτυξη μοντέλων AI/ML inference σε ένα Kubernetes cluster.

Το Kaito προσφέρει τις εξής βασικές διαφοροποιήσεις σε σύγκριση με τις περισσότερες παραδοσιακές μεθόδους ανάπτυξης μοντέλων που βασίζονται σε υποδομές εικονικών μηχανών:

- Διαχείριση αρχείων μοντέλων χρησιμοποιώντας container images. Παρέχεται ένας http server για την εκτέλεση inference κλήσεων μέσω της βιβλιοθήκης του μοντέλου.
- Αποφυγή ρύθμισης παραμέτρων ανάπτυξης για την προσαρμογή σε GPU hardware με τη χρήση προκαθορισμένων ρυθμίσεων.
- Αυτόματη προσθήκη GPU nodes με βάση τις απαιτήσεις του μοντέλου.
- Φιλοξενία μεγάλων εικόνων μοντέλων στο δημόσιο Microsoft Container Registry (MCR), εφόσον το επιτρέπει η άδεια χρήσης.

Με το Kaito, η διαδικασία ενσωμάτωσης μεγάλων μοντέλων AI inference στο Kubernetes γίνεται πολύ πιο απλή.


## Αρχιτεκτονική

Το Kaito ακολουθεί το κλασικό σχεδιαστικό πρότυπο Custom Resource Definition (CRD)/controller του Kubernetes. Ο χρήστης διαχειρίζεται έναν `workspace` custom resource που περιγράφει τις απαιτήσεις GPU και τις προδιαγραφές inference. Οι controllers του Kaito αυτοματοποιούν την ανάπτυξη συγχρονίζοντας τον `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Η παραπάνω εικόνα παρουσιάζει μια γενική επισκόπηση της αρχιτεκτονικής του Kaito. Τα κύρια συστατικά του περιλαμβάνουν:

- **Workspace controller**: Συγχρονίζει τον `workspace` custom resource, δημιουργεί `machine` (επεξηγείται παρακάτω) custom resources για να ενεργοποιήσει την αυτόματη προσθήκη nodes, και δημιουργεί το inference workload (`deployment` ή `statefulset`) βασισμένο στις προκαθορισμένες ρυθμίσεις του μοντέλου.
- **Node provisioner controller**: Το όνομα του controller είναι *gpu-provisioner* στο [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Χρησιμοποιεί το `machine` CRD που προέρχεται από το [Karpenter](https://sigs.k8s.io/karpenter) για να αλληλεπιδράσει με τον workspace controller. Ενσωματώνεται με τα APIs του Azure Kubernetes Service (AKS) για να προσθέτει νέους GPU nodes στο AKS cluster. 
> Σημείωση: Το [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) είναι ένα open source component. Μπορεί να αντικατασταθεί από άλλους controllers, εφόσον υποστηρίζουν τα APIs του [Karpenter-core](https://sigs.k8s.io/karpenter).

## Επισκόπηση βίντεο 
[Παρακολουθήστε το Demo του Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## Εγκατάσταση

Μπορείτε να βρείτε οδηγίες εγκατάστασης [εδώ](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Γρήγορη εκκίνηση

Αφού εγκαταστήσετε το Kaito, μπορείτε να δοκιμάσετε τις παρακάτω εντολές για να ξεκινήσετε μια υπηρεσία fine-tuning.

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

Η κατάσταση του workspace μπορεί να παρακολουθηθεί εκτελώντας την παρακάτω εντολή. Όταν η στήλη WORKSPACEREADY γίνει `True`, το μοντέλο έχει αναπτυχθεί με επιτυχία.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Στη συνέχεια, μπορείτε να βρείτε το cluster ip της inference υπηρεσίας και να χρησιμοποιήσετε ένα προσωρινό `curl` pod για να δοκιμάσετε το endpoint της υπηρεσίας μέσα στο cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Αποποίηση ευθύνης**:  
Αυτό το έγγραφο έχει μεταφραστεί χρησιμοποιώντας υπηρεσίες μετάφρασης που βασίζονται σε τεχνητή νοημοσύνη. Παρόλο που καταβάλλουμε προσπάθειες για ακρίβεια, παρακαλούμε να έχετε υπόψη σας ότι οι αυτοματοποιημένες μεταφράσεις ενδέχεται να περιέχουν λάθη ή ανακρίβειες. Το αρχικό έγγραφο στη μητρική του γλώσσα θα πρέπει να θεωρείται η αυθεντική πηγή. Για κρίσιμες πληροφορίες, συνιστάται επαγγελματική μετάφραση από άνθρωπο. Δεν φέρουμε ευθύνη για τυχόν παρεξηγήσεις ή εσφαλμένες ερμηνείες που προκύπτουν από τη χρήση αυτής της μετάφρασης.