## Kaito での推論

[Kaito](https://github.com/Azure/kaito) は、Kubernetes クラスター内で AI/ML 推論モデルのデプロイを自動化するオペレーターです。

Kaito は、仮想マシンインフラストラクチャの上に構築された主流のモデルデプロイ手法と比較して、以下の重要な差別化要素があります：

- コンテナイメージを使用してモデルファイルを管理します。モデルライブラリを使用して推論呼び出しを行うための http サーバーが提供されます。
- プリセット構成を提供することで、GPU ハードウェアに適合するようにデプロイパラメーターを調整する必要を避けます。
- モデルの要件に基づいて GPU ノードを自動プロビジョニングします。
- ライセンスが許可する場合、大規模なモデルイメージをパブリック Microsoft Container Registry (MCR) にホストします。

Kaito を使用することで、Kubernetes での大規模 AI 推論モデルのオンボーディングのワークフローが大幅に簡素化されます。

## アーキテクチャ

Kaito は、クラシックな Kubernetes Custom Resource Definition (CRD) / コントローラーデザインパターンに従っています。ユーザーは GPU 要件と推論仕様を記述した `workspace` カスタムリソースを管理します。Kaito コントローラーは、この `workspace` カスタムリソースを調整することでデプロイを自動化します。
<div align="left">
  <img src="https://github.com/Azure/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

上図は Kaito アーキテクチャの概要を示しています。その主要なコンポーネントは以下の通りです：

- **Workspace コントローラー**：`workspace` カスタムリソースを調整し、ノードの自動プロビジョニングをトリガーする `machine` (後述) カスタムリソースを作成し、モデルのプリセット構成に基づいて推論ワークロード (`deployment` または `statefulset`) を作成します。
- **Node プロビジョナーコントローラー**：このコントローラーの名前は [gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner) の *gpu-provisioner* です。これは、[Karpenter](https://sigs.k8s.io/karpenter) から派生した `machine` CRD を使用して Workspace コントローラーと対話します。Azure Kubernetes Service (AKS) API と統合して、AKS クラスターに新しい GPU ノードを追加します。
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) はオープンソースコンポーネントです。他のコントローラーが [Karpenter-core](https://sigs.k8s.io/karpenter) API をサポートしている場合、それらに置き換えることができます。

## インストール

インストールガイダンスは [こちら](https://github.com/Azure/kaito/blob/main/docs/installation.md) をご覧ください。

## クイックスタート推論 Phi-3
[サンプルコード推論 Phi-3](https://github.com/Azure/kaito/tree/main/examples/inference)

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

次のコマンドを実行して Workspace のステータスを追跡できます。WORKSPACEREADY カラムが `True` になると、モデルが正常にデプロイされたことを示します。

```sh
$ kubectl get workspace kaito_workspace_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini   Standard_NC6s_v3   True            True             True             10m
```

次に、推論サービスのクラスター IP を見つけ、一時的な `curl` ポッドを使用してクラスター内のサービスエンドポイントをテストできます。

```sh
$ kubectl get svc workspace-phi-3-mini
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

## クイックスタート推論 Phi-3 with adapters

Kaito をインストールした後、以下のコマンドを試して推論サービスを開始できます。

[サンプルコード推論 Phi-3 with Adapters](https://github.com/Azure/kaito/blob/main/examples/inference/kaito_workspace_phi_3_with_adapters.yaml)

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

次のコマンドを実行して Workspace のステータスを追跡できます。WORKSPACEREADY カラムが `True` になると、モデルが正常にデプロイされたことを示します。

```sh
$ kubectl get workspace kaito_workspace_phi_3_with_adapters.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-phi-3-mini-adapter   Standard_NC6s_v3   True            True             True             10m
```

次に、推論サービスのクラスター IP を見つけ、一時的な `curl` ポッドを使用してクラスター内のサービスエンドポイントをテストできます。

```sh
$ kubectl get svc workspace-phi-3-mini-adapter
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-phi-3-mini-adapter  ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-phi-3-mini-adapter -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**免責事項**:
この文書は機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期していますが、自動翻訳には誤りや不正確さが含まれる場合があることにご注意ください。元の言語での原文を権威ある情報源と見なすべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用によって生じたいかなる誤解や誤訳についても、当社は責任を負いません。