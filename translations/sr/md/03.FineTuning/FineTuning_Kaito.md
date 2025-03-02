## Fino podešavanje sa Kaito

[Kaito](https://github.com/Azure/kaito) je operator koji automatizuje implementaciju AI/ML modela za inferenciju u Kubernetes klasteru.

Kaito se razlikuje od većine standardnih metoda za implementaciju modela zasnovanih na infrastrukturi virtuelnih mašina u sledećem:

- Upravljanje fajlovima modela pomoću kontejnerskih slika. Obezbeđen je HTTP server za pozivanje inferencije koristeći biblioteku modela.
- Izbegavanje podešavanja parametara implementacije kako bi odgovarali GPU hardveru pružanjem unapred definisanih konfiguracija.
- Automatsko dodavanje GPU čvorova na osnovu zahteva modela.
- Hostovanje velikih slika modela u javnom Microsoft Container Registry (MCR) ako to dozvoljava licenca.

Koristeći Kaito, proces uvođenja velikih AI modela za inferenciju u Kubernetes značajno je pojednostavljen.

## Arhitektura

Kaito prati klasičan dizajn obrazaca Custom Resource Definition (CRD)/kontrolera u Kubernetesu. Korisnik upravlja resursom `workspace` koji opisuje zahteve za GPU i specifikaciju za inferenciju. Kaito kontroleri automatizuju implementaciju usklađivanjem resursa `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito arhitektura" alt="Kaito arhitektura">
</div>

Gornja slika prikazuje pregled Kaito arhitekture. Njegove glavne komponente uključuju:

- **Kontroler radnog prostora**: Usaglašava resurs `workspace`, kreira prilagođene resurse `machine` (objašnjeno u nastavku) kako bi pokrenuo automatsko dodavanje čvorova i kreira radno opterećenje za inferenciju (`deployment` ili `statefulset`) na osnovu unapred definisanih konfiguracija modela.
- **Kontroler za dodavanje čvorova**: Ime ovog kontrolera je *gpu-provisioner* u [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Koristi CRD `machine` koji potiče iz [Karpenter](https://sigs.k8s.io/karpenter) za interakciju sa kontrolerom radnog prostora. Integreše se sa Azure Kubernetes Service (AKS) API-jem kako bi dodao nove GPU čvorove u AKS klaster.  
> Napomena: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je komponenta otvorenog koda. Može biti zamenjena drugim kontrolerima ako podržavaju API-je [Karpenter-core](https://sigs.k8s.io/karpenter).

## Pregledni video 
[Pogledajte Kaito demonstraciju](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Instalacija

Molimo vas da proverite uputstvo za instalaciju [ovde](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Brzi početak

Nakon instalacije Kaito-a, možete isprobati sledeće komande za pokretanje servisa za fino podešavanje.

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

Status radnog prostora može se pratiti pokretanjem sledeće komande. Kada kolona WORKSPACEREADY postane `True`, model je uspešno implementiran.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Zatim možete pronaći klasterski IP servisa za inferenciju i koristiti privremeni `curl` pod za testiranje krajnje tačke servisa unutar klastera.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Одрицање од одговорности**:  
Овај документ је преведен помоћу услуга машинског превођења заснованих на вештачкој интелигенцији. Иако тежимо прецизности, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на изворном језику треба сматрати ауторитативним извором. За критичне информације препоручује се професионални људски превод. Не сносимо одговорност за било каква неспоразумевања или погрешна тумачења која могу произаћи из коришћења овог превода.