## Slutledning med Kaito

[Kaito](https://github.com/Azure/kaito) är en operator som automatiserar distributionen av AI/ML-slutledningsmodeller i ett Kubernetes-kluster.

Kaito har följande viktiga skillnader jämfört med de flesta vanliga metodologier för modellutplacering som bygger på virtuella maskininfrastrukturer:

- Hantera modelfiler med hjälp av containerbilder. En HTTP-server tillhandahålls för att utföra slutledningsanrop med hjälp av modellbiblioteket.
- Undvik att justera distributionsparametrar för att passa GPU-hårdvara genom att tillhandahålla förinställda konfigurationer.
- Automatisk provisionering av GPU-noder baserat på modellkrav.
- Värd för stora modellbilder i det offentliga Microsoft Container Registry (MCR) om licensen tillåter.

Med Kaito förenklas arbetsflödet för att ombord stora AI-slutledningsmodeller i Kubernetes avsevärt.

## Arkitektur

Kaito följer det klassiska Kubernetes Custom Resource Definition (CRD)/controller-designmönstret. Användaren hanterar en `workspace`-anpassad resurs som beskriver GPU-kraven och slutledningsspecifikationen. Kaito-kontrollerna automatiserar distributionen genom att samordna den `workspace`-anpassade resursen.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito-arkitektur" alt="Kaito-arkitektur">
</div>

Figuren ovan presenterar en översikt över Kaitos arkitektur. Dess huvudsakliga komponenter består av:

- **Workspace controller**: Samordnar den `workspace`-anpassade resursen, skapar `machine` (förklaras nedan) anpassade resurser för att trigga automatisk provisionering av noder och skapar slutledningsarbetsbelastningen (`deployment` eller `statefulset`) baserat på modellens förinställda konfigurationer.
- **Node provisioner controller**: Kontrollerens namn är *gpu-provisioner* i [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Den använder `machine` CRD som härstammar från [Karpenter](https://sigs.k8s.io/karpenter) för att interagera med workspace controller. Den integreras med Azure Kubernetes Service (AKS) API:er för att lägga till nya GPU-noder till AKS-klustret.  
> Notera: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) är en öppen källkomponent. Den kan ersättas av andra kontroller om de stöder [Karpenter-core](https://sigs.k8s.io/karpenter) API:er.

## Installation

Vänligen kontrollera installationsguiden [här](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Snabbstart Slutledning Phi-3
[Exempelkod Slutledning Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Arbetsytans status kan spåras genom att köra följande kommando. När kolumnen WORKSPACEREADY blir `True` har modellen distribuerats framgångsrikt.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Därefter kan man hitta kluster-IP:n för slutledningstjänsten och använda en temporär `curl`-pod för att testa tjänstens slutpunkt i klustret.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Snabbstart Slutledning Phi-3 med adaptrar

Efter att ha installerat Kaito kan man prova följande kommandon för att starta en slutledningstjänst.

[Exempelkod Slutledning Phi-3 med Adaptrar](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Arbetsytans status kan spåras genom att köra följande kommando. När kolumnen WORKSPACEREADY blir `True` har modellen distribuerats framgångsrikt.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Därefter kan man hitta kluster-IP:n för slutledningstjänsten och använda en temporär `curl`-pod för att testa tjänstens slutpunkt i klustret.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Ansvarsfriskrivning**:  
Detta dokument har översatts med hjälp av maskinbaserade AI-översättningstjänster. Även om vi strävar efter noggrannhet, var medveten om att automatiserade översättningar kan innehålla fel eller felaktigheter. Det ursprungliga dokumentet på dess ursprungliga språk bör betraktas som den auktoritativa källan. För kritisk information rekommenderas professionell mänsklig översättning. Vi ansvarar inte för eventuella missförstånd eller feltolkningar som uppstår vid användning av denna översättning.