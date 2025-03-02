## Kaitoでの推論

[Kaito](https://github.com/Azure/kaito) は、Kubernetesクラスター内でAI/ML推論モデルのデプロイを自動化するオペレーターです。

Kaitoは、従来の仮想マシンインフラストラクチャ上に構築された主流のモデルデプロイ手法と比較して、以下のような主要な差別化ポイントがあります：

- コンテナイメージを使用してモデルファイルを管理。モデルライブラリを使用して推論呼び出しを行うためのHTTPサーバーを提供。
- GPUハードウェアに合わせてデプロイパラメータを調整する必要をなくし、事前設定された構成を提供。
- モデル要件に基づいてGPUノードを自動的にプロビジョニング。
- ライセンスが許可する場合、大規模なモデルイメージをMicrosoft Container Registry (MCR) にホスト。

Kaitoを使用することで、Kubernetesにおける大規模AI推論モデルのオンボーディングワークフローが大幅に簡素化されます。

## アーキテクチャ

Kaitoは、クラシックなKubernetesのCustom Resource Definition (CRD) / コントローラーデザインパターンに従っています。ユーザーは、GPU要件と推論仕様を記述した`workspace`カスタムリソースを管理します。Kaitoコントローラーが`workspace`カスタムリソースを調整してデプロイを自動化します。
<div align="left">
  <img src="https://github.com/kaito-project/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

上記の図は、Kaitoのアーキテクチャ概要を示しています。主なコンポーネントは以下の通りです：

- **ワークスペースコントローラー**: `workspace`カスタムリソースを調整し、ノードの自動プロビジョニングをトリガーする`machine`（以下で説明）カスタムリソースを作成し、モデルの事前設定構成に基づいて推論ワークロード（`deployment`または`statefulset`）を作成します。
- **ノードプロビジョナーコントローラー**: このコントローラーの名前は[*gpu-provisioner*](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)です。`machine` CRDを使用してワークスペースコントローラーと連携します。このCRDは[Karpenter](https://sigs.k8s.io/karpenter)から派生しています。Azure Kubernetes Service (AKS) のAPIと統合し、AKSクラスターに新しいGPUノードを追加します。
> 注: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) はオープンソースのコンポーネントです。他のコントローラーが[Karpenter-core](https://sigs.k8s.io/karpenter) APIをサポートしている場合、それらに置き換えることができます。

## インストール

インストール手順については[こちら](https://github.com/Azure/kaito/blob/main/docs/installation.md)をご確認ください。

## Phi-3推論のクイックスタート
[Phi-3推論のサンプルコード](https://github.com/Azure/kaito/tree/main/examples/inference)

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

以下のコマンドを実行してワークスペースのステータスを追跡できます。`WORKSPACEREADY`列が`True`になると、モデルが正常にデプロイされたことを示します。

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

次に、推論サービスのクラスターIPを確認し、一時的な`curl`ポッドを使用してクラスター内のサービスエンドポイントをテストできます。

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## アダプター付きPhi-3推論のクイックスタート

Kaitoをインストールした後、以下のコマンドを実行して推論サービスを開始できます。

[アダプター付きPhi-3推論のサンプルコード](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

以下のコマンドを実行してワークスペースのステータスを追跡できます。`WORKSPACEREADY`列が`True`になると、モデルが正常にデプロイされたことを示します。

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

次に、推論サービスのクラスターIPを確認し、一時的な`curl`ポッドを使用してクラスター内のサービスエンドポイントをテストできます。

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**免責事項**:  
本書類は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを追求しておりますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知おきください。原文（元の言語で記載された文書）が信頼できる情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。