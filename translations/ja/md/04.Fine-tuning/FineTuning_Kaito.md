## Kaitoでのファインチューニング

[Kaito](https://github.com/Azure/kaito) は、KubernetesクラスターにおけるAI/ML推論モデルのデプロイメントを自動化するオペレーターです。

Kaitoは、仮想マシンインフラストラクチャ上に構築された主流のモデルデプロイメント手法と比較して、以下の重要な差別化ポイントがあります：

- コンテナイメージを使用してモデルファイルを管理します。モデルライブラリを使用して推論呼び出しを行うためのhttpサーバーが提供されます。
- プリセット構成を提供することで、GPUハードウェアに合わせたデプロイメントパラメータの調整を避けます。
- モデルの要件に基づいてGPUノードを自動プロビジョニングします。
- ライセンスが許可する場合、大規模なモデルイメージをMicrosoft Container Registry (MCR)にホストします。

Kaitoを使用することで、Kubernetesにおける大規模なAI推論モデルのオンボーディングのワークフローが大幅に簡素化されます。

## アーキテクチャ

Kaitoは、クラシックなKubernetesのCustom Resource Definition(CRD)/コントローラーデザインパターンに従います。ユーザーは、GPU要件と推論仕様を記述する`workspace`カスタムリソースを管理します。Kaitoコントローラーは、`workspace`カスタムリソースを調整することでデプロイメントを自動化します。
<div align="left">
  <img src="https://github.com/Azure/kaito/blob/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

上の図は、Kaitoのアーキテクチャ概要を示しています。主なコンポーネントは以下の通りです：

- **ワークスペースコントローラー**：`workspace`カスタムリソースを調整し、ノードの自動プロビジョニングをトリガーする`machine`（以下で説明）カスタムリソースを作成し、モデルのプリセット構成に基づいて推論ワークロード（`deployment`または`statefulset`）を作成します。
- **ノードプロビジョナーコントローラー**：このコントローラーの名前は、[gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)では*gpu-provisioner*です。これは、[Karpenter](https://sigs.k8s.io/karpenter)から派生した`machine` CRDを使用してワークスペースコントローラーと対話します。Azure Kubernetes Service(AKS)のAPIと統合し、新しいGPUノードをAKSクラスターに追加します。
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner) はオープンソースのコンポーネントです。他のコントローラーが[Karpenter-core](https://sigs.k8s.io/karpenter) APIをサポートしている場合、それらと置き換えることができます。

## 概要ビデオ 
[Kaitoデモを見る](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)
## インストール

インストールガイドは[こちら](https://github.com/Azure/kaito/blob/main/docs/installation.md)をご覧ください。

## クイックスタート

Kaitoをインストールした後、以下のコマンドを試してファインチューニングサービスを開始できます。

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

ワークスペースのステータスは、以下のコマンドを実行することで追跡できます。WORKSPACEREADY列が`True`になると、モデルが正常にデプロイされていることを示します。

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

次に、推論サービスのクラスターIPを見つけ、一時的な`curl`ポッドを使用してクラスター内のサービスエンドポイントをテストします。

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**免責事項**:
この文書は機械翻訳サービスを使用して翻訳されています。正確さを期していますが、自動翻訳にはエラーや不正確さが含まれる場合がありますのでご注意ください。原文が権威ある情報源とみなされるべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用に起因する誤解や誤った解釈について、当社は一切の責任を負いません。