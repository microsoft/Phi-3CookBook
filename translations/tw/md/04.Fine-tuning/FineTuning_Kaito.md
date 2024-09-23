## 使用 Kaito 進行微調

[Kaito](https://github.com/Azure/kaito) 是一個操作工具，可以在 Kubernetes 集群中自動化 AI/ML 推理模型的部署。

相比大多數基於虛擬機基礎設施的主流模型部署方法，Kaito 有以下幾個主要區別：

- 使用容器映像管理模型文件。提供一個 http 服務器來使用模型庫進行推理調用。
- 通過提供預設配置，避免調整部署參數以適應 GPU 硬件。
- 根據模型需求自動配置 GPU 節點。
- 如果許可證允許，將大型模型映像託管在公共的 Microsoft Container Registry (MCR) 中。

使用 Kaito，將大型 AI 推理模型引入 Kubernetes 的工作流程得到了極大簡化。

## 架構

Kaito 遵循經典的 Kubernetes 自定義資源定義（CRD）/控制器設計模式。用戶管理一個 `workspace` 自定義資源，描述 GPU 需求和推理規範。Kaito 控制器將通過協調 `workspace` 自定義資源來自動化部署。
<div align="left">
  <img src="https://github.com/Azure/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito 架構" alt="Kaito 架構">
</div>

上圖展示了 Kaito 架構概覽。其主要組件包括：

- **Workspace controller**：協調 `workspace` 自定義資源，創建 `machine`（如下所述）自定義資源以觸發節點自動配置，並根據模型預設配置創建推理工作負載（`deployment` 或 `statefulset`）。
- **Node provisioner controller**：該控制器的名稱在 [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) 中為 *gpu-provisioner*。它使用源自 [Karpenter](https://sigs.k8s.io/karpenter) 的 `machine` CRD 與 workspace controller 進行交互。它集成了 Azure Kubernetes Service (AKS) API，以向 AKS 集群添加新的 GPU 節點。
> 注意：[*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) 是一個開源組件。如果其他控制器支持 [Karpenter-core](https://sigs.k8s.io/karpenter) API，它們可以替換此組件。

## 安裝

請參閱安裝指南 [這裡](https://github.com/Azure/kaito/blob/main/docs/installation.md)。

## 快速開始

安裝 Kaito 後，可以嘗試以下命令來啟動微調服務。

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

可以通過運行以下命令來跟蹤 workspace 狀態。當 WORKSPACEREADY 列變為 `True` 時，表示模型已成功部署。

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

接下來，可以找到推理服務的集群 IP，並使用臨時 `curl` pod 測試集群中的服務端點。

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

免责声明：此翻译由AI模型从原文翻译而来，可能不完全准确。请审核输出内容并进行必要的修改。