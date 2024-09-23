## 使用 Kaito 进行微调

[Kaito](https://github.com/Azure/kaito) 是一个操作员，用于在 Kubernetes 集群中自动化 AI/ML 推理模型的部署。

与大多数基于虚拟机基础设施的主流模型部署方法相比，Kaito 具有以下主要差异：

- 使用容器镜像管理模型文件。提供一个 http 服务器来使用模型库进行推理调用。
- 通过提供预设配置，避免调整部署参数以适应 GPU 硬件。
- 根据模型需求自动配置 GPU 节点。
- 如果许可证允许，在公共的 Microsoft 容器注册表 (MCR) 中托管大型模型镜像。

使用 Kaito，Kubernetes 中大规模 AI 推理模型的上船流程大大简化。

## 架构

Kaito 遵循经典的 Kubernetes 自定义资源定义 (CRD)/控制器设计模式。用户管理一个 `workspace` 自定义资源，该资源描述 GPU 需求和推理规范。Kaito 控制器将通过协调 `workspace` 自定义资源来自动化部署。
<div align="left">
  <img src="https://github.com/Azure/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito 架构" alt="Kaito 架构">
</div>

上图展示了 Kaito 架构概述。其主要组件包括：

- **Workspace 控制器**：协调 `workspace` 自定义资源，创建 `machine`（如下所述）自定义资源以触发节点自动配置，并根据模型预设配置创建推理工作负载（`deployment` 或 `statefulset`）。
- **节点配置控制器**：该控制器在 [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) 中名为 *gpu-provisioner*。它使用源自 [Karpenter](https://sigs.k8s.io/karpenter) 的 `machine` CRD 与 workspace 控制器交互。它集成了 Azure Kubernetes 服务 (AKS) API，以向 AKS 集群添加新的 GPU 节点。
> 注意：[*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) 是一个开源组件。如果其他控制器支持 [Karpenter-core](https://sigs.k8s.io/karpenter) API，则可以替换它。

## 安装

请查看[此处](https://github.com/Azure/kaito/blob/main/docs/installation.md)的安装指南。

## 快速开始

安装 Kaito 后，可以尝试以下命令来启动微调服务。

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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # 微调输出 ACR 路径
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
    image: "ACR_REPO_HERE.azurecr.io/IMAGE_NAME_HERE:0.0.1" # 微调输出 ACR 路径
    imagePushSecret: ACR_REGISTRY_SECRET_HERE
    

$ kubectl apply -f examples/fine-tuning/kaito_workspace_tuning_phi_3.yaml
```

可以通过运行以下命令跟踪 workspace 状态。当 WORKSPACEREADY 列变为 `True` 时，模型已成功部署。

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

接下来，可以找到推理服务的集群 IP，并使用临时的 `curl` pod 测试集群中的服务端点。

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

免责声明：本翻译由AI模型从原文翻译而来，可能不够完美。请审阅输出内容并进行必要的修改。