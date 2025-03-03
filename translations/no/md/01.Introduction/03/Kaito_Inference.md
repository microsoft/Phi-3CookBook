## Inference med Kaito 

[Kaito](https://github.com/Azure/kaito) er en operatør som automatiserer utrullingen av AI/ML-inferensmodeller i en Kubernetes-klynge.

Kaito har følgende hovedforskjeller sammenlignet med de fleste vanlige metoder for modellutrulling som er bygget på virtuelle maskin-infrastrukturer:

- Administrer modelfiler ved hjelp av containerbilder. En HTTP-server tilbys for å utføre inferenskall ved bruk av modellbiblioteket.
- Unngå justering av utrullingsparametere for å passe til GPU-maskinvare ved å tilby forhåndsdefinerte konfigurasjoner.
- Automatisk klargjøring av GPU-noder basert på modellens krav.
- Host store modellbilder i den offentlige Microsoft Container Registry (MCR) dersom lisensen tillater det.

Med Kaito blir arbeidsflyten for å onboarde store AI-inferensmodeller i Kubernetes betydelig forenklet.


## Arkitektur

Kaito følger det klassiske Kubernetes Custom Resource Definition (CRD)/controller-designmønsteret. Brukeren administrerer en `workspace`-ressurs som beskriver GPU-kravene og spesifikasjonen for inferensen. Kaito-kontrollerne automatiserer utrullingen ved å synkronisere `workspace`-ressursen.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Figuren ovenfor viser en oversikt over Kaito-arkitekturen. Hovedkomponentene består av:

- **Workspace controller**: Synkroniserer `workspace`-ressursen, oppretter `machine` (forklart nedenfor) ressurser for å utløse automatisk klargjøring av noder, og oppretter inferensarbeidslasten (`deployment` eller `statefulset`) basert på forhåndsdefinerte modellkonfigurasjoner.
- **Node provisioner controller**: Kontrollerens navn er *gpu-provisioner* i [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Den bruker `machine`-CRD fra [Karpenter](https://sigs.k8s.io/karpenter) for å kommunisere med workspace controller. Den integreres med Azure Kubernetes Service (AKS)-APIer for å legge til nye GPU-noder i AKS-klyngen.  
> Merk: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) er en åpen kildekode-komponent. Den kan erstattes av andre kontrollere dersom de støtter [Karpenter-core](https://sigs.k8s.io/karpenter)-APIer.

## Installasjon

Se installasjonsveiledningen [her](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Hurtigstart: Inferens Phi-3
[Eksempelkode for inferens Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Statusen til arbeidsområdet kan spores ved å kjøre følgende kommando. Når kolonnen WORKSPACEREADY viser `True`, er modellen vellykket utrullet.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Deretter kan du finne inferenstjenestens cluster-IP og bruke en midlertidig `curl`-pod for å teste tjenesteendepunktet i klyngen.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Hurtigstart: Inferens Phi-3 med adaptere

Etter å ha installert Kaito, kan du prøve følgende kommandoer for å starte en inferenstjeneste.

[Eksempelkode for inferens Phi-3 med adaptere](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Statusen til arbeidsområdet kan spores ved å kjøre følgende kommando. Når kolonnen WORKSPACEREADY viser `True`, er modellen vellykket utrullet.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Deretter kan du finne inferenstjenestens cluster-IP og bruke en midlertidig `curl`-pod for å teste tjenesteendepunktet i klyngen.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved bruk av maskinbaserte AI-oversettelsestjenester. Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør anses som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for eventuelle misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.