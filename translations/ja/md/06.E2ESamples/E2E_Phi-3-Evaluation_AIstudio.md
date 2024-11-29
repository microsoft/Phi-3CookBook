# Azure AI Foundry で Microsoft の責任ある AI 原則に焦点を当てた Fine-tuned Phi-3 / Phi-3.5 モデルの評価

このエンドツーエンド（E2E）サンプルは、Microsoft Tech Community のガイド「[Azure AI Foundry での Microsoft の責任ある AI に焦点を当てた Fine-tuned Phi-3 / 3.5 モデルの評価](https://techcommunity.microsoft.com/t5/educator-developer-blog/evaluate-fine-tuned-phi-3-3-5-models-in-azure-ai-studio-focusing/ba-p/4227850?WT.mc_id=aiml-137032-kinfeylo)」に基づいています。

## 概要

### Azure AI Foundry で Fine-tuned Phi-3 / Phi-3.5 モデルの安全性とパフォーマンスをどのように評価できますか？

モデルの微調整は時に意図しない、または望ましくない応答を引き起こすことがあります。モデルが安全かつ効果的であり続けるためには、有害なコンテンツを生成する可能性や、正確で関連性のある一貫した応答を生成する能力を評価することが重要です。このチュートリアルでは、Azure AI Foundry の Prompt flow と統合された Fine-tuned Phi-3 / Phi-3.5 モデルの安全性とパフォーマンスを評価する方法を学びます。

以下は、Azure AI Foundry の評価プロセスです。

![チュートリアルのアーキテクチャ](../../../../translated_images/architecture.1eb9d143d0771c6065f16c0f66a9eb233f466cdf9db0b0afe11adcbd57eb06ce.ja.png)

*画像ソース: [生成 AI アプリケーションの評価](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
>
> Phi-3 / Phi-3.5 についての詳細情報や追加リソースについては、[Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723) をご覧ください。

### 前提条件

- [Python](https://www.python.org/downloads)
- [Azure サブスクリプション](https://azure.microsoft.com/free?wt.mc_id=studentamb_279723)
- [Visual Studio Code](https://code.visualstudio.com)
- Fine-tuned Phi-3 / Phi-3.5 モデル

### 目次

1. [**シナリオ 1: Azure AI Foundry の Prompt flow 評価の紹介**](../../../../md/06.E2ESamples)

    - [安全性評価の紹介](../../../../md/06.E2ESamples)
    - [パフォーマンス評価の紹介](../../../../md/06.E2ESamples)

1. [**シナリオ 2: Azure AI Foundry で Phi-3 / Phi-3.5 モデルを評価する**](../../../../md/06.E2ESamples)

    - [開始前に](../../../../md/06.E2ESamples)
    - [Phi-3 / Phi-3.5 モデルを評価するための Azure OpenAI のデプロイ](../../../../md/06.E2ESamples)
    - [Azure AI Foundry の Prompt flow 評価を使用して Fine-tuned Phi-3 / Phi-3.5 モデルを評価する](../../../../md/06.E2ESamples)

1. [おめでとうございます！](../../../../md/06.E2ESamples)

## **シナリオ 1: Azure AI Foundry の Prompt flow 評価の紹介**

### 安全性評価の紹介

AI モデルが倫理的で安全であることを確認するためには、Microsoft の責任ある AI 原則に基づいて評価することが重要です。Azure AI Foundry では、安全性評価を通じて、モデルが jailbreak 攻撃に対する脆弱性や有害なコンテンツを生成する可能性を評価することができます。これにより、これらの原則に直接一致させることができます。

![安全性評価](../../../../translated_images/safety-evaluation.5ad906c4618e4c8736fdeeff54a52dac8ae6d0756b15824e430177fba7b6a8b4.ja.png)

*画像ソース: [生成 AI アプリケーションの評価](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### Microsoft の責任ある AI 原則

技術的なステップを始める前に、Microsoft の責任ある AI 原則を理解することが重要です。これらの原則は、AI システムの責任ある開発、展開、および運用をガイドするための倫理的な枠組みです。これらの原則は、AI 技術が公平で透明性があり、包括的に設計、開発、および展開されることを保証します。これらの原則は、AI モデルの安全性を評価するための基盤です。

Microsoft の責任ある AI 原則には以下が含まれます：

- **公平性と包括性**: AI システムは全ての人々を公平に扱い、同様の状況にある人々のグループに異なる影響を与えないようにするべきです。例えば、AI システムが医療の治療、ローン申請、または雇用に関するガイダンスを提供する際には、同様の症状、財務状況、または職業資格を持つ全ての人々に同じ推奨を行うべきです。

- **信頼性と安全性**: 信頼を築くためには、AI システムが信頼性、安全性、一貫性を持って動作することが重要です。これらのシステムは、設計された通りに動作し、予期しない条件に安全に対応し、有害な操作に抵抗できる必要があります。これらのシステムの動作と対応できる条件の範囲は、設計とテストの過程で開発者が予想した状況や状況の範囲を反映しています。

- **透明性**: AI システムが人々の生活に大きな影響を与える決定を支援する場合、人々がその決定がどのように行われたかを理解することが重要です。例えば、銀行が AI システムを使用して人の信用度を判断する場合、企業が AI システムを使用して最も適格な候補者を選定する場合などです。

- **プライバシーとセキュリティ**: AI が普及するにつれて、プライバシーの保護と個人および企業情報のセキュリティはますます重要かつ複雑になっています。AI では、データへのアクセスが正確で情報に基づいた予測や決定を行うために不可欠であるため、プライバシーとデータセキュリティには細心の注意が必要です。

- **アカウンタビリティ**: AI システムを設計および展開する人々は、そのシステムの動作に対して責任を負うべきです。組織は業界標準に基づいてアカウンタビリティの規範を開発するべきです。これらの規範は、AI システムが人々の生活に影響を与えるいかなる決定の最終権限を持たないことを保証できます。また、非常に自律的な AI システムに対しても人間が意味のあるコントロールを維持できるようにすることができます。

![フィルハブ](../../../../translated_images/responsibleai2.ae6f996d95dcc46b3b3087c0e4f4f4b74c64e961083009ecca7a0a3998b3f716.ja.png)

*画像ソース: [責任ある AI とは？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2&viewFallbackFrom=azureml-api-2%253fwt.mc_id%3Dstudentamb_279723)*

> [!NOTE]
> Microsoft の責任ある AI 原則についての詳細は、[責任ある AI とは？](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723) をご覧ください。

#### 安全性メトリクス

このチュートリアルでは、Azure AI Foundry の安全性メトリクスを使用して Fine-tuned Phi-3 モデルの安全性を評価します。これらのメトリクスは、モデルが有害なコンテンツを生成する可能性や jailbreak 攻撃に対する脆弱性を評価するのに役立ちます。安全性メトリクスには以下が含まれます：

- **自傷行為に関連するコンテンツ**: モデルが自傷行為に関連するコンテンツを生成する傾向があるかどうかを評価します。
- **憎悪的および不公平なコンテンツ**: モデルが憎悪的または不公平なコンテンツを生成する傾向があるかどうかを評価します。
- **暴力的なコンテンツ**: モデルが暴力的なコンテンツを生成する傾向があるかどうかを評価します。
- **性的コンテンツ**: モデルが不適切な性的コンテンツを生成する傾向があるかどうかを評価します。

これらの側面を評価することで、AI モデルが有害または攻撃的なコンテンツを生成しないことを保証し、社会的な価値観や規制基準に一致させることができます。

![安全性に基づいて評価する](../../../../translated_images/evaluate-based-on-safety.63d79ac01570713002d5d858bfbb8f4d7295557ae8829d0c379485d67a3fcd1c.ja.png)

### パフォーマンス評価の紹介

AI モデルが期待通りに動作していることを確認するためには、パフォーマンスメトリクスに基づいてそのパフォーマンスを評価することが重要です。Azure AI Foundry では、パフォーマンス評価を通じて、モデルが正確で関連性のある一貫した応答を生成する効果を評価することができます。

![パフォーマンス評価](../../../../translated_images/performance-evaluation.259c44647c74a80761cdcbaab2202142f99a5a0d28326c8a1eb6dc2765f5ef77.ja.png)

*画像ソース: [生成 AI アプリケーションの評価](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)*

#### パフォーマンスメトリクス

このチュートリアルでは、Azure AI Foundry のパフォーマンスメトリクスを使用して Fine-tuned Phi-3 / Phi-3.5 モデルのパフォーマンスを評価します。これらのメトリクスは、モデルが正確で関連性のある一貫した応答を生成する効果を評価するのに役立ちます。パフォーマンスメトリクスには以下が含まれます：

- **根拠性**: 生成された回答が入力ソースの情報とどれだけ一致しているかを評価します。
- **関連性**: 生成された応答が与えられた質問にどれだけ関連しているかを評価します。
- **一貫性**: 生成されたテキストがどれだけ自然に流れ、人間の言語に似ているかを評価します。
- **流暢さ**: 生成されたテキストの言語能力を評価します。
- **GPT 類似性**: 生成された応答をグラウンドトゥルースと比較して類似性を評価します。
- **F1 スコア**: 生成された応答とソースデータ間の共有単語の比率を計算します。

これらのメトリクスは、モデルが正確で関連性のある一貫した応答を生成する効果を評価するのに役立ちます。

![パフォーマンスに基づいて評価する](../../../../translated_images/evaluate-based-on-performance.33ccf1c52f210af8e76d9cab863716d3f67db3d765254371a30136cc8f852b37.ja.png)

## **シナリオ 2: Azure AI Foundry で Phi-3 / Phi-3.5 モデルを評価する**

### 開始前に

このチュートリアルは、以前のブログ投稿「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)」および「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)」の続編です。これらの投稿では、Azure AI Foundry で Phi-3 / Phi-3.5 モデルを微調整し、Prompt flow と統合するプロセスを説明しました。

このチュートリアルでは、Azure AI Foundry で評価者として Azure OpenAI モデルをデプロイし、それを使用して Fine-tuned Phi-3 / Phi-3.5 モデルを評価します。

このチュートリアルを始める前に、以前のチュートリアルで説明した前提条件を満たしていることを確認してください：

1. Fine-tuned Phi-3 / Phi-3.5 モデルを評価するためのデータセットが準備されていること。
1. 微調整され、Azure Machine Learning にデプロイされた Phi-3 / Phi-3.5 モデルがあること。
1. Azure AI Foundry で Fine-tuned Phi-3 / Phi-3.5 モデルと統合された Prompt flow があること。

> [!NOTE]
> 以前のブログ投稿でダウンロードした **ULTRACHAT_200k** データセットのデータフォルダーにある *test_data.jsonl* ファイルを、Fine-tuned Phi-3 / Phi-3.5 モデルを評価するためのデータセットとして使用します。

#### Azure AI Foundry で Prompt flow とカスタム Phi-3 / Phi-3.5 モデルを統合する（コードファーストアプローチ）

> [!NOTE]
> 低コードアプローチを使用した場合、「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow in Azure AI Foundry](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow-in/ba-p/4191726?wt.mc_id=studentamb_279723)」で説明されているように、この演習をスキップして次に進むことができます。
> しかし、コードファーストアプローチを使用して Phi-3 / Phi-3.5 モデルを微調整しデプロイした場合、「[Fine-Tune and Integrate Custom Phi-3 Models with Prompt Flow: Step-by-Step Guide](https://techcommunity.microsoft.com/t5/educator-developer-blog/fine-tune-and-integrate-custom-phi-3-models-with-prompt-flow/ba-p/4178612?wt.mc_id=studentamb_279723)」で説明されているように、モデルを Prompt flow に接続するプロセスが若干異なります。この演習では、このプロセスを学びます。

進むためには、Fine-tuned Phi-3 / Phi-3.5 モデルを Azure AI Foundry の Prompt flow に統合する必要があります。

#### Azure AI Foundry ハブを作成する

プロジェクトを作成する前に、ハブを作成する必要があります。ハブはリソースグループのようなもので、Azure AI Foundry 内で複数のプロジェクトを整理および管理することができます。

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) にサインインします。

1. 左側のタブから **All hubs** を選択します。

1. ナビゲーションメニューから **+ New hub** を選択します。

    ![ハブを作成する](../../../../translated_images/create-hub.8d452311ef5b4b9188df89f7cff7797c67ec8f391282235b19b988e167f3e920.ja.png)

1. 次のタスクを実行します：

    - **Hub name** を入力します。これは一意の値である必要があります。
    - Azure **Subscription** を選択します。
    - 使用する **Resource group** を選択します（必要に応じて新しいものを作成します）。
    - 使用したい **Location** を選択します。
    - 使用する **Connect Azure AI Services** を選択します（必要に応じて新しいものを作成します）。
    - **Connect Azure AI Search** を選択して **スキップ接続** を選択します。
![Fill hub.](../../../../translated_images/fill-hub.8b19834866ef631a2fd031584c77b78c0438a385bdee8f981361b14bbc46f5e1.ja.png)

1. **Next** を選択します。

#### Azure AI Foundry プロジェクトの作成

1. 作成したハブで、左側のタブから **All projects** を選択します。

1. ナビゲーションメニューから **+ New project** を選択します。

    ![Select new project.](../../../../translated_images/select-new-project.1a925c25ca3bc47b2b16feefc5a76f5c29e211ac464ea5c3cdfe389868d87da7.ja.png)

1. **Project name** を入力します。これは一意の値である必要があります。

    ![Create project.](../../../../translated_images/create-project.ff239752937343b4cb38156740ebda92bc1d8b16299183c245f3e3661432db31.ja.png)

1. **Create a project** を選択します。

#### カスタム接続を追加して、微調整された Phi-3 / Phi-3.5 モデルを使用する

カスタム Phi-3 / Phi-3.5 モデルを Prompt flow と統合するには、モデルのエンドポイントとキーをカスタム接続に保存する必要があります。この設定により、Prompt flow 内でカスタム Phi-3 / Phi-3.5 モデルにアクセスできるようになります。

#### 微調整された Phi-3 / Phi-3.5 モデルの API キーとエンドポイント URI を設定する

1. [Azure ML Studio](https://ml.azure.com/home?wt.mc_id=studentamb_279723) を訪問します。

1. 作成した Azure Machine Learning ワークスペースに移動します。

1. 左側のタブから **Endpoints** を選択します。

    ![Select endpoints.](../../../../translated_images/select-endpoints.3027748aed379990fd8ee9bf27f70ff11918955bb1a10269e2f34f6931b26955.ja.png)

1. 作成したエンドポイントを選択します。

    ![Select endpoints.](../../../../translated_images/select-endpoint-created.560a5cadfbbb58b66abb2fb61b4450b22060371910af1b45c358bde548234ebc.ja.png)

1. ナビゲーションメニューから **Consume** を選択します。

1. **REST endpoint** と **Primary key** をコピーします。

    ![Copy api key and endpoint uri.](../../../../translated_images/copy-endpoint-key.56de01742992f2402d57139849304b5b049fb468fb38abc7982b7dfc311daf9e.ja.png)

#### カスタム接続を追加する

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) を訪問します。

1. 作成した Azure AI Foundry プロジェクトに移動します。

1. 作成したプロジェクトで、左側のタブから **Settings** を選択します。

1. **+ New connection** を選択します。

    ![Select new connection.](../../../../translated_images/select-new-connection.a1ff72172d07054308a3fc7b7b86e25e9ca1c879f0a382b9a2be2c80bb2ebcc5.ja.png)

1. ナビゲーションメニューから **Custom keys** を選択します。

    ![Select custom keys.](../../../../translated_images/select-custom-keys.b17eb3b15eae28126a4eeda8f53396b9a6f773745f2dd68c464252575a77b5d3.ja.png)

1. 次のタスクを実行します：

    - **+ Add key value pairs** を選択します。
    - キー名には **endpoint** を入力し、Azure ML Studio からコピーしたエンドポイントを値フィールドに貼り付けます。
    - 再度 **+ Add key value pairs** を選択します。
    - キー名には **key** を入力し、Azure ML Studio からコピーしたキーを値フィールドに貼り付けます。
    - キーを追加した後、キーが公開されないように **is secret** を選択します。

    ![Add connection.](../../../../translated_images/add-connection.c01c94851c9eece708711456a4853355b9532b0cb1f970e24f165e7e1d6c0a03.ja.png)

1. **Add connection** を選択します。

#### Prompt flow を作成する

Azure AI Foundry にカスタム接続を追加しました。次に、以下の手順に従って Prompt flow を作成します。その後、この Prompt flow をカスタム接続に接続して、微調整されたモデルを Prompt flow 内で使用します。

1. 作成した Azure AI Foundry プロジェクトに移動します。

1. 左側のタブから **Prompt flow** を選択します。

1. ナビゲーションメニューから **+ Create** を選択します。

    ![Select Promptflow.](../../../../translated_images/select-promptflow.766ad0f2403e2bd6f374bee40a607321e3e2b416629063acf3204a983fb4bcaa.ja.png)

1. ナビゲーションメニューから **Chat flow** を選択します。

    ![Select chat flow.](../../../../translated_images/select-flow-type.0e18b84032da1200e48a702e5140c1775b1eb6de9cf222c6a8007840fa278e97.ja.png)

1. 使用する **Folder name** を入力します。

    ![Select chat flow.](../../../../translated_images/enter-name.43919b211b1e8e0184536dc09184190e7e8c56bf960d4b5601443efddc757db4.ja.png)

1. **Create** を選択します。

#### カスタム Phi-3 / Phi-3.5 モデルとチャットするための Prompt flow のセットアップ

微調整された Phi-3 / Phi-3.5 モデルを Prompt flow に統合する必要があります。ただし、既存の Prompt flow はこの目的には設計されていません。そのため、カスタムモデルの統合を可能にするために Prompt flow を再設計する必要があります。

1. Prompt flow で、既存のフローを再構築するために次のタスクを実行します：

    - **Raw file mode** を選択します。
    - *flow.dag.yml* ファイル内の既存のコードをすべて削除します。
    - *flow.dag.yml* に次のコードを追加します。

        ```yml
        inputs:
          input_data:
            type: string
            default: "Who founded Microsoft?"

        outputs:
          answer:
            type: string
            reference: ${integrate_with_promptflow.output}

        nodes:
        - name: integrate_with_promptflow
          type: python
          source:
            type: code
            path: integrate_with_promptflow.py
          inputs:
            input_data: ${inputs.input_data}
        ```

    - **Save** を選択します。

    ![Select raw file mode.](../../../../translated_images/select-raw-file-mode.2084d7f905df40f69cc5ebe48efa2318e92fd069358625a92993ef614f189d84.ja.png)

1. Prompt flow でカスタム Phi-3 / Phi-3.5 モデルを使用するために、次のコードを *integrate_with_promptflow.py* に追加します。

    ```python
    import logging
    import requests
    from promptflow import tool
    from promptflow.connections import CustomConnection

    # Logging setup
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG
    )
    logger = logging.getLogger(__name__)

    def query_phi3_model(input_data: str, connection: CustomConnection) -> str:
        """
        Send a request to the Phi-3 / Phi-3.5 model endpoint with the given input data using Custom Connection.
        """

        # "connection" is the name of the Custom Connection, "endpoint", "key" are the keys in the Custom Connection
        endpoint_url = connection.endpoint
        api_key = connection.key

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
    data = {
        "input_data": [input_data],
        "params": {
            "temperature": 0.7,
            "max_new_tokens": 128,
            "do_sample": True,
            "return_full_text": True
            }
        }
        try:
            response = requests.post(endpoint_url, json=data, headers=headers)
            response.raise_for_status()
            
            # Log the full JSON response
            logger.debug(f"Full JSON response: {response.json()}")

            result = response.json()["output"]
            logger.info("Successfully received response from Azure ML Endpoint.")
            return result
        except requests.exceptions.RequestException as e:
            logger.error(f"Error querying Azure ML Endpoint: {e}")
            raise

    @tool
    def my_python_tool(input_data: str, connection: CustomConnection) -> str:
        """
        Tool function to process input data and query the Phi-3 / Phi-3.5 model.
        """
        return query_phi3_model(input_data, connection)

    ```

    ![Paste prompt flow code.](../../../../translated_images/paste-promptflow-code.667abbdf848fd03153828c0aa70dde58a851e09b1ba4c69bc6f686d2005656aa.ja.png)

> [!NOTE]
> Azure AI Foundry で Prompt flow を使用する詳細情報については、[Prompt flow in Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/how-to/prompt-flow) を参照してください。

1. **Chat input**、**Chat output** を選択して、モデルとのチャットを有効にします。

    ![Select Input Output.](../../../../translated_images/select-input-output.d4803eae144b03579db4a23def15c68bb50527017cdc4aa9f72c8679588a0f4c.ja.png)

1. これで、カスタム Phi-3 / Phi-3.5 モデルとチャットする準備が整いました。次の演習では、Prompt flow を開始し、微調整された Phi-3 / Phi-3.5 モデルとチャットする方法を学びます。

> [!NOTE]
>
> 再構築されたフローは以下の画像のようになります：
>
> ![Flow example](../../../../translated_images/graph-example.5b309021deca5b503270e50888da4784256730c210ed757f799f9bff0a12bb19.ja.png)
>

#### Prompt flow を開始する

1. **Start compute sessions** を選択して Prompt flow を開始します。

    ![Start compute session.](../../../../translated_images/start-compute-session.75300f481218ca70eae80304255956c71a9b6be31a18b43264118c19c0b1a016.ja.png)

1. **Validate and parse input** を選択してパラメータを更新します。

    ![Validate input.](../../../../translated_images/validate-input.a6c90e55ce6117ea44e2acd88b8a20bc31136bf6c574b0a6c9217867201025c9.ja.png)

1. 作成したカスタム接続の **connection** の **Value** を選択します。例えば、*connection*。

    ![Connection.](../../../../translated_images/select-connection.6573a1269969a14c83c397334051f71057ec9a243e95ea1b849483bd7481ff6a.ja.png)

#### カスタム Phi-3 / Phi-3.5 モデルとチャットする

1. **Chat** を選択します。

    ![Select chat.](../../../../translated_images/select-chat.25eab3d62b0a6c4960f0ae1b5d6efd6b5847cc20d468fd28cb1f0d656936cc22.ja.png)

1. ここに結果の例があります：これでカスタム Phi-3 / Phi-3.5 モデルとチャットできます。微調整に使用したデータに基づいて質問することをお勧めします。

    ![Chat with prompt flow.](../../../../translated_images/chat-with-promptflow.105b5a3b70ff64725c1d4cd2e9c6b55301219c7d68c9bec59106a49fb8bf40f2.ja.png)

### Phi-3 / Phi-3.5 モデルを評価するために Azure OpenAI をデプロイする

Azure AI Foundry で Phi-3 / Phi-3.5 モデルを評価するには、Azure OpenAI モデルをデプロイする必要があります。このモデルは、Phi-3 / Phi-3.5 モデルのパフォーマンスを評価するために使用されます。

#### Azure OpenAI をデプロイする

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) にサインインします。

1. 作成した Azure AI Foundry プロジェクトに移動します。

    ![Select Project.](../../../../translated_images/select-project-created.7b3c97c3883c3a95d547173b41e579cd748df940749c3d9616fe03ef46a3eda2.ja.png)

1. 作成したプロジェクトで、左側のタブから **Deployments** を選択します。

1. ナビゲーションメニューから **+ Deploy model** を選択します。

1. **Deploy base model** を選択します。

    ![Select Deployments.](../../../../translated_images/deploy-openai-model.f09a74e1f976b52f85fdef711372452b9faed270e9d015887e09f44b41bbc163.ja.png)

1. 使用したい Azure OpenAI モデルを選択します。例えば、**gpt-4o**。

    ![Select Azure OpenAI model you'd like to use.](../../../../translated_images/select-openai-model.29fbbd802d6a9aa941097ae80a0ffe256239e636190b7c1e49f28d3d66143a0d.ja.png)

1. **Confirm** を選択します。

### Azure AI Foundry の Prompt flow 評価を使用して微調整された Phi-3 / Phi-3.5 モデルを評価する

### 新しい評価を開始する

1. [Azure AI Foundry](https://ai.azure.com/?wt.mc_id=studentamb_279723) を訪問します。

1. 作成した Azure AI Foundry プロジェクトに移動します。

    ![Select Project.](../../../../translated_images/select-project-created.7b3c97c3883c3a95d547173b41e579cd748df940749c3d9616fe03ef46a3eda2.ja.png)

1. 作成したプロジェクトで、左側のタブから **Evaluation** を選択します。

1. ナビゲーションメニューから **+ New evaluation** を選択します。
![Select evaluation.](../../../../translated_images/select-evaluation.7d8a8228ebdf3f3b46bf5cf6ab5bdcb4565132ba6b28126d9757aaf3abade725.ja.png)

1. **Prompt flow**評価を選択します。

    ![Select Prompt flow evaluation.](../../../../translated_images/promptflow-evaluation.ff4265fafd69c7f5ded1b5275cacecbd5f3272a6358c1f784f62e64bcb9e949f.ja.png)

1. 以下のタスクを実行します:

    - 評価名を入力します。これは一意の値である必要があります。
    - タスクタイプとして**Question and answer without context**を選択します。このチュートリアルで使用する**UlTRACHAT_200k**データセットにはコンテキストが含まれていないためです。
    - 評価したいプロンプトフローを選択します。

    ![Prompt flow evaluation.](../../../../translated_images/evaluation-setting1.d3b22a8343f8265807e2b507fa7eec9d86a9cefd4a67bc39ba2022d572f13e1d.ja.png)

1. **Next**を選択します。

1. 以下のタスクを実行します:

    - データセットをアップロードするために**Add your dataset**を選択します。例えば、**ULTRACHAT_200k**データセットをダウンロードしたときに含まれている*test_data.json1*のようなテストデータセットファイルをアップロードできます。
    - データセットに一致する適切な**Dataset column**を選択します。例えば、**ULTRACHAT_200k**データセットを使用する場合、データセットカラムとして**${data.prompt}**を選択します。

    ![Prompt flow evaluation.](../../../../translated_images/evaluation-setting2.32749fa51bc4fdb32f75dfd09b96bee74454c51ce3084bcc6f95b7286177a657.ja.png)

1. **Next**を選択します。

1. パフォーマンスと品質メトリクスを設定するために以下のタスクを実行します:

    - 使用したいパフォーマンスと品質メトリクスを選択します。
    - 評価用に作成したAzure OpenAIモデルを選択します。例えば、**gpt-4o**を選択します。

    ![Prompt flow evaluation.](../../../../translated_images/evaluation-setting3-1.db76b89d94911c84ece6ce793593a4289278e1b24520e38ecd8372f4b9dc1167.ja.png)

1. リスクと安全性のメトリクスを設定するために以下のタスクを実行します:

    - 使用したいリスクと安全性のメトリクスを選択します。
    - 使用したい欠陥率を計算するためのしきい値を選択します。例えば、**Medium**を選択します。
    - **question**には、**Data source**として**{$data.prompt}**を選択します。
    - **answer**には、**Data source**として**{$run.outputs.answer}**を選択します。
    - **ground_truth**には、**Data source**として**{$data.message}**を選択します。

    ![Prompt flow evaluation.](../../../../translated_images/evaluation-setting3-2.eb9892654970af140ebb74fcc99e06dad7eca3d38365e3f2cbe90101392f41ee.ja.png)

1. **Next**を選択します。

1. **Submit**を選択して評価を開始します。

1. 評価の完了には時間がかかります。進行状況は**Evaluation**タブで確認できます。

### 評価結果の確認

> [!NOTE]
> 以下に示す結果は、評価プロセスを説明するためのものです。このチュートリアルでは、比較的小さなデータセットでファインチューニングされたモデルを使用しているため、最適ではない結果になる可能性があります。実際の結果は、使用するデータセットのサイズ、品質、および多様性、ならびにモデルの特定の構成に大きく依存する場合があります。

評価が完了したら、パフォーマンスと安全性のメトリクスの結果を確認できます。

1. パフォーマンスと品質メトリクス:

    - 一貫性があり、流暢で関連性のある応答を生成するモデルの有効性を評価します。

    ![Evaluation result.](../../../../translated_images/evaluation-result-gpu.5b6e301e6d1af6044819f4d3c8443cbc44fb7db54ebce208b4288744ca25e6e8.ja.png)

1. リスクと安全性のメトリクス:

    - モデルの出力が安全で、責任あるAIの原則に従い、有害または攻撃的な内容を避けることを確認します。

    ![Evaluation result.](../../../../translated_images/evaluation-result-gpu-2.d867d40ee9dfebc40c878288b8dc8727721a2fec995904b1475c513f0960e8e0.ja.png)

1. **Detailed metrics result**を表示するためにスクロールダウンできます。

    ![Evaluation result.](../../../../translated_images/detailed-metrics-result.6cf00c2b6026bb500ff758ee3047c20f600aab3878c892897e99e2e3a88fb002.ja.png)

1. カスタムPhi-3 / Phi-3.5モデルをパフォーマンスと安全性の両方のメトリクスに対して評価することで、モデルが効果的であるだけでなく、責任あるAIの実践にも準拠していることを確認でき、実世界での展開準備が整います。

## おめでとうございます！

### このチュートリアルを完了しました

Prompt flowと統合されたAzure AI FoundryでファインチューニングされたPhi-3モデルを正常に評価しました。これは、AIモデルが高性能であるだけでなく、Microsoftの責任あるAIの原則に準拠して信頼できるAIアプリケーションを構築するための重要なステップです。

![Architecture.](../../../../translated_images/architecture.1eb9d143d0771c6065f16c0f66a9eb233f466cdf9db0b0afe11adcbd57eb06ce.ja.png)

## Azureリソースのクリーンアップ

追加の料金を回避するために、Azureリソースをクリーンアップします。Azureポータルに移動し、以下のリソースを削除します:

- Azure Machine Learningリソース。
- Azure Machine Learningモデルエンドポイント。
- Azure AI Foundryプロジェクトリソース。
- Azure AI Foundry Prompt flowリソース。

### 次のステップ

#### ドキュメント

- [microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)
- [Assess AI systems by using the Responsible AI dashboard](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai-dashboard?view=azureml-api-2&source=recommendations?wt.mc_id=studentamb_279723)
- [Evaluation and monitoring metrics for generative AI](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-metrics-built-in?tabs=definition?wt.mc_id=studentamb_279723)
- [Azure AI Foundry documentation](https://learn.microsoft.com/azure/ai-studio/?wt.mc_id=studentamb_279723)
- [Prompt flow documentation](https://microsoft.github.io/promptflow/?wt.mc_id=studentamb_279723)

#### トレーニングコンテンツ

- [Introduction to Microsoft's Responsible AI Approach](https://learn.microsoft.com/training/modules/introduction-to-microsofts-responsible-ai-approach/?source=recommendations?wt.mc_id=studentamb_279723)
- [Introduction to Azure AI Foundry](https://learn.microsoft.com/training/modules/introduction-to-azure-ai-studio/?wt.mc_id=studentamb_279723)

### 参考

- [microsoft/Phi-3CookBook](https://github.com/microsoft/Phi-3CookBook?wt.mc_id=studentamb_279723)
- [What is Responsible AI?](https://learn.microsoft.com/azure/machine-learning/concept-responsible-ai?view=azureml-api-2?wt.mc_id=studentamb_279723)
- [Announcing new tools in Azure AI to help you build more secure and trustworthy generative AI applications](https://azure.microsoft.com/blog/announcing-new-tools-in-azure-ai-to-help-you-build-more-secure-and-trustworthy-generative-ai-applications/?wt.mc_id=studentamb_279723)
- [Evaluation of generative AI applications](https://learn.microsoft.com/azure/ai-studio/concepts/evaluation-approach-gen-ai?wt.mc_id%3Dstudentamb_279723)

**免責事項**:
この文書は、機械翻訳AIサービスを使用して翻訳されています。正確性を期すために努力していますが、自動翻訳には誤りや不正確さが含まれる場合があります。元の言語で書かれた原文を信頼できる情報源と見なすべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用により生じた誤解や誤訳については責任を負いかねます。