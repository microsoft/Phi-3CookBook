# Phi-3をローカルで開始する

このガイドでは、Ollamaを使用してPhi-3モデルを実行するためのローカル環境をセットアップする方法を説明します。GitHub Codespaces、VS Code Dev Containers、またはローカル環境を使用してモデルを実行することができます。

## 環境設定

### GitHub Codespaces

GitHub Codespacesを使用して、このテンプレートを仮想的に実行することができます。このボタンをクリックすると、ブラウザでWebベースのVS Codeインスタンスが開きます：

1. テンプレートを開く（これには数分かかる場合があります）：

    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/microsoft/phi-3cookbook)

2. ターミナルウィンドウを開く

### VS Code Dev Containers

⚠️ このオプションは、Docker Desktopに少なくとも16 GBのRAMが割り当てられている場合にのみ機能します。16 GB未満のRAMを持っている場合は、[GitHub Codespacesオプション](#github-codespaces)を試すか、[ローカル環境を設定](#local-environment)してください。

関連するオプションとして、VS Code Dev Containersがあります。これは、[Dev Containers拡張機能](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)を使用して、ローカルのVS Codeでプロジェクトを開きます：

1. Docker Desktopを起動する（インストールされていない場合はインストールする）
2. プロジェクトを開く：

    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/microsoft/phi-3cookbook)

3. プロジェクトファイルが表示されたら（これには数分かかる場合があります）、ターミナルウィンドウを開く。
4. [デプロイ手順](#deployment)に進む

### ローカル環境

1. 以下のツールがインストールされていることを確認する：

    * [Ollama](https://ollama.com/)
    * [Python 3.10+](https://www.python.org/downloads/)
    * [OpenAI Python SDK](https://pypi.org/project/openai/)

## モデルのテスト

1. Ollamaにphi3:miniモデルをダウンロードして実行するように依頼する：

    ```shell
    ollama run phi3:mini
    ```

    これにはモデルのダウンロードに数分かかります。

2. 出力に「success」と表示されたら、プロンプトからそのモデルにメッセージを送信できます。

    ```shell
    >>> Write a haiku about hungry hippos
    ```

3. 数秒後、モデルからの応答がストリームで表示されるはずです。

4. 言語モデルで使用されるさまざまな技術について学ぶには、Pythonノートブックファイル[ollama.ipynb](../../code/01.Introduce/ollama.ipynb)を開き、各セルを実行します。'phi3:mini'以外のモデルを使用した場合は、最初のセルの`MODEL_NAME`を変更してください。

5. Pythonからphi3:miniモデルと対話するには、Pythonファイル[chat.py](../../code/01.Introduce/chat.py)を開いて実行します。必要に応じて、ファイルの上部にある`MODEL_NAME`を変更できます。また、システムメッセージを変更したり、少数のショット例を追加したりすることもできます。
