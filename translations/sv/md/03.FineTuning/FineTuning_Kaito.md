## Finjustering med Kaito

[Kaito](https://github.com/Azure/kaito) är en operator som automatiserar driftsättningen av AI/ML-inferensmodeller i ett Kubernetes-kluster.

Kaito skiljer sig från de flesta vanliga metoder för modellimplementering som är baserade på virtualiseringsinfrastrukturer genom följande:

- Hantera modelfiler med hjälp av containerbilder. En HTTP-server tillhandahålls för att utföra inferenskörningar med modellbiblioteket.
- Undvik att behöva justera driftsättningsparametrar för att passa GPU-hårdvara genom att använda förinställda konfigurationer.
- Automatiskt provisionera GPU-noder baserat på modellkrav.
- Värd för stora modellbilder i det publika Microsoft Container Registry (MCR) om licensen tillåter det.

Med Kaito förenklas arbetsflödet för att introducera stora AI-inferensmodeller i Kubernetes avsevärt.

## Arkitektur

Kaito följer det klassiska Kubernetes-mönstret med Custom Resource Definition (CRD) och kontroller. Användaren hanterar en `workspace`-anpassad resurs som beskriver GPU-kraven och specifikationen för inferensen. Kaito-kontrollerna automatiserar driftsättningen genom att synkronisera `workspace`-resursen.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito-arkitektur" alt="Kaito-arkitektur">
</div>

Figuren ovan visar en översikt av Kaitos arkitektur. Dess huvudsakliga komponenter inkluderar:

- **Workspace controller**: Synkroniserar `workspace`-resursen, skapar `machine` (förklaras nedan) anpassade resurser för att trigga automatisk provisionering av noder, och skapar inferensarbetsbelastningar (`deployment` eller `statefulset`) baserat på förinställda modellkonfigurationer.
- **Node provisioner controller**: Denna kontrollers namn är *gpu-provisioner* i [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Den använder `machine` CRD, som härstammar från [Karpenter](https://sigs.k8s.io/karpenter), för att interagera med workspace-kontrollern. Den integreras med Azure Kubernetes Service (AKS) API:er för att lägga till nya GPU-noder i AKS-klustret. 
> Obs: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) är en öppen källkomponent. Den kan ersättas av andra kontroller om de stöder [Karpenter-core](https://sigs.k8s.io/karpenter) API:er.

## Översiktsvideo
[Titta på Kaito-demonstrationen](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Installation

Se installationsguiden [här](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Snabbstart

Efter att ha installerat Kaito kan du använda följande kommandon för att starta en finjusteringstjänst.

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

Statusen för workspace kan följas med följande kommando. När kolumnen WORKSPACEREADY blir `True` har modellen implementerats framgångsrikt.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Därefter kan du hitta inferenstjänstens cluster-ip och använda en temporär `curl`-pod för att testa tjänstens slutpunkt i klustret.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av AI-baserade maskinöversättningstjänster. Även om vi strävar efter noggrannhet, bör det noteras att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess originalspråk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi tar inget ansvar för eventuella missförstånd eller feltolkningar som uppstår till följd av användningen av denna översättning.