# Windows GPU を使用して Phi-3.5-Instruct ONNX の Prompt flow ソリューションを作成する

このドキュメントは、PromptFlow と ONNX (Open Neural Network Exchange) を使用して Phi-3 モデルを基にした AI アプリケーションを開発する方法の例です。

PromptFlow は、LLM (Large Language Model) ベースの AI アプリケーションのアイデア出しからプロトタイピング、テスト、評価まで、エンドツーエンドの開発サイクルを効率化するための開発ツール群です。

PromptFlow を ONNX と統合することで、開発者は以下を実現できます:

- **モデルパフォーマンスの最適化**: ONNX を活用して効率的なモデル推論とデプロイを実現。
- **開発の簡素化**: PromptFlow を使用してワークフローを管理し、繰り返し作業を自動化。
- **コラボレーションの強化**: チームメンバー間のコラボレーションを促進し、統一された開発環境を提供。

**Prompt flow** は、LLM ベースの AI アプリケーションのアイデア出し、プロトタイピング、テスト、評価から、本番環境へのデプロイやモニタリングまで、エンドツーエンドの開発サイクルを効率化する開発ツール群です。これにより、プロンプトエンジニアリングが大幅に簡素化され、プロダクション品質の LLM アプリケーションを構築できるようになります。

Prompt flow は OpenAI、Azure OpenAI Service、カスタマイズ可能なモデル (Huggingface、ローカル LLM/SLM) に接続できます。Phi-3.5 の量子化された ONNX モデルをローカルアプリケーションにデプロイすることを目指しています。Prompt flow を活用することで、ビジネスの計画をより良く立て、Phi-3.5 に基づいたローカルソリューションを完成させることができます。この例では、ONNX Runtime GenAI ライブラリを組み合わせて、Windows GPU を基にした Prompt flow ソリューションを完成させます。

## **インストール**

### **Windows GPU 用 ONNX Runtime GenAI**

Windows GPU 用 ONNX Runtime GenAI を設定するためのガイドラインはこちらをご覧ください [click here](./ORTWindowGPUGuideline.md)

### **VSCode で Prompt flow をセットアップ**

1. Prompt flow VS Code 拡張機能をインストールします

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.ja.png)

2. Prompt flow VS Code 拡張機能をインストールした後、拡張機能をクリックし、**Installation dependencies** を選択して、このガイドラインに従って環境に Prompt flow SDK をインストールします

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.ja.png)

3. [サンプルコード](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf) をダウンロードし、VS Code でこのサンプルを開きます

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.ja.png)

4. **flow.dag.yaml** を開いて Python 環境を選択します

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.ja.png)

   **chat_phi3_ort.py** を開いて Phi-3.5-instruct ONNX モデルの場所を変更します

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.ja.png)

5. Prompt flow を実行してテストします

**flow.dag.yaml** を開き、ビジュアルエディタをクリックします

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.ja.png)

クリック後、これを実行してテストします

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.ja.png)

1. ターミナルでバッチを実行して、さらに多くの結果を確認できます

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

デフォルトのブラウザで結果を確認できます

![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.ja.png)

**免責事項**:  
本書類は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を期すよう努めておりますが、自動翻訳には誤りや不正確さが含まれる場合があります。原文（元の言語の文書）を正式な情報源としてご参照ください。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いません。