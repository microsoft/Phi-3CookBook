# **ローカルサーバーでのPhi-3推論**

Phi-3をローカルサーバーにデプロイすることができます。ユーザーは[Ollama](https://ollama.com)や[LM Studio](https://llamaedge.com)のソリューションを選ぶことも、自分でコードを書くこともできます。[Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo)や[Langchain](https://www.langchain.com/)を通じてPhi-3のローカルサービスに接続し、Copilotアプリケーションを構築することができます。

## **Semantic Kernelを使ってPhi-3-miniにアクセスする**

Copilotアプリケーションでは、Semantic Kernel / LangChainを通じてアプリケーションを作成します。この種のアプリケーションフレームワークは、一般的にAzure OpenAI Service / OpenAIモデルと互換性があり、Hugging Faceのオープンソースモデルやローカルモデルもサポートします。では、Semantic Kernelを使ってPhi-3-miniにアクセスするにはどうすればよいでしょうか？.NETを例にとると、Semantic KernelのHugging Face Connectorと組み合わせることができます。デフォルトでは、Hugging FaceのモデルIDに対応しています（初めて使用する際には、Hugging Faceからモデルがダウンロードされるため、時間がかかります）。自分で構築したローカルサービスに接続することもできます。二つを比較すると、特に企業アプリケーションにおいては、後者の方が自律性が高いため、後者を使用することをお勧めします。

![sk](../../../../translated_images/sk.fc8f38bb6ac491315099aa29a2704de109fc0b052448c9bc3d7c02586c196ca4.ja.png)

この図から、Semantic Kernelを通じてローカルサービスにアクセスし、自分で構築したPhi-3-miniモデルサーバーに簡単に接続できることがわかります。以下は実行結果です。

![skrun](../../../../translated_images/skrun.f579fcb28592ba4644af8b578e66fb01923bf032b670cef44874c6550e85876d.ja.png)

***サンプルコード*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel

免責事項：この翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない可能性があります。
出力を確認し、必要な修正を行ってください。