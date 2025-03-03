## 使用 Kaito 進行推論

[Kaito](https://github.com/Azure/kaito) 是一個運算元，能自動化在 Kubernetes 叢集中部署 AI/ML 推論模型。

與大多數基於虛擬機基礎設施的主流模型部署方法相比，Kaito 有以下幾個主要區別：

- 使用容器映像管理模型文件。提供一個 HTTP 伺服器，使用模型庫進行推論調用。
- 通過預設配置，避免為了適配 GPU 硬體而調整部署參數。
- 根據模型需求自動分配 GPU 節點。
- 如果許可證允許，可在 Microsoft 公共容器註冊表 (MCR) 中託管大型模型映像。

使用 Kaito，可以大大簡化在 Kubernetes 中上線大型 AI 推論模型的工作流程。

## 架構

Kaito 採用經典的 Kubernetes 自訂資源定義 (CRD)/控制器設計模式。使用者管理描述 GPU 要求和推論規範的 `workspace` 自訂資源。Kaito 控制器將通過調和 `workspace` 自訂資源自動完成部署。
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito 架構" alt="Kaito 架構">
</div>

上圖展示了 Kaito 的架構概覽。其主要組件包括：

- **工作區控制器**：調和 `workspace` 自訂資源，創建 `machine`（如下所述）自訂資源以觸發節點自動分配，並基於模型預設配置創建推論工作負載（`deployment` 或 `statefulset`）。
- **節點分配控制器**：此控制器在 [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) 中的名稱為 *gpu-provisioner*。它使用來自 [Karpenter](https://sigs.k8s.io/karpenter) 的 `machine` CRD 與工作區控制器交互。它與 Azure Kubernetes Service (AKS) API 集成，向 AKS 叢集中添加新的 GPU 節點。
> 注意：[*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) 是一個開源組件。如果其他控制器支持 [Karpenter-core](https://sigs.k8s.io/karpenter) API，也可以替換它。

## 安裝

請參閱[此處](https://github.com/Azure/kaito/blob/main/docs/installation.md)的安裝指南。

## 快速開始 Phi-3 推論
[Phi-3 推論範例程式碼](https://github.com/Azure/kaito/tree/main/examples/inference)

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

可以通過執行以下命令來追蹤工作區的狀態。當 WORKSPACEREADY 欄位變為 `True` 時，模型已成功部署。

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

接下來，可以找到推論服務的叢集 IP，並使用臨時 `curl` pod 測試叢集中的服務端點。

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## 快速開始帶有適配器的 Phi-3 推論

安裝 Kaito 後，可以嘗試以下命令啟動推論服務。

[帶有適配器的 Phi-3 推論範例程式碼](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

可以通過執行以下命令來追蹤工作區的狀態。當 WORKSPACEREADY 欄位變為 `True` 時，模型已成功部署。

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

接下來，可以找到推論服務的叢集 IP，並使用臨時 `curl` pod 測試叢集中的服務端點。

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**免責聲明**：  
本文件使用基於機器的人工智能翻譯服務進行翻譯。雖然我們努力確保準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原始語言的文件作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而產生的任何誤解或錯誤解釋概不負責。