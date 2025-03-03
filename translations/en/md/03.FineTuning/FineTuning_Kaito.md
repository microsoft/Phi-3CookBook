## Fine-Tuning with Kaito 

[Kaito](https://github.com/Azure/kaito) is an operator that simplifies the deployment of AI/ML inference models in a Kubernetes cluster.

Kaito stands out from most mainstream model deployment approaches based on virtual machine infrastructures due to the following key features:

- Use container images to manage model files. It provides an HTTP server to handle inference calls using the model library.
- Eliminate the need to adjust deployment parameters for GPU hardware by offering preset configurations.
- Automatically provision GPU nodes based on model requirements.
- Host large model images in the public Microsoft Container Registry (MCR), provided licensing permits.

With Kaito, onboarding large AI inference models into Kubernetes becomes much more straightforward.

## Architecture

Kaito is built on the classic Kubernetes Custom Resource Definition (CRD)/controller design pattern. Users define a `workspace` custom resource to specify GPU requirements and inference details. Kaito controllers automate deployment by reconciling the `workspace` custom resource.
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

The diagram above provides an overview of Kaito's architecture. Its primary components include:

- **Workspace controller**: This component reconciles the `workspace` custom resource, generates `machine` (explained below) custom resources to trigger node auto-provisioning, and creates the inference workload (`deployment` or `statefulset`) based on the model's preset configurations.
- **Node provisioner controller**: Named *gpu-provisioner* in the [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner), this controller uses the `machine` CRD from [Karpenter](https://sigs.k8s.io/karpenter) to communicate with the workspace controller. It integrates with Azure Kubernetes Service (AKS) APIs to add GPU nodes to the AKS cluster as needed.  
> Note: The [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) is an open-source component and can be replaced with other controllers that support [Karpenter-core](https://sigs.k8s.io/karpenter) APIs.

## Overview video 
[Watch the Kaito Demo](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## Installation

Refer to the installation guide [here](https://github.com/Azure/kaito/blob/main/docs/installation.md).

## Quick start

After installing Kaito, you can use the following commands to launch a fine-tuning service.

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

You can track the workspace status by running the command below. Once the WORKSPACEREADY column displays `True`, the model deployment has been completed successfully.

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

Next, retrieve the inference service's cluster IP and use a temporary `curl` pod to test the service endpoint within the cluster.

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**Disclaimer**:  
This document has been translated using machine-based AI translation services. While we strive for accuracy, please be aware that automated translations may contain errors or inaccuracies. The original document in its native language should be considered the authoritative source. For critical information, professional human translation is recommended. We are not liable for any misunderstandings or misinterpretations arising from the use of this translation.