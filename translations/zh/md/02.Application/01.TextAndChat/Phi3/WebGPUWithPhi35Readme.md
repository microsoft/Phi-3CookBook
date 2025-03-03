# Phi-3.5-Instruct WebGPU RAG Chatbot

## 展示 WebGPU 和 RAG 模式的演示

基于 Phi-3.5 Onnx 托管模型的 RAG 模式采用了检索增强生成（Retrieval-Augmented Generation）方法，将 Phi-3.5 模型的强大功能与 ONNX 托管相结合，实现高效的 AI 部署。此模式在针对领域特定任务进行模型微调时尤为重要，兼具高质量、成本效益和长上下文理解能力。它是 Azure AI 套件的一部分，提供了广泛的模型选择，易于查找、试用和使用，满足各行业的定制化需求。

## 什么是 WebGPU
WebGPU 是一种现代化的网页图形 API，旨在直接通过网页浏览器高效访问设备的图形处理单元（GPU）。它被设计为 WebGL 的继任者，提供了若干关键改进：

1. **兼容现代 GPU**：WebGPU 专为与当代 GPU 架构无缝协作而设计，利用 Vulkan、Metal 和 Direct3D 12 等系统 API。
2. **性能提升**：支持通用 GPU 计算和更快速的操作，使其适用于图形渲染和机器学习任务。
3. **高级功能**：WebGPU 提供对更高级 GPU 功能的访问，能够支持更复杂和动态的图形及计算工作负载。
4. **减少 JavaScript 负担**：通过将更多任务卸载到 GPU，WebGPU 显著降低了 JavaScript 的工作负载，从而提升性能并带来更流畅的体验。

WebGPU 目前已在 Google Chrome 等浏览器中支持，其他平台的支持工作也在持续进行中。

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

#### 打开您的浏览器：
启动 Google Chrome 或 Microsoft Edge。

#### 访问 Flags 页面：
在地址栏中输入 `chrome://flags` 并按 Enter。

#### 搜索标志：
在页面顶部的搜索框中输入 'enable-unsafe-webgpu'。

#### 启用标志：
在搜索结果列表中找到 #enable-unsafe-webgpu 标志。

点击旁边的下拉菜单并选择 Enabled。

#### 重启浏览器：

启用标志后，您需要重启浏览器以使更改生效。点击页面底部出现的 Relaunch 按钮。

- 对于 Linux，请使用 `--enable-features=Vulkan` 启动浏览器。
- Safari 18（macOS 15）默认启用 WebGPU。
- 在 Firefox Nightly 中，输入 about:config 到地址栏，然后 `set dom.webgpu.enabled to true`。

### 为 Microsoft Edge 设置 GPU

以下是在 Windows 上为 Microsoft Edge 设置高性能 GPU 的步骤：

- **打开设置：** 点击开始菜单并选择设置。  
- **系统设置：** 进入系统，然后点击显示。  
- **图形设置：** 向下滚动并点击图形设置。  
- **选择应用：** 在“选择一个应用以设置首选项”下，选择桌面应用，然后点击浏览。  
- **选择 Edge：** 找到 Edge 的安装文件夹（通常是 `C:\Program Files (x86)\Microsoft\Edge\Application`），然后选择 `msedge.exe`。  
- **设置首选项：** 点击选项，选择高性能，然后点击保存。  
这将确保 Microsoft Edge 使用高性能 GPU，以获得更好的性能。  
- **重启** 机器以使这些设置生效。

### 示例：请[点击此链接](https://github.com/microsoft/aitour-exploring-cutting-edge-models/tree/main/src/02.ONNXRuntime/01.WebGPUChatRAG)

**免责声明**：  
本文件使用基于人工智能的机器翻译服务进行翻译。尽管我们努力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原文的母语版本作为权威来源。对于关键信息，建议使用专业人工翻译。因使用此翻译而导致的任何误解或误读，我们概不负责。