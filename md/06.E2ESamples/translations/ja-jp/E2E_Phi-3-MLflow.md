# MLflow

[MLflow](https://mlflow.org/) は、エンドツーエンドの機械学習ライフサイクルを管理するために設計されたオープンソースプラットフォームです。

![MLFlow](../../../../imgs/03/MLflow/MlFlowmlops.png)

MLFlowは、実験、再現性、デプロイメント、および中央モデルレジストリを含むMLライフサイクルを管理するために使用されます。MLFlowは現在、4つのコンポーネントを提供しています。

- **MLflow Tracking:** 実験、コード、データ構成、および結果を記録およびクエリします。
- **MLflow Projects:** データサイエンスコードを任意のプラットフォームで実行を再現する形式でパッケージ化します。
- **Mlflow Models:** 様々なサービング環境で機械学習モデルをデプロイします。
- **Model Registry:** 中央リポジトリにモデルを保存、注釈、および管理します。

実験の追跡、再現可能な実行へのコードのパッケージ化、およびモデルの共有とデプロイの機能を含みます。MLFlowはDatabricksに統合されており、様々なMLライブラリをサポートしているため、ライブラリに依存しません。便利なREST APIとCLIを提供しているため、任意の機械学習ライブラリおよび任意のプログラミング言語で使用できます。

![MLFlow](../../../../imgs/03/MLflow/MLflow2.png)

MLFlowの主な機能は次のとおりです。

- **実験追跡:** パラメータと結果を記録および比較します。
- **モデル管理:** モデルを様々なサービングおよび推論プラットフォームにデプロイします。
- **モデルレジストリ:** バージョン管理と注釈を含むMLflowモデルのライフサイクルを協力して管理します。
- **プロジェクト:** 共有または本番使用のためにMLコードをパッケージ化します。

MLFlowは、データの準備、モデルの登録と管理、実行のためのモデルのパッケージ化、サービスのデプロイ、およびモデルの監視を含むMLOpsループもサポートしています。特にクラウドおよびエッジ環境で、プロトタイプから本番ワークフローへの移行プロセスを簡素化することを目的としています。

## エンドツーエンドシナリオ - ラッパーを構築し、Phi-3をMLFlowモデルとして使用する

このエンドツーエンドサンプルでは、Phi-3小型言語モデル（SLM）をラップする2つの異なるアプローチを示し、MLFlowモデルとしてローカルまたはクラウド（例：Azure Machine Learningワークスペース）で実行します。

![MLFlow](../../../../imgs/03/MLflow/MlFlow1.png)

| プロジェクト | 説明 | 場所 |
| ------------ | ----------- | -------- |
| Transformer Pipeline | HuggingFaceモデルをMLFlowの実験的なtransformersフレーバーで使用したい場合、Transformer Pipelineはラッパーを構築する最も簡単なオプションです。 | [**TransformerPipeline.ipynb**](E2E_Phi-3-MLflow_TransformerPipeline.ipynb) |
| カスタムPythonラッパー | 記述時点では、transformer pipelineはHuggingFaceモデルのONNX形式のMLFlowラッパー生成をサポートしていません。実験的なoptimum Pythonパッケージを使用しても同様です。このような場合、MLFlowモードのカスタムPythonラッパーを構築できます。 | [**CustomPythonWrapper.ipynb**](E2E_Phi-3-MLflow_CustomPythonWrapper.ipynb) |

## プロジェクト: Transformer Pipeline

1. MLFlowおよびHuggingFaceの関連Pythonパッケージが必要です。

    ``` Python
    import mlflow
    import transformers
    ```

2. 次に、HuggingFaceレジストリのターゲットPhi-3モデルを参照してtransformer pipelineを開始する必要があります。_Phi-3-mini-4k-instruct_のモデルカードからわかるように、そのタスクは「テキスト生成」タイプです。

    ``` Python
    pipeline = transformers.pipeline(
        task = "text-generation",
        model = "microsoft/Phi-3-mini-4k-instruct"
    )
    ```

3. Phi-3モデルのtransformer pipelineをMLFlow形式で保存し、ターゲットアーティファクトパス、特定のモデル構成設定、および推論APIタイプなどの追加情報を提供できます。

    ``` Python
    model_info = mlflow.transformers.log_model(
        transformers_model = pipeline,
        artifact_path = "phi3-mlflow-model",
        model_config = model_config,
        task = "llm/v1/chat"
    )
    ```

## プロジェクト: カスタムPythonラッパー

1. ここでは、ONNXモデルの推論およびトークンのエンコード/デコードのためにMicrosoftの[ONNX Runtime generate() API](https://github.com/microsoft/onnxruntime-genai)を利用できます。以下の例では、ターゲットコンピューティングに対してonnxruntime_genaiパッケージを選択します。以下の例はCPUを対象としています。

    ``` Python
    import mlflow
    from mlflow.models import infer_signature
    import onnxruntime_genai as og
    ```

2. カスタムクラスは2つのメソッドを実装します。_load_context()_はPhi-3 Mini 4K Instructの**ONNXモデル**、**生成パラメータ**、および**トークナイザー**を初期化し、_predict()_は提供されたプロンプトに対して出力トークンを生成します。

    ``` Python
    class Phi3Model(mlflow.pyfunc.PythonModel):
        def load_context(self, context):
            # アーティファクトからモデルを取得
            model_path = context.artifacts["phi3-mini-onnx"]
            model_options = {
                 "max_length": 300,
                 "temperature": 0.2,
            }

            # モデルを定義
            self.phi3_model = og.Model(model_path)
            self.params = og.GeneratorParams(self.phi3_model)
            self.params.set_search_options(**model_options)

            # トークナイザーを定義
            self.tokenizer = og.Tokenizer(self.phi3_model)

        def predict(self, context, model_input):
            # 入力からプロンプトを取得
            prompt = model_input["prompt"][0]
            self.params.input_ids = self.tokenizer.encode(prompt)

            # モデルの応答を生成
            response = self.phi3_model.generate(self.params)

            return self.tokenizer.decode(response[0][len(self.params.input_ids):])
    ```

3. _mlflow.pyfunc.log_model()_関数を使用して、Phi-3モデルのカスタムPythonラッパー（ピクル形式）を生成し、元のONNXモデルと必要な依存関係を設定できます。

    ``` Python
    model_info = mlflow.pyfunc.log_model(
        artifact_path = artifact_path,
        python_model = Phi3Model(),
        artifacts = {
            "phi3-mini-onnx": "cpu_and_mobile/cpu-int4-rtn-block-32-acc-level-4",
        },
        input_example = input_example,
        signature = infer_signature(input_example, ["Run"]),
        extra_pip_requirements = ["torch", "onnxruntime_genai", "numpy"],
    )
    ```

## 生成されたMLFlowモデルの署名

1. 上記のTransformer Pipelineプロジェクトのステップ3で、MLFlowモデルのタスクを「_llm/v1/chat_」に設定しました。この指示により、OpenAIのChat APIと互換性のあるモデルのAPIラッパーが生成されます。以下のように表示されます。

    ``` Python
    {inputs:
      ['messages': Array({content: string (required), name: string (optional), role: string (required)}) (required), 'temperature': double (optional), 'max_tokens': long (optional), 'stop': Array(string) (optional), 'n': long (optional), 'stream': boolean (optional)],
    outputs:
      ['id': string (required), 'object': string (required), 'created': long (required), 'model': string (required), 'choices': Array({finish_reason: string (required), index: long (required), message: {content: string (required), name: string (optional), role: string (required)} (required)}) (required), 'usage': {completion_tokens: long (required), prompt_tokens: long (required), total_tokens: long (required)} (required)],
    params:
      None}
    ```

2. したがって、次の形式でプロンプトを送信できます。

    ``` Python
    messages = [{"role": "user", "content": "スペインの首都はどこですか？"}]
    ```

3. 次に、OpenAI API互換の後処理を使用して、_response[0][‘choices’][0][‘message’][‘content’]_などの出力を美化し、次のように表示します。

    ``` JSON
    質問: スペインの首都はどこですか？

    回答: スペインの首都はマドリードです。スペイン最大の都市であり、国の政治、経済、文化の中心地です。マドリードはイベリア半島の中心に位置し、豊かな歴史、芸術、建築で知られています。王宮、プラド美術館、マヨール広場などがあります。

    使用状況: {'prompt_tokens': 11, 'completion_tokens': 73, 'total_tokens': 84}
    ```

4. 上記のカスタムPythonラッパープロジェクトのステップ3で、MLFlowパッケージに入力例からモデルの署名を生成させました。MLFlowラッパーの署名は次のようになります。

    ``` Python
    {inputs:
      ['prompt': string (required)],
    outputs:
      [string (required)],
    params:
      None}
    ```

5. したがって、プロンプトには「prompt」辞書キーが含まれている必要があります。次のようになります。

    ``` Python
    {"prompt": "<|system|>あなたはスタンドアップコメディアンです。<|end|><|user|>原子についてのジョークを教えてください<|end|><|assistant|>",}
    ```

6. モデルの出力は文字列形式で提供されます。

    ``` JSON
    さて、原子に関連する小さなジョークを教えます！

    なぜ電子はプロトンと一緒にかくれんぼをしないのですか？

    それは、彼らが常に「共有」しているときに見つけるのが難しいからです！

    これはすべて楽しいものであり、私たちはただ少しの原子レベルのユーモアを楽しんでいるだけです！
    ```
