## 使用 Kaito 進行微調

[Kaito](https://github.com/Azure/kaito) 是一個運算操作工具，用於自動化在 Kubernetes 集群中部署 AI/ML 推理模型。

與大多數基於虛擬機基礎架構的主流模型部署方法相比，Kaito 具有以下主要特點：

- 使用容器映像管理模型文件，並提供一個 HTTP 伺服器以透過模型庫執行推理請求。
- 提供預設配置，無需調整部署參數以適配 GPU 硬體。
- 根據模型需求自動配置 GPU 節點。
- 如果許可證允許，可將大型模型映像託管於 Microsoft 公共容器註冊表 (MCR)。

使用 Kaito，可以大幅簡化在 Kubernetes 中引入大型 AI 推理模型的工作流程。

## 架構

Kaito 採用了經典的 Kubernetes 自定義資源定義 (CRD) / 控制器設計模式。使用者管理一個 `workspace` 自定義資源，該資源描述了 GPU 的需求和推理規範。Kaito 控制器將透過調和 `workspace` 自定義資源來自動化部署。
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito 架構" alt="Kaito 架構">
</div>

上圖展示了 Kaito 的架構概覽，其主要組件包括：

- **工作區控制器**：負責調和 `workspace` 自定義資源，創建 `machine`（下文解釋）自定義資源以觸發節點自動配置，並根據模型的預設配置創建推理工作負載（`deployment` 或 `statefulset`）。
- **節點配置控制器**：該控制器在 [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) 中被稱為 *gpu-provisioner*。它使用來自 [Karpenter](https://sigs.k8s.io/karpenter) 的 `machine` CRD 與工作區控制器互動，並透過 Azure Kubernetes Service (AKS) API 向 AKS 集群添加新的 GPU 節點。
> 注意：[*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) 是一個開源組件。如果其他控制器支援 [Karpenter-core](https://sigs.k8s.io/karpenter) API，也可以用來替代它。

## 概覽影片 
[觀看 Kaito 示範](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## 安裝

請參考[此處](https://github.com/Azure/kaito/blob/main/docs/installation.md)的安裝指南。

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

可以透過以下命令來追蹤工作區狀態。當 WORKSPACEREADY 欄位顯示為 `True` 時，表示模型已成功部署。

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

接下來，可以找到推理服務的集群 IP，並使用一個臨時的 `curl` pod 測試集群中的服務端點。

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**免責聲明**：  
本文檔使用基於機器的人工智能翻譯服務進行翻譯。我們雖然努力追求準確性，但請注意，自動翻譯可能包含錯誤或不準確之處。應以原文的母語版本作為權威來源。對於關鍵信息，建議尋求專業人工翻譯。我們對因使用此翻譯而引起的任何誤解或錯誤解釋概不負責。