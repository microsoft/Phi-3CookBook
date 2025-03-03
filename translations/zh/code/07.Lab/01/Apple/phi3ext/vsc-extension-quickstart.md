# 欢迎使用您的 VS Code 扩展

## 文件夹内容

* 此文件夹包含您的扩展所需的所有文件。
* `package.json` - 这是声明扩展和命令的清单文件。
  * 示例插件注册了一个命令，并定义了其标题和命令名称。通过这些信息，VS Code 可以在命令面板中显示该命令。此时还不需要加载插件。
* `src/extension.ts` - 这是您实现命令的主文件。
  * 该文件导出一个函数 `activate`，它会在您的扩展首次激活时被调用（在本例中通过执行命令激活）。在 `activate` 函数中，我们调用了 `registerCommand`。
  * 我们将包含命令实现的函数作为第二个参数传递给 `registerCommand`。

## 设置

* 安装推荐的扩展（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 和 dbaeumer.vscode-eslint）。

## 立即启动并运行

* 按下 `F5` 打开一个加载了您的扩展的新窗口。
* 通过按下 (`Ctrl+Shift+P` 或在 Mac 上按 `Cmd+Shift+P`) 并键入 `Hello World`，从命令面板运行您的命令。
* 在 `src/extension.ts` 文件中设置断点以调试您的扩展。
* 在调试控制台中查看扩展的输出。

## 进行更改

* 修改 `src/extension.ts` 文件中的代码后，可以从调试工具栏重新启动扩展。
* 您也可以重新加载 (`Ctrl+R` 或在 Mac 上按 `Cmd+R`) VS Code 窗口以加载更改后的扩展。

## 探索 API

* 打开文件 `node_modules/@types/vscode/index.d.ts` 时，您可以查看我们完整的 API 集。

## 运行测试

* 安装 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)。
* 通过 **Tasks: Run Task** 命令运行 "watch" 任务。确保该任务正在运行，否则可能无法发现测试。
* 从活动栏打开 Testing 视图并点击 "Run Test" 按钮，或者使用快捷键 `Ctrl/Cmd + ; A`。
* 在 Test Results 视图中查看测试结果的输出。
* 修改 `src/test/extension.test.ts` 或在 `test` 文件夹中创建新的测试文件。
  * 提供的测试运行器只会考虑名称模式匹配 `**.test.ts` 的文件。
  * 您可以在 `test` 文件夹中创建子文件夹，以任意方式组织您的测试。

## 更进一步

* 通过 [打包您的扩展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension) 来减小扩展大小并提高启动速度。
* 在 VS Code 扩展市场上 [发布您的扩展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 通过设置 [持续集成](https://code.visualstudio.com/api/working-with-extensions/continuous-integration) 来自动化构建过程。

**免责声明**：  
本文件使用基于机器的人工智能翻译服务进行翻译。尽管我们尽力确保翻译的准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的原文作为权威来源。对于关键信息，建议寻求专业人工翻译。因使用本翻译而引起的任何误解或误读，我们概不负责。