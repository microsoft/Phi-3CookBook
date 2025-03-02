## Kaitoを使ったファインチューニング

[Kaito](https://github.com/Azure/kaito) は、Kubernetesクラスタ内でAI/ML推論モデルのデプロイを自動化するオペレーターです。

Kaitoは、仮想マシンインフラストラクチャ上に構築された主流のモデルデプロイ方法と比較して、以下のような主な特徴を持っています：

- コンテナイメージを使用してモデルファイルを管理します。モデルライブラリを使った推論呼び出しを実行するためのHTTPサーバーを提供します。
- GPUハードウェアに適合させるためのデプロイパラメータの調整を、プリセット構成によって不要にします。
- モデルの要件に基づいてGPUノードを自動的にプロビジョニングします。
- ライセンスが許可する場合、大規模なモデルイメージをMicrosoft Container Registry (MCR) にホストします。

Kaitoを使用することで、Kubernetesにおける大規模AI推論モデルの導入ワークフローが大幅に簡素化されます。

## アーキテクチャ

Kaitoは、クラシックなKubernetesのカスタムリソース定義(CRD)/コントローラーデザインパターンに従っています。ユーザーは、GPU要件と推論仕様を記述した`workspace`カスタムリソースを管理します。Kaitoコントローラーは、`workspace`カスタムリソースを調整することでデプロイを自動化します。
<div align="left">
  <img src="https://github.com/kaito-project/kaito/raw/main/docs/img/arch.png" width=80% title="Kaito architecture" alt="Kaito architecture">
</div>

上記の図はKaitoアーキテクチャの概要を示しています。主なコンポーネントは以下の通りです：

- **Workspace controller**: `workspace`カスタムリソースを調整し、ノード自動プロビジョニングをトリガーするための`machine`（後述）カスタムリソースを作成し、モデルのプリセット構成に基づいて推論ワークロード（`deployment`または`statefulset`）を作成します。
- **Node provisioner controller**: コントローラーの名前は、[gpu-provisioner helm chart](https://github.com/Azure/gpu-provisioner/tree/main/charts/gpu-provisioner)内の*gpu-provisioner*です。[Karpenter](https://sigs.k8s.io/karpenter)から派生した`machine` CRDを使用してWorkspace controllerと連携します。Azure Kubernetes Service(AKS) APIと統合し、AKSクラスタに新しいGPUノードを追加します。
> Note: [*gpu-provisioner*](https://github.com/Azure/gpu-provisioner)はオープンソースのコンポーネントです。他のコントローラーが[Karpenter-core](https://sigs.k8s.io/karpenter) APIをサポートしている場合、それらに置き換えることが可能です。

## 概要ビデオ 
[Kaitoのデモを見る](https://www.youtube.com/embed/pmfBSg7L6lE?si=b8hXKJXb1gEZcmAe)

## インストール

インストールガイドについては[こちら](https://github.com/Azure/kaito/blob/main/docs/installation.md)をご確認ください。

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

以下のコマンドを実行することで、ワークスペースのステータスを確認できます。WORKSPACEREADY列が`True`になると、モデルが正常にデプロイされたことを示します。

```sh
$ kubectl get workspace kaito_workspace_tuning_phi_3.yaml
NAME                  INSTANCE            RESOURCEREADY   INFERENCEREADY   WORKSPACEREADY   AGE
workspace-tuning-phi-3   Standard_NC6s_v3   True            True             True             10m
```

次に、推論サービスのクラスタIPを確認し、クラスタ内の一時的な`curl`ポッドを使用してサービスエンドポイントをテストできます。

```sh
$ kubectl get svc workspace_tuning
NAME                  TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)            AGE
workspace-tuning-phi-3   ClusterIP   <CLUSTERIP>  <none>        80/TCP,29500/TCP   10m

export CLUSTERIP=$(kubectl get svc workspace-tuning-phi-3 -o jsonpath="{.spec.clusterIPs[0]}") 
$ kubectl run -it --rm --restart=Never curl --image=curlimages/curl -- curl -X POST http://$CLUSTERIP/chat -H "accept: application/json" -H "Content-Type: application/json" -d "{\"prompt\":\"YOUR QUESTION HERE\"}"
```

**免責事項**:  
本書類は、機械翻訳AIサービスを使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があります。元の言語で記載された原文を信頼できる情報源としてお考えください。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用に起因する誤解や解釈の相違について、当方は一切の責任を負いかねます。