# Phi-3 をローカルで始めよう

このガイドでは、Ollama を使用して Phi-3 モデルをローカル環境で実行するためのセットアップ方法を紹介します。GitHub Codespaces、VS Code Dev Containers、またはローカル環境でモデルを実行する方法があります。

## 環境セットアップ

### GitHub Codespaces

GitHub Codespaces を使用して、このテンプレートを仮想的に実行できます。以下のボタンをクリックすると、ブラウザで VS Code のウェブ版が開きます：

1. テンプレートを開く（数分かかることがあります）：

    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)

2. ターミナルウィンドウを開く

### VS Code Dev Containers

⚠️ Docker Desktop に少なくとも 16 GB の RAM が割り当てられている場合にのみ、このオプションは機能します。16 GB 未満の RAM しかない場合は、[GitHub Codespaces のオプション](../../../../md/01.Introduce)を試すか、[ローカル環境でセットアップ](../../../../md/01.Introduce)してください。

もう一つのオプションは VS Code Dev Containers で、[Dev Containers 拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)を使用してローカルの VS Code でプロジェクトを開きます：

1. Docker Desktop を起動する（未インストールの場合はインストール）
2. プロジェクトを開く：

    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

3. 開いた VS Code ウィンドウでプロジェクトファイルが表示されたら（数分かかることがあります）、ターミナルウィンドウを開く。
4. [デプロイ手順](../../../../md/01.Introduce)に進む

### ローカル環境

1. 以下のツールがインストールされていることを確認してください：

    * [Ollama](https://ollama.com/)
    * [Python 3.10+](https://www.python.org/downloads/)
    * [OpenAI Python SDK](https://pypi.org/project/openai/)

## モデルのテスト

1. Ollama に phi3:mini モデルをダウンロードして実行するように依頼します：

    ```shell
    ollama run phi3:mini
    ```

    モデルのダウンロードには数分かかります。

2. 出力に「success」と表示されたら、プロンプトからそのモデルにメッセージを送信できます。

    ```shell
    >>> Write a haiku about hungry hippos
    ```

3. 数秒後、モデルからのレスポンスストリームが表示されるはずです。

4. 言語モデルで使用されるさまざまな技術について学ぶには、Python ノートブック [ollama.ipynb](../../../../code/01.Introduce/ollama.ipynb) を開き、各セルを実行します。'phi3:mini' 以外のモデルを使用した場合は、ファイルの上部にある `MODEL_NAME` in the first cell.

5. To have a conversation with the phi3:mini model from Python, open the Python file [chat.py](../../../../code/01.Introduce/chat.py) and run it. You can change the `MODEL_NAME` を必要に応じて変更し、システムメッセージや数ショットの例も追加できます。

**免責事項**:
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を期していますが、自動翻訳には誤りや不正確さが含まれる可能性があることにご注意ください。元の言語で書かれた文書が権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤認について、当社は一切の責任を負いません。