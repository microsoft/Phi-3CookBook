## Ottimizzazione con Kaito

[Kaito](https://github.com/Azure/kaito) è un operatore che automatizza il deployment dei modelli di inferenza AI/ML in un cluster Kubernetes.

Kaito presenta le seguenti differenze chiave rispetto alla maggior parte delle metodologie di deployment dei modelli basate su infrastrutture di macchine virtuali:

- Gestisce i file dei modelli utilizzando immagini container. Viene fornito un server http per effettuare chiamate di inferenza utilizzando la libreria del modello.
- Evita di dover ottimizzare i parametri di deployment per adattarsi all'hardware GPU grazie a configurazioni preimpostate.
- Esegue il provisioning automatico dei nodi GPU in base ai requisiti del modello.
- Ospita immagini di modelli di grandi dimensioni nel Microsoft Container Registry (MCR) pubblico, se la licenza lo consente.

Grazie a Kaito, il flusso di lavoro per integrare grandi modelli di inferenza AI in Kubernetes viene notevolmente semplificato.

## Architettura

Kaito segue il classico pattern di design Kubernetes Custom Resource Definition (CRD)/controller. L'utente gestisce una risorsa personalizzata `workspace` che descrive i requisiti GPU e le specifiche di inferenza. I controller di Kaito automatizzano il deployment riconciliando la risorsa personalizzata `workspace`.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Architettura di Kaito" alt="Architettura di Kaito">
</div>

La figura sopra mostra una panoramica dell'architettura di Kaito. I suoi componenti principali sono:

- **Controller dello spazio di lavoro**: Riconcilia la risorsa personalizzata `workspace`, crea risorse personalizzate `machine` (spiegate di seguito) per attivare il provisioning automatico dei nodi e crea il carico di lavoro di inferenza (`deployment` o `statefulset`) basandosi sulle configurazioni preimpostate del modello.
- **Controller per il provisioning dei nodi**: Il nome del controller è *gpu-provisioner* nel [grafico helm gpu-provisioner](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Utilizza la CRD `machine` derivata da [Karpenter](https://sigs.k8s.io/karpenter) per interagire con il controller dello spazio di lavoro. Si integra con le API di Azure Kubernetes Service (AKS) per aggiungere nuovi nodi GPU al cluster AKS.  
> Nota: Il [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) è un componente open source. Può essere sostituito da altri controller se supportano le API di [Karpenter-core](https://sigs.k8s.io/karpenter).

## Video panoramica 
[Guarda la demo di Kaito](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## Installazione

Consulta la guida all'installazione [qui](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Guida rapida

Dopo aver installato Kaito, è possibile provare i seguenti comandi per avviare un servizio di ottimizzazione.

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

Lo stato dello spazio di lavoro può essere monitorato eseguendo il seguente comando. Quando la colonna WORKSPACEREADY diventa `True`, il modello è stato distribuito con successo.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Successivamente, è possibile trovare l'indirizzo IP del cluster del servizio di inferenza e utilizzare un pod temporaneo `curl` per testare l'endpoint del servizio nel cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Disclaimer (Avvertenza):**  
Questo documento è stato tradotto utilizzando servizi di traduzione automatica basati sull'intelligenza artificiale. Sebbene ci impegniamo per garantire l'accuratezza, si prega di notare che le traduzioni automatizzate possono contenere errori o imprecisioni. Il documento originale nella sua lingua madre dovrebbe essere considerato la fonte autorevole. Per informazioni critiche, si raccomanda una traduzione professionale effettuata da un traduttore umano. Non siamo responsabili per eventuali malintesi o interpretazioni errate derivanti dall'uso di questa traduzione.