## Inference med Kaito 

[Kaito](https://github.com/Azure/kaito) er en operator, der automatiserer udrulning af AI/ML-inferensmodeller i en Kubernetes-klynge.

Kaito adskiller sig på følgende måder fra de fleste almindelige metoder til modeludrulning, som er bygget oven på virtuelle maskine-infrastrukturer:

- Håndter modelfiler ved hjælp af containerbilleder. En HTTP-server stilles til rådighed for at udføre inferenskald ved brug af modellens bibliotek.
- Undgå at tilpasse udrulningsparametre til GPU-hardware ved at tilbyde forudindstillede konfigurationer.
- Automatisk provisionering af GPU-noder baseret på modellens krav.
- Host store modelbilleder i den offentlige Microsoft Container Registry (MCR), hvis licensen tillader det.

Med Kaito bliver arbejdsprocessen med at onboarde store AI-inferensmodeller i Kubernetes betydeligt forenklet.

## Arkitektur

Kaito følger det klassiske Kubernetes-designmønster for Custom Resource Definition (CRD)/controller. Brugeren administrerer en `workspace`-ressource, som beskriver GPU-krav og inferensspecifikationer. Kaito-controllere automatiserer udrulningen ved at synkronisere `workspace`-ressourcen.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Figuren ovenfor viser en oversigt over Kaitos arkitektur. Dens hovedkomponenter består af:

- **Workspace-controller**: Den synkroniserer `workspace`-ressourcen, opretter `machine`-ressourcer (forklaret nedenfor) for at starte automatisk provisionering af noder og opretter inferensarbejdsbyrder (`deployment` eller `statefulset`) baseret på modellens forudindstillinger.
- **Node provisioner-controller**: Controllerens navn er *gpu-provisioner* i [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Den bruger `machine` CRD, som stammer fra [Karpenter](https://sigs.k8s.io/karpenter), til at interagere med workspace-controlleren. Den integreres med Azure Kubernetes Service (AKS) API'er for at tilføje nye GPU-noder til AKS-klyngen. 
> Bemærk: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) er en open source-komponent. Den kan erstattes af andre controllere, hvis de understøtter [Karpenter-core](https://sigs.k8s.io/karpenter) API'er.

## Installation

Du kan finde installationsvejledningen [her](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Kom godt i gang med Inferens Phi-3
[Eksempelkode til Inferens Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Workspace-status kan følges ved at køre følgende kommando. Når WORKSPACEREADY-kolonnen bliver `True`, er modellen blevet udrullet med succes.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Derefter kan man finde inferenstjenestens cluster-ip og bruge en midlertidig `curl`-pod til at teste tjenestens endpoint i klyngen.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Kom godt i gang med Inferens Phi-3 med adapters

Efter installation af Kaito kan man prøve følgende kommandoer for at starte en inferenstjeneste.

[Eksempelkode til Inferens Phi-3 med Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Workspace-status kan følges ved at køre følgende kommando. Når WORKSPACEREADY-kolonnen bliver `True`, er modellen blevet udrullet med succes.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Derefter kan man finde inferenstjenestens cluster-ip og bruge en midlertidig `curl`-pod til at teste tjenestens endpoint i klyngen.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på nøjagtighed, skal du være opmærksom på, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os intet ansvar for misforståelser eller fejltolkninger, der opstår som følge af brugen af denne oversættelse.