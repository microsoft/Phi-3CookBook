## Inferencia s Kaito 

[Kaito](https://github.com/Azure/kaito) je operátor, ktorý automatizuje nasadenie modelov AI/ML inferencie v Kubernetes klustri.

Kaito má nasledujúce kľúčové odlišnosti v porovnaní s väčšinou bežných metodológií nasadzovania modelov postavených na infraštruktúre virtuálnych strojov:

- Spravuje súbory modelov pomocou kontajnerových obrazov. Poskytuje http server na vykonávanie inferenčných volaní pomocou knižnice modelu.
- Vyhýba sa ladenie parametrov nasadenia na prispôsobenie GPU hardvéru tým, že ponúka prednastavené konfigurácie.
- Automaticky pridáva GPU uzly na základe požiadaviek modelu.
- Hosťuje veľké obrazy modelov v verejnom Microsoft Container Registry (MCR), ak to licencia umožňuje.

Pomocou Kaito je pracovný postup zavádzania veľkých AI inferenčných modelov v Kubernetes výrazne zjednodušený.

## Architektúra

Kaito nasleduje klasický dizajnový vzor Kubernetes Custom Resource Definition (CRD)/controller. Používateľ spravuje vlastný zdroj `workspace`, ktorý popisuje požiadavky na GPU a špecifikáciu inferencie. Kaito kontroléry automatizujú nasadenie synchronizáciou vlastného zdroja `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Architektúra Kaito" alt="Architektúra Kaito">
</div>

Vyššie uvedený obrázok predstavuje prehľad architektúry Kaito. Hlavné komponenty zahŕňajú:

- **Workspace controller**: Synchronizuje vlastný zdroj `workspace`, vytvára vlastné zdroje `machine` (vysvetlené nižšie) na spustenie automatického pridávania uzlov a vytvára inferenčné pracovné zaťaženie (`deployment` alebo `statefulset`) na základe prednastavených konfigurácií modelu.
- **Node provisioner controller**: Názov tohto kontroléra je *gpu-provisioner* v [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Používa CRD `machine` pochádzajúce z [Karpenter](https://sigs.k8s.io/karpenter) na interakciu s workspace controllerom. Integruje sa s Azure Kubernetes Service (AKS) API na pridávanie nových GPU uzlov do AKS klustra. 
> Poznámka: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je open-source komponent. Môže byť nahradený inými kontrolérmi, ak podporujú API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Inštalácia

Prosím, pozrite si pokyny na inštaláciu [tu](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Rýchly štart inferencie Phi-3
[Vzorka kódu pre inferenciu Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Stav pracovného priestoru môžete sledovať spustením nasledujúceho príkazu. Keď sa stĺpec WORKSPACEREADY zmení na `True`, model bol úspešne nasadený.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Ďalej môžete nájsť cluster ip inferenčnej služby a použiť dočasný `curl` pod na testovanie koncového bodu služby v klustri.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Rýchly štart inferencie Phi-3 s adaptérmi

Po inštalácii Kaito môžete skúsiť nasledujúce príkazy na spustenie inferenčnej služby.

[Vzorka kódu pre inferenciu Phi-3 s adaptérmi](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Stav pracovného priestoru môžete sledovať spustením nasledujúceho príkazu. Keď sa stĺpec WORKSPACEREADY zmení na `True`, model bol úspešne nasadený.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Ďalej môžete nájsť cluster ip inferenčnej služby a použiť dočasný `curl` pod na testovanie koncového bodu služby v klustri.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Upozornenie**:  
Tento dokument bol preložený pomocou strojových prekladateľských služieb založených na umelej inteligencii. Aj keď sa snažíme o presnosť, prosím, majte na pamäti, že automatické preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za autoritatívny zdroj. Pre kritické informácie sa odporúča profesionálny preklad od človeka. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.