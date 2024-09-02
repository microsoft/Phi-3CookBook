# **Azure AI Studio を使用した評価**

![aistudo](../../../../imgs/05/AIStudio/AIStudio.png)

[Azure AI Studio](https://ai.azure.com?WT.mc_id=aiml-138114-kinfeylo) を使用して生成 AI アプリケーションを評価する方法。単一ターンまたはマルチターンの会話を評価する場合でも、Azure AI Studio はモデルのパフォーマンスと安全性を評価するためのツールを提供します。

![aistudo](../../../../imgs/05/AIStudio/AIPortfolio.png)

## Azure AI Studio を使用して生成 AI アプリを評価する方法
詳細な手順については、[Azure AI Studio ドキュメント](https://learn.microsoft.com/azure/ai-studio/how-to/evaluate-generative-ai-app?WT.mc_id=aiml-138114-kinfeylo) を参照してください。

以下は開始するための手順です。

## Azure AI Studio で生成 AI モデルを評価する

**前提条件**

- CSV または JSON 形式のテスト データセット。
- デプロイされた生成 AI モデル (Phi-3、GPT 3.5、GPT 4、または Davinci モデルなど)。
- 評価を実行するためのコンピューティング インスタンスを持つランタイム。

## 組み込みの評価指標

Azure AI Studio を使用すると、単一ターンおよび複雑なマルチターンの会話を評価できます。
特定のデータに基づいてモデルがグラウンドされる検索強化生成 (RAG) シナリオの場合、組み込みの評価指標を使用してパフォーマンスを評価できます。
さらに、一般的な単一ターンの質問応答シナリオ (非 RAG) を評価できます。

## 評価の実行の作成

Azure AI Studio UI から、[評価] ページまたは [Prompt Flow] ページに移動します。
評価作成ウィザードに従って評価の実行を設定します。評価にオプションの名前を指定します。
アプリケーションの目的に一致するシナリオを選択します。
モデルの出力を評価するために 1 つ以上の評価指標を選択します。

## カスタム評価フロー (オプション)

柔軟性を高めるために、カスタム評価フローを確立できます。特定の要件に基づいて評価プロセスをカスタマイズします。

## 結果の表示

評価を実行した後、Azure AI Studio で詳細な評価指標を記録、表示、および分析します。アプリケーションの機能と制限についての洞察を得ます。

**注** Azure AI Studio は現在パブリック プレビュー中であるため、実験および開発目的で使用してください。運用ワークロードの場合は、他のオプションを検討してください。詳細および段階的な手順については、公式の [AI Studio ドキュメント](https://learn.microsoft.com/azure/ai-studio/?WT.mc_id=aiml-138114-kinfeylo) を参照してください。
