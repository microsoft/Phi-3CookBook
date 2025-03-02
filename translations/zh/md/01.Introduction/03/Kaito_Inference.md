## 使用 Kaito 进行推理

[Kaito](https://github.com/Azure/kaito) 是一个操作器，用于在 Kubernetes 集群中自动化部署 AI/ML 推理模型。

与大多数基于虚拟机基础设施的主流模型部署方法相比，Kaito 具有以下关键差异化优势：

- 使用容器镜像管理模型文件。提供一个 HTTP 服务器，通过模型库进行推理调用。
- 提供预设配置，避免为适配 GPU 硬件而调整部署参数。
- 根据模型需求自动配置 GPU 节点。
- 如果许可证允许，可以在 Microsoft 公共容器注册表 (MCR) 中托管大型模型镜像。

通过 Kaito，可以大幅简化在 Kubernetes 中上线大型 AI 推理模型的流程。

## 架构

Kaito 遵循经典的 Kubernetes 自定义资源定义（CRD）/控制器设计模式。用户管理一个 `workspace` 自定义资源，该资源描述了 GPU 的需求和推理的具体规范。Kaito 控制器通过对 `workspace` 自定义资源的协调，实现自动化部署。
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito 架构" alt="Kaito 架构">
</div>

上图展示了 Kaito 架构的概览。其主要组件包括：

- **工作区控制器**：协调 `workspace` 自定义资源，创建 `machine`（下文会解释）自定义资源以触发节点的自动配置，并根据模型的预设配置创建推理工作负载（`deployment` 或 `statefulset`）。
- **节点配置控制器**：此控制器在 [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) 中名为 *gpu-provisioner*。它使用源自 [Karpenter](https://sigs.k8s.io/karpenter) 的 `machine` CRD 与工作区控制器交互。它集成了 Azure Kubernetes 服务 (AKS) 的 API，用于向 AKS 集群添加新的 GPU 节点。
> 注意：[*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) 是一个开源组件。如果其他控制器支持 [Karpenter-core](https://sigs.k8s.io/karpenter) 的 API，也可以替换该组件。

## 安装

请查看[安装指南](https://github.com/Azure/kaito/blob/main/docs/installation.md)。

## 快速开始：Phi-3 推理

[Phi-3 推理示例代码](https://github.com/Azure/kaito/tree/main/examples/inference)

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

可以通过运行以下命令跟踪工作区状态。当 WORKSPACEREADY 列变为 `True` 时，模型已成功部署。

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

接下来，可以找到推理服务的集群 IP，并使用一个临时的 `curl` pod 测试集群中的服务端点。

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## 快速开始：带适配器的 Phi-3 推理

安装 Kaito 后，可以尝试以下命令启动推理服务。

[带适配器的 Phi-3 推理示例代码](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

可以通过运行以下命令跟踪工作区状态。当 WORKSPACEREADY 列变为 `True` 时，模型已成功部署。

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

接下来，可以找到推理服务的集群 IP，并使用一个临时的 `curl` pod 测试集群中的服务端点。

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**免责声明**:  
本文件通过基于机器的人工智能翻译服务翻译而成。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文件为权威来源。对于关键信息，建议使用专业的人类翻译服务。对于因使用本翻译而引起的任何误解或误读，我们概不负责。