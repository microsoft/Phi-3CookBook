### 例のシナリオ

画像 (`demo.png`) を持っていて、その画像を処理し、新しいバージョンの画像 (`phi-3-vision.jpg`) を保存するPythonコードを生成したいとします。

上記のコードは次の手順でこのプロセスを自動化します:

1. 環境と必要な設定を整える。
2. モデルに必要なPythonコードを生成するよう指示するプロンプトを作成する。
3. プロンプトをモデルに送信し、生成されたコードを収集する。
4. 生成されたコードを抽出して実行する。
5. 元の画像と処理後の画像を表示する。

このアプローチでは、AIの力を活用して画像処理タスクを自動化し、目標をより簡単かつ迅速に達成できます。

[サンプルコードソリューション](../../../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

コード全体が何をしているのか、ステップごとに見ていきましょう:

1. **必要なパッケージのインストール**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    このコマンドは、`langchain_nvidia_ai_endpoints` パッケージをインストールし、最新バージョンであることを確認します。

2. **必要なモジュールのインポート**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    これらのインポートは、NVIDIA AIエンドポイントとのやり取り、パスワードの安全な管理、OSとのやり取り、base64形式でのデータのエンコード/デコードを行うために必要なモジュールを取り込みます。

3. **APIキーの設定**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    このコードは、環境変数 `NVIDIA_API_KEY` が設定されているか確認します。設定されていない場合は、ユーザーに安全にAPIキーを入力するよう促します。

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
    画像処理用のPythonコードを生成するようモデルに指示するテキストプロンプトを定義します。

6. **画像をBase64でエンコード**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'<img src="data:image/png;base64,{image_b64}" />'
    ```
    このコードは画像ファイルを読み取り、Base64形式でエンコードし、エンコードされたデータを含むHTML画像タグを作成します。

7. **テキストと画像をプロンプトに結合**:
    ```python
    prompt = f"{text} {image}"
    ```
    テキストプロンプトとHTML画像タグを1つの文字列に結合します。

8. **ChatNVIDIAを使用してコードを生成**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    このコードはプロンプトを `ChatNVIDIA` に送信し、生成されたコンテンツから `` model and collects the generated code in chunks, printing and appending each chunk to the `code` 文字列を収集します。

9. **生成されたコンテンツからPythonコードを抽出**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    これは、Markdownフォーマットを削除して生成されたコンテンツから実際のPythonコードを抽出します。

10. **生成されたコードを実行**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    このコードは抽出されたPythonコードをサブプロセスとして実行し、その出力をキャプチャします。

11. **画像を表示**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    これらの行は、`IPython.display` モジュールを使用して画像を表示します。

**免責事項**:  
この文書は、機械翻訳AIサービスを使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確な部分が含まれる場合があります。元の言語で記載された原文が正式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳を推奨します。本翻訳の使用に起因する誤解や解釈の誤りについて、当社は一切の責任を負いません。