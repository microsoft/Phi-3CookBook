## Fine-Tuning cu Kaito

[Kaito](https://github.com/Azure/kaito) este un operator care automatizează implementarea modelelor de inferență AI/ML într-un cluster Kubernetes.

Kaito are următoarele diferențieri cheie comparativ cu majoritatea metodologiilor mainstream de implementare a modelelor, construite pe infrastructuri de mașini virtuale:

- Gestionează fișierele modelului utilizând imagini container. Este oferit un server http pentru a efectua apeluri de inferență folosind biblioteca modelului.
- Evită ajustarea parametrilor de implementare pentru a se potrivi cu hardware-ul GPU, oferind configurații prestabilite.
- Asigură automat noduri GPU pe baza cerințelor modelului.
- Găzduiește imagini mari ale modelelor în Microsoft Container Registry (MCR) public, dacă licența permite acest lucru.

Folosind Kaito, fluxul de lucru pentru integrarea modelelor mari de inferență AI în Kubernetes este considerabil simplificat.

## Arhitectură

Kaito urmează modelul clasic de design bazat pe Definiția Resursei Personalizate (CRD)/controller din Kubernetes. Utilizatorul gestionează o resursă personalizată `workspace` care descrie cerințele GPU și specificațiile de inferență. Controllerele Kaito automatizează implementarea prin reconcilierea resursei personalizate `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Arhitectura Kaito" alt="Arhitectura Kaito">
</div>

Figura de mai sus prezintă o privire de ansamblu asupra arhitecturii Kaito. Componentele sale principale includ:

- **Controller-ul Workspace**: Reconcilierea resursei personalizate `workspace`, crearea resurselor personalizate `machine` (explicate mai jos) pentru a declanșa aprovizionarea automată a nodurilor și crearea sarcinii de inferență (`deployment` sau `statefulset`) pe baza configurațiilor prestabilite ale modelului.
- **Controller-ul Node Provisioner**: Numele acestui controller este *gpu-provisioner* în [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Acesta utilizează CRD-ul `machine` derivat din [Karpenter](https://sigs.k8s.io/karpenter) pentru a interacționa cu controller-ul Workspace. Se integrează cu API-urile Azure Kubernetes Service (AKS) pentru a adăuga noi noduri GPU în clusterul AKS. 
> Notă: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) este un component open-source. Poate fi înlocuit de alte controllere dacă acestea suportă API-urile [Karpenter-core](https://sigs.k8s.io/karpenter).

## Videoclip de prezentare
[Urmărește demo-ul Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## Instalare

Consultați ghidul de instalare [aici](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Ghid rapid

După instalarea Kaito, se pot utiliza următoarele comenzi pentru a începe un serviciu de fine-tuning.

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

Starea workspace-ului poate fi urmărită rulând următoarea comandă. Când coloana WORKSPACEREADY devine `True`, modelul a fost implementat cu succes.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Apoi, se poate găsi adresa IP a serviciului de inferență din cluster și se poate utiliza un pod temporar `curl` pentru a testa endpoint-ul serviciului în cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Declinare responsabilitate**:  
Acest document a fost tradus folosind servicii de traducere automată bazate pe inteligență artificială. Deși ne străduim să asigurăm acuratețea, vă rugăm să rețineți că traducerile automate pot conține erori sau inexactități. Documentul original, în limba sa maternă, ar trebui considerat sursa autoritară. Pentru informații critice, se recomandă traducerea profesională realizată de un specialist uman. Nu ne asumăm răspunderea pentru neînțelegeri sau interpretări greșite care pot apărea din utilizarea acestei traduceri.