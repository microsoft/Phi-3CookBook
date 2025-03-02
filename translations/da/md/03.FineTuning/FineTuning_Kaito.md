## Finjustering med Kaito

[Kaito](https://github.com/Azure/kaito) er en operator, der automatiserer udrulningen af AI/ML-inferensmodeller i en Kubernetes-klynge.

Kaito har følgende nøgleforskelle sammenlignet med de fleste mainstream-modeldeployeringstilgange, som er bygget på virtuelle maskine-infrastrukturer:

- Administrer modelfiler ved hjælp af containerbilleder. En HTTP-server stilles til rådighed for at udføre inferenskald ved hjælp af modellens bibliotek.
- Undgå at tilpasse udrulningsparametre til GPU-hardware ved at tilbyde forudindstillede konfigurationer.
- Automatisk provisionering af GPU-noder baseret på modellens krav.
- Værtsstore modelbilleder i det offentlige Microsoft Container Registry (MCR), hvis licensen tillader det.

Med Kaito bliver arbejdsgangen for at onboarde store AI-inferensmodeller i Kubernetes væsentligt forenklet.

## Arkitektur

Kaito følger det klassiske Kubernetes Custom Resource Definition(CRD)/controller designmønster. Brugeren administrerer en `workspace` custom resource, som beskriver GPU-kravene og inferensspecifikationen. Kaito-controllere automatiserer udrulningen ved at synkronisere `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Ovenstående figur viser en oversigt over Kaitos arkitektur. Dens vigtigste komponenter består af:

- **Workspace controller**: Synkroniserer `workspace` custom resource, opretter `machine` (forklaret nedenfor) custom resources for at udløse automatisk provisionering af noder og opretter inferensarbejdsbyrden (`deployment` eller `statefulset`) baseret på modellens forudindstillede konfigurationer.
- **Node provisioner controller**: Controllerens navn er *gpu-provisioner* i [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Den bruger `machine` CRD, som stammer fra [Karpenter](https://sigs.k8s.io/karpenter), til at interagere med workspace controlleren. Den integrerer med Azure Kubernetes Service(AKS)-API'er for at tilføje nye GPU-noder til AKS-klyngen.
> Bemærk: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) er en open source-komponent. Den kan erstattes af andre controllere, hvis de understøtter [Karpenter-core](https://sigs.k8s.io/karpenter)-API'er.

## Oversigtsvideo
[Se Kaito-demoen](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Installation

Tjek venligst installationsvejledningen [her](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Hurtig start

Efter installation af Kaito kan man prøve følgende kommandoer for at starte en finjusteringstjeneste.

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

Workspace-statussen kan følges ved at køre følgende kommando. Når kolonnen WORKSPACEREADY bliver `True`, er modellen blevet udrullet med succes.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Herefter kan man finde inferenstjenestens cluster-ip og bruge en midlertidig `curl`-pod til at teste tjenestens endpoint i klyngen.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Ansvarsfraskrivelse**:  
Dette dokument er blevet oversat ved hjælp af maskinbaserede AI-oversættelsestjenester. Selvom vi bestræber os på nøjagtighed, skal det bemærkes, at automatiserede oversættelser kan indeholde fejl eller unøjagtigheder. Det originale dokument på dets oprindelige sprog bør betragtes som den autoritative kilde. For kritisk information anbefales professionel menneskelig oversættelse. Vi påtager os ikke ansvar for misforståelser eller fejltolkninger, der måtte opstå som følge af brugen af denne oversættelse.