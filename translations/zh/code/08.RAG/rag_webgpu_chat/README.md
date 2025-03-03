Phi-3-mini WebGPU RAG 聊天机器人

## 展示 WebGPU 和 RAG 模式的演示
基于 Phi-3 Onnx 托管模型的 RAG 模式利用了检索增强生成（Retrieval-Augmented Generation）方法，将 Phi-3 模型的强大功能与 ONNX 托管相结合，实现高效的 AI 部署。这种模式对于领域特定任务的模型微调至关重要，兼具高质量、成本效益和长上下文理解能力。它是 Azure AI 套件的一部分，提供了易于查找、试用和使用的广泛模型选择，满足各行业的定制需求。Phi-3 模型，包括 Phi-3-mini、Phi-3-small 和 Phi-3-medium，可在 Azure AI 模型目录中找到，并支持自管理部署或通过 HuggingFace 和 ONNX 平台部署，体现了微软对可访问且高效的 AI 解决方案的承诺。

## 什么是 WebGPU
WebGPU 是一种现代化的网页图形 API，旨在直接从网络浏览器高效访问设备的图形处理单元（GPU）。它是 WebGL 的继任者，提供了以下几项关键改进：

1. **兼容现代 GPU**：WebGPU 专为与当代 GPU 架构无缝协作而设计，利用了 Vulkan、Metal 和 Direct3D 12 等系统 API。
2. **性能增强**：支持通用 GPU 计算和更快的操作，适用于图形渲染和机器学习任务。
3. **高级功能**：提供对更高级 GPU 功能的访问，支持更复杂和动态的图形及计算工作负载。
4. **降低 JavaScript 工作负载**：通过将更多任务卸载到 GPU，WebGPU 显著减少了 JavaScript 的工作负载，从而提升性能并提供更流畅的体验。

目前，WebGPU 已在 Google Chrome 等浏览器中得到支持，并在持续扩展至其他平台。

### 03.WebGPU
所需环境：

**支持的浏览器：**
- Google Chrome 113+
- Microsoft Edge 113+
- Safari 18（macOS 15）
- Firefox Nightly

### 启用 WebGPU：

- 在 Chrome/Microsoft Edge 中

启用 `chrome://flags/#enable-unsafe-webgpu` 标志。

#### 打开浏览器：
启动 Google Chrome 或 Microsoft Edge。

#### 访问 Flags 页面：
在地址栏中输入 `chrome://flags` 并按 Enter。

#### 搜索标志：
在页面顶部的搜索框中输入 'enable-unsafe-webgpu'。

#### 启用标志：
在结果列表中找到 #enable-unsafe-webgpu 标志。

点击旁边的下拉菜单并选择 Enabled。

#### 重启浏览器：

启用标志后，需要重启浏览器以使更改生效。点击页面底部出现的 Relaunch 按钮。

- 对于 Linux，请使用 `--enable-features=Vulkan` 启动浏览器。
- Safari 18（macOS 15）默认启用了 WebGPU。
- 在 Firefox Nightly 中，在地址栏输入 about:config 并 `set dom.webgpu.enabled to true`。

### 为 Microsoft Edge 设置 GPU 

以下是在 Windows 上为 Microsoft Edge 设置高性能 GPU 的步骤：

- **打开设置：** 点击开始菜单并选择设置。
- **系统设置：** 进入系统，然后选择显示。
- **图形设置：** 向下滚动并点击图形设置。
- **选择应用：** 在“选择一个应用以设置首选项”下，选择桌面应用，然后点击浏览。
- **选择 Edge：** 导航到 Edge 的安装文件夹（通常是 `C:\Program Files (x86)\Microsoft\Edge\Application`），并选择 `msedge.exe`。
- **设置首选项：** 点击选项，选择高性能，然后点击保存。
确保 Microsoft Edge 使用高性能 GPU 以获得更好的性能。
- **重启** 你的设备以使这些设置生效。

### 打开你的 Codespace：
导航到你的 GitHub 仓库。
点击 Code 按钮并选择 Open with Codespaces。

如果还没有 Codespace，可以点击 New codespace 创建一个。

**注意** 在你的 Codespace 中安装 Node 环境
从 GitHub Codespace 运行 npm 演示是测试和开发项目的好方法。以下是帮助你开始的分步指南：

### 设置你的环境：
打开 Codespace 后，确保已安装 Node.js 和 npm。你可以通过运行以下命令检查：
```
node -v
```
```
npm -v
```

如果未安装，可以使用以下命令安装：
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

### 安装依赖项：
运行以下命令以安装 package.json 文件中列出的所有必要依赖项：

```
npm install
```

### 运行演示：
安装依赖项后，可以运行演示脚本。通常在 package.json 的 scripts 部分中指定。例如，如果演示脚本名为 start，可以运行：

```
npm run build
```
```
npm run dev
```

### 访问演示：
如果你的演示涉及一个网络服务器，Codespaces 会提供一个 URL 供你访问。查找通知或检查 Ports 标签以找到 URL。

**注意：** 模型需要在浏览器中缓存，因此加载可能需要一些时间。

### RAG 演示
上传 Markdown 文件 `intro_rag.md` to complete the RAG solution. If using codespaces you can download the file located in `01.InferencePhi3/docs/`

### 选择文件：
点击“选择文件”按钮，选择你想上传的文档。

### 上传文档：
选择文件后，点击“上传”按钮，将文档加载到 RAG（检索增强生成）中。

### 开始聊天：
文档上传后，你可以基于文档内容使用 RAG 开始聊天会话。

**免责声明**：  
本文件使用基于机器的人工智能翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的原始文件作为权威来源。对于关键信息，建议寻求专业人工翻译。因使用本翻译而导致的任何误解或误读，我们概不负责。