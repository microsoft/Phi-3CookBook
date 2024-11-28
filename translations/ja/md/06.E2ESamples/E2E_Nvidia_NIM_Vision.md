### 例のシナリオ

画像 (`demo.png`) があり、その画像を処理して新しいバージョンを保存する Python コードを生成したいとします。

上記のコードは以下のプロセスを自動化します：

1. 環境と必要な設定を整える。
2. モデルに必要な Python コードを生成するよう指示するプロンプトを作成する。
3. プロンプトをモデルに送り、生成されたコードを収集する。
4. 生成されたコードを抽出して実行する。
5. 元の画像と処理された画像を表示する。

このアプローチは、画像処理タスクを自動化するために AI の力を活用し、目標達成をより簡単かつ迅速にします。

[サンプルコードソリューション](../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

では、コード全体が何をしているのかをステップバイステップで見ていきましょう：

1. **必要なパッケージのインストール**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    このコマンドは `langchain_nvidia_ai_endpoints` パッケージをインストールし、最新バージョンを確保します。

2. **必要なモジュールのインポート**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    これらのインポートは、NVIDIA AI エンドポイントとの対話、パスワードの安全な取り扱い、オペレーティングシステムとの対話、および base64 形式でのデータのエンコード/デコードに必要なモジュールを取り込みます。

3. **API キーの設定**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    このコードは `NVIDIA_API_KEY` 環境変数が設定されているかどうかを確認します。設定されていない場合、ユーザーに API キーを安全に入力するよう促します。

4. **モデルと画像パスの定義**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    使用するモデルを設定し、指定されたモデルで `ChatNVIDIA` のインスタンスを作成し、画像ファイルのパスを定義します。

5. **テキストプロンプトの作成**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    これは、画像を処理するための Python コードを生成するようモデルに指示するテキストプロンプトを定義します。

6. **画像を Base64 でエンコード**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    このコードは画像ファイルを読み込み、base64 でエンコードし、エンコードされたデータを持つ HTML 画像タグを作成します。

7. **テキストと画像をプロンプトに結合**:
    ```python
    prompt = f"{text} {image}"
    ```
    これはテキストプロンプトと HTML 画像タグを単一の文字列に結合します。

8. **ChatNVIDIA を使用してコードを生成**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    このコードはプロンプトを `ChatNVIDIA` に送り、生成されたコンテンツを `code` 文字列に格納します。

9. **生成されたコンテンツから Python コードを抽出**:
    ```python
    begin = code.index('```
    これはマークダウン形式を削除して、生成されたコンテンツから実際の Python コードを抽出します。

10. **生成されたコードを実行**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    これは抽出された Python コードをサブプロセスとして実行し、その出力をキャプチャします。

11. **画像を表示**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    これらの行は `IPython.display` モジュールを使用して画像を表示します。

**免責事項**:
この文書は機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期すために努めておりますが、自動翻訳にはエラーや不正確さが含まれる可能性があることをご承知おきください。原文の言語で書かれた元の文書を権威ある情報源と見なすべきです。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用による誤解や誤った解釈について、当方は責任を負いかねます。