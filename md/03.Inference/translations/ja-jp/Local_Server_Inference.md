# **ローカルサーバーでPhi-3を推論する**

Phi-3をローカルサーバーにデプロイすることができます。ユーザーは、[Ollama](https://ollama.com)や[LM Studio](https://llamaedge.com)のソリューションを選択するか、自分でコードを書くことができます。Phi-3のローカルサービスに接続するために、[Semantic Kernel](https://github.com/microsoft/semantic-kernel?WT.mc_id=aiml-138114-kinfeylo)や[Langchain](https://www.langchain.com/)を使用してCopilotアプリケーションを構築することができます。

## **Semantic Kernelを使用してPhi-3-miniにアクセスする**

Copilotアプリケーションでは、Semantic Kernel / LangChainを使用してアプリケーションを作成します。このタイプのアプリケーションフレームワークは通常、Azure OpenAI Service / OpenAIモデルと互換性があり、Hugging Face上のオープンソースモデルやローカルモデルもサポートできます。Semantic Kernelを使用してPhi-3-miniにアクセスする場合はどうすればよいでしょうか？.NETを例にとると、Semantic KernelのHugging Face Connectorと組み合わせて使用することができます。デフォルトでは、Hugging Face上のモデルIDに対応しています（初めて使用する場合、モデルはHugging Faceからダウンロードされるため、時間がかかります）。また、構築したローカルサービスに接続することもできます。これらの2つを比較すると、特に企業アプリケーションでは、後者を使用することをお勧めします。

![sk](../../imgs/03/LocalServer/sk.png)

図からわかるように、Semantic Kernelを使用してローカルサービスにアクセスすることで、構築したPhi-3-miniモデルサーバーに簡単に接続できます。以下は実行結果です。

![skrun](../../imgs/03/LocalServer/skrun.png)

***サンプルコード*** https://github.com/kinfey/Phi3MiniSamples/tree/main/semantickernel
