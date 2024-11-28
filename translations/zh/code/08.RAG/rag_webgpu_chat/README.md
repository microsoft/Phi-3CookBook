Phi-3-mini WebGPU RAG 聊天机器人

## 演示展示 WebGPU 和 RAG 模式
使用 Phi-3 Onnx 托管模型的 RAG 模式利用了检索增强生成方法，将 Phi-3 模型的强大功能与 ONNX 托管相结合，以实现高效的 AI 部署。这种模式在为特定领域任务微调模型时非常有用，提供了质量、成本效益和长上下文理解的结合。它是 Azure AI 套件的一部分，提供了易于查找、试用和使用的广泛模型，满足各行业的定制需求。Phi-3 模型，包括 Phi-3-mini、Phi-3-small 和 Phi-3-medium，均可在 Azure AI Model Catalog 上获得，并可以自我管理或通过 HuggingFace 和 ONNX 等平台进行微调和部署，展示了微软对可访问和高效 AI 解决方案的承诺。

## 什么是 WebGPU
WebGPU 是一种现代的网页图形 API，旨在直接从网页浏览器提供对设备图形处理单元（GPU）的高效访问。它被认为是 WebGL 的继任者，提供了几个关键改进：

1. **兼容现代 GPU**：WebGPU 构建为无缝兼容当代 GPU 架构，利用系统 API 如 Vulkan、Metal 和 Direct3D 12。
2. **增强性能**：支持通用 GPU 计算和更快的操作，适用于图形渲染和机器学习任务。
3. **高级功能**：WebGPU 提供对更高级 GPU 功能的访问，支持更复杂和动态的图形和计算工作负载。
4. **减少 JavaScript 工作负载**：通过将更多任务卸载到 GPU，WebGPU 显著减少了 JavaScript 的工作负载，从而提高性能和流畅体验。

目前，WebGPU 在 Google Chrome 等浏览器中得到支持，并正在努力扩展到其他平台。

### 03.WebGPU
所需环境：

**支持的浏览器：**
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18 (macOS 15)
- Firefox Nightly

### 启用 WebGPU：

- 在 Chrome/Microsoft Edge 中

启用 `chrome://flags/#enable-unsafe-webgpu` 标志。

#### 打开浏览器：
启动 Google Chrome 或 Microsoft Edge。

#### 访问 Flags 页面：
在地址栏中输入 `chrome://flags` 并按回车。

#### 搜索标志：
在页面顶部的搜索框中输入 'enable-unsafe-webgpu'

#### 启用标志：
在结果列表中找到 #enable-unsafe-webgpu 标志。

点击其旁边的下拉菜单并选择 Enabled。

#### 重启浏览器：

启用标志后，您需要重启浏览器以使更改生效。点击页面底部出现的 Relaunch 按钮。

- 对于 Linux，使用 `--enable-features=Vulkan` 启动浏览器。
- Safari 18 (macOS 15) 默认启用 WebGPU。
- 在 Firefox Nightly 中，输入 about:config 在地址栏中并 `set dom.webgpu.enabled to true`。

### 为 Microsoft Edge 设置 GPU

以下是在 Windows 上为 Microsoft Edge 设置高性能 GPU 的步骤：

- **打开设置：** 点击开始菜单并选择设置。
- **系统设置：** 进入系统，然后选择显示。
- **图形设置：** 向下滚动并点击图形设置。
- **选择应用：** 在“选择要设置首选项的应用”下，选择桌面应用然后浏览。
- **选择 Edge：** 导航到 Edge 安装文件夹（通常是 `C:\Program Files (x86)\Microsoft\Edge\Application`）并选择 `msedge.exe`。
- **设置首选项：** 点击选项，选择高性能，然后点击保存。
这将确保 Microsoft Edge 使用高性能 GPU 以获得更好的性能。
- **重启** 你的机器以使这些设置生效。

### 打开你的 Codespace：
导航到你的 GitHub 仓库。
点击 Code 按钮并选择 Open with Codespaces。

如果你还没有 Codespace，可以点击 New codespace 创建一个。

**注意** 在你的 codespace 中安装 Node 环境
从 GitHub Codespace 运行 npm 演示是测试和开发项目的好方法。以下是帮助你入门的分步指南：

### 设置你的环境：
一旦你的 Codespace 打开，确保你已安装 Node.js 和 npm。你可以通过运行以下命令来检查：
```
node -v
```
```
npm -v
```

如果没有安装，可以使用以下命令安装：
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### 导航到你的项目目录：
使用终端导航到 npm 项目所在的目录：
```
cd path/to/your/project
```

### 安装依赖：
运行以下命令以安装 package.json 文件中列出的所有必要依赖：
```
npm install
```

### 运行演示：
一旦依赖安装完成，你可以运行你的演示脚本。通常在 package.json 的 scripts 部分指定。例如，如果你的演示脚本名为 start，你可以运行：
```
npm run build
```
```
npm run dev
```

### 访问演示：
如果你的演示涉及一个 web 服务器，Codespaces 会提供一个 URL 以访问它。查找通知或检查 Ports 选项卡以找到 URL。

**注意：** 模型需要在浏览器中缓存，因此可能需要一些时间来加载。

### RAG 演示
上传 markdown 文件 `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### 选择你的文件：
点击“选择文件”按钮以选择你要上传的文档。

### 上传文档：
选择文件后，点击“上传”按钮以加载你的文档用于 RAG（检索增强生成）。

### 开始聊天：
一旦文档上传完成，你可以基于文档内容开始使用 RAG 的聊天会话。

**免责声明**：
本文件已使用基于机器的人工智能翻译服务进行翻译。虽然我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应将原文档的本国语言版本视为权威来源。对于关键信息，建议使用专业人工翻译。对于因使用此翻译而产生的任何误解或误释，我们概不负责。