## Fine-Tuning gamit ang Kaito

[Kaito](https://github.com/Azure/kaito) ay isang operator na awtomatikong nagde-deploy ng AI/ML inference model sa isang Kubernetes cluster.

May mga sumusunod na pangunahing pagkakaiba ang Kaito kumpara sa karamihan ng mga karaniwang paraan ng pag-deploy ng modelong nakabase sa virtual machine infrastructures:

- Pinamamahalaan ang mga model file gamit ang container images. May isang http server na ibinibigay para magsagawa ng inference calls gamit ang model library.
- Iniiwasan ang pag-tune ng deployment parameters para umangkop sa GPU hardware sa pamamagitan ng pagbibigay ng preset configurations.
- Awtomatikong nagpo-provision ng GPU nodes batay sa mga pangangailangan ng modelo.
- Nagho-host ng malalaking model images sa pampublikong Microsoft Container Registry (MCR) kung pinapayagan ng lisensya.

Sa pamamagitan ng Kaito, ang workflow ng pag-onboard ng malalaking AI inference models sa Kubernetes ay lubos na pinadali.

## Arkitektura

Ang Kaito ay sumusunod sa klasikong Kubernetes Custom Resource Definition (CRD)/controller design pattern. Pinamamahalaan ng user ang isang `workspace` custom resource na naglalarawan ng GPU requirements at inference specification. Awtomatikong ide-deploy ng mga Kaito controllers ang modelo sa pamamagitan ng pagre-reconcile ng `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

Ang larawan sa itaas ay nagpapakita ng overview ng Kaito architecture. Ang mga pangunahing bahagi nito ay binubuo ng:

- **Workspace controller**: Nirereconcile nito ang `workspace` custom resource, lumilikha ng mga `machine` (ipinaliwanag sa ibaba) custom resources para ma-trigger ang awtomatikong pag-provision ng node, at lumilikha ng inference workload (`deployment` o `statefulset`) batay sa mga preset configurations ng modelo.
- **Node provisioner controller**: Ang pangalan ng controller ay *gpu-provisioner* sa [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Ginagamit nito ang `machine` CRD na nagmula sa [Karpenter](https://sigs.k8s.io/karpenter) upang makipag-ugnayan sa workspace controller. Isinasama nito ang Azure Kubernetes Service (AKS) APIs upang magdagdag ng mga bagong GPU nodes sa AKS cluster.  
> Tandaan: Ang [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ay isang open-sourced na bahagi. Maaari itong palitan ng ibang controllers kung sinusuportahan nila ang [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## Overview na video  
[Manood ng Kaito Demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Instalasyon

Mangyaring tingnan ang gabay sa instalasyon [dito](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Mabilisang Simula

Pagkatapos i-install ang Kaito, maaaring subukan ang mga sumusunod na command upang simulan ang isang fine-tuning service.

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

Ang status ng workspace ay maaaring masubaybayan sa pamamagitan ng pagpapatakbo ng sumusunod na command. Kapag ang WORKSPACEREADY column ay naging `True`, matagumpay nang na-deploy ang modelo.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Sunod, maaaring hanapin ang cluster ip ng inference service at gumamit ng temporal na `curl` pod upang i-test ang service endpoint sa cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyo ng AI na batay sa makina. Bagama't aming sinisikap ang kawastuhan, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi pagkakatumpak. Ang orihinal na dokumento sa kanyang katutubong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasaling ginagawa ng tao. Kami ay hindi mananagot para sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.