## 使用 Kaito 進行推理

[Kaito](https://github.com/Azure/kaito) 是一個操作器，用於自動化在 Kubernetes 集群中部署 AI/ML 推理模型。

與大多數基於虛擬機基礎設施的主流模型部署方法相比，Kaito 具有以下主要差異：

- 使用容器映像管理模型文件。提供一個 http 服務器來通過模型庫執行推理調用。
- 通過提供預設配置，避免調整部署參數以適配 GPU 硬件。
- 根據模型需求自動分配 GPU 節點。
- 如果許可證允許，將大型模型映像托管在 Microsoft 公共容器註冊表 (MCR) 中。

使用 Kaito，在 Kubernetes 中引入大型 AI 推理模型的工作流程大大簡化。

## 架構

Kaito 採用了經典的 Kubernetes 自定義資源定義 (CRD)/控制器設計模式。用戶管理一個 `workspace` 自定義資源，該資源描述了 GPU 需求和推理規範。Kaito 控制器將通過調解 `workspace` 自定義資源來自動完成部署。
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito 架構" alt="Kaito 架構">
</div>

上圖展示了 Kaito 的架構概覽。其主要組件包括：

- **工作區控制器**：調解 `workspace` 自定義資源，創建 `machine`（下文解釋）自定義資源以觸發節點自動分配，並根據模型預設配置創建推理工作負載（`deployment` 或 `statefulset`）。
- **節點分配控制器**：該控制器在 [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) 中名為 *gpu-provisioner*。它使用源自 [Karpenter](https://sigs.k8s.io/karpenter) 的 `machine` CRD 與工作區控制器進行交互。它集成了 Azure Kubernetes Service (AKS) API，向 AKS 集群添加新的 GPU 節點。
> 注意：[*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) 是一個開源組件。如果其他控制器支持 [Karpenter-core](https://sigs.k8s.io/karpenter) API，也可以替換掉它。

## 安裝

請查看 [這裡](https://github.com/Azure/kaito/blob/main/docs/installation.md) 的安裝指南。

## 快速開始 Phi-3 推理
[Phi-3 推理示例代碼](https://github.com/Azure/kaito/tree/main/examples/inference)

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

可以通過運行以下命令來追蹤工作區狀態。當 WORKSPACEREADY 列變為 `True` 時，模型已成功部署。

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

接下來，可以找到推理服務的集群 IP，並使用臨時的 `curl` pod 在集群中測試服務端點。

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## 使用適配器快速開始 Phi-3 推理

安裝 Kaito 後，可以嘗試以下命令啟動推理服務。

[使用適配器的 Phi-3 推理示例代碼](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

可以通過運行以下命令來追蹤工作區狀態。當 WORKSPACEREADY 列變為 `True` 時，模型已成功部署。

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

接下來，可以找到推理服務的集群 IP，並使用臨時的 `curl` pod 在集群中測試服務端點。

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**免責聲明**:  
本文件是使用機器翻譯人工智能服務進行翻譯的。我們雖然努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文的母語版本作為權威來源。對於關鍵資訊，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解讀概不負責。