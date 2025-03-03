# VS Code拡張機能へようこそ

## フォルダーの内容

* このフォルダーには、拡張機能に必要なすべてのファイルが含まれています。
* `package.json` - これは、拡張機能とコマンドを宣言するマニフェストファイルです。
  * サンプルプラグインはコマンドを登録し、そのタイトルとコマンド名を定義します。この情報により、VS Codeはコマンドパレットにコマンドを表示できます。この時点ではプラグインをロードする必要はありません。
* `src/extension.ts` - これはコマンドの実装を提供するメインファイルです。
  * ファイルは1つの関数 `activate` をエクスポートします。この関数は拡張機能が初めてアクティブ化されたとき（この場合はコマンド実行時）に呼び出されます。`activate` 関数内で `registerCommand` を呼び出します。
  * コマンドの実装を含む関数を `registerCommand` の2番目のパラメーターとして渡します。

## セットアップ

* 推奨される拡張機能をインストールしてください（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner、dbaeumer.vscode-eslint）

## すぐに開始する

* `F5` を押して、拡張機能がロードされた新しいウィンドウを開きます。
* コマンドパレットからコマンドを実行します（`Ctrl+Shift+P` または Macでは `Cmd+Shift+P` を押して `Hello World` を入力します）。
* `src/extension.ts` 内のコードにブレークポイントを設定して拡張機能をデバッグします。
* デバッグコンソールで拡張機能の出力を確認します。

## 変更を加える

* `src/extension.ts` 内のコードを変更した後、デバッグツールバーから拡張機能を再起動できます。
* また、拡張機能をロードするためにVS Codeウィンドウを再読み込みすることもできます（`Ctrl+R` または Macでは `Cmd+R`）。

## APIを探索する

* `node_modules/@types/vscode/index.d.ts` ファイルを開くと、APIの完全なセットを確認できます。

## テストを実行する

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) をインストールします。
* **Tasks: Run Task** コマンドを使用して "watch" タスクを実行します。このタスクが実行されていないと、テストが認識されない場合があります。
* アクティビティバーからテストビューを開き、「Run Test」ボタンをクリックするか、ホットキー `Ctrl/Cmd + ; A` を使用します。
* テスト結果ビューでテスト結果の出力を確認します。
* `src/test/extension.test.ts` を変更するか、`test` フォルダー内に新しいテストファイルを作成します。
  * 提供されたテストランナーは `**.test.ts` という名前パターンに一致するファイルのみを考慮します。
  * テストを任意の方法で構造化するために `test` フォルダー内にフォルダーを作成できます。

## さらに進む

* [拡張機能をバンドルする](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo)ことで、拡張機能のサイズを削減し、起動時間を改善します。
* [拡張機能を公開する](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo)ことで、VS Code拡張機能マーケットプレイスに公開します。
* [継続的インテグレーション](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo)を設定してビルドを自動化します。

**免責事項**:  
本書類は、AI翻訳サービスを使用して機械的に翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確な箇所が含まれる可能性があります。原文（元の言語の文書）が正式かつ信頼できる情報源と見なされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の使用に起因する誤解や誤解釈について、当方は一切の責任を負いかねます。