# VS Code 拡張機能へようこそ

## フォルダーの内容

* このフォルダーには、拡張機能に必要なすべてのファイルが含まれています。
* `package.json` - これは、拡張機能とコマンドを宣言するマニフェストファイルです。
  * サンプルプラグインはコマンドを登録し、そのタイトルとコマンド名を定義します。この情報を使って、VS Code はコマンドパレットにコマンドを表示できます。まだプラグインをロードする必要はありません。
* `src/extension.ts` - これは、コマンドの実装を提供するメインファイルです。
  * ファイルは `activate` という1つの関数をエクスポートします。この関数は拡張機能が初めてアクティブ化されたとき（この場合はコマンドを実行することで）に呼び出されます。`activate` 関数の中で `registerCommand` を呼び出します。
  * コマンドの実装を含む関数を `registerCommand` の2番目のパラメーターとして渡します。

## セットアップ

* 推奨される拡張機能をインストールします (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, dbaeumer.vscode-eslint)


## すぐに始める

* `F5` を押して、拡張機能がロードされた新しいウィンドウを開きます。
* コマンドパレットからコマンドを実行するには、(`Ctrl+Shift+P` または Mac では `Cmd+Shift+P` を押して、`Hello World` と入力します。
* `src/extension.ts` 内のコードにブレークポイントを設定して、拡張機能をデバッグします。
* デバッグコンソールで拡張機能の出力を確認します。

## 変更を加える

* `src/extension.ts` のコードを変更した後、デバッグツールバーから拡張機能を再起動できます。
* また、拡張機能をロードするために VS Code ウィンドウを再読み込みすることもできます (`Ctrl+R` または Mac では `Cmd+R` を押します)。

## API を探索する

* ファイル `node_modules/@types/vscode/index.d.ts` を開くと、API の全セットを表示できます。

## テストを実行する

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) をインストールします。
* **Tasks: Run Task** コマンドで "watch" タスクを実行します。これが実行されていることを確認してください。そうでないと、テストが見つからない場合があります。
* アクティビティバーからテストビューを開き、"Run Test" ボタンをクリックするか、ホットキー `Ctrl/Cmd + ; A` を使用します。
* テスト結果ビューでテスト結果の出力を確認します。
* `src/test/extension.test.ts` に変更を加えるか、`test` フォルダー内に新しいテストファイルを作成します。
  * 提供されたテストランナーは、`**.test.ts` という名前パターンに一致するファイルのみを考慮します。
  * テストを任意の方法で構造化するために、`test` フォルダー内にフォルダーを作成できます。

## さらに進む

* [拡張機能をバンドルする](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo)ことで、拡張機能のサイズを減らし、起動時間を改善します。
* [拡張機能を公開する](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo)ことで、VS Code 拡張機能マーケットプレイスに公開します。
* [継続的インテグレーションを設定](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo)して、ビルドを自動化します。

**免責事項**：
この文書は機械翻訳AIサービスを使用して翻訳されています。正確さを期しておりますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご了承ください。原文の言語で記載された文書が権威ある情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤解について、当社は責任を負いません。