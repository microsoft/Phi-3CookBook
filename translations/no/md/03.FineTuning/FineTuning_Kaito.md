## Finjustering med Kaito

[Kaito](https://github.com/Azure/kaito) er en operatør som automatiserer distribusjonen av AI/ML-inferansemodeller i en Kubernetes-klynge.

Kaito skiller seg ut fra mange av de vanlige metodene for modellutplassering som er bygget på virtuelle maskin-infrastrukturer, på følgende måter:

- Administrer modelfiler ved hjelp av containerbilder. En HTTP-server tilbys for å utføre inferensekall ved hjelp av modellbiblioteket.
- Unngå å måtte justere distribusjonsparametere for å tilpasse GPU-maskinvare ved å tilby forhåndsdefinerte konfigurasjoner.
- Automatisk tildeling av GPU-noder basert på modellkrav.
- Hoste store modellbilder i Microsoft Container Registry (MCR) offentlig, dersom lisensen tillater det.

Ved å bruke Kaito blir arbeidsflyten for å onboarde store AI-inferansemodeller i Kubernetes betydelig forenklet.

## Arkitektur

Kaito følger det klassiske Kubernetes Custom Resource Definition (CRD)/controller-designmønsteret. Brukeren administrerer en `workspace` custom resource som beskriver GPU-kravene og spesifikasjonen for inferensen. Kaito-kontrollerne automatiserer distribusjonen ved å samkjøre `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Figuren ovenfor viser en oversikt over Kaito-arkitekturen. Hovedkomponentene består av:

- **Workspace controller**: Denne samkjører `workspace` custom resource, oppretter `machine` (forklart nedenfor) custom resources for å trigge automatisk tildeling av noder, og oppretter inferansearbeidsmengden (`deployment` eller `statefulset`) basert på modellens forhåndsdefinerte konfigurasjoner.
- **Node provisioner controller**: Kontrollerens navn er *gpu-provisioner* i [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Den bruker `machine` CRD fra [Karpenter](https://sigs.k8s.io/karpenter) for å samhandle med workspace controller. Den integreres med Azure Kubernetes Service (AKS)-APIer for å legge til nye GPU-noder i AKS-klyngen.
> Merk: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) er en åpen kildekode-komponent. Den kan erstattes av andre kontrollere, så lenge de støtter [Karpenter-core](https://sigs.k8s.io/karpenter)-APIer.

## Oversiktsvideo 
[Se Kaito-demoen](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## Installasjon

Se installasjonsveiledningen [her](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Kom i gang

Etter at Kaito er installert, kan du prøve følgende kommandoer for å starte en finjusteringstjeneste.

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

Statusen til arbeidsområdet kan spores ved å kjøre følgende kommando. Når kolonnen WORKSPACEREADY viser `True`, har modellen blitt distribuert med suksess.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Deretter kan du finne klynge-IP-en til inferansetjenesten og bruke en midlertidig `curl`-pod for å teste tjenesteendepunktet i klyngen.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Ansvarsfraskrivelse**:  
Dette dokumentet er oversatt ved hjelp av maskinbaserte AI-oversettelsestjenester. Selv om vi tilstreber nøyaktighet, vennligst vær oppmerksom på at automatiserte oversettelser kan inneholde feil eller unøyaktigheter. Det originale dokumentet på sitt opprinnelige språk bør betraktes som den autoritative kilden. For kritisk informasjon anbefales profesjonell menneskelig oversettelse. Vi er ikke ansvarlige for misforståelser eller feiltolkninger som oppstår ved bruk av denne oversettelsen.