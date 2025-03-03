## Inference met Kaito

[Kaito](https://github.com/Azure/kaito) is een operator die het implementeren van AI/ML-inferentiemodellen in een Kubernetes-cluster automatiseert.

Kaito onderscheidt zich op de volgende manieren van de meeste gangbare methodologieën voor modelimplementatie die zijn gebaseerd op virtuele machine-infrastructuren:

- Beheer modelfiles met behulp van containerafbeeldingen. Een http-server wordt geleverd om inferentie-aanroepen uit te voeren met behulp van de modellibrary.
- Vermijd het afstemmen van implementatieparameters op GPU-hardware door vooraf ingestelde configuraties te bieden.
- Automatisch GPU-nodes toewijzen op basis van modelvereisten.
- Host grote modelafbeeldingen in de openbare Microsoft Container Registry (MCR) als de licentie dit toestaat.

Met Kaito wordt de workflow voor het onboarden van grote AI-inferentiemodellen in Kubernetes aanzienlijk vereenvoudigd.

## Architectuur

Kaito volgt het klassieke Kubernetes Custom Resource Definition (CRD)/controller ontwerpmodel. De gebruiker beheert een `workspace` custom resource die de GPU-vereisten en de inferentiespecificatie beschrijft. Kaito-controllers automatiseren de implementatie door de `workspace` custom resource te reconciliëren.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito-architectuur" alt="Kaito-architectuur">
</div>

De bovenstaande afbeelding toont een overzicht van de Kaito-architectuur. De belangrijkste onderdelen zijn:

- **Workspace controller**: Deze reconcilieert de `workspace` custom resource, creëert `machine` (hieronder uitgelegd) custom resources om automatische node-toewijzing te starten, en creëert de inferentieworkload (`deployment` of `statefulset`) op basis van de vooraf ingestelde modelconfiguraties.
- **Node provisioner controller**: De naam van deze controller is *gpu-provisioner* in de [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Het gebruikt de `machine` CRD afkomstig van [Karpenter](https://sigs.k8s.io/karpenter) om te communiceren met de workspace controller. Het integreert met Azure Kubernetes Service (AKS)-API's om nieuwe GPU-nodes toe te voegen aan het AKS-cluster.
> Opmerking: De [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) is een open source-component. Het kan worden vervangen door andere controllers als deze [Karpenter-core](https://sigs.k8s.io/karpenter)-API's ondersteunen.

## Installatie

Bekijk de installatiehandleiding [hier](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Snel starten met Inference Phi-3
[Voorbeeldcode Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

De status van de workspace kan worden gevolgd door het volgende commando uit te voeren. Wanneer de kolom WORKSPACEREADY `True` wordt, is het model succesvol geïmplementeerd.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Vervolgens kun je het cluster-ip van de inferentieservice vinden en een tijdelijke `curl` pod gebruiken om het service-eindpunt in het cluster te testen.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Snel starten met Inference Phi-3 met adapters

Na het installeren van Kaito kun je de volgende commando's proberen om een inferentieservice te starten.

[Voorbeeldcode Inference Phi-3 met Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

De status van de workspace kan worden gevolgd door het volgende commando uit te voeren. Wanneer de kolom WORKSPACEREADY `True` wordt, is het model succesvol geïmplementeerd.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Vervolgens kun je het cluster-ip van de inferentieservice vinden en een tijdelijke `curl` pod gebruiken om het service-eindpunt in het cluster te testen.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Disclaimer**:  
Dit document is vertaald met behulp van AI-gestuurde vertaaldiensten. Hoewel we streven naar nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of verkeerde interpretaties die voortvloeien uit het gebruik van deze vertaling.