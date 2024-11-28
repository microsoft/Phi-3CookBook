# VS Code 拡張機能へようこそ

## フォルダーの内容

* このフォルダーには、拡張機能に必要なすべてのファイルが含まれています。
* `package.json` - これは拡張機能とコマンドを宣言するマニフェストファイルです。
  * サンプルプラグインはコマンドを登録し、そのタイトルとコマンド名を定義します。この情報を使って、VS Codeはコマンドパレットにコマンドを表示できます。プラグインをまだロードする必要はありません。
* `src/extension.ts` - これはコマンドの実装を提供するメインファイルです。
  * このファイルは1つの関数 `activate` をエクスポートし、これは拡張機能が初めてアクティブ化されたときに呼び出されます（この場合、コマンドを実行することで）。`activate` 関数の中で `registerCommand` を呼び出します。
  * コマンドの実装を含む関数を `registerCommand` の2番目のパラメーターとして渡します。

## セットアップ

* 推奨される拡張機能をインストールします (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, および dbaeumer.vscode-eslint)

## すぐに始める

* `F5` を押して、拡張機能が読み込まれた新しいウィンドウを開きます。
* コマンドパレットからコマンドを実行するには、(`Ctrl+Shift+P` または Macでは `Cmd+Shift+P`) を押して `Hello World` と入力します。
* `src/extension.ts` 内のコードにブレークポイントを設定して、拡張機能をデバッグします。
* デバッグコンソールで拡張機能の出力を確認します。

## 変更を加える

* `src/extension.ts` 内のコードを変更した後、デバッグツールバーから拡張機能を再起動できます。
* また、(`Ctrl+R` または Macでは `Cmd+R`) を押して、VS Codeウィンドウをリロードして変更を反映させることもできます。

## APIを探索する

* `node_modules/@types/vscode/index.d.ts` ファイルを開くと、APIの全セットを確認できます。

## テストを実行する

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) をインストールします。
* **Tasks: Run Task** コマンドを使って "watch" タスクを実行します。これが実行されていることを確認してください。そうしないと、テストが見つからない可能性があります。
* アクティビティバーからテストビューを開き、"Run Test" ボタンをクリックするか、ホットキー `Ctrl/Cmd + ; A` を使用します。
* テスト結果ビューでテスト結果の出力を確認します。
* `src/test/extension.test.ts` に変更を加えるか、`test` フォルダー内に新しいテストファイルを作成します。
  * 提供されたテストランナーは `**.test.ts` という名前パターンに一致するファイルのみを考慮します。
  * `test` フォルダー内にフォルダーを作成して、テストを好きなように構造化できます。

## さらに進む

* [拡張機能をバンドルする](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)ことで、拡張機能のサイズを減らし、起動時間を改善します。
* VS Code拡張機能マーケットプレイスで[拡張機能を公開する](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* [継続的インテグレーション](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)を設定してビルドを自動化します。

**免責事項**:
この文書は機械翻訳サービスを使用して翻訳されています。正確さを期していますが、自動翻訳にはエラーや不正確な部分が含まれる可能性があります。原文を権威ある情報源と見なしてください。重要な情報については、専門の人間による翻訳を推奨します。この翻訳の使用により生じる誤解や誤解については、一切の責任を負いかねます。