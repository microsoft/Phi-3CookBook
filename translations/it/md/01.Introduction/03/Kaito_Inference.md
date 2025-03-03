## Inferenza con Kaito

[Kaito](https://github.com/Azure/kaito) è un operatore che automatizza il deployment dei modelli di inferenza AI/ML in un cluster Kubernetes.

Kaito offre le seguenti differenziazioni chiave rispetto alla maggior parte delle metodologie di deployment dei modelli basate su infrastrutture di macchine virtuali:

- Gestione dei file modello tramite immagini container. È fornito un server http per effettuare chiamate di inferenza utilizzando la libreria del modello.
- Evita di regolare i parametri di deployment per adattarli all'hardware GPU grazie a configurazioni predefinite.
- Auto-provisioning dei nodi GPU in base ai requisiti del modello.
- Hosting di immagini di modelli di grandi dimensioni nel Microsoft Container Registry (MCR) pubblico, se la licenza lo consente.

Con Kaito, il flusso di lavoro per integrare grandi modelli di inferenza AI in Kubernetes viene notevolmente semplificato.

## Architettura

Kaito segue il classico pattern di design basato su Custom Resource Definition (CRD)/controller di Kubernetes. L'utente gestisce una risorsa personalizzata `workspace` che descrive i requisiti GPU e la specifica di inferenza. I controller di Kaito automatizzano il deployment riconciliando la risorsa personalizzata `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Architettura di Kaito" alt="Architettura di Kaito">
</div>

La figura sopra presenta una panoramica dell'architettura di Kaito. I suoi principali componenti includono:

- **Workspace controller**: Riconcilia la risorsa personalizzata `workspace`, crea risorse personalizzate `machine` (spiegate di seguito) per attivare l'auto-provisioning dei nodi e crea il carico di lavoro di inferenza (`deployment` o `statefulset`) basandosi sulle configurazioni predefinite del modello.
- **Node provisioner controller**: Il nome del controller è *gpu-provisioner* nel [grafico helm gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Utilizza il CRD `machine` originato da [Karpenter](https://sigs.k8s.io/karpenter) per interagire con il workspace controller. Si integra con le API di Azure Kubernetes Service (AKS) per aggiungere nuovi nodi GPU al cluster AKS.  
> Nota: Il [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) è un componente open source. Può essere sostituito da altri controller se supportano le API di [Karpenter-core](https://sigs.k8s.io/karpenter).

## Installazione

Si prega di consultare la guida all'installazione [qui](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Esempio rapido di inferenza Phi-3
[Codice di esempio per inferenza Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Lo stato del workspace può essere monitorato eseguendo il seguente comando. Quando la colonna WORKSPACEREADY diventa `True`, il modello è stato distribuito con successo.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Successivamente, è possibile trovare l'indirizzo IP del cluster del servizio di inferenza e utilizzare un pod temporaneo `curl` per testare l'endpoint del servizio nel cluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Esempio rapido di inferenza Phi-3 con adapter

Dopo aver installato Kaito, è possibile eseguire i seguenti comandi per avviare un servizio di inferenza.

[Codice di esempio per inferenza Phi-3 con adapter](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Lo stato del workspace può essere monitorato eseguendo il seguente comando. Quando la colonna WORKSPACEREADY diventa `True`, il modello è stato distribuito con successo.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Successivamente, è possibile trovare l'indirizzo IP del cluster del servizio di inferenza e utilizzare un pod temporaneo `curl` per testare l'endpoint del servizio nel cluster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Disclaimer**:  
Questo documento è stato tradotto utilizzando servizi di traduzione automatica basati sull'intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatiche potrebbero contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.