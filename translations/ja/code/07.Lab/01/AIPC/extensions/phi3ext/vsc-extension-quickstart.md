# VS Code 拡張機能へようこそ

## フォルダーの内容

* このフォルダーには拡張機能に必要なすべてのファイルが含まれています。
* `package.json` - これは拡張機能とコマンドを宣言するマニフェストファイルです。
  * サンプルプラグインはコマンドを登録し、そのタイトルとコマンド名を定義します。この情報に基づいてVS Codeはコマンドパレットにコマンドを表示できます。まだプラグインをロードする必要はありません。
* `src/extension.ts` - これはコマンドの実装を提供するメインファイルです。
  * このファイルは1つの関数 `activate` をエクスポートし、これは拡張機能が初めてアクティブ化されたときに呼び出されます（この場合、コマンドを実行することによって）。`activate` 関数内で `registerCommand` を呼び出します。
  * コマンドの実装を含む関数を `registerCommand` の2番目のパラメーターとして渡します。

## セットアップ

* 推奨拡張機能をインストールする（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner、dbaeumer.vscode-eslint）

## すぐに始める

* `F5` を押して、拡張機能が読み込まれた新しいウィンドウを開きます。
* コマンドパレットからコマンドを実行するには、`Ctrl+Shift+P` を押すか（Macでは `Cmd+Shift+P`）、`Hello World` を入力します。
* `src/extension.ts` 内のコードにブレークポイントを設定して、拡張機能をデバッグします。
* デバッグコンソールで拡張機能の出力を確認します。

## 変更を加える

* `src/extension.ts` 内のコードを変更した後、デバッグツールバーから拡張機能を再起動できます。
* また、VS Codeウィンドウをリロードして（Windowsでは `Ctrl+R`、Macでは `Cmd+R`）変更を読み込むこともできます。

## APIを探索する

* ファイル `node_modules/@types/vscode/index.d.ts` を開くと、APIの完全なセットを確認できます。

## テストを実行する

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) をインストールします。
* **Tasks: Run Task** コマンドで "watch" タスクを実行します。これが実行されていることを確認してください。そうしないと、テストが検出されない場合があります。
* アクティビティバーからテストビューを開き、"Run Test" ボタンをクリックするか、ホットキー `Ctrl/Cmd + ; A` を使用します。
* テスト結果ビューでテスト結果の出力を確認します。
* `src/test/extension.test.ts` に変更を加えるか、`test` フォルダー内に新しいテストファイルを作成します。
  * 提供されたテストランナーは、名前パターン `**.test.ts` に一致するファイルのみを考慮します。
  * テストを任意の方法で構造化するために `test` フォルダー内にフォルダーを作成できます。

## さらに進む

* [拡張機能をバンドル](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo) することで、拡張機能のサイズを減らし、起動時間を改善します。
* [拡張機能を公開](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo) して、VS Code拡張機能マーケットプレイスで公開します。
* [継続的インテグレーション](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo) を設定してビルドを自動化します。

**免責事項**:
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期しておりますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知おきください。原文の母国語の文書が信頼できる情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤った解釈について、当社は一切責任を負いません。