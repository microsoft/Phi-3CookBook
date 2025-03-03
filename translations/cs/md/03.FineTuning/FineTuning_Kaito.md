## Jemné ladění s Kaito

[Kaito](https://github.com/Azure/kaito) je operátor, který automatizuje nasazení modelů pro AI/ML inference v Kubernetes clusteru.

Kaito se odlišuje od většiny běžných metodik nasazení modelů, které jsou postaveny na infrastruktuře virtuálních strojů, následujícími klíčovými vlastnostmi:

- Správa souborů modelů pomocí kontejnerových obrazů. Poskytuje HTTP server pro volání inference pomocí knihovny modelů.
- Vyhýbá se ladění parametrů nasazení pro přizpůsobení GPU hardwaru díky přednastaveným konfiguracím.
- Automatické zajištění GPU uzlů na základě požadavků modelu.
- Hostování velkých obrazů modelů ve veřejném Microsoft Container Registry (MCR), pokud to licence umožňuje.

Díky Kaito je workflow nasazení velkých AI inference modelů v Kubernetes výrazně zjednodušený.

## Architektura

Kaito využívá klasický návrhový vzor Custom Resource Definition (CRD)/controller v Kubernetes. Uživatel spravuje vlastní prostředek `workspace`, který popisuje požadavky na GPU a specifikaci inference. Kaito controllery automatizují nasazení tím, že synchronizují vlastní prostředek `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Výše uvedený obrázek představuje přehled architektury Kaito. Hlavní komponenty zahrnují:

- **Workspace controller**: Synchronizuje vlastní prostředek `workspace`, vytváří vlastní prostředky `machine` (vysvětlené níže) pro spuštění automatického zajištění uzlů a vytváří inference workload (`deployment` nebo `statefulset`) na základě přednastavených konfigurací modelu.
- **Node provisioner controller**: Tento controller se v [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) nazývá *gpu-provisioner*. Používá `machine` CRD pocházející z [Karpenter](https://sigs.k8s.io/karpenter) pro interakci s workspace controllerem. Integruje se s API Azure Kubernetes Service (AKS) pro přidání nových GPU uzlů do AKS clusteru.  
> Poznámka: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) je open source komponenta. Může být nahrazen jinými controllery, pokud podporují API [Karpenter-core](https://sigs.k8s.io/karpenter).

## Přehledové video 
[Podívejte se na demo Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## Instalace

Pokyny k instalaci naleznete [zde](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Rychlý start

Po instalaci Kaito můžete použít následující příkazy k zahájení služby jemného ladění.

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

Stav workspace lze sledovat spuštěním následujícího příkazu. Jakmile se sloupec WORKSPACEREADY změní na `True`, model byl úspěšně nasazen.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Dále můžete zjistit clusterovou IP inference služby a použít dočasný `curl` pod pro otestování koncového bodu služby v clusteru.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Prohlášení**:  
Tento dokument byl přeložen pomocí strojových překladových služeb AI. Přestože se snažíme o přesnost, mějte prosím na paměti, že automatizované překlady mohou obsahovat chyby nebo nepřesnosti. Původní dokument v jeho rodném jazyce by měl být považován za závazný zdroj. Pro důležité informace doporučujeme profesionální lidský překlad. Nenese zodpovědnost za jakékoli nedorozumění nebo nesprávné interpretace vyplývající z použití tohoto překladu.