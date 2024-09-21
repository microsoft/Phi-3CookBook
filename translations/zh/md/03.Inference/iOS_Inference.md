# **在 iOS 上进行 Phi-3 推理**

Phi-3-mini 是微软推出的新系列模型，支持在边缘设备和物联网设备上部署大语言模型（LLMs）。Phi-3-mini 可用于 iOS、Android 和边缘设备的部署，使生成式 AI 可以在自带设备（BYOD）环境中部署。以下示例展示了如何在 iOS 上部署 Phi-3-mini。

## **1. 准备工作**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x（iPhone 14 A16 或更高版本）
- **d.** 安装 Python 3.10+（推荐使用 Conda）
- **e.** 安装 Python 库：`python-flatbuffers`
- **f.** 安装 CMake

### Semantic Kernel 和推理

Semantic Kernel 是一个应用框架，允许你创建兼容 Azure OpenAI 服务、OpenAI 模型甚至本地模型的应用程序。通过 Semantic Kernel 访问本地服务，可以轻松集成你自托管的 Phi-3-mini 模型服务器。

### 使用 Ollama 或 LlamaEdge 调用量化模型

许多用户更喜欢使用量化模型在本地运行模型。[Ollama](https://ollama.com) 和 [LlamaEdge](https://llamaedge.com) 允许用户调用不同的量化模型：

#### **Ollama**

你可以直接运行 `ollama run phi3` 或者离线配置。创建一个包含 `gguf` 文件路径的 Modelfile。运行 Phi-3-mini 量化模型的示例代码：

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> {{.Prompt}}<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

如果你想在云端和边缘设备上同时使用 `gguf`，LlamaEdge 是一个不错的选择。

## **2. 编译适用于 iOS 的 ONNX Runtime**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **注意事项**

- **a.** 在编译之前，确保 Xcode 已正确配置，并在终端中将其设置为活动开发者目录：

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** 需要为不同平台编译 ONNX Runtime。对于 iOS，可以为 `arm64` 或 `x86_64` 编译。

- **c.** 建议使用最新的 iOS SDK 进行编译。不过，如果需要兼容以前的 SDK，也可以使用较旧的版本。

## **3. 编译适用于 iOS 的 ONNX Runtime 生成式 AI**

> **注意:** 由于使用 ONNX Runtime 的生成式 AI 处于预览阶段，请注意可能的变化。

```bash

git clone https://github.com/microsoft/onnxruntime-genai
 
cd onnxruntime-genai
 
mkdir ort
 
cd ort
 
mkdir include
 
mkdir lib
 
cd ../
 
cp ../onnxruntime/include/onnxruntime/core/session/onnxruntime_c_api.h ort/include
 
cp ../onnxruntime/build_ios/Release/Release-iphoneos/libonnxruntime*.dylib* ort/lib
 
export OPENCV_SKIP_XCODEBUILD_FORCE_TRYCOMPILE_DEBUG=1
 
python3 build.py --parallel --build_dir ./build_ios --ios --ios_sysroot iphoneos --ios_arch arm64 --ios_deployment_target 17.5 --cmake_generator Xcode --cmake_extra_defines CMAKE_XCODE_ATTRIBUTE_CODE_SIGNING_ALLOWED=NO

```

## **4. 在 Xcode 中创建一个 App 应用程序**

我选择了 Objective-C 作为 App 开发方法，因为使用 ONNX Runtime C++ API 的生成式 AI 时，Objective-C 兼容性更好。当然，你也可以通过 Swift 桥接完成相关调用。

![xcode](../../../../translated_images/xcode.2817f1d089dc7d09ba6a41361db7052567d63f714062e2e4325b0e0895ccb4c4.zh.png)

## **5. 将 ONNX 量化的 INT4 模型复制到 App 应用程序项目中**

我们需要导入 ONNX 格式的 INT4 量化模型，首先需要下载它。

![hf](../../../../translated_images/hf.dd843c3e95f3b462a3d5f06dbbb17c1f1a33b87688c1cda4d990084ef71a4eed.zh.png)

下载后，需要将其添加到 Xcode 项目的 Resources 目录中。

![model](../../../../translated_images/model.2b8e95a590e70374b2294b16f8ae18c9110239a550e64dc034d6bc16d37e0106.zh.png)

## **6. 在 ViewControllers 中添加 C++ API**

> **注意:**

- **a.** 将相应的 C++ 头文件添加到项目中。

  ![Header File](../../../../translated_images/head.7eeb79e1de8f375590e7a5c54fcc8278d265fee3135ebce9c8e241e08d823f7c.zh.png)

- **b.** 在 Xcode 中包含 `onnxruntime-genai` 动态库。

  ![Library](../../../../translated_images/lib.9388329df08543518d094d14c8ca0c8e6f0ce264ee68630a8c5c3d783355b6d1.zh.png)

- **c.** 使用 C 示例代码进行测试。你还可以添加 ChatUI 等额外功能以增加功能性。

- **d.** 由于在项目中需要使用 C++，将 `ViewController.m` 重命名为 `ViewController.mm` 以启用 Objective-C++ 支持。

```objc

    NSString *llmPath = [[NSBundle mainBundle] resourcePath];
    char const *modelPath = llmPath.cString;

    auto model =  OgaModel::Create(modelPath);

    auto tokenizer = OgaTokenizer::Create(*model);

    const char* prompt = "<|system|>You are a helpful AI assistant.<|end|><|user|>Can you introduce yourself?<|end|><|assistant|>";

    auto sequences = OgaSequences::Create();
    tokenizer->Encode(prompt, *sequences);

    auto params = OgaGeneratorParams::Create(*model);
    params->SetSearchOption("max_length", 100);
    params->SetInputSequences(*sequences);

    auto output_sequences = model->Generate(*params);
    const auto output_sequence_length = output_sequences->SequenceCount(0);
    const auto* output_sequence_data = output_sequences->SequenceData(0);
    auto out_string = tokenizer->Decode(output_sequence_data, output_sequence_length);
    
    auto tmp = out_string;

```

## **7. 运行应用程序**

设置完成后，你可以运行应用程序查看 Phi-3-mini 模型推理的结果。

![Running Result](../../../../translated_images/result.a2debbd16a6697a8cbd23dadff703358ea87eee7d68f0643b83707a578ca73e8.zh.jpg)

有关更多示例代码和详细说明，请访问 [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios)。

免责声明：此翻译由AI模型从原文翻译而来，可能不够完美。请审核输出内容并进行必要的修改。