# 欢迎使用您的 VS Code 扩展

## 文件夹中包含的内容

* 此文件夹包含了您的扩展所需的所有文件。
* `package.json` - 这是清单文件，您可以在其中声明您的扩展和命令。
  * 示例插件注册了一个命令，并定义了其标题和命令名称。通过这些信息，VS Code 可以在命令面板中显示该命令。目前还不需要加载插件。
* `src/extension.ts` - 这是您提供命令实现的主文件。
  * 该文件导出一个函数 `activate`，这是扩展首次激活时调用的函数（在本例中是通过执行命令激活）。在 `activate` 函数内部，我们调用了 `registerCommand`。
  * 我们将包含命令实现的函数作为第二个参数传递给 `registerCommand`。

## 设置

* 安装推荐的扩展（amodio.tsl-problem-matcher, ms-vscode.extension-test-runner 和 dbaeumer.vscode-eslint）

## 立即开始运行

* 按下 `F5` 打开一个加载了您的扩展的新窗口。
* 按下命令面板中的快捷键（`Ctrl+Shift+P` 或 Mac 上的 `Cmd+Shift+P`）并输入 `Hello World` 来运行您的命令。
* 在 `src/extension.ts` 文件中为您的代码设置断点以调试扩展。
* 在调试控制台中查看扩展的输出。

## 进行更改

* 在 `src/extension.ts` 文件中更改代码后，您可以从调试工具栏重新启动扩展。
* 您也可以通过重新加载 VS Code 窗口（按 `Ctrl+R` 或 Mac 上的 `Cmd+R`）来加载您的更改。

## 探索 API

* 打开文件 `node_modules/@types/vscode/index.d.ts`，即可查看我们完整的 API 集。

## 运行测试

* 安装 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 通过 **Tasks: Run Task** 命令运行 "watch" 任务。确保此任务正在运行，否则可能无法发现测试。
* 从活动栏打开测试视图并点击 "Run Test" 按钮，或者使用快捷键 `Ctrl/Cmd + ; A`。
* 在测试结果视图中查看测试结果的输出。
* 修改 `src/test/extension.test.ts` 或在 `test` 文件夹中创建新的测试文件。
  * 提供的测试运行器只会考虑匹配名称模式 `**.test.ts` 的文件。
  * 您可以在 `test` 文件夹中创建子文件夹，以任何您喜欢的方式组织测试。

## 更进一步

* [通过打包扩展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo) 来减少扩展大小并提高启动速度。
* [在 VS Code 扩展市场上发布您的扩展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo)。
* 通过设置 [持续集成](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo) 来实现自动化构建。

**免责声明**：  
本文件使用基于机器的人工智能翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的原始文件作为权威来源。对于关键信息，建议使用专业人工翻译。因使用此翻译而导致的任何误解或误读，我们概不负责。