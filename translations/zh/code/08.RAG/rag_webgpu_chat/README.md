Phi-3-mini WebGPU RAG 聊天机器人

## 演示展示 WebGPU 和 RAG 模式
利用 Phi-3 Onnx 托管模型的 RAG 模式采用了检索增强生成的方法，将 Phi-3 模型的强大功能与 ONNX 托管结合起来，实现高效的 AI 部署。这种模式在微调特定领域任务的模型方面非常重要，提供了质量、成本效益和长文本理解的结合。这是 Azure AI 套件的一部分，提供了易于查找、试用和使用的广泛模型，满足各行各业的定制需求。Phi-3 模型，包括 Phi-3-mini、Phi-3-small 和 Phi-3-medium，可在 Azure AI 模型目录中找到，并且可以自我管理或通过 HuggingFace 和 ONNX 等平台进行微调和部署，展示了微软对可访问和高效 AI 解决方案的承诺。

## 什么是 WebGPU
WebGPU 是一种现代的网页图形 API，旨在直接从网页浏览器高效访问设备的图形处理单元（GPU）。它是 WebGL 的继任者，提供了几个关键改进：

1. **兼容现代 GPU**：WebGPU 旨在无缝兼容当代 GPU 架构，利用 Vulkan、Metal 和 Direct3D 12 等系统 API。
2. **增强性能**：支持通用 GPU 计算和更快的操作，适用于图形渲染和机器学习任务。
3. **高级功能**：WebGPU 提供对更高级的 GPU 功能的访问，支持更复杂和动态的图形和计算工作负载。
4. **减少 JavaScript 工作量**：通过将更多任务卸载到 GPU，WebGPU 显著减少了 JavaScript 的工作量，从而提升性能并带来更流畅的体验。

目前，WebGPU 在 Google Chrome 等浏览器中受支持，并正在努力扩展到其他平台。

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
在地址栏中输入 `chrome://flags` 并按下 Enter。

#### 搜索标志：
在页面顶部的搜索框中输入 'enable-unsafe-webgpu'

#### 启用标志：
在结果列表中找到 #enable-unsafe-webgpu 标志。

点击旁边的下拉菜单并选择 Enabled。

#### 重启浏览器：

启用标志后，您需要重启浏览器以使更改生效。点击页面底部出现的 Relaunch 按钮。

- 对于 Linux，使用 `--enable-features=Vulkan` 启动浏览器。
- Safari 18 (macOS 15) 默认启用 WebGPU。
- 在 Firefox Nightly 中，在地址栏输入 about:config 并设置 `dom.webgpu.enabled` 为 true。

### 为 Microsoft Edge 设置 GPU

以下是在 Windows 上为 Microsoft Edge 设置高性能 GPU 的步骤：

- **打开设置：** 点击开始菜单并选择设置。
- **系统设置：** 进入系统，然后选择显示。
- **图形设置：** 向下滚动并点击图形设置。
- **选择应用：** 在“选择应用以设置偏好”下，选择桌面应用程序，然后浏览。
- **选择 Edge：** 导航到 Edge 安装文件夹（通常是 `C:\Program Files (x86)\Microsoft\Edge\Application`）并选择 `msedge.exe`。
- **设置偏好：** 点击选项，选择高性能，然后点击保存。
这将确保 Microsoft Edge 使用您的高性能 GPU 以获得更好的性能。
- **重启** 机器以使这些设置生效。

### 打开您的 Codespace：
导航到您的 GitHub 仓库。
点击 Code 按钮并选择 Open with Codespaces。

如果您还没有 Codespace，可以点击 New codespace 创建一个。

**注意** 在您的 Codespace 中安装 Node 环境
从 GitHub Codespace 运行 npm 演示是测试和开发项目的好方法。以下是帮助您入门的分步指南：

### 设置您的环境：
一旦您的 Codespace 打开，确保您已安装 Node.js 和 npm。您可以通过运行以下命令来检查：
```
node -v
```
```
npm -v
```

如果它们未安装，您可以使用以下命令安装：
```
sudo apt-get update
```
```
sudo apt-get install nodejs npm
```

### 导航到您的项目目录：
使用终端导航到您的 npm 项目所在的目录：
```
cd path/to/your/project
```

### 安装依赖项：
运行以下命令以安装 package.json 文件中列出的所有必要依赖项：

```
npm install
```

### 运行演示：
依赖项安装完成后，您可以运行演示脚本。通常在 package.json 的 scripts 部分指定。例如，如果您的演示脚本名为 start，您可以运行：

```
npm run build
```
```
npm run dev
```

### 访问演示：
如果您的演示涉及到一个 Web 服务器，Codespaces 将提供一个 URL 以访问它。查找通知或检查 Ports 选项卡以找到 URL。

**注意：** 模型需要在浏览器中缓存，因此可能需要一些时间加载。

### RAG 演示
上传 markdown 文件 `intro_rag.md` 以完成 RAG 解决方案。如果使用 codespaces，您可以下载位于 `01.InferencePhi3/docs/` 的文件。

### 选择您的文件：
点击“选择文件”按钮以选择您要上传的文档。

### 上传文档：
选择文件后，点击“上传”按钮以加载您的文档以进行 RAG（检索增强生成）。

### 开始聊天：
一旦文档上传，您可以基于文档内容开始使用 RAG 进行聊天。

免责声明：本翻译由人工智能模型从原文翻译而来，可能不够完美。请审查输出内容并进行必要的修改。