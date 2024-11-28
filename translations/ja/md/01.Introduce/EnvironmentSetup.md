# Phi-3をローカル環境で始める

このガイドでは、Ollamaを使用してPhi-3モデルを実行するためのローカル環境を設定する方法を説明します。GitHub Codespaces、VS Code Dev Containers、またはローカル環境を使用してモデルを実行することができます。

## 環境設定

### GitHub Codespaces

GitHub Codespacesを使用して、このテンプレートを仮想的に実行することができます。ボタンをクリックすると、ブラウザでWebベースのVS Codeインスタンスが開きます。

1. テンプレートを開く（数分かかる場合があります）：

    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)

2. ターミナルウィンドウを開く

### VS Code Dev Containers

⚠️ このオプションは、Docker Desktopに少なくとも16 GBのRAMが割り当てられている場合にのみ機能します。16 GB未満のRAMをお使いの場合は、[GitHub Codespacesオプション](../../../../md/01.Introduce)を試すか、[ローカル環境で設定](../../../../md/01.Introduce)してください。

関連するオプションとして、VS Code Dev Containersがあります。これは、[Dev Containers拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)を使用して、ローカルのVS Codeでプロジェクトを開きます。

1. Docker Desktopを起動（インストールされていない場合はインストール）
2. プロジェクトを開く：

    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

3. 開いたVS Codeウィンドウで、プロジェクトファイルが表示されたら（数分かかる場合があります）、ターミナルウィンドウを開く。
4. [デプロイ手順](../../../../md/01.Introduce)に進む

### ローカル環境

1. 以下のツールがインストールされていることを確認してください：

    * [Ollama](https://ollama.com/)
    * [Python 3.10+](https://www.python.org/downloads/)
    * [OpenAI Python SDK](https://pypi.org/project/openai/)

## モデルのテスト

1. Ollamaにphi3:miniモデルをダウンロードして実行するよう依頼します：

    ```shell
    ollama run phi3:mini
    ```

    モデルのダウンロードには数分かかります。

2. 出力に「success」と表示されたら、プロンプトからそのモデルにメッセージを送信できます。

    ```shell
    >>> Write a haiku about hungry hippos
    ```

3. 数秒後、モデルからの応答がストリーム表示されるはずです。

4. 言語モデルで使用されるさまざまな技術について学ぶために、Pythonノートブック[ollama.ipynb](../../../../code/01.Introduce/ollama.ipynb)を開き、各セルを実行します。'phi3:mini'以外のモデルを使用した場合は、ファイルの上部にある`MODEL_NAME` in the first cell.

5. To have a conversation with the phi3:mini model from Python, open the Python file [chat.py](../../../../code/01.Introduce/chat.py) and run it. You can change the `MODEL_NAME`を必要に応じて変更し、システムメッセージを変更したり、few-shot例を追加したりすることもできます。

**免責事項**:
この文書は機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期していますが、自動翻訳には誤りや不正確さが含まれる場合がありますのでご注意ください。元の言語での文書が権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用による誤解や誤認に対して、当社は一切の責任を負いません。