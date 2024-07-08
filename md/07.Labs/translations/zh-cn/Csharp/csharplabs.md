##  欢迎来到使用 C# 的 Phi-3 Lab。

这里提供了一系列 Lab，展示了如何在.NET环境中集成强大的不同版本的Phi-3模型。

## 先决条件

在运行示例之前，请确保你已安装以下内容：

**.NET 8:** 确保你已经在你的机器上安装了[最新版本的.NET](https://dotnet.microsoft.com/download/dotnet/8.0)。

**（可选）Visual Studio或Visual Studio Code:** 你将需要一个能够运行.NET项目的IDE或代码编辑器。推荐使用[Visual Studio](https://visualstudio.microsoft.com/)或[Visual Studio Code](https://code.visualstudio.com/)。

**使用git** 从[Hugging Face](https://huggingface.co)本地克隆一个可用的Phi-3版本。

**下载 phi3-mini-4k-instruct-onnx 模型**

### 导航到存储模型的文件夹
```bash
cd c:\phi3\models
```
### 添加lfs支持
```bash
git lfs install 
```
### 克隆并下载 mini 4K instruct 模型
```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx
```

### 克隆并下载 vision 128K 模型
```bash
git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```
**重要:** 目前的演示是为使用 ONNX 版本的模型而设计的。前面的步骤克隆了以下模型。

![OnnxDownload](../../../imgs/07/00/DownloadOnnx.png)

## 关于实验室

主解决方案包含几个示例实验室，展示了使用C#的Phi-3模型的功能。

| 项目 | 描述 | 位置 |
| ------------ | ----------- | -------- |
| LabsPhi301    | 使用本地phi3模型并提问。该项目使用`Microsoft.ML.OnnxRuntime`库加载本地ONNX Phi-3模型。 | .\src\LabsPhi301\ |
| LabsPhi302    | 使用语义内核实现命令行聊天。 | .\src\LabsPhi302\ |
| LabsPhi303 | 使用本地phi3 Vision模型分析图像。该项目使用`Microsoft.ML.OnnxRuntime`库加载本地ONNX Phi-3 Vision模型。 | .\src\LabsPhi303\ |
| LabsPhi304 | 使用本地phi3 Vision模型分析图像。该项目使用`Microsoft.ML.OnnxRuntime`库加载本地ONNX Phi-3 Vision模型。项目还提供了一个菜单，用户可以选择不同的选项进行交互。 | .\src\LabsPhi304\ |
| LabsPhi305 | 使用托管在ollama模型中的Phi-3来回答问题。 |**即将推出**|
| LabsPhi306 | 使用Semantic Kernel实现命令行聊天。 |**即将推出**|
| LabsPhi307  | 使用本地嵌入和Semantic Kernel实现RAG。 |**即将推出**|

## 如何运行项目

要运行这些项目，请按以下步骤操作：
1. 将仓库克隆到你的本地机器。

2. 打开终端并导航到所需的项目。例如，让我们运行`LabsPhi301`。
    ```bash
    cd .\src\LabsPhi301\
    ```

3. 使用以下命令运行项目
    ```bash
    dotnet run
    ```

4. 示例项目会请求用户输入并使用本地模型进行回复。

    运行中的演示类似于这个：

    ![Chat running demo](../../../imgs/07/00/SampleConsole.gif)

    ***注意:** 第一个问题有一个拼写错误，Phi-3足够聪明，可以回答正确的答案！*

5. 项目`LabsPhi304`会请求用户选择不同的选项，然后处理请求。例如，分析本地图像。

    运行中的演示类似于这个：

    ![Image Analysis running demo](../../../imgs/07/00/SampleVisionConsole.gif)