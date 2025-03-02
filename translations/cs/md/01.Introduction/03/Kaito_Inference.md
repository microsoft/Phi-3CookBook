## Inference s Kaito

[Kaito](https://github.com/Azure/kaito) je operátor, který automatizuje nasazení AI/ML inferenčních modelů v Kubernetes clusteru.

Kaito se odlišuje od většiny běžných metod nasazení modelů postavených na infrastruktuře virtuálních strojů následujícími klíčovými způsoby:

- Správa souborů modelů pomocí kontejnerových obrazů. Poskytuje HTTP server pro volání inference pomocí knihovny modelu.
- Vyhýbá se ladění parametrů nasazení pro přizpůsobení GPU hardwaru díky přednastaveným konfiguracím.
- Automaticky zajišťuje GPU uzly na základě požadavků modelu.
- Hostuje velké obrazy modelů v veřejném Microsoft Container Registry (MCR), pokud to licence umožňuje.

Použitím Kaito je workflow nasazení velkých AI inferenčních modelů v Kubernetes výrazně zjednodušen.


## Architektura

Kaito využívá klasický designový vzor Kubernetes Custom Resource Definition (CRD)/controller. Uživatel spravuje vlastní prostředek `workspace`, který popisuje požadavky na GPU a specifikaci inference. Kaito controllery automatizují nasazení synchronizací vlastního prostředku `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Architektura Kaito" alt="Architektura Kaito">
</div>

Obrázek výše ukazuje přehled architektury Kaito. Mezi jeho hlavní komponenty patří:

- **Workspace controller**: Synchronizuje vlastní prostředek `workspace`, vytváří vlastní prostředky `machine` (vysvětleno níže) pro spuštění automatického zajištění uzlů a vytváří inferenční úlohu (`deployment` nebo `statefulset`) na základě přednastavených konfigurací modelu.
- **Node provisioner controller**: Tento controller se nazývá *gpu-provisioner* v [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Používá CRD `machine`, které pochází z [Karpenter](https://sigs.k8s.io/karpenter), aby komunikoval s workspace controllerem. Integruje se s Azure Kubernetes Service (AKS) API pro přidání nových GPU uzlů do AKS clusteru.  
> Poznámka: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je open-source komponenta. Lze ji nahradit jinými controllery, pokud podporují API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Instalace

Podívejte se na návod k instalaci [zde](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Rychlý start Inference Phi-3
[Ukázkový kód pro Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Stav pracovního prostoru lze sledovat spuštěním následujícího příkazu. Když se sloupec WORKSPACEREADY změní na `True`, model byl úspěšně nasazen.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Dále lze najít cluster IP inferenční služby a použít dočasný `curl` pod pro otestování koncového bodu služby v clusteru.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Rychlý start Inference Phi-3 s adaptéry

Po instalaci Kaito lze spustit následující příkazy pro spuštění inferenční služby.

[Ukázkový kód pro Inference Phi-3 s adaptéry](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Stav pracovního prostoru lze sledovat spuštěním následujícího příkazu. Když se sloupec WORKSPACEREADY změní na `True`, model byl úspěšně nasazen.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Dále lze najít cluster IP inferenční služby a použít dočasný `curl` pod pro otestování koncového bodu služby v clusteru.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Prohlášení**:  
Tento dokument byl přeložen pomocí strojových AI překladatelských služeb. Přestože usilujeme o přesnost, vezměte prosím na vědomí, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho původním jazyce by měl být považován za závazný zdroj. Pro kritické informace se doporučuje profesionální lidský překlad. Neodpovídáme za žádná nedorozumění nebo mylné interpretace vyplývající z použití tohoto překladu.