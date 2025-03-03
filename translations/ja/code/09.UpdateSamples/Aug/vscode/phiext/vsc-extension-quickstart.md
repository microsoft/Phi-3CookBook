# VS Code 拡張機能へようこそ

## フォルダーの内容

* このフォルダーには、拡張機能に必要なすべてのファイルが含まれています。
* `package.json` - これは、拡張機能やコマンドを宣言するマニフェストファイルです。
  * サンプルプラグインはコマンドを登録し、そのタイトルとコマンド名を定義します。この情報により、VS Code はコマンドパレットにコマンドを表示できます。この段階ではプラグインをロードする必要はありません。
* `src/extension.ts` - これはコマンドの実装を提供するメインファイルです。
  * このファイルは `activate` という関数をエクスポートします。この関数は拡張機能が初めてアクティブ化されたとき（この場合はコマンドを実行したとき）に呼び出されます。`activate` 関数内で `registerCommand` を呼び出します。
  * コマンドの実装を含む関数を `registerCommand` の2番目のパラメーターとして渡します。

## セットアップ

* 推奨される拡張機能をインストールしてください (amodio.tsl-problem-matcher、ms-vscode.extension-test-runner、dbaeumer.vscode-eslint)


## すぐに動作させる

* `F5` を押して、拡張機能がロードされた新しいウィンドウを開きます。
* コマンドパレットからコマンドを実行します (`Ctrl+Shift+P` または Mac の場合は `Cmd+Shift+P` を押して `Hello World` と入力)。
* `src/extension.ts` 内のコードにブレークポイントを設定して、拡張機能をデバッグします。
* デバッグコンソールで拡張機能の出力を確認します。

## 変更を加える

* `src/extension.ts` のコードを変更した後、デバッグツールバーから拡張機能を再起動できます。
* また、VS Code ウィンドウをリロードすることで (`Ctrl+R` または Mac の場合は `Cmd+R`)、変更をロードすることもできます。


## API を探索する

* `node_modules/@types/vscode/index.d.ts` ファイルを開くと、API の完全なセットを確認できます。

## テストを実行する

* [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner) をインストールしてください。
* **Tasks: Run Task** コマンドを使用して "watch" タスクを実行します。このタスクが実行中でないと、テストが検出されない場合があります。
* アクティビティバーのテストビューを開き、「Run Test」ボタンをクリックするか、ホットキー `Ctrl/Cmd + ; A` を使用します。
* テスト結果の出力はテスト結果ビューで確認できます。
* `src/test/extension.test.ts` を変更するか、`test` フォルダー内に新しいテストファイルを作成してください。
  * 提供されているテストランナーは、`**.test.ts` という名前パターンに一致するファイルのみを考慮します。
  * テストを任意の方法で構造化するために、`test` フォルダー内にフォルダーを作成できます。

## 次のステップへ

* [拡張機能をバンドル](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) することで、拡張機能のサイズを削減し、起動時間を短縮します。
* [拡張機能を公開](https://code.visualstudio.com/api/working-with-extensions/publishing-extension) して、VS Code 拡張機能マーケットプレイスで共有します。
* [継続的インテグレーション (CI)](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) を設定して、ビルドを自動化します。

**免責事項**:  
この文書は、機械ベースのAI翻訳サービスを使用して翻訳されています。正確性を追求しておりますが、自動翻訳には誤りや不正確さが含まれる可能性があることをご承知おきください。原文が記載された元の言語の文書が公式な情報源とみなされるべきです。重要な情報については、専門の人間による翻訳をお勧めします。本翻訳の使用に起因する誤解や解釈の誤りについて、当社は一切の責任を負いません。