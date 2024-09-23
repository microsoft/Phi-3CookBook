# VS Code 拡張機能へようこそ

## フォルダーの内容

* このフォルダーには拡張機能に必要なすべてのファイルが含まれています。
* `package.json` - これは拡張機能とコマンドを宣言するマニフェストファイルです。
  * サンプルプラグインはコマンドを登録し、そのタイトルとコマンド名を定義します。この情報を使って、VS Codeはコマンドパレットにコマンドを表示できます。プラグインをまだロードする必要はありません。
* `src/extension.ts` - ここにコマンドの実装を提供するメインファイルです。
  * ファイルは1つの関数 `activate` をエクスポートしており、これは拡張機能が初めてアクティブ化されるとき（この場合はコマンドを実行することで）に呼び出されます。`activate` 関数内で `registerCommand` を呼び出します。
  * コマンドの実装を含む関数を `registerCommand` の2番目のパラメーターとして渡します。

## セットアップ

* 推奨される拡張機能をインストールします (amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, and dbaeumer.vscode-eslint)

## すぐに始める

* `F5` を押して、拡張機能が読み込まれた新しいウィンドウを開きます。
* コマンドパレットから (`Ctrl+Shift+P` または Macでは `Cmd+Shift+P`) を押して `Hello World` と入力してコマンドを実行します。
* `src/extension.ts` 内にブレークポイントを設定して拡張機能をデバッグします。
* デバッグコンソールで拡張機能の出力を確認します。

## 変更を加える

* `src/extension.ts` のコードを変更した後、デバッグツールバーから拡張機能を再起動できます。
* また、VS Codeウィンドウをリロード (`Ctrl+R` または Macでは `Cmd+R`) して変更を読み込むこともできます。

## APIを探索する

* `node_modules/@types/vscode/index.d.ts` ファイルを開くと、APIの全セットを確認できます。

## テストを実行する

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) をインストールします。
* **Tasks: Run Task** コマンドから "watch" タスクを実行します。これが実行されていることを確認してください。そうしないとテストが検出されない場合があります。
* アクティビティバーからテストビューを開き、"Run Test" ボタンをクリックするか、ホットキー `Ctrl/Cmd + ; A` を使用します。
* テスト結果ビューでテスト結果の出力を確認します。
* `src/test/extension.test.ts` に変更を加えるか、`test` フォルダー内に新しいテストファイルを作成します。
  * 提供されたテストランナーは、`**.test.ts` という名前パターンに一致するファイルのみを考慮します。
  * `test` フォルダー内にフォルダーを作成して、テストを任意の方法で構造化できます。

## さらに進む

* [拡張機能のバンドル](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) を行うことで、拡張機能のサイズを減らし、起動時間を改善します。
* [拡張機能を公開](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) して、VS Code拡張機能マーケットプレイスに公開します。
* [継続的インテグレーション](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) を設定してビルドを自動化します。

免責事項: この翻訳はAIモデルによって原文から翻訳されたものであり、完璧ではない可能性があります。出力内容を確認し、必要な修正を行ってください。