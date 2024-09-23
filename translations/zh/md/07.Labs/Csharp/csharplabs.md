## 欢迎使用 C# 进行 Phi-3 实验室

这里有一系列实验室，展示了如何在 .NET 环境中集成强大的不同版本的 Phi-3 模型。

## 前置条件
在运行示例之前，请确保已安装以下内容：

**.NET 8:** 请确保你的机器上安装了[最新版本的 .NET](https://dotnet.microsoft.com/download/dotnet/8.0?WT.mc_id=aiml-137032-kinfeylo)。

**（可选）Visual Studio 或 Visual Studio Code:** 你需要一个能够运行 .NET 项目的 IDE 或代码编辑器。推荐使用 [Visual Studio](https://visualstudio.microsoft.com/) 或 [Visual Studio Code](https://code.visualstudio.com?WT.mc_id=aiml-137032-kinfeylo)。

**使用 git** 从 [Hugging Face](https://huggingface.co) 本地克隆其中一个可用的 Phi-3 版本。

**下载 phi3-mini-4k-instruct-onnx 模型**到你的本地机器：

### 导航到存储模型的文件夹
```bash
cd c:\phi3\models
```
### 添加 lfs 支持
```bash
git lfs install 
```
### 克隆并下载 mini 4K instruct 模型
```bash
git clone https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-onnx
```

### 克隆并下载 vision 128K 模型
```
git clone https://huggingface.co/microsoft/Phi-3-vision-128k-instruct-onnx-cpu
```
**重要:** 当前的演示设计用于使用模型的 ONNX 版本。前面的步骤克隆了以下模型。

![OnnxDownload](../../../../../translated_images/DownloadOnnx.237f4b37d4d8d66d3f4a4a7219d6004bd6f84bc72cce50251ffc034cb28f6fb8.zh.png)

## 关于实验室

主解决方案包含几个示例实验室，展示了使用 C# 的 Phi-3 模型的功能。

| 项目 | 描述 | 位置 |
| ------------ | ----------- | -------- |
| LabsPhi301    | 这是一个使用本地 phi3 模型提问的示例项目。项目使用 `Microsoft.ML.OnnxRuntime` 库加载本地 ONNX Phi-3 模型。 | .\src\LabsPhi301\ |
| LabsPhi302    | 这是一个使用 Semantic Kernel 实现控制台聊天的示例项目。 | .\src\LabsPhi302\ |
| LabsPhi303 | 这是一个使用本地 phi3 视觉模型分析图像的示例项目。项目使用 `Microsoft.ML.OnnxRuntime` 库加载本地 ONNX Phi-3 视觉模型。 | .\src\LabsPhi303\ |
| LabsPhi304 | 这是一个使用本地 phi3 视觉模型分析图像的示例项目。项目使用 `Microsoft.ML.OnnxRuntime` 库加载本地 ONNX Phi-3 视觉模型。项目还提供了一个菜单，用户可以选择不同的选项进行交互。 | .\src\LabsPhi304\ |
| LabsPhi305 | 这是一个使用托管在 ollama 模型中的 Phi-3 回答问题的示例项目。  |**即将推出**|
| LabsPhi306 | 这是一个使用 Semantic Kernel 实现控制台聊天的示例项目。 |**即将推出**|
| LabsPhi307  | 这是一个使用本地嵌入和 Semantic Kernel 实现 RAG 的示例项目。 |**即将推出**|

## 如何运行项目

要运行项目，请按照以下步骤操作：
1. 将仓库克隆到你的本地机器。

1. 打开终端并导航到所需的项目。例如，我们运行 `LabsPhi301`。
    ```bash
    cd .\src\LabsPhi301\
    ```

1. 使用以下命令运行项目
    ```bash
    dotnet run
    ```

1.  示例项目会请求用户输入，并使用本地模式回复。

    运行中的演示类似于这样：

    ![Chat running demo](../../../../../imgs/07/00/SampleConsole.gif)

    ***注意:** 第一个问题中有一个拼写错误，Phi-3 足够聪明地给出了正确答案！*

1.  项目 `LabsPhi304` 要求用户选择不同的选项，然后处理请求。例如，分析本地图像。

    运行中的演示类似于这样：

    ![Image Analysis running demo](../../../../../imgs/07/00/SampleVisionConsole.gif)

