# VS Code拡張機能へようこそ

## フォルダーの中身

* このフォルダーには、拡張機能に必要なすべてのファイルが含まれています。
* `package.json` - これは、拡張機能とコマンドを宣言するマニフェストファイルです。
  * サンプルプラグインはコマンドを登録し、そのタイトルとコマンド名を定義します。この情報をもとにVS Codeはコマンドパレットにコマンドを表示します。プラグインをまだ読み込む必要はありません。
* `src/extension.ts` - これは、コマンドの実装を提供するメインファイルです。
  * このファイルは`activate`という関数をエクスポートしており、拡張機能が最初にアクティブ化された際（この場合はコマンドを実行したとき）に呼び出されます。`activate`関数内で`registerCommand`を呼び出します。
  * コマンドの実装を含む関数を`registerCommand`の2番目のパラメーターとして渡します。

## セットアップ

* 推奨される拡張機能をインストールしてください（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner、dbaeumer.vscode-eslint）

## すぐに始める

* `F5`を押して、拡張機能が読み込まれた新しいウィンドウを開きます。
* コマンドパレットからコマンドを実行します（`Ctrl+Shift+P`またはMacでは`Cmd+Shift+P`を押し、`Hello World`と入力）。
* `src/extension.ts`内のコードにブレークポイントを設定して、拡張機能をデバッグします。
* デバッグコンソールで拡張機能の出力を確認します。

## 変更を加える

* `src/extension.ts`内のコードを変更した後、デバッグツールバーから拡張機能を再起動できます。
* または、VS Codeウィンドウを再読み込みして（`Ctrl+R`またはMacでは`Cmd+R`）、変更を反映することもできます。

## APIを探る

* `node_modules/@types/vscode/index.d.ts`ファイルを開くと、APIの全セットを見ることができます。

## テストを実行する

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)をインストールします。
* **Tasks: Run Task**コマンドを使って「watch」タスクを実行します。これが実行中でないと、テストが認識されない場合があります。
* アクティビティバーからテストビューを開き、「Run Test」ボタンをクリックするか、ホットキー`Ctrl/Cmd + ; A`を使用します。
* テスト結果の出力を「Test Results」ビューで確認します。
* `src/test/extension.test.ts`を変更するか、`test`フォルダー内に新しいテストファイルを作成します。
  * 提供されたテストランナーは、`**.test.ts`という名前パターンに一致するファイルのみを考慮します。
  * `test`フォルダー内にフォルダーを作成し、テストを任意の方法で構造化できます。

## 次のステップ

* [拡張機能をバンドル](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)することで、拡張機能のサイズを削減し、起動時間を改善します。
* [拡張機能を公開](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)して、VS Code拡張機能マーケットプレイスに登録します。
* [継続的インテグレーション](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)を設定してビルドを自動化します。

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を追求していますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご了承ください。元の言語で書かれた原文が公式な情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の使用に起因する誤解や解釈の相違について、当方は一切の責任を負いません。