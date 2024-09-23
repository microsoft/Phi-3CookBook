### 例のシナリオ

`demo.png`という画像があり、それを処理して新しいバージョンの画像 (`phi-3-vision.jpg`) を保存するPythonコードを生成したいとします。

上記のコードは以下のプロセスを自動化します：

1. 環境と必要な設定を整える。
2. モデルに必要なPythonコードを生成するよう指示するプロンプトを作成する。
3. プロンプトをモデルに送り、生成されたコードを収集する。
4. 生成されたコードを抽出して実行する。
5. 元の画像と処理された画像を表示する。

このアプローチはAIの力を活用して画像処理タスクを自動化し、目標達成をより簡単かつ迅速にします。

[サンプルコードソリューション](../../../../code/06.E2E/E2E_Nvidia_NIM_Phi3_Vision.ipynb)

コード全体が何をしているかをステップバイステップで見ていきましょう：

1. **必要なパッケージをインストール**:
    ```python
    !pip install langchain_nvidia_ai_endpoints -U
    ```
    このコマンドは `langchain_nvidia_ai_endpoints` パッケージを最新バージョンにインストールします。

2. **必要なモジュールをインポート**:
    ```python
    from langchain_nvidia_ai_endpoints import ChatNVIDIA
    import getpass
    import os
    import base64
    ```
    これらのインポートは、NVIDIA AIエンドポイントと対話するためのモジュール、パスワードを安全に取り扱うためのモジュール、OSと対話するためのモジュール、データをbase64形式でエンコード/デコードするためのモジュールを取り込みます。

3. **APIキーを設定**:
    ```python
    if not os.getenv("NVIDIA_API_KEY"):
        os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter your NVIDIA API key: ")
    ```
    このコードは `NVIDIA_API_KEY` 環境変数が設定されているか確認し、設定されていない場合はユーザーにAPIキーを安全に入力させます。

4. **モデルと画像パスを定義**:
    ```python
    model = 'microsoft/phi-3-vision-128k-instruct'
    chat = ChatNVIDIA(model=model)
    img_path = './imgs/demo.png'
    ```
    これにより使用するモデルが設定され、指定されたモデルで `ChatNVIDIA` のインスタンスが作成され、画像ファイルのパスが定義されます。

5. **テキストプロンプトを作成**:
    ```python
    text = "Please create Python code for image, and use plt to save the new picture under imgs/ and name it phi-3-vision.jpg."
    ```
    これはモデルに画像処理用のPythonコードを生成するよう指示するテキストプロンプトを定義します。

6. **画像をBase64でエンコード**:
    ```python
    with open(img_path, "rb") as f:
        image_b64 = base64.b64encode(f.read()).decode()
    image = f'
    ```
    このコードは画像ファイルを読み込み、base64でエンコードし、エンコードされたデータを持つHTML画像タグを作成します。

7. **テキストと画像をプロンプトに結合**:
    ```python
    prompt = f"{text} {image}"
    ```
    これによりテキストプロンプトとHTML画像タグが1つの文字列に結合されます。

8. **ChatNVIDIAを使用してコードを生成**:
    ```python
    code = ""
    for chunk in chat.stream(prompt):
        print(chunk.content, end="")
        code += chunk.content
    ```
    このコードはプロンプトを `ChatNVIDIA` モデルに送り、生成されたコードをチャンクごとに収集し、各チャンクを印刷して `code` 文字列に追加します。

9. **生成されたコンテンツからPythonコードを抽出**:
    ```python
    begin = code.index('```python') + 9
    code = code[begin:]
    end = code.index('```')
    code = code[:end]
    ```
    これにより、マークダウンのフォーマットを取り除き、生成されたコンテンツから実際のPythonコードを抽出します。

10. **生成されたコードを実行**:
    ```python
    import subprocess
    result = subprocess.run(["python", "-c", code], capture_output=True)
    ```
    これにより、抽出されたPythonコードがサブプロセスとして実行され、その出力がキャプチャされます。

11. **画像を表示**:
    ```python
    from IPython.display import Image, display
    display(Image(filename='./imgs/phi-3-vision.jpg'))
    display(Image(filename='./imgs/demo.png'))
    ```
    これらの行は `IPython.display` モジュールを使用して画像を表示します。

免責事項: この翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない可能性があります。 出力を確認し、必要な修正を行ってください。