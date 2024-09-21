# **在 iOS 上推理 Phi-3**

Phi-3-mini 是 Microsoft 推出的新系列模型，能夠在邊緣設備和物聯網設備上部署大型語言模型 (LLMs)。Phi-3-mini 可用於 iOS、Android 和邊緣設備的部署，允許在 BYOD 環境中部署生成式 AI。以下範例展示如何在 iOS 上部署 Phi-3-mini。

## **1. 準備工作**

- **a.** macOS 14+
- **b.** Xcode 15+
- **c.** iOS SDK 17.x (iPhone 14 A16 或更高版本)
- **d.** 安裝 Python 3.10+ (推薦使用 Conda)
- **e.** 安裝 Python 庫: `python-flatbuffers`
- **f.** 安裝 CMake

### Semantic Kernel 和推理

Semantic Kernel 是一個應用框架，允許您創建與 Azure OpenAI Service、OpenAI 模型甚至本地模型兼容的應用。通過 Semantic Kernel 訪問本地服務，可以輕鬆整合自托管的 Phi-3-mini 模型服務器。

### 使用 Ollama 或 LlamaEdge 調用量化模型

許多用戶喜歡使用量化模型來本地運行模型。[Ollama](https://ollama.com) 和 [LlamaEdge](https://llamaedge.com) 允許用戶調用不同的量化模型：

#### **Ollama**

您可以直接運行 `ollama run phi3` 或離線配置。創建一個 Modelfile，並將路徑指向您的 `gguf` 文件。運行 Phi-3-mini 量化模型的示例代碼：

```gguf
FROM {Add your gguf file path}
TEMPLATE \"\"\"<|user|> .Prompt<|end|> <|assistant|>\"\"\"
PARAMETER stop <|end|>
PARAMETER num_ctx 4096
```

#### **LlamaEdge**

如果您希望在雲端和邊緣設備同時使用 `gguf`，LlamaEdge 是一個很好的選擇。

## **2. 為 iOS 編譯 ONNX Runtime**

```bash

git clone https://github.com/microsoft/onnxruntime.git

cd onnxruntime

./build.sh --build_shared_lib --ios --skip_tests --parallel --build_dir ./build_ios --ios --apple_sysroot iphoneos --osx_arch arm64 --apple_deploy_target 17.5 --cmake_generator Xcode --config Release

cd ../

```

### **注意事項**

- **a.** 在編譯之前，請確保 Xcode 已正確配置，並在終端中設置為活動開發者目錄：

    ```bash
    sudo xcode-select -switch /Applications/Xcode.app/Contents/Developer
    ```

- **b.** ONNX Runtime 需要為不同平台編譯。對於 iOS，您可以編譯 `arm64` 或 `x86_64`。

- **c.** 建議使用最新的 iOS SDK 進行編譯。不過，如果您需要與以前的 SDK 兼容，也可以使用較舊版本。

## **3. 使用 ONNX Runtime 編譯生成式 AI 以適應 iOS**

> **Note:** 因為使用 ONNX Runtime 的生成式 AI 還在預覽階段，請注意可能的變更。

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

## **4. 在 Xcode 中創建一個 App 應用**

我選擇使用 Objective-C 作為 App 的開發方式，因為使用 ONNX Runtime C++ API 的生成式 AI 時，Objective-C 兼容性更好。當然，您也可以通過 Swift 橋接完成相關調用。

![xcode](../../../../translated_images/xcode.2817f1d089dc7d09ba6a41361db7052567d63f714062e2e4325b0e0895ccb4c4.tw.png)

## **5. 將 ONNX 量化的 INT4 模型複製到 App 應用項目中**

我們需要導入 ONNX 格式的 INT4 量化模型，這需要先下載

![hf](../../../../translated_images/hf.dd843c3e95f3b462a3d5f06dbbb17c1f1a33b87688c1cda4d990084ef71a4eed.tw.png)

下載後，您需要將其添加到 Xcode 中項目的 Resources 目錄中。

![model](../../../../translated_images/model.2b8e95a590e70374b2294b16f8ae18c9110239a550e64dc034d6bc16d37e0106.tw.png)

## **6. 在 ViewControllers 中添加 C++ API**

> **注意:**

- **a.** 將相應的 C++ 頭文件添加到項目中。

  ![Header File](../../../../translated_images/head.7eeb79e1de8f375590e7a5c54fcc8278d265fee3135ebce9c8e241e08d823f7c.tw.png)

- **b.** 在 Xcode 中包含 `onnxruntime-genai` 動態庫。

  ![Library](../../../../translated_images/lib.9388329df08543518d094d14c8ca0c8e6f0ce264ee68630a8c5c3d783355b6d1.tw.png)

- **c.** 使用 C 範例代碼進行測試。您還可以添加更多功能，如 ChatUI。

- **d.** 由於您需要在項目中使用 C++，請將 `ViewController.m` 重命名為 `ViewController.mm` 以啟用 Objective-C++ 支持。

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

## **7. 運行應用**

完成設置後，您可以運行應用以查看 Phi-3-mini 模型推理的結果。

![Running Result](../../../../translated_images/result.a2debbd16a6697a8cbd23dadff703358ea87eee7d68f0643b83707a578ca73e8.tw.jpg)

有關更多範例代碼和詳細說明，請訪問 [Phi-3 Mini Samples repository](https://github.com/Azure-Samples/Phi-3MiniSamples/tree/main/ios)。

免責聲明：此翻譯由AI模型從原文翻譯而來，可能不完美。請審核輸出並進行必要的修正。