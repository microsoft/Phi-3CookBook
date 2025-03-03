## Inference cu Kaito

[Kaito](https://github.com/Azure/kaito) este un operator care automatizează implementarea modelelor de inferență AI/ML într-un cluster Kubernetes.

Kaito are următoarele diferențieri cheie comparativ cu majoritatea metodologiilor de implementare a modelelor bazate pe infrastructuri de mașini virtuale:

- Gestionează fișierele model folosind imagini de containere. Este furnizat un server HTTP pentru a efectua apeluri de inferență utilizând biblioteca modelului.
- Evită ajustarea parametrilor de implementare pentru a se potrivi cu hardware-ul GPU prin furnizarea de configurații prestabilite.
- Provoacă automat noduri GPU pe baza cerințelor modelului.
- Găzduiește imagini de modele mari în Microsoft Container Registry (MCR) public, dacă licența permite.

Folosind Kaito, fluxul de lucru pentru integrarea modelelor mari de inferență AI în Kubernetes este mult simplificat.

## Arhitectură

Kaito urmează modelul clasic de proiectare Kubernetes bazat pe Definiții de Resurse Personalizate (CRD)/controlere. Utilizatorul gestionează o resursă personalizată `workspace` care descrie cerințele GPU și specificațiile de inferență. Controlerele Kaito vor automatiza implementarea sincronizând resursa personalizată `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Arhitectura Kaito" alt="Arhitectura Kaito">
</div>

Figura de mai sus prezintă o privire de ansamblu asupra arhitecturii Kaito. Componentele sale principale constau din:

- **Controlerul workspace-ului**: Sincronizează resursa personalizată `workspace`, creează resurse personalizate `machine` (explicate mai jos) pentru a declanșa auto-provizionarea nodurilor și creează sarcina de inferență (`deployment` sau `statefulset`) pe baza configurațiilor prestabilite ale modelului.
- **Controlerul de provizionare a nodurilor**: Numele controlerului este *gpu-provisioner* în [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Utilizează CRD-ul `machine` derivat din [Karpenter](https://sigs.k8s.io/karpenter) pentru a interacționa cu controlerul workspace-ului. Integrează API-urile Azure Kubernetes Service (AKS) pentru a adăuga noi noduri GPU în clusterul AKS.
> Notă: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) este un component open-source. Poate fi înlocuit cu alte controlere dacă acestea suportă API-urile [Karpenter-core](https://sigs.k8s.io/karpenter).

## Instalare

Consultați ghidul de instalare [aici](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Start rapid pentru inferență Phi-3
[Exemplu de cod pentru inferență Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Starea workspace-ului poate fi urmărită rulând următoarea comandă. Când coloana WORKSPACEREADY devine `True`, modelul a fost implementat cu succes.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

În continuare, se poate găsi IP-ul de cluster al serviciului de inferență și se poate folosi un pod temporar `curl` pentru a testa punctul final al serviciului din cluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Start rapid pentru inferență Phi-3 cu adaptoare

După instalarea Kaito, se pot încerca următoarele comenzi pentru a porni un serviciu de inferență.

[Exemplu de cod pentru inferență Phi-3 cu adaptoare](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Starea workspace-ului poate fi urmărită rulând următoarea comandă. Când coloana WORKSPACEREADY devine `True`, modelul a fost implementat cu succes.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

În continuare, se poate găsi IP-ul de cluster al serviciului de inferență și se poate folosi un pod temporar `curl` pentru a testa punctul final al serviciului din cluster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Declinarea responsabilității**:  
Acest document a fost tradus folosind servicii de traducere automată bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa nativă, trebuie considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru eventualele neînțelegeri sau interpretări greșite care pot apărea în urma utilizării acestei traduceri.