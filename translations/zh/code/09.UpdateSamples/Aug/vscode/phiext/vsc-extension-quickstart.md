# 欢迎使用您的 VS Code 扩展

## 文件夹内容

* 此文件夹包含您扩展所需的所有文件。
* `package.json` - 这是声明您的扩展和命令的清单文件。
  * 示例插件注册了一个命令，并定义了其标题和命令名称。借助这些信息，VS Code 可以在命令面板中显示该命令。此时还不需要加载插件。
* `src/extension.ts` - 这是您提供命令实现的主文件。
  * 该文件导出一个函数 `activate`，这是在您的扩展首次激活时调用的（在本例中是通过执行命令激活）。在 `activate` 函数中，我们调用了 `registerCommand`。
  * 我们将包含命令实现的函数作为第二个参数传递给 `registerCommand`。

## 设置

* 安装推荐的扩展（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 和 dbaeumer.vscode-eslint）

## 立即上手

* 按 `F5` 打开一个加载了您扩展的新窗口。
* 按下 (`Ctrl+Shift+P` 或 Mac 上的 `Cmd+Shift+P`) 并输入 `Hello World`，从命令面板运行您的命令。
* 在 `src/extension.ts` 文件中设置断点以调试您的扩展。
* 在调试控制台中查看您的扩展输出。

## 进行修改

* 修改 `src/extension.ts` 中的代码后，可以从调试工具栏重新启动扩展。
* 您还可以通过重新加载 (`Ctrl+R` 或 Mac 上的 `Cmd+R`) VS Code 窗口来加载更改。

## 探索 API

* 打开文件 `node_modules/@types/vscode/index.d.ts`，即可查看我们 API 的完整内容。

## 运行测试

* 安装 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 通过 **Tasks: Run Task** 命令运行 "watch" 任务。确保该任务正在运行，否则测试可能无法被发现。
* 从活动栏打开测试视图，点击“Run Test”按钮，或者使用快捷键 `Ctrl/Cmd + ; A`。
* 在测试结果视图中查看测试结果的输出。
* 修改 `src/test/extension.test.ts` 或在 `test` 文件夹中创建新的测试文件。
  * 提供的测试运行器只会考虑名称模式为 `**.test.ts` 的文件。
  * 您可以在 `test` 文件夹中创建子文件夹，以任何您喜欢的方式组织测试。

## 更进一步

* 通过[打包扩展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension)来减小扩展体积并提升启动速度。
* 在 VS Code 扩展市场上[发布您的扩展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension)。
* 通过设置[持续集成](https://code.visualstudio.com/api/working-with-extensions/continuous-integration)来实现自动化构建。

**免责声明**：  
本文件使用基于机器的人工智能翻译服务进行翻译。虽然我们尽力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文的母语版本作为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用本翻译而引起的任何误解或误读，我们概不负责。