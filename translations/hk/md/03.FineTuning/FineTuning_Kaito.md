## 使用 Kaito 進行微調

[Kaito](https://github.com/Azure/kaito) 是一個操作工具，用於自動化在 Kubernetes 集群中部署 AI/ML 推理模型。

與大多數基於虛擬機基礎架構的主流模型部署方法相比，Kaito 具有以下主要特點：

- 使用容器映像管理模型文件，並提供一個 http 伺服器來使用模型庫進行推理調用。
- 提供預設配置，避免為適配 GPU 硬件而調整部署參數。
- 根據模型需求自動配置 GPU 節點。
- 如果許可證允許，將大型模型映像托管在公共的 Microsoft Container Registry (MCR) 中。

透過 Kaito，將大型 AI 推理模型引入 Kubernetes 的工作流程大大簡化。

## 架構

Kaito 遵循經典的 Kubernetes Custom Resource Definition (CRD)/控制器設計模式。用戶管理一個 `workspace` 自定義資源，該資源描述了 GPU 的需求和推理規範。Kaito 控制器將透過協調 `workspace` 自定義資源來自動化部署。
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito 架構" alt="Kaito 架構">
</div>

上圖展示了 Kaito 的架構概覽。其主要組件包括：

- **工作空間控制器 (Workspace controller)**：負責協調 `workspace` 自定義資源，創建 `machine`（下文解釋）自定義資源以觸發節點自動配置，並基於模型預設配置創建推理工作負載（`deployment` 或 `statefulset`）。
- **節點配置控制器 (Node provisioner controller)**：該控制器在 [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) 中名為 *gpu-provisioner*。它使用來自 [Karpenter](https://sigs.k8s.io/karpenter) 的 `machine` CRD 與工作空間控制器進行交互。該控制器整合了 Azure Kubernetes Service (AKS) 的 API，為 AKS 集群新增 GPU 節點。
> 注意：[*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) 是一個開源組件。如果其他控制器支持 [Karpenter-core](https://sigs.k8s.io/karpenter) API，也可以替換它。

## 概覽影片
[觀看 Kaito 演示](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## 安裝

請參閱 [此處](https://github.com/Azure/kaito/blob/main/docs/installation.md) 的安裝指南。

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

可以透過執行以下命令來跟蹤工作空間的狀態。當 WORKSPACEREADY 欄位變為 `True` 時，表示模型已成功部署。

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

接下來，可以找到推理服務的集群 IP，並使用臨時的 `curl` pod 在集群中測試服務端點。

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**免責聲明**:  
本文件是使用機器翻譯人工智能服務翻譯的。儘管我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文檔的母語版本為權威來源。對於關鍵信息，建議使用專業的人工作翻譯。我們對因使用本翻譯而引起的任何誤解或誤讀概不負責。