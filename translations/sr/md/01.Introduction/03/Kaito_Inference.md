## Inference sa Kaitom

[Kaito](https://github.com/Azure/kaito) je operator koji automatizuje postavljanje AI/ML inferencijalnih modela u Kubernetes klaster.

Kaito se razlikuje od većine uobičajenih metoda za postavljanje modela baziranih na infrastrukturnim virtuelnim mašinama po sledećem:

- Upravljanje fajlovima modela pomoću kontejnerskih slika. Pruža se HTTP server za izvršavanje poziva za inferenciju koristeći biblioteku modela.
- Izbegavanje podešavanja parametara postavljanja za prilagođavanje GPU hardveru pružanjem unapred definisanih konfiguracija.
- Automatsko obezbeđivanje GPU čvorova na osnovu zahteva modela.
- Hostovanje velikih slika modela u javnom Microsoft Container Registry (MCR) ako licenca to dozvoljava.

Korišćenjem Kaita, radni tok za integraciju velikih AI inferencijalnih modela u Kubernetes postaje značajno pojednostavljen.

## Arhitektura

Kaito prati klasičan Kubernetes obrazac dizajna sa prilagođenim definicijama resursa (CRD) i kontrolerima. Korisnik upravlja prilagođenim resursom `workspace` koji opisuje GPU zahteve i specifikaciju za inferenciju. Kaito kontroleri automatski vrše postavljanje usklađivanjem sa prilagođenim resursom `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito arhitektura" alt="Kaito arhitektura">
</div>

Gornja slika prikazuje pregled Kaito arhitekture. Njegove glavne komponente uključuju:

- **Kontroler radnog prostora**: Usklađuje prilagođeni resurs `workspace`, kreira prilagođene resurse `machine` (objašnjeno u nastavku) za pokretanje automatskog obezbeđivanja čvorova i kreira radno opterećenje za inferenciju (`deployment` ili `statefulset`) na osnovu unapred definisanih konfiguracija modela.
- **Kontroler za obezbeđivanje čvorova**: Ime ovog kontrolera je *gpu-provisioner* u [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Koristi `machine` CRD koji potiče iz [Karpenter](https://sigs.k8s.io/karpenter) za interakciju sa kontrolerom radnog prostora. Integrisan je sa Azure Kubernetes Service (AKS) API-jima za dodavanje novih GPU čvorova u AKS klaster.
> Napomena: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je otvoren komponenta. Može se zameniti drugim kontrolerima ako podržavaju [Karpenter-core](https://sigs.k8s.io/karpenter) API-je.

## Instalacija

Molimo pogledajte uputstvo za instalaciju [ovde](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Brzi početak inferencije Phi-3
[Primer koda za inferenciju Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Status radnog prostora može se pratiti pokretanjem sledeće komande. Kada kolona WORKSPACEREADY postane `True`, model je uspešno postavljen.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Zatim, možete pronaći cluster IP inferencijalne usluge i koristiti privremeni `curl` pod za testiranje krajnje tačke usluge unutar klastera.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Brzi početak inferencije Phi-3 sa adapterima

Nakon instalacije Kaita, možete isprobati sledeće komande za pokretanje inferencijalne usluge.

[Primer koda za inferenciju Phi-3 sa adapterima](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Status radnog prostora može se pratiti pokretanjem sledeće komande. Kada kolona WORKSPACEREADY postane `True`, model je uspešno postavljen.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Zatim, možete pronaći cluster IP inferencijalne usluge i koristiti privremeni `curl` pod za testiranje krajnje tačke usluge unutar klastera.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Одрицање од одговорности**:  
Овај документ је преведен коришћењем машинских AI услуга за превођење. Иако настојимо да обезбедимо тачност, молимо вас да имате у виду да аутоматски преводи могу садржати грешке или нетачности. Оригинални документ на његовом изворном језику треба сматрати меродавним извором. За критичне информације препоручује се професионални људски превод. Не сносимо одговорност за било каква неспоразумевања или погрешна тумачења која могу произаћи из употребе овог превода.