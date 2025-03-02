## Doladenie s Kaito

[Kaito](https://github.com/Azure/kaito) je operátor, ktorý automatizuje nasadenie modelov AI/ML inferencie v Kubernetes klastri.

Kaito má nasledujúce kľúčové rozdiely v porovnaní s väčšinou bežných metodológií nasadzovania modelov postavených na infraštruktúrach virtuálnych strojov:

- Správa súborov modelov pomocou kontajnerových obrazov. Poskytuje HTTP server na vykonávanie inferenčných volaní pomocou knižnice modelu.
- Vyhýbanie sa ladenia parametrov nasadenia pre prispôsobenie GPU hardvéru vďaka prednastaveným konfiguráciám.
- Automatické prideľovanie GPU uzlov na základe požiadaviek modelu.
- Hosťovanie veľkých obrazov modelov vo verejnom Microsoft Container Registry (MCR), ak to licencia umožňuje.

Použitím Kaito je pracovný postup onboardingu veľkých AI inferenčných modelov v Kubernetes výrazne zjednodušený.

## Architektúra

Kaito nasleduje klasický dizajnový vzor Kubernetes Custom Resource Definition (CRD)/kontrolér. Používateľ spravuje vlastný zdroj `workspace`, ktorý popisuje požiadavky na GPU a špecifikáciu inferencie. Kaito kontroléry automatizujú nasadenie synchronizáciou vlastného zdroja `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architektúra" alt="Kaito architektúra">
</div>

Vyššie uvedený obrázok predstavuje prehľad architektúry Kaito. Jeho hlavné komponenty zahŕňajú:

- **Workspace controller**: Synchronizuje vlastný zdroj `workspace`, vytvára vlastné zdroje `machine` (vysvetlené nižšie) na spustenie automatického prideľovania uzlov a vytvára inferenčné pracovné zaťaženie (`deployment` alebo `statefulset`) na základe prednastavených konfigurácií modelu.
- **Node provisioner controller**: Názov tohto kontroléra je *gpu-provisioner* v [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Používa CRD `machine` pochádzajúce z [Karpenter](https://sigs.k8s.io/karpenter) na interakciu s workspace kontrolérom. Integruje sa s API Azure Kubernetes Service (AKS) na pridanie nových GPU uzlov do AKS klastra. 
> Poznámka: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je open-source komponent. Môže byť nahradený inými kontrolérmi, ak podporujú API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Prehľadové video 
[Pozrite si demo Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## Inštalácia

Pokyny na inštaláciu nájdete [tu](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Rýchly štart

Po inštalácii Kaito môžete použiť nasledujúce príkazy na spustenie služby doladenia.

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

Stav pracovného priestoru môžete sledovať spustením nasledujúceho príkazu. Keď sa stĺpec WORKSPACEREADY zmení na `True`, model bol úspešne nasadený.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Následne môžete nájsť clusterovú IP adresu inferenčnej služby a použiť dočasný `curl` pod na testovanie koncového bodu služby v klastri.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Upozornenie**:  
Tento dokument bol preložený pomocou služieb strojového prekladu s využitím umelej inteligencie. Hoci sa snažíme o presnosť, upozorňujeme, že automatizované preklady môžu obsahovať chyby alebo nepresnosti. Pôvodný dokument v jeho pôvodnom jazyku by mal byť považovaný za záväzný zdroj. Pre dôležité informácie odporúčame profesionálny ľudský preklad. Nenesieme zodpovednosť za akékoľvek nedorozumenia alebo nesprávne interpretácie vyplývajúce z použitia tohto prekladu.