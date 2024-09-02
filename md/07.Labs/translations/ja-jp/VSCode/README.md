# Microsoft Phi-3ファミリーを使用して独自のVisual Studio Code GitHub Copilot Chatを構築する

GitHub Copilot Chatでワークスペースエージェントを使用したことがありますか？独自のチームのコードエージェントを構築したいですか？このハンズオンラボでは、オープンソースモデルを組み合わせて、企業レベルのコードビジネスエージェントを構築することを目指しています。

## 基礎

### なぜMicrosoft Phi-3を選ぶのか

Phi-3は、テキスト生成、対話補完、コード生成のための異なるトレーニングパラメータに基づくphi-3-mini、phi-3-small、phi-3-mediumを含むファミリーシリーズです。また、Visionに基づくphi-3-visionもあります。これは、企業や異なるチームがオフラインの生成AIソリューションを作成するのに適しています。

このリンクを読むことをお勧めします [https://github.com/microsoft/Phi-3CookBook/blob/main/md/01.Introduce/Phi3Family.md](https://github.com/microsoft/Phi-3CookBook/blob/main/md/01.Introduce/Phi3Family.md)

### Microsoft GitHub Copilot Chat

GitHub Copilot Chat拡張機能は、GitHub Copilotと対話し、VS Code内で直接コーディング関連の質問に対する回答を受け取るためのチャットインターフェースを提供します。これにより、ドキュメントをナビゲートしたり、オンラインフォーラムを検索したりする必要がなくなります。

Copilot Chatは、生成された応答に明確さを加えるために、構文のハイライト、インデント、およびその他のフォーマット機能を使用することがあります。ユーザーの質問の種類に応じて、結果には、Copilotが応答を生成するために使用したコンテキストへのリンク（ソースコードファイルやドキュメントなど）や、VS Codeの機能にアクセスするためのボタンが含まれることがあります。

- Copilot Chatは、開発者のフローに統合され、必要な場所で支援を提供します：

- コーディング中にヘルプを得るために、エディタやターミナルから直接インラインチャットを開始します

- サイドバーのChatビューを使用して、いつでもAIアシスタントのヘルプを受けることができます

- Quick Chatを起動して、迅速に質問し、作業に戻ることができます

GitHub Copilot Chatは、次のようなさまざまなシナリオで使用できます：

- 問題を最適に解決する方法に関するコーディングの質問に回答する

- 他人のコードを説明し、改善提案を行う

- コード修正の提案を行う

- 単体テストケースを生成する

- コードドキュメントを生成する

このリンクを読むことをお勧めします [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/copilot-chat?WT.mc_id=aiml-137032-kinfeylo)

### Microsoft GitHub Copilot Chat @workspace

Copilot Chatで**@workspace**を参照すると、コードベース全体に関する質問をすることができます。質問に基づいて、Copilotは関連するファイルやシンボルをインテリジェントに取得し、リンクやコード例として回答に引用します。

質問に答えるために、**@workspace**は、開発者がVS Codeでコードベースをナビゲートする際に使用するのと同じソースを検索します：

- .gitignoreファイルによって無視されるファイルを除く、ワークスペース内のすべてのファイル

- ネストされたフォルダとファイル名を含むディレクトリ構造

- ワークスペースがGitHubリポジトリであり、コード検索によってインデックスが作成されている場合、GitHubのコード検索インデックス

- ワークスペース内のシンボルと定義

- 現在選択されているテキストまたはアクティブなエディタ内の表示テキスト

注意：無視されたファイル内でテキストを選択している場合、またはファイルを開いている場合、.gitignoreは無視されます。

このリンクを読むことをお勧めします [https://code.visualstudio.com/docs/copilot/copilot-chat](https://code.visualstudio.com/docs/copilot/workspace-context?WT.mc_id=aiml-137032-kinfeylo)

## このラボについて詳しく知る

GitHub Copilotは企業のプログラミング効率を大幅に向上させ、すべての企業がGitHub Copilotの関連機能をカスタマイズすることを望んでいます。多くの企業は、自社のビジネスシナリオとオープンソースモデルに基づいて、GitHub Copilotに似た拡張機能をカスタマイズしています。企業にとって、カスタマイズされた拡張機能は制御が容易ですが、これもユーザーエクスペリエンスに影響を与えます。結局のところ、GitHub Copilotは一般的なシナリオと専門性の処理においてより強力な機能を持っています。エクスペリエンスを一貫して保つことができれば、企業独自の拡張機能をカスタマイズする方が良いでしょう。GitHub Copilot Chatは、企業がChatエクスペリエンスで拡張するための関連APIを提供します。一貫したエクスペリエンスを維持し、カスタマイズされた機能を持つことがより良いユーザーエクスペリエンスです。

このラボでは、主にPhi-3モデルを使用し、ローカルNPUとAzureハイブリッドを組み合わせて、GitHub Copilot Chat ***@PHI3***でカスタムエージェントを構築し、企業の開発者がコード生成***(@PHI3 /gen)***および画像に基づいてコードを生成する***(@PHI3 /img)***のを支援します。

![PHI3](../../../../../imgs/07/01/cover.png)

### 注意：

このラボは現在、Intel CPUおよびApple SiliconのAIPCで実装されています。QualcommバージョンのNPUの更新を続けます。

## ラボ

| 名前 | 説明 | AIPC | Apple |
| ------------ | ----------- | -------- |-------- |
| Lab0 - インストール(✅) | 関連する環境とインストールツールを設定およびインストールする | [開始](./HOL/AIPC/01.Installations.md) |[開始](./HOL/Apple/01.Installations.md) |
| Lab1 - Phi-3-miniを使用してPrompt flowを実行する (✅) | AIPC / Apple Siliconと組み合わせて、ローカルNPUを使用してPhi-3-miniを通じてコード生成を作成する | [開始](./HOL/AIPC/02.PromptflowWithNPU.md) |  [開始](./HOL/Apple/02.PromptflowWithMLX.md) |
| Lab2 - Azure Machine Learning ServiceにPhi-3-visionをデプロイする(✅) | Azure Machine Learning ServiceのModel Catalog - Phi-3-visionイメージをデプロイしてコードを生成する | [開始](./HOL/AIPC/03.DeployPhi3VisionOnAzure.md) |[開始](./HOL/Apple/03.DeployPhi3VisionOnAzure.md) |
| Lab3 - GitHub Copilot Chatで@phi-3エージェントを作成する(✅)  | GitHub Copilot ChatでカスタムPhi-3エージェントを作成して、コード生成、グラフ生成コード、RAGなどを完了する | [開始](./HOL/AIPC/04.CreatePhi3AgentInVSCode.md) | [開始](./HOL/Apple/04.CreatePhi3AgentInVSCode.md) |
| サンプルコード (✅)  | サンプルコードをダウンロードする | [開始](../../../../../code/07.Lab/translations/ja-jp/01/AIPC/) | [開始](../../../../../code/07.Lab/translations/ja-jp/01/Apple/) |

## リソース

1. Phi-3 Cookbook [https://github.com/microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook)

2. GitHub Copilotの詳細を学ぶ [https://learn.microsoft.com/training/paths/copilot/](https://learn.microsoft.com/training/paths/copilot/?WT.mc_id=aiml-137032-kinfeylo)

3. GitHub Copilot Chatの詳細を学ぶ [https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/](https://learn.microsoft.com/training/paths/accelerate-app-development-using-github-copilot/?WT.mc_id=aiml-137032-kinfeylo)

4. GitHub Copilot Chat APIの詳細を学ぶ [https://code.visualstudio.com/api/extension-guides/chat](https://code.visualstudio.com/api/extension-guides/chat?WT.mc_id=aiml-137032-kinfeylo)

5. Azure AI Studioの詳細を学ぶ [https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/](https://learn.microsoft.com/training/paths/create-custom-copilots-ai-studio/?WT.mc_id=aiml-137032-kinfeylo)

6. Azure AI StudioのModel Catalogの詳細を学ぶ [https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview](https://learn.microsoft.com/azure/ai-studio/how-to/model-catalog-overview)
