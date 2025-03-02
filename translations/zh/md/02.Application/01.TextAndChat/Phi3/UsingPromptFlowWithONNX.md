# 使用 Windows GPU 创建基于 Phi-3.5-Instruct ONNX 的 Prompt Flow 解决方案

本文档是一个示例，展示如何使用 PromptFlow 和 ONNX（开放神经网络交换格式）开发基于 Phi-3 模型的 AI 应用程序。

PromptFlow 是一套开发工具，旨在简化基于 LLM（大型语言模型）的 AI 应用程序从构思、原型设计到测试和评估的全周期开发流程。

通过将 PromptFlow 与 ONNX 集成，开发者可以：

- **优化模型性能**：利用 ONNX 实现高效的模型推理和部署。
- **简化开发流程**：使用 PromptFlow 管理工作流并自动化重复任务。
- **增强协作能力**：通过提供统一的开发环境，促进团队成员之间的协作。

**Prompt flow** 是一套开发工具，旨在简化基于 LLM 的 AI 应用程序从构思、原型设计、测试、评估到生产部署和监控的端到端开发流程。它让提示工程更加简单，并使您能够构建具有生产质量的 LLM 应用程序。

Prompt flow 可以连接到 OpenAI、Azure OpenAI 服务以及可定制的模型（如 Huggingface、本地 LLM/SLM）。我们希望将 Phi-3.5 的量化 ONNX 模型部署到本地应用中。Prompt flow 可以帮助我们更好地规划业务并完成基于 Phi-3.5 的本地解决方案。在本示例中，我们将结合 ONNX Runtime GenAI Library 来完成基于 Windows GPU 的 Prompt flow 解决方案。

## **安装步骤**

### **Windows GPU 的 ONNX Runtime GenAI**

请阅读此指南以设置 Windows GPU 的 ONNX Runtime GenAI：[点击这里](./ORTWindowGPUGuideline.md)

### **在 VSCode 中设置 Prompt flow**

1. 安装 Prompt flow 的 VS Code 扩展

![pfvscode](../../../../../../translated_images/pfvscode.79f42ae5dd93ed35c19d6d978ae75831fef40e0b8440ee48b893b5a0597d2260.zh.png)

2. 安装 Prompt flow 的 VS Code 扩展后，点击扩展，并选择 **安装依赖项**，按照指南在您的环境中安装 Prompt flow SDK

![pfsetup](../../../../../../translated_images/pfsetup.0c82d99c7760aac29833b37faf4329e67e22279b1c5f37a73724dfa9ebaa32ee.zh.png)

3. 下载 [示例代码](../../../../../../code/09.UpdateSamples/Aug/pf/onnx_inference_pf)，并使用 VS Code 打开该示例

![pfsample](../../../../../../translated_images/pfsample.7bf40b133a558d86356dd6bc0e480bad2659d9c5364823dae9b3e6784e6f2d25.zh.png)

4. 打开 **flow.dag.yaml**，选择您的 Python 环境

![pfdag](../../../../../../translated_images/pfdag.c5eb356fa3a96178cd594de9a5da921c4bbe646a9946f32aa20d344ccbeb51a0.zh.png)

   打开 **chat_phi3_ort.py**，更改您的 Phi-3.5-instruct ONNX 模型位置

![pfphi](../../../../../../translated_images/pfphi.fff4b0afea47c92c8481174dbf3092823906fca5b717fc642f78947c3e5bbb39.zh.png)

5. 运行您的 Prompt flow 进行测试

打开 **flow.dag.yaml**，点击可视化编辑器

![pfv](../../../../../../translated_images/pfv.7af6ecd65784a98558b344ba69b5ba6233876823fb435f163e916a632394fc1e.zh.png)

点击后运行以测试

![pfflow](../../../../../../translated_images/pfflow.9697e0fda67794bb0cf4b78d52e6f5a42002eec935bc2519933064afbbdd34f0.zh.png)

6. 您可以在终端中运行批处理以查看更多结果

```bash

pf run create --file batch_run.yaml --stream --name 'Your eval qa name'    

```

您可以在默认浏览器中查看结果

![pfresult](../../../../../../translated_images/pfresult.972eb57dd5bec646e1aa01148991ba8959897efea396e42cf9d7df259444878d.zh.png)

**免责声明**：  
本文件使用基于机器的人工智能翻译服务进行翻译。尽管我们尽力确保准确性，但请注意，自动翻译可能包含错误或不准确之处。应以原始语言的文件为权威来源。对于关键信息，建议使用专业人工翻译。我们对因使用本翻译而引起的任何误解或误读不承担责任。