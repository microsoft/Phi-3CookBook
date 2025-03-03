## Paggamit ng Kaito

Ang [Kaito](https://github.com/Azure/kaito) ay isang operator na nag-a-automate ng deployment ng AI/ML inference model sa isang Kubernetes cluster.

Ang Kaito ay may mga sumusunod na pangunahing pagkakaiba kumpara sa karamihan ng mga tradisyunal na pamamaraan ng model deployment na nakabatay sa virtual machine infrastructures:

- Pamamahala ng mga model file gamit ang container images. Isang http server ang ibinibigay upang magsagawa ng inference calls gamit ang model library.
- Iniiwasan ang pag-aayos ng deployment parameters para magkasya sa GPU hardware sa pamamagitan ng pagbibigay ng preset configurations.
- Awtomatikong nagpo-provision ng GPU nodes batay sa mga pangangailangan ng modelo.
- Nagho-host ng malalaking model images sa pampublikong Microsoft Container Registry (MCR) kung pinapayagan ng lisensya.

Sa pamamagitan ng Kaito, ang workflow ng onboarding ng malalaking AI inference models sa Kubernetes ay lubos na pinasimple.

## Arkitektura

Ang Kaito ay sumusunod sa klasikong Kubernetes Custom Resource Definition (CRD)/controller design pattern. Ang user ay nagma-manage ng isang `workspace` custom resource na naglalarawan ng GPU requirements at inference specification. Ang mga Kaito controllers ay awtomatikong magde-deploy sa pamamagitan ng pag-reconcile ng `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Arkitektura ng Kaito" alt="Arkitektura ng Kaito">
</div>

Ang larawan sa itaas ay nagpapakita ng kabuuang arkitektura ng Kaito. Ang mga pangunahing bahagi nito ay binubuo ng:

- **Workspace controller**: Nirereconcile nito ang `workspace` custom resource, gumagawa ng `machine` (ipinapaliwanag sa ibaba) custom resources upang mag-trigger ng node auto provisioning, at gumagawa ng inference workload (`deployment` o `statefulset`) batay sa model preset configurations.
- **Node provisioner controller**: Ang pangalan ng controller ay *gpu-provisioner* sa [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner). Ginagamit nito ang `machine` CRD na nagmula sa [Karpenter](https://sigs.k8s.io/karpenter) upang makipag-ugnayan sa workspace controller. Ito ay naka-integrate sa Azure Kubernetes Service (AKS) APIs upang magdagdag ng mga bagong GPU nodes sa AKS cluster.  
> Tandaan: Ang [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) ay isang open-source na component. Maaari itong palitan ng ibang controllers kung sinusuportahan nila ang [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## Pag-install

Mangyaring tingnan ang gabay sa pag-install [dito](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Mabilis na Simula ng Inference Phi-3
[Sample Code Inference Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

Ang status ng workspace ay maaaring subaybayan sa pamamagitan ng pagsasagawa ng sumusunod na command. Kapag ang WORKSPACEREADY column ay naging `True`, matagumpay nang na-deploy ang modelo.

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

Susunod, maaaring hanapin ang cluster ip ng inference service at gumamit ng pansamantalang `curl` pod upang subukan ang service endpoint sa cluster.

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## Mabilis na Simula ng Inference Phi-3 na may Adapters

Pagkatapos ma-install ang Kaito, maaaring subukan ang mga sumusunod na command upang magsimula ng inference service.

[Sample Code Inference Phi-3 with Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

Ang status ng workspace ay maaaring subaybayan sa pamamagitan ng pagsasagawa ng sumusunod na command. Kapag ang WORKSPACEREADY column ay naging `True`, matagumpay nang na-deploy ang modelo.

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

Susunod, maaaring hanapin ang cluster ip ng inference service at gumamit ng pansamantalang `curl` pod upang subukan ang service endpoint sa cluster.

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Paunawa**:  
Ang dokumentong ito ay isinalin gamit ang mga serbisyong machine-based AI translation. Bagama't aming pinagsisikapang maging wasto, mangyaring tandaan na ang mga awtomatikong pagsasalin ay maaaring maglaman ng mga pagkakamali o hindi tumpak na impormasyon. Ang orihinal na dokumento sa orihinal nitong wika ang dapat ituring na opisyal na sanggunian. Para sa mahalagang impormasyon, inirerekomenda ang propesyonal na pagsasalin ng tao. Hindi kami mananagot sa anumang hindi pagkakaunawaan o maling interpretasyon na dulot ng paggamit ng pagsasaling ito.