## Fine-Tuning met Kaito

[Kaito](https://github.com/Azure/kaito) is een operator die het implementeren van AI/ML-inferentiemodellen in een Kubernetes-cluster automatiseert.

Kaito biedt de volgende belangrijke voordelen ten opzichte van de meeste gangbare modelimplementatiemethoden die zijn gebouwd op virtuele machine-infrastructuren:

- Beheer modelfiles met behulp van containerafbeeldingen. Er wordt een http-server geleverd om inferentie-aanroepen uit te voeren met behulp van de modellibrary.
- Vermijd het aanpassen van implementatieparameters aan GPU-hardware door vooraf ingestelde configuraties te bieden.
- Voorzie automatisch GPU-nodes op basis van modelvereisten.
- Host grote modelafbeeldingen in de openbare Microsoft Container Registry (MCR) als de licentie dit toestaat.

Met Kaito wordt het proces van het onboarden van grote AI-inferentiemodellen in Kubernetes aanzienlijk vereenvoudigd.

## Architectuur

Kaito volgt het klassieke Kubernetes Custom Resource Definition (CRD)/controllerontwerppatroon. De gebruiker beheert een `workspace`-custom resource die de GPU-vereisten en de inferentiespecificatie beschrijft. Kaito-controllers automatiseren de implementatie door de `workspace`-custom resource te reconciliëren.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architectuur" alt="Kaito architectuur">
</div>

De bovenstaande afbeelding toont een overzicht van de Kaito-architectuur. De belangrijkste componenten zijn:

- **Workspace controller**: Deze reconcilieert de `workspace`-custom resource, creëert `machine` (hieronder uitgelegd) custom resources om automatische provisioning van nodes te activeren, en creëert de inferentieworkload (`deployment` of `statefulset`) op basis van de vooraf ingestelde modelconfiguraties.
- **Node provisioner controller**: De naam van deze controller is *gpu-provisioner* in de [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Het gebruikt de `machine`-CRD afkomstig van [Karpenter](https://sigs.k8s.io/karpenter) om te communiceren met de workspace controller. Het integreert met de Azure Kubernetes Service (AKS)-API's om nieuwe GPU-nodes toe te voegen aan het AKS-cluster.
> Opmerking: De [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) is een open source component. Het kan worden vervangen door andere controllers als deze [Karpenter-core](https://sigs.k8s.io/karpenter)-API's ondersteunen.

## Overzichtsvideo 
[Bekijk de Kaito-demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## Installatie

Bekijk de installatiehandleiding [hier](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Snel starten

Na de installatie van Kaito kun je de volgende commando's proberen om een fine-tuning-service te starten.

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

De status van de workspace kan worden gevolgd door het volgende commando uit te voeren. Wanneer de kolom WORKSPACEREADY `True` wordt, is het model succesvol geïmplementeerd.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Vervolgens kun je het cluster-IP van de inferentieservice vinden en een tijdelijke `curl`-pod gebruiken om het service-endpoint in het cluster te testen.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Disclaimer**:  
Dit document is vertaald met behulp van AI-vertalingsdiensten. Hoewel we ons best doen voor nauwkeurigheid, dient u zich ervan bewust te zijn dat geautomatiseerde vertalingen fouten of onnauwkeurigheden kunnen bevatten. Het originele document in de oorspronkelijke taal moet worden beschouwd als de gezaghebbende bron. Voor cruciale informatie wordt professionele menselijke vertaling aanbevolen. Wij zijn niet aansprakelijk voor misverstanden of onjuiste interpretaties die voortvloeien uit het gebruik van deze vertaling.