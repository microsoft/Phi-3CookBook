# **Microsoft Phi-3 ファミリーで自分の Visual Studio Code GitHub Copilot Chat を作成しよう**

GitHub Copilot Chat のワークスペースエージェントを使ったことがありますか？自分のチームのコードエージェントを作りたいと思ったことはありませんか？このハンズオンラボでは、オープンソースモデルを組み合わせてエンタープライズレベルのコードビジネスエージェントを構築することを目指しています。

## **基礎**

### **なぜ Microsoft Phi-3 を選ぶのか**

Phi-3 はファミリーシリーズで、テキスト生成、対話完了、コード生成のために異なるトレーニングパラメータに基づく phi-3-mini、phi-3-small、phi-3-medium があります。また、Vision に基づく phi-3-vision もあります。これは、企業や異なるチームがオフライン生成 AI ソリューションを作成するのに適しています。

このリンクを読むことをお勧めします [https://github.com/microsoft/Phi-3CookBook/blob/main/md/01.Introduce/Phi3Family.md](https://github.com/microsoft/Phi-3CookBook/blob/main/md/01.Introduce/Phi3Family.md)

### **Microsoft GitHub Copilot Chat**

GitHub Copilot Chat 拡張機能は、チャットインターフェイスを提供し、VS Code 内で直接コーディング関連の質問に対する回答を受け取ることができます。ドキュメントを参照したり、オンラインフォーラムを検索する必要はありません。

Copilot Chat は、シンタックスハイライト、インデント、その他のフォーマット機能を使用して、生成された回答を明確にすることがあります。ユーザーからの質問の種類に応じて、回答にはソースコードファイルやドキュメントへのリンク、または VS Code 機能にアクセスするためのボタンが含まれることがあります。

- Copilot Chat は開発者のフローに統合され、必要な場所でサポートを提供します：

- エディタやターミナルから直接インラインチャットを開始して、コーディング中にサポートを受ける

- Chat ビューを使用して、いつでもサポートを受けられる AI アシスタントをサイドに配置

- クイックチャットを開始して、簡単な質問をして作業に戻る

GitHub Copilot Chat は、次のようなシナリオで使用できます：

- 問題を最適に解決する方法に関するコーディング質問に回答

- 他人のコードを説明し、改善点を提案

- コード修正を提案

- ユニットテストケースの生成

- コードドキュメントの生成

このリンクを読むことをお勧めします [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

###  **Microsoft GitHub Copilot Chat @workspace**

Copilot Chat で **@workspace** を参照すると、コードベース全体について質問することができます。質問に基づいて、Copilot は関連するファイルやシンボルをインテリジェントに取得し、リンクやコード例として回答に反映します。

**@workspace** は、VS Code でコードベースをナビゲートする際に開発者が使用する同じソースを検索して質問に回答します：

- .gitignore ファイルによって無視されるファイルを除く、ワークスペース内のすべてのファイル

- ネストされたフォルダやファイル名を含むディレクトリ構造

- ワークスペースが GitHub リポジトリであり、コード検索によってインデックスされている場合、GitHub のコード検索インデックス

- ワークスペース内のシンボルと定義

- アクティブなエディタ内の現在選択されているテキストまたは表示されているテキスト

注: .gitignore は、無視されているファイルを開いたり、その中のテキストを選択している場合はバイパスされます。

このリンクを読むことをお勧めします [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)

## **このラボについてもっと知る**

GitHub Copilot は企業のプログラミング効率を大幅に向上させました。すべての企業は GitHub Copilot の関連機能をカスタマイズしたいと考えています。多くの企業は、自社のビジネスシナリオとオープンソースモデルに基づいて、GitHub Copilot に似た拡張機能をカスタマイズしています。企業にとって、カスタマイズされた拡張機能は制御しやすいですが、これもユーザーエクスペリエンスに影響を与えます。結局のところ、GitHub Copilot は一般的なシナリオや専門性において強力な機能を持っています。エクスペリエンスを一貫させながら、企業独自の拡張機能をカスタマイズできればより良いでしょう。GitHub Copilot Chat は、企業がチャットエクスペリエンスを拡張するための関連 API を提供しています。一貫したエクスペリエンスを維持しながらカスタマイズ機能を持つことが、より良いユーザーエクスペリエンスです。

このラボでは主に、Phi-3 モデルを使用してローカル NPU と Azure ハイブリッドを組み合わせ、GitHub Copilot Chat 内でカスタムエージェント ***@PHI3*** を構築し、企業の開発者がコード生成を完了するのを支援します ***(@PHI3 /gen)*** および画像に基づいてコードを生成します ***(@PHI3 /img)***。

![PHI3](../../../../../translated_images/cover.d430b054ed524c747b7ab90cf1b12cbf65dbc199017fbd08ce9fab9f47204e03.ja.png)

### ***注意:*** 

このラボは現在、Intel CPU および Apple Silicon の AIPC で実装されています。Qualcomm バージョンの NPU も継続的に更新していきます。

## **ラボ**

| 名前 | 説明 | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - インストール (✅) | 関連環境とインストールツールの設定とインストール | [Go](./HOL/AIPC/01.Installations.md) |[Go](./HOL/Apple/01.Installations.md) |
| Lab1 - Phi-3-mini でプロンプトフローを実行 (✅) | AIPC / Apple Silicon と組み合わせて、ローカル NPU を使用して Phi-3-mini を通じてコード生成を作成 | [Go](./HOL/AIPC/02.PromptflowWithNPU.md) |  [Go](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Azure Machine Learning Service で Phi-3-vision をデプロイ (✅) | Azure Machine Learning Service のモデルカタログ - Phi-3-vision 画像をデプロイしてコードを生成 | [Go](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[Go](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - GitHub Copilot Chat で @phi-3 エージェントを作成 (✅)  | GitHub Copilot Chat でカスタム Phi-3 エージェントを作成し、コード生成、グラフ生成コード、RAG などを完了 | [Go](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [Go](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| サンプルコード (✅)  | サンプルコードをダウンロード | [Go](../../../../../code/07.Lab/01/AIPC) | [Go](../../../../../code/07.Lab/01/Apple) |

## **リソース**

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. GitHub Copilot についてもっと学ぶ [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. GitHub Copilot Chat についてもっと学ぶ [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. GitHub Copilot Chat API についてもっと学ぶ [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Azure AI Studio についてもっと学ぶ [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Azure AI Studio のモデルカタログについてもっと学ぶ [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)

