# VS Code 拡張機能へようこそ

## フォルダーの中身

* このフォルダーには拡張機能に必要なファイルがすべて含まれています。
* `package.json` - ここで拡張機能とコマンドを宣言します。
  * サンプルプラグインはコマンドを登録し、そのタイトルとコマンド名を定義します。この情報を使って、VS Codeはコマンドパレットにコマンドを表示できます。まだプラグインをロードする必要はありません。
* `src/extension.ts` - ここがコマンドの実装を提供するメインファイルです。
  * このファイルは1つの関数 `activate` をエクスポートしており、拡張機能が初めてアクティブ化されたとき（この場合はコマンドを実行することによって）に呼び出されます。`activate` 関数内で `registerCommand` を呼び出します。
  * コマンドの実装を含む関数を `registerCommand` の2番目のパラメータとして渡します。

## セットアップ

* 推奨される拡張機能をインストールします（amodio.tsl-problem-matcher, ms-vscode.extension-test-runner, dbaeumer.vscode-eslint）。

## すぐに使い始める

* `F5` を押して、拡張機能が読み込まれた新しいウィンドウを開きます。
* コマンドパレットからコマンドを実行します（`Ctrl+Shift+P` または Macでは `Cmd+Shift+P` を押して）`Hello World` と入力します。
* `src/extension.ts` 内にブレークポイントを設定して、拡張機能をデバッグします。
* デバッグコンソールで拡張機能の出力を確認します。

## 変更を加える

* `src/extension.ts` 内のコードを変更した後、デバッグツールバーから拡張機能を再起動できます。
* また、VS Codeウィンドウをリロードして（`Ctrl+R` または Macでは `Cmd+R`）変更を反映させることもできます。

## APIを探索する

* `node_modules/@types/vscode/index.d.ts` ファイルを開くと、APIの全セットを確認できます。

## テストを実行する

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) をインストールします。
* **Tasks: Run Task** コマンドを使って "watch" タスクを実行します。これが実行されていることを確認してください。そうでないとテストが見つからないかもしれません。
* アクティビティバーからテストビューを開き、"Run Test" ボタンをクリックするか、ホットキー `Ctrl/Cmd + ; A` を使います。
* テスト結果ビューでテスト結果の出力を確認します。
* `src/test/extension.test.ts` に変更を加えるか、`test` フォルダー内に新しいテストファイルを作成します。
  * 提供されたテストランナーは `**.test.ts` という名前パターンに一致するファイルのみを考慮します。
  * テストを任意の方法で構造化するために `test` フォルダー内にフォルダーを作成できます。

## さらに進む

* [拡張機能をバンドルする](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)ことで、拡張機能のサイズを削減し、起動時間を改善します。
* VS Code拡張機能マーケットプレイスで [拡張機能を公開する](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* [継続的インテグレーション](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)を設定してビルドを自動化します。

