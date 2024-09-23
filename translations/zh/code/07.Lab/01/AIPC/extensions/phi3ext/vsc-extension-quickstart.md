# 欢迎使用您的 VS Code 扩展

## 文件夹内容

* 这个文件夹包含了您的扩展所需的所有文件。
* `package.json` - 这是您声明扩展和命令的清单文件。
  * 示例插件注册了一个命令，并定义了它的标题和命令名称。通过这些信息，VS Code 可以在命令面板中显示该命令。它还不需要加载插件。
* `src/extension.ts` - 这是您实现命令的主要文件。
  * 该文件导出一个函数 `activate`，该函数在您的扩展第一次被激活时（在这种情况下通过执行命令）被调用。在 `activate` 函数内部，我们调用 `registerCommand`。
  * 我们将包含命令实现的函数作为第二个参数传递给 `registerCommand`。

## 设置

* 安装推荐的扩展（amodio.tsl-problem-matcher、ms-vscode.extension-test-runner 和 dbaeumer.vscode-eslint）

## 立即启动并运行

* 按 `F5` 打开一个加载了您的扩展的新窗口。
* 在命令面板中按 (`Ctrl+Shift+P` 或 Mac 上的 `Cmd+Shift+P`) 并输入 `Hello World` 来运行您的命令。
* 在 `src/extension.ts` 中设置断点以调试您的扩展。
* 在调试控制台中查找您的扩展的输出。

## 进行更改

* 在 `src/extension.ts` 中更改代码后，可以从调试工具栏重新启动扩展。
* 您也可以通过重新加载 (`Ctrl+R` 或 Mac 上的 `Cmd+R`) VS Code 窗口来加载您的更改。

## 探索 API

* 打开文件 `node_modules/@types/vscode/index.d.ts` 可以查看我们 API 的完整集合。

## 运行测试

* 安装 [Extension Test Runner](https://marketplace.visualstudio.com/items?itemName=ms-vscode.extension-test-runner)
* 通过 **Tasks: Run Task** 命令运行 "watch" 任务。确保该任务正在运行，否则可能无法发现测试。
* 从活动栏中打开测试视图并点击 "Run Test" 按钮，或者使用快捷键 `Ctrl/Cmd + ; A`
* 在测试结果视图中查看测试结果的输出。
* 对 `src/test/extension.test.ts` 进行更改或在 `test` 文件夹内创建新的测试文件。
  * 提供的测试运行器只会考虑名称模式匹配 `**.test.ts` 的文件。
  * 您可以在 `test` 文件夹内创建文件夹，以任何您想要的方式来组织您的测试。

## 更进一步

* 通过[打包您的扩展](https://code.visualstudio.com/api/working-with-extensions/bundling-extension?WT.mc_id=aiml-137032-kinfeylo)来减少扩展的大小并提升启动时间。
* 在 VS Code 扩展市场上[发布您的扩展](https://code.visualstudio.com/api/working-with-extensions/publishing-extension?WT.mc_id=aiml-137032-kinfeylo)。
* 通过设置[持续集成](https://code.visualstudio.com/api/working-with-extensions/continuous-integration?WT.mc_id=aiml-137032-kinfeylo)来自动化构建。

免责声明：本翻译由AI模型从原文翻译而来，可能不完全准确。请审阅输出内容并进行必要的修改。