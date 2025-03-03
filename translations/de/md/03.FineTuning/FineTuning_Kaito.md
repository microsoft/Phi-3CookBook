## Feinabstimmung mit Kaito

[Kaito](https://github.com/Azure/kaito) ist ein Operator, der die Bereitstellung von AI/ML-Inferenzmodellen in einem Kubernetes-Cluster automatisiert.

Kaito bietet folgende wesentliche Vorteile im Vergleich zu den meisten gängigen Modellbereitstellungsmethoden, die auf virtuellen Maschinen basieren:

- Verwalten von Modelldateien über Container-Images. Ein HTTP-Server wird bereitgestellt, um Inferenzaufrufe mithilfe der Modellbibliothek auszuführen.
- Vermeidung der Anpassung von Bereitstellungsparametern an GPU-Hardware durch vordefinierte Konfigurationen.
- Automatische Bereitstellung von GPU-Knoten basierend auf den Modellanforderungen.
- Hosting großer Modell-Images im öffentlichen Microsoft Container Registry (MCR), sofern es die Lizenz erlaubt.

Mit Kaito wird der Workflow zur Integration großer AI-Inferenzmodelle in Kubernetes erheblich vereinfacht.

## Architektur

Kaito folgt dem klassischen Kubernetes-Designmuster für benutzerdefinierte Ressourcen (Custom Resource Definition, CRD) und Controller. Der Benutzer verwaltet eine `workspace`-benutzerdefinierte Ressource, die die GPU-Anforderungen und die Inferenzspezifikation beschreibt. Die Kaito-Controller automatisieren die Bereitstellung, indem sie die `workspace`-Ressource abgleichen.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito-Architektur" alt="Kaito-Architektur">
</div>

Die obige Abbildung zeigt eine Übersicht der Kaito-Architektur. Zu den Hauptkomponenten gehören:

- **Workspace-Controller**: Dieser gleicht die `workspace`-benutzerdefinierte Ressource ab, erstellt `machine` (weiter unten erläutert) benutzerdefinierte Ressourcen, um die automatische Bereitstellung von Knoten auszulösen, und erstellt die Inferenz-Workloads (`deployment` oder `statefulset`) basierend auf den vordefinierten Modellkonfigurationen.
- **Node-Provisioner-Controller**: Der Name dieses Controllers lautet *gpu-provisioner* im [gpu-provisioner Helm Chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Er verwendet die `machine`-CRD, die von [Karpenter](https://sigs.k8s.io/karpenter) stammt, um mit dem Workspace-Controller zu interagieren. Er integriert sich mit den APIs des Azure Kubernetes Service (AKS), um neue GPU-Knoten zum AKS-Cluster hinzuzufügen.
> Hinweis: Der [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ist eine Open-Source-Komponente. Er kann durch andere Controller ersetzt werden, sofern diese die [Karpenter-core](https://sigs.k8s.io/karpenter)-APIs unterstützen.

## Übersichtsvideo 
[Sehen Sie sich die Kaito-Demo an](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Installation

Bitte folgen Sie der Installationsanleitung [hier](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Schnellstart

Nach der Installation von Kaito können Sie die folgenden Befehle ausprobieren, um einen Feinabstimmungsdienst zu starten.

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

Der Status des Workspaces kann mit dem folgenden Befehl überwacht werden. Wenn die Spalte WORKSPACEREADY den Wert `True` hat, wurde das Modell erfolgreich bereitgestellt.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Anschließend können Sie die Cluster-IP des Inferenzdienstes ermitteln und einen temporären `curl`-Pod verwenden, um den Service-Endpunkt im Cluster zu testen.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Haftungsausschluss**:  
Dieses Dokument wurde mithilfe von KI-basierten maschinellen Übersetzungsdiensten übersetzt. Obwohl wir uns um Genauigkeit bemühen, weisen wir darauf hin, dass automatisierte Übersetzungen Fehler oder Ungenauigkeiten enthalten können. Das Originaldokument in seiner ursprünglichen Sprache sollte als maßgebliche Quelle betrachtet werden. Für kritische Informationen wird eine professionelle menschliche Übersetzung empfohlen. Wir übernehmen keine Haftung für Missverständnisse oder Fehlinterpretationen, die sich aus der Nutzung dieser Übersetzung ergeben.