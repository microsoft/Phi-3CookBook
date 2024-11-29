# VS Code 拡張機能へようこそ

## フォルダーの内容

* このフォルダーには、拡張機能に必要なすべてのファイルが含まれています。
* `package.json` - これは拡張機能とコマンドを宣言するマニフェストファイルです。
  * サンプルプラグインはコマンドを登録し、そのタイトルとコマンド名を定義します。この情報を使って、VS Codeはコマンドパレットにコマンドを表示できます。プラグインをロードする必要はまだありません。
* `src/extension.ts` - これはコマンドの実装を提供するメインファイルです。
  * ファイルは `activate` という関数をエクスポートし、これは拡張機能が最初にアクティブ化されたとき（この場合はコマンドを実行することによって）に呼び出されます。`activate` 関数の内部で `registerCommand` を呼び出します。
  * コマンドの実装を含む関数を `registerCommand` の第二引数として渡します。

## セットアップ

* 推奨される拡張機能をインストールします (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, dbaeumer.vscode-eslint)

## すぐに始める

* `F5` を押して、拡張機能がロードされた新しいウィンドウを開きます。
* コマンドパレットからコマンドを実行するには、(`Ctrl+Shift+P` または Mac では `Cmd+Shift+P`) を押して `Hello World` を入力します。
* `src/extension.ts` 内のコードにブレークポイントを設定して、拡張機能をデバッグします。
* デバッグコンソールで拡張機能の出力を確認します。

## 変更を加える

* `src/extension.ts` のコードを変更した後、デバッグツールバーから拡張機能を再起動できます。
* また、拡張機能をロードするために VS Code ウィンドウをリロード (`Ctrl+R` または Mac では `Cmd+R`) することもできます。

## APIを探る

* ファイル `node_modules/@types/vscode/index.d.ts` を開くと、APIの完全なセットを確認できます。

## テストを実行

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) をインストールします。
* **Tasks: Run Task** コマンドで "watch" タスクを実行します。これが実行されていることを確認してください。さもないとテストが検出されないかもしれません。
* アクティビティバーからテストビューを開き、「Run Test」ボタンをクリックするか、ホットキー `Ctrl/Cmd + ; A` を使用します。
* テスト結果ビューでテスト結果の出力を確認します。
* `src/test/extension.test.ts` に変更を加えるか、`test` フォルダー内に新しいテストファイルを作成します。
  * 提供されたテストランナーは、`**.test.ts` という名前パターンに一致するファイルのみを考慮します。
  * `test` フォルダー内にフォルダーを作成して、テストを任意の方法で構造化できます。

## さらに進む

* [拡張機能をバンドルする](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)ことで、拡張機能のサイズを減らし、起動時間を改善します。
* VS Code 拡張機能マーケットプレースで [拡張機能を公開する](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* [継続的インテグレーション](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)を設定してビルドを自動化します。

**免責事項**:
この文書は機械ベースのAI翻訳サービスを使用して翻訳されています。正確さを期していますが、自動翻訳には誤りや不正確さが含まれる場合があります。元の言語での原文を権威ある情報源とみなすべきです。重要な情報については、専門の人間による翻訳をお勧めします。この翻訳の使用に起因する誤解や誤訳について、当社は一切の責任を負いません。