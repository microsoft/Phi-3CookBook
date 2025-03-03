## Inference z Kaito

[Kaito](https://github.com/Azure/kaito) je operator, ki avtomatizira uvajanje AI/ML inferenčnih modelov v Kubernetes grozd.

Kaito se v primerjavi z večino uveljavljenih metodologij za uvajanje modelov, ki temeljijo na infrastrukturi virtualnih strojev, razlikuje v naslednjih ključnih točkah:

- Upravljanje datotek modelov s pomočjo slik kontejnerjev. Na voljo je http strežnik za izvajanje inferenčnih klicev z uporabo knjižnice modelov.
- Izogibanje prilagajanju parametrov uvajanja za prilagoditev GPU strojni opremi z uporabo vnaprej določenih konfiguracij.
- Samodejno zagotavljanje GPU vozlišč glede na zahteve modela.
- Gostovanje velikih slik modelov v javnem Microsoft Container Registry (MCR), če licenca to dovoljuje.

S Kaito je delovni proces uvajanja velikih AI inferenčnih modelov v Kubernetes bistveno poenostavljen.

## Arhitektura

Kaito sledi klasičnemu vzorcu zasnove Kubernetes Custom Resource Definition (CRD)/kontrolor. Uporabnik upravlja `workspace` prilagojen vir, ki opisuje zahteve za GPU in specifikacijo inferenc. Kaito kontrolorji bodo avtomatizirali uvajanje z usklajevanjem prilagojenega vira `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito arhitektura" alt="Kaito arhitektura">
</div>

Zgornja slika prikazuje pregled arhitekture Kaito. Njegove glavne komponente so:

- **Workspace kontrolor**: Usklajuje prilagojen vir `workspace`, ustvarja prilagojene vire `machine` (pojasnjeni spodaj) za sprožitev samodejnega zagotavljanja vozlišč in na podlagi vnaprej določenih konfiguracij modela ustvarja inferenčno delovno obremenitev (`deployment` ali `statefulset`).
- **Node provisioner kontrolor**: Ime tega kontrolorja je *gpu-provisioner* v [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Uporablja `machine` CRD, ki izhaja iz [Karpenter](https://sigs.k8s.io/karpenter), za interakcijo z Workspace kontrolorjem. Integrira se z API-ji Azure Kubernetes Service (AKS) za dodajanje novih GPU vozlišč v AKS grozd.
> Opomba: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je odprtokodna komponenta. Lahko ga nadomestite z drugimi kontrolorji, če podpirajo API-je [Karpenter-core](https://sigs.k8s.io/karpenter).

## Namestitev

Navodila za namestitev najdete [tukaj](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Hitri začetek Inferenca Phi-3
[Primer kode Inferenca Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Stanje delovnega prostora lahko spremljate z izvajanjem naslednjega ukaza. Ko stolpec WORKSPACEREADY postane `True`, je bil model uspešno uveden.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Nato lahko poiščete cluster ip inferenčne storitve in uporabite začasni `curl` pod za testiranje končne točke storitve v grozdu.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Hitri začetek Inferenca Phi-3 z adapterji

Po namestitvi Kaito lahko zaženete naslednje ukaze za zagon inferenčne storitve.

[Primer kode Inferenca Phi-3 z adapterji](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Stanje delovnega prostora lahko spremljate z izvajanjem naslednjega ukaza. Ko stolpec WORKSPACEREADY postane `True`, je bil model uspešno uveden.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Nato lahko poiščete cluster ip inferenčne storitve in uporabite začasni `curl` pod za testiranje končne točke storitve v grozdu.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Omejitev odgovornosti**:  
Ta dokument je bil preveden z uporabo storitev strojnega prevajanja na osnovi umetne inteligence. Čeprav si prizadevamo za natančnost, vas opozarjamo, da lahko avtomatizirani prevodi vsebujejo napake ali netočnosti. Izvirni dokument v svojem maternem jeziku je treba obravnavati kot avtoritativni vir. Za ključne informacije priporočamo profesionalni človeški prevod. Ne prevzemamo odgovornosti za morebitne nesporazume ali napačne razlage, ki izhajajo iz uporabe tega prevoda.