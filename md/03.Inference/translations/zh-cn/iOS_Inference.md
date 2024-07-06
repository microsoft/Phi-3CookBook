# **在 iOS 上使用 Phi-3 进行推理**

Phi-3-mini是微软推出的一款新型模型系列，可实现在边缘设备和物联网设备上部署大型语言模型（LLMs）。Phi-3-mini支持在iOS、Android和边缘设备上部署，允许在BYOD（自带设备）环境中部署生成式AI。以下示例基于iOS部署Phi-3-mini。

## **1. 准备工作**


a. macOS 14+

b. Xcode 15+
   
c. iOS SDK 17.x (iPhone 14 A16 或更新)
   
d. 安装 Python 3.10+ (推荐使用 Conda)
   
e. 安装 Python 库 - python-flatbuffers

f. 安装 CMake

### Semantic Kernel 和推理:
Semantic Kernel 是一个应用框架，允许您创建与Azure OpenAI服务、OpenAI模型甚至本地模型兼容的应用程序。通过Semantic Kernel访问本地服务可以轻松地连接到您自建的Phi-3-mini模型服务器。

### 使用 Ollama 或 LlamaEdge 调用量化模型:
许多用户更喜欢使用本地运行的量化模型。[Ollama](https://ollama.com) 和 [LlamaEdge](https://llamaedge.com) 允许个人用户调用不同的量化模型:

**Ollama**
您可以直接运行 ollama run phi3 或者离线配置它。创建一个Modelfile，其中包含指向您的gguf文件的路径。以下是运行Phi-3-mini量化模型的示例代码:

```

FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> {{.Prompt}}<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096

```
**LlamaEdge**
如果您想在云端和边缘设备上同时使用gguf，那么LlamaEdge可以是您的选择。


## **2.为 iOS 编译 ONNX Runtime**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```
 
***注意*** 

  a. 在编译之前，您必须确保Xcode配置正确，并在终端上进行设置。


```bash

sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer 

```
 
  b. ONNX Runtime需要根据不同平台进行编译。对于iOS，您可以基于arm64 / x86_64进行编译。
   
  c.  建议直接使用最新的iOS SDK进行编译。当然，您也可以降低版本以兼容过去的SDK。


## **3.为iOS编译生成式AI的 ONNX Runtime**


 ***注意:*** 因为生成式AI与ONNX Runtime处于预览阶段，请注意其变化。


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


## **4. 在Xcode中创建应用程序**

我选择了 Objective-C 作为应用程序开发语言，因为使用生成式AI与ONNX Runtime C++ API时，Objective-C 具有更好的兼容性。当然，您也可以通过 Swift bridging来完成相关调用。


![xcode](../../../../imgs/03/iOS/xcode.png)


## **5. 将ONNX量化的INT4模型拷贝到应用项目中**

我们需要导入ONNX格式的INT4量化模型，这需要先下载该模型。

![hf](../../../../imgs/03/iOS/hf.png)

下载后，您需要将其添加到Xcode项目的Resources目录中。

![model](../../../../imgs/03/iOS/model.png)


 ## **6. 在ViewControllers中添加C++ API**
 
***注意***:

  a. 为项目添加相应的C++头文件


  ![head](../../../../imgs/03/iOS/head.png)

  b. 在Xcode中添加onnxruntime生成的AI动态库

  
  ![lib](../../../../imgs/03/iOS/lib.png)
 
  c. 可以直接在此示例中使用C代码进行测试。您还可以直接添加 moretorun 来运行（例如ChatUI）

  d. 因为需要调用C++，请将 ViewController.m 更改为 ViewController.mm

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


## **7. 运行结果**

![result](../../../../imgs/03/iOS/result.jpg)

***示例代码：*** https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios